import numpy as np
from scipy.optimize import brentq
from nmm2_jcA import fp, gam_w, init, rk4, PI, ETA
def lockin_grid(Cvals,dfHz,Amp,fc_Hz,t_set=600.0,t_meas=1200.0,dt=0.05):
    CC,DD=np.meshgrid(Cvals,dfHz,indexing="ij")
    C=CC.ravel().copy(); Om=2*PI*(DD.ravel()/1000.0); n=C.size
    y=init(n); wc=2*PI*(fc_Hz/1000.0); t=0.0; Am=np.full(n,Amp); eta=np.full(n,ETA)
    for _ in range(int(t_set/dt)): y=rk4(y,t,dt,eta,C,Am,Om,wc); t+=dt
    nm=int(t_meas/dt); w=np.hanning(nm)
    ac=np.zeros(n);as_=np.zeros(n);av=np.zeros(n);awc=np.zeros(n);aws=np.zeros(n)
    for k in range(nm):
        y=rk4(y,t,dt,eta,C,Am,Om,wc); t+=dt
        re=y[0];co=np.cos(Om*t);si=np.sin(Om*t)
        ac+=w[k]*re*co;as_+=w[k]*re*si;av+=w[k]*re;awc+=w[k]*co;aws+=w[k]*si
    vb=av/w.sum();c=ac-vb*awc;s=as_-vb*aws
    return (2/w.sum()*np.sqrt(c**2+s**2)).reshape(CC.shape)
Chopf=brentq(lambda C: gam_w(fp(C)[0],C)[0],15.0,18.0)
Cg=np.linspace(13.0,Chopf-0.07,16)
dfHz=np.linspace(40.0,58.0,13)
gam=np.zeros(len(Cg)); g=(0.05,0.05)
for i,C in enumerate(Cg):
    x,re,ri=fp(C,g); g=(re,ri); gam[i],_=gam_w(x,C)
M=lockin_grid(Cg,dfHz,8.0,300.0); peak=M.max(1); fpk=dfHz[M.argmax(1)]
print(f"J*={Chopf:.3f}")
print(" J     gamma  fpk   peakA")
for i in range(len(Cg)): print(f"{Cg[i]:6.2f} {gam[i]:7.4f} {fpk[i]:5.1f} {peak[i]:.4e}")
np.savez("nmm2_jcD.npz",C=Cg,gamma=gam,peak=peak,fpk=fpk,dfHz=dfHz,M=M,Chopf=Chopf)
print("DONE")
