"""Audit the Landau numerical integration without changing its input caches.

Reconstruct summary statistics from raw grids, and independently evaluate the
PING Jacobian and Hessian analytically. Compare the central-carrier beat-source
approximation with the finite-sideband AM and genuine two-tone kernels. Rates
are per ms in PING and per s in JR. Run from any directory with the project venv.
"""
from pathlib import Path
import argparse
import hashlib
import json

import numpy as np
from nmm2_jcA import fp, TAU_E, TAU_I, TAU_A, TAU_G

ROOT = Path(__file__).resolve().parents[1]
CODE = ROOT / "code"


def jacobian(x, coupling):
    a = np.zeros((8, 8))
    for r, v, tau in ((0, 1, TAU_E), (2, 3, TAU_I)):
        a[r, r], a[r, v] = 2*x[v]/tau, 2*x[r]/tau
        a[v, r], a[v, v] = -2*np.pi**2*tau*x[r], 2*x[v]/tau
    a[1, 4], a[1, 6] = coupling, -coupling
    a[3, 4], a[3, 6] = coupling, -2*coupling
    for r, s, z, tau in ((0, 4, 5, TAU_A), (2, 6, 7, TAU_G)):
        a[s, z] = 1/tau
        a[z, r], a[z, s], a[z, z] = 1/tau, -1/tau, -2/tau
    return a


def hessian(u, v):
    u, v = np.broadcast_arrays(u, v)
    out = np.zeros_like(u, dtype=complex)
    for r, k, tau in ((0, 1, TAU_E), (2, 3, TAU_I)):
        out[..., r] = 2*(u[..., r]*v[..., k] + u[..., k]*v[..., r])/tau
        out[..., k] = 2*(u[..., k]*v[..., k] - (np.pi*tau)**2*u[..., r]*v[..., r])/tau
    return out


def audit_modes():
    # This local, versioned cache contains the producer's variable-length grids.
    d = np.load(CODE / "nmm2_jcurve_modes.npz", allow_pickle=True)
    table = json.loads((ROOT / "docs/landau1_nmm2_jcurve_modes_2026-10-05.json").read_text())
    for key in ("C", "gam_crit", "f_crit", "Gpk_src", "fGpk_src", "simpk", "crit"):
        np.testing.assert_allclose(d[key], table[key], rtol=1e-12, atol=0)
    grids = [np.asarray(row, dtype=float) for row in d["sim_amps"]]
    peaks = np.array([row.max() for row in grids])
    np.testing.assert_allclose(d["simpk"], peaks, rtol=1e-12)
    bracketed = [0 < row.argmax() < len(row)-1 for row in grids]
    assert all(bracketed) and all(d["bracketed"])
    idx = d["amp_idx"]
    ref = max(d["amp_amps_A2"][0]) / 4 / d["Gpk_src"][idx[0]]
    ratios = {}
    for amp in (2, 4, 8):
        rows = [np.asarray(row, dtype=float) for row in d[f"amp_amps_A{amp}"]]
        assert all(0 < row.argmax() < len(row)-1 for row in rows)
        ratios[str(amp)] = np.array([row.max() for row in rows]) / amp**2 / d["Gpk_src"][idx] / ref
        np.testing.assert_allclose(ratios[str(amp)], table["amp_check"][f"A{amp}"], rtol=1e-12)
    fgrid = d["fgrid"]
    omega = 2*np.pi*fgrid/1000
    wc = 2*np.pi*.300
    b = np.zeros(8); b[1] = 1/TAU_E
    eye = np.eye(8)
    gains = {k: [] for k in ("central", "am", "twotone")}
    frequencies = {k: [] for k in gains}
    eigen_errors = []
    for i, coupling in enumerate(d["C"]):
        a = jacobian(fp(coupling)[0], coupling)
        claimed = -d["gam_crit"][i] + 2j*np.pi*d["f_crit"][i]/1000
        eigen_errors.append(float(np.min(abs(np.linalg.eigvals(a)-claimed))))
        def q(w):
            matrices = 1j*np.asarray(w)[..., None, None]*eye-a
            return np.linalg.solve(matrices, np.broadcast_to(b, matrices.shape[:-1])[..., None])[..., 0]
        q0 = q(wc)
        sources = {
            "central": np.broadcast_to(hessian(q0, q0.conj()), (len(fgrid), 8)),
            # Each gain is twice the physical beat amplitude per input amplitude squared.
            "am": (hessian(q(wc+omega), q0.conj()) + hessian(q0, q(wc-omega).conj()))/2,
            "twotone": hessian(q(wc+omega/2), q(wc-omega/2).conj()),
        }
        matrices = 1j*omega[:, None, None]*eye-a
        for key, source in sources.items():
            response = abs(np.linalg.solve(matrices, source[..., None])[:, 0, 0])
            j = response.argmax()
            gains[key].append(float(response[j]))
            frequencies[key].append(float(fgrid[j]))
    gains = {k: np.array(v) for k, v in gains.items()}
    rel_source_error = gains["central"]/d["Gpk_src"] - 1
    assert max(eigen_errors) < 1e-7
    assert np.max(abs(rel_source_error)) < .002
    near = d["C"] >= 16.25
    slopes = {k: float(np.polyfit(np.log(1/d["gam_crit"][near]), np.log(v[near]), 1)[0]) for k, v in gains.items()}
    return {
        "critical_eigenvalue_max_absolute_error_per_ms": max(eigen_errors),
        "central_source_max_relative_error_vs_finite_difference": float(np.max(abs(rel_source_error))),
        "critical_range_gain_exponent": slopes,
        "critical_damping_range_per_ms": [float(d["gam_crit"][near].max()), float(d["gam_crit"][near].min())],
        "full_range_gain_exponent": float(np.polyfit(np.log(1/d["gam_crit"]), np.log(d["Gpk_src"]), 1)[0]),
        "am_finite_sideband_gain_over_central_range": [float(np.min(gains["am"]/gains["central"])), float(np.max(gains["am"]/gains["central"]))],
        "twotone_gain_over_central_range": [float(np.min(gains["twotone"]/gains["central"])), float(np.max(gains["twotone"]/gains["central"]))],
        "amp2_max_normalized_departure": float(np.max(abs(ratios["2"]-1))),
        "amp8_max_normalized_excess": float(np.max(ratios["8"]-1)),
        "amp8_endpoint_normalized_ratio": float(ratios["8"][-1]),
        "grid_spacing_Hz": float(fgrid[1]-fgrid[0]),
        "all_main_and_amplitude_peaks_bracketed": True,
        "max_parabolic_peak_correction": float(max(d["simpk_parabolic"]/d["simpk"]-1)),
        "C": d["C"].tolist(), "linear_peak_frequencies_Hz": frequencies,
        "gain_convention": "Twice the physical second-order rate amplitude per input amplitude squared; central carrier 300 Hz, AM m=1 or equal genuine tones.",
    }


