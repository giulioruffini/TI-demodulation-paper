# Ricardo's 6 November results: interface corrections and the per-node export

Checked on 7 November 2026 for Kaiti's handoff of 13:04. Scope: point 4 of the email
(interface counts and the normal-jump attribution) and point 5 (the exporter), plus the
leaf-level comparison of both JSON files against the prior PR snapshot. Kaiti covers the
GM-only contrasts, the eight steering variants, and the manuscript.

Sources: `build/review_ricardo_2026-11-07/` (the email and the four files Kaiti fetched
from PR #2 at 6ade413); the local ref `overleaf/ricardo/fem` at 335a65f, which is the PR
as it stood before Ricardo's four new commits; the local baseline 146679e. PR #2 lives in
the Overleaf-mirror repository (`giulioruffini/TN0484---Temporal-Interference-TI-NMM-demodulation`),
base `main`, six commits, eight files. Nothing was run on the NPZ: it is not committed and
has not been received. Nothing was merged, pushed, or mailed.

## 1. Existing numbers are unchanged

| file | prior PR (335a65f) → head (6ade413) | changed | removed | added |
|---|---|---|---|---|
| `fem_quadmaps.json` | 1620 → 2090 leaves | 0 | 0 | 470: `definitions` 2, `conditions_gm_only_roi` 84, `steering_1to3` 384 |
| `fem_orientation_interface.json` | 1772 → 1892 leaves | 0 | 0 | 120, all under `interfaces/jump_across_interface` |

The prior PR snapshot of `fem_quadmaps.json` is byte-identical to the local
`code/fem_quadmaps.json` (md5 aea7e230…), so the manuscript's numbers come from leaves that
did not move. The 120 interface leaves are, per interface and map, the own-maximum tail's
`n`, `n_below_1`, `n_above_bound`, `min`, `share_within_bound`, and the `outside_bound_E1`
block (above-bound, below-1 and all-node medians of the realized normal jump and of the
tangential mismatch, with the mismatch's percentile among all interface nodes).

Not fetched, so not checked: the head versions of `code/fem_quadmaps.py` (+84 −2),
`code/fem_orientation_interface.py` (+530, new file in the PR), `docs/fem_ixi002_violante.md`
(+70 −6, where the interface paragraph Ricardo rewrites lives; it is not in the local
manuscript or parts) and `data/fem_ixi002/LICENSE`. "The committed scripts reproduce both
files byte for byte" needs the private library and cannot be checked here.

## 2. Point 4, the six own-maximum tails

Every figure in the email and in the replacement paragraph is in the head JSON
(`interfaces/jump_across_interface/<interface>/<map>/own_maximum_lo_over_hi`).

| interface (nodes; ceiling) | map | above ceiling | max | below floor | p1 | min | within |
|---|---|---|---|---|---|---|---|
| CSF/GM (120,892; r = 4.475, r² = 20.03) | env | 33 (0.027%) | 7.905 | 3513 (2.91%) | 0.9950 | 0.885 | 97.07% |
| | quad | 3 (0.0025%) | 20.63 | 3845 (3.18%) | 0.9891 | 0.796 | 96.82% |
| | msp | 3 (0.0025%) | 21.27 | 3936 (3.26%) | 0.9879 | 0.686 | 96.74% |
| GM/WM (126,426; r = 2.667, r² = 7.11) | env | 45 (0.036%) | 3.514 | 2275 (1.80%) | 0.9972 | 0.920 | 98.16% |
| | quad | 33 (0.026%) | 8.667 | 2075 (1.64%) | 0.9952 | 0.877 | 98.33% |
| | msp | 34 (0.027%) | 8.571 | 2211 (1.75%) | 0.9947 | 0.880 | 98.22% |

So: "fewer than 0.05%" (largest 0.036%), "1.6–3.3% below the floor", "first percentile
0.988–0.997", "minimum 0.69–0.92" all hold. "97–98% within" rounds 96.7–98.3%; the exact
range is safer in print. The share he printed as 0.000 is `share_above_bound` = 0.000273
for the envelope at CSF/GM, and "just below 1" rested on its p1 = 0.995; both as he says.
The ceilings are the conductivity ratios 1.79/0.40 and 0.40/0.15 (`conductivities_S_per_m`).

The fixed-direction tails he reported on 30 October (envelope at CSF/GM: 4.36% below 1,
p1 0.928, 2.88% above r, max 7.2 × 10⁴) are unchanged in the head file.

## 3. The normal-jump attribution

The `outside_bound_E1` numbers match the email at all six tails:

| tail | realized normal jump, median | tangential mismatch, percentile of all nodes |
|---|---|---|
| above ceiling, CSF/GM env / quad / msp | 7.08 / 4.57 / 5.27 (r = 4.475) | 62.7 / 74.5 / 67.4 |
| above ceiling, GM/WM env / quad / msp | 2.80 / 2.78 / 2.78 (r = 2.667) | 69.2 / 64.7 / 60.4 |
| below floor, CSF/GM env / quad / msp | 0.81 / 1.11 / 1.02 | 24.1 / 26.9 / 28.8 |
| below floor, GM/WM env / quad / msp | 0.86 / 1.14 / 1.12 | 20.7 / 21.3 / 22.3 |
| all nodes | 2.18 (CSF/GM), 1.83 (GM/WM) | 50 |

The jump is E1's only (the block's name says so); E2's is not stored for these nodes.

Physics. With the tangential field continuous and the normal component scaled by a factor
f on the less conductive side, the own-maximum ratio lies in [1, f] for the envelope and
[1, f²] for the quadratic maps (the 30 October derivation; f ≥ 1 cannot break the floor).
The above-ceiling tail is therefore explained by the stored numbers: the realized f exceeds
r there (medians 7.1 and 2.8 against 4.475 and 2.67), the tangential mismatch is ordinary,
and a ratio of 7.9 fits under a realized f of about 7. For the below-floor tail the stored
medians do not by themselves produce a ratio below 1 at four of the six tails (1.02–1.14 is
above 1); what the numbers show is that these nodes sit in the lower tail of the realized
jump (0.8–1.1 against all-node medians of 1.8–2.2), where the floor has no margin, so the
ordinary node-level mismatch of the recovered fields (median 0.3–0.4% of the field at these
nodes) takes the ratio just below 1. That reading fits p1 = 0.988–0.997: most below-floor
nodes are within about 1% of the floor, and the minima 0.69–0.92 are the extreme of the
same scatter. "Both departures follow the scatter of the realized normal jump" is right as
a description of where the tails sit; "explained by" would overstate it for the floor.
A wording for the replacement paragraph: "At the nodes below the floor it is near 1 (median
0.81–1.14), leaving no margin, so the ordinary node-level mismatch takes the ratio just
below 1 (first percentile 0.988–0.997); at those above the ceiling it overshoots r …".
Kaiti's call.

