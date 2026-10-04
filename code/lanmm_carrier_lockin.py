"""
Phase-sensitive carrier dependence of the LaNMM response (review item R6).

The manuscript (App. E and the caption of the P1-drive map) attributes the carrier
comparison "~7% of peak off the gamma resonance under superficial P2 drive, ~25% of
peak under direct P1 drive" to a lock-in read-out of v_P1 at the beat frequency. The
committed caches (lanmm_field_<target>_twotone.npz) hold band-power changes only, and
lanmm_field_tongues.py defines `lockin` without calling it. This script re-runs the
carrier--beat sweep with the same integrator, grid, waveform, amplitudes, settling,
and window as the cached maps, and reads it with the quadrature lock-in at Delta f
(in-phase, quadrature, amplitude) for v_P1 and v_P2, alongside the band-power change,
which is checked against the cache.

Observable      v_P1(t) (deep pyramidal membrane potential), also v_P2
Estimator       Hann-windowed quadrature lock-in at Omega = 2 pi Delta f over the
                measurement window (lanmm_field_tongues.lockin); amplitude = hypot(I, Q)
Field           two tones eps[cos((wc - Om/2) t) + cos((wc + Om/2) t)], mV, added inside
                the sigmoid argument of the target population
Grid            f_c = 25..80 Hz (56), Delta f = 5..15 Hz (41)
Amplitude       eps = 1.5 mV (P2 drive), 0.5 mV (P1 drive), as in the cached maps
Integration     RK4, dt = 1e-4 s, 2.0 s settling, 3.0 s measurement
Baseline        eps = 0 (field-free): the autonomous alpha of the column leaks into the
                lock-in at nearby Delta f through the finite window; stored per Delta f

Outputs         lanmm_carrier_lockin_<target>_twotone.npz, and a printed summary.
"""
import os, sys, json, time
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import lanmm_field_tongues as L


def lockin_iq(v, t, df):
    w = np.hanning(v.shape[0])[:, None]
    om = 2 * np.pi * np.atleast_1d(df)[None, :]
    tt = t[:, None]
    vb = v - (w * v).sum(0) / w.sum()
    I = 2 * (w * vb * np.cos(om * tt)).sum(0) / w.sum()
    Q = 2 * (w * vb * np.sin(om * tt)).sum(0) / w.sum()
    return I, Q


def run(target, eps_c, wave='twotone', dt=1e-4, t_settle=2.0, t_meas=3.0,
        fc=np.linspace(25, 80, 56), df=np.linspace(5, 15, 41)):
    F, D = np.meshgrid(fc, df, indexing='ij')
    t0 = time.perf_counter()
    ts, v1, v2 = L.integrate(eps_c, F, D, wave=wave, target=target,
                             dt=dt, t_settle=t_settle, t_meas=t_meas)
    I1, Q1 = lockin_iq(v1, ts, D.ravel()); I2, Q2 = lockin_iq(v2, ts, D.ravel())
    P1 = L.band_power(v1, dt); P2 = L.band_power(v2, dt)
    F1c = L.dominant_freq(v1, dt); F2c = L.dominant_freq(v2, dt)
    # field-free baseline: identical dynamics at every grid point, so one trajectory
    tb, b1, b2 = L.integrate(0.0, np.array([fc[0]]), np.array([df[0]]), wave=wave,
                             target=target, dt=dt, t_settle=t_settle, t_meas=t_meas)
    I10, Q10 = lockin_iq(np.repeat(b1, df.size, axis=1), tb, df)
    I20, Q20 = lockin_iq(np.repeat(b2, df.size, axis=1), tb, df)
    Pb1 = float(L.band_power(b1, dt)[0]); Pb2 = float(L.band_power(b2, dt)[0])
    f0 = float(L.dominant_freq(b1, dt)[0])
    out = dict(fc=fc, df=df, eps_c=eps_c, wave=wave, target=target, dt=dt,
               t_settle=t_settle, t_meas=t_meas,
               L1=np.hypot(I1, Q1).reshape(F.shape), I1=I1.reshape(F.shape), Q1=Q1.reshape(F.shape),
               L2=np.hypot(I2, Q2).reshape(F.shape), I2=I2.reshape(F.shape), Q2=Q2.reshape(F.shape),
               Pc1=(P1 - Pb1).reshape(F.shape), Pc2=(P2 - Pb2).reshape(F.shape),
               F1c=F1c.reshape(F.shape), F2c=F2c.reshape(F.shape),
               L1_base=np.hypot(I10, Q10), L2_base=np.hypot(I20, Q20),
               P1_base=Pb1, P2_base=Pb2, f_alpha_base=f0,
               wall_s=time.perf_counter() - t0)
    return out


