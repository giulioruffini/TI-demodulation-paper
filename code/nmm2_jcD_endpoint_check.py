"""
S10 endpoint check: stability of the fully forced NMM2 J-curve states (review brief, Oct 5, 2026).

S10 (nmm2_jcD.py) drives the PING mean field at eta = 0 with the AM surrogate
A(1 + cos Omega t) cos(omega_c t), A = 8, carrier 300 Hz, beat at the per-coupling peak
(50.5 Hz at the last seven couplings), dt = 0.05 ms, 600 ms settling, 1200 ms window.
Kaiti's DC-only averaged-equilibrium screen (ping_other_sweeps_screen.py) finds the
averaged point unstable at the last five couplings. That screen does not test the
periodically forced solution. Here, for the last seven couplings and two references:
  (i)   the largest Lyapunov exponent of the forced system along the driven trajectory
        (tangent vector integrated with the field-free Jacobian, which is exact because
        the field enters additively), over the published 1200 ms window and a 4800 ms check;
  (ii)  the decay rate of a small perturbation applied after settling;
  (iii) the amplitude spectrum of r_E: lines at the beat and its harmonics against the
        largest line in 40-60 Hz more than 1.5 Hz from the beat;
  (iv)  the lock-in amplitude at the beat, checked against the cached S10 peak.
A negative Lyapunov exponent and a decaying perturbation mean the driven state is an
attracting (quasi-periodic) forced response; an exponent at zero within resolution would
mean an autonomous component.
Output: ../docs/r7_s10_endpoint_check_2026-10-05.json
"""
import os, sys, json
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import nmm2_jcA as J
import ping_fast_carrier_check as P


def jac(y, C):
    return P.ping_jacobian(y, C)


def step_pair(y, d, t, dt, eta, C, Amp, Om, wc):
    """RK4 on the state and on a tangent vector d (linearized about the stage states)."""
    a = (eta, C, Amp, Om, wc)
    k1 = J.rhs(y, t, *a);            l1 = jac(y, C) @ d
    y2 = y + .5 * dt * k1;           k2 = J.rhs(y2, t + .5 * dt, *a); l2 = jac(y2, C) @ (d + .5 * dt * l1)
    y3 = y + .5 * dt * k2;           k3 = J.rhs(y3, t + .5 * dt, *a); l3 = jac(y3, C) @ (d + .5 * dt * l2)
    y4 = y + dt * k3;                k4 = J.rhs(y4, t + dt, *a);      l4 = jac(y4, C) @ (d + dt * l3)
    return y + (dt / 6) * (k1 + 2 * k2 + 2 * k3 + k4), d + (dt / 6) * (l1 + 2 * l2 + 2 * l3 + l4)


