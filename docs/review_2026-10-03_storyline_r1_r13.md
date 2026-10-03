# Storyline decisions and R1–R13 audit of v0.14.4

Reviewed October 3, 2026, against manuscript commit `2ccea30` and repository HEAD
`095cb9b`. The scientific argument is ready for a structural decision, but the
earlier disposition log overstates closure of several review items. Some repairs
are present in Theory or Methods while contradictory claims survive in Results,
captions, or the storyline.

This is a review only. No manuscript, bibliography, planning source, PDF, figure,
simulation, or parameter was changed. The release and circulation holds remain.
Line numbers below refer to `TN0484_envelope_demodulation.tex` at `2ccea30`.

## Recommendations on the four decisions

1. **Keep carrier access before the Results; move the detailed transduction tests
   after the model results.** Section 2.6 supplies the assumptions and attenuation
   calculation needed to interpret §4.3, so it is not merely later interpretation.
   Section 2.4's amplitude/harmonic discrimination and spatial consequences lead
   naturally into the predictions, after the reader has seen generation and
   amplification. Retain the product-versus-envelope distinction beside the
   two-tone derivation in §2.2, with a forward reference to the detailed treatment.
   Move all of §2.4's substantive content, including the numerical spatial example
   and the correction for network filtering. This is a proposed relocation, not a cut.

2. **Move Methods §3.2 into Appendix E, before the LaNMM results.** Retain a brief
   description and pointer in the main model overview. Keep the signed-polarization
   input, the explanation of why rate clipping creates an unintended rectifier,
   the FFT estimator and its units, the integration settings, and both signed maps
   with that appendix. This makes the low-carrier extension self-contained.

3. **Promote S11 first; retain S3 and S10 in the supplement.** S11 directly supports
   the abstract's claim that beat-locked rate modulation grows faster than the mean
   shift, and shows both quantities in the same units from the same rate readout.
   The main QIF raster does not substitute for that comparison. S10 is the next
   candidate if the paper is to emphasize the coupling intervention in the exact
   mean field; a later combined JR/NMM2 gain figure could serve that purpose, but
   would be a separate figure-design decision. S3 supports the shared-amplifier
   control, whose mathematical explanation can remain in the main text. None of
   these figures should be deleted. S10's unqualified source-invariance caption
   needs the R4 correction before any promotion.

4. **Keep the new abstract, with local scope corrections.** Its progression from
   the absent input line to mixing, time scales, amplification, and implications
   is clearer than the earlier version. Replace “the corresponding static curve”
   with “its static rate curve” to avoid identifying the QIF curve with the JR
   logistic. Make the model basis explicit in the result sentence. Qualify the
   product-law dose-map sentence with “in this weak-input regime,” and the common
   TI/tACS amplifier with matched input coupling, observable, and operating state.
   These are proposed wording changes, not an applied replacement abstract.

## The map needs qualifications and explicit retention notes

The map's introductory claim that the static and dynamic detectors are “one object”
(p. 2 and the §2.3 row) is too broad. The static QIF curve is an adiabatic limit of
the dynamic QIF population. This does not identify the JR logistic with that curve,
or identify either with measured sodium-channel kinetics. Preserve the constructive
slow-synapse argument and both time-scale conditions; no new periaxonal model is
needed for it.

The §1 row places primate timing results under evidence of network dependence.
Timing changes alone do not establish a circuit mechanism. The synaptic-blockade
and network-model findings provide the relevant network evidence. The §4.7–4.8 row
should say “larger modulation than mean-rate change,” preserving the reported
8–10% QIF rate increase and weak per-neuron locking. It should not restore the
categorical “timing-not-rate” claim.

The §2.3 row must identify `C(Q,omega)` as a **single-carrier DC** coefficient and
separate it from the **two-tone PING beat** calculation. The quoted 1.1%, 0.1%,
and 0.03% are errors of the propagated second-order response at four selected
stable points, not a validation over the complete finite-amplitude sweep.
The §2.7 row should preserve the same distinction when describing the role of `F'`.

The §2.4 row should state “smooth memoryless transfer with nonzero curvature”
for leading square-law detection. The linear envelope law belongs to the specified
ideal rectifiers, not every rectifying biological mechanism. Retain the step
counterexample and its 0.151 harmonic ratio. For the off-resonance test, retain
the actual correction: `|G(2 Omega)/G(Omega)|` is about 1.22–1.25 at the suggested
quarter-resonance frequency, not exactly one.

The §4.3–4.4 row says the open-loop comparison “licenses” the AM surrogate for
dense sweeps. That is the unresolved part of R2. Retain the different DC terms,
the surrogate's extra second harmonic, and the limit of the one-point control.
The §4.6 row should retain approximately fixed leading detection and a changing
network transfer, not imply that damping is the only quantity that changes.

The map's “Arnold-tongue entrainment read by output frequency” and QIF “gating”
phrases repeat the unresolved inference in R7. Retain frequency-dominance maps,
coexisting rhythms, and sidebands as observations; mark phase capture and a unique
amplitude-gating mechanism as unestablished by these measurements. Figure S4 is a
direct low-frequency control, not a two-tone TI capture demonstration.

