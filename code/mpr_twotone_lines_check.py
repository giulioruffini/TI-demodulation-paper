"""One MPR population (tau=1, Delta=1) driven by two tones at 1000+-5 Hz (tau=15 ms), current coupling.
Measures in the RATE: the carrier line, the beat line and the DC shift; compares with the chain
membrane -> v^2 -> rate readout, and with NMM1 on the same membrane."""
import numpy as np
D=1.0; Q=-1.0; TAU_MS=15.0
def F(Q): return np.sqrt((Q+np.sqrt(Q*Q+D*D))/2)/np.pi
def Fp(Q,h=1e-5): return (F(Q+h)-F(Q-h))/(2*h)
def Fpp(Q,h=1e-4): return (F(Q+h)-2*F(Q)+F(Q-h))/h**2
r0=F(Q); v0=-D/(2*np.pi*r0); d=D/(np.pi*r0); nu=2*np.pi*r0
Hv=lambda w:(1j*w+d)/((1j*w+d)**2+nu**2); Hr=lambda w:2*r0*Hv(w)/(1j*w+d)
C=lambda w:r0*(w*w+3*d*d-nu*nu)/((d*d+nu*nu)*((d*d+nu*nu-w*w)**2+4*d*d*w*w))
fc=1000.0; df=10.0; w1=2*np.pi*(fc-df/2)*TAU_MS*1e-3; w2=2*np.pi*(fc+df/2)*TAU_MS*1e-3; Om=w2-w1; a=0.5
def rhs(y,t):
    r,v=y; I=a*np.cos(w1*t)+a*np.cos(w2*t)
    return np.array([D/np.pi+2*r*v, v*v+Q-np.pi**2*r*r+I])
dt=2*np.pi/w2/60; Tset=60.0; ncyc=30; Tmeas=ncyc*2*np.pi/Om
n=int((Tset+Tmeas)/dt); y=np.array([r0,v0]); t=0.0; acc={}
def lock(): return {k:np.zeros(2) for k in ('w1','Om')}
L=lock(); R=lock(); rsum=0.0; nm=0   # R: reference sums, to remove DC leakage exactly
for i in range(n):
    k1=rhs(y,t); k2=rhs(y+0.5*dt*k1,t+0.5*dt); k3=rhs(y+0.5*dt*k2,t+0.5*dt); k4=rhs(y+dt*k3,t+dt)
    y=y+dt*(k1+2*k2+2*k3+k4)/6; t+=dt
    if t>Tset:
        r=y[0]; rsum+=r; nm+=1
        c1=np.array([np.cos(w1*t),np.sin(w1*t)]); cO=np.array([np.cos(Om*t),np.sin(Om*t)])
        L['w1']+=r*c1; L['Om']+=r*cO; R['w1']+=c1; R['Om']+=cO
rbar=rsum/nm
amp=lambda k:2*np.hypot(*(L[k]-rbar*R[k]))/nm
car_sim=amp('w1'); beat_sim=amp('Om'); dc_sim=rbar-r0
car_pred=a*abs(Hr(w1)); beat_pred=(a*a/(w1*w2))*abs(Hr(Om)); dc_pred=a*a*(C(w1)+C(w2))
# NMM1 on the same membrane: static curve F on the membrane-filtered drive (normalized to DC)
g=lambda w:abs(Hv(w)/Hv(1e-9))
car_nmm1=Fp(Q)*a*g(w1); beat_nmm1=0.5*Fpp(Q)*a*a*g(w1)*g(w2)
print(f"Q={Q}, r*={r0:.3f} ({r0/TAU_MS*1e3:.1f} Hz), d={d:.2f}, nu={nu:.2f}; tones {fc-df/2:.0f}/{fc+df/2:.0f} Hz -> w*tau={w1:.1f}/{w2:.1f}, Omega*tau={Om:.2f}")
print(f"membrane excursion per tone a/(w tau) = {a/w1:.2e}  (a={a})")
print(f"{'quantity in the RATE':28s} {'sim':>11s} {'chain pred.':>12s} {'NMM1 same membr.':>17s} {'NMM2/NMM1':>10s}")
print(f"{'carrier line at w1':28s} {car_sim:11.3e} {car_pred:12.3e} {car_nmm1:17.3e} {car_sim/car_nmm1:10.3f}")
print(f"{'beat line at Omega':28s} {beat_sim:11.3e} {beat_pred:12.3e} {beat_nmm1:17.3e} {beat_sim/beat_nmm1:10.3f}")
print(f"{'DC shift':28s} {dc_sim:11.3e} {dc_pred:12.3e} {'':17s}")
print(f"static-curve gain F' a = {Fp(Q)*a:.3e}  (what a sigmoid with NO membrane would put at w1)")
print(f"predicted NMM2/NMM1 beat ratio d^2/(3d^2-nu^2) = {d*d/(3*d*d-nu*nu):.3f}")
