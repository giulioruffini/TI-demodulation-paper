"""Static-to-fast crossover of the MPR detector, and the fast-carrier approximation in the
manuscript's PING mean field (added 2026-09-22 for the v0.14 revision).

Three computations, all perturbative in the field amplitude unless stated:

 1. Uncoupled MPR population (tau = 1, J = 0), current forcing a cos(w t). The second-order
    DC rate shift is a^2 C(Q, w) with the closed form (Kaiti's review brief N4.1, checked here
    against the resolvent/Hessian matrix calculation)
        C(Q, w) = r [w^2 + 3 d^2 - nu^2] / ((d^2 + nu^2) {[d^2 + nu^2 - w^2]^2 + 4 d^2 w^2}),
    r = F(Q), d = Delta/(pi r), nu = 2 pi r. Limits: C -> F''(Q)/4 as w -> 0 (the static
    transfer curvature) and C -> F'(Q)/(2 w^2) as w -> inf (Kapitza: the v^2 term acting on the
    integrator-limit voltage excursion, read through the slope). Sign change at
    w_z = sqrt(nu^2 - 3 d^2) when Q > Delta/sqrt(3).
 2. Independent RK4 integrations of the same population at finite amplitude, averaged over
    whole carrier periods, against C(Q, w).
 3. The eight-state PING of Eq. (nmm2-ping): at four stable operating points and two tones
    centred at 300, 1000 and 2000 Hz, the exact second-order complex beat response (full
    Hessian source, full resolvent) against the fast-carrier approximation in which each
    tone's voltage phasor is a_j/(i w_j tau_E) and only the v_E^2 mixing term is kept.
    Ported from crossover_review_checks.py (Kaiti, review v2, 2026-09-22); conventions are the
    manuscript's (time in ms, unit current per tone in the tau_E-divided voltage equation).

Writes ping_fast_carrier_check.json (consumed by mpr_crossover_fig.py) and prints a summary.
Pure numpy/scipy; runs in about a minute.
"""
import json, os
import numpy as np
from scipy.optimize import root

HERE = os.path.dirname(os.path.abspath(__file__))
D = 1.0

# ---------------------------------------------------------------- 1. uncoupled MPR
def F(Q):   return np.sqrt((Q + np.hypot(Q, D)) / 2) / np.pi
def Fp(Q):  return F(Q) / (2 * np.hypot(Q, D))
def Fpp(Q): return F(Q) / (4 * np.hypot(Q, D) ** 3) * (np.hypot(Q, D) - 2 * Q)

def params(Q):
    r = F(Q); return r, D / (np.pi * r), 2 * np.pi * r          # r*, d (relaxation), nu (ringing)

def C_closed(Q, w):
    r, d, nu = params(Q); s = d * d + nu * nu
    return r * (w * w + 3 * d * d - nu * nu) / (s * ((s - w * w) ** 2 + 4 * d * d * w * w))

def C_matrix(Q, w):
    r, d, _ = params(Q)
    A = np.array([[-d, 2 * r], [-2 * np.pi ** 2 * r, -d]])
    R, V = np.linalg.solve(1j * w * np.eye(2) - A, [0.0, 1.0])
    q = [np.real(R * np.conj(V)), (abs(V) ** 2 - np.pi ** 2 * abs(R) ** 2) / 2]
    return float(-np.linalg.solve(A, q)[0])

def zero_crossing(Q):
    r, d, nu = params(Q); x = nu * nu - 3 * d * d
    return float(np.sqrt(x)) if x > 0 else None

