# Submission-readiness review — v0.14.6

**Draft6 update (October 5).** Both-step checks at cutoffs 200 and 400 are verified.
The higher-cutoff depths span 0.121–0.141, and the cutoff-400 overshoot survives
time-step refinement. The requested R7 diagnostics are complete at the stated
claim scope; quantitative cutoff convergence remains a limitation, not an asserted
result. See [the draft6 record](docs/revision_2026-10-05_v0150draft6.md).


**Draft5 update (October 5).** Cutoff checks locate sensitivity of the weak-drive
spiking depth: 0.093, 0.127, and 0.139 at cutoffs 100, 200, and 400, versus the
mean-field 0.128. Agreement at 200 is not a joint convergence test. The longer
carrier window suppresses the apparent 55 Hz response below 0.0001 while TI's
persists near 0.31, supporting the leakage interpretation. Original rasters
remain. See [the draft5 record](docs/revision_2026-10-05_v0150draft5.md).


**Draft4 update (October 5).** The R7 follow-ups distinguish a stable beat response
at amplitude 10 from induced gamma at amplitude 35. Figure S13 adds both regimes
and equal-RMS mean-field carrier controls without replacing Figure 10 or S12.
The controls reproduce the rectified shift and gamma induction under a single
carrier. A full-period variational calculation establishes stability of the S10
endpoint (largest multiplier 0.034); the DC-only screen is not its stability test.
The amplitude-10 spiking depth remains below the ideal mean field and is reported
with that limitation. See [the draft4 record](docs/revision_2026-10-05_v0150draft4.md).


**Draft3 update (October 5).** Klaus's raster analysis exposed a further R7
classification error: a field-free stable QIF state does not remain a purely
beat-forced state at the published amplitude. The text and captions now distinguish
dominant off-beat gamma from the smaller beat-locked component and identify these
as finite-amplitude illustrations. The weak-input calculation remains separate.
See [the draft3 record](docs/revision_2026-10-05_v0150draft3.md). Klaus's E-only
stability calculation and an independent reproduction support the rectified-DC
explanation. At amplitude 10 the mean field stays forced. Complementary spiking
runs and equal-RMS carrier controls are proposed; the current draft retains the
corrected amplitude-35 examples as evidence of a change in operating regime.

**Draft2 update (October 4).** Klaus verified the R6 integration; the maximum P1
window difference is now rounded to 9.6 percentage points. The reconstructed kHz
producer reproduces all seven stored arrays bit for bit in independent runs, and
both runner modes use the intended data. R12's missing-producer gap is closed.
See [the draft2 record](docs/revision_2026-10-04_v0150draft2.md). The earlier
updates below describe their reviewed versions; author approval and declarations
remain open.

**October 4 repair update.** The findings below are the historical review of
v0.14.6. They are addressed at the revised claim level in **v0.15.0-draft1**;
see [the revision record](docs/revision_2026-10-04_v0150draft1.md) and
[the R6 integration note](docs/r6_integration_2026-10-04.md). R6's old percentages
are withdrawn and replaced by defined, preserved calculations. R12's targeted
reproduction repairs pass; the kHz two-tone producer remains unavailable and that
illustration is explicitly replot-only. Author declarations, approval, and release
alignment remain open. This update does not turn the original read-only review
into a record of tests it did not perform.

---

Reviewed October 4, 2026, at manuscript commit `9bc574c` on `two-tone-validation`.
This record does not change the manuscript version.

**Verdict: not yet ready for submission.** The effective weak-field mixing argument
survives this review. The remaining work is to align several claims with their
evidence, repair the reproduction package, and obtain the author approvals and
declarations. A new Hodgkin–Huxley study, periaxonal circuit model, or biological
experiment is not a prerequisite. The pending section-placement decisions do not
prevent the scientific corrections below.

This was a bounded readiness review, with independent checks of claims, numerical
evidence, and recent citations. It was not a complete rederivation, a fresh execution
of every simulation, or a source-by-source audit of all 59 cited works. No fatal
defect was identified within that scope. Line numbers below refer to
`TN0484_envelope_demodulation.tex` at the reviewed commit.

## Scientific claims and reproducibility

