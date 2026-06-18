"""Plotter for fig_entrainment (S: the above-Hopf / oscillatory regime).

Rebuilt, honest 3-panel figure of entrainment of the autonomous JR alpha limit
cycle by a direct Delta f drive --- the supercritical counterpart of the 1/gamma
forced gain on the stable side:

  (a) 1:1 Arnold tongue   -- CONTINUOUS lock-in A_Omega over (Delta f, drive eps),
                             with the 1:1-locked boundary overlaid (entrain.npz).
  (b) frequency locking   -- dominant output frequency rides Delta f inside the
                             tongue, returns to f0 outside (entrain_b.npz).
  (c) toward criticality  -- 1:1 locking range (tongue width) grows, and the
                             autonomous cycle amplitude falls, as the operating
                             point approaches the Hopf (entrain_crit.npz). Wide
                             Delta f window => near-Hopf points are not grid-clipped.

Data: entrain.py (a,b) and entrain_crit.py (c). Run those first.
"""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
FIGS = os.environ.get("TN_FIGDIR") or os.path.join(os.path.dirname(HERE), "figures")
os.makedirs(FIGS, exist_ok=True)
NEBLUE = "#0a4f8c"; NERED = "#b3361f"; NEGREEN = "#1a9850"

for f in ("entrain.npz", "entrain_b.npz", "entrain_crit.npz"):
    if not os.path.exists(os.path.join(HERE, f)):
        raise SystemExit(f"{f} not found -- run entrain.py and entrain_crit.py first.")
A = np.load(os.path.join(HERE, "entrain.npz"))
Bd = np.load(os.path.join(HERE, "entrain_b.npz"))
Cd = np.load(os.path.join(HERE, "entrain_crit.npz"))

fig, ax = plt.subplots(1, 3, figsize=(13.6, 4.1))

# ---- (a) Arnold tongue: continuous lock-in + locked boundary -----------------
dfg, epsg = A["dfg"], A["epsg"]; lockin = A["lockin"].T   # -> (eps, df)
f0 = float(A["f0"])
pm = ax[0].pcolormesh(dfg, epsg, lockin, shading="gouraud", cmap="viridis")
# 1:1-locked boundary (from the binary mask), drawn as a contour
ax[0].contour(dfg, epsg, A["locked"].T, levels=[0.5], colors="w", linewidths=1.6)
ax[0].axvline(f0, ls=":", color="w", lw=1.2, alpha=0.8)
ax[0].text(f0, epsg[-1] * 0.97, r"$f_0$", color="w", ha="center", va="top", fontsize=10)
ax[0].text(0.03, 0.95, "1:1 locked\n(white contour)", transform=ax[0].transAxes,
           color="w", fontsize=8.5, va="top")
ax[0].set_xlabel(r"drive frequency $\Delta f$ (Hz)")
ax[0].set_ylabel(r"drive amplitude $\varepsilon$ (mV)")
ax[0].set_title("(a) 1:1 Arnold tongue (lock-in)")
cb = fig.colorbar(pm, ax=ax[0]); cb.set_label(r"lock-in $A_\Omega$ at $\Delta f$ (mV)")

# ---- (b) frequency locking ---------------------------------------------------
dfb, fd = Bd["dfb"], Bd["fd"]
locked_b = np.abs(fd - dfb) < 0.3
ax[1].plot(dfb, dfb, ls="--", color="0.6", lw=1.1, label=r"$f_{\rm out}=\Delta f$ (locked)")
ax[1].axhline(f0, ls=":", color=NERED, lw=1.2, label=r"$f_0$ (free cycle)")
ax[1].plot(dfb, fd, "-", color=NEBLUE, lw=1.0, alpha=0.5, zorder=2)
ax[1].plot(dfb[locked_b], fd[locked_b], "o", color=NEBLUE, ms=4.5, zorder=3, label="locked")
ax[1].plot(dfb[~locked_b], fd[~locked_b], "o", mfc="none", mec=NEBLUE, ms=4.5, zorder=3,
           label="unlocked")
ax[1].set_xlabel(r"drive frequency $\Delta f$ (Hz)")
ax[1].set_ylabel(r"output frequency $f_{\rm out}$ (Hz)")
ax[1].set_title(r"(b) frequency locking ($\varepsilon=%.1f$ mV)" % float(Bd["eps_b"]))
ax[1].legend(fontsize=7.5, frameon=False, loc="upper left")

# ---- (c) entrainment grows toward criticality --------------------------------
dist = Cd["pH"] - Cd["pg"]; lr = Cd["lock_range"]; amp0 = Cd["amp0"]
clip = Cd["clipped"] if "clipped" in Cd.files else np.zeros_like(lr, bool)
order = np.argsort(-dist)                      # far -> near Hopf
dist, lr, amp0, clip = dist[order], lr[order], amp0[order], clip[order].astype(bool)
ax[2].plot(dist, lr, "-", color=NEBLUE, lw=1.8, zorder=2)
ax[2].plot(dist[~clip], lr[~clip], "o", color=NEBLUE, ms=6, zorder=3, label="locking range")
if clip.any():                                 # honesty: mark grid-clipped lower bounds
    ax[2].plot(dist[clip], lr[clip], "^", mfc="none", mec=NEBLUE, ms=8, mew=1.5,
               zorder=3, label="clipped (lower bound)")
ax[2].set_xlabel(r"distance to Hopf  $p_{\rm Hopf}-p$")
ax[2].set_ylabel(r"1:1 locking range (Hz)", color=NEBLUE)
ax[2].tick_params(axis="y", labelcolor=NEBLUE)
ax[2].invert_xaxis()                            # Hopf (criticality) to the right
ax[2].set_title("(c) entrainment grows toward criticality")
ax[2].annotate("toward Hopf", xy=(0.97, 0.06), xytext=(0.55, 0.06),
               xycoords="axes fraction", fontsize=8, color="0.4",
               arrowprops=dict(arrowstyle="->", color="0.4"))
axr = ax[2].twinx()
axr.plot(dist, amp0, "s--", color=NERED, lw=1.4, ms=5, alpha=0.9)
axr.set_ylabel("autonomous cycle amplitude (mV)", color=NERED)
axr.tick_params(axis="y", labelcolor=NERED)
ax[2].legend(fontsize=7.5, frameon=False, loc="upper left")

fig.tight_layout()
for ext in ("pdf", "png"):
    fig.savefig(os.path.join(FIGS, f"fig_entrainment.{ext}"), dpi=150, bbox_inches="tight")
print("wrote fig_entrainment.{pdf,png} to", FIGS)
