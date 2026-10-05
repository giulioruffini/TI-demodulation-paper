"""
Field-on operating point of the NMM2 PING mean field under two-tone TI (QIF forced
condition of Fig. 10a,b: eta = 0.85, A_f = 35 per tone, f_c = 300 Hz, Delta f = 55 Hz).

Question (review, October 5, 2026): the cached run shows a 51-52.5 Hz line of depth
0.6-0.7 with the field on, absent with it off, in both the spiking network and the exact
mean field. Does the rectified DC shift of the field explain it?

Method. The PING nonlinearities are quadratic (v^2, r^2, r v in the MPR equations), so
the carrier average of the dynamics is exact at second order: the slow variables obey
the field-free equations plus a constant source equal to the DC part of
(1/2) D^2 f[x_1, x_1], where x_1 is the first-order carrier response. For tones of
amplitude a at omega_j entering the tau_E-divided E voltage equation (b = e_v/tau_E),
    x_1 = sum_j a Re[q_j e^{i omega_j t}],  q_j = (i omega_j I - A)^{-1} b,
    s_DC = sum_j (a^2/4) Re D^2 f[q_j, conj(q_j)].
The source acts on E only (I receives no first-order carrier through the synapses to
leading order, and the Hessian keeps whatever it does receive). In the fast-carrier limit
q_j[v_E] -> 1/(i omega_j tau_E), so s_DC[v_E] = a^2/(tau_E (omega tau_E)^2) for two tones,
an E-only drive shift delta_eta_E = a^2/(omega tau_E)^2. The effective operating point
solves f_0(x) + s_DC(x) = 0 self-consistently; its stability is the Jacobian there.

Checks. (i) E-only shift scan to the critical delta_eta_E* and the corresponding a*;
(ii) direct RK4 integration of the mean field (nmm2_ping._rhs, two tones) at several
amplitudes: mean rate against the effective point, and the amplitude spectrum of r_E
(beat line at 55 Hz versus any line in the gamma band away from the beat).

Outputs: ../docs/r7_ping_field_operating_point_2026-10-05.json and
         ../docs/r7_ping_field_spectra_2026-10-05.png
"""
import os, sys, json
import numpy as np
from scipy.optimize import root
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import ping_fast_carrier_check as P
import nmm2_ping as M
M.WAVE = 'twotone'
TE, TI_, TA, TG, C = P.TE, P.TI, P.TA, P.TG, 15.0


def f0(x, eta_E, eta_I):
    """Field-free PING right-hand side with separate E and I background drives."""
    r_e, v_e, r_i, v_i, s_e, z_e, s_i, z_i = x
    return np.array([
        (1.0 / (np.pi * TE) + 2 * r_e * v_e) / TE,
        (eta_E - (np.pi * TE * r_e) ** 2 + v_e ** 2) / TE + C * (s_e - s_i),
        (1.0 / (np.pi * TI_) + 2 * r_i * v_i) / TI_,
        (eta_I - (np.pi * TI_ * r_i) ** 2 + v_i ** 2) / TI_ + C * (s_e - 2 * s_i),
        z_e / TA, (r_e - 2 * z_e - s_e) / TA,
        z_i / TG, (r_i - 2 * z_i - s_i) / TG])


def fixed_point(eta_E, eta_I, src=None, x0=None):
    src = np.zeros(8) if src is None else src
    if x0 is None:
        x0 = P.ping_equilibrium(C, 0.5 * (eta_E + eta_I))
    fun = lambda x: f0(x, eta_E, eta_I) + src
    sol = root(fun, x0, tol=1e-12)
    ok = np.linalg.norm(fun(sol.x)) < 1e-10        # hybr reports failure when started at the solution
    assert ok and sol.x[0] > 0 and sol.x[2] > 0, (sol.message, np.linalg.norm(fun(sol.x)))
    return sol.x


