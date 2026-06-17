"""
Envelope demodulation -> resonance in a Jansen-Rit neural mass.

A high-frequency amplitude-modulated (AM) "field"
        s(t) = eps * (1 + m cos(Omega t)) * cos(2 pi f_c t)
is injected into the argument of the pyramidal output sigmoid (i.e. the
field polarizes the spike-generating nonlinearity).  The AM signal has NO
spectral power at the envelope frequency Omega; the sigmoid's curvature
demodulates it, depositing a component at Omega that then drives the JR
alpha resonance.  Near the supercritical Hopf (p ~ 315 Hz, f0 ~ 11.1 Hz)
the forced response is strongly amplified.

Outputs:
  - resonance curves (response @ Omega vs Omega) for several distances to
    the Hopf, on the stable side (forced resonance) and the limit-cycle
    side (entrainment);
  - a demodulation sanity panel (input vs output spectra + time traces).
"""
import numpy as np
from scipy.optimize import brentq
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ---------------- Jansen-Rit parameters ----------------
A, B = 3.25, 22.0
a, b = 100.0, 50.0
v0, e0, r = 6.0, 2.5, 0.56
C = 135.0
C1, C2, C3, C4 = C, 0.8*C, 0.25*C, 0.25*C

def Sigm(v):
    """Population firing-rate sigmoid sigma(v) = 2 e0 / (1 + exp[r (v0 - v)])."""
    return 2.0*e0/(1.0+np.exp(r*(v0-v)))

def Sigm1(v):
    """First derivative sigma'(v) = 2 e0 r E / (1+E)^2,  E = exp[r(v0-v)]."""
    E = np.exp(r*(v0-v))
    return 2.0*e0*r*E/(1.0+E)**2

def Sigm2(v):
    """Second derivative sigma''(v) = 2 e0 r^2 E (E-1) / (1+E)^3.
    Vanishes at the inflection v=v0 (E=1); sets the square-law demodulation gain."""
    E = np.exp(r*(v0-v))
    return 2.0*e0*r*r*E*(E-1.0)/(1.0+E)**3

# ---------------- vectorized RHS ----------------
# State Y has shape (N,6): columns y0,y1,y2,y3,y4,y5 ; v = y1 - y2 (LFP)
# p : (N,) external input ; sfield : (N,) injected field at this time
def rhs(Y, p, sfield, lin=None):
    """lin: if None, full sigmoid. Else (v_op, S1) linearizes the pyramidal
    output sigmoid about v_op -> field enters purely linearly (no demodulation)."""
    y0,y1,y2,y3,y4,y5 = Y.T
    d = np.empty_like(Y)
    d[:,0]=y3
    d[:,1]=y4
    d[:,2]=y5
    if lin is None:
        pyr = Sigm(y1-y2+sfield)                 # nonlinear: demodulates
    else:
        v_op, S1 = lin
        pyr = Sigm(v_op) + S1*((y1-y2+sfield)-v_op)  # linearized: cannot demodulate
    d[:,3]=A*a*pyr                     - 2*a*y3 - a*a*y0
    d[:,4]=A*a*(p + C2*Sigm(C1*y0))    - 2*a*y4 - a*a*y1
    d[:,5]=B*b*(C4*Sigm(C3*y0))        - 2*b*y5 - b*b*y2
    return d

def field(t, eps, m, Omega, fc):
    return eps*(1.0+m*np.cos(Omega*t))*np.cos(2*np.pi*fc*t)

