"""
Genuine two-tone JR figures.

The paper's headline demonstration must show the waveform physical TI actually
delivers -- two tones at f1 and f2 -- not the amplitude-modulated surrogate, whose
spectrum carries a third line at the carrier and whose demodulated output carries a
spurious 2*Omega component at 25% of the fundamental.

Produces
--------
  fig_demodulation_twotone   Fig. 3 replacement: two-tone input (lines only at f1,f2,
                             nothing in the alpha band) -> synthesized alpha output.
  fig_curvature_twotone      Combined mechanistic figure (Fig. 6 + S8 + the surrogate
                             equivalence control):
                               (a) signed open-loop response vs operating point,
                                   against (1/2) sigma''(v*) eps^2
                               (b) log-log amplitude scaling, expecting slope 2
                               (c) nonlinear vs linearized sigmoid, closed loop
                               (d) AM vs two-tone at Omega, ratio -> 1 as eps -> 0

The (d) control is what licenses continued use of the AM surrogate for the dense
perturbative sweeps (Figs. 4 and 9), which measure only the leading Omega component.
"""

import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import figstyle
figstyle.apply()
import overlap
from jr_demod import (integrate, steady_v, Sigm, Sigm2, openloop_inphase,
                      field, v0 as V0)

NEBLUE, NERED, NEGRAY = figstyle.NEBLUE, figstyle.NERED, figstyle.NEGRAY
HERE = os.path.dirname(os.path.abspath(__file__))
FIGS = os.environ.get("TN_FIGDIR") or os.path.join(HERE, "..", "figures")
os.makedirs(FIGS, exist_ok=True)

F0 = 11.1
fc, m, dt = 100.0, 1.0, 2e-4


def spec(x, dt):
    x = x - x.mean()
    w = np.hanning(len(x))
    return np.fft.rfftfreq(len(x), dt), np.abs(np.fft.rfft(x * w)) / (w.sum() / 2)


# ------------------------------------------------------- Fig. 3, two-tone
def fig_demod():
    p0 = np.array([330.0])
    Om0 = np.array([2 * np.pi * F0])
    amp, t, v, s = integrate(p0, Om0, eps=1.0, m=m, fc=fc, t_settle=10.0,
                             t_meas=3.0, dt=dt, record=True, wave='twotone')
    fI, PI = spec(s, dt)
    fV, PV = spec(v, dt)

    fig, ax = plt.subplots(2, 2, figsize=(10.5, 6.2))
    w0 = (t >= t[0]) & (t <= t[0] + 0.5)
    tt = t[w0] - t[0]

    ax[0, 0].plot(tt, s[w0], color=NEGRAY, lw=0.6, alpha=0.8)
    # envelope of two equal tones: A(t) = 2 eps |cos(Om t / 2)| -- a rectified
    # cosine, not a sinusoid. It is A^2 that is sinusoidal at Omega.
    ax[0, 0].plot(tt, 2.0 * np.abs(np.cos(np.pi * F0 * tt)), color=NERED, lw=1.9)
    ax[0, 0].set_xlabel("time (s)")
    ax[0, 0].set_ylabel("field (mV)")
    figstyle.panel(ax[0, 0], "a")

    ax[0, 1].semilogy(fI, PI + 1e-9, color=NEGRAY, lw=1.4)
    ax[0, 1].set_xlim(0, 130)
    ax[0, 1].set_ylim(1e-4, 3)
    ax[0, 1].axvspan(8, 13, color=NERED, alpha=0.13)
    for fl in (fc - F0 / 2, fc + F0 / 2):
        ax[0, 1].axvline(fl, color=NEGRAY, ls="--", lw=0.6, alpha=0.45)
    ax[0, 1].set_xlabel("frequency (Hz)")
    ax[0, 1].set_ylabel("power")
    figstyle.panel(ax[0, 1], "b")

    ax[1, 0].plot(tt, v[w0], color=NEBLUE, lw=1.7)
    ax[1, 0].set_xlabel("time (s)")
    ax[1, 0].set_ylabel("LFP $v$ (mV)")
    figstyle.panel(ax[1, 0], "c")

    ax[1, 1].semilogy(fV, PV + 1e-9, color=NEBLUE, lw=1.4)
    ax[1, 1].set_xlim(0, 130)
    ax[1, 1].set_ylim(1e-4, 3)
    ax[1, 1].axvspan(8, 13, color=NERED, alpha=0.13)
    ax[1, 1].annotate("demodulated\nalpha line", xy=(11, 1.2), xytext=(40, 0.3),
                      fontsize=8, color=NEBLUE,
                      arrowprops=dict(arrowstyle="->", color=NEBLUE, lw=0.8))
    ax[1, 1].set_xlabel("frequency (Hz)")
    ax[1, 1].set_ylabel("power")
    figstyle.panel(ax[1, 1], "d")

    from matplotlib.ticker import LogLocator, NullFormatter
    for axis in (ax[0, 1].yaxis, ax[1, 1].yaxis):
        axis.set_minor_locator(LogLocator(subs=()))
        axis.set_minor_formatter(NullFormatter())

    fig.tight_layout(w_pad=2.5, h_pad=1.8)
    figstyle.thin_ticks(fig)
    figstyle.scale_text(fig, placed_frac=1)
    overlap.check(fig, placed_frac=1, name="jr_twotone_figs.py:demod")
    fig.savefig(f"{FIGS}/fig_demodulation_twotone.png", dpi=300)
    fig.savefig(f"{FIGS}/fig_demodulation_twotone.pdf")
    plt.close(fig)

    ia = np.argmin(np.abs(fV - F0))
    band = (fI > 8) & (fI < 13)
    print(f"  two-tone input: max power in 8-13 Hz band = {PI[band].max():.3e}")
    print(f"  output alpha line at {fV[ia]:.2f} Hz, power = {PV[ia]:.3e}")
    print("  wrote fig_demodulation_twotone")


