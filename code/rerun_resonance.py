"""Higher-quality resonance sweep: longer settle (transients) + longer measure
(lock-in/beat resolution) + finer Omega grid near the peak.
Usage:  python3 rerun_resonance.py {stable|cycle|plot}
Split into stable/cycle calls to keep each run short."""
import sys, numpy as np
from jr_demod import integrate

F0=11.1; fc=100.0; m=1.0; eps=0.3; dt=2e-4
T_SET, T_MEA = 10.0, 20.0                     # 10 s settle, 20 s measure (long lock-in)
# finer grid concentrated near the resonance
f_om = np.unique(np.concatenate([np.arange(9.5,12.501,0.10),
                                 np.arange(10.6,11.601,0.03)]))
Om   = 2*np.pi*f_om
P_STABLE=[330.,355.,395.]; P_CYCLE=[310.,290.,265.]

def sweep(plist):
    out={}
    for p in plist:
        pv=np.full_like(Om,p)
        out[p]=integrate(pv,Om,eps,m,fc,T_SET,T_MEA,dt)
        print(f"  p={p:.0f}  peak={out[p].max():.3f} mV @ {f_om[out[p].argmax()]:.2f} Hz")
    return np.array([out[p] for p in plist])

mode=sys.argv[1] if len(sys.argv)>1 else "plot"
if mode=="stable":
    print("stable side:"); np.savez("sweep_hi_stable.npz", f_om=f_om, rs=sweep(P_STABLE), p=P_STABLE)
elif mode=="cycle":
    print("cycle side:");  np.savez("sweep_hi_cycle.npz",  f_om=f_om, rc=sweep(P_CYCLE),  p=P_CYCLE)
elif mode=="plot":
    import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
    S=np.load("sweep_hi_stable.npz"); C=np.load("sweep_hi_cycle.npz")
    f=S["f_om"]; rs=S["rs"]; rc=C["rc"]; ps=S["p"]; pc=C["p"]
    NEB="#1b3a6b"; cols=["#1b3a6b","#2f7ec4","#9ec9e8"]; cols2=["#7a1f1f","#c44","#e8a0a0"]
    fig,ax=plt.subplots(1,2,figsize=(11,4.3))
    for i,p in enumerate(ps):
        ax[0].plot(f,rs[i],color=cols[i],lw=2,label=f"p={p:.0f}  (dist. to Hopf {p-315:.0f})")
    ax[0].set_title("Stable focus (below Hopf): forced resonance",fontsize=11)
    for i,p in enumerate(pc):
        ax[1].plot(f,rc[i],color=cols2[i],lw=2,label=f"p={p:.0f}  (dist. to Hopf {p-315:.0f})")
    ax[1].set_title("Limit cycle (above Hopf): entrainment",fontsize=11)
    for a in ax:
        a.axvline(F0,ls=":",c="0.5",lw=1); a.set_xlabel("envelope frequency  $\\Omega/2\\pi$  (Hz)")
        a.set_ylabel("demodulated response @ $\\Omega$  (mV)")
        a.legend(fontsize=8,frameon=False); a.spines[["top","right"]].set_visible(False)
    fig.suptitle("Envelope demodulation $\\rightarrow$ alpha resonance in Jansen-Rit "
                 "(carrier $f_c=100$ Hz, AM input has NO power at $\\Omega$)",fontsize=11)
    fig.tight_layout(rect=[0,0,1,0.95])
    fig.savefig("../paper/figures/fig_resonance.png",dpi=150)
    fig.savefig("../paper/figures/fig_resonance.pdf")
    print("STABLE peaks:", [f"{rs[i].max():.3f}" for i in range(len(ps))])
    print("CYCLE  peaks:", [f"{rc[i].max():.3f}" for i in range(len(pc))])
    print("wrote fig_resonance")