def integrate(p, Omega, eps, m, fc, t_settle, t_meas, dt, record=False, lin=None):
    """RK4. p,Omega shape (N,). Returns lock-in amplitude @Omega of v=y1-y2.
    If record, also returns (t_arr, v_arr, s_arr) for system 0 over the window.
    lin: pass (v_op,S1) to linearize the field-receiving sigmoid (control)."""
    N = p.shape[0]
    Y = np.zeros((N,6))
    nset = int(round(t_settle/dt))
    nmea = int(round(t_meas/dt))
    t = 0.0
    for _ in range(nset):
        s1=field(t,eps,m,Omega,fc)
        k1=rhs(Y,p,s1,lin)
        s2=field(t+0.5*dt,eps,m,Omega,fc)
        k2=rhs(Y+0.5*dt*k1,p,s2,lin)
        k3=rhs(Y+0.5*dt*k2,p,s2,lin)
        s3=field(t+dt,eps,m,Omega,fc)
        k4=rhs(Y+dt*k3,p,s3,lin)
        Y=Y+(dt/6.0)*(k1+2*k2+2*k3+k4)
        t+=dt
    # measurement window: demeaned Hann-windowed lock-in at Omega.
    # We accumulate the windowed quadratures of v and of the window's own cos/sin
    # so the DC of v can be removed exactly (else it leaks into the Omega bin).
    w = np.hanning(nmea); wsum=w.sum()
    acc_c=np.zeros(N); acc_s=np.zeros(N); acc_v=np.zeros(N)   # sum w v cos, w v sin, w v
    acc_wc=np.zeros(N); acc_ws=np.zeros(N)                    # sum w cos, w sin (per Omega)
    if record:
        t_arr=np.empty(nmea); v_arr=np.empty(nmea); s_arr=np.empty(nmea)
    for k in range(nmea):
        s1=field(t,eps,m,Omega,fc); k1=rhs(Y,p,s1,lin)
        s2=field(t+0.5*dt,eps,m,Omega,fc); k2=rhs(Y+0.5*dt*k1,p,s2,lin)
        k3=rhs(Y+0.5*dt*k2,p,s2,lin)
        s3=field(t+dt,eps,m,Omega,fc); k4=rhs(Y+dt*k3,p,s3,lin)
        Y=Y+(dt/6.0)*(k1+2*k2+2*k3+k4); t+=dt
        v=Y[:,1]-Y[:,2]; co=np.cos(Omega*t); si=np.sin(Omega*t)
        acc_c+=w[k]*v*co; acc_s+=w[k]*v*si; acc_v+=w[k]*v
        acc_wc+=w[k]*co;  acc_ws+=w[k]*si
        if record:
            t_arr[k]=t; v_arr[k]=v[0]; s_arr[k]=s1[0]
    vbar=acc_v/wsum                                          # windowed mean of v
    c=acc_c-vbar*acc_wc; s=acc_s-vbar*acc_ws                 # remove DC leakage
    amp=2.0/wsum*np.sqrt(c**2+s**2)
    if record:
        return amp, t_arr, v_arr, s_arr
    return amp

def steady_v(p, dt=2e-4, t=4.0):
    """field-free steady-state v=y1-y2 for each p (shape N) and sigmoid slope there."""
    N=p.shape[0]; Y=np.zeros((N,6)); z=np.zeros(N)
    for _ in range(int(t/dt)):
        k1=rhs(Y,p,z); k2=rhs(Y+0.5*dt*k1,p,z)
        k3=rhs(Y+0.5*dt*k2,p,z); k4=rhs(Y+dt*k3,p,z)
        Y=Y+(dt/6.0)*(k1+2*k2+2*k3+k4)
    v=Y[:,1]-Y[:,2]
    return v, Sigm1(v)

# ----------------------------------------------------------------------
# Open-loop "detector": the sigmoid alone, no network feedback.
# Demonstrates A_Omega ~ (1/2) sigma''(v*) eps^2 m  and carrier independence.
# ----------------------------------------------------------------------
def openloop_lockin(v_star, eps, m, Omega, fc, dt=2e-4, T=2.0):
    """Pass the AM field through sigma at fixed operating point(s) v_star and
    return the Hann-windowed lock-in amplitude of sigma(v*+s(t)) at Omega.
    v_star, Omega, fc are broadcast to a common shape (N,); eps, m scalar."""
    v_star, Omega, fc = np.broadcast_arrays(np.atleast_1d(np.asarray(v_star,float)),
                                            np.atleast_1d(np.asarray(Omega,float)),
                                            np.atleast_1d(np.asarray(fc,float)))
    n = int(round(T/dt)); t = np.arange(n)*dt
    Om = Omega[:, None]                                       # (N,1)
    s = eps*(1.0+m*np.cos(Om*t))*np.cos(2*np.pi*fc[:, None]*t)  # (N,n)
    y = Sigm(v_star[:, None] + s)                             # (N,n)
    y = y - y.mean(1, keepdims=True)                          # demean (avoid DC leakage)
    w = np.hanning(n)
    c = (y*(w*np.cos(Om*t))).sum(1); s_ = (y*(w*np.sin(Om*t))).sum(1)
    return 2.0/w.sum()*np.sqrt(c**2 + s_**2)

def openloop_inphase(v_star, eps, m, Omega, fc, dt=2e-4, T=2.0):
    """SIGNED in-phase (cosine) lock-in component of sigma(v*+s(t)) at Omega.
    For the static detector the demodulated term is in phase with the envelope
    cos(Omega t), so this returns ~ (1/2) sigma''(v*) eps^2 m -- including the
    SIGN reversal across the inflection v0 (where sigma''=0)."""
    v_star, Omega, fc = np.broadcast_arrays(np.atleast_1d(np.asarray(v_star,float)),
                                            np.atleast_1d(np.asarray(Omega,float)),
                                            np.atleast_1d(np.asarray(fc,float)))
    n = int(round(T/dt)); t = np.arange(n)*dt
    Om = Omega[:, None]
    s = eps*(1.0+m*np.cos(Om*t))*np.cos(2*np.pi*fc[:, None]*t)
    y = Sigm(v_star[:, None] + s); y = y - y.mean(1, keepdims=True)
    w = np.hanning(n)
    return 2.0/w.sum()*(y*(w*np.cos(Om*t))).sum(1)