"No own-maximum map is dimmer on the less conductive side" with "in the continuum" added
is correct: the continuum statement is the [1, r] bound; the discrete field is below 1 at
1.6–3.3% of nodes.

## 4. The other "none / all" claims

- "There is no brightening near the CSF" rests on `near_far_p99` (GM nodes within 2 mm of
  the CSF/GM interface against farther GM): p99 ratios 0.90 (env), 0.86 (quad), 0.93 (msp).
  A 99th-percentile statement, as Ricardo says; "the upper tail does not brighten" is the
  supported form. The same block has the WM side brighter near GM/WM in the upper tail
  (ratios 1.25, 1.62, 1.57), should the text generalize.
- "The remaining interior maxima are at the level of the field-recovery noise": the file
  has no noise figure (no key contains "noise"). `local_maxima_on_boundary` gives only the
  counts (GM, along n*: 270–330 interior maxima out of 13,800–14,100 strict maxima, 2.0–2.3%).
  Drop the clause, as he proposes.
- "Tangential continuity on every face, largest mismatch 5 × 10⁻¹¹": `components_per_face`
  maxima are 5.2 × 10⁻¹¹ (CSF/GM, E1), 1.1 × 10⁻¹², 4.7 × 10⁻¹², 5.1 × 10⁻¹⁴. This holds for
  the element fields at the faces. The recovered nodal fields are not tangentially continuous:
  median mismatch 1.0–1.3% of the field, maxima 0.55–2.5 of the field
  (`jump_across_interface/<interface>/components`). Any sentence must name the element fields.
