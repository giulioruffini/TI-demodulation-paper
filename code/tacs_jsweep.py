"""SUPPLEMENTARY: tACS shares the network amplifier. A direct low-frequency (tACS)
drive at Delta f skips demodulation (it is already in-band) but feeds the SAME
near-Hopf resonator. Pinning v* and sweeping the coupling C(=J) toward the JR alpha
Hopf, the tACS lock-in grows as 1/gamma and the resonance sharpens -- the amplification
half of the TI mechanism, with no carrier. (pure numpy.)"""
import os, numpy as np, matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
import figstyle; figstyle.apply()
FIGS=os.environ.get("TN_FIGDIR") or os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "figures")
os.makedirs(FIGS, exist_ok=True)
A,B=3.25,22.0; a,b=100.0,50.0; v0,e0,rr=6.0,2.5,0.56
def Sigm(v): return 2*e0/(1+np.exp(rr*(v0-v)))
def p_of_C(vs,C):
    y0=(A/a)*Sigm(vs); return (a/A)*(vs+(B/b)*0.25*C*Sigm(0.25*C*y0))-0.8*C*Sigm(C*y0)
def rhs(Y,p,C,sf):
    C1=C;C2=0.8*C;C3=0.25*C;C4=0.25*C; y0,y1,y2,y3,y4,y5=Y.T; d=np.empty_like(Y)
    d[:,0]=y3;d[:,1]=y4;d[:,2]=y5
    d[:,3]=A*a*Sigm(y1-y2+sf)-2*a*y3-a*a*y0
    d[:,4]=A*a*(p+C2*Sigm(C1*y0))-2*a*y4-a*a*y1
    d[:,5]=B*b*(C4*Sigm(C3*y0))-2*b*y5-b*b*y2
    return d
def fp_v(p,C):
    C2=0.8*C;C3=0.25*C;C4=0.25*C
    def F(v):
        y0=(A/a)*Sigm(v);y1=(A/a)*(p+C2*Sigm(C*y0));y2=(B/b)*(C4*Sigm(C3*y0));return y1-y2-v
    vs=np.linspace(-20,40,3000);Fs=F(vs);idx=np.where(Fs[:-1]*Fs[1:]<0)[0]
    if not len(idx): return vs[np.argmin(np.abs(Fs))]
    lo,hi=vs[idx[0]],vs[idx[0]+1];flo=F(lo)
    for _ in range(200):
        mid=.5*(lo+hi);fm=F(mid)
        if flo*fm<=0: hi=mid
        else: lo=mid;flo=fm
        if hi-lo<1e-12: break
    return .5*(lo+hi)
def jac_eig(p,C,h=1e-6):
    v=fp_v(p,C);C2=0.8*C;C3=0.25*C;C4=0.25*C
    y0=(A/a)*Sigm(v);y1=(A/a)*(p+C2*Sigm(C*y0));y2=(B/b)*(C4*Sigm(C3*y0))
    x=np.array([y0,y1,y2,0,0,0]);J=np.zeros((6,6))
    f=lambda xx: rhs(xx[None,:],np.array([p]),np.array([C]),np.array([0.0]))[0]
    for j in range(6):
        dx=np.zeros(6);dx[j]=h;J[:,j]=(f(x+dx)-f(x-dx))/(2*h)
    ev=np.linalg.eigvals(J);i=np.argmax(ev.real);return v,-ev[i].real,abs(ev[i].imag)
