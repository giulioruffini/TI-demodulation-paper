# R12: the producer of `khz_twotone.npz` is recovered

Klaus, October 4, 2026, on branch `r12-khz-twotone` from `5e9d98a` (v0.15.0-draft1).
The task was to recover the producer and settings of `code/khz_twotone.npz`, the cache
behind Figure S6 (two-tone kHz demodulation), or else to supply a fresh, fully
specified calculation. The producer is recovered: a script with the settings below
reproduces both cached spectra with a maximum absolute difference of 0.0 in every bin.
No shared manuscript, figure, cache, or todo file is changed on this branch.

## No producer survives in the record, but the cache fixes the run

The cache entered in commit `a7d6e6f` (July 22, 2026) together with
`make_khz_twotone_fig.py`, which only replots it; no commit before or after adds,
removes, or mentions a script that writes it, and `jr_twotone_figs.py` and
`khz_analysis.py` from the same period do not. The arrays themselves fix most of
the run. The input and output spectra have 133,334 bins, so the record has 266,666
samples; the top frequency, 33,333.3 Hz, gives $dt=1.5\times10^{-5}$ s; the bin width,
0.250001 Hz, gives 4.0 s of data. The stored beat $F_0=10.914393$ Hz is, to the last
digit, the imaginary part of the leading eigenvalue of the Jansen--Rit column at the
`khz_direct.py` operating point ($p=400$ s$^{-1}$, $C=135$, $v^*=8.599$ mV,
$\gamma=1.740$ s$^{-1}$), and $f_{1,2}=2000\mp F_0/2$ Hz exactly. The input peaks,
0.49266 and 0.48831 mV, are a 0.5 mV tone after Hann scalloping at the two bin offsets
(0.985 and 0.977 of the amplitude), so each tone has amplitude 0.5 mV. The remaining
settings are those of the 2 kHz trace in `khz_direct.py` (panel b of Figure S9): the
7-state column with the field low-passed by a first-order state of time constant
$\tau=0.2$ ms before the pyramidal sigmoid, RK4, zero initial state, Hann window,
amplitude normalization $2|X|/\sum w$, plain-mean removal.

Two settings were not those of `khz_direct.py` and were identified from the cache.
The relative phase of the two tones at the start of the window depends on the
settling time, and the Hann sidelobes of each tone reach the other at the $10^{-5}$
level, so the cached input spectrum is a fingerprint of the settling time: a scan
over 0.5--12 s in 0.25 s steps selects 4.0 s (residual $6\times10^{-8}$ against
$\geq2\times10^{-6}$ for every other value), with samples recorded before each
integration step rather than after. With these two settings the output spectrum,
which also carries the residual transient of the 4 s settle (the field-free DC bin
of 0.000776 mV is that transient), matches exactly.

## Comparison against the cache

| Settings | input spectrum, max $|\Delta|$ (mV) | output spectrum, max $|\Delta|$ (mV) | output line (mV) | input 8--14 Hz max (mV) |
|---|---:|---:|---:|---:|
| 5.0 s settle, after-step samples (khz_direct convention) | $9.0\times10^{-6}$ | $2.6\times10^{-4}$ (0.14\% at the line) | 0.076262 | $7.8\times10^{-14}$ |
| **4.0 s settle, before-step samples** | **0.0** | **0.0** | **0.076158** (cache 0.076158) | $2.2430\times10^{-13}$ (cache $2.2430\times10^{-13}$) |

The DC bin of the output (0.000776 mV) and the two input peaks also match to the
last digit. The records are `docs/r12_khz_twotone_compare_2026-10-04.json` (recovered
settings) and `docs/r12_khz_twotone_compare_tset5_after.json` (khz_direct defaults).

## Producer, commands, parameters

`code/khz_twotone_producer.py` imports `rhs7` and the operating point from
`khz_direct.py` and the eigenvalue solver from `timing_not_rate.py`; it adds the
two-tone field and the before-step sampling. Default settings are the recovered ones.

```sh
.venv/bin/python -B code/khz_twotone_producer.py --compare            # 40 s; prints the differences
.venv/bin/python -B code/khz_twotone_producer.py --write code/khz_twotone_fresh.npz   # regenerate under a new name
.venv/bin/python -B code/khz_twotone_producer.py --compare --t-set 5.0 --sample after  # the khz_direct convention
```

| Parameter | Value |
|---|---|
| Model | Jansen--Rit column of `khz_direct.py` (constants from `timing_not_rate.py`), 6 states plus the filtered field $x_f$, $\dot x_f=(E-x_f)/\tau$; pyramidal sigmoid argument $y_1-y_2+x_f$ |
| Operating point | $p=400$ s$^{-1}$, $C=135$; $v^*=8.599$ mV, $\gamma=1.740$ s$^{-1}$, $F_0=10.914393$ Hz |
| Field | $E(t)=\varepsilon[\cos2\pi f_1t+\cos2\pi f_2t]$, $\varepsilon=0.5$ mV per tone, $f_{1,2}=2000\mp F_0/2=1994.5428,\ 2005.4572$ Hz |
| Access | $\tau=0.2$ ms |
| Integration | RK4, $dt=1.5\times10^{-5}$ s, zero initial state, 4.0 s settling (266,666 steps), 4.0 s measurement (266,666 samples), samples before each step |
| Spectra | plain mean removed, Hann window, amplitude $2|X|/\sum w$, `rfft`; bins 0.250001 Hz |

## Consequences for the text, left for the integrating pass

- `run_all.py` and the README can drop the "replot only, producer absent" status for
  `fig_khz_twotone` once the producer is integrated as the data step before
  `make_khz_twotone_fig.py`; with `--write` to a scratch name it does not touch the cache.
- Results §4.3 says the input "carries $2.2\times10^{-13}$ of its spectral amplitude in
  the 8--14 Hz band". The number is the Hann amplitude in mV; relative to the 0.49 mV
  tone peaks it is $4.6\times10^{-13}$. Either quote mV or the ratio.
- The 2 kHz two-tone run settled 4 s at $p=400$ ($\gamma=1.74$ s$^{-1}$), leaving a
  transient of order $10^{-3}$ relative in the window; the Methods sentence "settled for
  10--16 s" describes the 100 Hz runs, not this one. A clause in Methods would close it.
- The output line sits in the 11.00 Hz bin of a 0.25 Hz grid for a 10.91 Hz beat; the
  caption's "10.9 Hz" is right, and "11.0 Hz" elsewhere is the bin.

## Uncertainty

None remains about the reproduction: every stored array is reproduced bit for bit from
the stated settings. The sampling convention (before the step) and the 4.0 s settle
were inferred from the data rather than read from a script; a scratch script with
exactly these choices is the only way the cache can have been made, but that script
itself is not recovered.
