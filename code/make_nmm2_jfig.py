"""Plotter for fig_nmm2_jcurve (NMM2 PING coupling sweep / "J curve").
Reads nmm2_jcD.npz (nmm2_jcD.py) and the critical-mode/linear-gain/re-measured table\ndocs/landau1_nmm2_jcurve_modes_2026-10-05.json (nmm2_jcurve_modes.py --sim), and writes
fig_nmm2_jcurve.{png,pdf} into ../figures/. Run from the code/ directory:

    python3 nmm2_jcA.py        # (engine, imported by nmm2_jcD.py)
    python3 nmm2_jcD.py        # -> nmm2_jcD.npz  (resonance-peak grid)
    python3 make_nmm2_jfig.py  # -> ../figures/fig_nmm2_jcurve.{png,pdf}

Companion to make_jfig.py (the Jansen-Rit J-curve plotter)."""
import os, numpy as np, matplotlib
matplotlib.use("Agg"); import matplotlib.pyplot as plt
import figstyle; figstyle.apply()
import overlap

HERE = os.path.dirname(os.path.abspath(__file__))
NPZ  = os.path.join(HERE, "nmm2_jcD.npz")
FIGDIR = os.environ.get("TN_FIGDIR") or os.path.join(HERE, "..", "figures"); os.makedirs(FIGDIR, exist_ok=True)
if not os.path.exists(NPZ):
    raise SystemExit("nmm2_jcD.npz not found -- run nmm2_jcD.py first.")

d = np.load(NPZ)
C, Chopf = d["C"], float(d["Chopf"])
import json
M = json.load(open(os.path.join(HERE, "..", "docs", "landau1_nmm2_jcurve_modes_2026-10-05.json")))
gc = np.array(M["gam_crit"]); sim = np.array(M["simpk"]); G = np.array(M["Gpk_src"]); fG = np.array(M["fGpk_src"])
crit = np.array(M["crit"], bool)                         # response peak carried by the critical mode (producer field)
mid = (C > 14.5) & (C < 16.0)
Glin = G * np.median(sim[mid] / G[mid])                  # linear response, scaled to the measured gain away from the Hopf

fig, ax = plt.subplots(1, 2, figsize=(9.4, 4.0))
# (a) the NMM2 J curve
ax[0].plot(C, sim*1e3, 'o-', color='#0a4f8c', lw=2, label='simulated peak')
ax[0].plot(C, Glin*1e3, '-', color='0.45', lw=1.2, label='linear response')
ax[0].axvline(Chopf, ls='--', color='#b3361f', lw=1.3)
ax[0].text(Chopf-0.04, Glin.max()*1e3*0.97, 'gamma\nHopf $J^*$', color='#b3361f',
           ha='right', va='top', fontsize=9)
ax[0].set_xlabel(r'inter-QIF coupling $J\;(=C)$')
ax[0].set_ylabel(r'peak demodulated $A_\Omega$ ($r_E$, $\times10^{-3}$)')
figstyle.panel(ax[0], "a"); ax[0].grid(alpha=.3); ax[0].legend(fontsize=8, loc='upper left')
# (b) gain against the critical mode's damping
x = 1/gc
hi = crit & (C > 16.2); lo = crit & ~hi
ax[1].loglog(x[hi], sim[hi]*1e3, 'o-', color='#0a4f8c', lw=2, label='simulated, critical mode')
ax[1].loglog(x[lo], sim[lo]*1e3, 'o-', color='#0a4f8c', lw=2)
ax[1].loglog(x[~crit], sim[~crit]*1e3, 'o', mfc='white', color='#0a4f8c', label='simulated, 55 Hz mode')
ax[1].loglog(x, Glin*1e3, '-', color='0.45', lw=1.2, label='linear response')
xg = np.array([x[hi].min()/1.6, x.max()]); k = Glin[-1]*gc[-1]   # anchored where the critical mode dominates
ax[1].loglog(xg, k*xg*1e3, 'k--', lw=1, label=r'$\propto 1/\gamma$')
ax[1].set_xlabel(r'$1/\gamma$ of the critical mode (ms)')
ax[1].set_ylabel(r'peak $A_\Omega$ ($\times10^{-3}$)')
figstyle.panel(ax[1], "b")
ax[1].legend(fontsize=7); ax[1].grid(alpha=.3, which='both')

# log minor ticks collide once the type is enlarged: label decades only
from matplotlib.ticker import LogLocator, NullFormatter, MaxNLocator
ax[0].xaxis.set_major_locator(MaxNLocator(5))
for a in (ax[1].xaxis, ax[1].yaxis):
    a.set_major_locator(LogLocator(base=10.0))
    a.set_minor_formatter(NullFormatter())
plt.tight_layout(w_pad=2.5)
figstyle.scale_text(plt.gcf(), placed_frac=0.92)
plt.savefig(os.path.join(FIGDIR, "fig_nmm2_jcurve.png"), dpi=300)
plt.savefig(os.path.join(FIGDIR, "fig_nmm2_jcurve.pdf"))
print("wrote", os.path.join(FIGDIR, "fig_nmm2_jcurve.{png,pdf}"))
