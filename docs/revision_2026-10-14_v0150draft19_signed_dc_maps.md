# Draft19: signed steady sources and geometric maps

Giulio found the positive mean-square map misleading because it could be read as
an always-excitatory DC response. This local revision starts from `d3a3107`
(draft18 scientific source `e17e4a9`). The redline remains against draft13
`c620335`, the recorded reading baseline.

The paper now separates mean-square polarization, the signed detector source,
and the mean response after recurrent feedback. In the static JR detector,
`Y_DC = sigma'' I / 2`, with `I = (epsilon_1^2 + epsilon_2^2) / 2`.
The field factor is nonnegative; the curvature determines the source sign.
Reversing the cell orientation preserves both squared projections. Other
directions change their magnitudes, with sign fixed only while the detector
coefficient is fixed. The circuit determines the resulting mean-rate change.

Table 2 retains its geometric comparison and adds the signed steady source.
Section 2.6 states the sign distinction, the QIF regime qualification, and the
boundary restriction for the magnitude with a spatially constant coefficient.
The shared notation, abstract, steering test, FEM placeholders, and storyline
use the same distinction. No FEM results are supplied or inferred.

Figure S13 retains the original modulation and pre-gain mean profiles and adds
panel (c), showing the static JR source for uniform positive curvature and
equal-magnitude negative curvature. Both curves use one positive normalization,
so suppression remains visible. These are assumed detector states before
recurrence. Ricardo's third field-only map remains mean-square polarization;
any signed source must state its detector and operating point and use a scale
centered at zero. A network-response map additionally requires a circuit model.

The positive effective E-drive shift in the fast-carrier QIF example remains a
specific model result. The adiabatic rate shift follows the signed curvature of
the effective rate curve. The manuscript's existing crossover equation supplies
the distinction; no new physiological claim is introduced.

## Validation and outputs

The figure producer preserves its default two-panel internal-note mode. Its
paper mode adds the signed panel and checks a direct full-sigmoid average at
opposite-curvature baselines against the quadratic prediction. Those signs
agree; relative errors are below 0.0005%. The record is
`docs/draft19_spatial_map_checks_2026-10-14.json`.

The working JNE article, supplement, fixed-baseline redline, storyline, and
standalone S13 figure build to 43, 21, 52, 13, and 1 pages. Logs contain no
errors, undefined references, overfull boxes, duplicate labels, or outstanding
rerun requests. The redline needed an additional reference-settling build;
its remaining math-font-size warnings come from latexdiff. The abstract is
296 words. Article and supplement label numbers are unchanged.

The changed table, sign argument, FEM placeholders, test row, notation, figure
and caption, and corresponding redline and storyline pages were inspected as
rendered images. Figure S13 passes figcheck for text collisions, clipping, and
minimum base type size at its stated placement. The prose checker reports no
mechanical findings in the changed manuscript, shared sources, or this note.
The README's two existing flags are false positives: a line-broken "rather than"
and dash placeholders in a Markdown table, not sentence-level em dashes.
The article and redline on the review shelf are byte-identical to the outputs.
Details are in `docs/draft19_signed_dc_maps_audit_2026-10-14.json` and
`docs/validation_current.json`.

The full TN PDF remains the draft18 archive output until a coordinated cut.
The original internal reading note and its figure assets remain unchanged.

No explanation, result, numerical claim, or numbered equation is removed. The
new detector formula is unnumbered. Klaus was asked for a bounded read-only
check of signs, orientation, the dynamic QIF exception, and the spatial scope.
That independent check is pending at this checkpoint; the local algebraic,
numerical, build, and visual checks above are complete.

## Release status

Draft19 is local. The earlier Overleaf sync covers draft18 source `e17e4a9`
mirrored as `7006e90`; it is not a sync of these changes. No new synchronization,
GitHub push, Calliope cut, Zenodo release, or coauthor circulation is performed.
