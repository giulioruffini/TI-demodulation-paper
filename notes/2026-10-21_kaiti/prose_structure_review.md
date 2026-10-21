# Journal prose and placement: Kaiti's independent review

October 21, 2026. Source reviewed at `6c0e23a`; journal manuscript unchanged.
This responds to every item in Klaus's
`notes/2026-10-21_klaus/prose_structure_review.md`. Verdicts below assess his
proposed action, not merely whether the passages share a topic. This is a proposal
for discussion with Klaus and Giulio, not authorization to relocate material.

## The article is readable but carries too much repeated explanation

The sentences generally read well. The remaining difficulty is cumulative: readers
repeatedly encounter the same distinction between access, source, and response,
interleaved with numerical procedures and qualifications. Shortening can improve
the argument, provided the assumptions remain beside the claims they qualify.
The prose checker reports no mechanical findings; it does not test this structural
problem.

Repetitions are not minimal. The largest opportunities are the access literature,
the harmonic-test explanation, waveform comparisons, and numerical protocols.
Some apparent repetitions do different work: an equation defines a model, a result
tests it, and a Discussion paragraph interprets its biological scope. Those should
be shortened according to their purpose, rather than reduced to one occurrence.

Some material belongs in the supplement. Electrode construction, numerical solver
settings, sensitivity tables, the full harmonic series, and auxiliary mixture
inversion can move while the main paper remains self-contained. The physical-time
QIF equations, the source/response distinction, the uniformity assumptions on the
DC restriction, and the amplitude convention behind 2–5% belong in the main paper.
So does a concise distinction between beat locking and phase capture.

## Current length and counting scope

The count below expands the shared model caption using
`code/build_jne_redline.py:expanded_source`, then selects Introduction through
Conclusion. It excludes the abstract, declarations, references, notation appendix,
and supplement. TeXcount mathematical-token counts are excluded. The raw report
and reproduction script are alongside this note.

| Section | Text | Headings | Captions and other outside text | Total |
|---|---:|---:|---:|---:|
| Introduction | 674 | 1 | 67 | 742 |
| Theory | 4,194 | 65 | 240 | 4,499 |
| Methods | 3,299 | 50 | 84 | 3,433 |
| Results | 2,441 | 76 | 892 | 3,409 |
| Discussion | 2,522 | 34 | 135 | 2,691 |
| Conclusion | 202 | 1 | 0 | 203 |
| Total | 13,332 | 227 | 1,418 | 14,977 |

