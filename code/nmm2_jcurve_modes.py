"""Landau finding 1 (2026-10-05): does the NMM2 J-curve peak follow 1/gamma of the CRITICAL mode?
Tracks the eigenvalue that crosses at the gamma Hopf J* by continuation backward from J*, computes
the exact linear-response gain from a beat-frequency source in the v_E equation to r_E over a fine
frequency grid, and re-measures the simulated lock-in peak on an adaptive grid centred on the
linear-response peak. Same engine, drive, and lock-in as nmm2_jcD.py. Writes nmm2_jcurve_modes.npz."""
import numpy as np, json, sys
from scipy.optimize import brentq
from nmm2_jcA import fp, gam_w, rhs, init, rk4, PI, ETA

def jac(x, C, h=1e-7):
    J = np.zeros((8, 8))
    f = lambda xx: rhs(xx.reshape(8, 1), 0.0, ETA, np.array([C]), np.zeros(1), 0.0, 0.0).ravel()
    for j in range(8):
        d = np.zeros(8); d[j] = h; J[:, j] = (f(x + d) - f(x - d)) / (2 * h)
    return J

Chopf = brentq(lambda C: gam_w(fp(C)[0], C)[0], 15.0, 18.0)
cache = np.load("nmm2_jcD.npz")
Cg = cache["C"]
# fixed points, continued from low C as in nmm2_jcD
xs = []; g = (0.05, 0.05)
for C in Cg:
    x, re, ri = fp(C, g); g = (re, ri); xs.append(x)
xH, _, _ = fp(Chopf, g)
# continuation of the critical eigenvalue backward from J*
evH = np.linalg.eigvals(jac(xH, Chopf))
lam = evH[np.argmin(np.abs(evH.real) + 1e3 * (evH.imag <= 0))]   # Re~0, Im>0
crit = np.zeros(len(Cg), complex)
Cpath = np.concatenate([[Chopf], Cg[::-1]])
xpath = [xH] + xs[::-1]
for k in range(1, len(Cpath)):
    # sub-steps for a safe continuation
    C0, C1 = Cpath[k - 1], Cpath[k]
    for s in np.linspace(0, 1, 21)[1:]:
        Cs = C0 + s * (C1 - C0)
        xs_, _, _ = fp(Cs, (xpath[k][0], xpath[k][2]))
        ev = np.linalg.eigvals(jac(xs_, Cs)); ev = ev[ev.imag > 0]
        lam = ev[np.argmin(np.abs(ev - lam))]
    crit[len(Cg) - k] = lam
gam_crit = -crit.real; f_crit = crit.imag / (2 * PI) * 1000
# exact linear-response gain v_E-source -> r_E
fgrid = np.linspace(15, 90, 1501); b = np.zeros(8); b[1] = 1.0
Gpk = np.zeros(len(Cg)); fGpk = np.zeros(len(Cg))
for i, (C, x) in enumerate(zip(Cg, xs)):
    J = jac(x, C)
    G = np.array([abs(np.linalg.solve(1j * 2 * PI * f / 1000 * np.eye(8) - J, b)[0]) for f in fgrid])
    Gpk[i] = G.max(); fGpk[i] = fgrid[G.argmax()]
print(f"J*={Chopf:.4f}")
print("  C      gam_plot gam_crit f_crit  fG_pk  fpk_cache")
for i in range(len(Cg)):
    print(f"{Cg[i]:7.3f} {cache['gamma'][i]:8.4f} {gam_crit[i]:8.4f} {f_crit[i]:6.1f} {fGpk[i]:6.1f} {cache['fpk'][i]:6.1f}")
np.savez("/private/tmp/r1/modes_partial.npz", C=Cg, gam_crit=gam_crit, f_crit=f_crit, Gpk=Gpk, fGpk=fGpk, Chopf=Chopf)

# ---- scaling of the exact linear gain against the critical-mode damping
Gg = Gpk * gam_crit
print("\nGpk*gam_crit (normalized to the last point):", np.round(Gg / Gg[-1], 3))
near = Cg >= 16.25
sl = np.polyfit(np.log(1 / gam_crit[near]), np.log(Gpk[near]), 1)[0]
sl_all = np.polyfit(np.log(1 / gam_crit), np.log(Gpk), 1)[0]
print(f"log-log slope of linear Gpk vs 1/gam_crit: critical-dominated range (C>=16.25, gamma {gam_crit[near].max():.4f}-{gam_crit[near].min():.4f}/ms) {sl:.3f}; full sweep {sl_all:.3f}")

# ---- re-measured simulation peak: adaptive fine grid, settling >= 3.5/gamma
def lockin_pairs(C, fHz, Amp=8.0, fc_Hz=300.0, t_set=5000.0, t_meas=4000.0, dt=0.05):
    n = C.size; Om = 2 * PI * fHz / 1000.0
    y = init(n); wc = 2 * PI * fc_Hz / 1000.0; t = 0.0; Am = np.full(n, Amp); eta = np.full(n, ETA)
    for _ in range(int(t_set / dt)): y = rk4(y, t, dt, eta, C, Am, Om, wc); t += dt
    nm = int(t_meas / dt); w = np.hanning(nm)
    ac = np.zeros(n); as_ = np.zeros(n); av = np.zeros(n); awc = np.zeros(n); aws = np.zeros(n)
    for k in range(nm):
        y = rk4(y, t, dt, eta, C, Am, Om, wc); t += dt
        re = y[0]; co = np.cos(Om * t); si = np.sin(Om * t)
        ac += w[k] * re * co; as_ += w[k] * re * si; av += w[k] * re; awc += w[k] * co; aws += w[k] * si
    vb = av / w.sum(); c = ac - vb * awc; s = as_ - vb * aws
    return 2 / w.sum() * np.sqrt(c ** 2 + s ** 2)
if "--sim" in sys.argv:
    offs = np.array([-0.6, -0.3, -0.15, 0.0, 0.15, 0.3, 0.6])
    CC = np.repeat(Cg, len(offs)); FF = (fGpk[:, None] + offs[None, :]).ravel()
    A = lockin_pairs(CC, FF).reshape(len(Cg), len(offs))
    simpk = A.max(1)
    ratio = simpk / Gpk
    print("\nsim peak / linear Gpk (normalized to C=15.0 region median):")
    ref = np.median(ratio[(Cg > 14.5) & (Cg < 16.0)])
    for i in range(len(Cg)):
        print(f"{Cg[i]:7.3f} gam_crit {gam_crit[i]:.4f} simpk {simpk[i]:.4e} cache {cache['peak'][i]:.4e}  sim/lin {ratio[i]/ref:6.3f}  edge {'*' if A[i].argmax() in (0, len(offs)-1) else ''}")
    np.savez("nmm2_jcurve_modes.npz", C=Cg, gam_plot=cache["gamma"], gam_crit=gam_crit, f_crit=f_crit,
             Gpk=Gpk, fGpk=fGpk, simpk=simpk, sim_grid=A, offs=offs, cache_peak=cache["peak"], Chopf=Chopf)
    json.dump({"Chopf": Chopf, "slope_lin_near": sl, "slope_lin_all": sl_all,
               "C": Cg.tolist(), "gam_plot": cache["gamma"].tolist(), "gam_crit": gam_crit.tolist(),
               "f_crit": f_crit.tolist(), "Gpk": Gpk.tolist(), "fGpk": fGpk.tolist(),
               "simpk": simpk.tolist(), "cache_peak": cache["peak"].tolist()},
              open("../docs/landau1_nmm2_jcurve_modes_2026-10-05.json", "w"), indent=1)
    print("DONE")
