"""S5 panel (c): entrainment is easier NEAR CRITICALITY. Sweep the autonomous
operating point p across the limit-cycle range toward the Hopf (p_Hopf~315); at fixed
drive, measure the 1:1 locking range (tongue width in Delta f). It grows as the Hopf is
approached and the autonomous cycle amplitude -> 0 -- the entrainment counterpart of the
1/gamma forced-gain divergence on the stable side."""
import numpy as np
A,B=3.25,22.0; a,b=100.0,50.0; v0,e0,rr=6.0,2.5,0.56
def Sigm(v): return 2*e0/(1+np.exp(rr*(v0-v)))
def rhs(Y,p,sf):
    C=135.0;C1=C;C2=0.8*C;C3=0.25*C;C4=0.25*C
    y0,y1,y2,y3,y4,y5=Y.T; d=np.empty_like(Y)
    d[:,0]=y3;d[:,1]=y4;d[:,2]=y5
    d[:,3]=A*a*Sigm(y1-y2+sf)-2*a*y3-a*a*y0
    d[:,4]=A*a*(p+C2*Sigm(C1*y0))-2*a*y4-a*a*y1
    d[:,5]=B*b*(C4*Sigm(C3*y0))-2*b*y5-b*b*y2
    return d
def run(p,eps,Om,t_set,t_meas,dt,dec=5):
    N=len(p);Y=np.zeros((N,6));Y[:,1]=0.1;t=0.0
    sf=lambda tt: eps*np.cos(Om*tt)
    for _ in range(int(t_set/dt)):
        k1=rhs(Y,p,sf(t));k2=rhs(Y+.5*dt*k1,p,sf(t+.5*dt));k3=rhs(Y+.5*dt*k2,p,sf(t+.5*dt));k4=rhs(Y+dt*k3,p,sf(t+dt))
        Y=Y+(dt/6)*(k1+2*k2+2*k3+k4);t+=dt
    nm=int(t_meas/dt);buf=[]
    vmax=np.full(N,-1e9);vmin=np.full(N,1e9)
    for k in range(nm):
        k1=rhs(Y,p,sf(t));k2=rhs(Y+.5*dt*k1,p,sf(t+.5*dt));k3=rhs(Y+.5*dt*k2,p,sf(t+.5*dt));k4=rhs(Y+dt*k3,p,sf(t+dt))
        Y=Y+(dt/6)*(k1+2*k2+2*k3+k4);t+=dt
        v=Y[:,1]-Y[:,2];vmax=np.maximum(vmax,v);vmin=np.minimum(vmin,v)
        if k%dec==0: buf.append(v.copy())
    buf=np.array(buf);bb=buf-buf.mean(0,keepdims=True);fr=np.fft.rfftfreq(len(bb),d=dt*dec)
    P=np.abs(np.fft.rfft(bb*np.hanning(len(bb))[:,None],axis=0));fdom=fr[1:][np.argmax(P[1:],axis=0)]
    return fdom, vmax-vmin
dt=2e-4; pH=315.0; eps=0.5
pg=np.array([160,200,235,265,285,298,306,311],float)
# autonomous f0(p), amp0(p)
f0=np.zeros(len(pg)); amp0=np.zeros(len(pg))
for i,p in enumerate(pg):
    fd,am=run(np.array([p]),0.0,np.array([2*np.pi*10.0]),6.0,6.0,dt); f0[i]=fd[0]; amp0[i]=am[0]
# locking range at fixed eps: Delta f grid relative to each f0
nd=36; rel=np.linspace(-5.0,5.0,nd); dlo=10.0/(nd-1)
P=[];DF=[]
for i,p in enumerate(pg):
    P+=[p]*nd; DF+=list(f0[i]+rel)
P=np.array(P);DF=np.array(DF);Om=2*np.pi*DF
fdom,_=run(P,eps,Om,5.0,5.0,dt)
locked=(np.abs(fdom-DF)<0.30).reshape(len(pg),nd)
lock_range=locked.sum(1)*dlo   # Hz
print(" p     dist=pH-p  f0     cycAmp   lockRange(Hz)")
for i in range(len(pg)):
    print(f"{pg[i]:5.0f}  {pH-pg[i]:7.0f}  {f0[i]:5.2f}  {amp0[i]:6.2f}  {lock_range[i]:6.2f}")
np.savez("entrain_crit.npz",pg=pg,pH=pH,f0=f0,amp0=amp0,lock_range=lock_range,eps=eps)
print("saved")
