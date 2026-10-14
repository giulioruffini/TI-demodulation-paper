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
His returned algebraic check, dated 11:35 CEST and based on `d3a3107`, agrees
with the plan and the static sign, QIF crossover, and homogeneous-boundary
arguments. It is an independent sign/scope check, not a fidelity review of the
subsequent draft19 edits. Section 2.6 now states the concrete example: the
static source is negative at the pinned JR operating point of 8.30 mV.
Independent substitution gives curvature -0.1508169 s^-1 mV^-2 and source
-1.88521e-4 s^-1 for two 0.05 mV tones, matching his reported value. Carrier
polarity reversal is also stated explicitly.

One normalization in his generic dynamic-source suggestion needs qualification:
the manuscript defines kappa_DC per squared peak current, not per mean-square
polarization. In its normalized current units the coefficient multiplying the
mean square is twice kappa_DC; conversion to polarization also needs H_v and
the physical-rate time scale. The paper therefore retains its existing dynamic
definitions rather than identifying this coefficient directly with the static
polarization coefficient sigma''/2. The adiabatic qualification is retained:
finite-frequency values follow the full crossover formula, not F''/4 exactly.

Klaus's subsequent textual check of `faeb858` (message dated 11:50 CEST)
passes the static sign, boundary statement, steering factors, and S13
normalization. It identifies an ambiguous antecedent in the QIF paragraph:
"its adiabatic mean-rate shift" could refer to the fast-carrier limit. The
paragraph now names the uncoupled population and puts the fast-carrier and
slow-carrier limits in separate sentences. It also states that recurrence need
not preserve the source sign. The remaining "physiological DC map" wording is
replaced with distinct signed-source and physiological mean-response maps.
The optional explicit negative JR-source example was already in `15c1d59`.

## Release status

Draft19 is local. The earlier Overleaf sync covers draft18 source `e17e4a9`
mirrored as `7006e90`; it is not a sync of these changes. No new synchronization,
GitHub push, Calliope cut, Zenodo release, or coauthor circulation is performed.

Later on October 14, Giulio authorized sharing this draft privately with Ricardo.
That subsequent GitHub update and collaborator invitation are recorded in
`share_2026-10-14_ricardo.md`; the earlier local-only statement describes the
revision checkpoint before that authorization.
