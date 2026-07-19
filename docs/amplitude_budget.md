# The TI amplitude budget

Working note, 2026-07-19. Four stages sit between an applied field and a firing-rate
modulation at the envelope frequency. Three lose amplitude and one recovers it. This note
puts a verified number on each, then runs the head-to-head comparison at matched field.

All empirical constants were fetched from primary sources. Where the commonly quoted figure
differs from what the source says, the discrepancy is noted — there were several.

## The four stages

| | Stage | Factor | Value |
|---|---|---|---|
| 1 | Field → membrane polarization | $\lambda$ | 0.12–0.49 mV per V/m |
| 2 | Carrier low-pass at $f_c$ | $\kappa(f_c)$ | 0.003–0.62, compartment-dependent |
| 3 | Envelope transduction by $\Sigma''$ | $\eta = r\varepsilon/4$ | 0.003–0.014 at human fields |
| 4 | Network amplification near the Hopf | $Q = \pi f_0\tau$ | 3–63, median $\approx 8$ |

Stages 1–3 are losses; stage 4 is the only gain. Stage 3 has not previously been quantified,
and its *form* matters more than its size.

## Stage 1 — field to membrane

$\lambda \approx 0.2$ mV/(V/m) is the standard figure and it is **mis-attributed**. Bikson
et al. 2004 measured $0.12 \pm 0.05$ mV per mV/mm in rat CA1 — 40% lower. The 0.2 traces to
Deans et al. 2007: $0.18 \pm 0.04$ mV/(V/m) at DC in CA3, rising to $0.21 \pm 0.03$ at 10 Hz
(not significant). Radman et al. 2009 gives, for rat L5/6 pyramidal somata — the
tES-relevant population — a polarization length up to **0.49 mm**, 2.5× the usual figure.
Radman reports ranges only, so any "mean" cited to it is unsupported.

Note $1$ mV/mm $= 1$ V/m exactly, so mV/(V/m) and polarization length in mm are numerically
interchangeable.

Rest to threshold is **~22–24 mV** (Koga et al. 2010, mouse ACC L2/3, in vivo). The familiar
"10–20 mV" could not be confirmed from any primary source and looks like textbook folklore.
The verified number makes the gap *larger* than the usual framing: at 0.8 V/m (the corrected
Huang value at 2 mA), somatic polarization is 0.10–0.39 mV against ~23 mV, a shortfall of
**60–240×**.

This is the ordinary weak-tES problem and it applies to tACS equally. It is the gap that
network amplification exists to answer.

## Stage 2 — the carrier filter, and a wrong premise in the paper

$\kappa(f_c) = [1+(2\pi f_c\tau_m)^2]^{-1/2}$. At $f_c = 1$ kHz:

| compartment | $\tau_m$ | $\kappa$ | source |
|---|---|---|---|
| bouton | 48.5 ms **[unconfirmed]** | 0.0033 | Szabadics & Soltesz 2009 |
| soma, human L2/3 | 16.5 ms | 0.0097 | Eyal et al. 2016 |
| soma, in vivo | 8.4 ms | 0.019 | eNeuro 2018 |
| axon | ≤1 ms | 0.157 | Esmaeilpour et al. 2021 |
| node, myelinated | 0.3 ms | 0.469 | Cassarà et al. 2025 |

**The paper's fast-element argument contains an error.** Around line 1349 it invokes
presynaptic terminals, which "polarize ~2–10× more than somata," as a fast compartment. The
*sensitivity* claim is verified (Chakraborty et al. 2018 measure ~4×), but the *speed* claim
is not.

A caution on the counter-evidence. Whole-bouton recordings are reported to give
$\tau_m = 48.5 \pm 3.5$ ms — slower than the soma — but **I could not confirm that number
from the primary source.** The record is real (Szabadics & Soltesz 2009, *J. Neurosci.*
29(13):4239–4251, PMID 19339618), the figure sits in the body rather than the abstract, and
the full text was unreachable. It should be checked against the PDF before being used
anywhere. The correction below therefore rests on the physics, not on that measurement, and
the paper edit cites no number.

