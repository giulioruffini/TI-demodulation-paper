# Ricardo's interface and orientation contribution: PR #2 review

October 30, 2026. Manuscript baseline: draft24 at `30ed891`. Reviewed the full
Gmail thread `1a111f0bee3155d8`, including Giulio's October 20 request, and the
three PR files at `335a65f8d714b83ed1cf4de76211ff8886b51da7`. Klaus's independent
check is `4faf779`, `notes/2026-10-30_klaus/pr2_bound_check.md`. No manuscript,
figure, or simulation input changed; PR #2 remains unmerged.

## Provenance supplied; wording still requires correction

The PR supplies the orientation/interface producer, its JSON, and the HippUnfold
image digest, version, invocation, and segmentation-model hash. The three shared
input identifiers (Violante fields, Yatsuda fields, aseg) match the existing
`fem_quadmaps.json`. Those identifiers are BLAKE2b-512; the existing
`inputs_sha512` key is a documented misnomer. The imported private TI library is
identified by URL but needs an exact revision. Its inputs are not bundled in this
PR. This review checks code and recorded output, not an independent FEM rerun.

The laminar calculation uses 934 valid nodes out of 1,568 and checks 565 interior
nodes separately. The script computes nodewise ratios to each map's own
orientation maximum. Recorded medians are 0.2914 for envelope excursion, 0.1050
for quadratic excursion, and 0.1189 for mean-square polarization. These agree with
the proposed rounded values and quantify a geometric projection under the
laminar-detector hypothesis, not measured neuronal coupling.

## Exact bounds and discrete interface statistics differ

Under the common isotropic continuum interface transform, each nonnegative
degree-k map maximized over orientation has a low/high ratio in [1, r^k].
Generic fixed oblique projections have no such conductivity-ratio bounds.
An exact low-side envelope maximizer nevertheless retains an envelope floor of
one: its low-side value is at least the high-side maximum, which is at least its
high-side value. An exact high-side envelope maximizer similarly retains the
ceiling r. These qualifications were in our October 20 notes but omitted from
the sent explanation; Ricardo's reply inherits that omission.

The new code takes n* from recovered GM nodal fields and evaluates interface
jumps using separately averaged element fields. GM is the low-conductivity side
at CSF/GM and the high-conductivity side at GM/WM. The optimization and field
definitions therefore require explicit separation. The element-side averages
also need not satisfy a single continuum transform with the averaged normal.
Fixed obliqueness alone does not explain violations of the special envelope
bounds. A normal factor smaller than r but still at least one does not by itself
break the own-maximum floor either.

The JSON contradicts the email's statement that no own-maximum map exceeds the
ceiling. At CSF/GM the envelope exceeds r at 33 nodes (0.0273%), with a maximum
7.905 against r = 4.475; at GM/WM, 45 nodes (0.0356%) exceed r, reaching 3.514
against 2.667. The second-order maps also have rare exceedances. The full table
is in Klaus's note. These are discrepancies in the discrete fields/measurement,
not counterexamples to the continuum theorem.

The approximately 7 x 10^4 tail is the projected envelope maximum. The projected
quadratic maximum is 1.288 x 10^5. Such ratios require reporting their denominators
before any interpretation as large absolute exposure. Prefer medians/IQRs in the
article; leave the tails in the numerical diagnostic.

The reported normal jumps 2.15 (1.45–3.18) and 1.88 (1.51–2.24) select faces with
high-side normal fraction at least 0.10. State that selection. Across faces the
tangential residual is near rounding; at nodes the separate averages do not
retain that property. Replace “only on average” by a statement about the weak
finite-element formulation: raw continuous-Galerkin flux is not generally
locally conservative. See Cockburn, Gopalakrishnan, and Wang (2007),
[author manuscript record](https://pdxscholar.library.pdx.edu/mth_fac/64/).

## Integration and convergence plan

Keep one orientation paragraph and one short interface qualification in the
article, with a brief Methods definition and both producer names in provenance.
Place the interface proof, complete tables, face-selection sweep, and convergence
diagnostic in Supplement S3. Preserve the distinction between map-specific
orientation maxima and the common n* used in the current-ratio maps. The
October 20 integration proposal remains the starting text, shortened to fit
draft24 rather than appended wholesale.

Before the offered refinement, obtain the pinned solver/library, mesh, potentials,
and boundary-condition inputs and reproduce the existing result. One uniform
refinement tests discretization at fixed geometry; it does not establish a
converged limit or test segmentation uncertainty. Compare a normalized,
area-weighted normal-current mismatch and the map medians alongside the same
normal-fraction sweep, rather than relying on extreme projection ratios.
Unresolved convergence remains explicit until that check is completed.

Gmail access was verified directly for Giulio's Neuroelectrics account. Klaus
uses Claude Code's Gmail MCP connector; this session uses the connected Gmail
tools. No email was sent to Ricardo. The separate disclosure about his internal
note needs Giulio's decision after its text, attribution, and access scope are
available; it does not change this scientific review.
