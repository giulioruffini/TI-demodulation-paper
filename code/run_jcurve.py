import numpy as np, jr_jsweep_engine as E
from scipy.optimize import brentq
eps,m,fc=0.3,1.0,100.0; dt=2e-4; VSTAR=8.30; sig2=E.Sigm2(VSTAR)
Chopf=brentq(lambda C: E.jac_eig(E.p_of_C(VSTAR,C),C)[1], 120,140)
Cs=np.linspace(110, Chopf-0.7, 14)
ps=np.array([E.p_of_C(VSTAR,C) for C in Cs])
gam=np.zeros(len(Cs)); w0=np.zeros(len(Cs))
for i,C in enumerate(Cs): _,gam[i],w0[i],_=E.jac_eig(ps[i],C)
Acl=E.closed_lockin(ps,Cs,w0.copy(),eps,m,fc,12.0,5.0,dt)
Aop=E.openloop(np.full(len(Cs),VSTAR),eps,m,w0.copy(),fc)
np.savez("jcurve_main.npz",C=Cs,p=ps,gamma=gam,w0=w0,Acl=Acl,Aop=Aop,
         gain=Acl/Aop,Chopf=Chopf,vstar=VSTAR,sig2=sig2)
print(f"Chopf={Chopf:.2f} sig2={sig2:+.4f}")
print(" C     gamma  f0    A_open   A_clsd  gain")
for i in range(len(Cs)):
    print(f"{Cs[i]:6.1f} {gam[i]:6.2f} {w0[i]/2/np.pi:5.2f} {Aop[i]:.3e} {Acl[i]:.2e} {Acl[i]/Aop[i]:6.1f}")