def simulate(Q, w, a=0.05, dt_max=0.002):
    """RK4, whole-period average of r over >= 12 periods (and >= 30/d), after settling >= 35/d."""
    r0, d, _ = params(Q); v0 = -D / (2 * np.pi * r0)
    P = 2 * np.pi / w; steps = int(np.ceil(P / dt_max)); dt = P / steps
    n0 = max(2, int(np.ceil((35 / d) / P))) * steps
    n1 = max(12, int(np.ceil((30 / d) / P))) * steps
    r, v, acc = r0, v0, 0.0
    for i in range(n0 + n1):
        t = i * dt
        def f(rr, vv, tt): return D / np.pi + 2 * rr * vv, vv * vv + Q + a * np.cos(w * tt) - np.pi ** 2 * rr * rr
        k1 = f(r, v, t); k2 = f(r + dt / 2 * k1[0], v + dt / 2 * k1[1], t + dt / 2)
        k3 = f(r + dt / 2 * k2[0], v + dt / 2 * k2[1], t + dt / 2); k4 = f(r + dt * k3[0], v + dt * k3[1], t + dt)
        if i >= n0:
            acc += dt * (r + 2 * (r + dt / 2 * k1[0]) + 2 * (r + dt / 2 * k2[0]) + (r + dt * k3[0])) / 6
        r += dt * (k1[0] + 2 * k2[0] + 2 * k3[0] + k4[0]) / 6
        v += dt * (k1[1] + 2 * k2[1] + 2 * k3[1] + k4[1]) / 6
    return (acc / (n1 * dt) - r0) / (a * a), dt, n0 * dt, n1 * dt

# ---------------------------------------------------------------- 3. PING (Eq. nmm2-ping)
TE, TI, TA, TG = 15.0, 7.5, 10.0, 2.5

def ping_equilibrium(C, eta):
    def eqs(rs):
        r, s = rs; v = -1 / (2 * np.pi * TE * r); z = -1 / (2 * np.pi * TI * s)
        return [(eta - (np.pi * TE * r) ** 2 + v * v) / TE + C * (r - s),
                (eta - (np.pi * TI * s) ** 2 + z * z) / TI + C * (r - 2 * s)]
    sol = root(eqs, [0.09, 0.045])
    if not sol.success or np.min(sol.x) <= 0:
        raise RuntimeError(sol.message)
    r, s = sol.x
    return np.array([r, -1 / (2 * np.pi * TE * r), s, -1 / (2 * np.pi * TI * s), r, 0.0, s, 0.0])

def ping_jacobian(x, C):
    r, v, s, z, *_ = x; A = np.zeros((8, 8))
    A[0, 0] = 2 * v / TE; A[0, 1] = 2 * r / TE
    A[1, 0] = -2 * np.pi ** 2 * TE * r; A[1, 1] = 2 * v / TE; A[1, 4] = C; A[1, 6] = -C
    A[2, 2] = 2 * z / TI; A[2, 3] = 2 * s / TI
    A[3, 2] = -2 * np.pi ** 2 * TI * s; A[3, 3] = 2 * z / TI; A[3, 4] = C; A[3, 6] = -2 * C
    A[4, 5] = 1 / TA; A[5, 0] = 1 / TA; A[5, 4] = -1 / TA; A[5, 5] = -2 / TA
    A[6, 7] = 1 / TG; A[7, 2] = 1 / TG; A[7, 6] = -1 / TG; A[7, 7] = -2 / TG
    return A

def ping_hessian(a, b):
    """Bilinear form D^2 f (x*)[a, b] of the PING right-hand side (only the MPR quadratics)."""
    q = np.zeros(8, complex)
    for k, t in ((0, TE), (2, TI)):
        q[k] = 2 / t * (a[k] * b[k + 1] + a[k + 1] * b[k])
        q[k + 1] = 2 / t * a[k + 1] * b[k + 1] - 2 * np.pi ** 2 * t * a[k] * b[k]
    return q

