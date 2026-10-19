"""Fig. 8: envelope and quadratic maps in a realistic head (Sec. 4.5).

IXI002, Violante et al. (2023) montage, native FreeSurfer hippocampal label.
(a-d) The four maps on the sagittal plane through the hippocampal centroid at
1:1 and 1:3, each column on one color scale (its gray-matter p99 at 1:1).
(e) Target-to-cortex ratio over the current-ratio sweep. (f) Focus shift along
the hippocampal long axis relative to 1:1. (g) The isotropic comparison.
Data: fem_quadmaps.py (fem_quadmaps.npz, fem_quadmaps.json); no simulation
runs here.
"""
import json
import os

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import matplotlib.patheffects as pe
import figstyle; figstyle.apply()

HERE = os.path.dirname(os.path.abspath(__file__))
FIGS = os.environ.get("TN_FIGDIR") or os.path.join(os.path.dirname(HERE), "figures")
os.makedirs(FIGS, exist_ok=True)
for f in ("fem_quadmaps.npz", "fem_quadmaps.json"):
    if not os.path.exists(os.path.join(HERE, f)):
        raise SystemExit(f"{f} not found -- run fem_quadmaps.py first.")
D = np.load(os.path.join(HERE, "fem_quadmaps.npz"))
R = json.load(open(os.path.join(HERE, "fem_quadmaps.json"), encoding="utf-8"))

ORDER = ["env", "quad", "msp", "iso"]
NAME = {"env": r"$\mathcal{M}[\mathcal{A}]$", "quad": r"$\mathcal{M}[\mathcal{A}^2/2]$",
        "msp": r"$\mathcal{I}$", "iso": r"isotropic $\mathcal{M}[\mathcal{A}^2/2]$"}
UNIT = {"env": "mV", "quad": r"mV$^2$", "msp": r"mV$^2$", "iso": r"mV$^2$"}
COLOR = {"env": figstyle.NEBLUE, "quad": figstyle.NERED, "msp": figstyle.NEGREEN,
         "iso": figstyle.NEGRAY}
GOLD = "#ffd166"
share = D["share"]
S11, S13 = 0.5, 0.75

# Size the canvas so the equal-aspect slices fill their cells (inches throughout).
t1 = D["slice_t1"]
W, LEFT, RIGHT, BOT, TOP = 10.4, 0.08, 0.98, 0.07, 0.95
WS = 0.06
ph = W * (RIGHT - LEFT) / (4 + 3 * WS) * t1.shape[0] / t1.shape[1]
rows_top = [ph, ph, 0.13]
top_h = sum(rows_top) + WS * 2 * np.mean(rows_top)
bot_h, gap = 2.9, 0.85
fig = plt.figure(figsize=(W, (top_h + gap + bot_h) / (TOP - BOT)))
outer = fig.add_gridspec(2, 1, height_ratios=[top_h, bot_h], hspace=gap / np.mean([top_h, bot_h]),
                         left=LEFT, right=RIGHT, bottom=BOT, top=TOP)
top = outer[0].subgridspec(3, 4, height_ratios=rows_top, hspace=WS, wspace=WS)
bottom = outer[1].subgridspec(1, 3, width_ratios=[1.75, 1.15, 1.2], wspace=0.42)
LETTER = dict(color="w", fontsize=8, fontweight="bold",
              path_effects=[pe.withStroke(linewidth=1.6, foreground="k")])

# ---- (a-d) maps on the sagittal plane -----------------------------------------
hip, brain = D["slice_hip"], D["slice_brain"]
lo, hi = np.percentile(t1[t1 > 0], (1, 99.5))
for j, k in enumerate(ORDER):
    vmax = float(D["gm_p99_1to1"][j])
    for i, cond in enumerate(("1:1", "1:3")):
        ax = fig.add_subplot(top[i, j])
        ax.imshow(t1, cmap="gray", origin="lower", vmin=lo, vmax=hi, interpolation="nearest")
        v = np.ma.masked_where(~brain.astype(bool) | ~np.isfinite(D["slice_maps"][2 * j + i]),
                               D["slice_maps"][2 * j + i])
        im = ax.imshow(v, cmap="viridis", origin="lower", vmin=0, vmax=vmax,
                       interpolation="nearest")
        ax.contour(hip, [0.5], colors=GOLD, linewidths=0.9)
        p11, p13 = D["slice_foci_1to1"][j], D["slice_foci_1to3"][j]
        ax.plot(*p11, "o", mfc="none", mec="w", ms=5, mew=1.1)
        if i == 1:
            ax.plot(*p13, "^", mfc="w", mec="k", ms=5, mew=0.5)
        ax.set_xticks([]); ax.set_yticks([])
        for s in ax.spines.values():
            s.set_visible(False)
        if j == 0:
            ax.set_ylabel(f"{cond}\n" + ("2 + 2 mA" if cond == "1:1" else "1 + 3 mA"))
            ax.text(0.03, 0.95, "A", transform=ax.transAxes, va="top", **LETTER)
            ax.text(0.97, 0.95, "P", transform=ax.transAxes, va="top", ha="right", **LETTER)
        if i == 0:
            ax.set_title(NAME[k], fontsize=10.5, loc="right" if k == "iso" else "center")
            figstyle.panel(ax, "abcd"[j])
    cb = fig.colorbar(im, cax=fig.add_subplot(top[2, j]), orientation="horizontal")
    cb.set_label(UNIT[k], labelpad=1)
    cb.ax.tick_params(labelsize=7.5)
    cb.ax.xaxis.set_major_locator(matplotlib.ticker.MaxNLocator(4))
    cb.set_ticks([t for t in cb.ax.get_xticks() if 0 <= t <= vmax])

