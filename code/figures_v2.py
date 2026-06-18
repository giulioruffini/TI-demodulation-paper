"""v2 figures: concept schematic, bifurcation+sigmoid, 2-D map,
carrier independence (+ synapse transfer function), operating-point law."""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
from jr_demod import Sigm, Sigm1, Sigm2, A, a, v0, e0, r
import os, figstyle; figstyle.apply()
FIGS = os.environ.get("TN_FIGDIR") or os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "figures")
os.makedirs(FIGS, exist_ok=True)

NEB=figstyle.NEBLUE; NEB2="#2f7ec4"; NEL=figstyle.NEBLUE_L; NER=figstyle.NERED; GR=figstyle.NEGRAY
d = np.load("analyses_v2.npz")

# ============================================================== FIG 1: concept
def concept():
    fig = plt.figure(figsize=(11.5, 4.4)); ax = fig.add_axes([0,0,1,1]); ax.axis("off")
    ax.set_xlim(0,100); ax.set_ylim(0,44)
    stages = [
        (4 , "AM field  $s(t)$", "carrier $f_c$\nenvelope $\\Omega$", NEL),
        (30, "Nonlinear detector", "firing-rate sigmoid\n$\\sigma(v)$,  curvature $\\sigma''$", NEB2),
        (56, "Tuned resonator", "2nd-order synapses\nnear Hopf,  $f_0$", NEB2),
        (82, "Demodulated\noutput @ $\\Omega$", "alpha rhythm\nrecovered", NEL),
    ]
    w=16; h=12; y=14
    for x,title,sub,col in stages:
        ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle="round,pad=0.4,rounding_size=1.2",
                     fc=col, ec=NEB, lw=1.6, alpha=0.9))
        ax.text(x+w/2, y+h-3.2, title, ha="center", va="center", fontsize=10.5,
                weight="bold", color="white" if col==NEB2 else NEB)
        ax.text(x+w/2, y+3.4, sub, ha="center", va="center", fontsize=8.2,
                color="white" if col==NEB2 else "#0a3050")
    for x0 in [4+w, 30+w, 56+w]:
        ax.add_patch(FancyArrowPatch((x0+0.4,y+h/2),(x0+3.6,y+h/2),
                     arrowstyle="-|>", mutation_scale=16, lw=2, color=GR))
    # radio analogy strip
    ax.text(50,41,"The cortical column as an AM radio receiver",ha="center",
            fontsize=12, weight="bold", color=NEB)
    analog=["RF signal","square-law /\ndiode detector","RLC tank\n(tuned)","audio (message)"]
    for (x,_,_,_),lab in zip(stages,analog):
        ax.text(x+w/2, y-3.0, lab, ha="center", va="center", fontsize=8,
                style="italic", color=GR)
    # mini waveforms above boxes: AM -> rectified -> filtered -> recovered envelope
    def wav(xc, kind, tag):
        axx=fig.add_axes([xc/100-0.066, 0.69, 0.13, 0.17]); axx.axis("off")
        tt=np.linspace(0,1,500); env=1+0.8*np.cos(2*np.pi*2*tt); am=env*np.cos(2*np.pi*22*tt)
        if   kind=="am":     s=am
        elif kind=="rect":   s=am**2                                   # detector output (rectified)
        elif kind=="ripple": s=np.cos(2*np.pi*2*tt)+0.16*np.cos(2*np.pi*22*tt)  # post-tank
        else:                s=np.cos(2*np.pi*2*tt)                    # recovered envelope
        axx.plot(tt,s,color=NEB,lw=1.0); axx.margins(y=0.15)
        axx.set_title(tag, fontsize=7.5, color=GR, pad=1)
    wav(12,"am","AM field"); wav(38,"rect","rectified"); wav(64,"ripple","filtered"); wav(90,"sine","envelope @ $\\Omega$")
    fig.savefig(f"{FIGS}/fig_concept.png",dpi=300); fig.savefig(f"{FIGS}/fig_concept.pdf")
    print("wrote fig_concept")