# ----------------------------------------------------------------------
# Field-free min/max of the LFP vs p  -> JR bifurcation diagram.
# ----------------------------------------------------------------------
def fixed_point_state(p):
    """6-D field-free fixed point [y0,y1,y2,0,0,0] for each p (shape N),
    solving the self-consistent equation for v=y1-y2 (lowest/resting branch)."""
    p=np.atleast_1d(np.asarray(p,float)); Y=np.zeros((p.shape[0],6))
    for i,pp in enumerate(p):
        def F(v):
            y0=(A/a)*Sigm(v); y1=(A/a)*(pp+C2*Sigm(C1*y0)); y2=(B/b)*(C4*Sigm(C3*y0))
            return y1-y2-v
        vs=np.linspace(-20,40,2000); Fs=F(vs)
        idx=np.where(Fs[:-1]*Fs[1:]<0)[0]
        v=brentq(F,vs[idx[0]],vs[idx[0]+1]) if len(idx) else vs[np.argmin(np.abs(Fs))]
        y0=(A/a)*Sigm(v); y1=(A/a)*(pp+C2*Sigm(C1*y0)); y2=(B/b)*(C4*Sigm(C3*y0))
        Y[i,:3]=[y0,y1,y2]
    return Y

def freefield_minmax(p, dt=2e-4, t_settle=4.0, t_meas=2.0, seed_kick=1e-2):
    """Integrate with no field for each p (shape N); return (vmin,vmax,vmean)
    of v=y1-y2 over the measurement window. Each run starts at its fixed point
    plus a tiny kick: above the Hopf it stays put (flat band), below it the
    limit cycle grows -- giving a clean bifurcation diagram."""
    N=p.shape[0]; Y=fixed_point_state(p); Y[:,1]+=seed_kick; z=np.zeros(N)
    for _ in range(int(t_settle/dt)):
        k1=rhs(Y,p,z); k2=rhs(Y+0.5*dt*k1,p,z)
        k3=rhs(Y+0.5*dt*k2,p,z); k4=rhs(Y+dt*k3,p,z)
        Y=Y+(dt/6.0)*(k1+2*k2+2*k3+k4)
    nm=int(t_meas/dt); vmin=np.full(N,np.inf); vmax=np.full(N,-np.inf); acc=np.zeros(N)
    for _ in range(nm):
        k1=rhs(Y,p,z); k2=rhs(Y+0.5*dt*k1,p,z)
        k3=rhs(Y+0.5*dt*k2,p,z); k4=rhs(Y+dt*k3,p,z)
        Y=Y+(dt/6.0)*(k1+2*k2+2*k3+k4)
        v=Y[:,1]-Y[:,2]; vmin=np.minimum(vmin,v); vmax=np.maximum(vmax,v); acc+=v
    return vmin, vmax, acc/nm

if __name__=="__main__":
    fc   = 100.0     # carrier (Hz)
    m    = 1.0       # modulation depth
    eps  = 0.3       # field amplitude (mV at the sigmoid) -- linear regime
    dt   = 2e-4
    t_settle, t_meas = 10.0, 3.0

    f_om = np.arange(9.5, 12.501, 0.05)      # envelope freq sweep (Hz)
    Om   = 2*np.pi*f_om
    p_stable = [330.0, 355.0, 395.0]         # forced-resonance side (focus)
    p_cycle  = [310.0, 290.0, 265.0]         # entrainment side (limit cycle)

    def sweep(plist):
        out={}
        for p in plist:
            pv=np.full_like(Om,p)
            out[p]=integrate(pv,Om,eps,m,fc,t_settle,t_meas,dt)
            print(f"  p={p:.0f}  max-resp={out[p].max():.3f} mV at {f_om[np.argmax(out[p])]:.2f} Hz")
        return out
    print("Stable (forced-resonance) side:"); rs=sweep(p_stable)
    print("Limit-cycle (entrainment) side:"); rc=sweep(p_cycle)
    np.savez("sweep_results.npz", f_om=f_om, p_stable=p_stable, p_cycle=p_cycle,
             rs=np.array([rs[p] for p in p_stable]),
             rc=np.array([rc[p] for p in p_cycle]),
             fc=fc, m=m, eps=eps)
    print("saved sweep_results.npz")
