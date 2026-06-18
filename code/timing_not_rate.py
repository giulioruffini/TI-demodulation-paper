"""Timing, not rate (Jansen-Rit). At FIXED detection (pinned v*, so sigma'' is
constant) we drive the column toward the Hopf through the coupling C and read out,
at the resonant beat Df=f0(C):
  - AC : lock-in amplitude at Df of the LFP v=y1-y2  (the envelope-locked response),
  - DC : shift of the mean pyramidal firing rate <Sigma(v)> from its field-free value.
The network transfer is G(Om)~[(w0^2-Om^2)^2+(2*g*Om)^2]^{-1/2}: at Om=w0 it is
~1/(2*g*w0) (diverges as the Hopf is approached, g->0), while at Om=0 it is ~1/w0^2
(flat). So the AC entrains and is resonantly amplified ~1/g, while the DC mean-rate
shift is not -- matching the in-vivo finding that TI alters spike timing, not rate
(Vieira 2024).

Self-contained (pure numpy; bisection root-finder so no scipy). The JR dynamics and
the pinned-v* construction p(C) match jr_jsweep_engine.py used for the J-curve."""
import numpy as np, sys, os

# --- Jansen-Rit constants (Table 1) ---
A, B = 3.25, 22.0; a, b = 100.0, 50.0; v0, e0, rr = 6.0, 2.5, 0.56

def Sigm(v):  return 2*e0/(1+np.exp(rr*(v0-v)))

def p_of_C(vstar, C):
    """External drive p that pins the field-free fixed point at v=vstar, given C."""
    y0 = (A/a)*Sigm(vstar)
    return (a/A)*(vstar+(B/b)*0.25*C*Sigm(0.25*C*y0)) - 0.8*C*Sigm(C*y0)

def rhs(Y, p, C, sf):
    C1 = C; C2 = 0.8*C; C3 = 0.25*C; C4 = 0.25*C
    y0, y1, y2, y3, y4, y5 = Y.T; d = np.empty_like(Y)
    d[:, 0] = y3; d[:, 1] = y4; d[:, 2] = y5
    d[:, 3] = A*a*Sigm(y1-y2+sf)    - 2*a*y3 - a*a*y0
    d[:, 4] = A*a*(p+C2*Sigm(C1*y0)) - 2*a*y4 - a*a*y1
    d[:, 5] = B*b*(C4*Sigm(C3*y0))   - 2*b*y5 - b*b*y2
    return d

def field(t, eps, m, Om, fc): return eps*(1+m*np.cos(Om*t))*np.cos(2*np.pi*fc*t)

def _fp_v(p, C):
    """Field-free fixed-point v=y1-y2 via bracketing + bisection (replaces brentq)."""
    C2 = 0.8*C; C3 = 0.25*C; C4 = 0.25*C
    def F(v):
        y0 = (A/a)*Sigm(v); y1 = (A/a)*(p+C2*Sigm(C*y0)); y2 = (B/b)*(C4*Sigm(C3*y0))
        return y1-y2-v
    vs = np.linspace(-20, 40, 3000); Fs = F(vs)
    idx = np.where(Fs[:-1]*Fs[1:] < 0)[0]
    if not len(idx):
        return vs[np.argmin(np.abs(Fs))]
    lo, hi = vs[idx[0]], vs[idx[0]+1]; flo = F(lo)
    for _ in range(200):
        mid = 0.5*(lo+hi); fm = F(mid)
        if flo*fm <= 0: hi = mid
        else: lo = mid; flo = fm
        if hi-lo < 1e-12: break
    return 0.5*(lo+hi)

def jac_eig(p, C, h=1e-6):
    """Returns (v*, damping gamma=-Re lambda, |Im lambda|) of the leading eigenpair."""
    v = _fp_v(p, C); C2 = 0.8*C; C3 = 0.25*C; C4 = 0.25*C
    y0 = (A/a)*Sigm(v); y1 = (A/a)*(p+C2*Sigm(C*y0)); y2 = (B/b)*(C4*Sigm(C3*y0))
    x = np.array([y0, y1, y2, 0, 0, 0]); Jm = np.zeros((6, 6))
    f = lambda xx: rhs(xx[None, :], np.array([p]), np.array([C]), np.array([0.0]))[0]
    for j in range(6):
        dx = np.zeros(6); dx[j] = h; Jm[:, j] = (f(x+dx)-f(x-dx))/(2*h)
    ev = np.linalg.eigvals(Jm); i = np.argmax(ev.real)
    return v, -ev[i].real, abs(ev[i].imag)