# ============================================ FIG 2: bifurcation + sigmoid/sigma''
def bifurcation_sigmoid():
    fig, ax = plt.subplots(1, 2, figsize=(11, 4.0))
    pb=d["p_bif"]; vmin=d["vmin"]; vmax=d["vmax"]; vmean=d["vmean"]
    ax[0].fill_between(pb, vmin, vmax, color=NEL, alpha=0.7, label="oscillation range (min–max)")
    ax[0].plot(pb, vmean, color=NEB, lw=1.3, label="mean / fixed point")
    # mark only the two real boundaries: the SNIC (cycle onset) and the Hopf;
    # shade/label the alpha-cycle band between them. (Stray operating-point lines removed.)
    osc = (vmax - vmin) > 0.2
    p_snic = float(pb[osc][0]) if osc.any() else 115.0
    y0, y1 = ax[0].get_ylim()
    ax[0].axvspan(p_snic, 315, color=NEL, alpha=0.18, lw=0)
    for pc in (p_snic, 315):
        ax[0].axvline(pc, color=NER, ls="--", lw=1.2, alpha=0.85)
    ax[0].text(p_snic+4, y0+(y1-y0)*0.40, f"SNIC\n$p\\approx{p_snic:.0f}$", color=NER, fontsize=8, ha="left", va="center")
    ax[0].text(318, y1*0.92, "Hopf\n$p\\approx315$\n$f_0\\approx11.1$ Hz", color=NER, fontsize=8, va="top")
    ax[0].text((p_snic+315)/2, y0+0.5, "alpha limit cycle", color=NEB, fontsize=8.5, ha="center", style="italic")
    ax[0].text(360, y0+0.5, "stable focus\n(resonator)", color=GR, fontsize=8.5, ha="center", style="italic")
    ax[0].set_xlabel("external input  $p$  (Hz)"); ax[0].set_ylabel("LFP $v=y_1-y_2$ (mV)")
    ax[0].set_title("JR bifurcation diagram")
    ax[0].legend(loc="upper left", fontsize=8)
    figstyle.panel(ax[0], "a")

    vv=np.linspace(-2,16,400)
    axb=ax[1]; axt=axb.twinx()
    axb.plot(vv, Sigm(vv), color=NEB, lw=2, label="$\\sigma(v)$ (firing rate)")
    axt.plot(vv, Sigm2(vv), color=NER, lw=1.6, ls="--", label="$\\sigma''(v)$ (demod gain)")
    axt.axhline(0, color=GR, lw=0.6)
    axb.axvline(v0, color=GR, ls=":", lw=1); axb.text(v0+0.2, 0.3, "inflection $v_0$\n$\\sigma''=0$",
        fontsize=8, color=GR)
    # operating points reached by closed-loop JR
    for vop,p in zip(d["v_ref"], d["p_ref"]):
        axb.plot(vop, Sigm(vop), "o", color=NEB2, ms=5)
    axb.set_xlabel("membrane potential $v$ (mV)")
    axb.set_ylabel("$\\sigma(v)$  (s$^{-1}$)", color=NEB)
    axt.set_ylabel("$\\sigma''(v)$", color=NER)
    axb.set_title("Sigmoid and its curvature $\\sigma''$", fontsize=11)
    l1,la1=axb.get_legend_handles_labels(); l2,la2=axt.get_legend_handles_labels()
    axb.legend(l1+l2, la1+la2, fontsize=8, frameon=False, loc="upper left")
    axb.set_title("Sigmoid $\\sigma(v)$ and its curvature $\\sigma''$")
    figstyle.panel(axb, "b")
    fig.tight_layout(); fig.savefig(f"{FIGS}/fig_bifurcation_sigmoid.png",dpi=300)
    fig.savefig(f"{FIGS}/fig_bifurcation_sigmoid.pdf"); print("wrote fig_bifurcation_sigmoid")

# ===================================================== FIG 3: 2-D resonance map
def resonance_map():
    fig, ax = plt.subplots(figsize=(7.2,4.3))
    fmap=d["f_map"]; pmap=d["p_map"]; Amap=d["A_map"]
    ext=[fmap[0],fmap[-1],pmap[0],pmap[-1]]
    im=ax.imshow(Amap, origin="lower", aspect="auto", extent=ext, cmap="viridis", interpolation="bilinear")
    ax.axvline(11.1, color="white", ls=":", lw=1)
    ax.annotate("near Hopf\n(high Q)", xy=(8.7, 320), color="white", fontsize=8.5, va="bottom")
    ax.annotate("far from Hopf", xy=(8.7, 396), color="white", fontsize=8.5, va="top")
    ax.set_xlabel("envelope frequency  $\\Omega/2\\pi$  (Hz)")
    ax.set_ylabel("external input  $p$  (Hz)  $\\rightarrow$ toward Hopf")
    ax.set_title("Demodulated response @ $\\Omega$  (mV): resonance ridge sharpens near Hopf", fontsize=10)
    fig.colorbar(im, label="response @ $\\Omega$ (mV)")
    fig.tight_layout(); fig.savefig(f"{FIGS}/fig_resonance_map.png",dpi=300)
    fig.savefig(f"{FIGS}/fig_resonance_map.pdf"); print("wrote fig_resonance_map")

