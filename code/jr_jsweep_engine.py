"""Numerics for the J-curve: pinned-v* coupling sweep in the Jansen-Rit column."""
import numpy as np
from scipy.optimize import brentq
A,B=3.25,22.0; a,b=100.0,50.0; v0,e0,rr=6.0,2.5,0.56
def Sigm(v):  return 2*e0/(1+np.exp(rr*(v0-v)))
def Sigm2(v):
    Ex=np.exp(rr*(v0-v)); return 2*e0*rr*rr*Ex*(Ex-1)/(1+Ex)**3
def p_of_C(vstar,C):
    """external drive p that pins the field-free fixed point at v=vstar, given C."""
    y0=(A/a)*Sigm(vstar)
    return (a/A)*(vstar+(B/b)*0.25*C*Sigm(0.25*C*y0)) - 0.8*C*Sigm(C*y0)
def rhs(Y,p,C,sf):
    C1=C; C2=0.8*C; C3=0.25*C; C4=0.25*C
    y0,y1,y2,y3,y4,y5=Y.T; d=np.empty_like(Y)
    d[:,0]=y3; d[:,1]=y4; d[:,2]=y5
    d[:,3]=A*a*Sigm(y1-y2+sf)   -2*a*y3-a*a*y0
    d[:,4]=A*a*(p+C2*Sigm(C1*y0))-2*a*y4-a*a*y1
    d[:,5]=B*b*(C4*Sigm(C3*y0)) -2*b*y5-b*b*y2
    return d
def field(t,eps,m,Om,fc): return eps*(1+m*np.cos(Om*t))*np.cos(2*np.pi*fc*t)
def _fp_v(p,C):
    C1=C; C2=0.8*C; C3=0.25*C; C4=0.25*C
    def F(v):
        y0=(A/a)*Sigm(v); y1=(A/a)*(p+C2*Sigm(C1*y0)); y2=(B/b)*(C4*Sigm(C3*y0))
        return y1-y2-v
    vs=np.linspace(-20,40,3000); Fs=F(vs); idx=np.where(Fs[:-1]*Fs[1:]<0)[0]
    return brentq(F,vs[idx[0]],vs[idx[0]+1]) if len(idx) else vs[np.argmin(np.abs(Fs))]
def jac_eig(p,C,h=1e-6):
    v=_fp_v(p,C); C2=0.8*C; C3=0.25*C; C4=0.25*C
    y0=(A/a)*Sigm(v); y1=(A/a)*(p+C2*Sigm(C*y0)); y2=(B/b)*(C4*Sigm(C3*y0))
    x=np.array([y0,y1,y2,0,0,0]); Jm=np.zeros((6,6))
    f=lambda xx: rhs(xx[None,:],np.array([p]),np.array([C]),np.array([0.0]))[0]
    for j in range(6):
        dx=np.zeros(6); dx[j]=h; Jm[:,j]=(f(x+dx)-f(x-dx))/(2*h)
    ev=np.linalg.eigvals(Jm); i=np.argmax(ev.real)
    return v, -ev[i].real, abs(ev[i].imag), ev
def closed_lockin(p,C,Om,eps,m,fc,t_set,t_meas,dt):
    N=len(p); Y=np.zeros((N,6)); t=0.0
    ns=int(t_set/dt); nm=int(t_meas/dt)
    for _ in range(ns):
        s1=field(t,eps,m,Om,fc); k1=rhs(Y,p,C,s1)
        s2=field(t+.5*dt,eps,m,Om,fc); k2=rhs(Y+.5*dt*k1,p,C,s2)
        k3=rhs(Y+.5*dt*k2,p,C,s2)
        s3=field(t+dt,eps,m,Om,fc); k4=rhs(Y+dt*k3,p,C,s3)
        Y=Y+(dt/6)*(k1+2*k2+2*k3+k4); t+=dt
    w=np.hanning(nm); ws=w.sum()
    ac=np.zeros(N); as_=np.zeros(N); av=np.zeros(N); awc=np.zeros(N); aws=np.zeros(N)
    for k in range(nm):
        s1=field(t,eps,m,Om,fc); k1=rhs(Y,p,C,s1)
        s2=field(t+.5*dt,eps,m,Om,fc); k2=rhs(Y+.5*dt*k1,p,C,s2)
        k3=rhs(Y+.5*dt*k2,p,C,s2)
        s3=field(t+dt,eps,m,Om,fc); k4=rhs(Y+dt*k3,p,C,s3)
        Y=Y+(dt/6)*(k1+2*k2+2*k3+k4); t+=dt
        v=Y[:,1]-Y[:,2]; co=np.cos(Om*t); si=np.sin(Om*t)
        ac+=w[k]*v*co; as_+=w[k]*v*si; av+=w[k]*v; awc+=w[k]*co; aws+=w[k]*si
    vb=av/ws; c=ac-vb*awc; s=as_-vb*aws
    return 2/ws*np.sqrt(c**2+s**2)
def openloop(v_star,eps,m,Om,fc,dt=2e-4,T=3.0):
    n=int(T/dt); t=np.arange(n)*dt
    s=eps*(1+m*np.cos(Om[:,None]*t))*np.cos(2*np.pi*fc*t)
    y=Sigm(v_star[:,None]+s); y=y-y.mean(1,keepdims=True); w=np.hanning(n)
    c=(y*(w*np.cos(Om[:,None]*t))).sum(1); s_=(y*(w*np.sin(Om[:,None]*t))).sum(1)
    return 2/w.sum()*np.sqrt(c**2+s_**2)
