"""
Equal-RMS unmodulated-carrier control for the PING mean field (review brief, October 5, 2026).

At background drive 0.85, compare two-tone TI at a per tone (300 -/+ 27.5 Hz) with a
single 300 Hz carrier of peak amplitude sqrt(2) a (same RMS, hence the same rectified
DC source in the fast-carrier limit: a^2/(omega tau_E)^2 for both). Same integrator,
dt = 0.05 ms, 800 ms settling, 800 ms window (44 beat cycles) as ping_field_operating_point.py.
Reports, for each run, the mean rate shift, the largest line in 40-60 Hz away from 55 Hz
(induced gamma), the 55 Hz line (beat), and the averaged-point stability.
Output: ../docs/r7_carrier_control_2026-10-05.json
"""
import os, sys, json
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import ping_field_operating_point as K


def rhs_general(y, t, eta, tones):
    """PING right-hand side with an arbitrary list of (amplitude, omega) tones on E, vectorized."""
    r_e, v_e, r_i, v_i, s_e, z_e, s_i, z_i = y
    F = sum(a * np.cos(w * t) for a, w in tones)
    M = K.M
    return np.array([
        (M.DEL / (M.PI * M.TAU_E) + 2 * r_e * v_e) / M.TAU_E,
        (eta - (M.PI * M.TAU_E * r_e) ** 2 + v_e ** 2 + F) / M.TAU_E + M.C * (M.A_EE * s_e - M.A_EI * s_i),
        (M.DEL / (M.PI * M.TAU_I) + 2 * r_i * v_i) / M.TAU_I,
        (eta - (M.PI * M.TAU_I * r_i) ** 2 + v_i ** 2) / M.TAU_I + M.C * (M.A_IE * s_e - M.A_II * s_i),
        z_e / M.TAU_A, (r_e - 2 * z_e - s_e) / M.TAU_A,
        z_i / M.TAU_G, (r_i - 2 * z_i - s_i) / M.TAU_G])


def run(eta, tones, dt=0.05, t_settle=800.0, t_meas=800.0):
    y = K.P.ping_equilibrium(15.0, eta).astype(float); t = 0.0
    def rk4(y, t):
        k1 = rhs_general(y, t, eta, tones); k2 = rhs_general(y + .5 * dt * k1, t + .5 * dt, eta, tones)
        k3 = rhs_general(y + .5 * dt * k2, t + .5 * dt, eta, tones); k4 = rhs_general(y + dt * k3, t + dt, eta, tones)
        return y + (dt / 6) * (k1 + 2 * k2 + 2 * k3 + k4)
    for _ in range(int(t_settle / dt)):
        y = rk4(y, t); t += dt
    nm = int(t_meas / dt); re = np.empty(nm)
    for k in range(nm):
        y = rk4(y, t); t += dt; re[k] = y[0]
    return re, dt


def dc_source_tones(x, tones):
    A = K.P.ping_jacobian(x, K.C); b = np.zeros(8); b[1] = 1 / K.TE; s = np.zeros(8)
    for a, w in tones:
        q = np.linalg.solve(1j * w * np.eye(8) - A, b)
        s += (a * a / 4) * np.real(K.P.ping_hessian(q, np.conj(q)))
    return s


def effective(eta, tones):
    x = K.fixed_point(eta, eta)
    for ak in np.linspace(0.0, 1.0, 13)[1:]:
        for _ in range(4):
            s = dc_source_tones(x, [(a * ak, w) for a, w in tones])
            x = K.fixed_point(eta, eta, src=s, x0=x)
    g, f, _ = K.leading_mode(x)
    return x, K.TE * s[1], g, f


if __name__ == '__main__':
    eta, fc, df = 0.85, 300.0, 55.0
    w = lambda f: 2 * np.pi * f / 1000
    x0 = K.fixed_point(eta, eta)
    rows = []
    for a in (10.0, 35.0):
        cases = {f'two tones a={a:g}': [(a, w(fc - df / 2)), (a, w(fc + df / 2))],
                 f'one carrier sqrt2*a={np.sqrt(2)*a:.2f}': [(np.sqrt(2) * a, w(fc))]}
        for label, tones in cases.items():
            xe, dEta, g, f = effective(eta, tones)
            re, dt = run(eta, tones)
            mean, beat, other, f_other, _, _ = K.spectrum_lines(re[:, None], dt, df)
            rows.append(dict(case=label, a=a, rms=float(np.sqrt(sum(t[0] ** 2 / 2 for t in tones))),
                             delta_eta_E=float(dEta), averaged_point_growth_per_ms=float(g), averaged_mode_Hz=float(f),
                             mean_rE=float(mean[0]), mean_rE_free=float(x0[0]), mean_shift_pct=float(100 * (mean[0] / x0[0] - 1)),
                             beat55_depth=float(beat[0]), other_line_depth=float(other[0]), other_line_Hz=float(f_other[0]),
                             rE_min=float(re.min()), rE_max=float(re.max())))
            r = rows[-1]
            print(f"{label:28s} rms={r['rms']:.2f} dEta_E={dEta:.4f} growth={g:+.5f}/ms ({f:.1f} Hz) | mean shift {r['mean_shift_pct']:+.2f}% | "
                  f"55 Hz depth {beat[0]:.4f} | largest other 40-60 Hz line {other[0]:.4f} at {f_other[0]:.2f} Hz | r_E {re.min():.4f}-{re.max():.4f}")
    json.dump(dict(eta=eta, fc_Hz=fc, df_Hz=df, rows=rows), open(os.path.join(HERE, '..', 'docs', 'r7_carrier_control_2026-10-05.json'), 'w'), indent=1)
    print('wrote json')
