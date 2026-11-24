"""Shorter membrane time scales in the uncoupled QIF/MPR population.

Run from the repository root:
    .venv/bin/python code/qif_short_tau_check.py

Writes docs/qif_short_tau_2026-10-02.json. The manuscript and its figures are
unchanged. Time is in seconds for the uncoupled calculation. The imported PING
check retains that module's millisecond convention.

The physical-rate equations are
    tau*r_dot = Delta/(pi*tau) + 2*r*v
    tau*v_dot = v*v + Q - (pi*tau*r)**2 + a1*cos(w1*t) + a2*cos(w2*t).
We integrate rho=tau*r, so both state equations have the same tau prefactor.
The input amplitudes are held fixed in this dimensionless current convention;
no conversion from applied electric field is assumed or calibrated here.

Two comparisons are kept separate:
* fixed_parameters: Q=0, Delta=1, hence physical baseline rate grows as 1/tau;
* matched_rate_voltage: preserve the 15-ms population's rate and voltage by
  setting Delta=s*Delta0 and Q=s*s*(Q0+v0*v0)-v0*v0, s=tau/tau0.
The latter is a controlled parameter comparison, not a fitted biological model.
"""

import json
from pathlib import Path

import numpy as np
from scipy.integrate import solve_ivp

import ping_fast_carrier_check as ping


TAU0 = 0.015
RHO0 = 1.0 / (np.pi * np.sqrt(2.0))
V0 = -1.0 / np.sqrt(2.0)
R0 = RHO0 / TAU0
F1, F2 = 980.0, 1020.0
OMEGA = 2 * np.pi * (F2 - F1)
TAUS_MS = (15.0, 1.5, 1.0, 0.2, 0.15)
OUTPUT = Path(__file__).resolve().parents[1] / "docs/qif_short_tau_2026-10-02.json"


def state(tau, protocol):
    if protocol == "fixed_parameters":
        return np.array([RHO0, V0]), 0.0, 1.0
    if protocol == "matched_rate_voltage":
        scale = tau / TAU0
        return np.array([tau * R0, V0]), 0.5 * (scale**2 - 1), scale
    raise ValueError(protocol)


def quadratic(a, b):
    """Hessian of the undivided (rho,v) equations, applied to two vectors."""
    return np.array([
        2 * (a[0] * b[1] + a[1] * b[0]),
        2 * a[1] * b[1] - 2 * np.pi**2 * a[0] * b[0],
    ])


def response(tau, protocol):
    x, q, delta = state(tau, protocol)
    rho, v = x
    jac = np.array([[2 * v, 2 * rho], [-2 * np.pi**2 * rho, 2 * v]]) / tau
    drive = np.array([0.0, 1.0]) / tau

    def first_order(f):
        return np.linalg.solve(2j * np.pi * f * np.eye(2) - jac, drive)

    h1, h2 = first_order(F1), first_order(F2)
    source = 0.5 * quadratic(h2, h1.conj()) / tau
    beat = np.linalg.solve(1j * OMEGA * np.eye(2) - jac, source)[0] / tau
    return {
        "tau_ms": tau * 1000,
        "protocol": protocol,
        "Q": q,
        "Delta": delta,
        "r_baseline_Hz": rho / tau,
        "v_baseline": v,
        "voltage_carrier_1000Hz_per_a": abs(first_order(1000)[1]),
        "v_squared_beat_source_per_a1a2": abs(h2[1] * h1[1].conj()),
        "rate_beat_Hz_per_a1a2": abs(beat),
        "rate_beat_complex_Hz_per_a1a2": [beat.real, beat.imag],
        "intrinsic_eigenvalues_per_second": [
            [z.real, z.imag] for z in np.linalg.eigvals(jac)
        ],
    }


