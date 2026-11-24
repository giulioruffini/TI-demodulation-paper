"""Bounded numerical diagnostic for the S3(a) high-carrier upturn of the soma route.

fig_khz_direct(a): the tau_m = 16 ms curve leaves the 1/f_c^2 guide above ~1.5 kHz and
turns up at 4 kHz (1.7e-6 mV at 2.66 kHz, 4e-6 mV at 4 kHz). Suspects, tested with the
existing solver (khz_direct.rhs7/step/lockin_sweep, RK4, Hann lock-in at Omega = f0):
  A  reference: the generator's settings (dt = 2e-5 s, settle 6 s, measure 3 s), soma
     route, carriers from the generator's grid plus 6 and 8 kHz;
  B  field off (eps = 0), same settings: whatever the lock-in reads is the residual of
     the start-up transient (all columns start at Y = 0, far from the fixed point) at
     Omega, which is the autonomous frequency f0 by construction;
  C  settle 12 s instead of 6 s (field on): a transient floor falls, a solver floor does not;
  D  dt = 1e-5 s (field on, settle 6 s): a time-step artifact changes, a transient does not;
  E  6 s field-off pre-equilibration, then 6 s with the field on (a pre-equilibrated
     start, not an exact fixed-point initialization).
Inputs (eps, m, carriers, tau) are those of the generator. Nothing is written to code/.
Run: cd <staged code dir>; python khz_direct_upturn_diag.py > khz_direct_upturn_diag.log
"""
import os, sys, time, json
import numpy as np
sys.path.insert(0, os.getcwd())
import khz_direct as K
from timing_not_rate import jac_eig

vfp, g0, w0 = jac_eig(K.p, K.C); F0 = w0 / (2 * np.pi); K.Om = 2 * np.pi * F0
print(f"operating point v*={vfp:.3f} mV, gamma={g0:.4f} (1/s), f0={F0:.3f} Hz")
print(f"transient after 6 s ~ exp(-gamma 6) = {np.exp(-g0*6):.3e}; after 12 s {np.exp(-g0*12):.3e}")

fcs_gen = np.geomspace(100., 4000., 10)
fcs = np.r_[fcs_gen[-4:], 6000., 8000.]
TAU = 16e-3
guide = lambda A1k, f: A1k * (f / fcs_gen[-4]) ** -2      # anchored at the 1.17 kHz point

def run(label, dt=2e-5, t_set=6.0, t_meas=3.0, eps=0.5, fixed_point_start=False, carriers=fcs):
    N = len(carriers); tau = np.full(N, TAU); direct = np.zeros(N, bool)
    K.eps = eps
    t0 = time.time()
    if fixed_point_start:
        # field-free fixed point of the 6 JR states; xf = 0
        Y = np.zeros((N, 7)); t = 0.0
        # settle the field-free column first (eps = 0) so the start is the fixed point
        K.eps = 0.0
        ns = int(t_set / dt)
        for _ in range(ns):
            Y = K.step(Y, t, dt, carriers, tau, direct); t += dt
        K.eps = eps
        ns = int(t_set / dt); nm = int(t_meas / dt)
        for _ in range(ns):
            Y = K.step(Y, t, dt, carriers, tau, direct); t += dt
        w = np.hanning(nm); ws = w.sum()
        ac = np.zeros(N); as_ = np.zeros(N); av = np.zeros(N); awc = np.zeros(N); aws = np.zeros(N)
        for k in range(nm):
            Y = K.step(Y, t, dt, carriers, tau, direct); t += dt
            v = Y[:, 1] - Y[:, 2]; co = np.cos(K.Om * t); si = np.sin(K.Om * t)
            ac += w[k]*v*co; as_ += w[k]*v*si; av += w[k]*v; awc += w[k]*co; aws += w[k]*si
        vb = av/ws; c = ac - vb*awc; s = as_ - vb*aws
        out = 2/ws*np.sqrt(c**2 + s**2)
    else:
        out = K.lockin_sweep(carriers, tau, direct, dt, t_set, t_meas)
    el = time.time() - t0
    print(f"\n[{label}] dt={dt:g} settle={t_set:g} s measure={t_meas:g} s eps={eps:g}"
          f"{' fixed-point start' if fixed_point_start else ''}  ({el:.0f} s)")
    for f, v in zip(carriers, out):
        print(f"   f_c={f:7.1f} Hz  A_Omega={v:.3e} mV   guide={guide(out[0], f):.3e}   ratio={v/guide(out[0], f):.3f}")
    return out

res = {}
res["A_reference"] = run("A reference")
res["B_field_off"] = run("B field off", eps=0.0)
res["C_settle12"] = run("C settle 12 s", t_set=12.0)
res["D_dt1e-5"] = run("D dt 1e-5", dt=1e-5)
res["E_fixed_point_start"] = run("E fixed-point start", fixed_point_start=True)
json.dump({k: v.tolist() for k, v in res.items()} | {"fc_Hz": fcs.tolist(), "f0_Hz": F0, "gamma_per_s": g0},
          open("khz_direct_upturn_diag.json", "w"), indent=1)
print("\nwrote khz_direct_upturn_diag.json")
