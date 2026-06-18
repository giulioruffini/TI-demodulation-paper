"""Plotter for fig_timing_not_rate ('timing, not rate', Jansen-Rit): the AC
envelope-locked response is resonantly amplified ~1/gamma toward the Hopf while the DC
mean-rate shift stays flat. Reads timing_not_rate.npz (run timing_not_rate.py first).

  python3 timing_not_rate.py   # -> timing_not_rate.npz  (the C-sweep data)
  python3 make_timing_fig.py   # -> ../figures/fig_timing_not_rate.{png,pdf}
"""
import numpy as np, os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import figstyle; figstyle.apply()

HERE = os.path.dirname(os.path.abspath(__file__))
FIGS = os.environ.get("TN_FIGDIR") or os.path.join(os.path.dirname(HERE), "figures")
os.makedirs(FIGS, exist_ok=True)
d = np.load(os.path.join(HERE, "timing_not_rate.npz"))
g = d["gam"]; AC = d["AC"]; DC = d["DC"]*1e3   # DC in mHz
o = np.argsort(g)[::-1]                          # far-from-Hopf -> Hopf
g, AC, DC = g[o], AC[o], DC[o]

NEBLUE = figstyle.NEBLUE; NERED = figstyle.NERED
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9.4, 3.6))

# --- Panel a: raw AC (log) and DC (linear, twin) vs damping gamma ---
ax1.semilogy(g, AC, "o-", color=NEBLUE, lw=1.6, ms=4, label=r"AC at $\Delta f=f_0$")
kk = AC[0]*g[0]
ax1.semilogy(g, kk/g, "--", color=NEBLUE, lw=1.0, alpha=0.6, label=r"$\propto 1/\gamma$")
ax1.set_xlabel(r"damping $\gamma$  (distance to Hopf) $\;\rightarrow$ Hopf")
ax1.set_ylabel(r"AC lock-in $A_\Omega$ at $\Delta f$  (mV)", color=NEBLUE)
ax1.invert_xaxis()
ax1.tick_params(axis="y", labelcolor=NEBLUE)
axr = ax1.twinx()
axr.plot(g, DC, "s-", color=NERED, lw=1.4, ms=3.5)
axr.set_ylabel(r"DC mean-rate shift $\Delta\bar r$  (mHz)", color=NERED)
axr.tick_params(axis="y", labelcolor=NERED)
axr.set_ylim(-6, 8)
ax1.set_title("(a) timing entrains, rate does not", fontsize=9)
ax1.legend(loc="upper left", frameon=False)

# --- Panel b: gains normalized to the far-from-Hopf value, vs gamma (log-y) ---
ax2.semilogy(g, AC/AC[0], "o-", color=NEBLUE, lw=1.6, ms=4, label=r"AC at $\Delta f$ (timing)")
ax2.semilogy(g, np.abs(DC)/np.abs(DC[0]), "s-", color=NERED, lw=1.4, ms=3.5,
             label=r"$|$DC mean rate$|$")
ax2.semilogy(g, g[0]/g, "--", color="0.5", lw=1.0, label=r"$\propto 1/\gamma$")
ax2.axhline(1.0, color=NERED, lw=0.8, ls=":", alpha=0.6)
ax2.set_xlabel(r"damping $\gamma$  (distance to Hopf) $\;\rightarrow$ Hopf")
ax2.set_ylabel("gain, normalized to far-from-Hopf")
ax2.invert_xaxis()
ax2.set_title("(b) AC gain $\\sim 1/\\gamma$ (saturating); DC flat", fontsize=9)
ax2.legend(loc="upper left", frameon=False)

fig.tight_layout()
for ext in ("pdf", "png"):
    fig.savefig(os.path.join(FIGS, f"fig_timing_not_rate.{ext}"), dpi=300, bbox_inches="tight")
print("wrote fig_timing_not_rate.pdf / .png")
print(f"  AC grows {AC[-1]/AC[0]:.1f}x; DC stays within "
      f"[{DC.min():.2f}, {DC.max():.2f}] mHz over gamma {g[0]:.2f}->{g[-1]:.3f}")
