"""Two-tone kHz control figure: a real TI waveform at a real TI carrier.

Renders the saved khz_twotone.npz run -- two genuine tones at 1994.5/2005.5 Hz
through the fast-element filter (tau = 0.2 ms) into the recurrent JR column.
"""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import figstyle
figstyle.apply()
import overlap
from matplotlib.ticker import LogLocator, NullFormatter

NEBLUE, NERED, NEGRAY = figstyle.NEBLUE, figstyle.NERED, figstyle.NEGRAY
HERE = os.path.dirname(os.path.abspath(__file__))
FIGS = os.environ.get("TN_FIGDIR") or os.path.join(HERE, "..", "figures")

d = np.load(os.path.join(HERE, "khz_twotone.npz"))
fI, PI, fV, PV = d["fI"], d["PI"], d["fV"], d["PV"]
f1, f2, F0 = float(d["f1"]), float(d["f2"]), float(d["F0"])

fig, ax = plt.subplots(1, 2, figsize=(11.0, 3.9))

ax[0].semilogy(fI, PI + 1e-16, color=NEGRAY, lw=1.2)
ax[0].set_xlim(1900, 2100)
ax[0].set_ylim(1e-14, 3)
ax[0].axvline(f1, color=NEGRAY, ls="--", lw=0.6, alpha=0.5)
ax[0].axvline(f2, color=NEGRAY, ls="--", lw=0.6, alpha=0.5)
ax[0].set_xlabel("frequency (Hz)")
ax[0].set_ylabel("input power")
figstyle.panel(ax[0], "a")

ax[1].semilogy(fV, PV + 1e-16, color=NEBLUE, lw=1.2)
ax[1].set_xlim(0, 60)
ax[1].set_ylim(1e-8, 1)
ax[1].axvspan(8, 14, color=NERED, alpha=0.13)
ax[1].set_xlabel("frequency (Hz)")
ax[1].set_ylabel("output power")
ax[1].annotate(f"demodulated\n{F0:.1f} Hz line", xy=(F0, PV[np.argmin(np.abs(fV - F0))]),
               xytext=(26, 3e-3), fontsize=8, color=NEBLUE,
               arrowprops=dict(arrowstyle="->", color=NEBLUE, lw=0.8))
figstyle.panel(ax[1], "b")

for a in ax:
    a.yaxis.set_minor_locator(LogLocator(subs=()))
    a.yaxis.set_minor_formatter(NullFormatter())

fig.tight_layout(w_pad=3.5)
figstyle.thin_ticks(fig)
figstyle.scale_text(fig, placed_frac=1)
overlap.check(fig, placed_frac=1, name="make_khz_twotone_fig.py")
fig.savefig(f"{FIGS}/fig_khz_twotone.png", dpi=300)
fig.savefig(f"{FIGS}/fig_khz_twotone.pdf")
band = (fI > 8) & (fI < 14)
print(f"  input 8-14 Hz max power : {PI[band].max():.3e}")
print(f"  output line at {fV[np.argmin(np.abs(fV-F0))]:.2f} Hz : {PV[np.argmin(np.abs(fV-F0))]:.3e}")
print("  wrote fig_khz_twotone")
