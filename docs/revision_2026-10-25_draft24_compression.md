# Draft24 — prose consolidation and figure repairs

Giulio approved a content-preserving compression pass and the figure repairs on
October 25. The editing baseline is `ac20693` (draft23 science at `3eceb94`);
the recorded reading baseline remains draft20, `e20c047`. The JNE article and
supplement are the working editions. The canonical TN artifacts remain untouched.

## Prose checkpoint

The first pass removes repeated explanations from Theory and repeated setup
from Methods and Results. The Introduction, Discussion, Conclusion, abstract,
figure captions, model appendix, and efficiency derivation remain unchanged.
The full PING system remains in Methods. Six glossary rows used only in
supplementary derivations are retained verbatim in the supplement and full TN,
but omitted from the article's notation table. All article symbols remain.

| Section | Draft23 | First draft24 pass | Reduction |
|---|---:|---:|---:|
| Introduction | 688 | 688 | 0 |
| Theory | 4,200 | 3,179 | 1,021 |
| Methods | 1,960 | 1,695 | 265 |
| Results | 3,392 | 3,137 | 255 |
| Discussion | 1,460 | 1,460 | 0 |
| Conclusion | 224 | 224 | 0 |
| Article appendices | 1,547 | 1,497 | 50 |
| Total | 13,471 | 11,880 | 1,591 |

`code/count_jne_words.py` reproduces these counts and includes the ordinary
table bodies omitted by the previous procedure. Mathematical tokens, abstract,
references, front matter, and declarations are excluded. The unchanged abstract
adds 299 words; the first-pass article plus abstract is therefore 12,179 under
this convention. The count alone is not a claim of meeting a publisher's limit.
The first article build has 39 pages, down from 41; the supplement has 31.
Final pagination awaits the figure repairs.

The shortened Theory retains the expansion and steady/beat sources, the
superficial/deep worked example, the current-product invariance conditions,
the multicompartment extension, harmonic signatures, the scalar subharmonic
proof and its exclusions, all amplitude-matching conventions, the near-Hopf
law, access estimates and evidence table, PEIX, and the MPR crossover.
Methods retains waveforms, observables, full models, settings, numerical
criteria, and interpretation limits. Results retain all numerical outcomes;
their protocols are stated more briefly where Methods already explains them.
The paragraph replacements are archived in `notes/2026-10-25_kaiti/` for
comparison, with subsequent wording fixes visible in Git.

## Checks at the prose checkpoint

The automated retention check verifies all 131 baseline labels and 67 citation
keys, and 32 labeled equation bodies unchanged except for whitespace and
sentence punctuation. The abstract, model appendix, efficiency derivation,
original QIF solver, and FEM numeric inputs are byte-identical. Article and
supplement build without errors, undefined/multiple references, or overfull
boxes; printed text has no unresolved references. The notation routing retains
the supplement-only rows, and the annotated draft20 hash is unchanged.
The mechanical prose checker reports no findings. These checks precede the
independent scientific/readability review and final visual inspection.

## Figure repairs and numerical check

Klaus prepares candidate repairs under `notes/2026-10-25_klaus/figrepair/`;
Kaiti inspects and integrates them. The defect list is in
`notes/2026-10-25_klaus/figure_check.md`. Its supplementary figure numbers
refer to appearance order. The manuscript retains historical S labels:
in particular, the third displayed supplementary figure, `fig_khz_direct`,
is Figure S9, not S3. File names are the integration keys.

All panels and data are retained. Legend/inset collisions, adjacent colorbar
numbers, supplementary type size, and wording receive local repairs. The
slow-access high-frequency upturn in Figure S9 receives a bounded numerical
check before its cause is described. No further theta-neuron run is authorized
or queued. Final figure, reference, and fidelity checks remain pending here.

The release hold and local push guard remain active. No public push, submission
tag, deposit, or coauthor circulation is part of this revision.


## Integrated revision

