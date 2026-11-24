# Ricardo's PR #2 (335a65f): the interface bound along n*, checked against his JSON

Klaus, 2026-10-30, for Kaiti's decision request of 15:47 and 15:51. Read-only: no manuscript edit,
no message to Ricardo. Script `pr2_jump_tails.py` (this folder) reads
`code/fem_orientation_interface.json` at the PR head and prints `pr2_jump_tails.txt`.

## Gmail route

This session reads Giulio's Neuroelectrics Gmail through the claude.ai Gmail MCP connector of
Claude Code (deferred tools, loaded with ToolSearch `select:mcp__claude_ai_Gmail__get_thread,...`).
The thread is 1a111f0bee3155d8, "Re: FEM request: envelope vs quadratic TI dose maps on a real
montage"; `get_thread` with PLAIN_TEXT returns 380 kB, so the result lands in a file and the bodies
are under the key `plaintextBody`, with quoted lines stripped by a short script. Giulio sends;
the session only reads and drafts.

## What the sent exchange says

Giulio's reply of October 20 (14:18 CEST, forwarded again on October 29) states, in its item 3,
that current continuity bounds the magnitude ratio and each map at its own orientation maximum
by r (r² for second-order maps), that no bound holds along a fixed projection direction because
the high-side projection can vanish by cancellation, and that "n* held on both sides is such a
direction". It does not state the refinement of my addendum of October 20 (14:10, in
`notes/2026-10-20_klaus/interface_bound_check.md`): that an exact envelope maximizer of the less
conductive side keeps an envelope floor of one, and an exact maximizer of the more conductive
side keeps the ceiling r. Nor does it distinguish the source of n* from the fields the ratio is
built from. Both points exist only in my note and in Kaiti's
`notes/2026-10-20_kaiti/ricardo_points_2_3_integration.md`.

Ricardo's reply of October 30 (16:15 CEST) accepts the correction, verifies it on 500,000 random
configurations, and rewrites the bound paragraph: no bound along a fixed direction "on either
side"; n* qualifies "because it is fixed and oblique, a median 63--64° from the interface normal,
not because the projection along it vanishes"; along n* the ratio falls below 1 at 4--13% of
interface nodes and above the bound at 0.2--2.9%, reaching about 7×10⁴; the own-maximum maps lie
within [1, r^deg] at 97--98% of nodes, "the rest fall just below 1 ... none above".

## What the code does

`fem_orientation_interface.py` at 335a65f computes n* once from the recovered nodal fields
(`nstar = ti_max_direction(E1, E2)`, line 367) and looks it up by the GM row of each interface
node (`nstar_at(gm_row)`, lines 446 and 448, for both interfaces). The jump itself uses the mean
element field over each side's tetrahedra adjacent to the node (`node_side_field`, lines 301--304).
So n* is the envelope maximizer of the GM row's recovered field, not of the GM-side element mean
that enters the ratio, and the two side means are not related by the continuum map A: per face
the tangential field is continuous to 10⁻¹³, but per node the tangential mismatch is a median
1% of the field with a 95th percentile of 8--17%, and the per-node normal ratio has a 5th
percentile below one (−1.05 at CSF/GM, 0.74 at GM/WM over all nodes; above one only once the
high-side normal part exceeds 0.2 of the field).

## Agreement with Kaiti's qualification, with two refinements

Agreed: the below-one values of the envelope along n* at CSF/GM come from discretization, and
"fixed and oblique" alone cannot produce them, because there n* is (approximately) the envelope
maximizer of the less conductive side. Two refinements.

1. **Which discretization.** A smaller normal jump by itself cannot break the floor: any normal
   factor ≥ 1 keeps |A'n| ≥ 1 and the own-maximum argument goes through unchanged. What breaks it
   is the node-level mismatch (n* from the recovered row, tangential parts unequal at the node, a
   per-node normal ratio below one where the high-side normal part is small). The median realized
   jump of 2.15 against 4.475 is a separate finding.

2. **The two interfaces differ in sign.** The GM row's n* is the less conductive side's maximizer
   at CSF/GM (GM over CSF) and the more conductive side's at GM/WM (WM over GM). The continuum
   prediction for the envelope is therefore a floor of one at CSF/GM and a ceiling of r at GM/WM,
   and the JSON shows exactly that asymmetry; quad and msp have neither along n*; the own-maximum
   maps have both at both interfaces.

| interface, map (along n*) | below 1 | p1 | above r^deg | max |
|---|---|---|---|---|
| CSF/GM envelope (floor expected) | 4.36% | 0.928 | 2.88% | 7.2×10⁴ |
| CSF/GM quadratic | 9.42% | 0.811 | 1.35% | 1.3×10⁵ |
| CSF/GM mean-square | 12.85% | 0.698 | 0.52% | 435 |
| GM/WM envelope (ceiling expected) | 12.04% | 0.462 | 0.20% | 225 |
| GM/WM quadratic | 9.68% | 0.556 | 0.22% | 315 |
| GM/WM mean-square | 9.85% | 0.758 | 0.39% | 208 |

The envelope at CSF/GM falls below one at 4.4% of nodes with a first percentile of 0.93 (small
shortfalls, the discrete routes above), and at GM/WM at 12% with a first percentile of 0.46 (no
floor exists there). The exceedances mirror it: 2.9% above r at CSF/GM, 0.2% at GM/WM. Ricardo's
pooled "4--13%" and "0.2--2.9%" are the extremes of this table across maps and interfaces.

## Points for the PR review (Kaiti's call)

- "None above" is contradicted by the JSON. Own-maximum nodes above the ceiling: envelope 33
  (0.027%, max 7.9 against r = 4.475) at CSF/GM and 45 (0.036%, max 3.51 against 2.667) at GM/WM;
  second-order maps 3 at CSF/GM (max 21.3 against 20.03) and 33--34 at GM/WM (max 8.7 against
  7.11). Below one: 1.6--3.3%, first percentile 0.988--0.997, as the text says. The same node-level
  mismatch explains both tails.
- "Not because the projection along it vanishes" and the maximum of 7×10⁴ describe the same
  mechanism: obliqueness is why no bound exists, near-cancellation of the high-side projection is
  where the large values come from. The two wordings are not in conflict, but the second half of
  his sentence contradicts his own maximum.
- Ricardo's paragraph is correct for a generic fixed direction. If the manuscript says which side's
  envelope n* maximizes, the measured tails read as a confirmation: floor at CSF/GM, ceiling at
  GM/WM, both up to the discrete mismatch, with the second-order maps unbounded on both sides.
- The variant "GM/WM from recovered nodal fields" (both rows recovered, n* exact for the GM row)
  behaves as a high-side maximizer should: envelope median 1.08, 5th percentile 0.67, 95th 1.79
  under r = 2.667.

## Kaiti's independent verification (16:03)

Kaiti re-derived the tails from the PR JSON and agrees on the floor/ceiling split and on the
false "none above". Two additions from her read: the quoted 7×10⁴ is the envelope maximum only
(the quadratic maximum is 1.29×10⁵, as in the table above); and the face medians and
interquartile ranges Ricardo quotes (2.15, 1.45--3.18; 1.88, 1.51--2.24) are taken over faces whose
high-side normal fraction is at least 0.10, which the prose should state. The shared field and
label hashes match the existing `fem_quadmaps.json`. Her recommendation: brief orientation and
interface text in the article, proof, tails and mesh diagnostics in the supplement; "weak
conservation" rather than an unspecified exact average for the normal current of linear elements.