The underlying premise, that small compartments are electrically fast, is false regardless.
For an
isopotential compartment $\tau_m = R_m C_m$ with both per unit area, so $\tau_m$ does not
scale with size: a small terminal has small $C$ *and* large $R_{\rm in}$. Short axonal time
constants come from myelinated/nodal membrane with high leak conductance, not from size.

The fix is to keep the claims apart. Terminals are the *sensitive* compartment; nodes and
axons are the *fast* one. The paper's separate list (axon, AIS, node, $\tau \approx 0.2$ ms)
is well supported by the 0.3 ms myelinated value and should carry the fast-element argument
alone.

An empirical check, and it is reassuring: Esmaeilpour et al. 2021 measured slice thresholds
of ~5 V/m at 100 Hz, ~60 V/m at 1 kHz, ~80 V/m at 2 kHz — ratios of 12× and 16×, against
5.4× and 10.7× for an exact single-RC with $\tau_m = 1$ ms. **The real roll-off is flatter
than first-order at 2 kHz**, so the $\kappa$ above is conservative. Aspart et al. 2018 shows
why: cutoff is set by $\tau$ *and* electrotonic length, and bent cables exhibit a resonance,
so a realistic neuron is not monotonically low-pass in field sensitivity.

## Stage 3 — envelope transduction, and why it cannot be out-amplified

You suspected this stage adds a reduction. It does, and its form is the point.

For two carriers of amplitude $\varepsilon$ each in membrane-polarization units, the
square-law detector delivers a drive at $\Delta f$ of $\tfrac12\Sigma''\varepsilon^2$.
Against direct drive at $\Delta f$ at the same *peak* polarization $2\varepsilon$, which
gives $2\Sigma'\varepsilon$, the transduction efficiency is