def ping_checks(states=((13.5, 0.0), (15.0, 0.0), (16.0, 0.0), (15.0, 0.85)), carriers=(300.0, 1000.0, 2000.0)):
    out = []
    for C, eta in states:
        x = ping_equilibrium(C, eta); A = ping_jacobian(x, C); eig = np.linalg.eigvals(A)
        fHz = eig.imag * 1000 / (2 * np.pi)
        modes = eig[(eig.imag > 0) & (fHz > 25) & (fHz < 90)]
        e = modes[np.argmax(modes.real)]; Om = abs(e.imag)
        assert np.max(eig.real) < 0, "operating point must be a stable focus"
        b = np.zeros(8); b[1] = 1 / TE                     # unit current per tone, tau_E-divided equation
        for fc in carriers:
            wc = 2 * np.pi * fc / 1000; w1, w2 = wc - Om / 2, wc + Om / 2
            q1 = np.linalg.solve(1j * w1 * np.eye(8) - A, b)
            q2 = np.linalg.solve(1j * w2 * np.eye(8) - A, b)
            d = 0.5 * ping_hessian(q2, np.conj(q1))          # exact quadratic difference-frequency source
            d0 = b / (TE ** 2 * w1 * w2)                     # fast-carrier limit: v_j ~ a_j/(i w_j tau_E), v_E^2 only
            y = np.linalg.solve(1j * Om * np.eye(8) - A, d)[0]
            y0 = np.linalg.solve(1j * Om * np.eye(8) - A, d0)[0]
            out.append(dict(C=C, eta=eta, r_E=float(x[0]), v_E=float(x[1]), gamma_per_ms=float(-e.real),
                            beat_Hz=float(Om * 1000 / (2 * np.pi)), fc_Hz=fc,
                            exact_y=[float(y.real), float(y.imag)], fast_y=[float(y0.real), float(y0.imag)],
                            relative_error=float(abs(y0 - y) / abs(y)),
                            source_exact_vE=float(abs(d[1])), source_fast_vE=float(abs(d0[1]))))
    return out

if __name__ == "__main__":
    # 1. closed form vs matrix method
    Qs = np.linspace(-3, 6, 91); ws = np.logspace(-2, 2.5, 46)
    err = max(abs(C_closed(Q, w) - C_matrix(Q, w)) for Q in Qs for w in ws)
    print(f"closed form vs resolvent/Hessian: max |diff| = {err:.2e} over {len(Qs)*len(ws)} (Q, w) pairs")
    # 2. finite-amplitude simulations
    sims = []
    for Q in (0.0, 3.0):
        for w in (0.1, 1.0, 3.2, 6.4, 25.6):
            sim, dt, ts, tm = simulate(Q, w)
            tgt = C_closed(Q, w)
            sims.append(dict(Q=Q, w=w, a=0.05, dt=dt, settle=ts, measure=tm, sim=float(sim), closed=float(tgt),
                             rel=float((sim - tgt) / tgt) if tgt != 0 else None))
            print(f"  Q={Q:.1f} w={w:5.1f}: sim {sim:+.6f}  closed {tgt:+.6f}  rel {(sim-tgt)/tgt:+.2e}")
    # 3. PING
    ping = ping_checks()
    for p in ping:
        print(f"  PING C={p['C']:4.1f} eta={p['eta']:.2f} f0={p['beat_Hz']:5.1f} Hz gamma={p['gamma_per_ms']:.4f}/ms "
              f"fc={p['fc_Hz']:6.0f} Hz: relative error of the fast-carrier form {100*p['relative_error']:.3f}%")
    limits = {str(Q): dict(Fp=float(Fp(Q)), Fpp=float(Fpp(Q)), r=float(F(Q)), d=float(params(Q)[1]),
                           nu=float(params(Q)[2]), w_zero=zero_crossing(Q)) for Q in (0.0, D / np.sqrt(3), 3.0)}
    json.dump(dict(closed_vs_matrix_max_abs_diff=float(err), simulations=sims, ping=ping, limits=limits,
                   tau_E_ms=TE, note="see module docstring; ported from Kaiti's crossover_review_checks.py"),
              open(os.path.join(HERE, "ping_fast_carrier_check.json"), "w"), indent=1)
    print("wrote ping_fast_carrier_check.json")
