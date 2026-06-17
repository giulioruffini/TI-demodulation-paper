"""
Stage A: locate the Jansen-Rit Hopf bifurcation in the external-input
parameter p, and read off the natural (alpha-band) frequency there.

Standard Jansen-Rit parameters (Jansen & Rit 1995; Grimbert & Faugeras 2006).
"""
import numpy as np
from scipy.optimize import brentq

# --- parameters ---
A, B = 3.25, 22.0          # mV  (excitatory / inhibitory PSP gains)
a, b = 100.0, 50.0         # 1/s (synaptic rates)
v0, e0, r = 6.0, 2.5, 0.56 # sigmoid: half-max potential, max rate, slope
C = 135.0
C1, C2, C3, C4 = C, 0.8*C, 0.25*C, 0.25*C

def Sigm(v):
    return 2.0*e0/(1.0+np.exp(r*(v0-v)))

def rhs(x, p):
    y0,y1,y2,y3,y4,y5 = x
    d = np.empty(6)
    d[0]=y3
    d[1]=y4
    d[2]=y5
    d[3]=A*a*Sigm(y1-y2)        - 2*a*y3 - a*a*y0
    d[4]=A*a*(p + C2*Sigm(C1*y0))- 2*a*y4 - a*a*y1
    d[5]=B*b*(C4*Sigm(C3*y0))   - 2*b*y5 - b*b*y2
    return d

def fixed_point(p):
    # self-consistent solve for v = y1 - y2
    def F(v):
        y0 = (A/a)*Sigm(v)
        y1 = (A/a)*(p + C2*Sigm(C1*y0))
        y2 = (B/b)*(C4*Sigm(C3*y0))
        return y1 - y2 - v
    # bracket
    vs = np.linspace(-20, 40, 4000)
    Fs = np.array([F(v) for v in vs])
    roots=[]
    for i in range(len(vs)-1):
        if Fs[i]==0 or Fs[i]*Fs[i+1]<0:
            roots.append(brentq(F, vs[i], vs[i+1]))
    # return lowest branch fixed point (the resting one)
    return roots

def state_from_v(v, p):
    y0 = (A/a)*Sigm(v)
    y1 = (A/a)*(p + C2*Sigm(C1*y0))
    y2 = (B/b)*(C4*Sigm(C3*y0))
    return np.array([y0,y1,y2,0,0,0])

def jacobian(x, p, eps=1e-6):
    n=6; J=np.zeros((n,n)); f0=rhs(x,p)
    for j in range(n):
        dx=np.zeros(n); dx[j]=eps
        J[:,j]=(rhs(x+dx,p)-rhs(x-dx,p))/(2*eps)
    return J

print("p   n_fp   maxRe(lambda)   Im@maxRe[Hz]")
ps=np.arange(0,400.01,2.0)
records=[]
for p in ps:
    roots=fixed_point(p)
    # use the lowest-v (resting) branch for stability tracking
    v=roots[0]
    x=state_from_v(v,p)
    ev=np.linalg.eigvals(jacobian(x,p))
    i=np.argmax(ev.real)
    records.append((p, len(roots), ev[i].real, abs(ev[i].imag)/(2*np.pi)))

records=np.array(records)
# find Hopf: max-real-part crosses zero
re=records[:,2]
for k in range(len(re)-1):
    if re[k]<0 and re[k+1]>=0:
        p_lo,p_hi=records[k,0],records[k+1,0]
        # refine
        def maxre(p):
            v=fixed_point(p)[0]; x=state_from_v(v,p)
            return np.max(np.linalg.eigvals(jacobian(x,p)).real)
        p_h=brentq(maxre,p_lo,p_hi,xtol=1e-3)
        v=fixed_point(p_h)[0]; x=state_from_v(v,p_h)
        ev=np.linalg.eigvals(jacobian(x,p_h))
        i=np.argmax(ev.real); f0=abs(ev[i].imag)/(2*np.pi)
        print(f"\n>>> Hopf near p={p_h:.2f}  f0={f0:.2f} Hz  (resting-branch crossing)")

# print a coarse table
for rec in records[::8]:
    print(f"{rec[0]:5.0f}  {int(rec[1])}     {rec[2]:+8.2f}      {rec[3]:6.2f}")
