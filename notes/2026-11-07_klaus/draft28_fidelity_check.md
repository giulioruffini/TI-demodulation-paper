# Draft28 (b42fb1e) fidelity check against draft27 (146679e) and PR #2 head 6ade413

Checked on 7 November 2026 for Kaiti's 13:52 handoff. Read-only: the manuscript diff, the
two new supplement parts, the three modified parts, the availability paragraph, Kaiti's
revision record and check script, and Ricardo's documents as imported. Every number was
compared with `code/fem_quadmaps.json` and `code/fem_orientation_interface.json`, which at
b42fb1e are byte-identical to the PR head (as are the three scripts and the LICENSE; Kaiti
edited only the two Markdown files, for figure numbering and a status section). Nothing
was built, edited, pushed or mailed. The presentation's FEM slide and backup table were
read for numbers only.

**Verdict: no blocker.** Every number in the main text, Table 3, S3 and the slides is in
the stored outputs; no scientific statement of draft27 was dropped; the continuum bound is
derived correctly on both sides; the node-mean and face-level continuity statements match
the code. Three wording suggestions below, none numerical.

## Main text

| statement | source | status |
|---|---|---|
| Table 3 GM-only rows: 1.09, 0.84, 0.76/0.55; 0.94 (0.97), 0.51/0.51; 0.71 (0.85), 0.76 (0.87), 0.40/0.46 | `conditions_gm_only_roi` | all match |
| both beat maps fall to 75% at every node, to machine precision | `checks`: quad and iso 1:3/1:1 − 0.75, max 2.2 × 10⁻¹⁶ | holds for both |
| isotropic beat 1.18 (1.08 degree-matched) | 1.177, 1.085 | match |
| upper tail 52% WM against 25% | 0.517, 0.251 | match |
| only the envelope exceeds one at 1:1 (GM only), none at 1:3; no mean-based contrast exceeds one | GM-only: env 1.086, quad 0.935/0.967, iso 0.943/0.971, msp ≤ 0.874; 1:3 env 0.839; largest mean 0.807 | match |
| laminar fractions 0.29, 0.11, 0.12; 934 of 1,568 | `laminar_aligned_cell/all_defined` 0.291, 0.105, 0.119; `laminar_defined_nodes` 934 | match |
| median projected interface jumps 1.13–1.34 | `measured_lo_over_hi` medians 1.170, 1.282, 1.253, 1.135, 1.327, 1.337 | match |

Draft27's results sentences survive in compressed form: the 4 → 3 mA² product, the fixed
quadratic pattern, the two focus directions, the 1.08 against 1.22 comparison, the 1.24 peak,
the 32-combination directions, the radial-versus-atlas remark. "Mean-square polarization
favors the reference" at 1:1 is now carried by Table 3 (0.92, 0.96) and by "no mean-based
contrast exceeds one".

## S3, orientation (`fem_orientation.tex`)

All 24 angle entries of Table S-orientation (median and quartiles, both montages, three
directions, four axes) match `vs_PC_axes_deg` and `vs_laminar_deg` to the rounding. The
field-weighted medians differ from the node medians by at most 1.34° on the PC axes and
1.50° on the laminar axis ("at most about 1.5°"). Laminar: 934 (59.6%), 565 interior; 33°
(21–54) from PC3, 76° (55–83) from PC2; spread 31° (23–51); PC3 = PC1 × PC2 recomputed from
`pc_axes` (−0.161, 0.282, 0.946). Absolute projections 0.36, 0.31 (0.358, 0.313). All twelve
fraction entries of Table S-laminar match `laminar_aligned_cell` (all-defined and interior,
both montages); the caption's interior angles 71°, 74°, 71° match. Carrier separation 14.2°
(10.2–18.6), 7.5° (4.2–11.4), p95 29.2° and 16.8°. Cap overlap: e2 9.4 and 18.4 mm from AF8
and Fp2, e4 10.4 and 19.0 mm from P8 and PO8, 20-mm discs, 20-mm criterion.

## S3, interfaces (`fem_interfaces.tex`)