def summarize(o):
    fc, df, L1, L1b = o['fc'], o['df'], o['L1'], o['L1_base']
    j10 = int(np.argmin(np.abs(df - 10.0)))
    ridge = L1.max(axis=1); jmax = L1.argmax(axis=1)
    peak = ridge.max(); kpk = int(ridge.argmax())
    # beats within one window resolution (1/t_meas) of the autonomous alpha are leakage-prone
    near = np.abs(df - o['f_alpha_base']) <= 1.0 / o['t_meas']
    L1_far = np.where(near[None, :], -np.inf, L1)
    ridge_far = L1_far.max(axis=1)
    # frequency-dominance (capture screen) of v_P1 at the beat, as in the tongue maps
    cap = np.abs(o['F1c'] - df[None, :]) < 0.3
    L1_free = np.where(cap | near[None, :], -np.inf, L1)   # neither captured nor leakage-prone
    ridge_free = L1_free.max(axis=1)
    s = dict(target=o['target'], eps_c=float(o['eps_c']), f_alpha_base=o['f_alpha_base'],
             peak_L1_mV=float(peak), peak_fc=float(fc[kpk]), peak_df=float(df[jmax[kpk]]),
             ridge_over_peak_min=float(ridge.min() / peak), ridge_min_fc=float(fc[ridge.argmin()]),
             ridge_over_peak_median=float(np.median(ridge) / peak),
             at10_over_peak_min=float(L1[:, j10].min() / L1[:, j10].max()),
             at10_over_peak_median=float(np.median(L1[:, j10]) / L1[:, j10].max()),
             ridge_df_per_fc=[float(x) for x in df[jmax]],
             leakage_floor_max_mV=float(L1b.max()), leakage_floor_at10_mV=float(L1b[j10]),
             ridge_far_over_peakfar_min=float(ridge_far.min() / ridge_far.max()),
             ridge_far_over_peakfar_median=float(np.median(ridge_far) / ridge_far.max()),
             n_fc_ridge_below_2x_leakage=int(np.sum(ridge < 2 * L1b.max())),
             captured_fraction=float(cap.mean()), captured_at_ridge_fraction=float(cap[np.arange(len(fc)), jmax].mean()),
             ridge_free_over_peakfree_min=float(ridge_free.min() / ridge_free.max()),
             ridge_free_over_peakfree_median=float(np.median(ridge_free) / ridge_free.max()),
             peak_free_fc=float(fc[int(ridge_free.argmax())]), peak_free_df=float(df[int(L1_free[int(ridge_free.argmax())].argmax())]),
             peak_free_mV=float(ridge_free.max()),
             wall_s=float(o['wall_s']))
    far = np.abs(fc - fc[kpk]) > 10.0
    s['far_from_peak_carrier_median'] = float(np.median(ridge[far]) / peak)
    s['far_from_peak_carrier_min'] = float(ridge[far].min() / peak)
    return s


if __name__ == '__main__':
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument('--targets', default='P2,P1')
    ap.add_argument('--quick', action='store_true')
    ap.add_argument('--tmeas', type=float, default=3.0)
    ap.add_argument('--tag', default='')
    a = ap.parse_args()
    kw = dict(t_meas=a.tmeas)
    if a.quick:
        kw = dict(fc=np.linspace(25, 80, 12), df=np.linspace(5, 15, 11), t_settle=1.0, t_meas=1.5)
    summaries = {}
    for tgt in a.targets.split(','):
        eps_c = 1.5 if tgt == 'P2' else 0.5
        print(f'[{tgt}] eps={eps_c} mV two tones ...', flush=True)
        o = run(tgt, eps_c, **kw)
        tag = ('_quick' if a.quick else '') + a.tag
        np.savez(os.path.join(HERE, f'lanmm_carrier_lockin_{tgt}_twotone{tag}.npz'), **o)
        # cache cross-check of the band-power change (same integrator and window)
        cache = os.path.join(HERE, f'lanmm_field_{tgt}_twotone.npz')
        if os.path.exists(cache) and not a.quick:
            c = np.load(cache)
            rel = np.max(np.abs(o['Pc1'] - c['Pc1'])) / np.max(np.abs(c['Pc1']))
            print(f'  band-power change vs cache: max |diff| / max|cache| = {rel:.2e}')
        s = summarize(o); summaries[tgt] = s
        print(json.dumps(s, indent=1))
    with open(os.path.join(HERE, f'lanmm_carrier_lockin_summary{("_quick" if a.quick else "") + a.tag}.json'), 'w') as f:
        json.dump(summaries, f, indent=1)