| Severity | Item | Evidence and consequence | Required disposition |
|---|---|---|---|
| MAJOR | R4: fixed detection does not mean only damping changes | Lines 1368–1373 say that only damping changes and that amplification depends only on distance to criticality. An independent analytic JR Jacobian calculation, with the operating point pinned, shows that coupling also changes the mode frequency and its input–output residue. | Keep the fixed-curvature result and the leading near-Hopf scaling. Describe the changing network transfer and qualify the observed agreement between parameter paths. The PING claim of source invariance over a coupling sweep (1400–1405) also needs evidence across that sweep; the reported four-state response comparison does not establish it. |
| MAJOR | R7: frequency dominance and rate modulation do not establish capture or gamma-amplitude gating | The qualification at 2168–2172 is correct, but stronger claims remain at 1199–1204, 1379–1384, 1443–1454, 2081–2090, and 2173–2180, and in captions. A forced component can dominate the spectrum while the autonomous rhythm persists. Rate folding and sidebands do not uniquely identify modulation of the autonomous gamma amplitude. An 11 Hz detuning alone does not locate an Arnold-tongue boundary. | Use the measured quantities consistently: frequency dominance, beat-locked rate, coexisting rhythms, and intermodulation sidebands. If retaining phase capture or phase–amplitude coupling as demonstrated results, add the corresponding phase-drift or modal-amplitude evidence. Narrowing the interpretation requires no new experiment. |
| MAJOR | R6: the LaNMM 7%/25% comparison is not supported by the supplied calculation | Lines 2107–2111 and 2274–2276 report phase-sensitive carrier comparisons. The committed P1/P2 caches contain band-power changes and dominant frequencies, with no lock-in array. `lanmm_field_tongues.py` defines `lockin` but does not call it; `make_lanmm_field_figs.py` plots the band-power arrays. | Recover or compute and preserve the phase-sensitive comparison with its analysis window and normalization, or revise the numerical claims to match the available evidence. This is a provenance gap, not evidence that the numbers are false. Also reconcile “falling only to 25%” with the caption's “median 25%.” |
| MAJOR | R2: an open-loop control is presented as validation of recurrent sweeps | Lines 521–523 and the caption at 1280–1283 say the comparison verifies or licenses the dense sweeps. The implemented comparison is an open-loop sigmoid at one operating point. The text at 1291–1296 already states the correct limitation: different DC terms may change the recurrent operating state near the Hopf. | Propagate that qualification to Theory and the caption, and identify the recurrent sweeps as AM-surrogate results. A recurrent two-tone comparison is needed only if claiming their quantitative equivalence beyond the established scope. |
| MAJOR | R12: the one-command reproduction and scratch-output claims exceed the implementation | `run_all.py --only fig_resonance` selects a data producer without its plotting step; `--only fig_concept` misses its uncommitted data dependency. `make_lanmm_field_figs.py` and `khz_direct.py` contain fixed output paths despite the README's scratch-output guarantee. The producer of `khz_twotone.npz` is absent. Some plot generators still label Fourier amplitudes as power. | Resolve dependencies before filtering, honor `TN_FIGDIR` throughout, correct generator labels, and restore the missing producer or state the limit accurately. Check the repaired entry points from a clean checkout. Align the public archive and availability statement with the eventual submitted version; release remains held. |
| MINOR | R9: the finite-damping peak formula uses the wrong frequency convention | The caption at 1213 uses the standard undamped-frequency expression while defining the frequency through the imaginary part of the eigenvalue. The near-Hopf approximation in 750–768 protects the central scaling result. | Correct or qualify the caption formula. Use the full input–output resolvent for an exact network peak; retain the leading inverse-damping scaling when the mode has nonzero input and output projections. |
| MINOR | R3/R5 and numerical wording | The magnitude-only sum at 425–432 assumes aligned phases, although the dominant-entry-point scope at 441–446 limits its consequence. “Timing-not-rate” overstates the QIF result: the cached mean-rate increases are 10.535% and 7.617%. Whole-cycle windows remove an incomplete-cycle contribution, not all finite-window estimator bias. | Qualify the sum as phase aligned, use “larger modulation than mean-rate change” where appropriate, round the QIF changes to about 8–11%, and narrow the finite-window statement. These do not require a new model. |
| MINOR | Citation and build details | Cifra supports the distinction between direct field–protein effects and membrane polarization, but describes protocol-dependent thresholds, not a universal lower bound. Plovie's first name is Tom, not Thomas. The existing logs have bibliography month-macro and shared citation-label warnings. | Replace the categorical “require” formulation by a reported-field-range statement, specifying the applied extracellular field in the stimulation comparison. Correct Plovie's name and clear or document the remaining build warnings. |

## The matrix check preserves the near-Hopf result

With the JR operating point fixed at 8.30 mV, the analytic Jacobian gives:

| Coupling C | Damping (s⁻¹) | Mode frequency (Hz) | Magnitude of input–output residue |
|---:|---:|---:|---:|
| 110 | 10.739053 | 8.991078 | 43.253904 |
| 120 | 6.716898 | 9.908486 | 47.769608 |
| 130 | 2.642620 | 10.710105 | 51.590793 |

The input is a generated rate entering the pyramidal synapse; the readout is the
pyramidal potential difference. The residue includes these fixed input and output
choices. Both frequency and residue change while the detector curvature remains
fixed. Near a simple Hopf bifurcation, a finite nonzero residue still gives the
leading inverse-damping growth. It does not make the full gain a function of damping
alone over a finite parameter interval.