def diagnose(C, beat_Hz, Amp=8.0, fc_Hz=300.0, dt=0.05, t_set=600.0, t_meas=1200.0, t_long=4800.0, eps=1e-4):
    eta = J.ETA; Om = 2 * np.pi * beat_Hz / 1000; wc = 2 * np.pi * fc_Hz / 1000
    x0, re0, ri0 = J.fp(C); gfree, w0 = J.gam_w(x0, C)
    y = J.init(1)[:, 0].copy(); t = 0.0
    for _ in range(int(t_set / dt)):
        y = J.rk4(y, t, dt, eta, C, Amp, Om, wc); t += dt
    # (i) Lyapunov over the window and over the long check; (iv) lock-in; (iii) spectrum
    d = np.random.default_rng(0).normal(size=8); d /= np.linalg.norm(d)
    nm = int(t_meas / dt); nl = int(t_long / dt); re = np.empty(nl); acc = 0.0; lam_win = None
    renorm = int(1.0 / dt)
    for k in range(nl):
        y, d = step_pair(y, d, t, dt, eta, C, Amp, Om, wc); t += dt; re[k] = y[0]
        if (k + 1) % renorm == 0:
            nrm = np.linalg.norm(d); acc += np.log(nrm); d /= nrm
        if k + 1 == nm:
            lam_win = acc / t_meas
    lam_long = acc / t_long
    w = np.hanning(nm); r = re[:nm]; mean = r.mean()
    tt = np.arange(1, nm + 1) * dt + t_set
    c = ((r - mean) * w * np.cos(Om * tt)).sum(); s = ((r - mean) * w * np.sin(Om * tt)).sum()
    lockin = 2 * np.hypot(c, s) / w.sum()
    X = 2 * np.abs(np.fft.rfft((r - mean) * w)) / w.sum() / mean; f = np.fft.rfftfreq(nm, dt / 1000)
    jb = np.argmin(np.abs(f - beat_Hz)); j2 = np.argmin(np.abs(f - 2 * beat_Hz))
    band = (f >= 40) & (f <= 60) & (np.abs(f - beat_Hz) > 1.5)
    kk = np.argmax(X[band]); other, f_other = X[band][kk], f[band][kk]
    # (ii) perturbation decay after settling: two trajectories, same forcing
    ya = J.init(1)[:, 0].copy(); t2 = 0.0
    for _ in range(int(t_set / dt)):
        ya = J.rk4(ya, t2, dt, eta, C, Amp, Om, wc); t2 += dt
    yb = ya.copy(); yb[0] += eps * ya[0]
    n2 = int(t_meas / dt); dev = np.empty(n2)
    for k in range(n2):
        ya = J.rk4(ya, t2, dt, eta, C, Amp, Om, wc); yb = J.rk4(yb, t2, dt, eta, C, Amp, Om, wc); t2 += dt
        dev[k] = np.linalg.norm(yb - ya)
    # envelope decay rate from the log of the deviation, fitted over the window (after 100 ms)
    tdev = np.arange(1, n2 + 1) * dt; m = tdev > 100.0
    slope = np.polyfit(tdev[m], np.log(dev[m] + 1e-300), 1)[0]
    return dict(C=float(C), beat_Hz=float(beat_Hz), gamma_free_per_ms=float(gfree), mode_free_Hz=float(w0 * 1000 / (2 * np.pi)),
                lyapunov_window_per_ms=float(lam_win), lyapunov_long_per_ms=float(lam_long),
                perturbation_decay_per_ms=float(slope), lockin_at_beat=float(lockin), mean_rE=float(mean),
                beat_depth=float(X[jb]), beat_2nd_harmonic_depth=float(X[j2]), other_line_depth=float(other), other_line_Hz=float(f_other),
                rE_min=float(r.min()), rE_max=float(r.max()), t_meas_ms=t_meas, t_long_ms=t_long)


if __name__ == '__main__':
    cache = np.load(os.path.join(HERE, 'nmm2_jcD.npz'))
    screen = json.load(open(os.path.join(HERE, '..', 'docs', 'r7_other_sweeps_screen_2026-10-05.json')))['jcurve']
    idx = [0, 10] + list(range(len(cache['C']) - 7, len(cache['C'])))
    rows = []
    for i in idx:
        C, fpk, peak = float(cache['C'][i]), float(cache['fpk'][i]), float(cache['peak'][i])
        r = diagnose(C, fpk); r['cached_peak'] = peak; r['cached_gamma'] = float(cache['gamma'][i])
        r['screen_averaged_growth'] = float(screen[i]['averaged_growth']); r['screen_shift'] = float(screen[i]['shift'])
        rows.append(r)
        print(f"C={C:.5f} beat={fpk:4.1f}: gamma_free={r['gamma_free_per_ms']:.5f}/ms | screen averaged growth {r['screen_averaged_growth']:+.6f} | "
              f"Lyapunov {r['lyapunov_window_per_ms']:+.6f} (1.2 s) {r['lyapunov_long_per_ms']:+.6f} (4.8 s) | perturbation decay {r['perturbation_decay_per_ms']:+.6f}/ms | "
              f"lock-in {r['lockin_at_beat']:.5f} (cache {peak:.5f}) | beat depth {r['beat_depth']:.3f}, 2nd harm {r['beat_2nd_harmonic_depth']:.3f}, other {r['other_line_depth']:.4f} at {r['other_line_Hz']:.2f} Hz", flush=True)
    json.dump(dict(settings=dict(Amp=8.0, fc_Hz=300.0, dt=0.05, t_set=600.0, t_meas=1200.0, t_long=4800.0, eta=0.0, waveform='AM surrogate'),
                   rows=rows), open(os.path.join(HERE, '..', 'docs', 'r7_s10_endpoint_check_2026-10-05.json'), 'w'), indent=1)
    print('wrote json')