def leading_mode(x):
    eig = np.linalg.eigvals(P.ping_jacobian(x, C))
    k = np.argmax(eig.real)
    return eig[k].real, abs(eig[k].imag) * 1000 / (2 * np.pi), eig


def dc_source(x, a, fc_Hz, df_Hz):
    """Exact second-order DC source of two tones of amplitude a at fc -/+ df/2."""
    A = P.ping_jacobian(x, C); b = np.zeros(8); b[1] = 1 / TE
    w1 = 2 * np.pi * (fc_Hz - df_Hz / 2) / 1000; w2 = 2 * np.pi * (fc_Hz + df_Hz / 2) / 1000
    s = np.zeros(8)
    for w in (w1, w2):
        q = np.linalg.solve(1j * w * np.eye(8) - A, b)
        s += (a * a / 4) * np.real(P.ping_hessian(q, np.conj(q)))
    return s


def effective_point(eta, a, fc_Hz, df_Hz, iters=6, ramp=12):
    """Self-consistent effective point, reached by ramping the amplitude from zero so the
    root solve always starts near its solution (the E-only shift grows as a^2)."""
    x = fixed_point(eta, eta)
    for ak in np.linspace(0.0, a, ramp + 1)[1:]:
        for _ in range(iters):
            s = dc_source(x, ak, fc_Hz, df_Hz)
            x = fixed_point(eta, eta, src=s, x0=x)
    return x, s


def numeric_jacobian(x, eta, a, fc_Hz, df_Hz, h=1e-6):
    """Jacobian of the averaged system including the state dependence of s_DC."""
    J = np.zeros((8, 8))
    for k in range(8):
        xp = x.copy(); xm = x.copy(); xp[k] += h; xm[k] -= h
        J[:, k] = (f0(xp, eta, eta) + dc_source(xp, a, fc_Hz, df_Hz)
                   - f0(xm, eta, eta) - dc_source(xm, a, fc_Hz, df_Hz)) / (2 * h)
    return J


def mf_run(eta, a, fc_Hz, df_Hz, dt=0.05, t_settle=800.0, t_meas=800.0):
    """Direct integration of the mean field (nmm2_ping._rhs, two tones) for a vector of a."""
    a = np.atleast_1d(np.asarray(a, float)); n = a.size
    y = M._init(n); y[:, :] = P.ping_equilibrium(C, eta)[:, None]
    wO = 2 * np.pi * df_Hz / 1000; wc = 2 * np.pi * fc_Hz / 1000
    t = 0.0
    for _ in range(int(t_settle / dt)):
        y = _rk4v(y, t, dt, eta, a, wO, wc); t += dt
    nm = int(t_meas / dt); re = np.empty((nm, n))
    for k in range(nm):
        y = _rk4v(y, t, dt, eta, a, wO, wc); t += dt; re[k] = y[0]
    return re, dt


def _rhs_v(y, t, eta, a, wO, wc):
    """nmm2_ping right-hand side with a per-column amplitude vector."""
    r_e, v_e, r_i, v_i, s_e, z_e, s_i, z_i = y
    F = a * (np.cos((wc - wO / 2) * t) + np.cos((wc + wO / 2) * t))
    return np.array([
        (M.DEL / (M.PI * M.TAU_E) + 2 * r_e * v_e) / M.TAU_E,
        (eta - (M.PI * M.TAU_E * r_e) ** 2 + v_e ** 2 + F) / M.TAU_E + M.C * (M.A_EE * s_e - M.A_EI * s_i),
        (M.DEL / (M.PI * M.TAU_I) + 2 * r_i * v_i) / M.TAU_I,
        (eta - (M.PI * M.TAU_I * r_i) ** 2 + v_i ** 2) / M.TAU_I + M.C * (M.A_IE * s_e - M.A_II * s_i),
        z_e / M.TAU_A, (r_e - 2 * z_e - s_e) / M.TAU_A,
        z_i / M.TAU_G, (r_i - 2 * z_i - s_i) / M.TAU_G])


