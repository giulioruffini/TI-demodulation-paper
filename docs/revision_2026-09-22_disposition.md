# Disposition log — revision to v0.14.0 (2026-09-22)

Source of the issue IDs: Kaiti's consolidated brief v2 (`_private/reviews/2026-09-22_kaiti_v2/`),
Giulio's decisions memo of the same day, and the readability/notation review
(`docs/review_2026-09-22_readability_notation.md`). Status vocabulary: **implemented**,
**retained** (with justification), **deferred** (the associated claim removed or narrowed),
**removed**.

## R — priority issues

| ID | Issue | Status | What was done |
|---|---|---|---|
| R1 | One level of claim | implemented | Abstracts, Introduction, Discussion and Conclusion rewritten around three levels (model results, coupling assumptions, biological hypotheses). "Reproduces TI's known behavior" gone; the doors are a hypothesis in an access-filter model. Opening no longer claims uniqueness. |
| R2 | Genuine two tones primary | implemented | Introduction Eq. (am) is now the two-tone sum; sec:coupling derives the beat from the cross term (N1) and defines the AM surrogate separately (eq:amsur) for the dense sweeps only. Surrogate control described as an open-loop check at one operating point, not a recurrent test. |
| R3 | Fast access is a model assumption | implemented | "In this access-filter model" qualifies the doors; "candidate route"; TMS inferences removed; Clusella Eq. (17) correctly described as the slow-input QIF transfer, not a logistic. Eq. (doors) still sums scalar magnitudes; phase of the access transfer noted as an assumption of the model (not re-derived). |
| R4 | Fixed coefficient does not fix detection | implemented | New sec:dynamic gives the fast-carrier source and its error against the exact second-order response (1.1 / 0.1 / 0.03 % at 300 / 1000 / 2000 Hz, four states, `ping_fast_carrier_check.py`, Fig. crossover b). "No pinning needed" now rests on that, and the JR pinned sweep is described as holding the local curvature fixed while the network transfer changes. |
| R5 | Timing-versus-rate evidence | implemented | `timing_not_rate.py` rate read-out now includes the field; both AC and DC read from the same rate in the same units (Fig. timing regenerated): modulation 26 to 346 mHz, mean shift −1.3 to −7.7 mHz, ratio 19 to 66. QIF: per-neuron PPC added; "timing, not rate" replaced by a factor-of-three statement at the population level with weak per-neuron locking. |
| R6 | LaNMM maps hid the negative part | implemented | Maps regenerated signed on a zero-centered scale; Methods state the FFT band-power estimator; text reports 95 / 97 % negative fractions (P1-driven) and 44 / 31 % (P2-driven). The "broadband in carrier" claim is scoped to the lock-in read-out. |
| R7 | Entrainment criterion | deferred (claim narrowed) | Zero-drive row excluded from the capture contour (0.5 Hz resolution floor stated); the set is now called the frequency-dominance set and described as a screen, not a capture test; the gamma-amplitude inset (45–70 Hz filter, fold from 40 ms) replaced by a rate fold over the full window. A phase-based capture test was not run; no capture claim depends on it. |
| R8 | Square law vs envelope follower not a binary | implemented | Step detector added (arccos law; harmonic ratio 0.151 at the optimum, `threshold_bound_check.py`); "confirms rectification / decides" replaced by "distinguishes these effective response laws under the stated controls". |
| R9 | Mathematical scope | partly implemented | Nonzero-curvature condition stated; ω0 vs canonical frequency noted; Lorentzian in power; H renamed H_s and called low-pass. Stuart–Landau appendix retained with its odd-forcing/linear-observable scope (the even-mode attraction argument was not re-derived; the claim is restricted by the surrounding text, not the appendix itself). |
| R10 | Memoryless bound vs dynamic estimate | implemented | Bound moved to App. bound as a memoryless comparator with its convention stated; efficiency symbol renamed η_det; Discussion budget retitled and its metaphors removed; Vieira's reduced-locking phenotype noted. A scenario table of couplings was not added: the assumptions are stated in prose with sources. |
| R11 | Retrospective exponent fit | removed | Replaced by one sentence on non-identifiability and the prospective test. |
| R12 | Numerics and reproduction | implemented | QIF: 800 ms settle, integer-cycle windows, dt and threshold checks; Hopf at η̄ = 1.110 from the Jacobian (finite-size-offset paragraph removed); Fig. 3 spectrum labeled as amplitude; tone frequencies quoted exactly; `run_all.py` map covers all two-tone figures and the new scripts. Fig. 6(b) range stated (0.05–0.2 mV fit). |
| R13 | Static transfer vs fast-carrier detector | implemented | New sec:dynamic with the closed-form C(Q, ω), its limits, the sign change, the PING fast-carrier source and Fig. crossover; consequences propagated to sec:nmm, sec:opp, predictions, Discussion, Conclusion. |

