#!/usr/bin/env python3
"""Reproduce the pinned-JR DC and linear-response calculations.

Run from any directory with NumPy and SciPy installed. The script reads the
repository's jr_jsweep_engine.py and writes check_jr_dc_response.json beside
itself. Calculations use equilibria, Jacobians and linear transfer functions;
there are no time-domain simulations and no changes to the engine.
"""

from pathlib import Path
import hashlib
import importlib.util
import json

import numpy as np
from scipy.optimize import brentq, minimize_scalar


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
ENGINE_PATH = ROOT / "code" / "jr_jsweep_engine.py"
SPEC = importlib.util.spec_from_file_location("jr_jsweep_engine", ENGINE_PATH)
ENGINE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(ENGINE)

V_STAR = 8.30  # mV, field-free sigmoid argument and synaptic voltage
EPSILON = 0.2  # mV at the pyramidal sigmoid entry
KA, KB = ENGINE.A / ENGINE.a, ENGINE.B / ENGINE.b


def sigmoid_derivative(u):
    rate = ENGINE.Sigm(u)
    return ENGINE.rr * rate * (1.0 - rate / (2.0 * ENGINE.e0))


def synaptic_voltage(u, coupling, background):
    y0 = KA * ENGINE.Sigm(u)
    y1 = KA * (background + 0.8 * coupling * ENGINE.Sigm(coupling * y0))
    y2 = KB * 0.25 * coupling * ENGINE.Sigm(0.25 * coupling * y0)
    return y1 - y2


def equilibrium_argument(epsilon, coupling, background):
    # Continue the equilibrium near the pinned state, not an arbitrary root.
    return brentq(
        lambda u: synaptic_voltage(u, coupling, background) + epsilon - u,
        V_STAR - 1.0,
        V_STAR + 1.0,
        xtol=1e-13,
    )


def jacobian(coupling, u):
    """Exact six-state Jacobian with constant imposed polarization."""
    y0 = KA * ENGINE.Sigm(u)
    a, b, A, B = ENGINE.a, ENGINE.b, ENGINE.A, ENGINE.B
    matrix = np.zeros((6, 6))
    matrix[:3, 3:] = np.eye(3)
    matrix[3] = [-a * a, A * a * sigmoid_derivative(u),
                 -A * a * sigmoid_derivative(u), -2 * a, 0, 0]
    matrix[4] = [A * a * 0.8 * coupling**2
                 * sigmoid_derivative(coupling * y0),
                 -a * a, 0, 0, -2 * a, 0]
    matrix[5] = [B * b * 0.0625 * coupling**2
                 * sigmoid_derivative(0.25 * coupling * y0),
                 0, -b * b, 0, 0, -2 * b]
    return matrix


def leading_mode(coupling, u):
    eigenvalues = np.linalg.eigvals(jacobian(coupling, u))
    return eigenvalues[np.argmax(eigenvalues.real)]


def return_transfer(frequency_hz, coupling):
    """Dimensionless loop factor at the pinned field-free state."""
    omega = 2 * np.pi * frequency_hz
    ha = ENGINE.A * ENGINE.a / (ENGINE.a + 1j * omega)**2
    hb = ENGINE.B * ENGINE.b / (ENGINE.b + 1j * omega)**2
    y0 = KA * ENGINE.Sigm(V_STAR)
    return sigmoid_derivative(V_STAR) * ha * (
        0.8 * coupling**2 * sigmoid_derivative(coupling * y0) * ha
        - 0.0625 * coupling**2 * sigmoid_derivative(0.25 * coupling * y0) * hb
    )


def response_gains(frequency_hz, coupling):
    loop = return_transfer(frequency_hz, coupling)
    total = 1 / (1 - loop)
    return np.array([loop * total, total, sigmoid_derivative(V_STAR) * total])


def finite_dc_result(epsilon, coupling, background):
    u = equilibrium_argument(epsilon, coupling, background)
    rate = ENGINE.Sigm(u)
    base_rate = ENGINE.Sigm(V_STAR)
    y0 = KA * rate
    y1 = KA * (background + 0.8 * coupling * ENGINE.Sigm(coupling * y0))
    y2 = KB * 0.25 * coupling * ENGINE.Sigm(0.25 * coupling * y0)
    state = np.array([[y0, y1, y2, 0.0, 0.0, 0.0]])
    residual = ENGINE.rhs(state, np.array([background]),
                          np.array([coupling]), np.array([epsilon]))[0]
    assert np.max(np.abs(residual)) < 1e-6
    mode = leading_mode(coupling, u)
    return {
        "epsilon_mV": epsilon,
        "sigmoid_argument_mV": u,
        "synaptic_voltage_mV": y1 - y2,
        "delta_argument_mV": u - V_STAR,
        "delta_synaptic_voltage_mV": y1 - y2 - V_STAR,
        "delta_rate_s_inv": rate - base_rate,
        "rate_percent_change": 100 * (rate - base_rate) / base_rate,
        "damping_s_inv": -mode.real,
        "mode_frequency_Hz": abs(mode.imag) / (2 * np.pi),
        "maximum_engine_rhs_residual": np.max(np.abs(residual)),
    }


