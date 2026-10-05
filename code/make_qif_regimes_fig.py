"""Complementary QIF amplitude comparison and equal-RMS mean-field controls.

Reads preserved amplitude-10/35 spiking caches and the control traces generated
by verify_r7_followups.py. All panels use eta=0.85, carrier 300 Hz, beat 55 Hz.
The unmodulated control is a mean-field result, not a spiking-network result.
"""
import os
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

import figstyle
import overlap
import make_qif_figs as R


def main():
    here = Path(__file__).resolve().parent
    out = Path(os.environ.get('TN_FIGDIR', here.parent/'figures'))
    out.mkdir(parents=True, exist_ok=True)
    figstyle.apply()
    fig, axes = plt.subplots(2, 2, figsize=(10, 7))
    for col, (amplitude, filename) in enumerate(((10, 'qif_raster_twotone_a10.npz'),
                                                (35, 'qif_raster_twotone.npz'))):
        data = np.load(here/filename, allow_pickle=True)
        R.meta, R.conds = data['meta'].item(), data['conds'].item()
        R.DISPLAY_START, R.DISPLAY_END = 600., 800.
        ax = axes[0, col]
        rate_axis = R.raster_panel(ax, 'forced_on', 'ab'[col], True,
                                   annot=rf'$A_f={amplitude}$')
        rate_axis.set_ylim(0, .25)
        rate_axis.set_yticks([0, .1, .2], labels=['0', '100', '200'])
        rate_axis.set_ylabel('E rate (Hz)', color=figstyle.NEBLUE)
        rate_axis.tick_params(axis='y', colors=figstyle.NEBLUE)
        R.beat_inset(ax, 'forced_off', 'forced_on')
        ax.set_xlim(600, 800)
        ax.set_xticks([600, 640, 680, 720, 760, 800])
        ax.set_yticks([0, 100, 200, 300, 400])
        ax.set_xlabel('time in measurement window (ms)')
        ax.set_ylabel('E neuron #')
    cache = np.load(here/'ping_carrier_control_traces.npz')
    for col, amplitude in enumerate((10, 35)):
        ax = axes[1, col]
        for key, color, label in [('TI', figstyle.NEBLUE, 'two-tone TI'),
                                  ('carrier', figstyle.NERED, 'equal-RMS carrier')]:
            rate = cache[f'{key}_{amplitude}']
            win = np.hanning(len(rate))
            frequency = np.fft.rfftfreq(len(rate), float(cache['dt_ms'])/1000)
            depth = 2*np.abs(np.fft.rfft((rate-rate.mean())*win))/win.sum()/rate.mean()
            ax.plot(frequency, depth, color=color, label=label)
        ax.axvline(55, color='0.5', lw=.8, ls='--')
        ax.set(xlim=(40, 65), ylim=(0, .8), xlabel='frequency (Hz)',
               ylabel='line amplitude / mean rate')
        ax.set_xticks([40, 45, 50, 55, 60, 65])
        ax.set_yticks([0, .2, .4, .6, .8])
        ax.legend(loc='upper right', fontsize=9)
        figstyle.panel(ax, 'cd'[col])
    fig.tight_layout(w_pad=2.5, h_pad=3)
    figstyle.scale_text(fig, placed_frac=1)
    overlap.check(fig, placed_frac=1, name='qif_regimes')
    for extension in ('pdf', 'png'):
        fig.savefig(out/f'fig_qif_regimes.{extension}', dpi=450, bbox_inches='tight')
    plt.close(fig)
    print('wrote complementary QIF-regime comparison')


if __name__ == '__main__':
    main()
