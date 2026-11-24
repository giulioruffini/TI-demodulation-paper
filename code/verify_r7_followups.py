"""Recompute amplitude-10 cache statistics and equal-RMS mean-field controls.

Rate lock-ins and pooled phase consistency are read from the stored time series,
not from the cached summaries. The carrier controls use the original nmm2_ping
integrator; a single carrier is represented by two coincident half-amplitude tones.
Writes a compact trace cache for the supplementary comparison and a JSON audit.
"""
import argparse
import hashlib
import json
from pathlib import Path

import numpy as np
import nmm2_ping as M
import ping_fast_carrier_check as P
import ping_field_operating_point as K

HERE = Path(__file__).resolve().parent


def cache_check(path):
    cache = np.load(path, allow_pickle=True)
    meta, conditions = cache['meta'].item(), cache['conds'].item()
    result = dict(file=path.name, sha256=hashlib.sha256(path.read_bytes()).hexdigest(),
                  N=int(meta['Ne']), dt_ms=float(meta['dt']), conditions={})
    for regime in ('forced', 'entrain'):
        if regime+'_on' not in conditions:
            continue
        pair = {}
        for state in ('off', 'on'):
            q = conditions[regime+'_'+state]['q']
            start = q['kmeas']; rate = q['re_t'][start:]; times = q['ts'][start:]
            phase = np.exp(2j*np.pi*q['df']*times/1000)
            weight = np.hanning(len(rate)); mean = rate.mean()
            depth = 2*abs(np.sum(weight*(rate-mean)*phase))/weight.sum()/mean
            vs = abs(np.sum(rate*phase))/rate.sum()
            count = rate.sum()*meta['Ne']*meta['dt']
            pooled_ppc = (count*vs*vs-1)/(count-1)
            ok = q['n_spk'] >= q['nmin']
            ppc = (q['n_spk'][ok]*q['VS_n'][ok]**2-1)/(q['n_spk'][ok]-1)
            assert abs(depth-q['AC']/q['rmean']) < 1e-10
            assert abs(vs-q['VS']) < 1e-10
            assert abs(pooled_ppc-q['PPC']) < 1e-10
            assert abs(np.median(ppc)-q['PPC_n_median']) < 1e-10
            pair[state] = dict(rate=float(mean), beat_depth=float(depth),
                               pooled_VS=float(vs), pooled_PPC=float(pooled_ppc),
                               median_cell_PPC=float(np.median(ppc)))
        pair['rate_change_pct'] = 100*(pair['on']['rate']/pair['off']['rate']-1)
        pair['depth_to_rate_change'] = pair['on']['beat_depth']/(pair['rate_change_pct']/100)
        result['conditions'][regime] = pair
    return result


def controls():
    M.WAVE = 'twotone'
    dt, settle, measure, eta = .05, 800., 800., .85
    wc = 2*np.pi*300/1000
    original = json.loads((HERE.parent/'docs/r7_carrier_control_2026-10-05.json').read_text())
    traces, rows = {}, []
    for amplitude in (10., 35.):
        for waveform in ('TI', 'carrier'):
            a = amplitude if waveform == 'TI' else amplitude/np.sqrt(2)
            beat = 55. if waveform == 'TI' else 0.
            omega = 2*np.pi*beat/1000
            y = P.ping_equilibrium(15., eta)
            rate = []
            t = 0.
            for k in range(round((settle+measure)/dt)):
                y = M._rk4(y, t, dt, eta, a, omega, wc); t += dt
                if k >= round(settle/dt):
                    rate.append(y[0])
            rate = np.array(rate)
            mean, line, other, freq, _, _ = K.spectrum_lines(rate[:, None], dt, 55)
            reference = original['rows'][len(rows)]
            for key, value in [('mean_rE', mean[0]), ('beat55_depth', line[0]),
                                ('other_line_depth', other[0])]:
                assert abs(value-reference[key]) < 1e-7, (waveform, amplitude, key)
            rows.append(dict(a=amplitude, waveform=waveform, mean_rate=float(mean[0]),
                             beat_depth=float(line[0]), other_depth=float(other[0]),
                             other_Hz=float(freq[0])))
            traces[f'{waveform}_{int(amplitude)}'] = rate
    return rows, dict(dt_ms=dt, settle_ms=settle, measurement_ms=measure,
                      carrier_Hz=300., beat_Hz=55., **traces)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--json', required=True, type=Path)
    parser.add_argument('--traces', required=True, type=Path)
    parser.add_argument('--controls-only', action='store_true',
                        help='regenerate the four control traces without the convergence-cache audit')
    args = parser.parse_args()
    files = ['qif_raster_twotone.npz', 'qif_raster_twotone_a10.npz',
             'qif_raster_twotone_a10_long.npz', 'qif_raster_twotone_a10_n16k.npz',
             'qif_raster_twotone_a10_dt2.npz']
    checks = [] if args.controls_only else [cache_check(HERE/name) for name in files]
    rows, traces = controls()
    np.savez_compressed(args.traces, **traces)
    args.json.write_text(json.dumps(dict(cache_checks=checks, carrier_controls=rows), indent=2)+'\n')
    print(f'{len(checks)} QIF caches verified; four carrier-control trajectories reproduced.')
