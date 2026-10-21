# Journal prose revision proposal

October 21, 2026. Joint review by Kaiti and Klaus; no manuscript changes applied.
This decision summary reconciles
`../notes/2026-10-21_kaiti/prose_structure_review.md` (`ac246f4`) and
`../notes/2026-10-21_klaus/prose_joint_plan.md` (`6609258`). The itemized R/P/C
verdicts and retention requirements remain in those notes.

## Shared verdict

The article is generally clear sentence by sentence, but its repeated explanations
and procedural detail interrupt the argument. Repetition is not minimal, and some
material belongs outside the main narrative. We recommend a content-preserving
first pass, followed by a new count before considering further shortening.

Introduction through Conclusion currently contains 13,332 text words, 227 heading
words, and 1,418 caption/other words: 14,977 excluding mathematical tokens. This
excludes the abstract, declarations, references, and notation appendix. JNE's normal
research-paper length is 12,000 words; longer papers can be considered when their
content justifies the length. The publisher does not specify the counting treatment
of captions and mathematical tokens on these pages.
Sources: [article types](https://publishingsupport.iopscience.iop.org/journals/journal-of-neural-engineering/about-journal-neural-engineering/)
and [article-length guidance](https://publishingsupport.iopscience.iop.org/journals/journal-of-neural-engineering/),
checked October 21.

## Agreed first pass, subject to Giulio's approval

Move the detailed FEM construction and solver procedures, numerical run catalogue,
sensitivity tables, and AM/two-tone comparison values to the supplement. Keep the
model assumptions, definitions of the measured quantities, convergence summaries,
and the qualifications needed to interpret each result in the article.

Consolidate repeated explanations of access, harmonic tests, recurrent gain, and
amplitude matching. Keep one general receiver equation, with a short spatial
explanation where the dose maps are introduced. Replace the FEM numerical catalogue
with a table. Give the tDCS/tACS comparison its own Theory subsection, preserving
the 2–5% result and its equal-per-carrier polarization convention.

Move the full harmonic series and auxiliary mixture inversion, envelope-mean proof,
and orientation-average derivation out of the narrative. Keep the harmonic-test
predictions, the one-line quadratic subharmonic identity with its assumptions, and
the consequences of orientation averaging. Retain the main notation appendix,
access evidence table, core MPR equations, and static-rate curve.

The slow-synapse display can be shortened by retaining the relation
`r(t) ≈ F(Q(t))/τ_m` inline and stating both time-scale conditions locally: population
relaxation must be fast relative to synaptic variation for the static-rate
reduction, and fast relative to the carrier to apply that map directly to TI.
The already defined second-order synaptic operator need not be displayed again
there. This accepts Klaus's compression while preserving the model connection.

Keep short cutoff qualifications beside the spiking result and caption. Shorten
the prediction table's evidence cells to observations, interpretive limits, and
citations; retain explicit statements where biological tests are still absent.
Keep brief definitions of the observables at first use, with detailed vocabulary
and metrics in the supplement.

## Placement choices for Giulio

| Choice | Joint recommendation or remaining difference |
|---|---|
| Violante discussion | Remove repeated displacement magnitudes and ratio algebra while preserving the mean-map ordering, biological interpretation, and qualifications. Shortening this approved block was explicitly deferred on October 20. |
| Full PING equations | Optionally move the full system from Methods to an article appendix, keeping E/I coupling and forcing definitions in Methods. This shortens the narrative, not the article word count. |
| Vieira footnote | Move the detailed experimental numbers to the supplement; retain the unmatched-polarization/readout qualification beside the comparison. |
| Article appendices and supplement | Keep compact model specifications and the crossover derivation needed for the dynamic detector in article appendices. Cross-reference equations retained in Theory rather than duplicating them. Organize the supplementary file by topic. Keep a brief pointer to the low-carrier laminar extension, with its full study supplementary. |
| Efficiency bound | Kaiti recommends an article appendix containing a compact argument for the 0.348 bound if that quantitative claim remains. Klaus favors the derivation in the supplement because the bound supports a Discussion comparison. This is the remaining disagreement. |
| Length target | Complete the approved first pass and recount before choosing further cuts or justifying a longer article. Neither reviewer promises a numerical saving from the overlapping proposal list. |

IOP distinguishes article appendices from separate supplementary files: integral
material belongs in the article, while supplementary files are outside its Version
of Record and are not reviewed by default. This is why the destination of essential
supporting calculations matters. [IOP supplementary-material guidance](https://publishingsupport.iopscience.iop.org/questions/supplementary-material-and-data-in-journal-articles/)

## Implementation after approval

Kaiti updates the storyline and shared source, then builds the journal article and
supplement, checks references and counts, and updates the current redline against
the unchanged draft20 baseline. Klaus checks fidelity against the retention list.
Edition routing preserves a single source for every block; no TN export or
publication is authorized by this review. No simulations or scientific results
are changed by the proposed pass.

The review and reconciliation are complete. Manuscript changes await Giulio's
decision on this concrete proposal, as requested.
