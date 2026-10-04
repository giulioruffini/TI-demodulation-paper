# R6 integration: the carrier comparison uses a specified beat average

Klaus's branch `r6-lanmm-lockin`, commit `f65a047`, was integrated into
`two-tone-validation` as `cb37926`. His calculation establishes that the old 7%/25%
claims have no preserved lock-in provenance. The reconstructed band-power changes
agree with the earlier caches to numerical precision. The manuscript now replaces
those percentages with a defined statistic and displays both measurement windows.
The original handoff remains in `r6_lanmm_carrier_lockin_2026-10-04.md` as a historical
record; the qualifications below supersede its proposed wording.

## The statistic is a carrier profile within each drive condition

Let S(fc) be the arithmetic mean of the quadrature lock-in magnitude of v_P1 over
17 beat frequencies: 7–9 Hz and 12.25–14 Hz, at 0.25 Hz spacing. They lie more than
1.5 Hz from the field-free dominant alpha peak. Carriers run from 25 to 80 Hz in
1 Hz steps. Each tone has amplitude 1.5 mV for P2 drive and 0.5 mV for P1 drive.
The calculation uses the published RK4 integrator, a 0.1 ms step, 2 s settling,
and either 3 or 10 s of measurement. Each profile is normalized by its own maximum
over carriers. This comparison does not match power between targets.

| Drive | Window | Maximum S (mV) | Peak carrier (Hz) | At 25 Hz | 30–80 Hz range (median) | At 60 / 80 Hz |
|---|---:|---:|---:|---:|---:|---:|
| P2 | 3 s | 0.449845 | 39 | 16.590% | 23.347–100.000% (42.488%) | 48.928 / 38.768% |
| P2 | 10 s | 0.450465 | 39 | 16.423% | 22.941–100.000% (41.625%) | 48.710 / 37.888% |
| P1 | 3 s | 0.091631 | 25 | 100.000% | 42.200–67.773% (52.807%) | 53.596 / 53.106% |
| P1 | 10 s | 0.090677 | 25 | 100.000% | 41.650–66.588% (52.413%) | 51.984 / 53.494% |

The machine-readable values and input hashes are in
`r6_lanmm_carrier_lockin_verified.json`; its values take precedence over rounding
in this note. Across carriers, the largest changes in normalized amplitude between
windows are 3.07 percentage points for P2 and 9.61 for P1. The peak carriers and
aggregate ranges persist, but individual values are not window independent.

## Frequency dominance and background limit the interpretation

The saved flag tests whether the largest spectral peak lies within 0.3 Hz of the
beat. It does not measure the unwrapped phase difference and therefore does not
establish capture. All carrier-wise lock-in maxima near alpha pass that dominance
screen; none of the selected off-alpha points does. The P2 lock-in ridge spans
10–10.75 Hz. Neither a large alpha lock-in nor failure of this screen isolates a
forced component from all autonomous activity.

The mean field-free lock-in over the selected beats is 0.004773 mV with the 3 s
window and 0.001195 mV with 10 s. Its maximum is at 8 Hz: 0.01817 and 0.01729 mV.
A field-free trajectory check finds that this component persists in later
subwindows, so calling the entire background leakage is incorrect. Some driven
grid points are at or below their corresponding background. The smallest S exceeds
the mean background by about 16 and 8 for P2 and P1 with 3 s, and 62 and 32 with
10 s. These are aggregate comparisons, not pointwise signal isolation.

The retrospective P1 statistic at a 10 Hz beat gives 0.250343 with 3 s and 0.443328
with 10 s. This demonstrates the window sensitivity of a possible numerical match
to 25%; it does not recover historical provenance. Its 25 Hz reference does not
pass the frequency-dominance screen. No unique calculation of the old 7% was found.

Three different carrier frequencies must remain distinct. The field-free P2 gamma
peak is near 39.7 Hz. The maximum of the full P2-driven alpha-power map is at a
36 Hz carrier and a 10.25 Hz beat; the 10 Hz beat slice peaks at a 44 Hz carrier.
The separately defined off-alpha S profile peaks at 39 Hz. The revised text and
captions identify which measurement supports each number.

## Reproduction and manuscript changes

The independent checker reads the four committed caches without running ODEs:

```sh
.venv/bin/python -B code/summarize_lanmm_carrier_lockin.py --output docs/r6_lanmm_carrier_lockin_verified.json
.venv/bin/python -B code/summarize_lanmm_carrier_lockin.py --format markdown
```

The supplementary field-free check is independently runnable:

```sh
.venv/bin/python -B docs/review_v0150_field_free.py
```

Its output is preserved in `r6_field_free_check_2026-10-04.txt`. The original sweep
commands and transcripts remain with Klaus's commit. No original cache was changed.

Methods defines S, amplitudes, windows, beat selection, and background. Appendix E
replaces the old carrier-rejection percentages with the four-row table and the
window/background limitations. The S1/S7 captions distinguish band power from
lock-in amplitude. Frequency-dominance wording is propagated throughout the
manuscript and affected figure labels. These repairs preserve the finite-amplitude
LaNMM extension without treating it as a quantitative weak-field or kHz test.