def run(p, C, Om, eps, m, fc, t_set, t_meas, dt):
    """Vectorized over the parameter axis. Returns (AC lock-in at Om, mean rate)."""
    N = len(p); Y = np.zeros((N, 6)); t = 0.0
    ns = int(t_set/dt); nm = int(t_meas/dt)
    for _ in range(ns):
        s1 = field(t, eps, m, Om, fc); k1 = rhs(Y, p, C, s1)
        s2 = field(t+.5*dt, eps, m, Om, fc); k2 = rhs(Y+.5*dt*k1, p, C, s2)
        k3 = rhs(Y+.5*dt*k2, p, C, s2)
        s3 = field(t+dt, eps, m, Om, fc); k4 = rhs(Y+dt*k3, p, C, s3)
        Y = Y + (dt/6)*(k1+2*k2+2*k3+k4); t += dt
    w = np.hanning(nm); ws = w.sum()
    ac = np.zeros(N); as_ = np.zeros(N); av = np.zeros(N)
    awc = np.zeros(N); aws = np.zeros(N); arate = np.zeros(N)
    for k in range(nm):
        s1 = field(t, eps, m, Om, fc); k1 = rhs(Y, p, C, s1)
        s2 = field(t+.5*dt, eps, m, Om, fc); k2 = rhs(Y+.5*dt*k1, p, C, s2)
        k3 = rhs(Y+.5*dt*k2, p, C, s2)
        s3 = field(t+dt, eps, m, Om, fc); k4 = rhs(Y+dt*k3, p, C, s3)
        Y = Y + (dt/6)*(k1+2*k2+2*k3+k4); t += dt
        v = Y[:, 1]-Y[:, 2]; co = np.cos(Om*t); si = np.sin(Om*t)
        ac += w[k]*v*co; as_ += w[k]*v*si; av += w[k]*v
        awc += w[k]*co; aws += w[k]*si; arate += w[k]*Sigm(v)
    vb = av/ws; c = ac-vb*awc; s = as_-vb*aws
    AC = 2/ws*np.sqrt(c**2+s**2)
    return AC, arate/ws

if __name__ == "__main__":
    HERE = os.path.dirname(os.path.abspath(__file__))
    vstar = 8.30; m = 1.0; fc = 100.0; eps = 0.3
    dt = 2e-4; t_set = 18.0; t_meas = 20.0
    quick = "--quick" in sys.argv
    if quick:
        t_set = 8.0; t_meas = 8.0
    # locate the alpha Hopf C* (gamma=0) by bisection (scipy-free), then sample C
    # geometrically toward it so the steep 1/gamma rise -- and the noisier near-Hopf DC
    # behaviour -- are well resolved (was a sparse linear grid).
    lo, hi = 130.0, 137.0
    for _ in range(60):
        mid = 0.5 * (lo + hi)
        if jac_eig(p_of_C(vstar, mid), mid)[1] > 0: lo = mid
        else: hi = mid
    Chopf = 0.5 * (lo + hi)
    Cs = np.sort(Chopf - np.geomspace(0.25, Chopf - 120.0, 6 if quick else 26))
    ps = np.array([p_of_C(vstar, C) for C in Cs])
    gam = np.zeros_like(Cs); om = np.zeros_like(Cs)
    for i, C in enumerate(Cs):
        _, g, o = jac_eig(ps[i], C); gam[i] = g; om[i] = o
    Om = om.copy()                       # drive at the (per-C) eigenfrequency = resonance
    AC, rate_on = run(ps, Cs, Om, eps, m, fc, t_set, t_meas, dt)
    rate_off = Sigm(vstar)               # pinned field-free fixed point -> constant baseline
    DC = rate_on - rate_off
    print("  C      p       gamma   f0(Hz)   AC(mV)      DC_rate(Hz)   |AC/DC|")
    for i in range(len(Cs)):
        print(f"{Cs[i]:7.2f}{ps[i]:8.2f}{gam[i]:8.3f}{om[i]/2/np.pi:8.2f}"
              f"{AC[i]:12.4e}{DC[i]:13.3e}{abs(AC[i]/DC[i]):9.1f}")
    np.savez(os.path.join(HERE, "timing_not_rate.npz"),
             Cs=Cs, ps=ps, gam=gam, om=om, AC=AC, DC=DC, rate_on=rate_on,
             rate_off=rate_off, vstar=vstar, eps=eps, m=m, fc=fc)
    print("saved timing_not_rate.npz")
