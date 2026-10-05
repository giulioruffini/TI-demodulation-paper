# Landau findings 1, 5, 6, 18, 19, 21, 29: recomputations and proposed wording

Klaus, October 5, 2026, branch `landau-draft10` from draft10 (`0c394df`). New computations only;
the manuscript source is untouched here and Kaiti integrates. Python: the project `.venv`.

## Finding 1 (and 19): the NMM2 coupling sweep and 1/γ

`code/nmm2_jcurve_modes.py` tracks the eigenvalue that crosses at the gamma Hopf
$J^*=16.660$ by continuation backward from $J^*$, computes the exact linear-response gain from
the second-order beat source $\mathrm{Re}\,D^2f[q,\bar q]$ to $r_E$ on a 0.025 Hz grid, and
re-measures the simulated peak on an adaptive grid centred on the linear peak with 5 s
settling and a 4 s window, and runs the amplitude check (`--sim`; one producer for every field
the figure and this note use). Table, settings, and normalizations:
`docs/landau1_nmm2_jcurve_modes_2026-10-05.json`; raw lock-in grids including the amplitude check:
`code/nmm2_jcurve_modes.npz`. Gain grid: 3001 points over 15 to 90 Hz (0.025 Hz).

- The PING column has two weakly damped modes. The critical mode carries the response peak at
  the lowest couplings, $J\le14.30$ (36 to 41 Hz, $\gamma_{\rm crit}\ge0.040$ ms$^{-1}$), and again
  for $J\ge16.25$ ($\gamma_{\rm crit}\le0.0081$ ms$^{-1}$, 49 to 50.6 Hz). In between,
  $14.62\le J\le16.19$, a second, more damped mode at 53 to 57 Hz carries it. The published abscissa followed the 25 to 90 Hz band filter,
  which for the first 11 points picked the non-critical pair (Landau is right).
- Where the critical mode carries the response, the exact linear gain grows as $1/\gamma_{\rm crit}$:
  fitted exponent $1.016$ over a 5.8-fold range of $\gamma$ ($0.0081$ to $0.0014$ ms$^{-1}$).
  Over the full sweep the exponent is $0.70$, because the other mode carries the middle.
- Simulated peak over linear gain, per $A^2$ (normalized at $J=15.53$):

| $J$ | $\gamma_{\rm crit}$ (ms$^{-1}$) | $A=2$ | $A=4$ | $A=8$ (published) |
|---|---|---|---|---|
| 15.527 | 0.0218 | 1.000 | 1.013 | 1.065 |
| 16.190 | 0.0094 | 0.998 | 1.004 | 1.025 |
| 16.254 | 0.0081 | 1.013 | 1.071 | 1.328 |
| 16.434 | 0.0045 | 1.034 | 1.151 | 1.480 |
| 16.566 | 0.0019 | 1.081 | 1.221 | 0.932 |
| 16.590 | 0.0014 | 1.104 | 1.153 | 0.728 |

  At a quarter of the amplitude ($A=2$, one sixteenth of the power) the simulation follows linear
  response to within about 10% at the nine checked couplings. At the published
  amplitude the critical-mode response first exceeds linear response by up to 48%, as the
  rectified mean shift moves the operating point toward the Hopf, then saturates.
- The cached peaks are accurate to 2% except at $J=16.25$ to $16.43$, where the 1.5 Hz grid missed
  the narrowing resonance by up to 20%. The figure now uses the re-measured peaks.
- `code/make_nmm2_jfig.py` redraws Fig. nmm2_jcurve: (a) simulated peak and scaled linear
  response against $J$; (b) against $1/\gamma_{\rm crit}$, filled symbols where the critical mode
  carries the peak, open where the 55 Hz mode does, with the $1/\gamma$ reference anchored in the
  critical range.

## Finding 5 (and 6, 29): two tones instead of the AM surrogate

Matched beat source: two tones of amplitude $\varepsilon$ at $f_c\mp\Delta f/2$ give the surrogate's
$\Omega$ source and a DC source $\varepsilon^2$ instead of $\tfrac34\varepsilon^2$.

**Timing versus rate** (`code/timing_not_rate_twotone.py`, cache `timing_not_rate_twotone.npz`,
same couplings and settings as Fig. timing). Two tones: modulation $25.6\to338.6$ mHz ($13.2\times$),
mean shift $-1.77\to-7.72$ mHz ($4.4\times$), far-from-Hopf DC exactly $4/3$ of the surrogate's.
Modulation/mean: $14.5\times$ far from the Hopf, maximum $58\times$ at $\gamma\approx1.0$ s$^{-1}$,
$44\times$ nearest the Hopf (surrogate: $19$, $66$, $45$). The figure can stay surrogate-based
if the text states both; or swap the cache for the two-tone one (same format).

