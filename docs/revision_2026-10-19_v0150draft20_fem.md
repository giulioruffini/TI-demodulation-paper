# Draft20: realistic-head envelope and quadratic maps

Ricardo Salvador's contribution from private-mirror PR #1, commit `d779094`, is
ported into the canonical `two-tone-validation` branch from `30ba4a6`. Its
Methods 3.3, Results 4.5, Figure 8, six references, producer, numerical outputs,
and settings document replace the approved FEM placeholders. The mirror is a
downstream collaboration copy; this integration does not merge its build setting
or old documentation into the research checkout.

The result separates the geometric predictions. From 2+2 to 1+3 mA, the envelope
focus moves 2.54 mm anterior and the mean-square focus 4.49 mm posterior. The
quadratic and isotropic beat maps rescale by 0.75 without moving. All 32 supplied
combinations preserve these directions, although displacement magnitudes vary.
These are geometric maps on one anatomy, before detection and recurrent gain.
No physiological excitation or suppression map is inferred.

## Integration and qualifications

Theory now points to the completed FEM comparison. At balanced currents, the
envelope contrast is 1.22 versus 1.08 for the square-root quadratic map, a milder
reweighting than the retained two-site example. The Discussion connects the
anterior envelope displacement to the published Violante steering direction and
keeps BOLD separate from a measured neural beat map. The current-ratio prediction
row now distinguishes the completed geometric test from the unperformed
physiological test. The storyline records the completed Methods and Results in
their existing locations. No section or numbered equation is moved.

The PR's variable named `cortex` selects all gray matter outside the hippocampal
ROI, including other deep gray matter. Methods, Results, Figure 8, and the
forward pointer now call this the reference and define the mask explicitly.
The arrays and every numerical value are unchanged. Percentiles and centroids
weight mesh nodes equally. The square-root contrasts are labeled as geometric
degree matching; they do not replace the raw predictions of the detector laws.

The FEM field per unit current is denoted by `F_j`, leaving `E_j` for an applied
field. The text uses mA, consistent with the existing pair-current notation;
Ricardo's producer uses A consistently. The conversion from the 1 A solves is
explicit. Conductivity is `sigma_cond`, defined with units and added to the
notation table. The shared table also identifies the reference maximizing
direction `n*`, which remains fixed throughout the current-ratio sweep.

The access section states that compartment anatomy determines a projection
model. Laminar, axon-aligned, and isotropic choices are modeling assumptions;
maximizing a map over orientation does not establish the detector's direction.
Methods distinguishes the long axis used to report focus displacement from the
projection direction. It also states that population curvature at the model's
operating point is not a measured AIS transfer. Calibrating an anatomical
detector requires access and input-output information beyond FEM geometry.

Giulio confirmed Ricardo's authorship and CRediT roles through Klaus's October 19,
16:04 message: conceptualization (current-ratio steering), methodology (head
modeling), software, formal analysis, data curation, and visualization. The
provisional marker is removed. RS joins the GALVANI ERC Synergy 855109 funding
acknowledgment; no other grant is added. His placement after Borja remains the
existing provisional byline position. Approval of the final submission version
remains an item for all authors.
The shared abstract is unchanged. A possible FEM addition, for Giulio's
decision, is: "On one realistic head, changing the current ratio moves the
envelope and mean-square foci in opposite directions, while the quadratic beat
focus stays fixed." Adding this requires replacing text within the 300-word
budget, not appending it to the current abstract.

## Figure and numerical checks

Figure 8 has one envelope bar in panel (g); its duplicate degree-matched bar
carried the same number. The caption explains the distinction between raw and
square-root contrasts. The quadratic zero line in panel (f) is drawn above the
gray reference guide. Panel (e)'s raw quadratic curve was already red in both
the supplied PNG and the producer; the reported gray/red mismatch was not
reproduced. Both the curve and legend remain red.

Materializing tick labels before final-size scaling fixes the undersized type
found by figcheck. Shorter labels and fewer ticks retain all data. The final
figure has no detected text collisions or base type below 6 pt at its stated
placement. The figure and its rendered page were inspected individually.