# ------------------------------- combined curvature / scaling / control
def fig_curvature():
    # (a) signed open-loop response across the operating range, two-tone
    vs = np.linspace(V0 - 6.0, V0 + 6.0, 121)
    Om = np.full_like(vs, 2 * np.pi * F0)
    fcv = np.full_like(vs, fc)
    eps_ol = 0.3
    meas = openloop_inphase(vs, eps_ol, m, Om, fcv, wave='twotone')
    pred = 0.5 * Sigm2(vs) * eps_ol ** 2

    # (b) amplitude scaling, closed loop, well-damped focus
    epsv = np.array([0.05, 0.1, 0.2, 0.4, 0.8])
    resp = np.array([integrate(np.array([395.0]), np.array([2 * np.pi * 10.9]),
                               epsv[i], m, fc, 8.0, 3.0, dt, wave='twotone')[0]
                     for i in range(len(epsv))])
    slope = np.polyfit(np.log(epsv[:3]), np.log(resp[:3]), 1)[0]

    # (c) nonlinear vs linearized sigmoid, closed loop
    p1 = np.array([330.0])
    Om1 = np.array([2 * np.pi * F0])
    vop, S1 = steady_v(p1)
    r_nl = integrate(p1, Om1, 1.0, m, fc, 10.0, 3.0, dt, wave='twotone')[0]
    r_li = integrate(p1, Om1, 1.0, m, fc, 10.0, 3.0, dt, lin=(vop, S1),
                     wave='twotone')[0]

    # (d) AM vs two-tone equivalence at Omega
    eps_eq = np.geomspace(0.02, 1.0, 9)
    v_eq = np.array([8.0])
    a_am, a_2t = [], []
    for e in eps_eq:
        a_am.append(abs(openloop_inphase(v_eq, e, m, np.array([2 * np.pi * F0]),
                                         np.array([fc]), wave='am')[0]))
        a_2t.append(abs(openloop_inphase(v_eq, e, m, np.array([2 * np.pi * F0]),
                                         np.array([fc]), wave='twotone')[0]))
    a_am, a_2t = np.array(a_am), np.array(a_2t)

    fig, ax = plt.subplots(2, 2, figsize=(12.0, 7.6))

    ax[0, 0].axhline(0, color=NEGRAY, lw=0.6)
    ax[0, 0].axvline(V0, color=NEGRAY, ls=":", lw=1.0)
    ax[0, 0].plot(vs, pred, "--", color=NERED, lw=1.6,
                  label=r"$\frac{1}{2}\sigma''(v^*)\varepsilon^2$")
    ax[0, 0].plot(vs, meas, color=NEBLUE, lw=1.8, label="measured (two-tone)")
    ax[0, 0].set_xlabel("operating point $v^*$ (mV)")
    ax[0, 0].set_ylabel("signed response @ $\\Omega$ (s$^{-1}$)")
    ax[0, 0].legend(loc="lower right", fontsize=8)
    figstyle.panel(ax[0, 0], "a")

    ax[0, 1].loglog(epsv, resp, "o-", color=NEBLUE, ms=6)
    ax[0, 1].loglog(epsv, resp[0] * (epsv / epsv[0]) ** 2, "--", color=NEGRAY,
                    lw=1.2, label=f"slope 2 (measured {slope:.2f})")
    ax[0, 1].set_xlabel("field amplitude $\\varepsilon$ (mV)")
    ax[0, 1].set_ylabel("response @ $\\Omega$ (mV)")
    ax[0, 1].legend(loc="upper left", fontsize=8)
    figstyle.panel(ax[0, 1], "b")

    ax[1, 0].bar([0, 1], [r_nl, r_li], color=[NEBLUE, NEGRAY], width=0.55)
    ax[1, 0].set_yscale("log")
    ax[1, 0].set_xticks([0, 1])
    ax[1, 0].set_xticklabels(["sigmoid", "linearized"])
    ax[1, 0].set_ylabel("response @ $\\Omega$ (mV)")
    ax[1, 0].annotate(f"${r_nl/max(r_li,1e-12):.0f}\\times$", xy=(0.5, np.sqrt(r_nl * max(r_li, 1e-12))),
                      ha="center", fontsize=10, color=NERED)
    figstyle.panel(ax[1, 0], "c")

    ax[1, 1].semilogx(eps_eq, a_2t / a_am, "o-", color=NEBLUE, ms=5)
    ax[1, 1].axhline(1.0, color=NEGRAY, ls="--", lw=1.0)
    ax[1, 1].set_xlabel("field amplitude $\\varepsilon$ (mV)")
    ax[1, 1].set_ylabel("two-tone / AM  at $\\Omega$")
    ax[1, 1].set_ylim(0.95, 1.02)
    figstyle.panel(ax[1, 1], "d")

    # Log minor-tick labels collide once the type is scaled up for the page;
    # label decades only, as make_figures.py does for the same reason.
    from matplotlib.ticker import LogLocator, NullFormatter
    for axis in (ax[0, 1].xaxis, ax[0, 1].yaxis, ax[1, 0].yaxis, ax[1, 1].xaxis):
        axis.set_minor_locator(LogLocator(subs=()))
        axis.set_minor_formatter(NullFormatter())

    fig.tight_layout(w_pad=5.0, h_pad=3.0)
    figstyle.thin_ticks(fig)
    figstyle.scale_text(fig, placed_frac=1)
    overlap.check(fig, placed_frac=1, name="jr_twotone_figs.py:curvature")
    fig.savefig(f"{FIGS}/fig_curvature_twotone.png", dpi=300)
    fig.savefig(f"{FIGS}/fig_curvature_twotone.pdf")
    plt.close(fig)

    print(f"  curvature: max |measured - predicted| / max|predicted| = "
          f"{np.max(np.abs(meas - pred)) / np.max(np.abs(pred)):.4f}")
    print(f"  square law: log-log slope (small eps) = {slope:.2f}")
    print(f"  linearization control: {r_nl:.4f} -> {r_li:.3e} mV "
          f"({r_nl/max(r_li,1e-12):.0f}x collapse)")
    print(f"  AM/two-tone ratio at Omega: {a_2t[0]/a_am[0]:.4f} (eps={eps_eq[0]:.2f}) "
          f"-> {a_2t[-1]/a_am[-1]:.4f} (eps={eps_eq[-1]:.2f})")
    print("  wrote fig_curvature_twotone")


if __name__ == "__main__":
    print("Fig. 3 (two-tone):")
    fig_demod()
    print("Combined curvature/scaling/equivalence figure:")
    fig_curvature()
