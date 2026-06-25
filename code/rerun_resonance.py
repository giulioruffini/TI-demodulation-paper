"""Higher-quality resonance sweep: longer settle (transients) + longer measure
(lock-in/beat resolution) + finer Omega grid near the peak.
Usage:  python3 rerun_resonance.py {stable|cycle|plot}
Split into stable/cycle calls to keep each run short."""
import sys, os, numpy as np
from jr_demod import integrate
FIGS = os.environ.get("TN_FIGDIR") or os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "figures")
os.makedirs(FIGS, exist_ok=True)

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
    import figstyle; figstyle.apply()
    S=np.load("sweep_hi_stable.npz")
    f=S["f_om"]; rs=S["rs"]; ps=S["p"]
    cols=["#1b3a6b","#2f7ec4","#9ec9e8"]
    # Single panel: the fixed-point (stable-focus) regime. The demodulated drive
    # forces a Lorentzian at f0 whose height grows as the Hopf is approached
    # (gain ~ 1/gamma). The above-Hopf / entrainment story is told with the
    # correct observable (f_out, Arnold tongue) in fig_entrainment.
    fig,ax=plt.subplots(1,2,figsize=(10.0,4.0),
                        gridspec_kw={"width_ratios":[2.1,1.0]})
    peaks=np.array([rs[i].max() for i in range(len(ps))])
    dist =ps-315.0                               # distance from Hopf (>0, stable side) ~ gamma
    for i,p in enumerate(ps):
        ax[0].plot(f,rs[i],color=cols[i],lw=2.2,
                   label=f"$p={p:.0f}$  (dist. to Hopf {p-315:.0f})")
    ax[0].axvline(F0,ls=":",c="0.5",lw=1)
    ax[0].set_xlabel("envelope frequency  $\\Omega/2\\pi$  (Hz)")
    ax[0].set_ylabel("demodulated response @ $\\Omega$  (mV)")
    ax[0].set_title("Forced resonance below the Hopf (stable focus)",fontsize=11)
    ax[0].legend(fontsize=8.5,frameon=False)
    ax[0].spines[["top","right"]].set_visible(False)
    # companion: peak height vs distance to Hopf -- the 1/gamma growth
    ax[1].plot(dist,peaks,"o-",color="#1b3a6b",lw=2,ms=7)
    for d,pk in zip(dist,peaks):
        ax[1].annotate(f"{pk:.2f}",(d,pk),textcoords="offset points",
                       xytext=(6,4),fontsize=8,color="#1b3a6b")
    ax[1].set_xlabel("distance to Hopf  $p-315$  ($\\propto\\gamma$)")
    ax[1].set_ylabel("peak response @ $f_0$  (mV)")
    ax[1].set_title("Peak grows as $p\\!\\to\\!315$",fontsize=11)
    ax[1].spines[["top","right"]].set_visible(False)
    ax[1].set_xlim(0,None); ax[1].set_ylim(0,None)
    fig.suptitle("Envelope demodulation $\\rightarrow$ alpha resonance in Jansen-Rit "
                 "(carrier $f_c=100$ Hz, AM input has NO power at $\\Omega$)",fontsize=11)
    fig.tight_layout(rect=[0,0,1,0.95])
    fig.savefig(f"{FIGS}/fig_resonance.png",dpi=300)
    fig.savefig(f"{FIGS}/fig_resonance.pdf")
    print("STABLE peaks:", [f"{rs[i].max():.3f}" for i in range(len(ps))])
    print("wrote fig_resonance (single regime: stable focus)")
