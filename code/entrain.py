"""S4: the OSCILLATORY (above-Hopf) regime needs entrainment metrics, not 1/gamma.
Drive the autonomous JR alpha limit cycle (input p in the cycle range, p<p_Hopf~315)
with a direct Delta f sinusoid; sweep (Delta f, amplitude).
(a) 1:1 Arnold tongue: region where the column's dominant output frequency locks to Delta f.
(b) at fixed drive: locking (lock-in at Delta f) peaks in the tongue while the cycle
    AMPLITUDE barely moves -> entrainment of phase/timing, not amplitude amplification."""
import numpy as np, matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
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
def integ(p,eps,Om,t_set,t_meas,dt,dec=5):
    N=len(p);Y=np.zeros((N,6));Y[:,1]=0.1;t=0.0
    sf=lambda tt: eps*np.cos(Om*tt)
    for _ in range(int(t_set/dt)):
        k1=rhs(Y,p,sf(t));k2=rhs(Y+.5*dt*k1,p,sf(t+.5*dt))
        k3=rhs(Y+.5*dt*k2,p,sf(t+.5*dt));k4=rhs(Y+dt*k3,p,sf(t+dt))
        Y=Y+(dt/6)*(k1+2*k2+2*k3+k4);t+=dt
    nm=int(t_meas/dt);buf=[];ts=[]
    w=np.hanning(nm);ws=w.sum();ac=np.zeros(N);as_=np.zeros(N);av=np.zeros(N);awc=np.zeros(N);aws=np.zeros(N)
    vmax=np.full(N,-1e9);vmin=np.full(N,1e9)
    for k in range(nm):
        k1=rhs(Y,p,sf(t));k2=rhs(Y+.5*dt*k1,p,sf(t+.5*dt))
        k3=rhs(Y+.5*dt*k2,p,sf(t+.5*dt));k4=rhs(Y+dt*k3,p,sf(t+dt))
        Y=Y+(dt/6)*(k1+2*k2+2*k3+k4);t+=dt
        v=Y[:,1]-Y[:,2];co=np.cos(Om*t);si=np.sin(Om*t)
        ac+=w[k]*v*co;as_+=w[k]*v*si;av+=w[k]*v;awc+=w[k]*co;aws+=w[k]*si
        vmax=np.maximum(vmax,v);vmin=np.minimum(vmin,v)
        if k%dec==0: buf.append(v.copy());ts.append(t)
    vb=av/ws;c=ac-vb*awc;s=as_-vb*aws;lockin=2/ws*np.sqrt(c**2+s**2)
    buf=np.array(buf)  # (nt,N)
    # dominant output frequency via FFT
    bb=buf-buf.mean(0,keepdims=True); fr=np.fft.rfftfreq(len(bb),d=dt*dec)
    P=np.abs(np.fft.rfft(bb*np.hanning(len(bb))[:,None],axis=0))
    fdom=fr[1:][np.argmax(P[1:],axis=0)]
    return lockin, vmax-vmin, fdom

dt=2e-4; p0=250.0
# autonomous f0 and cycle amplitude (no drive)
l0,amp0,f0=integ(np.array([p0]),0.0,np.array([2*np.pi*10.0]),6.0,6.0,dt)
f0=float(f0[0]); amp0=float(amp0[0]); print(f"autonomous p={p0}: f0={f0:.2f} Hz, cycle amp={amp0:.2f} mV")

# (a) tongue grid
dfg=np.linspace(f0-4.0,f0+4.0,30); epsg=np.linspace(0.0,1.3,11)
DF,EP=np.meshgrid(dfg,epsg,indexing="ij")
p=np.full(DF.size,p0); Om=2*np.pi*DF.ravel(); eps=EP.ravel()
# vectorized over grid: eps per element
def integ_vec(p,eps,Om,t_set,t_meas,dt,dec=5):
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
fdom,amp=integ_vec(p,eps,Om,5.0,5.0,dt)
locked=(np.abs(fdom-DF.ravel())<0.25).astype(float).reshape(DF.shape)  # 1:1 lock
np.savez("entrain.npz",dfg=dfg,epsg=epsg,locked=locked,f0=f0,amp0=amp0,p0=p0)
print("tongue done; locked fraction:", locked.mean())

# (b) one drive amplitude: lock-in + amplitude vs Delta f
eps_b=0.6; dfb=np.linspace(f0-4.0,f0+4.0,44); Omb=2*np.pi*dfb
li,ampb,fd=integ([np.full(len(dfb),p0)][0],eps_b,Omb,6.0,6.0,dt)
np.savez("entrain_b.npz",dfb=dfb,li=li,ampb=ampb,fd=fd,f0=f0,amp0=amp0,eps_b=eps_b)
print("panel b done")
