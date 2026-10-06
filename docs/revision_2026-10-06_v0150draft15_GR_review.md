# TN0484 draft15: organization and annotated-review revision

October 6, 2026. Editing baseline `56070fa`; reading baseline draft13,
`c620335`. Giulio's revision brief was relayed by Klaus at 18:30 and checked
against the actual annotated PDF. The annotation-by-annotation record is
`gr_review_annotation_resolution_2026-10-06.md`.

The Theory now separates detector laws and harmonics (2.4), envelope oscillations
and spatial weighting (2.5), and the mean shift (2.6). The comparison table sits
beside the envelope argument; the two mean-map proofs follow in the next
subsection. The equal-RMS statement covers a dynamic detector at second order
when the DC coefficient is effectively constant across the carrier interval.
No new focality theorem or neural simulation was added.

JR Results are followed by the NMM2 mean field and its coupling sweep, then the
QIF network. Predictions and tests belong to Discussion 5.1. The QIF section
leads with the distinction between modulating a stable state and inducing gamma.
Its cutoff diagnostics are retained in Methods, and its Results still state
that quantitative finite-network convergence is unestablished. The Vieira,
illustrative-budget, and detector-bound paragraphs now state their consequences
for this weak-input account.

Figure 2 is the approved model schematic from `fig-models-ti`, corrected commit
`c7ce5e0` following the initial proposal `57bd255`. Its source and PDF are retained.
The caption defines the displayed filters, time constants, connectivity, current
coupling, total single-neuron input, and arrow colors. The shared notation table
includes the schematic's kernels and total-input symbol. The redline helper
expands this caption input so it appears in the fixed-baseline comparison.

The shared abstract uses “steady drive” for the generated DC source and states
the restriction in terms of its magnitude, under uniform conductivity, access,
and detection. The Introduction is unchanged. Existing carrier comparisons are
credited in Prediction 1; the proposed access-corrected test now states its
normalization and the need to control recurrent gain. The source locations and
DOIs are recorded in the audit.

## Length and retention

These counts use TeXcount text, headings, and captions, excluding math-token
counts (`-sum=1,1,1,0,0,0,0`). The older default `-sum` totals, which also count
math objects, are retained in `word_counts_draft15_GR_review.json`.

| Section | Before | After |
|---|---:|---:|
| Introduction | 973 | 973 |
| Theory | 4747 | 5113 |
| Methods | 2540 | 2699 |
| Results | 3799 | 3232 |
| Discussion | 1441 | 1960 |
| Conclusion | 230 | 230 |
| Total | 13730 | 14207 |

The QIF subsection including its two captions falls from 980 to 897 words.
The Results-to-Discussion relocation accounts for much of the section-level
change; it is not a deletion. The approved schematic and the requested
explanations increase the overall count. No claim of net shortening is made.

The source audit checks equation-body retention, all original labels and cited
keys, unchanged existing figure files and simulation caches, the unchanged
two-site example, and the two verbatim diagnostic relocations. Main figures are
renumbered by the insertion of Figure 2 and the approved grouping of model
results; Figure S1–S13 numbering and all equation numbers remain unchanged.
The carrier-control caption is the only existing caption with changed text.
The annotation record lists every deduplication; no substantive removal is
proposed in this pass.

## Validation and holds

Current page counts, the final abstract count, hashes, build diagnostics, visual
checks, and peer-review status are recorded in `validation_current.json`.
The JNE article and supplement are built from the same source; the combined TN
is a private validation build. No numerical rerun is needed because the model
code, cached data, and existing figures are unchanged. The storyline follows the
new order and the redline remains against `c620335`.

GitHub push, Calliope/Zenodo cut, Overleaf sync, and coauthor circulation remain
on hold. The revision addresses the annotated review; it is not a submission
or a claim that all author declarations are complete.