# ---- (e) target-to-cortex ratio over the sweep ---------------------------------
ax = fig.add_subplot(bottom[0])
for k in ("env", "quad", "msp"):
    ax.plot(share, D[f"{k}__tc_p95"], "-", color=COLOR[k], label=NAME[k])
    if k != "env":
        ax.plot(share, D[f"{k}__tc_p95_degree_matched"], "--", color=COLOR[k], lw=1.3)
for x in (S11, S13):
    ax.axvline(x, color="0.6", ls=":", lw=1.0)
ax.axhline(1.0, color="0.75", lw=0.8)
ax.text(S11, 1.0, " 1:1", color="0.4", fontsize=8, va="bottom", ha="left",
        transform=ax.get_xaxis_transform())
ax.text(S13, 1.0, " 1:3", color="0.4", fontsize=8, va="bottom", ha="left",
        transform=ax.get_xaxis_transform())
ax.set_xlabel("posterior current fraction")
ax.set_ylabel("target / reference (p95)")
handles = [Line2D([], [], color=COLOR[k], label=NAME[k]) for k in ("env", "quad", "msp")]
handles.append(Line2D([], [], color="0.3", ls="--", lw=1.3, label=r"degree-matched ($\sqrt{\cdot}$)"))
ax.legend(handles=handles, loc="upper right", ncol=2, columnspacing=1.0)
ax.set_xlim(share[0], share[-1])
ax.set_ylim(0.76, 1.36)
ax.set_xticks([0.1, 0.3, 0.5, 0.7, 0.9])
ax.set_yticks([0.8, 1.0, 1.2])
figstyle.panel(ax, "e")

# ---- (f) focus displacement along the long axis --------------------------------
ax = fig.add_subplot(bottom[1])
for k in ("env", "quad", "msp"):
    band = np.vstack([D[f"{k}__disp_axis_top{t}_mm"] for t in (5, 10, 25, 50)])
    ax.fill_between(share, band.min(axis=0), band.max(axis=0), color=COLOR[k], alpha=0.15, lw=0)
    ax.plot(share, D[f"{k}__disp_axis_top10_mm"], "-", color=COLOR[k])
for x in (S11, S13):
    ax.axvline(x, color="0.6", ls=":", lw=1.0)
ax.axhline(0.0, color="0.75", lw=0.8, zorder=0)
ax.set_xlabel("posterior current fraction")
ax.set_ylabel("focus shift from 1:1 (mm)")
ax.text(0.03, 0.97, "anterior", transform=ax.transAxes, va="top", color="0.4", fontsize=8)
ax.text(0.97, 0.03, "posterior", transform=ax.transAxes, ha="right", color="0.4", fontsize=8)
ax.set_xlim(share[0], share[-1])
ax.set_xticks([0.2, 0.4, 0.6, 0.8])
ax.set_yticks([-8, -4, 0, 4])
figstyle.panel(ax, "f")

# ---- (g) isotropic comparison ---------------------------------------------------
ax = fig.add_subplot(bottom[2])
c11 = R["conditions"]["1:1"]
bars = [("env", c11["env"]["tc_p95"], c11["env"]["tc_p95"]),
        ("quad", c11["quad"]["tc_p95"], c11["quad"]["degree_matched"]["tc_p95"]),
        ("iso", c11["iso"]["tc_p95"], c11["iso"]["degree_matched"]["tc_p95"])]
x = np.arange(len(bars))
ax.bar(x[0], bars[0][1], 0.52, color=COLOR["env"])
ax.bar(x[1:] - 0.19, [b[1] for b in bars[1:]], 0.36,
       color=[COLOR[b[0]] for b in bars[1:]])
ax.bar(x[1:] + 0.19, [b[2] for b in bars[1:]], 0.36, color="w", hatch="////",
       edgecolor=[COLOR[b[0]] for b in bars[1:]], lw=1.0)
ax.axhline(1.0, color="0.75", lw=0.8)
ax.set_xticks(x, [r"$\mathcal{M}[\mathcal{A}]$" + "\nalong " + r"$\mathbf{n}^*$",
                  r"$\mathcal{M}[\mathcal{A}^2/2]$" + "\nalong " + r"$\mathbf{n}^*$",
                  r"$\mathcal{M}[\mathcal{A}^2/2]$" + "\nisotropic"])
ax.tick_params(axis="x", labelsize=7.5)
ax.set_ylabel("target / reference (p95)")
ax.set_ylim(0, 1.6)
ax.set_yticks([0, 0.4, 0.8, 1.2, 1.6])
ax.legend(handles=[plt.Rectangle((0, 0), 1, 1, color="0.4", label="raw"),
                   plt.Rectangle((0, 0), 1, 1, fc="w", ec="0.4", hatch="////",
                                 label="degree-matched")], loc="upper center",
          bbox_to_anchor=(0.55, 1.02), ncol=2, handlelength=1.2, columnspacing=0.8)
figstyle.panel(ax, "g")

# Materialize tick labels before sizing text for the final printed width.
fig.canvas.draw()
figstyle.scale_text(fig, placed_frac=1.0)
fig.savefig(os.path.join(FIGS, "fig_fem.pdf"), metadata={"CreationDate": None})   # reruns byte-identical
fig.savefig(os.path.join(FIGS, "fig_fem.png"))
print("wrote", os.path.join(FIGS, "fig_fem.pdf"))