In the Discussion row, terminals belong under strong polarization, not established
fast access. Retain the area-independent specific `R_m C_m` argument. Preserve
Cohen's 12-nm periaxonal space, the roughly 1-ms fitted decay, and the distinction
from a measured TI transfer; keep the two different Luff papers separately named.

The efficiency row needs the matching convention: TI tones of amplitude epsilon
each versus a direct drive of amplitude `2 epsilon`, at matched peak polarization.
That is not an equal-RMS comparison. Mark the small-input bound as perturbative,
and the 0.3479 optimum as numerically evaluated and restricted to its stated
memoryless family. Preserve the absence of a calibrated mapping from generated
drive to the primate phase statistic. The current “two bounds” summary should
not turn the numerical optimum into a certified inequality.

Add explicit retention entries for the following content that is absent or too
compressed in the map:

- The nonlinear QIF curve at zero recurrence, its non-saturating shape, and the
  distinction between its local slope and curvature.
- The fact that the plotted NMM2/QIF simulations retain finite membrane times;
  the fast-membrane expression is an analytic limit, not a new simulation result.
- The distinction between surviving synaptic resonance and modes that require
  the membrane dynamics eliminated by the reduction.
- Local polarization versus applied field versus normalized QIF current, with
  the QIF field-to-current calibration still unspecified.
- The matched input direction, observable, and operating-state conditions for
  cancelling the common TI/tACS transfer.
- The LaNMM signed suppression fractions for both P1 and P2 drive, the difference
  between loss of band power and a frequency shift, and the missing displayed
  lock-in evidence for the 7%/25% comparison.
- The settling/window and numerical checks, the 45% threshold sensitivity of
  phase concentration, and the remaining reproduction limitations.
- All 22 figure identities, including S3/S10/S11 regardless of their placement.

The last-page statement “None of these is executed in v0.14.4” needs a procedural
correction: decisions 1–3 are unexecuted, but the new abstract is already applied
provisionally. The abstract page and source comment correctly say so.

## R1–R13 are not all closed

“Closed” here means the original issue is resolved at the stated claim level;
it does not imply biological validation. “Partial” means a repair is present but
a conflicting statement or requested evidence remains. “Open” means the main
inference remains unsupported. The audit uses the September 22 consolidated v2
brief, not just its disposition table.

| ID | Status in v0.14.4 | Evidence and remaining action |
|---|---|---|
| R1: level of claim | Closed at the headline level | Abstract, Introduction, Discussion, and Conclusion distinguish model results, assumed access, and unresolved human efficacy. Local overclaims are tracked below rather than treated as closed by those caveats. |
| R2: genuine tones and surrogate | Partial | The two-tone derivation and §4.1 correction are present. Line 492 and Fig. 6d still imply the one-point open-loop comparison validates recurrent sweeps, despite the narrower statement at lines 1259–1263. Qualify those claims or supply the recurrent comparison. The different DC terms matter near Hopf. |
| R3: access assumptions and phase | Partial | The short time is labeled as assumed; quasistatic electromagnetism is separated from membrane charging; gate double counting is removed. Eq. 8 still sums magnitude gains across compartments. Specify this as a phase-aligned/dominant-route approximation, or define a complex effective transfer and a projection into the detector input. “Phases can be retained” does not implement that calculation. |
| R4: fixed detection | Partial | The fast-carrier asymptote and four-point second-order check are present. §4.6 line 1336 still says “only gamma changes,” and its next sentence makes the gain depend only on distance to criticality. S10 states exact source independence; Methods applies the approximately 1% result to the J sweep without a full-sweep check. Keep local curvature fixed in JR while allowing modal projections to vary; scope the PING evidence to the tested perturbative conditions. |
| R5: timing versus mean rate | Partial, numerical repair present | `timing_not_rate.py:90` now uses `Sigm(v + s3)`; QIF has per-neuron PPC and the reported mean-rate change. S12's title at line 2295 still says “Timing, not rate,” and the phrase survives in §4.6 and the map. Replace the categorical wording consistently; retain the weak per-neuron result. |
| R6: signed LaNMM evidence | Partial | Signed maps and the FFT estimator are fixed. The 7%/25% lock-in contrast still points to Figs. S1/S7, whose panels are band-power changes. The generator renders `Pc1/Pc2`; its producer defines a lock-in function but does not save a lock-in map in these caches. Display or cite the corresponding lock-in calculation, or narrow the claim. State the 99.5th-percentile color saturation and 2-s settling/3-s measurement convention. |
| R7: entrainment and gating | Open | Methods/App. F acknowledge a frequency-dominance screen, and the zero-drive contour artifact is fixed. Results, S4/S7/S8, and the QIF text still assert capture or infer its absence from 11-Hz detuning. The rate fold and sidebands do not uniquely establish gamma-amplitude gating. Either propagate the narrower observational language or perform the relevant phase/modal-amplitude tests. The tests are not required if the stronger claims are withdrawn. |
| R8: detector classes | Closed for the specified comparisons | The step detector is separated from a linear envelope follower, its harmonic ratio is 0.151, and transduction class is not identified with anatomy. Preserve those restrictions when shortening the map. The nonzero-curvature qualification belongs to R9. |
| R9: mathematical scope | Partial | Appendix C now correctly restricts its conclusion to the weak-input cubic normal form and linear readout; saturation and power-versus-amplitude distinctions are partly present. Eq. 20 still uses the canonical oscillator expression with the eigenvalue imaginary part as its undamped frequency; Fig. 4 quotes the corresponding peak-shift formula as exact. Introduce the actual network resolvent, retain the Hopf approximation as an approximation, and scope the remaining square-law summaries to nonzero curvature. |
| R10: efficiency comparison | Partial, scope repaired | The memoryless comparison, matching convention, and lack of human calibration are now explicit. Lines 1638–1639 give a ratio proportional to epsilon but say relative efficiency decreases with input amplitude. It increases with amplitude at fixed operating point in this weak-input approximation, or decreases as the field is weakened. Correct that reversed sentence. |
| R11: retrospective exponent fit | Closed | Discussion states that an unspecified nonlinear mapping to PLV prevents identification of the exponent. The earlier proposed retrospective fit is no longer asserted to identify it. |
| R12: numerics and reproduction | Partial | Longer settling, whole-cycle windows, time-step/threshold checks, corrected Hopf location, and spectrum labeling are present. No complete clean reproduction or population-size/initial-condition convergence record was found in the reviewed material. `run_all.py:147` still skips all data-only producers under `--only`; its gap list retains the kHz cache without a standalone producer. The LaNMM plotter hardcodes its output directory, contradicting the README's scratch-output guarantee. |
| R13: static versus dynamic mixing | Closed for the model distinction | The QIF static curve, DC crossover, fast two-tone source, units, and model-specific state dependence are present. QIF is not used as validation of the JR curvature law. The remaining finite-frequency/full-sweep scope and phase issues are R3/R4, not a reason to discard the slow-synapse connection. |