# ====================================== FIG 4: carrier independence + synapse TF
def carrier_independence():
    fig, ax = plt.subplots(1, 2, figsize=(11,4.0))
    fc=d["fc_grid"]
    ax[0].semilogx(fc, d["A_ci_cl"], "o-", color=NEB, label="closed-loop JR (near Hopf)")
    ax[0].semilogx(fc, d["A_ci_ol"], "s--", color=NEB2, ms=4, label="open-loop detector")
    ax[0].axvline(d["F0"], color=NER, ls=":", lw=1); ax[0].text(d["F0"]*1.05, ax[0].get_ylim()[1]*0.1,
        "$f_0$", color=NER, fontsize=9)
    ax[0].set_ylim(0, None)
    ax[0].set_xlabel("carrier frequency  $f_c$  (Hz)")
    ax[0].set_ylabel("demodulated response @ $\\Omega$ (mV)")
    ax[0].set_title("Carrier independence\n($A_\\Omega\\propto\\sigma''\\varepsilon^2 m$, independent of $f_c$)", fontsize=10)
    ax[0].legend(fontsize=8, frameon=False); ax[0].spines[["top","right"]].set_visible(False)

    w=2*np.pi*np.logspace(0,3,400)
    H=(A*a)/np.abs((1j*w+a)**2)          # excitatory 2nd-order synapse |H(w)|
    H=H/H.max()
    ax[1].loglog(w/(2*np.pi), H, color=NEB, lw=2)
    ax[1].axvline(a/(2*np.pi), color=GR, ls=":", lw=1); ax[1].text(a/(2*np.pi)*1.1, 0.3,
        "corner\n$a/2\\pi\\approx16$ Hz", fontsize=8, color=GR)
    ax[1].axvspan(8,13, color=NER, alpha=0.12); ax[1].text(8.5,2e-3,"envelope",fontsize=8,color=NER)
    ax[1].axvline(100, color=NEB2, ls="--", lw=1); ax[1].text(105,2e-3,"carrier 100 Hz",fontsize=8,color=NEB2)
    ax[1].set_xlabel("frequency (Hz)"); ax[1].set_ylabel("$|H(\\omega)|$ (norm.)")
    ax[1].set_title("2nd-order synapse band-pass:\ncarrier suppressed, envelope passed", fontsize=10)
    figstyle.panel(ax[0], "a"); figstyle.panel(ax[1], "b")
    fig.tight_layout(); fig.savefig(f"{FIGS}/fig_carrier_independence.png",dpi=300)
    fig.savefig(f"{FIGS}/fig_carrier_independence.pdf"); print("wrote fig_carrier_independence")

# ================================================ FIG 5: operating-point law (signed)
def operating_point():
    fig, ax = plt.subplots(figsize=(7.6,4.4))
    vg=d["vgrid"]
    ax.axhline(0, color=GR, lw=0.6)
    ax.plot(vg, d["A_ol_signed"], color=NEB, lw=2, label="measured (signed, in-phase) $A_\\Omega$")
    ax.plot(vg, d["A_theory_signed"], "--", color=NER, lw=1.6,
            label="$\\frac{1}{2}\\sigma''(v^*)\\,\\varepsilon^2 m$  (theory)")
    ax.axvline(v0, color=GR, ls=":", lw=1)
    ax.annotate("inflection $v_0$:\n$\\sigma''=0$, sign flips", xy=(v0,0), xytext=(v0+1.2, ax.get_ylim()[1]*0.55),
                fontsize=8, color=GR, arrowprops=dict(arrowstyle="->", color=GR, lw=0.8))
    yref=np.interp(d["v_ref"], vg, d["A_ol_signed"])
    ax.plot(d["v_ref"], yref, "o", color="#1a9850", ms=6, label="JR operating points ($p$=265–395)")
    ax.set_xlabel("operating point  $v^*$  (mV)   [indexed by PEIX]")
    ax.set_ylabel("demodulated response @ $\\Omega$ (mV)")
    ax.set_title("Demodulation gain $=\\frac{1}{2}\\sigma''(v^*)\\varepsilon^2 m$: curvature law, "
                 "incl. sign reversal", fontsize=10)
    ax.legend(fontsize=8.5, frameon=False, loc="upper right"); ax.spines[["top","right"]].set_visible(False)
    fig.tight_layout(); fig.savefig(f"{FIGS}/fig_operating_point.png",dpi=300)
    fig.savefig(f"{FIGS}/fig_operating_point.pdf"); print("wrote fig_operating_point")

if __name__=="__main__":
    concept(); bifurcation_sigmoid(); resonance_map()
    carrier_independence(); operating_point()
    print("v2 figures done.")