**TI/tACS** (`code/ti_tacs_twotone.py`, `docs/landau5_ti_tacs_twotone_2026-10-05.json`). Ratios at
the cached tACS couplings change by about 2% at most: $0.142\to0.142$ far, $0.238\to0.235$ at
$\gamma=1.07$, $0.469\to0.459$ at $\gamma=0.12$ s$^{-1}$. Source-matched controls (60 s settling,
20 s window): $0.987$, $0.929$, $0.900$ (surrogate $0.99$, $0.94$, $0.92$); the $6.99\times$ input
gives $6.97$, $3.95$, $1.96$, unchanged.

**NMM2 endpoint** (`code/nmm2_endpoint_twotone.py`, `docs/landau5_s10_endpoint_twotone_{25,27}.json`;
5 s settling, 8 s Lyapunov run). Last two couplings: Lyapunov $-0.00096$ and $-0.00079$ ms$^{-1}$,
perturbation decay $-0.0016$ and $-0.0014$ ms$^{-1}$ (surrogate $-0.0013$; Kaiti's Floquet
$-0.00169$). Attracting. Beat lock-in $0.0109$ and $0.0115$, about 11% above the surrogate,
from the larger DC push toward the Hopf. (The 1.2 s-window Lyapunov is positive, $+0.002$; it is a
transient average, which the 8 s value supersedes.)

## Findings 18, 21: the abstract sentence

The modulation/mean ratio rises $4\times$ toward the Hopf and then falls by a quarter closest to
it, with either waveform. "Rate modulation grows faster than the mean-rate change near resonance"
is true for most of the approach but not at the end.

## Proposed wording (for Kaiti to integrate)

Abstract, replace the sentence: "Approaching resonance, rate modulation outgrows the mean-rate
change until rectification of the amplified oscillation takes over the mean."

Waveform-scope paragraph (after "...and the kHz demonstration."): "The AM surrogate is retained
for the dense coupling and drive sweeps (Figs. jcurve, timing, tacs, nmm2_jcurve). Their
mean-shift-dependent results were repeated with genuine two tones: the timing-versus-rate ratios
are reported for both waveforms, the TI/tACS ratios change by about 2% at most, and the NMM2 endpoint
remains attracting." Drop "every claim that turns on the waveform is run with genuine two tones"
or restrict it to the listed demonstrations.

Timing paragraph: "With genuine two tones, the beat-locked modulation of $r_P$ at $\Delta f=f_0$
grows $13\times$ ($26$ to $339$~mHz), tracking $1/\gamma$ before saturating near criticality;
the shift of its mean grows $4.4\times$ ($-1.8$ to $-7.7$~mHz), through rectification of the
growing oscillation, but stays below $0.2\%$ of the $3.9$~Hz baseline. Modulation exceeds the
mean shift by $15\times$ far from the Hopf; the ratio peaks at $58\times$ near
$\gamma=1$~s$^{-1}$ and falls to $44\times$ closest to the Hopf, where rectification of the
amplified oscillation feeds the mean. The $m=1$ surrogate, whose DC source is $3/4$ of the
two-tone value, gives $19$, $66$, and $45\times$." Same numbers in the Fig. timing caption.

TI/tACS paragraph: append "(genuine two tones: $0.14$, $0.24$, $0.46$)" after the three cached
ratios and "(two tones: $0.99$, $0.93$, $0.90$)" after the matched controls.

NMM2 paragraph, replace "the demodulated peak of $r_E$ grows as $1/\gamma$ before departing from
this scaling near criticality": "two weakly damped modes compete. Over an intermediate coupling range ($14.6\le J\le16.2$) a
second mode near $55$~Hz carries the peak response; for $\gamma\lesssim0.008$~ms$^{-1}$ the critical mode near
$50$~Hz does, and there the linear-response gain grows as $1/\gamma$ (fitted exponent $1.02$ over
a $5.8$-fold range). At the plotted drive the simulated peak first exceeds linear response by up
to $48\%$, as the rectified mean shift moves the state toward the Hopf, then saturates; at a
quarter of that drive amplitude it stays within about $10\%$ of linear response." Endpoint sentence: add
"with genuine two tones the endpoint perturbation decays at $-0.0014$~ms$^{-1}$." Replace "share
the leading gain scaling" by "share the $1/\gamma$ gain scaling of their critical mode".

Fig. nmm2_jcurve caption (a,b): "(a) Simulated peak (blue) and exact linear response (gray, scaled
far from $J^*$) of $r_E$ as $J\to J^*$. (b) The same against $1/\gamma$ of the critical mode:
filled where the critical mode carries the peak, open where a second mode near $55$~Hz does ($14.6\le J\le16.2$). The
linear response follows $1/\gamma$ (dashed) where the critical mode dominates; the simulated peak
first exceeds and then falls below it at this drive amplitude."

## Provenance repair (19:55)

At Kaiti's request: `nmm2_jcurve_modes.py --sim` now produces every field the plotter and this
note use (`Gpk_src`, `fGpk_src`, `crit`, `simpk`, `sim_over_lin_src`, `amp_check`), with raw
lock-in grids in the npz; the rerun reproduces the earlier inline values to the printed digits.
Interval statement corrected (the critical mode also carries the lowest couplings), the grid
spacing stated as committed, and "quarter drive power" corrected to quarter amplitude.