- "At every node" (envelope equals TImax to machine precision) and "all 32 combinations"
  rest on a maximum and on counts, as he says.
- Carrier separation: `orientation/montages/<montage>/carrier_separation_deg/per_node` gives
  medians 14.2° (Violante) and 7.5° (Yatsuda), p95 29.2° and 16.8°; his "7–14°" were the
  medians, his "17 and 29" the p95s. The block is the 1,568 ROI nodes (`orientation/roi_nodes`).

## 5. Point 5, the exporter (`code/fem_export_nodes.py` at 6ade413)

**76 numbers and 8 counts.** The count follows from the loop structure given the head
JSON: for `conditions` and `conditions_gm_only_roi`, 2 ratios × 4 maps × 3 statistics
(`tc_p95`, `tc_mean`, `roi_mean`) = 24 plus the degree-matched `tc_p95` of the three
degree-2 maps at both ratios = 6, twice (60); radial `tc_p95` for 2 ratios × 4 maps (8);
the four aseg steering variants' envelope and mean-square `roi_mean_change` (8); the same
variants' rising-node counts, compared as integers (8). The JSON has exactly four aseg
variants (Violante and Yatsuda × GM+WM and GM). Not compared, though the fields support them:
the degree-matched `tc_mean` and `roi_mean`, every `roi_p95`, `cortex_p95`, `cortex_p99`,
the whole `sweep`, `displacement_1to3_vs_1to1`, `upper_tail_1to1`, the aseg half of
`sensitivity_grid`, the quad and iso steering entries, and the reference-rising fractions
(8.9%, 14.0%). The check could be widened without new inputs.

**Re-implementation.** `np_maps` equals `maps_at` (λ₀ = 0.5, 4 mA total, 1:3 as 1 + 3 mA
with the posterior pair at 3 mA), `np_stats` equals `stats` for the three compared
statistics, the reference is GM outside the ROI as in `main()` (`ctx`), and the radial
center is the mean of all GM and WM rows as in `main()`. Checked against the local
`code/fem_quadmaps.py`, which the head version extends (+84 −2, not fetched).

**Direction reconstruction.** `np_n_star` is the Grossman closed form: with a the larger
field and b the other, sign-flipped to an acute angle, the envelope-maximizing direction is
along b when |b| ≤ |a| cos θ (the condition coded as |b|² ≤ a·b), else in the plane of a
and b perpendicular to a − b (coded as (a × b) × (a − b)). Both branches are right, the
form is scale-invariant so passing per-ampere fields where `held()` passes 2 mA fields
changes nothing, and parallel fields fall in the first branch, so the cross product never
divides by zero there. Two small points: a zero field row gives a NaN direction, and the
check's comparisons (`worst = max(worst, |got/want − 1|)`, `n_star_dev > 1e-12`) are silent
on NaN, since `max` and `>` both ignore it; an `np.isfinite` assertion on the loaded arrays
would close that. The agreement to 4 × 10⁻¹⁶ is a claim about the run, not checkable here.

**Row counts.** 446,877 = 274,718 GM + 172,159 WM: the interface file's `local_maxima_on_boundary`
has those two `n_nodes`, and `n_rows.brain` in `fem_quadmaps.json` is 446,877. The reference
counts in the steering variants are consistent: 273,544 = 274,718 − 1,174 (aseg GM ROI nodes),
273,705 = 274,718 − 1,013 (atlas GM).

**The atlas label.** Its omission makes these leaves unreproducible from the export: the
four atlas steering variants (including the +29.7% that the Discussion cites as the largest
mean-square rise), `robustness/atlas_label`, the atlas half of `sensitivity_grid`, and
`n_rows/roi_atlas*`. The FreeSurfer side is complete. The CC BY-NC claim for
`labels_Neuromorphometrics.xml` is Ricardo's reading of the SPM12 file; not verified here
(no SPM12 on this machine), and consistent with how that atlas is usually distributed. The
data-availability text should say which numbers the record does not cover.

