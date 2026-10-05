"""
TI-to-tACS response ratio across the pinned coupling sweep (Giulio's question, October 5, 2026).

Reads the Figure 9 cache (jcurve_main.npz: TI, AM surrogate, eps 0.3 mV, m 1, carrier 100 Hz,
closed-loop lock-in at the beat, operating point pinned at v* = 8.30 mV) and the Figure S3
cache (tacs_jsweep.npz, preserved with this analysis: direct drive eps 0.1 mV,
same field-free pinning and coupling range) and compares the
ratio of closed-loop responses with the linear-response prediction (1/2)|Sigma''| eps^2 m /
(Sigma' eps_t), which contains no gamma. The TI curve is interpolated (log) onto the tACS
couplings. Output: ../docs/r7_ti_tacs_ratio_vs_gamma_2026-10-05.json
"""
import os, json, hashlib
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
T = np.load(os.path.join(HERE, "jcurve_main.npz")); S = np.load(os.path.join(HERE, "tacs_jsweep.npz"))
C_ti, g_ti, A_ti, Aop = T["C"], T["gamma"], T["Acl"], T["Aop"]; C_ta, g_ta, A_ta = S["Cs"], S["gam"], S["A"]
e0, rho, v0, v = 2.5, 0.56, 6.0, 8.30
s = 1 / (1 + np.exp(rho * (v0 - v))); S1 = 2 * e0 * rho * s * (1 - s); S2 = 2 * e0 * rho ** 2 * s * (1 - s) * (1 - 2 * s)
eps_ti, m, eps_ta = 0.3, 1.0, 0.1
pred = 0.5 * abs(S2) * eps_ti ** 2 * m / (S1 * eps_ta)
o = np.argsort(C_ti)
if not (C_ti.min() <= C_ta.min() and C_ta.max() <= C_ti.max()):
    raise ValueError("tACS coupling grid extends outside the TI interpolation range")
if np.any(A_ti <= 0) or np.any(A_ta <= 0):
    raise ValueError("positive amplitudes are required for the log interpolation and ratio")
A_i = np.exp(np.interp(C_ta, C_ti[o], np.log(A_ti[o]))); Aop_i = np.interp(C_ta, C_ti[o], Aop[o])
rows = [dict(C=float(c), gamma_per_s=float(g), A_TI_mV=float(a), A_tACS_mV=float(b), ratio=float(a / b),
             ratio_over_linear=float(a / b / pred), TI_gain=float(a / ao))
        for c, g, a, b, ao in zip(C_ta, g_ta, A_i, A_ta, Aop_i)]
out = dict(v_star_mV=v, Sigma1=float(S1), Sigma2=float(S2), eps_TI_mV=eps_ti, m=m, eps_tACS_mV=eps_ta,
           linear_response_ratio=float(pred), rows=rows,
           units={"TI_gain": "mV s", "ratio": "dimensionless"},
           pinning="field-free v*=8.30 mV; the stimulated mean is not clamped",
           interpolation="linear interpolation of log TI amplitude in coupling C; no extrapolation",
           input_sha256={name: hashlib.sha256(open(os.path.join(HERE, name), "rb").read()).hexdigest()
                         for name in ("jcurve_main.npz", "tacs_jsweep.npz")},
           reading="The ratio is about 0.14 far from the Hopf and rises near it at these fixed, unequal "
                   "input amplitudes. Earlier saturation of the larger tACS response is consistent with "
                   "the curves; this cache comparison alone does not separate saturation from mean shifts.")
json.dump(out, open(os.path.join(HERE, "..", "docs", "r7_ti_tacs_ratio_vs_gamma_2026-10-05.json"), "w"), indent=1)
print(f"linear-response ratio {pred:.4f}")
for r in rows:
    print(f"C={r['C']:7.2f} gamma={r['gamma_per_s']:6.3f}/s  A_TI={r['A_TI_mV']:.4f}  A_tACS={r['A_tACS_mV']:.4f}  ratio={r['ratio']:.4f}  x linear={r['ratio_over_linear']:.3f}  TI gain={r['TI_gain']:.1f}")