def tacs_lockin(p,C,Om,eps,t_set=12.0,t_meas=6.0,dt=2e-4):
    N=len(p);Y=np.zeros((N,6));t=0.0;ns=int(t_set/dt);nm=int(t_meas/dt)
    sf=lambda tt: eps*np.cos(Om*tt)
    for _ in range(ns):
        k1=rhs(Y,p,C,sf(t));k2=rhs(Y+.5*dt*k1,p,C,sf(t+.5*dt))
        k3=rhs(Y+.5*dt*k2,p,C,sf(t+.5*dt));k4=rhs(Y+dt*k3,p,C,sf(t+dt))
        Y=Y+(dt/6)*(k1+2*k2+2*k3+k4);t+=dt
    w=np.hanning(nm);ws=w.sum();ac=np.zeros(N);as_=np.zeros(N);av=np.zeros(N);awc=np.zeros(N);aws=np.zeros(N)
    for k in range(nm):
        k1=rhs(Y,p,C,sf(t));k2=rhs(Y+.5*dt*k1,p,C,sf(t+.5*dt))
        k3=rhs(Y+.5*dt*k2,p,C,sf(t+.5*dt));k4=rhs(Y+dt*k3,p,C,sf(t+dt))
        Y=Y+(dt/6)*(k1+2*k2+2*k3+k4);t+=dt
        v=Y[:,1]-Y[:,2];co=np.cos(Om*t);si=np.sin(Om*t)
        ac+=w[k]*v*co;as_+=w[k]*v*si;av+=w[k]*v;awc+=w[k]*co;aws+=w[k]*si
    vb=av/ws;c=ac-vb*awc;s=as_-vb*aws;return 2/ws*np.sqrt(c**2+s**2)

vstar=8.30; eps=0.1   # weak tACS drive (linear regime)
# (b) coupling sweep toward Hopf, drive at each f0
Cs=np.linspace(110,136.3,12); ps=np.array([p_of_C(vstar,C) for C in Cs])
gam=np.zeros(len(Cs));w0=np.zeros(len(Cs))
for i,C in enumerate(Cs): _,gam[i],w0[i]=jac_eig(ps[i],C)
A_tacs=tacs_lockin(ps,Cs,w0.copy(),eps)
print(" C    gamma  f0   A_tacs")
for i in range(len(Cs)): print(f"{Cs[i]:6.1f}{gam[i]:7.3f}{w0[i]/2/np.pi:6.2f}  {A_tacs[i]:.3e}")
# (a) resonance vs df at 3 couplings
fdf=np.arange(8.5,13.51,0.12); Om=2*np.pi*fdf
Csel=[120.0,130.0,135.5]; res={}
for C in Csel:
    p=p_of_C(vstar,C); res[C]=tacs_lockin(np.full_like(Om,p),np.full_like(Om,C),Om,eps,14.0,8.0)
    g=jac_eig(p,C)[1]; print(f"res C={C} gamma={g:.2f} peak={res[C].max():.3f}")
np.savez("tacs_jsweep.npz",Cs=Cs,gam=gam,w0=w0,A=A_tacs,fdf=fdf,Csel=Csel,**{f"r{int(C*10)}":res[C] for C in Csel})

fig,ax=plt.subplots(1,2,figsize=(9.4,4.0))
cols=plt.cm.viridis(np.linspace(.15,.82,len(Csel)))
for C,c in zip(Csel,cols):
    g=jac_eig(p_of_C(vstar,C),C)[1]
    ax[0].plot(fdf,res[C],color=c,lw=1.9,label=f"$C$={C:.0f} ($\\gamma$={g:.1f})")
ax[0].set_xlabel(r'drive frequency $\Delta f$ (Hz)'); ax[0].set_ylabel(r'lock-in $A_\Omega$ (mV)')
ax[0].set_title('(a) tACS resonance sharpens as $C\\to C^*$'); ax[0].legend(fontsize=8); ax[0].grid(alpha=.3)
ax[1].loglog(1/gam,A_tacs,'o-',color='#0a4f8c',lw=2,label='tACS (direct $\\Delta f$ drive)')
xg=np.array([1/gam.max(),1/gam.min()]);k=A_tacs[5]*gam[5]
ax[1].loglog(xg,k*xg,'k--',lw=1,label=r'$\propto 1/\gamma$')
ax[1].set_xlabel(r'$1/\gamma$ (closeness to Hopf)'); ax[1].set_ylabel(r'$A_\Omega$ (mV)')
ax[1].set_title(r'(b) same $1/\gamma$ amplification as TI'); ax[1].legend(fontsize=8); ax[1].grid(alpha=.3,which='both')
plt.tight_layout()
plt.savefig(os.path.join(FIGS,"fig_tacs_jcurve.pdf"))
plt.savefig(os.path.join(FIGS,"fig_tacs_jcurve.png"),dpi=300)
print(f"saved fig_tacs_jcurve.{{pdf,png}} to {FIGS}")