**Can a third party reproduce the 76 numbers from the file?** Not with the script as
committed. `fem_export_nodes.py` imports `fem_quadmaps` at module level, and
`fem_quadmaps.py` exits at import unless `TI_MODEL_ROOT` points at the private library
(lines 56–60 of the local copy). The "NumPy-only consumer" is NumPy-only in its body but
cannot be imported without the library, so `check()` is a self-check for Ricardo until the
import moves inside `export()` (as `export_fem_portable.py` already does, "so --help works
without the private library") and a check-only entry point reads an existing NPZ. The
interface file is outside the export altogether: it needs the mesh faces, the element
fields on both sides, the potentials and the laminar field (its `provenance` lists
`potentials_violante`, `mesh_violante`, `laminar_io_laplace`, `positions_*`). Point 4
therefore rests on the committed JSON, `fem_orientation_interface.py`, and the private
library, and will stay that way.

**Hash label.** `fem_quadmaps.json` calls its input digests `inputs_sha512`;
`fem_orientation_interface.json` and the exporter's README call the same digests
(identical 128-hex strings for `fields_violante`, `fields_yatsuda`, `aseg`)
`inputs_blake2b512`. Both come from `ti_model.provenance.hash_file`. One label is wrong;
Ricardo should say which hash the function computes and relabel, since the README tells a
reader to verify the NPZ inputs by BLAKE2b-512.

**`fem_portable.py` and its exporter are on GitHub.** They are in the public companion
repository `giulioruffini/TI-demodulation-paper`, branch `two-tone-validation` (since
ceec291, draft23; pushed 24 October): `code/fem_portable.py`, `code/export_fem_portable.py`,
`docs/fem_portable.md`, `notes/2026-10-24_kaiti/check_portable_fem.py`. They are not in the
Overleaf-mirror repository where PR #2 lives, which is where Ricardo looked. The schema he
asks for (`read_bundle`, lines 64–85): one NPZ with `metadata` (JSON string; `schema` must be
`tn0484-fields-v1`; `montages` lists the montage names) and, per montage, arrays prefixed
`<montage>__`: `xyz_mm`, `E1_per_A`, `E2_per_A`, `n_star` (float, shape (n, 3), all finite;
n* unit or zero) and `gm`, `wm`, `aseg`, `atlas` (bool, shape (n,)). His file differs in every
key (`E1_violante`, `tissue`, `roi_aseg_left_hippocampus`, …) and has no atlas mask, which
`read_bundle` requires. Kaiti's note already says the consumer should accept declared labels
rather than invent one.

## 6. Verified here versus awaiting the NPZ

Verified from the committed files: no existing leaf of either JSON changed between the
prior PR snapshot and the head; every number in point 4 and in the replacement paragraph;
the derived ranges; the normal-jump and tangential-mismatch figures; the carrier-separation
percentiles; the row and reference counts; the 76 + 8 arithmetic; the map, statistic,
reference and radial definitions in the consumer; the closed form of n*; the consequences of
the omitted atlas label; the import barrier; the hash-label mismatch; the portable schema.

Awaiting the file: that `check()` passes (worst relative difference, the eight counts),
the n* agreement to 4 × 10⁻¹⁶, 45.7 MB, the dtypes and shapes the README lists, the
`metadata` block (input hashes equal to the JSON `provenance` digests; both repositories'
commits and `clean` flags), the `pairs_*` arrays, and the attribution and LICENSE texts.
Beyond Ricardo's own check, the file would let us recompute the full aseg side of
`fem_quadmaps.json` (sweep, foci, upper tail, grid) with an independent consumer.

## 7. For the report

No blocker. Wording: the floor sentence (Sec. 3), "element fields" for the continuity
claim, "96.7–98.3%" instead of "97–98%", and the data-availability statement of what the
record does not cover. Repository: move the library import inside `export()` and add a
check-only entry; make the two hash labels agree; tell Ricardo where the portable scripts
are and give him the schema above.
