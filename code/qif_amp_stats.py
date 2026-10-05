"""
Dependent statistics of a QIF raster cache (published layout), for comparing tone
amplitudes (review brief, October 5, 2026). For each condition pair off/on: mean rate and
its change, beat depth (lock-in / mean) in the spiking network and in the mean field,
largest line in 40-60 Hz more than 2 Hz from the beat (spiking and mean field, Hann
amplitude spectrum over the measurement window, normalized by the mean), pooled vector
strength, pooled and per-neuron pairwise phase consistency, and the ratio of beat depth to
fractional mean-rate change.

    python qif_amp_stats.py qif_raster_twotone.npz qif_raster_twotone_a10.npz [--json out.json]
"""
import os, sys, json, argparse
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))


def lines(r, dt_ms, df):
    n = len(r); w = np.hanning(n); m = r.mean()
    X = 2 * np.abs(np.fft.rfft((r - m) * w)) / w.sum() / m; f = np.fft.rfftfreq(n, dt_ms / 1000)
    jb = np.argmin(np.abs(f - df)); band = (f >= 40) & (f <= 60) & (np.abs(f - df) > 2.0)
    k = np.argmax(X[band]); return float(X[jb]), float(X[band][k]), float(f[band][k])


def stats(path):
    d = np.load(path, allow_pickle=True); meta = d['meta'].item(); conds = d['conds'].item(); dt = float(meta['dt'])
    out = dict(file=os.path.basename(path), Af=float(meta['Af']), floor_ms=float(meta.get('floor_ms', 800.0)), conditions={})
    for reg in ('forced', 'entrain'):
        if f'{reg}_on' not in conds: continue
        qo, qn = conds[f'{reg}_off']['q'], conds[f'{reg}_on']['q']; df = float(qn['df']); km = int(qn['kmeas'])
        ro, rn = qo['re_t'][km:], qn['re_t'][km:]
        mo, mn = conds[f'{reg}_off']['mf_re'][km:], conds[f'{reg}_on']['mf_re'][km:]
        bo, oo, fo = lines(ro, dt, df); bn, on, fn = lines(rn, dt, df)
        mbo, moo, mfo = lines(mo, dt, df); mbn, mon, mfn = lines(mn, dt, df)
        rate_change = float(rn.mean() / ro.mean() - 1)
        out['conditions'][reg] = dict(
            eta=float(qn['etabar']), beat_Hz=df, window_ms=float(qn['t_meas']), cycles=int(round(qn['t_meas'] * df / 1000)),
            rate_off=float(ro.mean()), rate_on=float(rn.mean()), rate_change_pct=100 * rate_change,
            beat_depth_spiking=float(qn['AC'] / qn['rmean']), beat_depth_spiking_fft=bn, beat_depth_meanfield=mbn,
            other_line_spiking_off=oo, other_line_spiking_on=on, other_line_Hz_on=fn,
            other_line_meanfield_off=moo, other_line_meanfield_on=mon, other_line_meanfield_Hz_on=mfn,
            mf_rate_off=float(mo.mean()), mf_rate_on=float(mn.mean()), mf_rate_change_pct=100 * float(mn.mean() / mo.mean() - 1),
            VS_pooled_off=float(qo['VS']), VS_pooled_on=float(qn['VS']), PPC_pooled_off=float(qo['PPC']), PPC_pooled_on=float(qn['PPC']),
            PPC_neuron_median_off=float(qo['PPC_n_median']), PPC_neuron_median_on=float(qn['PPC_n_median']),
            depth_over_rate_change=float(qn['AC'] / qn['rmean'] / rate_change) if rate_change else float('nan'))
    return out


if __name__ == '__main__':
    ap = argparse.ArgumentParser(); ap.add_argument('files', nargs='+'); ap.add_argument('--json', default='')
    a = ap.parse_args(); res = [stats(os.path.join(HERE, f) if not os.path.isabs(f) else f) for f in a.files]
    for r in res:
        print(f"== {r['file']} (Af={r['Af']:g}, window floor {r['floor_ms']:.0f} ms)")
        for reg, c in r['conditions'].items():
            print(f"  {reg:8s} eta={c['eta']:.2f} beat={c['beat_Hz']:.0f} Hz ({c['cycles']} cycles): rate {c['rate_off']:.4f}->{c['rate_on']:.4f} ({c['rate_change_pct']:+.1f}%; MF {c['mf_rate_change_pct']:+.1f}%) | "
                  f"beat depth spiking {c['beat_depth_spiking']:.3f} (MF {c['beat_depth_meanfield']:.3f}) | other 40-60 Hz line spiking off/on {c['other_line_spiking_off']:.3f}/{c['other_line_spiking_on']:.3f} at {c['other_line_Hz_on']:.1f} Hz (MF {c['other_line_meanfield_off']:.3f}/{c['other_line_meanfield_on']:.3f}) | "
                  f"VS pooled {c['VS_pooled_off']:.3f}/{c['VS_pooled_on']:.3f} | PPC pooled {c['PPC_pooled_on']:.4f} | PPC/neuron median {c['PPC_neuron_median_off']:.4f}/{c['PPC_neuron_median_on']:.4f} | depth/rate-change {c['depth_over_rate_change']:.1f}")
    if a.json:
        json.dump(res, open(a.json, 'w'), indent=1); print('wrote', a.json)