JNE normally permits up to 12,000 words for a research paper
([article types](https://publishingsupport.iopscience.iop.org/journals/journal-of-neural-engineering/about-journal-neural-engineering/),
checked October 21). The page does not specify the counting treatment of captions
or mathematics. Its general guidance allows longer articles when the scientific
content justifies them
([article length](https://publishingsupport.iopscience.iop.org/journals/journal-of-neural-engineering/)).
The 44 manuscript pages are not equivalent to 44 typeset journal pages.

Klaus's older count understates the current text after today's comparison. His R
and P savings overlap: R6/P4, R12/P7, and R13/P3 include the same material, for
example. A 3,500-word saving is an editing target, not a verified consequence of
the list. Recount after an approved first pass before choosing further cuts.

## Repetition proposals

| Item | Verdict | Proposed treatment |
|---|---|---|
| R1: repeated stages | Modify | Keep the Introduction's definitions and the Conclusion's synthesis. Remove the repeated stage sentence in the Discussion opener, retaining its comparison with prior work. Shorten the Introduction's final roadmap. The Results opener also distinguishes the spiking-network question; either retain that transition or incorporate it in the relevant result. The prediction table performs a separate experimental function. |
| R2: access calibration | Modify | Consolidate the literature and repeated calibration language in 2.7/5.1. Keep a short assumption in the Introduction, the effective-input qualification beside the AIS explanation in 2.2, and the measured/assumed distinction beside Table 2. Table 2 plus the Conclusion alone leaves the model's entry point insufficiently qualified. |
| R3: time constants | Modify | Let Table 2 hold the literature catalogue. Retain the illustrative contrast between somatic and assumed fast access in 2.7, and the actual 2 kHz result in 4.2. The table does not currently contain all attenuation factors, so moving them requires an explicit destination. |
| R4: two receiver equations | Modify | Use one numbered general receiver equation in 2.6, while retaining a short spatial statement in 2.3 that names local curvature and susceptibility. The equations express the same factorization at different levels, but one exposes spatial dependence and the other field access. Preserve signed projections in 2.3; do not move that definition with the amplifier. |
| R5: TI/tACS amplifier | Agree | Keep the quantitative test in 4.7 and the concise conclusion. Reduce 5.3 to its implications and scope: matched source and state, finite-amplitude departures, and the comparison with previous work. |
| R6: harmonic tests | Modify | Give the detector law and gain correction once in Theory, implementation only in Methods, and the off-resonance example with the proposed experiment. Shorten the table's theoretical recap. Retain both amplitude scaling and harmonic ratio: neither alone identifies all three classes. |
| R7: waveform checks | Modify | Collect detailed AM/two-tone agreement values in a supplement table. Keep the main Methods' unequal steady-source and second-harmonic warning, identify the waveform in each figure, and retain a short result-specific statement where the waveform affects the conclusion. These checks concern different operating regimes and cannot be represented as one universal equivalence. |
| R8: FEM numbers | Modify | Give the full numerical comparison once in 4.4, preferably as a table. In 5.2 retain the mean-square increase versus beat/envelope decreases needed for the BOLD argument; remove repeated displacement magnitudes and relocate the ratio algebra if approved. The current Conclusion and Table 3 repeat the qualitative result, not the quoted numerical catalogue. |
| R9: relative amplitudes | Modify | Make 2.5 the home of the matching conventions and retain its 2–5% result. In 5.4 use the calibrated-input budget and name its total-peak convention without repeating the derivation. The 0.348 bound uses that same convention, not a third matching convention. It answers a different question from the weak-JR estimate. |
| R10: no applied DC | Agree | Merge the two statements in 2.5 into one distinction between applied field, detected source, and circuit response. |
| R11: QIF cutoff | Disagree | Keep a short cutoff qualification beside the weak-drive result and in its caption. Move the numerical cutoff range from Methods to the existing supplement table, retaining a concise Methods statement and pointer. A reader of the figure should not infer quantitative convergence. |
| R12: MPR/PING equations | Disagree | Retain the two-variable physical-time MPR equations in Theory: they show the quadratic voltage mixer and explain the dynamic departure from a static sigmoid. The two-population PING equations specify a different level of the model. The supplement derives coefficients and supplies checks; it is not a third identical presentation of the same system. Compress repeated definitions instead. |
| R13: vocabulary | Modify | Remove the separate Methods subsection by incorporating brief definitions where the observables are introduced. Keep the full criteria and metrics in Appendix F. Main-text readers still need to know that frequency dominance and a rate fold do not establish phase capture or gamma-amplitude gating. |

## Placement proposals

| Item | Verdict | Main text retained; destination for details |
|---|---|---|
| P1: FEM procedure and sensitivities | Agree | Retain subject/montage, quasi-static conductivity assumption, current convention, fixed projection, ROI/reference definitions, degree matching, and focus definition. Move electrode recipe, solve/recovery settings, mesh counts, atlas/tissue/focus sensitivity specifications to a dedicated supplement section. Keep the result that displacement directions persist across the tested choices and that absolute contrast depends on orientation; put the numerical matrix in a supplement table. |
| P2: numerical steps and leakage | Modify | Move the per-run step/window catalogue and vectorized implementation detail. Retain integrator, convergence criterion, and a sentence explaining mean subtraction in the lock-in. The latter prevents confusion between a small generated beat and leakage from the much larger baseline. |
| P3: vocabulary | Modify | As R13. Moving the entire definition without a main-text replacement would make the later interpretation harder to follow. |
| P4: harmonic ladder and mixed family | Modify | Move the full Fourier series, higher harmonics, mixed-family inversion and its branch footnote. Retain the 1/5 second-harmonic ratio, the vanishing weak-quadratic ratio, amplitude laws, and network correction. A three-class statement alone is too compressed to support the proposed test. |
| P5: mean-map proof and direct comparison | Modify | Move the envelope-norm proof and derivation of orientation averages. Retain the one-line quadratic subharmonic identity, all uniformity assumptions, and the contrast with a beat product whose Laplacian has no fixed sign. Retain the outcome that orientation averaging can cancel the beat while preserving intensity. Give the tDCS/tACS comparison its own subsection. |
| P6: access prose and Table 2 | Modify | Keep Table 2 in the main paper and merge its duplicated literature discussion. Retain the field-versus-current distinction, fast-time assumption, point-versus-cable contrast, and rule that membrane access enters once. Three sentences would not carry those distinctions adequately. |
| P7: mean-field equations | Disagree | Keep the core MPR system and static limit in Theory. If the full PING system moves to Appendix B, retain its E/I coupling and forcing definitions in Methods. That is a separate optional relocation, not removal of the theoretical mechanism. |
| P8: bound and Vieira footnote | Modify | Keep a compact statement of the numerically estimated 0.348 supremum, its matched-peak memoryless class, and the exclusion of dynamic QIF. Detailed threshold shape/harmonics can accompany the existing derivation. Move Vieira's experimental numbers to the supplement only with the main comparison still stating that local polarizations and readouts were not matched. |
| P9: strong-field QIF discussion | Modify | Keep numerical threshold evidence in 4.9 and compress repeated explanation within that section. Section 5.3 contains no repeated numerical threshold catalogue: it connects the mechanism to strong-field experiments and limits physiological inference. Retain that interpretation in a shorter paragraph. |
| P10: evidence column | Modify | Shorten each cell to the observation plus the limit on its interpretation and a citation. Retain explicit statements where a prediction is untested or supported only by the present simulation. Bare citations would obscure those distinctions. |

## Local clarity proposals and additions

| Item | Verdict | Treatment |
|---|---|---|
| C1: spatial section's receiver paragraph | Modify | As R4: move the numbered general factorization but preserve the local physiological weighting needed to interpret a spatial dose map. |
| C2: E/I weight sentence | Modify | The two drive terms are already displayed in Eq. 22. Delete the prose that repeats both rows; retain the definition of target/source indexing and the doubled inhibitory self-coupling. Adding another display would duplicate the existing one. |
| C3: FEM numerical paragraph | Agree | Replace the numerical catalogue with a compact table comparing map means, target/reference contrast, and focus displacement under 1:1 and 1:3. Define raw versus degree-matched statistics in its caption. Replace the prose rather than adding a second presentation. |
| C4: Violante interpretation | Modify | Preserve the biological comparison and its qualifications. Remove duplicated geometric displacement values; keep the mean-map ordering needed for the inference. This needs Giulio's decision because shortening this block was explicitly deferred on October 20. |

The remaining opportunities are more specific than a general style pass:

* The final Introduction paragraph combines model scope, the static/dynamic
  distinction, related endogenous coupling, and experimental tests. Keep a concise
  model progression there; let Table 3 and the Conclusion carry the test programme.
* Section 3.4 first describes a continuation diagram and later a field-free
  min/max diagram obtained from initialized runs. Specify which output each
  procedure supplies; the common name makes the method ambiguous.
* Section 3.3 calls gray matter outside the ROI a cortical-reference proxy while
  explicitly including deep gray matter. Use the literal reference definition
  throughout. A cortex-only contrast is a proposed test, not a computed result.
* Section 4.9 repeats the strong-field shift and threshold within its own text.
  Retain the refined estimate and its comparison with the threshold once. The
  detailed single-cell phase statistics can move with the numerical checks if the
  main result retains the observation that population modulation arises from weak
  individual phase biases.
* In 2.9, adjacent sentences both say the fast DC response follows the positive
  slope. Merge them around the physical explanation through voltage squaring.
* Keep the main notation appendix: Giulio explicitly asked for it in the reading
  copy on October 6. Its relocation is not an available space-saving default.

## Relation to the October 20 decisions

The October 20 pass already moved the general NMM1 operator, exact MPR mixing
coefficients and crossover exponents, JR sweep settings, detailed QIF cutoff
checks, PING endpoint stability protocol, and detailed bifurcation-caption text.
These cannot be counted again as new relocations. It also established one Methods
home for the AM-surrogate protocol and kept harmonic-filtering examples with
experimental tests.

The physical-time MPR system, spatial examples, harmonic ladder, mean-map proofs,
and access evidence table were deliberately retained in that revision and its
storyline. They can be reconsidered, but that retention is not evidence that
Giulio explicitly rejected every possible subsequent move. The documented
exception is shortening the approved Violante discussion, which was explicitly
left unapplied. Vieira's details were retained as an attached footnote; moving
them is a new placement choice. See
`docs/revision_2026-10-20_draft21_legibility.md` and
`planning/tn0484_storyline.tex`.

## Proposed first pass for Giulio's decision

Approve a content-preserving pass comprising the FEM/numerical procedure moves,
the auxiliary harmonic derivations, the envelope-mean proof, and the repeated
explanations identified above, with the retained content specified in the tables.
Keep the primary results, model bridge, main notation, and local qualifications.
Treat the Violante block and relocation of the full PING system as separate
choices. Update the storyline before implementing any approved structural change,
then rebuild the journal and supplement, check references and claim fidelity,
and recount. No word-saving total is promised before that pass.

This review changes no source, abstract, figure, numerical result, or PDF. It is
an editorial assessment, not a new scientific or numerical validation.
