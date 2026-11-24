# Referee deliverables, Klaus, 2026-10-24

Handoff from Kaiti (21:04), on K's approval of the reconciled plan (69c106b):
(1) an analytic kHz feasibility figure and (2) a theta-neuron pilot of the QIF
network. Everything lives in this folder; nothing in the manuscript, `code/`,
or the canonical artifacts was changed, and no build or reset was run.

## 1. Analytic kHz feasibility figure

Files: `feasibility_khz.py` (self-contained, numpy + matplotlib),
`feasibility_khz.pdf` and `.png` (300 dpi, 12 × 3.7 in, three panels),
`feasibility_khz_curves.csv` (every curve: $\tau$, $\lambda_0$, $E$, $f_c$,
access factor, $\varepsilon_{1,2}$, $Y_\Omega$, $Y_{\rm DC}$,
$\varepsilon_{\rm eq}$), `feasibility_khz_anchors.json` (the numbers quoted
below). Runtime 1.4 s.

### Formulas and units

Tones $f_{1,2} = f_c \mp \Delta f/2$ with $\Delta f = 10$ Hz; the access factor
is insensitive to $\Delta f$ at these carriers (two-tone and $|H(\omega_c)|^2$
agree to $10^{-4}$). Access $H(\omega) = 1/(1 + i\omega\tau)$, polarization
$\varepsilon_j = \lambda_0 E\,|H(\omega_j)|$ in mV with $E$ the local field per
tone in V/m (the same for both tones) and $\lambda_0$ in mV per V/m. Two-tone
access factor $|H(\omega_1)||H(\omega_2)|$. JR sigmoid with $\rho = 0.56$ /mV,
$v_0 = 6$ mV, $e_0 = 2.5$ /s at the pinned $v^* = 8.30$ mV:
$\Sigma' = 0.4745$ /s/mV, $\Sigma'' = -0.1508$ /s/mV$^2$ (Eq. direct-comparison
values reproduced). Beat source $Y_\Omega = \tfrac12\Sigma''\varepsilon_1
\varepsilon_2$ (1/s), steady source $Y_{\rm DC} = \tfrac14\Sigma''
(\varepsilon_1^2 + \varepsilon_2^2)$ (1/s), equivalent direct polarization
$\varepsilon_{\rm eq} = [\Sigma''/(2\Sigma')]\,\varepsilon_1\varepsilon_2 =
-0.1589\,\varepsilon_1\varepsilon_2$ mV per mV$^2$, the tDCS or tACS
polarization at the same entry point that gives the same leading source
(Sec. 2.6). Optional sealed long cable: each tone acquires
$(1+\omega^2\tau^2)^{-1/4}$, so the two-tone factor is
$(1+\omega_c^2\tau^2)^{-1/2}$ (S1).

### Panels

- (a) Two-tone access factor against $f_c$ (0.3–10 kHz) for $\tau$ = 0.05,
  0.2, 1, 15 ms, with the sealed-cable curve at 0.2 ms dotted; vertical marks at
  1.3 kHz (Missey, Emory), 2 kHz (manuscript example), 9 kHz (Missey, Czech and
  Hungarian centers).
- (b) $|\varepsilon_{\rm eq}|$ in µV against $f_c$ for the same $\tau$ at
  $E$ = 0.3 V/m per tone; left axis $\lambda_0$ = 0.5, right axis the same curves
  at $\lambda_0$ = 0.15 (factor 0.09). Scaling $\varepsilon_{\rm eq} \propto
  \lambda_0^2 E^2$ covers the rest of the requested grid (0.1–1 V/m: factors
  1/9 and 11).
- (c) $|\varepsilon_{\rm eq}|$ against $E$ per tone (0.1–1 V/m) at
  $\tau$ = 0.2 ms for 1.3, 2, and 9 kHz, $\lambda_0$ = 0.5 (orange) and 0.15
  (blue); star at the Sec. 5.4 budget ($E$ = 0.5 V/m, 2 kHz, 0.2 ms,
  $\lambda_0$ = 0.5: $\varepsilon_{1,2}$ = 0.0926/0.0922 mV,
  $\varepsilon_{\rm eq}$ = 1.36 µV, $Y_\Omega = Y_{\rm DC} = -6.4\times10^{-4}$ /s).

### Anchors (two-tone factor and ratios; field factor = $\sqrt{P_{1.3}/P_9}$)

| $\tau$ (ms) | $P$(1.3 kHz) | $P$(2 kHz) | $P$(9 kHz) | $P_9/P_{1.3}$ | field factor 9 vs 1.3 kHz | cable $P_9/P_{1.3}$ |
|---|---|---|---|---|---|---|
| 0.05 | 0.86 | 0.72 | 0.11 | 0.13 | 2.8 | 0.36 |
| 0.2 | 0.27 | 0.14 | 0.0078 | 0.028 | 5.9 | 0.17 |
| 1 | 0.015 | 0.0063 | 3.1e-4 | 0.021 | 6.9 | 0.15 |
| 15 | 6.7e-5 | 2.8e-5 | 1.4e-6 | 0.021 | 6.9 | 0.14 |

$|\varepsilon_{\rm eq}|$ (µV) at $E$ = 0.3 V/m, $\lambda_0$ = 0.5, for
$\tau$ = 0.05 / 0.2 / 1 / 15 ms: 1.3 kHz 3.1 / 0.97 / 0.053 / 2e-4; 2 kHz
2.6 / 0.49 / 0.022 / 1e-4; 9 kHz 0.40 / 0.028 / 0.0011 / 7e-7. At
$\lambda_0$ = 0.15 divide by 11. For scale, a direct 0.5 V/m field at
$\lambda_0$ = 0.5 polarizes by 250 µV; the budget's 1.36 µV is 0.5% of it,
the 2–5% of Sec. 2.6 being the equal-per-carrier matching at 0.1–0.3 mV.

### Draft caption (for Kaiti to cut)

**Carrier access sets the generated TI source at fixed applied field.**
(a) Two-tone access factor $|H(\omega_1)||H(\omega_2)|$ of a first-order
membrane with time $\tau$ against carrier frequency; dotted, sealed-cable end
at 0.2 ms. Marks: 1.3 and 9 kHz (the two carrier arms of Missey et al. 2026)
and 2 kHz. Above both corners the factor falls as $f_c^{-2}$, so 9 kHz delivers
$(1.3/9)^2 \approx 0.02$ of the 1.3 kHz source for any $\tau \gtrsim 0.2$ ms,
and 0.13 at 0.05 ms. (b) Equivalent direct polarization
$|\varepsilon_{\rm eq}| = |\Sigma''|\varepsilon_1\varepsilon_2/(2\Sigma')$ of
the JR detector at the pinned operating point for 0.3 V/m per tone; left axis
$\lambda_0$ = 0.5 mV per V/m, right axis 0.15. (c) The same against local
field per tone at 0.2 ms for the marked carriers; star, the Sec. 5.4 budget.
Illustrative assumptions: point-membrane access, uniform assumed $\lambda_0$,
static JR detection at $v^*$ = 8.30 mV, open-loop sources before synaptic and
recurrent gain, equal fields for both tones. The factor applies to the static
chain only; the exact mean field and the QIF network compute access within
$\tau_E$.

### Limitations

No cable geometry beyond the sealed-end bound; no channel kinetics; no
network gain (a $1/\gamma$ resonance multiplies both TI and matched direct
sources equally); $\lambda_0$ at kHz is not the DC value; the Esmaeilpour 2021
slice thresholds (5, 60, 80 V/m at 0.1, 1, 2 kHz) are outside the weak-input
range and are not plotted.

## 2. Theta-neuron pilot

Protocol: `theta_pilot_protocol.md`, committed before any run (768d431).
Script: `theta_pilot.py`; outputs `theta_pilot_<run>.json` and `.npz`, log
`theta_pilot.log`. Results follow.

### Runs performed (5 of the 8 budgeted; 12.3 min network + 1.1 min mean field)

$\bar\eta = 0.85$, 300 Hz carrier, 55 Hz beat, two tones $A_f = 10$ on E,
Euler, 800 ms burn-in, integer-cycle windows, same quantiles, seed, synapses,
and readouts as `code/qif_raster.py`; mean field (MF) integrated by the
published RK4 routine at the same step and window.

| run | $N$/pop | $\Delta t$ (ms) | window | $\langle r_E\rangle$ (1/ms) | depth | Δ vs `on` | VS pooled | PPC pooled | PPC/neuron median | MF depth | min |
|---|---|---|---|---|---|---|---|---|---|---|---|
| off | 8000 | 0.0025 | 44 cyc | 0.0504 | 0.0057 | | 0.002 | 0.0000 | −0.021 | 0.0008 | 1.7 |
| on | 8000 | 0.0025 | 44 cyc | 0.0518 | 0.1558 | | 0.077 | 0.0059 | −0.014 | 0.1277 | 1.7 |
| dt2 | 8000 | 0.00125 | 44 cyc | 0.0518 | 0.1551 | −0.4% | 0.077 | 0.0060 | −0.014 | 0.1277 | 3.2 |
| long | 8000 | 0.0025 | 88 cyc | 0.0518 | 0.1511 | −3.0% | 0.075 | 0.0057 | −0.005 | 0.1278 | 2.5 |
| n2 | 16000 | 0.0025 | 44 cyc | 0.0518 | 0.1373 | −11.9% | 0.068 | 0.0046 | −0.015 | 0.1277 | 3.3 |

Depth = lock-in at 55 Hz / mean E rate, field on. Mean rate rises 2.8% from
`off` to `on` (published QIF: 2.8%). Largest Euler advance of any neuron per
step: 1.2–1.6 rad at $N$ = 8000 (the extreme excitability quantile), 3.2 rad at
$N$ = 16000; the half-step check shows this does not move the depth.

### Pre-registered verdict

The step and window checks pass (−0.4%, −3.0%). The population check fails
the 5% criterion (−11.9%). By the stop rule the pilot stops here: the three
equal-power controls (`sc10`, `tt35`, `sc35`) are deferred, and no parameter
was adjusted at any point. Mean-field agreement was not a target.

### What the pilot established

1. The cutoff dependence of the published QIF runs is a $1/V_{\rm peak}$
   effect, and the theta network is its limit. A least-squares fit of the
   published series (depth 0.093, 0.127, 0.139 at $V_{\rm peak}$ = 100, 200,
   400, S4) to $d_\infty - c/V_{\rm peak}$ gives $d_\infty$ = 0.156
   ($c$ = 6.2, residuals ≤ 0.002), against the theta value 0.156 at the same
   $N$, step, and window. The mechanism is the reset lag $\approx 2\tau_E/
   V_{\rm peak}$ = 0.3, 0.15, 0.075 ms per spike, which the theta form removes.
2. With the cutoff removed, one population doubling moves the depth toward
   the exact mean field: 0.156 at 8000, 0.137 at 16000, mean field 0.128.
   One doubling does not establish that the remaining gap is purely finite
   size: the largest sampled Euler advance in phase also rose from 1.5 to
   3.2 rad, so the population and time-step limits are not separated and
   joint convergence is untested (Kaiti's correction, 21:30). What can be
   said is that at $N$ = 8000 the cutoff-free depth lies 22% above the mean
   field while the published cutoff run lies 27% below it, so the
   $V_{\rm peak}$ = 200 agreement with the mean field was a cancellation.
3. The qualitative statements hold at every setting: beat depth 0.137–0.156
   in all driven runs; the mean-rate rise of 2.8% (ratio 5–6; published 3.4
   at $V_{\rm peak}$ = 100) is a baseline statement, since only the baseline
   settings have a matched field-off run, the driven mean rate being 0.0518
   at every setting; per-neuron phase consistency stays at the field-off
   control level (median PPC −0.005 to −0.015) while the pooled vector
   strength rises from 0.002 to 0.07–0.08, the "many weakly biased cells"
   picture of Sec. 4.9.

### Qualitative fallback wording (for Kaiti)

"At $A_f = 10$ and $\bar\eta = 0.85$ the spiking network's beat depth lies
between 0.09 and 0.16 depending on the spike cutoff and population size
(0.093 at $V_{\rm peak}$ = 100; 0.156 and 0.137 for the cutoff-free theta
form at $N$ = 8000 and 16000), against the mean-field 0.128; at the baseline
settings the mean rate rises by 2.8%." Table S-finite-network can carry the
two theta rows. The sentence "quantitative convergence remains unestablished at this
population size" stays true and now has a measured size dependence behind it.

### Limitations

The population dependence was measured at one doubling; the direction is
toward the mean field, the exponent is not determined, and the step and
population limits are not separated because the largest phase advance per
step grows with $N$ (one more doubling at $N$ = 32000 with a halved step,
about 15 min, would address both, but lies outside the pre-registered list
and was not run). The theta integrator is Euler at the published step,
validated by the half-step check only for these statistics. The equal-power
single-carrier controls remain tested only in the mean field; they are two
runs of the same script (`--runs sc10,sc35`, plus `tt35` for comparison) if
K and Kaiti decide to run them. Phase statistics carry no pass criterion and
are reported as measured. The weak-drive depth at $V_{\rm peak}$ = 100 in the
manuscript (0.093) stands as published; this pilot explains it, it does not
replace it.

### Files

`theta_pilot_{off,on,dt2,n2,long}.json` (settings, statistics, runtimes),
`theta_pilot_{…}.npz` (E rate at 0.1 ms resolution, mean-field rate, window
index), `theta_pilot.log` (timestamped lines), `theta_pilot_protocol.md`.