$$\boxed{\;\eta \;=\; \frac{\tfrac12\Sigma''\varepsilon^2}{2\Sigma'\varepsilon} \;=\; \frac{r\,\varepsilon}{4}\;}$$

with $r = \Sigma''/\Sigma' \approx 0.56$ mV$^{-1}$ off the inflection.

**$\eta$ is proportional to the drive amplitude.** Break-even ($\eta = 1$) needs
$\varepsilon = 4/r \approx 7.1$ mV, the same order as the 23 mV from rest to threshold. So in
the weak-field regime the detector is always lossy, and *the loss worsens as the field
weakens*. At $\varepsilon = 0.1$ mV it costs 71×.

One consequence belongs in the paper plainly: **the transduction penalty cannot be recovered
by the resonance.** $Q$ is a gain applied downstream of the detector, so it scales TI and
tACS alike and cancels in their ratio. A quadratic detector followed by a linear amplifier is
still a quadratic detector.

## Stage 4 — network amplification

$Q = \omega_0/2\gamma = \pi f_0\tau$: $\pi$ times the number of cycles the ringing survives
(derivation in §7). With the verified Wilting & Priesemann range ($\tau$ 100–2000 ms,
**median ≈ 250 ms**; $\hat m$ 0.963–0.998 at $\Delta t = 4$ ms) and $f_0 = 10$ Hz, $Q$ runs
from 3 to 63, with **$Q \approx 8$ at the median**.

## The head-to-head at 1 V/m

Same peak field; tACS applied at 10 Hz versus TI through a 1 kHz carrier; drive in units of
$\Sigma'$:

| | polarization | drive at 10 Hz | vs tACS |
|---|---|---|---|
| **tACS at 10 Hz** | 0.200 mV | $2.0\times10^{-1}$ | 1 |
| TI, node (0.3 ms) | 0.047 mV | $6.2\times10^{-4}$ | $3.1\times10^{-3}$ |
| TI, axon (1 ms) | 0.016 mV | $6.9\times10^{-5}$ | $3.5\times10^{-4}$ |
| TI, soma (16.5 ms) | 0.0010 mV | $2.6\times10^{-7}$ | $1.3\times10^{-6}$ |
| TI, bouton (48.5 ms) | 0.0003 mV | $3.0\times10^{-8}$ | $1.5\times10^{-7}$ |

At matched field TI is **300× weaker than tACS at best** (fast nodal membrane), and a million
times weaker at the soma. Applying $Q$ at the median leaves the node case ~41× short; even at
the extreme $\tau = 2$ s it is ~5× short.

Isolating stage 3 alone, with no carrier filtering at all ($\kappa = 1$), the square law
still costs **71×**. The transduction penalty is real and large independently of the membrane
question.

## What the quadratic detector does to rodent-to-human translation

This falls out of $\eta \propto \varepsilon$, and I think it is the most useful thing here.

Rampersad et al. give 383 V/m in mouse at 0.776 mA against 0.24–0.57 V/m in optimized human
montages — a field ratio of roughly **770×**. Because the detector is quadratic, demodulated
drive scales as $E^2$, so that becomes

$$\left(\frac{383}{0.5}\right)^2 \approx 5.9\times10^{5}.$$

**A ~770× field advantage becomes a ~590,000× advantage in demodulated drive.** Concretely:
in mouse $\varepsilon \approx 18$ mV, above the 7.1 mV break-even, so $\eta \approx 2.5$ and
the detector runs at unity efficiency or better. In humans $\varepsilon \approx 0.023$ mV,
so $\eta \approx 0.003$ and it is 305× lossy. The mouse is not a scaled-down human here; it
is operating in a different regime of the same nonlinearity.

That is a quantitative, mechanism-derived account of why TI translates poorly from rodent to
human — derived from *our own* model, which is what makes it worth leading with rather than
burying. Rampersad's "currents over 500 mA per electrode pair would be required" is the
linear version of the same statement; ours says the true penalty is the square of theirs.

## Consequences for the paper

1. **Lead the Discussion with the budget, not with the mechanism's success.** The mechanism
   explains TI's phenomenology — carrier independence, $\Delta f$ tuning, timing without rate
   change — and it explains the translation failure. It does not close the amplitude gap at
   human fields. Saying so is far stronger than leaving the dose question qualitative; a
   referee holding Rampersad and Karimi will otherwise say it for us.
2. **Separate the two gaps explicitly.** $Q$ answers "why does any weak field do anything";
   $\Sigma''$ answers "why is there anything at $\Delta f$ at all". $Q$ cancels in the
   TI/tACS ratio and cannot be offered as the answer to the second question.
3. **Fix the terminal/fast-element conflation** (§2). Substantive correction, not wording.
4. **Correct line 544**: "human L2/3 pyramidal cells ~12 ms" cites `deitcher2017` and
   `eyal2016` together, but Eyal reports $16.5 \pm 3.7$ ms, not 12. Deitcher supports
   12.03 ± 1.79. Cite them separately so they bracket the adopted 16 ms.
5. **`fig:jcurve` stays in the main text.** It shows coupling setting $\gamma$ and hence $Q$
   — the only tunable term in the budget, and the line back to the $J$-tuning in Clusella.
6. **Add the $\Delta f$-detuning prediction.** Resonance FWHM is $1/(\pi\tau)$: 1.3 Hz at the
   median $\tau$, 0.16 Hz at the upper end. Individual alpha drifts more than that within a
   session, which turns the occipito-parietal alpha null in Mansourinezhad et al. into a
   design specification rather than a refutation — but only if the bandwidth is stated in
   advance with a predicted detuning curve and a closed-loop experiment. Invoked after the
   fact it is special pleading.

## The $Q$ derivation

Linearizing about the stable focus, $\lambda_\pm = -\gamma \pm i\omega_0$, the impulse
response is $\propto e^{-\gamma t}\cos(\omega_0 t+\phi)$ and the reverberation time is
$\tau = 1/\gamma$. From

$$\chi(\Omega) = \frac{1}{\bigl[\gamma+i(\Omega-\omega_0)\bigr]\bigl[\gamma+i(\Omega+\omega_0)\bigr]}$$

we get $|\chi(\omega_0)| \simeq 1/(2\gamma\omega_0)$ and $|\chi(0)| \simeq 1/\omega_0^2$ for
$\gamma \ll \omega_0$, so

$$Q = \frac{|\chi(\omega_0)|}{|\chi(0)|} \simeq \frac{\omega_0}{2\gamma} = \pi f_0\tau
= \pi\frac{\tau}{T_0},$$

with half-power width $\gamma/\pi$, so $Q = f_0/\Delta f_{\rm FWHM}$ consistently. Verified
numerically: the exact ratio matches $\pi f_0\tau$ to within 2% at $\tau = 100$ ms. In
branching-parameter form, $\tau \simeq \Delta t/(1-m)$ gives $Q \simeq \pi f_0\Delta t/(1-m)$.

## Why the measured $\tau$ cannot be used as $1/\gamma$ for alpha

My earlier caveat was too soft. **Wilting & Priesemann's $\tau$ cannot be identified with the
damping rate of an alpha-band mode**, on four independent grounds.

Their model is $A_{t+1}|A_t = m A_t + h$, a first-order autoregressive process. A scalar
AR(1) has a single real eigenvalue; complex eigenvalues, hence oscillation, require AR(2) or
higher. **There is no frequency parameter anywhere in the estimator.** The fitted
autocorrelation $r_k = b\,m^k$ is a monotone exponential with no cosine factor and no zero
crossings. The observable is wideband summed population spiking with no band decomposition.
And where oscillations are present the authors treat them as residual structure the model
does not absorb — for seasonal epidemic data they had to bolt on an explicit cosine with an
externally supplied period, precisely because the base model cannot generate an oscillation,
and that modified model was never applied to the neural data.

Compounding this, none of the three preparations is an alpha setup: rat hippocampus is a
theta structure, the cat is anesthetized V1, the monkey is PFC during working memory.

**The defensible citation**: in-vivo cortical population activity exhibits an aggregate
relaxation timescale of a few hundred milliseconds — a wideband, mode-agnostic statement
about proximity to instability, not a measurement of any rhythm's damping. Used that way it
motivates the order of magnitude of $Q$ without pretending to measure it. Used as $1/\gamma$
for alpha it is simply wrong, and a referee who knows the estimator will say so.

Related: **Priesemann et al. 2014 is not independent confirmation.** It reports no $m$ and no
$\tau$; its parameter is $\alpha \approx 0.98$–0.99 from a different method, and it is
largely a negative result about the naive estimator. Do not present the two as agreeing
measurements of one number.

## Two citation traps found during verification

**Huang et al. 2017 must be cited with its correction.** The erratum was a stimulator-spec
misreading — peak-to-peak read as zero-to-peak — so "all values we reported in the paper for
measured voltages and field magnitudes have to be multiplied by a factor of 2." This
inverted the paper's headline: originally measured fields were *smaller* than models
predicted; corrected, they agree. Pre-correction figures still circulate, so anyone citing
the 2017 paper alone quotes values 2× too small.

**TI really does use more current than tACS, but the factor depends on convention.** All
three major human TI studies (Violante 2023, Wessel 2023, Vassiliadis 2024) report 2 mA
**per channel, baseline-to-peak**, i.e. 4 mA total; conventional tACS is reported at 1–2 mA
**peak-to-peak**. Like-for-like that is **4–8× more current**, and the naive "2 mA in both"
comparison understates it by at least 2×. This matters for the budget: TI's ~0.5 V/m at
depth is achieved at roughly 4× the current, so the per-milliamp comparison is worse than the
per-field comparison above.

One unresolved discrepancy: Wessel and Vassiliadis use the same montage, current and group
but report 0.26 versus 0.5–0.6 V/m in striatum, almost exactly 2×. Plausibly envelope
amplitude versus peak-to-peak, but neither text confirms it. **Cite one paper and its stated
quantity; do not merge them.**

## Still unverified — do not quote

Radman's mean polarization length (ranges only); any dendritic mV/(V/m) attributed to Bikson
2004; any human in-vivo coupling constant (none exists — Opitz and Vöröslakos measure fields,
not coupling); McCormick 1985 and Mason & Larkman 1990 $\tau_m$ values; Destexhe & Paré's
"~4 ms" in-vivo $\tau_m$, additionally contested by a 2018 study finding TTX did not change
in-vivo $\tau_m$.
