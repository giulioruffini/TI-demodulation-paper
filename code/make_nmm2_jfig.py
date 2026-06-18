"""Plotter for fig_nmm2_jcurve (NMM2 PING coupling sweep / "J curve").
Reads the committed data nmm2_jcD.npz (produced by nmm2_jcD.py) and writes
fig_nmm2_jcurve.{png,pdf} into ../figures/. Run from the code/ directory:

    python3 nmm2_jcA.py        # (engine, imported by nmm2_jcD.py)
    python3 nmm2_jcD.py        # -> nmm2_jcD.npz  (resonance-peak grid)
    python3 make_nmm2_jfig.py  # -> ../figures/fig_nmm2_jcurve.{png,pdf}

Companion to make_jfig.py (the Jansen-Rit J-curve plotter)."""
import os, numpy as np, matplotlib
matplotlib.use("Agg"); import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
NPZ  = os.path.join(HERE, "nmm2_jcD.npz")
FIGDIR = os.environ.get("TN_FIGDIR") or os.path.join(HERE, "..", "figures"); os.makedirs(FIGDIR, exist_ok=True)
if not os.path.exists(NPZ):
    raise SystemExit("nmm2_jcD.npz not found -- run nmm2_jcD.py first.")

d = np.load(NPZ)
C, gam, peak, Chopf = d["C"], d["gamma"], d["peak"], float(d["Chopf"])

fig, ax = plt.subplots(1, 2, figsize=(9.4, 4.0))
# (a) the NMM2 J curve
ax[0].plot(C, peak*1e3, 'o-', color='#0a4f8c', lw=2)
ax[0].axvline(Chopf, ls='--', color='#b3361f', lw=1.3)
ax[0].text(Chopf-0.05, peak.max()*1e3*0.5, 'gamma Hopf $J^*$', color='#b3361f',
           ha='right', rotation=90, fontsize=9)
ax[0].set_xlabel(r'inter-QIF coupling $J\;(=C)$')
ax[0].set_ylabel(r'peak demodulated $A_\Omega$ ($r_E$, $\times10^{-3}$)')
ax[0].set_title('(a) NMM2 $J$ curve (exact mean field)'); ax[0].grid(alpha=.3)
ax[0].text(0.04, 0.95,
           "rectifier = exact $v_E^2$\n(quadratic coeff = 2, fixed)\n"
           "$J$ = literal QIF coupling\n$\\bar\\eta=0$, resonance peak",
           transform=ax[0].transAxes, fontsize=7.5, va='top',
           bbox=dict(fc='white', ec='0.7'))
# (b) gain ~ 1/gamma, saturating
ax[1].loglog(1/gam, peak*1e3, 'o-', color='#0a4f8c', lw=2, label='measured')
xg = np.array([1/gam.max(), 1/gam.min()]); k = (peak[7]*1e3)*gam[7]
ax[1].loglog(xg, k*xg, 'k--', lw=1, label=r'$\propto 1/\gamma$')
ax[1].set_xlabel(r'$1/\gamma$  (closeness to gamma Hopf)')
ax[1].set_ylabel(r'peak $A_\Omega$ ($\times10^{-3}$)')
ax[1].set_title(r'(b) amplification $\propto 1/\gamma$, saturating')
ax[1].legend(fontsize=8); ax[1].grid(alpha=.3, which='both')

plt.tight_layout()
plt.savefig(os.path.join(FIGDIR, "fig_nmm2_jcurve.png"), dpi=135)
plt.savefig(os.path.join(FIGDIR, "fig_nmm2_jcurve.pdf"))
print("wrote", os.path.join(FIGDIR, "fig_nmm2_jcurve.{png,pdf}"))