Faces 241,780 / 253,608 / 0; edge 1.51 mm (1.37–1.66); node counts 120,892 and 126,426;
r = 4.475 and 2.667, squares 20.03 and 7.11; n* angle to the normal 64° and 63°; normal
fraction medians 20% and 46%; predicted medians 1.26–1.80; Table S-jumps (six medians with
quartiles) matches `measured_lo_over_hi`; projected tails 4.4–12.8% below one and 0.2–2.9%
above r^k, maxima 7.2 × 10⁴ and 1.29 × 10⁵; Table S-tails (24 entries) matches
`own_maximum_lo_over_hi`, with the ranges 96.7–98.3%, 1.6–3.3%, < 0.05%, p1 0.988–0.997,
minimum 0.686; tolerances as coded (absolute 10⁻⁹ at one, relative 10⁻⁹ at the ceiling).
Per-face normal jumps at the 10% cutoff 2.15 (1.45–3.18) and 1.88 (1.51–2.24), cutoff
ranges 1.97–2.17 and 1.88–1.90, E2 1.99–2.17 and 1.86–1.88, all from
`components_per_face`; the element-face residual 5.2 × 10⁻¹¹; nodal residual medians
0.95–1.0% ("about 1%"). Above-ceiling E1 normal-jump medians exceed r at all six tails,
envelope 7.08 and 2.80; percentiles 60th–75th; below-floor medians 0.81–1.14, stated as
an association, not a cause. Near/far p99 ratios 0.90, 0.86, 0.93 and 1.25, 1.62, 1.57;
top-1% composition 67–73% WM, 81–82% near GM/WM against 73%, 24–31% near CSF against
47.5%; local-maxima fractions 98.0/96.5 and 97.9/96.1 against 90.0/73.4, counts 262 of
13,144, 227 of 6,395, 270 of 12,659, 245 of 6,262; 95.4% within 2 mm.

The continuum derivation is right on both sides. With A = 1 + (r − 1)νν^T, E_low = A E_high
encodes tangential continuity and σ_high E_n,high = σ_low E_n,low; eigenvalues 1, 1, r; the
projection identity n·AE = |An| m·E with 1 ≤ |An| ≤ r gives the ceiling r^k for a map
homogeneous of degree k, and n ∝ A⁻¹m for a high-side maximizer m gives |An| = 1/|A⁻¹m| ≥ 1,
hence the floor. The fixed-projection remarks are right too: along the low side's own
maximizer the ratio is M_low/f(n·E_high) ≥ M_low/M_high ≥ 1, and along the high side's
maximizer it is f(m·E_low)/M_high ≤ M_low/M_high ≤ r^k; GM is the low side at CSF/GM and
the high side at GM/WM, and n* is the maximizer of the recovered GM nodal field, not of the
side means that enter the jump.

Node mean versus face continuity, as coded (`node_side_field`, head script lines 235–249):
each interface node's side field is the mean of the element fields of that side's
tetrahedra across the node's incident interface faces, and the node normal is the
normalized sum of those faces' area vectors. The text's "averaged over its incident
interface-face element samples" and "normalized sum of their area vectors" say exactly
this; Ricardo's Markdown says "adjacent tetrahedra on each side", which is looser. The
tangential identity holds per face for the element fields and fails for these node means;
the text keeps the two apart.

## Other parts, references, availability

`fem_sensitivities.tex`: the GM-only table (16 entries) matches; "no raw or degree-matched
mean contrast reaches one in either tissue definition" holds (largest raw 0.807,
degree-matched 0.739). `steering_algebra.tex`: eight variants, 17.2–29.7%, −43.9 to −46.2%,
−25%; 1,353 of 1,568 (86.3%), 2 (0.13%), 80.8–90.9%, 0–0.2%, reference 8.9% and 14.0%,
equal node weights along n*. `references.bib`: `dekraker2022` (eLife 11, e77945,
10.7554/eLife.77945) added and cited once. The availability paragraph names both
producers, the exporter, the mesh-and-potentials requirement, the atlas and interface
exclusions, the BLAKE2b-512 hashes and the four records, and no longer names the
unrun consumer. Slides: the GM-only table, 1,174 nodes, 17.2–29.7%, 43.9–46.2%, 86.3%,
0.13% and the backup table match.

## Suggestions (wording, none blocking)

1. Main text, last sentence of the FEM results: "Median projected interface jumps are
   1.13–1.34, but their continuum limits remain unresolved" conflates two things. A fixed
   projection has no continuum bound (S3 says so); what is unresolved is whether the
   orientation maxima's departures from [1, r^k] close under refinement. Suggested:
   "Median projected interface jumps are 1.13–1.34; the continuum bounds apply to the
   orientation maxima, which leave them at 1.7–3.3% of interface nodes, and whether
   refinement closes that gap is unresolved (supplement, \S\ref{supp:fem-interfaces})."
   (1.7–3.3 = 100 − within; or keep "1.6–3.3% below one and fewer than 0.05% above".)
2. Methods, "Radial, laminar, and isotropically averaged projections provide sensitivity
   comparisons (supplement, \S\ref{supp:fem-orientation})": the radial comparison lives in
   \S\ref{supp:fem-sensitivities}; point to both or drop the pointer's claim to the radial.
3. Table 3: the GM-only rows leave "Mean change" blank although the values exist
   (`steering_1to3`, Violante/aseg/GM: envelope −44.7%, beats −25%, mean square +27.3%).
   Optional; the supplement table carries them.

Not checked: the storyline update, `docs/current_state.md`, the redline, and the
presentation beyond its FEM numbers; Kaiti's rendered-page review stands for layout.
