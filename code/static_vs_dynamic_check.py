"""NMM1 (static curve) versus NMM2 (MPR dynamics), same membrane, same steady-state curve.
Single uncoupled MPR population, tau = 15 ms, current drive a cos(wt) into the voltage equation.
(a) linear rate response to the drive; (b) rectified DC output per a^2; (c) ratio NMM2/NMM1."""
import numpy as np, matplotlib
matplotlib.use("Agg"); import matplotlib.pyplot as plt
D=1.0; TAU=15e-3
def F(Q):  return np.sqrt((Q+np.sqrt(Q*Q+D*D))/2)/np.pi
def Fp(Q,h=1e-5): return (F(Q+h)-F(Q-h))/(2*h)
def Fpp(Q,h=1e-4): return (F(Q+h)-2*F(Q)+F(Q-h))/h**2
def rates(Q): r=F(Q); return r, D/(np.pi*r), 2*np.pi*r          # r*, d, nu  (tau=1 units)
def Hv(Q,w): r,d,nu=rates(Q); return (1j*w+d)/((1j*w+d)**2+nu**2)  # current -> voltage (the membrane NMM2 has)
def Hr(Q,w): r,d,nu=rates(Q); return 2*r*Hv(Q,w)/(1j*w+d)          # current -> rate, linear
def C(Q,w):  r,d,nu=rates(Q); return r*(w*w+3*d*d-nu*nu)/((d*d+nu*nu)*((d*d+nu*nu-w*w)**2+4*d*d*w*w))
def C_static(Q,w): return Fpp(Q)/4*abs(Hv(Q,w)/Hv(Q,1e-9))**2     # NMM1: static F on the membrane-filtered drive
f=np.logspace(0,4,600); w=2*np.pi*f*TAU
cases=((-1.0,"#1f4e79","$Q=-1$ (quiescent, $\\nu<d$)"),(0.2,"#1a9850","$Q=0.2$ (below inflection, $\\nu\\approx d$)"),(3.0,"#c0392b","$Q=3$ (above inflection, $\\nu\\gg d$)"))
fig,ax=plt.subplots(1,3,figsize=(15,4.3))
for Q,col,lab in cases:
    r,d,nu=rates(Q); fd=d/(2*np.pi*TAU); fnu=nu/(2*np.pi*TAU)
    # (a) linear rate response, normalized to DC
    ax[0].plot(f,abs(Hr(Q,w)/Hr(Q,1e-9)),color=col,lw=1.8,label=lab)      # NMM2: rate lags the voltage (inertia) x membrane
    ax[0].plot(f,abs(Hv(Q,w)/Hv(Q,1e-9)),color=col,lw=1.0,ls="--")         # NMM1 with the same membrane: static curve on the filtered voltage
    # (b) rectified output
    cd=C(Q,w); cs=C_static(Q,w)
    ax[1].plot(f,abs(cd),color=col,lw=1.8,label=lab)
    ax[1].plot(f,abs(cs),color=col,lw=1.0,ls="--")
    neg=cd<0
    if neg.any() and (~neg).any():
        fz=f[np.argmax(~neg & (f>fd/10))]; ax[1].axvline(fz,color=col,lw=0.7,alpha=0.5)
        ax[1].text(fz*1.1,3e-6,"sign change",color=col,fontsize=7,rotation=90,va="bottom")
    # (c) ratio
    R=cd/cs; ax[2].plot(f,R,color=col,lw=1.8,label=lab)
    ax[2].axhline(d*d/(3*d*d-nu*nu),color=col,lw=0.8,ls=":")
    ax[2].text(1.2e4,d*d/(3*d*d-nu*nu),f"{d*d/(3*d*d-nu*nu):.2f}",color=col,fontsize=8,va="center")
    for a in ax: a.axvline(fnu,color=col,lw=0.6,ls=":",alpha=0.6)
    print(f"Q={Q:5.1f}  r*={r:.3f}  d={d:.2f}  nu={nu:.2f}  f_d={fd:.0f} Hz  f_nu={fnu:.0f} Hz  R(inf)=d^2/(3d^2-nu^2)={d*d/(3*d*d-nu*nu):+.3f}")
g1=0.5*(f/50.)**-1; g2=0.5*(f/50.)**-2
ax[0].plot(f,g1,color="0.6",lw=0.8,ls="--"); ax[0].text(3000,g1[np.searchsorted(f,3000)]*1.8,"$\\propto f^{-1}$",fontsize=8,color="0.4")
ax[0].plot(f,g2,color="0.6",lw=0.8,ls="--"); ax[0].text(3000,g2[np.searchsorted(f,3000)]*1.8,"$\\propto f^{-2}$",fontsize=8,color="0.4")
ax[0].set_xscale("log"); ax[0].set_yscale("log"); ax[0].set_ylim(1e-5,2)
ax[0].set_ylabel("linear response of the rate at the drive frequency (norm. to DC)"); ax[0].set_title("(a) linear response: the NMM2 rate lags the voltage by one power",fontsize=10,loc="left")
ax[0].text(1.3,3.5e-5,"dashed: NMM1 rate on the same membrane, $\\propto 1/f$ (membrane)",fontsize=7.5,color="0.3")
ax[0].text(1.3,1.5e-5,"solid: NMM2 rate, $\\propto 1/f^2$ (membrane $\\times$ rate inertia)",fontsize=7.5,color="0.3")
ax[1].set_xscale("log"); ax[1].set_yscale("log"); ax[1].set_ylim(1e-7,1)
gl=1e-2*(f/100.)**-2; ax[1].plot(f,gl,color="0.6",lw=0.8,ls="--"); ax[1].text(2000,gl[np.searchsorted(f,2000)]*1.6,"$\\propto f^{-2}$",fontsize=8,color="0.4")
ax[1].set_ylabel("|rectified DC rate shift| / $a^2$ ($\\tau=1$ units)"); ax[1].set_title("(b) rectified (beat) output: same slope, the membrane",fontsize=10,loc="left")
ax[2].set_xscale("log"); ax[2].set_ylim(-0.6,1.3); ax[2].axhline(0,color="0.6",lw=0.7); ax[2].axhline(1,color="0.6",lw=0.7)
ax[2].set_ylabel("NMM2 / NMM1  (same membrane, same curve $F$)"); ax[2].set_title("(c) ratio NMM2 / NMM1 of the rectified output",fontsize=10,loc="left")
ax[2].text(1.3,1.2,"$R\\to d^2/(3d^2-\\nu^2)$ above the population rates: a constant, no power of $f$",fontsize=8)
for a in ax:
    a.set_xlim(1,1e4); a.set_xlabel("carrier frequency $f_c$ (Hz), $\\tau=15$ ms")
    for fx in (300,1000,2000): a.axvline(fx,color="0.8",lw=0.7,ls=":")
ax[0].legend(fontsize=7,loc="lower left",frameon=False); ax[2].legend(fontsize=7,loc="lower left",frameon=False)
fig.tight_layout(); fig.savefig("static_vs_dynamic.png",dpi=130); fig.savefig("static_vs_dynamic.pdf")