def coupling_result(coupling):
    background = ENGINE.p_of_C(V_STAR, coupling)
    loop = return_transfer(0.0, coupling).real
    dc_gains = response_gains(0.0, coupling).real
    mode = leading_mode(coupling, V_STAR)

    # Check the scalar DC transfer against the full six-state Jacobian.
    input_vector = np.array([0, 0, 0,
                             ENGINE.A * ENGINE.a * sigmoid_derivative(V_STAR), 0, 0])
    voltage_readout = np.array([0, 1, -1, 0, 0, 0])
    full_dc = voltage_readout @ np.linalg.solve(-jacobian(coupling, V_STAR),
                                               input_vector)
    assert np.isclose(full_dc, dc_gains[0], rtol=1e-12, atol=1e-12)

    frequencies = np.linspace(0, 40, 8001)
    amplitudes = np.abs(response_gains(frequencies, coupling)[0])
    peak_index = np.argmax(amplitudes)
    assert 0 < peak_index < len(frequencies) - 1
    peak = minimize_scalar(
        lambda f: -abs(response_gains(f, coupling)[0]),
        bounds=(frequencies[peak_index - 1], frequencies[peak_index + 1]),
        method="bounded",
    )
    assert peak.success
    peak_gains = np.abs(response_gains(peak.x, coupling))
    original_v, original_gamma, _, _ = ENGINE.jac_eig(background, coupling)
    assert abs(original_v - V_STAR) < 1e-10
    assert abs(original_gamma + mode.real) < 2e-6
    return {
        "C": coupling,
        "background_p_s_inv": background,
        "dc_loop_factor": loop,
        "dc_gains_v_u_r": dc_gains.tolist(),
        "dc_linear_shifts_at_plus_0p2mV_v_u_r": (EPSILON * dc_gains).tolist(),
        "dc_gain_from_full_jacobian": full_dc,
        "field_free_damping_s_inv": -mode.real,
        "field_free_mode_frequency_Hz": abs(mode.imag) / (2 * np.pi),
        "engine_finite_difference_damping_difference_s_inv": original_gamma + mode.real,
        "voltage_peak_frequency_Hz": peak.x,
        "infinitesimal_peak_gains_abs_v_u_r": peak_gains.tolist(),
        "finite_dc": [finite_dc_result(eps, coupling, background)
                      for eps in [-EPSILON, EPSILON]],
    }


def main():
    rate = ENGINE.Sigm(V_STAR)
    ch = brentq(lambda c: leading_mode(c, V_STAR).real, 136.3, 137.0)
    ch_mode = leading_mode(ch, V_STAR)
    assert abs(ch_mode.imag) > 1.0
    dc_c = 136.3
    background = ENGINE.p_of_C(V_STAR, dc_c)
    epsilon_h = brentq(
        lambda eps: leading_mode(dc_c, equilibrium_argument(eps, dc_c, background)).real,
        -0.3, 0.0,
    )
    dc_crossing = finite_dc_result(epsilon_h, dc_c, background)
    assert dc_crossing["mode_frequency_Hz"] > 1.0
    data = {
        "calculation": "Equilibria, Jacobians and linear transfer functions only; no time simulations.",
        "engine": str(ENGINE_PATH.relative_to(ROOT)),
        "engine_sha256": hashlib.sha256(ENGINE_PATH.read_bytes()).hexdigest(),
        "gain_order": ["synaptic_voltage_v", "total_sigmoid_argument_u", "pyramidal_rate_r"],
        "gain_units": ["mV/mV", "mV/mV", "s^-1/mV"],
        "peak_definition": "Maximum of infinitesimal |v/epsilon| over 0-40 Hz; u and r evaluated at the same frequency.",
        "parameters": {key: float(getattr(ENGINE, key)) for key in ["A", "B", "a", "b", "v0", "e0", "rr"]},
        "field_free_sigmoid": {
            "argument_mV": V_STAR, "rate_s_inv": rate,
            "slope_s_inv_per_mV": sigmoid_derivative(V_STAR),
            "curvature_s_inv_per_mV_squared": ENGINE.Sigm2(V_STAR),
            "plus_0p2mV_local_rate_delta_s_inv": ENGINE.Sigm(V_STAR + EPSILON) - rate,
            "minus_0p2mV_local_rate_delta_s_inv": ENGINE.Sigm(V_STAR - EPSILON) - rate,
            "plus_0p2mV_local_percent": 100 * (ENGINE.Sigm(V_STAR + EPSILON) - rate) / rate,
        },
        "couplings": [coupling_result(c) for c in [110.0, 130.0, 136.3]],
        "pinned_coupling_crossing": {
            "C_H": ch, "frequency_Hz": abs(ch_mode.imag) / (2 * np.pi),
            "dc_loop_factor": return_transfer(0.0, ch).real,
            "dc_total_argument_gain": response_gains(0.0, ch)[1].real,
        },
        "dc_induced_complex_pair_crossing_at_C136p3": dc_crossing,
        "crossing_scope": "Equilibrium stability crossing only; no attractor or Hopf criticality calculation.",
    }
    output = HERE / "check_jr_dc_response.json"
    output.write_text(json.dumps(data, indent=2) + "\n")
    print(output)
    print("All equilibrium and Jacobian consistency checks passed.")


if __name__ == "__main__":
    main()
