"""fig_mpr_crossover: (a) the uncoupled MPR detector coefficient kappa_DC(Q, w) from the static
curvature F''/4 at slow carriers to the Kapitza limit F'/(2 w^2) at fast ones, with
finite-amplitude simulations; (b) the error of the fast-carrier form for the manuscript's
PING at four operating points and three carriers. Reads ping_fast_carrier_check.json
(run ping_fast_carrier_check.py first)."""
import json, os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import figstyle; figstyle.apply()
import overlap
from ping_fast_carrier_check import C_closed, Fp, Fpp, D

HERE = os.path.dirname(os.path.abspath(__file__))
FIGS = os.environ.get("TN_FIGDIR") or os.path.join(os.path.dirname(HERE), "figures")
J = json.load(open(os.path.join(HERE, "ping_fast_carrier_check.json")))
TE = J["tau_E_ms"]
NEBLUE, NERED, NEGRAY = figstyle.NEBLUE, figstyle.NERED, figstyle.NEGRAY
NEGREEN = "#1a9850"

fig, (a1, a2) = plt.subplots(1, 2, figsize=(11.0, 4.0), gridspec_kw=dict(width_ratios=[1.35, 1]))

# ---- (a) uncoupled MPR: kappa_DC(Q, w)/... vs w tau
w = np.logspace(-1.3, 2.3, 400)
Qi = D / np.sqrt(3)
for Q, col, lab in ((0.0, NEBLUE, r"$Q=0$ (below inflection, $F''>0$)"),
                    (Qi, NEGREEN, r"$Q=\Delta/\sqrt{3}$ (inflection, $F''=0$)"),
                    (3.0, NERED, r"$Q=3$ (above inflection, $F''<0$)")):
    C = np.array([C_closed(Q, x) for x in w])
    a1.plot(w, C, color=col, lw=1.8, label=lab)
    a1.axhline(Fpp(Q) / 4, color=col, lw=0.9, ls=":", alpha=0.8)
    a1.plot(w, Fp(Q) / (2 * w ** 2), color=col, lw=0.9, ls="--", alpha=0.8)
    pts = [s for s in J["simulations"] if abs(s["Q"] - Q) < 1e-9]
    if pts:
        a1.plot([p["w"] for p in pts], [p["sim"] for p in pts], "o", color=col, ms=6, mfc="white", mew=1.5)
wz = J["limits"]["3.0"]["w_zero"]
a1.axvline(wz, color=NERED, lw=0.8, alpha=0.5)
a1.text(wz * 1.08, -0.0046, r"sign change $\tilde\omega_z$", color=NERED, fontsize=8, rotation=90, va="bottom")
a1.axhline(0, color="0.6", lw=0.8)
a1.set_xscale("log"); a1.set_xlim(w[0], w[-1]); a1.set_ylim(-0.005, 0.02)
a1.set_xlabel(r"normalized carrier frequency $\tilde\omega=\omega\tau_m$")
a1.set_ylabel(r"$\kappa_{\rm DC}$ (normalized units)")
a1.text(0.06, 0.0165, r"$\frac{1}{4} F''(Q)$: static curvature", color=NEBLUE, fontsize=8)
a1.text(14.0, 0.0082, r"$F'(Q)/(2\tilde\omega^2)$", color=NEBLUE, fontsize=8)
for f_hz, lab in ((300.0, "300 Hz"), (1000.0, "1 kHz")):      # carriers used in the paper, for tau = tau_E = 15 ms
    x = 2 * np.pi * f_hz * TE * 1e-3
    a1.axvline(x, color="0.75", lw=0.8, ls=":")
    a1.text(x * 1.06, -0.0046, lab + r" ($\tau_E$)", color="0.45", fontsize=7.5, rotation=90, va="bottom")
a1.legend(loc="upper right", bbox_to_anchor=(0.995, 0.86), frameon=False, fontsize=7.5)
figstyle.panel(a1, "a")

# ---- (b) PING: relative error of the fast-carrier form
states = {}
for p in J["ping"]:
    states.setdefault((p["C"], p["eta"]), []).append(p)
cols = [NEBLUE, NEGREEN, NERED, NEGRAY]
for (key, rows), col in zip(states.items(), cols):
    rows = sorted(rows, key=lambda r: r["fc_Hz"])
    fc = [r["fc_Hz"] for r in rows]; err = [100 * r["relative_error"] for r in rows]
    a2.loglog(fc, err, "o-", color=col, lw=1.4, ms=5,
              label=rf"$J={key[0]:g}$, $\bar\eta={key[1]:g}$ ($\gamma={rows[0]['gamma_per_ms']:.3f}$/ms)")
fc = np.array([300.0, 2000.0]); a2.loglog(fc, 1.0 * (300.0 / fc) ** 2, "--", color="0.5", lw=1.0, label=r"$\propto f_c^{-2}$")
a2.set_xlabel(r"carrier frequency $f_c$ (Hz)"); a2.set_ylabel("error of the fast-carrier source (%)")
from matplotlib.ticker import NullLocator, NullFormatter, FixedLocator, FixedFormatter
a2.set_xlim(250, 2500); a2.set_ylim(0.01, 2)
a2.xaxis.set_minor_locator(NullLocator()); a2.xaxis.set_minor_formatter(NullFormatter())
a2.yaxis.set_minor_locator(NullLocator()); a2.yaxis.set_minor_formatter(NullFormatter())
a2.xaxis.set_major_locator(FixedLocator([300, 1000, 2000])); a2.xaxis.set_major_formatter(FixedFormatter(["300", "1000", "2000"]))
a2.yaxis.set_major_locator(FixedLocator([0.01, 0.1, 1])); a2.yaxis.set_major_formatter(FixedFormatter(["0.01", "0.1", "1"]))
a2.legend(loc="lower left", frameon=False, fontsize=8)
figstyle.panel(a2, "b")

fig.tight_layout()
figstyle.scale_text(fig, placed_frac=1.0)
overlap.check(fig, placed_frac=1.0, name="mpr_crossover_fig.py")
for ext in ("pdf", "png"):
    fig.savefig(os.path.join(FIGS, f"fig_mpr_crossover.{ext}"), dpi=300, bbox_inches="tight")
print("wrote fig_mpr_crossover.pdf / .png")