def _rk4v(y, t, dt, *args):
    k1 = _rhs_v(y, t, *args); k2 = _rhs_v(y + .5 * dt * k1, t + .5 * dt, *args)
    k3 = _rhs_v(y + .5 * dt * k2, t + .5 * dt, *args); k4 = _rhs_v(y + dt * k3, t + dt, *args)
    return y + (dt / 6) * (k1 + 2 * k2 + 2 * k3 + k4)


def spectrum_lines(re, dt, df_Hz):
    """Beat line and the largest off-beat line in 40-60 Hz, as depths (amplitude / mean)."""
    n = re.shape[0]; w = np.hanning(n)[:, None]; mean = re.mean(0)
    X = 2 * np.abs(np.fft.rfft((re - mean) * w, axis=0)) / w.sum(); f = np.fft.rfftfreq(n, dt / 1000)
    jb = np.argmin(np.abs(f - df_Hz)); beat = X[jb] / mean
    band = (f >= 40) & (f <= 60) & (np.abs(f - df_Hz) > 2.0)
    k = np.argmax(X[band], axis=0); other = X[band][k, np.arange(re.shape[1])] / mean; f_other = f[band][k]
    return mean, beat, other, f_other, f, X / mean


if __name__ == "__main__":
    eta, fc, df = 0.85, 300.0, 55.0
    out = dict(eta=eta, fc_Hz=fc, df_Hz=df, C=C, tau_E=TE)
    x0 = fixed_point(eta, eta); g0, f0Hz, _ = leading_mode(x0)
    out['field_free'] = dict(r_E=float(x0[0]), v_E=float(x0[1]), r_I=float(x0[2]),
                             leading_real_per_ms=float(g0), relax_ms=float(-1 / g0), mode_Hz=float(f0Hz))
    print(f"field-free eta={eta}: r_E={x0[0]:.5f}, gamma mode {f0Hz:.2f} Hz, Re(lambda)={g0:+.5f}/ms (relaxation {-1/g0:.0f} ms)")
    # common-drive Hopf for reference
    lo, hi = 0.85, 1.5
    for _ in range(50):
        mid = 0.5 * (lo + hi); xm = fixed_point(mid, mid); gm = leading_mode(xm)[0]
        lo, hi = (mid, hi) if gm < 0 else (lo, mid)
    out['common_drive_hopf_eta'] = float(0.5 * (lo + hi)); print(f"common-drive Hopf: eta_H = {out['common_drive_hopf_eta']:.4f}")
    # E-only critical shift
    lo, hi = 0.0, 3.0
    for _ in range(50):
        mid = 0.5 * (lo + hi); xm = fixed_point(eta + mid, eta); gm = leading_mode(xm)[0]
        lo, hi = (mid, hi) if gm < 0 else (lo, mid)
    dcrit = 0.5 * (lo + hi); xc = fixed_point(eta + dcrit, eta); fcrit = leading_mode(xc)[1]
    wtau = 2 * np.pi * fc / 1000 * TE
    out['E_only_critical_shift'] = dict(delta_eta_E=float(dcrit), mode_Hz_at_crossing=float(fcrit),
                                        a_crit_fast_limit=float(wtau * np.sqrt(dcrit)), omega_tau_E=float(wtau))
    print(f"E-only Hopf: delta_eta_E* = {dcrit:.4f} (mode {fcrit:.2f} Hz) -> a* = omega tau_E sqrt(delta) = {wtau*np.sqrt(dcrit):.2f} per tone")
    # effective point versus amplitude
    amps = [35.0, 30.0, 25.0, 20.0, 15.0, 10.0, 5.0]
    rows = []
    for a in amps:
        x, s = effective_point(eta, a, fc, df)
        gA, fA, _ = leading_mode(x)
        Jn = numeric_jacobian(x, eta, a, fc, df); en = np.linalg.eigvals(Jn); kn = np.argmax(en.real)
        rows.append(dict(a=a, delta_eta_E=float(TE * s[1]), delta_eta_E_fast_limit=float(a * a / wtau ** 2),
                         src_rE=float(s[0]), src_rI=float(s[2]), src_vI=float(s[3]),
                         r_E_eff=float(x[0]), v_E_eff=float(x[1]), r_I_eff=float(x[2]),
                         leading_real_per_ms=float(gA), mode_Hz=float(fA),
                         leading_real_numeric=float(en[kn].real), mode_Hz_numeric=float(abs(en[kn].imag) * 1000 / (2 * np.pi))))
        print(f"a={a:5.1f}: delta_eta_E={TE*s[1]:.4f} (fast limit {a*a/wtau**2:.4f}); r_E_eff={x[0]:.5f}; "
              f"Re(lambda)={gA:+.5f}/ms, mode {fA:.2f} Hz; numeric Jacobian {en[kn].real:+.5f}/ms, {abs(en[kn].imag)*1000/(2*np.pi):.2f} Hz")
    # direct mean-field integration
    re, dt = mf_run(eta, amps, fc, df)
    mean, beat, other, f_other, f, Xn = spectrum_lines(re, dt, df)
    for i, a in enumerate(amps):
        rows[i].update(mf_mean_rE=float(mean[i]), mf_beat_depth=float(beat[i]), mf_other_line_depth=float(other[i]),
                       mf_other_line_Hz=float(f_other[i]), mf_rE_min=float(re[:, i].min()), mf_rE_max=float(re[:, i].max()))
        print(f"  MF a={a:5.1f}: <r_E>={mean[i]:.5f} (eff. point {rows[i]['r_E_eff']:.5f}); beat {df:.0f} Hz depth {beat[i]:.4f}; "
              f"largest other line in 40-60 Hz: {other[i]:.4f} at {f_other[i]:.2f} Hz; r_E range {re[:,i].min():.4f}-{re[:,i].max():.4f}")
    out['amplitudes'] = rows
    json.dump(out, open(os.path.join(HERE, '..', 'docs', 'r7_ping_field_operating_point_2026-10-05.json'), 'w'), indent=1)
    # figure: spectra
    import matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
    fig, ax = plt.subplots(1, 2, figsize=(12, 4.2), constrained_layout=True)
    for i, a in enumerate(amps):
        ax[0].plot(f, Xn[:, i], label=f"a={a:g}")
    ax[0].set_xlim(0, 120); ax[0].set_yscale('log'); ax[0].set_ylim(1e-4, 2)
    ax[0].axvline(df, color='k', ls=':', lw=0.8); ax[0].set_xlabel('frequency (Hz)'); ax[0].set_ylabel('amplitude / mean r_E')
    ax[0].set_title(f'PING mean field, eta={eta}, two tones at {fc:.0f} Hz, beat {df:.0f} Hz'); ax[0].legend(fontsize=8)
    ax[1].plot(amps, [r['leading_real_per_ms'] for r in rows], 'o-', label='Re(leading eigenvalue) at effective point (/ms)')
    ax[1].axhline(0, color='k', lw=0.8); ax[1].set_xlabel('tone amplitude a'); ax[1].set_ylabel('Re lambda (/ms)')
    ax2 = ax[1].twinx(); ax2.plot(amps, [r['mf_other_line_depth'] for r in rows], 's--', color='C3', label='largest off-beat gamma line (depth)')
    ax2.plot(amps, [r['mf_beat_depth'] for r in rows], '^--', color='C2', label='beat line (depth)'); ax2.set_ylabel('line depth')
    ax[1].legend(loc='upper left', fontsize=8); ax2.legend(loc='center left', fontsize=8); ax[1].set_title('stability and spectral lines versus amplitude')
    fig.savefig(os.path.join(HERE, '..', 'docs', 'r7_ping_field_spectra_2026-10-05.png'), dpi=140)
    print('wrote json + png')
