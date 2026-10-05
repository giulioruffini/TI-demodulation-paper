"""Independently check the QIF cutoff caches and carrier-window comparison.

The cutoff summaries are recomputed from preserved data. The mean-field carrier
controls are reintegrated with the original PING RK4 implementation, then read
through a Hann lock-in over the first 800 and all 3200 post-settling milliseconds.
"""
import argparse
import json
from pathlib import Path

import numpy as np
import nmm2_ping as M
import ping_fast_carrier_check as P
from verify_r7_followups import cache_check

HERE = Path(__file__).resolve().parent


def cutoff_timestep_check():
    """Compare both time steps at each cutoff without rerunning old controls."""
    reference = json.loads((HERE.parent/'docs/r7_qif_amp10_vpeak_dt_2026-10-05.json').read_text())
    rows, changes = [], []
    for cutoff, suffix in ((100, ''), (200, '_vp200'), (400, '_vp400')):
        pair = []
        for step in ('', '_dt2'):
            path = HERE/f'qif_raster_twotone_a10{suffix}{step}.npz'
            row = cache_check(path)
            metadata = np.load(path, allow_pickle=True)['meta'].item()
            row['V_peak'] = cutoff
            assert metadata['VPEAK'] == cutoff
            expected = reference[len(rows)]
            assert row['dt_ms'] == expected['dt_ms']
            result = row['conditions']['forced']
            for value, key in ((result['off']['rate'], 'rate_off'),
                               (result['on']['rate'], 'rate_on'),
                               (result['on']['beat_depth'], 'beat_depth'),
                               (result['rate_change_pct'], 'rate_change_pct')):
                assert abs(value-expected[key]) < 1e-10
            pair.append(result['on']['beat_depth'])
            rows.append(row)
        changes.append(dict(V_peak=cutoff, depth_change_pct=100*(pair[1]/pair[0]-1)))
    return dict(cutoff_timestep_checks=rows, step_changes=changes)


def check():
    cutoffs = []
    reference = json.loads((HERE.parent/'docs/r7_qif_amp10_vpeak_2026-10-05.json').read_text())
    for cutoff, suffix, expected in zip((100, 200, 400), ('', '_vp200', '_vp400'), reference):
        path = HERE/f'qif_raster_twotone_a10{suffix}.npz'
        row = cache_check(path)
        metadata = np.load(path, allow_pickle=True)['meta'].item()
        assert metadata['VPEAK'] == cutoff
        row['V_peak'] = cutoff
        pair = row['conditions']['forced']
        target = expected['conditions']['forced']
        assert abs(pair['on']['beat_depth']-target['beat_depth_spiking']) < 1e-10
        assert abs(pair['rate_change_pct']-target['rate_change_pct']) < 1e-10
        row['relative_depth_difference_from_MF'] = (
            pair['on']['beat_depth']/target['beat_depth_meanfield']-1)
        cutoffs.append(row)

    reference = json.loads((HERE.parent/'docs/r7_carrier_control_longwindow_2026-10-05.json').read_text())
    M.WAVE = 'twotone'
    dt, settle, measure, eta = .05, 800., 3200., .85
    wc = 2*np.pi*300/1000
    rows = []
    for waveform in ('TI', 'carrier'):
        amplitude = 35. if waveform == 'TI' else 35./np.sqrt(2)
        omega = 2*np.pi*55/1000 if waveform == 'TI' else 0.
        y = P.ping_equilibrium(15., eta)
        rate = []
        time = 0.
        for k in range(round((settle+measure)/dt)):
            y = M._rk4(y, time, dt, eta, amplitude, omega, wc)
            time += dt
            if k >= round(settle/dt):
                rate.append(y[0])
        rate = np.asarray(rate)
        for window in (800., 3200.):
            data = rate[:round(window/dt)]
            weight = np.hanning(len(data))
            frequencies = np.fft.rfftfreq(len(data), dt/1000)
            spectrum = 2*np.abs(np.fft.rfft(weight*(data-data.mean())))/weight.sum()/data.mean()
            beat = spectrum[np.argmin(abs(frequencies-55))]
            region = (frequencies >= 40) & (frequencies <= 60) & (abs(frequencies-55) > 1.5)
            gamma_index = np.flatnonzero(region)[np.argmax(spectrum[region])]
            row = dict(waveform=waveform, measurement_ms=window, depth_55=float(beat),
                       gamma_Hz=float(frequencies[gamma_index]),
                       gamma_depth=float(spectrum[gamma_index]))
            expected = reference[len(rows)]
            for key in ('depth_55', 'gamma_Hz', 'gamma_depth'):
                assert abs(row[key]-expected[key]) < 1e-7, (waveform, window, key)
            rows.append(row)
    return dict(cutoff_checks=cutoffs, carrier_windows=rows,
                carrier_settings=dict(dt_ms=dt, settling_ms=settle, eta=eta,
                                      carrier_Hz=300., beat_Hz=55., TI_tone_amplitude=35.))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--json', required=True, type=Path)
    parser.add_argument('--timesteps-only', action='store_true',
                        help='verify both time steps at all three cutoffs from their caches')
    args = parser.parse_args()
    result = cutoff_timestep_check() if args.timesteps_only else check()
    args.json.write_text(json.dumps(result, indent=2)+'\n')
    print('Six cutoff/time-step summaries verified.' if args.timesteps_only else
          'Three cutoff summaries and four carrier-window spectra verified.')