## A — answers to the PDF comments

| ID | Status | Note |
|---|---|---|
| A1 electrical / uniqueness | implemented | Abstracts and Introduction. |
| A2 direct question | implemented | "We ask which features... follow from..., and where additional biophysics is required." |
| A3 notation | partly implemented | r for the rate in the coupling equations; E vs ε distinguished; H_s / H_c; ℓ for the space constant; 𝓕 for the SL forcing; ℳ[y]; δ defined; table rows added. Eigenvalue λ± and coupling λ still share a glyph. |
| A4 human/rodent numbers | retained with sources | Chain E → λ_f E → ε stated with citations; no scenario table. |
| A5 ε1, ε2 and m | implemented | Two-tone derivation first; m belongs to the surrogate only. |
| A6 "built to decide" | implemented | Conditional statement. |
| A7 transduction section opener | implemented | Plain statement first; order (amplitude scaling, harmonics, spatial) retained. |
| A8 acronyms | implemented | AM, LFP, tACS, SNIC, RF, PAC, PLV defined at first use. |
| A9 PEIX | implemented | Conditional role; model-dependent relation to efficacy. |
| A10 "We doubt" | implemented | Replaced by the scope statement. |
| A11 budget language | implemented | Heading and metaphors replaced. |
| A12 conclusion "why?" | implemented | Conclusion rewritten (Giulio's text). |

## K — items from the sigmoid/QIF note

| ID | Status | Note |
|---|---|---|
| K01 replace the coefficient globally | qualified, implemented | σ'' kept for JR; dynamic source for NMM2; no global substitution. |
| K02 remove the sign flip | qualified, implemented | Removed from headline predictions and the deck; retained as a JR-specific result and model comparison. |
| K03 redo the amplitude estimate | implemented | Bound restricted to the memoryless comparator (appendix). |
| K04 Fig. 6(a) reinterpretation | implemented | Described as a check of the memoryless law. |
| K05 lead the kHz argument with NMM2 | partly | sec:dynamic states the fast-carrier regime; actual kHz PING runs not added (perturbative check at 1 and 2 kHz instead). |
| K06 recruitment curvature | not imported | The note's integration-by-parts identity was not added to the paper. |
| K07 abstract/Introduction | implemented | Model-specific, no compartment identified. |
| K08 notation and m | implemented | See A3, A5. |
| K09 transduction section | implemented | See A7. |
| K10 register | partly | Self-grading and defensive sentences in the revised sections removed; a systematic em-dash sweep of untouched paragraphs remains (see readability review). |
| K11 acronyms | implemented | MRG remains undefined in the Introduction (not touched). |
| K12 PEIX | implemented | See A9. |
| K13 100 vs 300 Hz | implemented | Crossover at the population's own frequency stated; no universal cortical crossover claimed. |
| K14 rodent regime | retained | Statement that mV polarizations leave the perturbative regime kept; no rectifier class inferred from species. |
| K15 decisive simulations | partly | Single-carrier DC crossover (analytic + simulated); PING carrier check (perturbative); state sweep of the full recurrent beat response not run. |

## Claims changed or removed

- Removed: "the firing-rate nonlinearity is a square-law detector" as a general statement; NMM2 as validation of the σ'' law; "no pinning needed because the quadratic coefficient is fixed"; the sign reversal as a headline biological prediction; "timing, not rate" and its order-of-magnitude figure; the per-neuron vector-strength claim; the finite-size Hopf offset; the retrospective ΔPLV exponent fit; the TMS inferences; "two orders below 1/ρ"; the identification of the steep-sigmoid limit with a linear envelope follower; the 0.5 Hz zero-drive capture width; the LaNMM as physical grounding of kHz access.
- Narrowed: carrier independence at fixed polarization (polarization = carrier-frequency voltage excursion in the dynamic model); the tACS-shares-the-amplifier cancellation (conditional on matched input, observable and state); the LaNMM results (appendix extension at low carriers); the 0.3479 ceiling (memoryless comparator only); "supported" → "qualitatively consistent" in the predictions table.
- Added: sec:dynamic (crossover, fast-carrier source, Fig. crossover); App. bound (with the step-detector optimum); signed LaNMM maps; converged QIF metrics with PPC; field-inclusive JR rate read-out; Hopf at 1.110.

## Not done in this revision

- Systematic em-dash and word-tic sweep of paragraphs not otherwise revised.
- Notation collisions λ± / λ, m (depth) / m←n index, p (input) / p (exponent, now gone) — only p resolved by removal.
- Phase-based capture test for the LaNMM tongues; kHz PING time-domain runs; a state sweep of the full recurrent beat response; a scenario table of field couplings.
- Co-author confirmations (affiliations, funding lines, CRediT, AI-tool versions) — unchanged TODOs in the source.