`code/check_fem_integration.py` checks 44 numerical arrays against the JSON,
the condition summaries, the full-sweep quadratic and isotropic current-product
scaling, and all 32 displacement signs per map. All checks pass. The interpolated
slice maps preserve the 0.75 factor within their float32 precision. The report is
`docs/fem_integration_checks_2026-10-19.json`; the layout result is
`docs/fem_figcheck_2026-10-19.json`. The producer and both numerical output files
are byte-identical to Ricardo's PR.

This is a check of the portable results and their integration, not a rerun of
the private FEM solver. Recomputing fields and maps requires Neuroelectrics'
temporal-interference library and its IXI002 fields and labels. The Methods,
data-availability statement, and settings document distinguish that dependency
from reproducing the figure from the included outputs.

The six added bibliography entries were checked against publisher, author, or
tool-maintainer sources. The CAT entry now includes the Alzheimer's Disease
Neuroimaging Initiative listed by the publisher. Yatsuda's Methods confirms the
FT7-F8 / TP7-P8 starting montage; the cited comparison uses that placement as
a sensitivity, while retaining Ricardo's electrode model and solver settings.

The JNE article, supplement, fixed-baseline redline, and storyline build to
46, 21, 55, and 13 pages. Their final logs contain no errors, undefined
references, overfull boxes, duplicate labels, or outstanding rerun requests.
The redline remains against draft13 (`c620335`), including the intervening
section and figure moves; its reference-settling pass was run separately.
The abstract remains 296 words by texcount. All manuscript labels are retained,
and the reserved Figure 8 label now points to the FEM figure. The prose checker
reports no mechanical findings in the manuscript, notation, storyline, or this
record. Output hashes and diagnostic counts are in `docs/validation_current.json`.

## Remaining author details and release scope

Through the peer-message skill, Klaus was asked to obtain Ricardo's definitions
for the reported field angles and interface factors before those numerical
claims enter the paper. The conductivity ratio 1.79/0.40 gives a normal-field
jump at a CSF-gray-matter interface under current continuity; it does not by
itself establish a universal factor for the magnitude or an arbitrary projection.
The roughly 4.5 and 20 factors therefore await appropriately scoped wording.
The 58-77 degree range likewise needs its reference axes, summary statistic,
ROI, and reproducible location. Per-hypothesis montage optimization remains a
follow-up outside this paper.

Klaus's initial review applies to `d779094`, before these integration edits.
It verifies the supplied numerical headlines and reports a successful build.
Its note remains at `notes/2026-10-19_klaus/fem_pr1_review.md`.

Ricardo's private-repository write access was verified on October 19. After the
fidelity pass, the private mirror advanced to `c386e54`, preserving his original
`d779094` commit and integrating canonical scientific source `1640b2b`. GitHub
reports PR #1 merged. The article and supplement build independently from the
shared subset and match the reviewed PDFs page for page; the shared PDFs are
byte-identical to the canonical files. Public GitHub, Calliope, Zenodo, and
circulation to other coauthors remain held. No separate Overleaf website pull
was performed. The full TN PDF retains its draft18 archive build. The sharing
record is `docs/share_2026-10-19_ricardo.md`.

No scientific explanation, example, or numerical result is removed. The
replaced text consists of the completed placeholders and stale proposed-test
wording; the only removed graphic is the duplicate envelope bar.

Klaus's read-only fidelity check of the integration checkpoint `23b515c` passed
(message dated October 19, 16:16 CEST). He verified that the producer, JSON and
NPZ are byte-identical to Ricardo's contribution, the figure edits affect only
presentation, and all numbers in Methods, Results, the figure caption, Theory,
Discussion, and the prediction row match the supplied outputs. He withdrew
the raw-quadratic color concern after inspecting a higher-resolution rendering.

His two optional wording notes are applied after that reviewed checkpoint.
The remark about amperes in the producer moves from Methods to the settings
document, which also links the producer's field notation to the manuscript's.
Theory now states invariance for any fixed target and reference regions. The
prediction row uses the same terminology and specifies a cortex-only reference
for a test of deep-target selectivity. The FEM reference remains all gray
matter outside the ROI; no mask, array, or numerical result changes.