def audit_timing():
    result = {}
    for name, cache in (("AM", "timing_not_rate.npz"), ("twotone", "timing_not_rate_twotone.npz")):
        d = np.load(CODE / cache)
        order = np.argsort(d["gam"])[::-1]
        ac, dc, g = (d[k][order] for k in ("AC", "DC", "gam"))
        ratio = ac/abs(dc)
        result[name] = {
            "modulation_mHz": [float(ac[0]*1000), float(ac[-1]*1000)],
            "mean_shift_mHz": [float(dc[0]*1000), float(dc[-1]*1000)],
            "modulation_growth": float(ac[-1]/ac[0]), "mean_shift_growth": float(dc[-1]/dc[0]),
            "ratios_far_max_nearest": [float(ratio[0]), float(ratio.max()), float(ratio[-1])],
            "peak_ratio_gamma_per_s": float(g[ratio.argmax()]),
            "maximum_absolute_fractional_mean_shift": float(max(abs(dc))/d["rate_off"]),
            "baseline_rate_Hz": float(d["rate_off"]),
        }
    return result


def audit_controls():
    d = json.loads((ROOT / "docs/landau5_ti_tacs_twotone_2026-10-05.json").read_text())
    ratio_am = np.array(d["TI_AM"])/d["tACS_0p1"]
    ratio_two = np.array(d["TI_twotone"])/d["tACS_0p1"]
    np.testing.assert_allclose(ratio_am, d["ratio_AM"])
    np.testing.assert_allclose(ratio_two, d["ratio_twotone"])
    m = d["matched"]
    np.testing.assert_allclose(np.array(m["TI_twotone"])/m["tACS_matched"], m["TI_over_matched"])
    return {"max_fractional_ratio_change": float(max(abs(ratio_two/ratio_am-1))), "matched": m}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json", type=Path, required=True)
    args = parser.parse_args()
    report = {"modes": audit_modes(), "timing": audit_timing(), "ti_tacs": audit_controls()}
    inputs = [CODE / name for name in ("nmm2_jcurve_modes.npz", "timing_not_rate.npz", "timing_not_rate_twotone.npz")]
    report["sha256"] = {str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest() for p in inputs}
    args.json.parent.mkdir(parents=True, exist_ok=True)
    args.json.write_text(json.dumps(report, indent=2)+"\n")
    print(json.dumps({k: {a: b for a, b in v.items() if a not in ("C", "linear_peak_frequencies_Hz")} for k, v in report.items() if k != "sha256"}, indent=2))
