"""Refined NMM2 J-curve (clean version). Fixed eta=0; sweep J(=C) toward the gamma
Hopf. Fixed point solved ALGEBRAICALLY (exact -> smooth). Detection = exact v^2
(quadratic coefficient =2, a hard constant, operating-point-independent), so no
pinning is needed: only the network distance-to-Hopf gamma changes with J."""
import numpy as np
from scipy.optimize import brentq, fsolve
TAU_E,TAU_A,TAU_I,TAU_G=15.0,10.0,7.5,2.5
A_EE,A_EI,A_IE,A_II=1.0,1.0,1.0,2.0
DEL=1.0; PI=np.pi; ETA=0.0

def rhs(y,t,eta,C,Amp,wO,wc):
    r_e,v_e,r_i,v_i,s_e,z_e,s_i,z_i=y
    F=Amp*(1.0+np.cos(wO*t))*np.cos(wc*t)
    return np.array([
        (DEL/(PI*TAU_E)+2*r_e*v_e)/TAU_E,
        (eta-(PI*TAU_E*r_e)**2+v_e**2+F)/TAU_E + C*(A_EE*s_e-A_EI*s_i),
        (DEL/(PI*TAU_I)+2*r_i*v_i)/TAU_I,
        (eta-(PI*TAU_I*r_i)**2+v_i**2)/TAU_I + C*(A_IE*s_e-A_II*s_i),
        z_e/TAU_A,(r_e-2*z_e-s_e)/TAU_A,
        z_i/TAU_G,(r_i-2*z_i-s_i)/TAU_G])
def rk4(y,t,dt,*a):
    k1=rhs(y,t,*a);k2=rhs(y+.5*dt*k1,t+.5*dt,*a)
    k3=rhs(y+.5*dt*k2,t+.5*dt,*a);k4=rhs(y+dt*k3,t+dt,*a)
    return y+(dt/6)*(k1+2*k2+2*k3+k4)
def init(n):
    y=np.zeros((8,n));y[0]=0.05;y[1]=-2.0;y[2]=0.05;y[3]=-2.0;y[4]=0.05;y[6]=0.05;return y
_ve=lambda r_e:-DEL/(2*PI*TAU_E*r_e); _vi=lambda r_i:-DEL/(2*PI*TAU_I*r_i)
def eqs(x,C):
    r_e,r_i=x
    return [(ETA-(PI*TAU_E*r_e)**2+_ve(r_e)**2)/TAU_E + C*(r_e-r_i),
            (ETA-(PI*TAU_I*r_i)**2+_vi(r_i)**2)/TAU_I + C*(r_e-2*r_i)]
def fp(C,guess=(0.05,0.05)):
    r_e,r_i=fsolve(eqs,guess,args=(C,)); 
    return np.array([r_e,_ve(r_e),r_i,_vi(r_i),r_e,0.0,r_i,0.0]),r_e,r_i
def gam_w(x,C,h=1e-7):
    J=np.zeros((8,8))
    f=lambda xx: rhs(xx.reshape(8,1),0.0,ETA,np.array([C]),np.zeros(1),0.0,0.0).ravel()
    for j in range(8):
        d=np.zeros(8);d[j]=h;J[:,j]=(f(x+d)-f(x-d))/(2*h)
    ev=np.linalg.eigvals(J);fHz=np.abs(ev.imag)/(2*PI)*1000.0
    b=(fHz>25)&(fHz<90);c=np.where(b)[0]
    i=c[np.argmax(ev.real[c])] if len(c) else np.argmax(ev.real)
    return -ev[i].real,abs(ev[i].imag)
def lockin(Cg,Om,Amp,fc_Hz,t_set=900.0,t_meas=1700.0,dt=0.04):
    n=len(Cg);y=init(n);wc=2*PI*(fc_Hz/1000.0);t=0.0;Amp=np.full(n,Amp);eta=np.full(n,ETA)
    for _ in range(int(t_set/dt)): y=rk4(y,t,dt,eta,Cg,Amp,Om,wc);t+=dt
    nm=int(t_meas/dt);w=np.hanning(nm)
    ac=np.zeros(n);as_=np.zeros(n);av=np.zeros(n);awc=np.zeros(n);aws=np.zeros(n)
    for k in range(nm):
        y=rk4(y,t,dt,eta,Cg,Amp,Om,wc);t+=dt
        re=y[0];co=np.cos(Om*t);si=np.sin(Om*t)
        ac+=w[k]*re*co;as_+=w[k]*re*si;av+=w[k]*re;awc+=w[k]*co;aws+=w[k]*si
    vb=av/w.sum();c=ac-vb*awc;s=as_-vb*aws
    return 2/w.sum()*np.sqrt(c**2+s**2)
if __name__=="__main__":
    Chopf=brentq(lambda C: gam_w(fp(C)[0],C)[0], 15.0,18.0)
    print(f"gamma Hopf at J*={Chopf:.3f} (eta=0)")
    Cg=np.linspace(12.5,Chopf-0.08,24)
    gam=np.zeros(len(Cg));w0=np.zeros(len(Cg));ve=np.zeros(len(Cg))
    g=(0.05,0.05)
    for i,C in enumerate(Cg):
        x,re,ri=fp(C,g); g=(re,ri); ve[i]=x[1]; gam[i],w0[i]=gam_w(x,C)
    Acl=lockin(Cg,w0.copy(),8.0,300.0)
    print(" J(=C)  v_e*   gamma   f0Hz   A_lockin")
    for i in range(len(Cg)):
        print(f"{Cg[i]:6.2f} {ve[i]:6.3f} {gam[i]:7.4f} {w0[i]/2/PI*1000:5.1f} {Acl[i]:.4e}")
    np.savez("nmm2_jcA.npz",C=Cg,gamma=gam,w0=w0,ve=ve,Acl=Acl,Chopf=Chopf)
    print("DONE")