For eigenvalues −γ ± iω₀, a constant-numerator two-pole response has squared
denominator `(γ² + ω₀² − Ω²)² + 4γ²Ω²`; its positive-frequency peak is at
`Ω² = ω₀² − γ²` when that quantity is positive. The caption's
`ω₀² − 2γ²` instead treats ω₀ as the undamped natural frequency. The JR network
also has a frequency-dependent numerator. These are finite-damping corrections,
not a refutation of the leading inverse-damping result.

The check is preserved in `docs/review_v0146_jr_matrix.py`. It evaluates the analytic
Jacobian and the linear resolvent, reads an existing cache, and integrates no ODEs:

```sh
.venv/bin/python -B docs/review_v0146_jr_matrix.py
```

## The weak-field framing and Klaus's revisions stand

The effective second-order coefficient has the correct memoryless limit,
χ⁽²⁾ = Σ″/2 under the manuscript's cosine-amplitude convention. Smooth cellular
processes can contribute to this coefficient; their memory remains in its frequency
dependence, and symmetry or cancellation can make it vanish. QIF supplies the
quadratic structure without fixing a universal biological coefficient. The
Lorentzian-average interpretation of F(Q), its recruitment and single-cell curvature
contributions, and the distinction between mixing and subsequent amplification are
consistent with that framing.

Klaus's restored efficiency consequence is appropriate for matched input coupling,
observable, and operating state. His gate-filter sentence correctly states both
conditions: do not duplicate included dynamics, and justify any additional filter
for kinetics that the chosen detector does not contain. It does not require adding
a sodium-channel model to this paper. The restored cellular-mixing/circuit-gain
explanation and the χ⁽²⁾ notation row should be retained. R10's weak-input efficiency
trend is repaired.

The Plovie citation distinguishes HH/FH from the tested leaky, exponential, and
adaptive-exponential integrate-and-fire models; it does not test QIF. The direct
source is the [published article record and abstract](https://biblio.ugent.be/publication/01JZAPVAS03438EK6DB5644CKK).
The [Cifra review](https://pubs.rsc.org/en/content/articlehtml/2026/cs/d3cs00244f)
supports the scope distinction, subject to the wording correction above.

## Submission requirements remain open in the local record

The manuscript comments at 1764–1803 still mark funding for Grossman, Canals, and
Mirasso, remaining competing-interest declarations, and author-role confirmation as
pending. The all-authors-approval sentence is commented out. Obtain approval of the
actual submission version from every author, including Grossman; the current record
does not establish it. This is required by [IOP's ethical policy](https://publishingsupport.iopscience.iop.org/ethical-policy-journals/).
Record the AI-tool versions actually used, as required by
[IOP's generative-AI policy](https://publishingsupport.iopscience.iop.org/questions/generative-ai-tools/).
Do not guess missing versions or declarations.

The structured JNE abstract is below the normal 300-word limit. A fresh TeX count
puts the main article, captions, abstract, and declarations at approximately 11,400
words, excluding the bibliography and supplement. That is below JNE's normal
12,000-word guidance; 31 locally typeset pages is not itself a submission defect.
See [JNE's journal guidance](https://publishingsupport.iopscience.iop.org/journals/journal-of-neural-engineering/about-journal-neural-engineering/)
and [IOP's article-format guidance](https://publishingsupport.iopscience.iop.org/questions/structure-and-format-of-your-journal-article/).

The three placement choices remain editorial decisions. The previous recommendations
stand: move the transduction-class discussion after Results while retaining carrier
access in Theory, place the LaNMM methods with their appendix results, and consider
promoting S11. None is needed to repair the scientific statements above. No content
has been cut or reordered in this review.

## Verification scope and release state

The 47-page TN, 31-page JNE article, 18-page supplement, and v0.14.5-to-v0.14.6
redline were inspected as existing artifacts. Selected changed and claim-bearing
pages were rendered and visually checked, including the final χ⁽²⁾ table row.
Existing logs show no LaTeX errors, undefined references or citations, or overfull
boxes; the warnings noted above remain. Builds were not rerun in this review.

Read-only checks reproduced the open-loop surrogate ratios (0.999997 at 0.02 mV and
0.988033 at 1 mV), JR rate-modulation numbers, QIF rate/modulation summaries, and the
LaNMM signed band-power fractions. The latter agree with the reported rounded
percentages: P1 95%/97%, P2 44%/31%. These checks do not validate the missing
phase-sensitive 7%/25% comparison. A time-step/threshold check exists in an ignored
QIF run log; preserve its verification record with the release. A full clean-checkout
reproduction and general initial-condition/population-size convergence audit were
not performed here; the latter is not introduced as a new prerequisite for the
paper's illustrative scope.

The manuscript, figures, simulation code, and generated PDFs are unchanged by this
review. GitHub push, Calliope/Zenodo release, Overleaf synchronization, and coauthor
email remain held. The repair pass should precede final author approval and release.
