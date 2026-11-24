# R7 follow-ups: amplitude-10 spiking runs, the equal-RMS carrier control, and the S10 endpoint

Klaus, October 5, 2026, branch `r7-followups` from `669128b` (v0.15.0-draft3), answering
`docs/klaus_next_checks_2026-10-05.md`. Published caches, figures, manuscript, builds, and
todo are untouched; new caches carry their own names. Scripts: `code/qif_raster_amp.py`
(the published QIF script's functions at a chosen amplitude), `code/qif_amp_stats.py`,
`code/ping_carrier_control.py`, `code/nmm2_jcD_endpoint_check.py`; `code/make_qif_figs.py`
gains `QIF_SRC`/`QIF_TAG` environment overrides so it can render an alternative cache.

## 1. The spiking network at 10 per tone

Same model, N = 8000 per population, dt = 0.0025 ms, 800 ms settling, integer-cycle windows
(44 cycles at 55 Hz, 34 at 42 Hz), field-off controls, mean field at the same step.
Caches `code/qif_raster_twotone_a10.npz` (both conditions), `_a10_long.npz` (drive 0.85,
88 cycles), `_a10_n16k.npz` (drive 0.85, N = 16000). Figures in `docs/r7_amp10_figs/`
(same layout and rasterized treatment as draft3). Statistics in
`docs/r7_qif_amp10_stats_2026-10-05.json`; the 35-per-tone row is the published cache
re-measured with the same script.

| drive, beat | a | rate change (spiking / MF) | beat depth (spiking / MF) | largest other 40--60 Hz line, off / on (spiking; MF on) | VS pooled on | PPC pooled on | PPC per neuron, median off / on | depth / rate change |
|---|---:|---|---|---|---:|---:|---|---:|
| 0.85, 55 Hz | 35 | +10.5% / +12.3% | 0.290 / 0.314 | 0.005 / 0.685 at 52.5 Hz; MF 0.601 | 0.115 | 0.0132 | $-0.018$ / $+0.003$ | 2.8 |
| 0.85, 55 Hz | **10** | +2.8% / +2.9% | **0.093 / 0.128** | 0.005 / 0.016 at 51.2 Hz; MF 0.000 | 0.046 | 0.0021 | $-0.018$ / $-0.016$ | 3.4 |
| 1.5, 42 Hz | 35 | +7.6% / +9.4% | 0.232 / 0.239 | 0.860 / 0.921 at 53.1 Hz; MF 1.002 | 0.129 | 0.0166 | $-0.023$ / $+0.005$ | 3.0 |
| 1.5, 42 Hz | **10** | +1.6% / +1.8% | **0.023 / 0.024** | 0.860 / 0.898 at 54.4 Hz; MF 0.991 | 0.015 | 0.0002 | $-0.023$ / $-0.023$ | 1.5 |

At drive 0.85 and 10 per tone the field-on response is a forced response: the rate ripples
at the beat with the envelope and there are no gamma bursts (panel b of the new raster);
the mean rate rises 2.8% against 10.5% at 35; the beat-locked depth exceeds the fractional
rate change by 3.4. The per-neuron PPC median is unchanged from the field-off value, so no per-neuron
locking is resolved at this amplitude; a negative median does not prove locking absent, only
that it is below the resolution of this statistic. The beat-locked activity is resolved at
the population level: pooled vector strength 0.046.

The residual off-beat line at 51--52 Hz (0.016 with the field on, 0.005 off) behaves like
finite-size noise driven through the resonance rather than an oscillation: it falls to 0.012
(on) and 0.002 (off) with the 88-cycle window, as the $1/\sqrt{T}$ scaling of an incoherent
peak predicts, and the mean field has none. Two windows are consistent with that scaling;
they do not prove it.

At drive 1.5 and 10 per tone the beat-locked component is 0.023, invisible in the raster and
in the fold (panel d shows the unperturbed gamma with the envelope drawn over it). Between
10 and 35 that component scales approximately as the square of the amplitude
(0.023 × 12.25 = 0.28 against 0.232; two points, not a square-law validation), whereas at
drive 0.85 it does not (0.093 × 12.25 = 1.14 against 0.290): the forced response at 35 is
saturated and the state has crossed the threshold. In the mean field the
beat depth is square-law between 5 and 10 per tone (0.030 → 0.128, ratio 4.3) and saturates
above 15, so 10 sits at the top of the square-law range.

Finite-size and discretization. The spiking beat depth at 10 is 27% below the mean field
(0.093 against 0.128), more than at 35 (8%). Doubling the population to 16000 gives 0.083
(rate +2.8%, PPC median $-0.016$; cache `_a10_n16k.npz`), and halving the time step to
0.00125 ms gives 0.093 again (cache `_a10_dt2.npz`), so the gap is neither finite-size
noise nor the Euler step. It is a difference between the finite network as implemented
(V_peak = 100, deterministic Lorentzian quantiles, spike-count rate) and the exact mean
field at weak drive. The V_peak check below locates it.

**Spike cutoff (added 13:30 at Kaiti's request).** Same condition and settings with the
spike/reset threshold raised from the published V_peak = 100 (caches `_a10_vp200.npz`,
`_a10_vp400.npz`; `docs/r7_qif_amp10_vpeak_2026-10-05.json`):

| V_peak | field-free rate (MF 0.0506) | rate change | beat depth (MF 0.128) | other line on | PPC per neuron, median off / on |
|---:|---:|---:|---:|---:|---|
| 100 | 0.0527 | +2.8% | 0.093 | 0.016 | $-0.018$ / $-0.016$ |
| 200 | 0.0515 | +2.8% | 0.127 | 0.006 | $-0.020$ / $-0.015$ |
| 400 | 0.0509 | +2.9% | 0.139 | 0.004 | $-0.021$ / $-0.015$ |

The field-free rate converges to the mean-field value as the cutoff rises, and at
V_peak = 200 the beat depth agrees with the mean field within 1%. The gap at the published
cutoff is therefore the finite spike threshold, which shortens each spike's trajectory and
biases the weak-drive response low by about 27%.

**Step refinement (added 14:00 at Kaiti's request).** The same three cutoffs at
dt = 0.00125 ms (caches `_vp200_dt2.npz`, `_vp400_dt2.npz`, and `_dt2.npz` from before;
`docs/r7_qif_amp10_vpeak_dt_2026-10-05.json`):

| V_peak | dt (ms) | field-free rate | rate change | beat depth (MF 0.128) |
|---:|---:|---:|---:|---:|
| 100 | 0.0025 / 0.00125 | 0.0527 / 0.0527 | +2.8% / +2.8% | 0.093 / 0.093 |
| 200 | 0.0025 / 0.00125 | 0.0515 / 0.0515 | +2.8% / +2.8% | 0.127 / 0.121 |
| 400 | 0.0025 / 0.00125 | 0.0509 / 0.0509 | +2.9% / +2.9% | 0.139 / 0.141 |

Halving the step changes the depth by at most 5% at any cutoff and leaves the rates
unchanged to four digits, so the Euler step is not the issue and my earlier attribution of
the 400 overshoot to the step was wrong. The weak-drive beat depth of the finite network
depends on the cutoff at the ±10% level and is not converged in it at N = 8000: 0.093 at
100, 0.121--0.127 at 200, 0.139--0.141 at 400, with the mean field's 0.128 between the last
two. Agreement at 200 is a cutoff check, not a joint convergence. For weak-drive
comparisons quote the spiking depth as 0.12--0.14 against the mean field's 0.13, or quote
the published-cutoff value with its 27% low bias; the published runs at 35 per tone and
V_peak = 100 had an 8% gap.

## 2. The equal-RMS unmodulated carrier (mean field)

Drive 0.85; two tones at 300 ∓ 27.5 Hz of amplitude a against one 300 Hz tone of amplitude
√2 a (same RMS); dt 0.05 ms, 800 ms settling, 800 ms window. Averaged-point shift and
stability from the exact second-order source (`ping_field_operating_point.py`).
`docs/r7_carrier_control_2026-10-05.json`.

| drive | δη_E (averaged) | averaged growth (/ms) | mean rate shift | 55 Hz depth | largest other 40--60 Hz line |
|---|---:|---:|---:|---:|---|
| two tones, a = 10 | 0.133 | $-0.0090$ | +2.9% | 0.128 | none |
| one carrier, 14.14 | 0.129 | $-0.0088$ | +2.8% | 0.000 | none |
| two tones, a = 35 | 1.653 | $+0.0321$ | +11.8% | 0.300 | 0.605 at 51.25 Hz |
| one carrier, 49.50 | 1.606 | $+0.0315$ | +12.0% | 0.011 | 0.709 at 51.25 Hz |

The prediction holds in the mean field: the unmodulated carrier of equal RMS produces the
same rectified shift (within 3%), the same mean-rate rise, and at 35 the same induced gamma
(0.71 against 0.61), with no beat line; at 10 neither waveform induces gamma and only TI
carries the 55 Hz line. The spiking network was not run for the single carrier.

**Leakage check (added 13:26 at Kaiti's request).** The single carrier's 55 Hz entry of
0.011 in the 800 ms window is Hann leakage of the 51.25 Hz gamma line, three bins away: with
a 3200 ms window (0.31 Hz bins, 11 bins away) it falls to 0.00009, while the two-tone 55 Hz
line holds at 0.300 → 0.314 (`docs/r7_carrier_control_longwindow_2026-10-05.json`). The
induced gamma resolves at 51.6--51.9 Hz with the longer window.

## 3. The S10 endpoint is an attracting driven state

S10 settings reproduced exactly (AM surrogate, A = 8, carrier 300 Hz, beat 50.5 Hz at the
last seven couplings, dt 0.05 ms, 600 ms settling, 1200 ms window): the lock-in at the beat
matches the cached peak at every tested coupling to five digits.
`docs/r7_s10_endpoint_check_2026-10-05.json`, `docs/r7_s10_endpoint_longsettle_2026-10-05.json`.

| C | γ_free (/ms) | DC-only screen (Kaiti) | Lyapunov, 1.2 s / 4.8 s (/ms) | perturbation decay (/ms) | lock-in (cache) | 2nd harmonic / other line |
|---:|---:|---:|---|---:|---|---|
| 13.000 | 0.0487 | $-0.0132$ | $-0.0120$ / $-0.0129$ | $-0.0134$ | 0.00093 (0.00093) | 0.001 / 0.000 |
| 16.492 | 0.00334 | $-0.00075$ | $+0.0010$ / $-0.0019$ | $-0.0023$ | 0.00761 (0.00761) | 0.010 / 0.0035 |
| 16.534 | 0.00249 | $+0.00008$ | $+0.0015$ / $-0.0013$ | $-0.0018$ | 0.00887 (0.00887) | 0.014 / 0.0041 |
| 16.590 | 0.00138 | $+0.00114$ | $+0.0022$ / $-0.0007$ | $-0.0013$ | 0.01041 (0.01041) | 0.020 / 0.0048 |

Diagnostic: a tangent vector integrated with the exact Jacobian along the forced trajectory
(the field enters additively, so the field-free Jacobian is exact), and a second trajectory
started with a $10^{-4}$ relative perturbation after settling. The perturbation decays at
every tested coupling, at a rate close to the field-free damping (−0.0013 /ms at the
endpoint against γ_free = 0.0014); the 4.8 s Lyapunov exponent is negative throughout. The
1.2 s exponent is positive at the last seven couplings only because a random tangent vector
grows transiently along the non-normal directions before aligning with the slow mode; it is
a finite-time artifact, not an instability. With 3 s settling the perturbation decay is
−0.0017 to −0.0019 /ms at the last three couplings and the lock-in changes by +0.5 to +0.8%,
so the published 600 ms settling, shorter than the 725 ms relaxation time at the endpoint,
biases the cached peak by under 1%. The spectrum has the beat, its second harmonic (the
surrogate's own 2Ω content plus the nonlinearity, 12% at the endpoint), and no line away
from the beat beyond the Hann skirt (the "other line" at 52.5 Hz is 2 Hz from a 50.5 Hz
beat in a 1.2 s window).

Kaiti's independent full-period Floquet calculation (8×8 variational matrix over the
2000 ms common forcing period after 8000 ms settling) gives a largest multiplier modulus
0.0342, exponent −0.00169 /ms, in agreement with the perturbation decay above.

Conclusion: the DC-only averaged screen overstates the loss of stability; the fully forced
endpoint is amplification about a stable driven state, with the beat-frequency response
itself contributing to the slow balance that the DC-only average omits. Recommended wording
for the S10 caption and the J-curve text: "At the last couplings the rectified mean shift
(0.064 in E drive) reduces the stability margin; a perturbation of the fully forced solution
still decays at a rate close to the field-free damping (−0.0013 /ms at the endpoint), so
the curve measures amplification about a stable driven state. Settling of 600 ms biases
the endpoint lock-in by less than 1%." Preserve the measured curve.

## Proposed figure use

The amplitude-10 forced pair (drive 0.85, off/on) is the weak-field forced demonstration the
present Figure 10(a,b) was meant to be, with a 9% (spiking) to 13% (mean field) beat-locked
ripple and a 2.8% rate change. The amplitude-10 oscillatory pair shows nothing visible and
would not carry a panel. The amplitude-35 runs remain the threshold-crossing example at the
same drive 0.85, now with the equal-RMS carrier control to show that the induced gamma is the
carrier's and the beat patterning is TI's. One arrangement: Figure 10 as drive 0.85 at
10 per tone (a,b) and at 35 per tone (c,d), with the single-carrier control in S12 or a new
supplementary figure, and the drive-1.5 pair at 35 kept in the supplement. That is Kaiti's
and Giulio's call; all runs and renders are on this branch.
