import os, numpy as np, matplotlib
matplotlib.use("Agg"); import matplotlib.pyplot as plt
HERE=os.path.dirname(os.path.abspath(__file__))
FIGS=os.environ.get("TN_FIGDIR") or os.path.join(HERE, "..", "figures")
os.makedirs(FIGS, exist_ok=True)
M=np.load(os.path.join(HERE,"jcurve_main.npz")); R=np.load(os.path.join(HERE,"jcurve_res.npz"))
Cs,gam,w0,Acl,Aop,gain=M["C"],M["gamma"],M["w0"],M["Acl"],M["Aop"],M["gain"]
Chopf=float(M["Chopf"]); sig2=float(M["sig2"]); vstar=float(M["vstar"])
fdf=R["fdf"]; Csel=R["Csel"]
fig,ax=plt.subplots(1,3,figsize=(13.5,4.0))
# (a) THE J CURVE
ax[0].plot(Cs,Acl,'o-',color='#0a4f8c',lw=2,zorder=3)
ax[0].axvline(Chopf,ls='--',color='#b3361f',lw=1.3)
ax[0].text(Chopf-0.25,Acl.max()*0.5,'Hopf $C^*$',color='#b3361f',ha='right',rotation=90,fontsize=9)
ax[0].set_xlabel(r'network coupling $C\;(\equiv J)$'); ax[0].set_ylabel(r'demodulated $A_\Omega$ (mV)')
ax[0].set_title('(a) the $J$ curve'); ax[0].grid(alpha=.3)
ax[0].text(0.04,0.95,f"$v^*$ pinned\n$\\sigma''(v^*)={sig2:+.3f}$ (fixed)\n$A_{{\\rm open}}$ const",
           transform=ax[0].transAxes,fontsize=8,va='top',bbox=dict(fc='white',ec='0.7'))
# (b) resonance families sharpening
cols=plt.cm.viridis(np.linspace(0.12,0.82,len(Csel)))
# recompute gamma labels
import jr_jsweep_engine as E
for C,c in zip(Csel,cols):
    g=E.jac_eig(E.p_of_C(vstar,C),C)[1]
    ax[1].plot(fdf,R[f"res_{int(round(C*10))}"],color=c,lw=1.9,label=f"$C$={C:.0f} ($\\gamma$={g:.1f})")
ax[1].set_xlabel(r'envelope frequency $\Delta f$ (Hz)'); ax[1].set_ylabel(r'$A_\Omega$ (mV)')
ax[1].set_title(r'(b) resonance sharpens as $C\to C^*$'); ax[1].legend(fontsize=8); ax[1].grid(alpha=.3)
# (c) gain vs 1/gamma with 1/gamma guide
ax[2].loglog(1/gam,gain,'o-',color='#0a4f8c',lw=2,label='measured')
xg=np.array([1/gam.max(),1/gam.min()]); k=gain[3]*gam[3]
ax[2].loglog(xg,k*xg,'k--',lw=1,label=r'$\propto 1/\gamma$')
ax[2].set_xlabel(r'$1/\gamma$  (closeness to Hopf)'); ax[2].set_ylabel(r'network gain $A_\Omega/A_{\rm open}$')
ax[2].set_title(r'(c) gain $\propto 1/\gamma$, then saturates'); ax[2].legend(fontsize=8); ax[2].grid(alpha=.3,which='both')
plt.tight_layout()
plt.savefig(os.path.join(FIGS,"fig_jcurve.pdf"))
plt.savefig(os.path.join(FIGS,"fig_jcurve.png"),dpi=150)
print(f"saved fig_jcurve.{{pdf,png}} to {FIGS}")
