"""Stuart-Landau dissociation (TN0484 appendix): the SL normal form AMPLIFIES near the
Hopf (~1/gamma) but CANNOT demodulate a TI carrier -- it has no square-law (even-order)
term. This isolates the paper's two ingredients: amplification = universal near-Hopf
susceptibility (shared with tACS); detection = the model-specific square-law SL lacks.

SL:  zdot = (a + i*w0) z - |z|^2 z + F(t),   stable side a<0 (gamma = -a = distance to Hopf).
AM field: F(t) = eps (1 + m cos(Om t)) cos(wc t).

Parity argument: the field forces at odd carrier index k=+-1; the cubic z|z|^2 maps
odd->odd and the linear operator preserves k, so z has support only at odd k and zero
weight at the beat Delta f (k=0) to all orders. Demodulation is the O(eps^2) square-law
term (1/2) sigma'' eps^2 m; SL has no even-order term, so it is identically zero.

Two panels (fig_sl_dissociation, S-numbered):
 (a) SL forced directly in-band at Delta f -> lock-in ~ 1/gamma  (tACS works).
 (b) SL under the AM carrier -> ~zero Delta f line; a square-law detector (F^2) restores it.

Self-contained: numpy only.
"""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import figstyle; figstyle.apply()

FIGS = os.environ.get("TN_FIGDIR") or os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "figures")
os.makedirs(FIGS, exist_ok=True)
NEBLUE, NERED, NEGRAY = figstyle.NEBLUE, figstyle.NERED, figstyle.NEGRAY
TWO_PI = 2 * np.pi


def sl_lockin(a, w0, Ffun, Om, T=60.0, t_meas=40.0, dt=2e-4):
    """Integrate the SL ODE (RK4, vectorized over the array `a`); return the lock-in
    amplitude of Re(z) at angular frequency Om over the tail window."""
    a = np.atleast_1d(np.asarray(a, float))
    z = np.full(a.shape, 0.01 + 0.0j)
    t = 0.0; n = int(T / dt); km = n - int(t_meas / dt)
    ac = np.zeros_like(a); as_ = np.zeros_like(a); cnt = 0

    def f(zz, tt):
        return (a + 1j * w0) * zz - (np.abs(zz) ** 2) * zz + Ffun(tt)

    for k in range(n):
        k1 = f(z, t); k2 = f(z + .5 * dt * k1, t + .5 * dt)
        k3 = f(z + .5 * dt * k2, t + .5 * dt); k4 = f(z + dt * k3, t + dt)
        z = z + (dt / 6) * (k1 + 2 * k2 + 2 * k3 + k4); t += dt
        if k >= km:
            x = z.real; ac += x * np.cos(Om * t); as_ += x * np.sin(Om * t); cnt += 1
    return 2.0 / cnt * np.hypot(ac, as_)


def tone_lockin(sig, t, Om):
    """Lock-in amplitude of a sampled real signal at Om (rectangular window)."""
    x = sig - sig.mean()
    return 2.0 / len(x) * np.hypot((x * np.cos(Om * t)).sum(), (x * np.sin(Om * t)).sum())


if __name__ == "__main__":
    f0 = 10.0; fc = 100.0; df = 10.0          # Delta f = f0 (resonant), carrier 100 Hz
    w0 = TWO_PI * f0; wc = TWO_PI * fc; Om = TWO_PI * df
    eps = 0.5; m = 1.0

    # --- (a) tACS-like: weak direct in-band drive at Delta f; sweep gamma=-a toward 0.
    # A weak drive keeps z in the linear regime so the forced response tracks 1/gamma
    # (a strong drive would saturate via the cubic, exactly as the main-text J-curve does). ---
    gam = np.geomspace(1.5, 0.05, 16)         # distance to Hopf
    a_grid = -gam
    eps_w = 0.02
    F_tacs = lambda tt: eps_w * np.cos(Om * tt)
    AC_forced = sl_lockin(a_grid, w0, F_tacs, Om)

    # --- (b) TI: AM carrier into the SL vs a square-law detector control ---
    a0 = -0.5
    F_am = lambda tt: eps * (1.0 + m * np.cos(Om * tt)) * np.cos(wc * tt)
    AC_sl = float(sl_lockin(a0, w0, F_am, Om)[0])       # SL Re(z) at Delta f -> ~floor
    # square-law detector: lock-in of F(t)^2 at Delta f (the demodulated envelope line)
    dt = 2e-4; tt = np.arange(0.0, 40.0, dt)
    AC_sq = tone_lockin(F_am(tt) ** 2, tt, Om)
    print(f"(a) forced lock-in: {AC_forced[0]:.3e} (gamma={gam[0]:.2f}) -> "
          f"{AC_forced[-1]:.3e} (gamma={gam[-1]:.2f})")
    print(f"(b) AM carrier:  SL Re(z)@df = {AC_sl:.3e} ;  square-law F^2@df = {AC_sq:.3e} ;  "
          f"ratio = {AC_sq / max(AC_sl, 1e-12):.1e}")

    fig, (axA, axB) = plt.subplots(1, 2, figsize=(9.4, 3.7))
    # (a)
    axA.loglog(1.0 / gam, AC_forced, "o-", color=NEBLUE, ms=4, label="SL forced lock-in")
    kk = AC_forced[0] * gam[0]
    axA.loglog(1.0 / gam, kk / gam, "--", color=NEGRAY, lw=1.0, label=r"$\propto 1/\gamma$")
    axA.set_xlabel(r"$1/\gamma$  (closeness to Hopf)")
    axA.set_ylabel(r"lock-in of $\mathrm{Re}\,z$ at $\Delta f$")
    axA.set_title(r"(a) SL amplifies: forced response $\propto 1/\gamma$ (tACS)")
    axA.legend(loc="upper left")
    # (b)
    bars = [AC_sl, AC_sq]; labs = ["SL state\n$\\mathrm{Re}\\,z$", "square-law\ndetector $F^2$"]
    axB.bar([0, 1], bars, width=0.6, color=[NEBLUE, NERED])
    axB.set_yscale("log"); axB.set_xticks([0, 1]); axB.set_xticklabels(labs)
    axB.set_ylabel(r"lock-in at $\Delta f$")
    axB.set_ylim(min(bars) * 0.3, max(bars) * 3)
    for x, v in zip([0, 1], bars):
        axB.text(x, v * 1.4, f"{v:.1e}", ha="center", fontsize=8)
    axB.set_title(r"(b) SL cannot demodulate the TI carrier")
    axB.text(0.5, 0.04, f"$\\sim$%.0e$\\times$ gap" % (AC_sq / max(AC_sl, 1e-12)),
             transform=axB.transAxes, ha="center", fontsize=8, color=NEGRAY)

    fig.tight_layout()
    for ext in ("pdf", "png"):
        fig.savefig(os.path.join(FIGS, f"fig_sl_dissociation.{ext}"), dpi=300, bbox_inches="tight")
    print("wrote fig_sl_dissociation.{pdf,png} to", FIGS)
