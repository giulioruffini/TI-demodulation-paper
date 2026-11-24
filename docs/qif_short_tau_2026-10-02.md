# Shorter membrane time scales increase carrier access in a QIF reduction

Research note, October 2, 2026. This analysis follows K's request to use existing
biophysics and assess a shorter effective QIF time scale. It does not implement
a periaxonal circuit or revise the manuscript. Numerical results are in
`qif_short_tau_2026-10-02.json`; reproduce them from the repository root with
`.venv/bin/python code/qif_short_tau_check.py`.

## Published time constants describe different response modes

| Source | Number and its meaning | Use in this analysis |
|---|---|---|
| [Cohen et al., Cell (2020)](https://doi.org/10.1016/j.cell.2019.11.039), STAR Methods, “Spatial Resolution and Parameter Bounds” | Minimum time constant approximately **1 ms**, from exponential fits to averaged axonal responses, used to choose spatial resolution. | Supports considering millisecond axonal dynamics; it is not a measured TI access time constant. |
| [Luff et al., PWM-TI, Brain Stimulation (2024)](https://doi.org/10.1016/j.brs.2023.12.010), Methods 2.3 and Fig. 5C–F | A **1 ms** passive RC example and a **1–100 ms** parameter range, varying leak conductance at fixed specific capacitance. This simplified experiment used intracellular current stimulation. | A short time scale already used in Grossman's modeling, independently of Cohen. |
| [Semenov et al., Cell Reports Physical Science (2025)](https://doi.org/10.1016/j.xcrp.2025.102660), Fig. 4 | External-field charging **0.70 ± 0.08 μs** at the cathodic pole and **0.65 ± 0.05 μs** at the anodic pole (mean ± SEM, 19 experiments). Measurements used 2-μs, 140-V/cm pulses in isolated hippocampal neurons. | Direct evidence that field-induced charging can be much faster than the response to intracellular current injection. It does not identify a periaxonal mechanism or calibrate the whole QIF time constant. |

The first comparison below therefore includes 1 ms as a literature-motivated
sensitivity case and 0.15–0.2 ms as more exploratory cases. None of these values
is claimed to be a fitted periaxonal TI parameter.

## The inspected Grossman articles do not use Cohen's nanocircuit

The search used Grossman's [Imperial publication list](https://profiles.imperial.ac.uk/nirg/publications)
and the following main articles and reference lists. No citation of Cohen's 2020
nanocircuit paper or implementation of that mechanism was found in these texts.
Other occurrences of “Cohen” referred to statistics, motor learning, or MEG.

| Article | DOI |
|---|---|
| Violante et al., human hippocampal TI (2023) | [10.1038/s41593-023-01456-8](https://doi.org/10.1038/s41593-023-01456-8) |
| Wessel et al., striatal theta-burst TI (2023) | [10.1038/s41593-023-01457-7](https://doi.org/10.1038/s41593-023-01457-7) |
| Luff et al., PWM-TI (2024) | [10.1016/j.brs.2023.12.010](https://doi.org/10.1016/j.brs.2023.12.010) |
| Luff et al., The neuron mixer (2024) | [10.1016/j.celrep.2024.114274](https://doi.org/10.1016/j.celrep.2024.114274) |
| Kurtin et al., resting-state connectivity after TI (2025) | [10.1016/j.brs.2025.04.010](https://doi.org/10.1016/j.brs.2025.04.010) |
| Rintoul et al., acoustoelectric neural recording (2026) | [10.1038/s44172-026-00598-4](https://doi.org/10.1038/s44172-026-00598-4) |
| Rintoul et al., acoustoelectric neuromodulation (2026) | [10.1038/s41467-026-73826-2](https://doi.org/10.1038/s41467-026-73826-2) |

This is a bounded negative finding about the inspected published articles.
It does not exclude an unpublished model, a different reference, or a suggestion
Nir made in conversation. The 2026 acoustoelectric work concerns mixing between
acoustic and electric fields, a different mechanism from periaxonal access.

## The QIF membrane admits larger carrier excursions when its effective time scale is shorter

For an uncoupled population, let r be the physical firing rate in Hz, v the
dimensionless mean voltage, tau the membrane time scale in seconds, Q the
constant normalized drive, and Delta the Lorentzian excitability half-width.
The input amplitudes a1 and a2 are normalized currents, with angular frequencies
w1 and w2 in radians per second. The equations are

\[
\tau\dot r=\frac{\Delta}{\pi\tau}+2rv,\qquad
\tau\dot v=v^2+Q-(\pi\tau r)^2+
a_1\cos(\omega_1t)+a_2\cos(\omega_2t).
\]

Write r_star and v_star for the field-free equilibrium. Its linear voltage
response to a unit input at angular frequency w is

\[
H_v(\omega)=\frac{d+i\omega\tau}
{(d+i\omega\tau)^2+(2\pi\tau r_*)^2},\qquad d=-2v_*>0.
\]

When w*tau is large compared with both d and 2*pi*tau*r_star,
the voltage excursion is approximately a/(w*tau). For the frequency difference
Omega=w2-w1, the cross term in v squared then contributes

\[
(\delta v)^2\supset
\frac{a_1a_2}{\omega_1\omega_2\tau^2}\cos(\Omega t).
\]

This is the source inside the undivided tau*v_dot equation. Dividing the whole
equation by tau divides the source too; it does not insert another membrane
filter. Reducing tau by a factor s increases this source by approximately 1/s^2
while the high-frequency approximation remains valid. The exact response above
must replace that approximation once the carrier approaches the population's
intrinsic rates.

All comparisons keep the mapping from the applied field to the normalized input
amplitudes fixed. This is an assumption about the reduced model. In a physical
RC circuit, reducing tau through resistance at fixed capacitance and fixed
injected current also changes the DC current-to-voltage gain: high-frequency
voltage approaches I/(i*w*C), independently of resistance. A shorter measured
time constant alone therefore does not specify the field-to-voltage amplitude.

## Matching the baseline preserves the increase in the quadratic source

Holding Q and Delta fixed gives

\[
r_* = \frac{1}{\pi\tau}
\sqrt{\frac{Q+\sqrt{Q^2+\Delta^2}}{2}},\qquad
v_*=-\frac{\Delta}{2\pi\tau r_*}.
\]

Thus changing tau alone raises the physical firing rate as 1/tau. To separate
that effect from access, the controlled comparison holds both r_star and v_star
fixed. Starting from tau0=15 ms, Q0=0, Delta0=1, the baseline is r_star=15.005 Hz
and v_star=-1/sqrt(2). For s=tau/tau0, it sets

\[
\Delta_s=s\Delta_0,\qquad Q_s=s^2(Q_0+v_*^2)-v_*^2.
\]

The following numbers use the exact linear response at a 1-kHz carrier. The
quadratic-source ratio uses tones at 980 and 1020 Hz and equals the magnitude of
their voltage-phasor product relative to the 15-ms value.

| tau (ms) | Q | Delta | Voltage amplitude / input amplitude at 1 kHz | v-squared beat-source ratio |
|---:|---:|---:|---:|---:|
| 15 | 0 | 1 | 0.01061 | 1 |
| 1.5 | -0.495 | 0.1 | 0.10495 | 97.8 |
| 1 | -0.497778 | 0.066667 | 0.15530 | 214 |
| 0.2 | -0.499911 | 0.013333 | 0.52857 | 2,480 |
| 0.15 | -0.499950 | 0.01 | 0.58840 | 3,073 |

The baseline rate and voltage are identical in every row; drive and heterogeneity
are explicitly recalibrated. These are sensitivity results for a QIF reduction,
not estimates of human TI efficacy. The last column measures the v-squared source,
not the total population response. The calculation also includes the r*v and
r-squared contributions to the full second-order response, then propagates that
source through the population's response at 40 Hz. Those rate coefficients are
reported separately in the JSON.

Direct nonlinear integrations at input amplitudes 0.05 and 0.025 per tone checked
the complex beat coefficient for tau=15, 1.5, and 0.15 ms. Extrapolating the
amplitude-normalized coefficients to zero amplitude agreed with the second-order
calculation to relative errors of 2.2e-8, 1.6e-9, and 1.3e-5, respectively. The
measurement windows contain whole cycles of both carriers and the beat.

## The recurrent amplifier needs recalibration after a global time-scale change

In the paper's PING model at coupling C=15 and common background excitability
eta=0, shortening both excitatory and
inhibitory membrane time scales by the same factor, with every other parameter
fixed, preserves the dimensionless voltages but multiplies physical rates by
the reciprocal factor. The excitatory rate goes from 47.99 Hz to 479.91 Hz for
a tenfold reduction and to 4,799 Hz for a hundredfold reduction. The least-damped
oscillatory mode shifts from 53.21 Hz to 109.30 Hz and 105.81 Hz, respectively,
and becomes more strongly damped. These mode frequencies are not asserted to be
the maxima of the forced-response spectrum.

The supported reduced-model conclusion is that shorter effective membrane
dynamics can substantially strengthen the carrier excursions reaching the QIF
quadratic, including in a comparison with matched baseline rate and voltage.
These parameter changes do not obstruct the existing adiabatic reduction of NMM2.
A comparison at fixed physical rates requires consistent parameter normalization,
but the conceptual starting point is the slow-synapse limit below.

## A fast membrane gives the established slow-synapse reduction

As Giulio pointed out after reviewing these results, fast membrane dynamics relative
to synapses put NMM2 in its existing slow-synapse regime. Section 3.1 of
[Clusella et al. (2023)](https://doi.org/10.1007/s00422-022-00952-7) derives this map
to a model with a static transfer curve. No new periaxonal implementation is needed
to study this limit.

Let Q be the total normalized drive in the MPR voltage equation, with the synaptic
normalization retained from that equation. If the rate and voltage relax to their
attracting equilibrium much faster than Q changes, setting their fast derivatives
to zero gives

\[
r(t)\simeq\Phi_{\tau_m}(Q(t)),\qquad
\Phi_{\tau_m}(Q)=\frac{1}{\pi\tau_m}
\sqrt{\frac{Q+\sqrt{Q^2+\Delta^2}}{2}}.
\]

Here Delta is the excitability half-width and r is the physical firing rate. The
second-order synaptic equations remain dynamic, with this rate as their input.
The static curve is nonlinear even without recurrent coupling.

This reduction applies to slow synaptic inputs when the population relaxation time
is short relative to synaptic variation. Applying the same static curve directly
to the kHz carrier requires the stronger condition that population relaxation is
also fast relative to the carrier. In that regime, consider a perturbation
q(t)=a1*cos(omega1*t)+a2*cos(omega2*t) about a background Q0. Here a1 and a2
are the input amplitudes and omega1 and omega2 their angular frequencies. The
second-order difference-frequency term in the rate is

\[
\frac{1}{2}\Phi_{\tau_m}''(Q_0)a_1a_2
\cos[(\omega_1-\omega_2)t].
\]

The static curve therefore supplies mixing through its curvature, while its slope
sets the local gain entering recurrent synaptic feedback. The remaining synaptic
network can support resonance for suitable architecture and parameters; a resonance
depending on the eliminated membrane dynamics need not survive. If only the
synaptic time-scale separation holds, carrier mixing must instead be evaluated
from the fast driven subsystem before reducing the slow network dynamics.
