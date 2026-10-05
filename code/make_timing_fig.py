"""Plotter for fig_timing_not_rate (Jansen-Rit): beat-locked modulation of the pyramidal
rate versus the shift of its mean, both read from the SAME observable r_P = Sigma(v + s)
in the same units (mHz), as the coupling drives the column toward the Hopf at pinned
detection. (2026-09-22: the rate read-out now includes the field; the earlier figure
compared an LFP lock-in in mV with a field-free rate mean.) Reads the genuine
two-tone sweep, timing_not_rate_twotone.npz.

  python3 timing_not_rate.py   # -> timing_not_rate.npz  (the C-sweep data)
  python3 timing_not_rate_twotone.py  # -> timing_not_rate_twotone.npz
  python3 make_timing_fig.py   # -> ../figures/fig_timing_not_rate.{png,pdf}
"""
import numpy as np, os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import figstyle; figstyle.apply()
import overlap

HERE = os.path.dirname(os.path.abspath(__file__))
FIGS = os.environ.get("TN_FIGDIR") or os.path.join(os.path.dirname(HERE), "figures")
os.makedirs(FIGS, exist_ok=True)
d = np.load(os.path.join(HERE, "timing_not_rate_twotone.npz"))
g = d["gam"]; AC = d["AC"]*1e3; DC = d["DC"]*1e3   # rate lock-in and mean shift, both in mHz
o = np.argsort(g)[::-1]                          # far-from-Hopf -> Hopf
g, AC, DC = g[o], AC[o], DC[o]

NEBLUE = figstyle.NEBLUE; NERED = figstyle.NERED
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9.4, 3.6))

# --- Panel a: raw AC (log) and DC (linear, twin) vs damping gamma ---
ax1.semilogy(g, AC, "o-", color=NEBLUE, lw=1.6, ms=4, label=r"beat-locked rate modulation at $\Delta f=f_0$")
ax1.semilogy(g, np.abs(DC), "s-", color=NERED, lw=1.4, ms=3.5, label=r"$|$mean-rate shift$|$")
kk = AC[0]*g[0]
ax1.semilogy(g, kk/g, "--", color=NEBLUE, lw=1.0, alpha=0.6, label=r"$\propto 1/\gamma$")
ax1.set_xlabel(r"damping $\gamma$ (s$^{-1}$) $\;\rightarrow$ Hopf")
ax1.set_ylabel(r"rate $r_P$: beat lock-in, $|$mean shift$|$  (mHz)")
ax1.invert_xaxis()
figstyle.panel(ax1, "a")
ax1.legend(loc="upper left", frameon=False)

# --- Panel b: gains normalized to the far-from-Hopf value, vs gamma (log-y) ---
ax2.semilogy(g, AC/AC[0], "o-", color=NEBLUE, lw=1.6, ms=4, label=r"beat-locked modulation")
ax2.semilogy(g, np.abs(DC)/np.abs(DC[0]), "s-", color=NERED, lw=1.4, ms=3.5,
             label=r"$|$mean-rate shift$|$")
ax2.semilogy(g, g[0]/g, "--", color="0.5", lw=1.0, label=r"$\propto 1/\gamma$")
ax2.axhline(1.0, color=NERED, lw=0.8, ls=":", alpha=0.6)
ax2.set_xlabel(r"damping $\gamma$ (s$^{-1}$) $\;\rightarrow$ Hopf")
ax2.set_ylabel("gain, normalized to far-from-Hopf")
ax2.invert_xaxis()
figstyle.panel(ax2, "b")
ax2.legend(loc="upper left", frameon=False)

fig.tight_layout()
figstyle.scale_text(fig, placed_frac=1.0)
overlap.check(fig, placed_frac=1.0, name="make_timing_fig.py")
for ext in ("pdf", "png"):
    fig.savefig(os.path.join(FIGS, f"fig_timing_not_rate.{ext}"), dpi=300, bbox_inches="tight")
print("wrote fig_timing_not_rate.pdf / .png")
print(f"  beat-locked modulation grows {AC[-1]/AC[0]:.1f}x ({AC[0]:.1f} -> {AC[-1]:.1f} mHz); "
      f"|mean-rate shift| grows {abs(DC[-1])/abs(DC[0]):.1f}x ({DC[0]:.2f} -> {DC[-1]:.2f} mHz); "
      f"ratio AC/|DC| from {AC[0]/abs(DC[0]):.0f} to {AC[-1]/abs(DC[-1]):.0f} (max {np.max(AC/np.abs(DC)):.0f}); "
      f"gamma {g[0]:.2f}->{g[-1]:.3f}; baseline rate {float(d['rate_off'])*1e3:.0f} mHz")