Klaus's independent prose review (`6d44ae6`,
`notes/2026-10-25_klaus/draft24_prose_fidelity.md`) found the science preserved
and proposed local corrections. They are applied: the cable comparison points
to the figure that contains it; the assumed-access simulation is described as
a consequence, not physiological validation; the Brunel citation is attached
to circuit resonance without an intrinsic cellular resonance. Explanatory
clauses restore the fixed-curvature inference, weak-drive scope, envelope-following
assumption, negative JR curvature, purpose of the spiking comparison, and
motivation for PEIX. An unused transduction symbol and ambiguous antecedents
were removed. The MPR equations are called population equations because their
input may include recurrence.

The final count is 11,958 before the unchanged 299-word abstract, against
13,471 in draft23: 1,513 words removed (11.2%). The count including the abstract
is 12,257. This is a measured reduction, not a claim of strict compliance with
the journal's normal length. The article is 40 pages; the supplement is 31.
The first prose-only build was one page shorter before the explanatory
restorations and the separate raster phase-fold panels.

Thirteen plotted figures receive local changes, plus the LaNMM schematic's
panel-letter overlay. Most follow Klaus's candidates (`4132c50`). Further
inspection led to separate phase-fold axes in Figures 13 and 14, preserving
all raster data; shorter legends and curve annotations; and shorter laminar
colorbar labels with fixed layout after text sizing. The captions define the
retained power-change observable and phase-fold normalization. Figure data
and numerical caches remain unchanged except for the corrected settling
interval in the supplementary kHz sweep described below.

### Settling correction in Figure S9

The original six-second settling interval leaves a field-free oscillation
of 7.73e-6 mV at the lock-in frequency. It interferes with the weak slow-access
response and produces the high-frequency dip and upturn. With twelve seconds
of settling, the slow-access response at 1.17, 1.76, 2.65 and 4 kHz becomes
4.43e-5, 1.95e-5, 8.61e-6 and 3.79e-6 mV, respectively. The direct and fast
routes change by less than 0.1%. No quoted manuscript value uses the corrected
slow-access points. Supplementary Methods now states the settling and
measurement windows explicitly.

The diagnostic uses the same solver and readout, and its timestep-halving
comparison changes the affected amplitudes by less than 0.2% without removing
the upturn. A separate run uses six seconds of field-off pre-equilibration
followed by six seconds with the field on; it agrees with the twelve-second
settling result. This is a pre-equilibrated start, not exact fixed-point
initialization. These descriptions qualify the shorthand in Klaus's candidate
README. The source and cached diagnostic are in
`notes/2026-10-25_klaus/figrepair/diag/khz_direct_upturn_diag.*`.

### Review artifacts

The reading baseline remains draft20 (`e20c047`); an additional redline compares
with the immediately preceding draft23 (`ac20693`). The redline builder gives
the curvature figure its own float-page placement because deleted prose made
an adjacent float stack overflow by 3.9 points. This affects review layout only.
Final checks and delivery are recorded below.


## Closure and delivery

Klaus's final bounded integration check passed at `322f396`
(`notes/2026-10-25_klaus/draft24_final_check.md`). It confirms the prose
restorations, figure layout, captions, and diagnostic qualifications.
The article and supplement build without errors, undefined or duplicate
references, or overfull boxes. The isolated full-TN routing build passes,
with the pre-existing canonical TN PDF and bibliography left untouched.
Both redlines pass the same reference and overflow checks (53 pages against
draft20, 43 against draft23). All 131 labels, 67 citation keys and 32 labeled
equations remain; the full PING system and protected numerical inputs are
unchanged. The QIF plotting audit confirms identical raster and phase-fold
calculations. Modified Python files pass syntax compilation. The prose
checker is clean apart from its known Markdown table-separator false positive.

All 27 figures were viewed individually, and the revised figures were also
checked in the compiled pages. The figure record and artifact hashes are in
`notes/2026-10-25_kaiti/figure_review.md` and `artifact_manifest.json`.

The article, supplement, both redlines, and storyline were copied to
`/Users/giulio/Downloads/TN0484_draft24_2026-10-25/`, verified byte-for-byte,
and the containing folder was opened. Its README identifies the two redline
baselines and the count convention. No public push or deposit was performed.
