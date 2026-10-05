# v0.15.0-draft5: spike-cutoff sensitivity and carrier leakage

The baseline is draft4 (`8d8cb7b`). Klaus's follow-up `b1a1c4c` is integrated as
`8f03544`. The abstracts, all 23 figures, their order, every equation and citation,
and the original simulation caches remain. Methods, QIF Results, the S13 caption,
and the storyline gain the cutoff and longer-window evidence.

## The spiking depth depends on the finite cutoff

For background drive 0.85, amplitude 10 per tone, N=8000, dt=0.0025 ms, and the
same 800 ms settling/measurement windows:

| Spike cutoff | Field-free rate (/ms) | Beat depth | Relative difference from MF | Mean-rate rise |
|---:|---:|---:|---:|---:|
| 100 | 0.0526641 | 0.0926385 | -27.5% | 2.7649% |
| 200 | 0.0514794 | 0.1269358 | -0.63% | 2.8334% |
| 400 | 0.0509092 | 0.1393291 | +9.08% | 2.8939% |
| Mean field | 0.0506255 | 0.1277363 | — | 2.9006% |

Changing only the cutoff removes most of the original discrepancy at 200 and
reverses its sign at 400. This establishes sensitivity to the finite spike/reset
implementation. It does not establish a converged limiting amplitude. The
Euler increment near cutoff 400 is large in absolute voltage units, but its
responsibility for the overshoot has not been isolated. Klaus has been sent a
bounded half-step check at cutoffs 200 and 400; no higher-cutoff result is silently
substituted for the existing figures.

Figure S13 retains the same cutoff 100 at both amplitudes. Its caption and Results
report the sensitivity. Median per-cell phase consistency remains negative at
all tested cutoffs; this does not exclude locking in a subset of cells.

## The apparent carrier beat shrinks with the spectral window

With 800 ms settling and otherwise unchanged settings, increasing the Hann-window
measurement from 800 to 3200 ms gives:

| Input | 55 Hz depth, 800 ms | 55 Hz depth, 3200 ms |
|---|---:|---:|
| TI, 35 per tone | 0.2997220 | 0.3138372 |
| Single carrier, peak sqrt(2) × 35 | 0.0109826 | 0.00009204 |

The carrier entry decreases by a factor of about 119 while TI's line persists.
This supports spectral leakage from the nearby gamma line as the source of the
short-window carrier estimate. The text states the measured residual rather than
an exactly zero response. Single-carrier controls remain mean-field calculations;
no corresponding spiking network is claimed.

## Independent verification and review copies

`code/verify_r7_cutoff_leakage.py` recomputes the three cutoff-cache summaries
with the established independent reader. It then reintegrates both carrier
conditions for 3200 post-settling milliseconds using the original PING RK4
implementation. The four 800/3200 ms spectral estimates match Klaus's JSON
within 1e-7; cutoff rate and depth summaries agree within 1e-10. The file
`docs/r7_cutoff_leakage_independent_2026-10-05.json` stores the results and cache
hashes. This is not a fresh spiking-network rerun.

The prose checker is clean. The revision is local; author declarations,
submission-version approval, and the optional placement decisions remain open.
GitHub push, Calliope/Zenodo release, Overleaf sync, and coauthor email remain held.

The builds contain 50 TN pages, 32 article pages, 20 supplementary pages,
50 redline pages, and eight storyline pages. All compile without errors,
undefined references/citations, or overfull boxes. The changed Results, S13
caption, redline, and storyline pages were rendered and inspected. The abstracts,
32 labeled equations, 23 figures, and citation sequence are retained. Output
hashes are recorded in `validation_2026-10-05_v0150draft5.json`.
