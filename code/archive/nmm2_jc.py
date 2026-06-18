import numpy as np
TAU_E,TAU_A,TAU_I,TAU_G=15.0,10.0,7.5,2.5
A_EE,A_EI,A_IE,A_II=1.0,1.0,1.0,2.0
DEL=1.0; PI=np.pi
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
def fp_all(eta,Cg,T=800.0,dt=0.05):
    n=len(Cg);y=init(n);t=0.0;z=np.zeros(n)
    for _ in range(int(T/dt)): y=rk4(y,t,dt,eta,Cg,z,0.0,0.0);t+=dt
    return y
def jac_eig_at(x,eta,C,h=1e-7):
    J=np.zeros((8,8))
    f=lambda xx: rhs(xx.reshape(8,1),0.0,eta,np.array([C]),np.zeros(1),0.0,0.0).ravel()
    for j in range(8):
        dx=np.zeros(8);dx[j]=h;J[:,j]=(f(x+dx)-f(x-dx))/(2*h)
    ev=np.linalg.eigvals(J)
    fHz=np.abs(ev.imag)/(2*PI)*1000.0
    band=(fHz>30)&(fHz<80)            # gamma pair only
    cand=np.where(band)[0]
    i=cand[np.argmax(ev.real[cand])] if len(cand) else np.argmax(ev.real)
    return -ev[i].real,abs(ev[i].imag)
def lockin_re(eta,Cg,Om,Amp,fc_Hz,t_set=600.0,t_meas=1000.0,dt=0.05):
    n=len(Cg);y=init(n);wc=2*PI*(fc_Hz/1000.0);t=0.0;Amp=np.full(n,Amp)
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
    eta=0.0
    Cg=np.array([10,11,12,13,14,15,15.7,16.2,16.4,16.5],float)
    X=fp_all(eta,Cg)
    gam=np.zeros(len(Cg));w0=np.zeros(len(Cg))
    for i,C in enumerate(Cg): gam[i],w0[i]=jac_eig_at(X[:,i],eta,C)
    Acl=lockin_re(eta,Cg,w0.copy(),8.0,300.0)
    print("  C    v_e*    gamma   f0(Hz)  A_lockin(r_e)")
    for i in range(len(Cg)):
        print(f"{Cg[i]:5.1f} {X[1,i]:7.3f} {gam[i]:7.4f} {w0[i]/2/PI*1000:6.1f} {Acl[i]:.3e}")
    np.savez("nmm2_jcurve.npz",C=Cg,gamma=gam,w0=w0,ve=X[1],Acl=Acl)
    print("DONE")
