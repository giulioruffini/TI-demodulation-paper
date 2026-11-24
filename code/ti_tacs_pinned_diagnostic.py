"""
Pinning fixes the field-free point, not the stimulated mean: TI versus tACS at three
couplings of the pinned Jansen-Rit sweep (Kaiti's request, October 5, 2026).

For C in {110, 133.9090909, 136.3}, p = p_of_C(8.30, C) as in the published sweeps, beat at
the field-free modal frequency, four conditions: field off; TI (AM surrogate, eps 0.3 mV,
m 1, carrier 100 Hz, the Figure 9 drive); tACS eps 0.1 mV (the Figure S3 drive); tACS with
the source-matched amplitude eps_t = (1/2)|Sigma''(8.30)| eps^2 m / Sigma'(8.30) =
0.0143039 mV, which delivers the same leading in-band drive as TI's beat. Recorded over the
window: mean of v = y1 - y2, mean pyramidal rate Sigma(v + s) (field in the argument), and
the Hann lock-in at the beat. Settings: dt 2e-4 s, 12 s settling, 6 s window (published);
a repeat with 60 s settling and 20 s window at all three couplings, since the relaxation
time at the endpoint is 8 s. Output: ../docs/r7_ti_tacs_pinned_diagnostic_2026-10-05.json
"""
import os, sys, json
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import jr_jsweep_engine as E

VSTAR, EPS_TI, M, FC, EPS_TA = 8.30, 0.3, 1.0, 100.0, 0.1
def Sigm1(v):
    s = 1 / (1 + np.exp(E.rr * (E.v0 - v))); return 2 * E.e0 * E.rr * s * (1 - s)
EPS_TA_MATCH = 0.5 * abs(E.Sigm2(VSTAR)) * EPS_TI ** 2 * M / Sigm1(VSTAR)


def run(C, Om, cond, t_set, t_meas, dt=2e-4):
    p = np.array([E.p_of_C(VSTAR, C)]); Cv = np.array([C]); Y = np.zeros((1, 6)); t = 0.0
    def s_of(tt):
        if cond == 'off': return np.array([0.0])
        if cond == 'TI': return np.array([E.field(tt, EPS_TI, M, Om, FC)])
        if cond == 'tACS': return np.array([EPS_TA * np.cos(Om * tt)])
        if cond == 'tACS_matched': return np.array([EPS_TA_MATCH * np.cos(Om * tt)])
    ns, nm = int(t_set / dt), int(t_meas / dt)
    def step(Y, t):
        s1 = s_of(t); k1 = E.rhs(Y, p, Cv, s1); s2 = s_of(t + .5 * dt); k2 = E.rhs(Y + .5 * dt * k1, p, Cv, s2)
        k3 = E.rhs(Y + .5 * dt * k2, p, Cv, s2); s3 = s_of(t + dt); k4 = E.rhs(Y + dt * k3, p, Cv, s3)
        return Y + (dt / 6) * (k1 + 2 * k2 + 2 * k3 + k4)
    for _ in range(ns):
        Y = step(Y, t); t += dt
    w = np.hanning(nm); ws = w.sum(); ac = as_ = av = awc = aws = 0.0; rate = 0.0; vmin = np.inf; vmax = -np.inf
    for k in range(nm):
        Y = step(Y, t); t += dt
        v = float(Y[0, 1] - Y[0, 2]); sf = float(s_of(t)[0]); co = np.cos(Om * t); si = np.sin(Om * t)
        ac += w[k] * v * co; as_ += w[k] * v * si; av += w[k] * v; awc += w[k] * co; aws += w[k] * si
        rate += w[k] * float(E.Sigm(v + sf)); vmin = min(vmin, v); vmax = max(vmax, v)
    vb = av / ws; c = ac - vb * awc; s = as_ - vb * aws
    return dict(mean_v=float(vb), mean_rate=float(rate / ws), lockin=float(2 / ws * np.hypot(c, s)), v_min=vmin, v_max=vmax)


if __name__ == '__main__':
    out = dict(vstar=VSTAR, eps_TI=EPS_TI, m=M, fc=FC, eps_tACS=EPS_TA, eps_tACS_matched=float(EPS_TA_MATCH),
               Sigma1=float(Sigm1(VSTAR)), Sigma2=float(E.Sigm2(VSTAR)), results=[])
    print(f"source-matched tACS amplitude {EPS_TA_MATCH:.10f} mV")
    for C in (110.0, 133.9090909, 136.3):
        p = E.p_of_C(VSTAR, C); vfp, gam, w0, _ = E.jac_eig(p, C)
        print(f"== C={C:.7f}: p={p:.4f}, field-free v*={vfp:.4f}, gamma={gam:.4f}/s, f0={w0/2/np.pi:.3f} Hz")
        for (t_set, t_meas) in ((12.0, 6.0), (60.0, 20.0)):
            rows = {}
            for cond in ('off', 'TI', 'tACS', 'tACS_matched'):
                rows[cond] = run(C, w0, cond, t_set, t_meas)
            r = rows
            print(f"   settle {t_set:.0f} s, window {t_meas:.0f} s:")
            for cond in ('off', 'TI', 'tACS', 'tACS_matched'):
                q = r[cond]; print(f"     {cond:13s} <v>={q['mean_v']:.5f} mV (shift {q['mean_v']-r['off']['mean_v']:+.5f}) <rate>={q['mean_rate']:.5f} (shift {q['mean_rate']-r['off']['mean_rate']:+.5f}) lock-in {q['lockin']:.5f} mV  v range {q['v_min']:.3f}-{q['v_max']:.3f}")
            print(f"     ratios: TI/tACS {r['TI']['lockin']/r['tACS']['lockin']:.4f}; TI/tACS_matched {r['TI']['lockin']/r['tACS_matched']['lockin']:.4f}; tACS/tACS_matched {r['tACS']['lockin']/r['tACS_matched']['lockin']:.3f} (linear: {EPS_TA/EPS_TA_MATCH:.3f})")
            out['results'].append(dict(C=C, p=float(p), v_fixed=float(vfp), gamma=float(gam), f0_Hz=float(w0 / 2 / np.pi), t_set=t_set, t_meas=t_meas, conditions=rows))
    json.dump(out, open(os.path.join(HERE, '..', 'docs', 'r7_ti_tacs_pinned_diagnostic_2026-10-05.json'), 'w'), indent=1)
    print('wrote json')