Thus four items are closed at their stated scope (R1, R8, R11, R13), eight are
partial, and R7 remains open. R5 and R10 need local wording repairs; their underlying
numerical/scope corrections should be preserved. The historical September 22
disposition should not be used as a current all-clear.

For R3, a scalar effective carrier input with complex amplitudes
`z_j = K(omega_j) E_j` produces a static beat proportional to
`(sigma''/2) Re[z_2 conjugate(z_1) exp(i Omega t)]`. Here `K` includes the defined
projection from compartment voltages to the detector input, `E_j` is the applied
tone amplitude, and `Omega = omega_2 - omega_1`. This expresses the phase issue
without adding a periaxonal circuit.

For R9, with Jacobian `J`, effective input vector `b`, and readout vector `c`, the
linear transfer is `G(Omega) = c^T (i Omega I - J)^(-1) b`. Near a simple Hopf pair,
its resonant term has a parameter-dependent residue divided by
`gamma + i(Omega - omega_H)`. That gives the leading `1/gamma` peak growth when the
residue is nonzero. It does not make the full network a constant-numerator
canonical oscillator or make only gamma change in a coupling sweep.

## The Cifra citation needs a scope clause, not a threshold claim

Cifra et al., *Chemical Society Reviews* **55**, 7568–7616 (2026),
[doi:10.1039/D3CS00244F](https://pubs.rsc.org/en/content/articlehtml/2026/cs/d3cs00244f),
§4.1 and Fig. 15 (journal p. 7588; local PDF p. 22), exclude fields below
0.1 kV/m from their focus because direct molecular effects are expected to be
small relative to thermal fluctuations. This is not a universal onset threshold;
the figure expressly treats the response statistically.

Proposed Discussion clause: “direct field-induced protein structural changes are
reviewed mainly at much stronger fields, with fields below 0.1 kV/m outside that
review's scope [Cifra et al.].”

Keep this distinct from channel responses driven through membrane polarization;
the review does not rule out that cellular mixing route. Place the citation in
the Discussion, not as evidence for a gate cutoff. It has not been added to the
manuscript or bibliography.

## Review evidence and limits

Read the seven-page storyline and all changed redline pages, compared the v0.14.3
and v0.14.4 source diff, and checked the current manuscript passages and relevant
figure pages. Inspected the JR rate readout, QIF measurement code, LaNMM map producer
and plotter, PING check source/results, and reproduction orchestrator. An AST check
confirmed that `--only` excludes the producers; no simulation or figure-generation
pipeline was run. The previously recorded PING errors are 1.0698%, 0.09429%, and
0.02354% at 300, 1000, and 2000 Hz across the four stored states; those checks were
inspected, not represented as new full-grid validation. The official Cifra article
and the downloaded PDF were checked for the scope statement.

The next action remains K's four structural/abstract decisions. Repairs listed
here are proposals for the subsequent authorized pass, with no content removed
or reordered during this review.