def integrated_beat(tau, amplitude):
    """Independent finite-amplitude time integration, matched-rate comparison."""
    x0, q, delta = state(tau, "matched_rate_voltage")
    settle, duration = 0.4, 0.5
    count = 25000
    times = settle + duration * np.arange(count) / count

    def rhs(t, x):
        rho, v = x
        forcing = amplitude * (np.cos(2 * np.pi * F1 * t) + np.cos(2 * np.pi * F2 * t))
        return np.array([
            delta / np.pi + 2 * rho * v,
            v*v + q - (np.pi * rho)**2 + forcing,
        ]) / tau

    sol = solve_ivp(
        rhs, (0.0, settle + duration), x0, method="DOP853", t_eval=times,
        rtol=2e-12, atol=2e-14, max_step=1 / (F2 * 24),
    )
    if not sol.success:
        raise RuntimeError(sol.message)
    rate_change = (sol.y[0] - x0[0]) / tau
    # The 0.5-s measurement interval contains integer cycles of both carriers
    # and their 40-Hz difference, avoiding linear carrier leakage into the beat.
    return 2 * np.mean(rate_change * np.exp(-1j * OMEGA * times)) / amplitude**2


def ping_fixed_parameter_check():
    """Recompute the existing PING's equilibrium and modes without retuning it."""
    original = ping.TE, ping.TI
    try:
        ping.TE, ping.TI = 15.0, 7.5
        baseline = ping.ping_equilibrium(15.0, 0.0)
        rows = []
        for tau_ms in TAUS_MS:
            scale = tau_ms / 15.0
            ping.TE, ping.TI = tau_ms, tau_ms / 2
            x = baseline.copy()
            # Exact equilibrium scaling when both membrane taus change together
            # and Delta, eta, C, synaptic weights, and synaptic taus are fixed.
            x[[0, 2, 4, 6]] /= scale
            jac = ping.ping_jacobian(x, 15.0)
            eig = np.linalg.eigvals(jac)
            modes = eig[eig.imag > 1e-9]
            mode = modes[np.argmax(modes.real)]
            rows.append({
                "tau_E_ms": tau_ms, "tau_I_ms": tau_ms / 2,
                "r_E_Hz": x[0] * 1000, "r_I_Hz": x[2] * 1000,
                "max_eigenvalue_real_per_ms": max(eig.real),
                "least_damped_oscillatory_mode_Hz": mode.imag * 1000 / (2*np.pi),
                "oscillatory_mode_damping_per_ms": -mode.real,
            })
        return rows
    finally:
        ping.TE, ping.TI = original


def main():
    rows = [response(t / 1000, p) for p in ("fixed_parameters", "matched_rate_voltage") for t in TAUS_MS]
    validation = []
    for tau_ms in (15.0, 1.5, 0.15):
        tau = tau_ms / 1000
        target = response(tau, "matched_rate_voltage")
        expected = complex(*target["rate_beat_complex_Hz_per_a1a2"])
        full, half = integrated_beat(tau, 0.05), integrated_beat(tau, 0.025)
        extrapolated = (4 * half - full) / 3
        error = abs(extrapolated - expected) / abs(expected)
        validation.append({
            "tau_ms": tau_ms, "amplitudes": [0.05, 0.025],
            "coefficient_full": [full.real, full.imag],
            "coefficient_half": [half.real, half.imag],
            "quadratic_limit_relative_error": error,
        })
        print(f"tau={tau_ms:g} ms: time-domain quadratic-limit error {error:.3g}", flush=True)
        if error > 0.002:
            raise AssertionError(f"Time integration disagrees at tau={tau_ms:g} ms")
    payload = {
        "carriers_Hz": [F1, F2], "beat_Hz": F2 - F1,
        "input_convention": "fixed normalized current amplitudes inside tau*v_dot equation",
        "uncoupled": rows, "validation": validation,
        "PING_fixed_parameters": ping_fixed_parameter_check(),
    }
    OUTPUT.write_text(json.dumps(payload, indent=2) + "\n")
    for row in rows:
        print(f"{row['protocol']:22s} tau={row['tau_ms']:5g} ms, r={row['r_baseline_Hz']:8.3f} Hz, "
              f"|Hv|={row['voltage_carrier_1000Hz_per_a']:.6f}, "
              f"v^2 source={row['v_squared_beat_source_per_a1a2']:.8g}")
    print(OUTPUT)


if __name__ == "__main__":
    main()
