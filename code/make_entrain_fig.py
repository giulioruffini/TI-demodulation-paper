"""Frequency-dominance plots for the driven autonomous JR alpha cycle.

Panels show the lock-in amplitude and dominant-frequency screen, output frequency,
and the screen's width as the Hopf is approached. These statistics do not test
absence of phase drift. Data: entrain.py and entrain_crit.py; cache keys retain
historical names for compatibility.
"""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import figstyle; figstyle.apply()
import overlap

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

fig, ax = plt.subplots(1, 3, figsize=(10.2, 3.7))

# ---- (a) lock-in amplitude and dominant-frequency screen --------------------
dfg, epsg = A["dfg"], A["epsg"]; lockin = A["lockin"].T   # -> (eps, df)
f0 = float(A["f0"])
pm = ax[0].pcolormesh(dfg, epsg, lockin, shading="gouraud", cmap="viridis")
# Historical locked cache key: dominant-frequency screen, not a phase test.
ax[0].contour(dfg, epsg, A["locked"].T, levels=[0.5], colors="w", linewidths=1.6)
ax[0].axvline(f0, ls=":", color="w", lw=1.2, alpha=0.8)
ax[0].text(f0 + 0.2, epsg[-1] * 0.18, r"$f_0$", color="w", ha="left", va="bottom", fontsize=10)
ax[0].text(0.03, 0.95, "frequency dominance\n(white contour)", transform=ax[0].transAxes,
           color="w", fontsize=8.5, va="top")
ax[0].set_xlabel(r"drive frequency $\Delta f$ (Hz)")
ax[0].set_ylabel(r"drive amplitude $\varepsilon$ (mV)")
figstyle.panel(ax[0], "a")
cb = fig.colorbar(pm, ax=ax[0]); cb.set_label(r"$A_\Omega$ (mV)")

# ---- (b) output frequency  ---------------------------------------------------
dfb, fd = Bd["dfb"], Bd["fd"]
locked_b = np.abs(fd - dfb) < 0.3
ax[1].plot(dfb, dfb, ls="--", color="0.6", lw=1.1, label=r"$f_{\rm out}=\Delta f$")
ax[1].axhline(f0, ls=":", color=NERED, lw=1.2, label=r"$f_0$ (free cycle)")
ax[1].plot(dfb, fd, "-", color=NEBLUE, lw=1.0, alpha=0.5, zorder=2)
ax[1].plot(dfb[locked_b], fd[locked_b], "o", color=NEBLUE, ms=4.5, zorder=3, label="within screen")
ax[1].plot(dfb[~locked_b], fd[~locked_b], "o", mfc="none", mec=NEBLUE, ms=4.5, zorder=3,
           label="outside screen")
ax[1].set_xlabel(r"drive frequency $\Delta f$ (Hz)")
ax[1].set_ylabel(r"$f_{\rm out}$ (Hz)")
figstyle.panel(ax[1], "b")
ax[1].legend(fontsize=8.5, frameon=False, loc="upper left")

# ---- (c) dominance width toward criticality  --------------------------------
dist = Cd["pH"] - Cd["pg"]; lr = Cd["lock_range"]; amp0 = Cd["amp0"]
clip = Cd["clipped"] if "clipped" in Cd.files else np.zeros_like(lr, bool)
order = np.argsort(-dist)                      # far -> near Hopf
dist, lr, amp0, clip = dist[order], lr[order], amp0[order], clip[order].astype(bool)
ax[2].plot(dist, lr, "-", color=NEBLUE, lw=1.8, zorder=2)
ax[2].plot(dist[~clip], lr[~clip], "o", color=NEBLUE, ms=6, zorder=3, label="dominance width")
if clip.any():                                 # honesty: mark grid-clipped lower bounds
    ax[2].plot(dist[clip], lr[clip], "^", mfc="none", mec=NEBLUE, ms=8, mew=1.5,
               zorder=3, label="clipped (lower bound)")
ax[2].set_xlabel(r"distance to Hopf  $p_{\rm Hopf}-p$")
ax[2].set_ylabel(r"dominance width (Hz)", color=NEBLUE)
ax[2].tick_params(axis="y", labelcolor=NEBLUE)
ax[2].invert_xaxis()                            # Hopf (criticality) to the right
figstyle.panel(ax[2], "c")
axr = ax[2].twinx()
axr.plot(dist, amp0, "s--", color=NERED, lw=1.4, ms=5, alpha=0.9)
axr.set_ylabel("cycle amp. (mV)", color=NERED)
axr.tick_params(axis="y", labelcolor=NERED)

figstyle.thin_ticks(fig, n=5)
ax[1].set_xticks([8, 10, 12, 14])
ax[1].set_yticks([8, 10, 12, 14])
fig.tight_layout(w_pad=2.0)
figstyle.scale_text(fig, placed_frac=1, max_scale=1.8)
fig.tight_layout(w_pad=2.0)
for ext in ("pdf", "png"):
    overlap.check(fig, placed_frac=1, name="make_entrain_fig.py")
    fig.savefig(os.path.join(FIGS, f"fig_entrainment.{ext}"), dpi=300, bbox_inches="tight")
print("wrote fig_entrainment.{pdf,png} to", FIGS)
