# Review of Ricardo's FEM pull request (mirror PR #1, commit d779094)

Reviewed 2026-10-19 by Klaus in a detached worktree of `overleaf/ricardo/fem`, which is based on mirror main aa18f10 (draft19 = afa5e44).

## What was checked

- **Build.** `./build.sh jne` on the PR branch gives 46 pages, 0 errors and 0 undefined references. Fig. 8 renders on page 27.
- **Numbers.** Every headline value in §4.5 matches `code/fem_quadmaps.npz`:
  - target-to-cortex ratio: envelope 1.221 → 0.954; quadratic 1.167 at every ratio; 𝓘 0.918 → 0.903;
  - focus shift at 1:3: envelope +2.54 mm, quadratic 0.00, 𝓘 −4.49 mm;
  - hippocampal-mean ratio: envelope 0.553, quadratic 0.750, 𝓘 1.244;
  - envelope peak 1.235 at a posterior share of 0.525; 𝓘 shifts +1.48 mm at a share of 0.1 and −6.31 mm at 0.9;
  - JSON checks: the quadratic and isotropic 1:3/1:1 ratio is 0.75 to within 2.2e-16.
- **Physics.**
  - The isotropic average ⟨(E1·n)(E2·n)⟩ = E1·E2/3 matches our appendix.
  - The quadratic map's invariance to the current ratio is the product law.
  - The interface factors are 1.79/0.40 ≈ 4.5 for the envelope and its square, ≈ 20, for the second-order maps.
- **Literature.** The steering direction was checked against the Violante 2023 full text (PMC10620081). Their 1:3 condition (1 mA on e1–e2, 3 mA on e3–e4) "steered the location with the largest amplitude to the Ant region", which agrees with Ricardo's anterior envelope shift.
- **Figure reproducibility.** Re-running `make_fem_fig.py` locally gives a PNG 7 px shorter. The PR pins matplotlib 3.11.0 and this machine has 3.10.7, so the difference is not a defect.

## Stale text outside the placeholders (draft19 lines)

- **l. 732:** "A finite-element comparison ... can quantify this reweighting." This should now point to §4.5. At 1:1 the real head gives envelope 1.22 against quadratic 1.08 (degree-matched), which is much milder than the illustrative 40×.
- **Discussion, l. ~2086–2100 (Violante paragraph):** add the head-model result. Envelope steering is anterior, matching Violante's report; the beat cannot move; 𝓘 moves posterior. If detection were square-law, the 1:3 condition would not steer the beat at all. The phrase "a spatial beat measurement ... is needed" still stands.
- **Table, l. ~2258:** "The realistic-montage ... comparisons remain proposed tests" should become: the realistic-montage comparison is §4.5; the physiological beat map remains proposed.
- **CRediT, l. 2386–2388:** "provisional; to be confirmed by R. Salvador" needs his confirmation; add data curation.
- **Abstract:** no mention of the FEM result yet. Whether to add one is a decision for Giulio.

## Figure nits

- **Panel (e):** the legend gives M[A²/2] as red solid, but the raw quadratic line is drawn in gray at 1.167. Only the degree-matched line is red.
- **Panel (f):** the quadratic zero line is the black axis line, not red.
- **Panel (g):** the envelope's raw and degree-matched bars are identical. That is correct for a first-order map, but the hatched duplicate could be dropped.

## Ricardo's four post-package points

1. **Detector compartment fixes the projection direction:** AIS laminar, nodes longitudinal, terminals isotropic; own-optimal is an upper bound. Fits §2.2 (access).
2. **Measured field orientation:** 58–77° from the long axis and 21–35° from mediolateral. The long axis is the axis the focus moves along, not the field direction. With the carriers 7–14° apart there is no stable balance axis.
3. **Interface brightening:** about 4.5× for the envelope and about 20× for the second-order maps. Add a caption line and link it to the boundary-maximum result in §2.6.
4. **Limitation:** σ'' is evaluated at the population operating point, not at the AIS potential.

**Montage optimization per detector hypothesis:** follow-up, outside this paper.
