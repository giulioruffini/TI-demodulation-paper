# Which interface ratios the conductivity ratio bounds — analytic check for Kaiti

Klaus, 2026-10-20, requested by Kaiti (14:05). Base 7b472cb. Script: `interface_bound_check.py`
(this folder), 20,000 random interfaces, r = 4.5, direction grid of 4,000 points.

## Setup

Unit interface normal ν, conductivities σ_high and σ_low, r = σ_high/σ_low > 1. Tangential continuity
and normal-current continuity give E_low = A E_high with A = I + (r − 1) ν νᵀ. A is symmetric with
eigenvalues {1, 1, r}, so 1 ≤ |Av|/|v| ≤ r for every v.

## Results

1. **Magnitude.** |E_low|/|E_high| ∈ [1, r]. For second-order maps built from magnitudes, [1, r²].

2. **Maps at their own orientation maximum.** Write M(E1, E2) = max_n f(n·E1, n·E2) with f homogeneous
   of degree k and even in each argument (envelope excursion 2 min(|a|,|b|), k = 1; quadratic excursion
   2|ab| and 𝓘 = (a² + b²)/2, k = 2). Since A is symmetric, n·(A E_j) = (A n)·E_j = |An| m·E_j with
   m = An/|An|, so f(n·AE1, n·AE2) = |An|^k f(m·E1, m·E2) ≤ r^k M(E1, E2); maximizing over n gives
   M(AE1, AE2) ≤ r^k M(E1, E2). Lower bound: take n ∝ A⁻¹m* for the high-side maximizer m*; then
   |An| = 1/|A⁻¹m*| ≥ 1, so M(AE1, AE2) ≥ M(E1, E2). Own-maximum ratios lie in [1, r^k].
   Numerically the worst ratios over 20,000 cases are 4.500 (magnitude), 4.528 (envelope), 20.252
   (quadratic) and 20.250 (𝓘) against r = 4.5 and r² = 20.25; the 0.6% overshoots are the direction
   grid, not violations.

3. **Fixed projection direction.** n·E_low = n·E_high + (r − 1)(E_high·ν)(n·ν). The ratio
   (n·E_low)/(n·E_high) is unbounded and can be negative, because the high-side projection can vanish
   by cancellation between the normal and tangential parts. Counterexample: ν = ẑ, E_high = (1, 0, 0.2),
   n ∝ (−0.2, 0, 1): n·E_high = 0, n·E_low = 0.69, while |E_low|/|E_high| = 1.32. The envelope-maximizing
   n* of the low (gray-matter) side, held fixed on both sides as in Ricardo's table, is such a direction:
   over the random ensemble the fixed-n* ratio exceeds r (envelope) or r² (second-order maps) in 11–19%
   of cases and falls below 1 in 0.2–2.4%. (The random ensemble has isotropic fields and large normal
   components; it shows that no bound exists, not what the hippocampal distribution looks like.)

**Consequence for Ricardo's text.** "These ratios bound the brightening of a map from above" holds for
the field magnitude and for each map at its own orientation maximum, not for the fixed-n* jumps his
table reports. Those are measurements with no a priori bound; that their interquartile upper ends
(≤ 2.07) sit below r and r² is a finding, not a theorem. Suggested wording: r and r² bound the
magnitude and the own-maximum maps; the fixed-direction jumps are reported as medians with
interquartile ranges.

## Two corrections to my 7b472cb note, accepted from Kaiti

- **Median inversion.** The j ≈ 2.54 obtained from the marginal medians (0.20 on the CSF side, 0.46 on
  the gray-matter side) assumes a common node with a continuous tangential component; medians of two
  marginal distributions do not compose, so it is an illustration, not a measured median normal jump
  and not a one-sided error bound. The statement "measured jumps are a resolution-limited lower bound"
  is withdrawn from the check note and from the Gmail draft. A bound of that kind would need the paired
  per-node normal and tangential components on both sides and a mesh-convergence check of the jump
  statistic; the draft now asks for those, and otherwise keeps Ricardo's "not resolved at this mesh
  resolution".
- **Laminar fraction denominator.** Ricardo's fractions 0.29 (envelope), 0.11 (quadratic) and 0.12 (𝓘)
  are relative to each map's own orientation maximum at the node, not to the envelope-maximizing n*
  used in Fig. 8. My item 4 and the first Gmail draft said "that the envelope-maximizing direction
  reports"; corrected to "available at each map's own optimal orientation". Relative to n* the beat and
  𝓘 fractions would be larger than 0.11 and 0.12, since those maps along n* are already below their
  own maxima.

## Addendum (14:10): the GM-side envelope-optimal n*, Kaiti's open case

With n* the envelope maximizer of the low (gray-matter) side, held on both sides, the envelope map's
numerator is M(L1, L2), its own maximum on the low side, and the denominator 2 min(|n*·E1|, |n*·E2|) is
at most M(E1, E2) ≤ M(L1, L2). So the envelope ratio along this n* is ≥ 1 exactly, with no upper bound
(numerically: minimum 0.994 over 20,000 cases, the shortfall being the 4,000-point direction grid;
exceedances of r in 19%). For the quadratic and 𝓘 maps along the same n* neither bound holds, since n*
maximizes neither map on either side (2.1–2.4% below 1, 11% above r²). Kaiti's two-dimensional
counterexample (r = 4.475, E_high = (1, 1), ν = (1, 0), n = (1, −0.9)/√1.81) reproduces: projection
ratio 35.75, magnitude ratio 3.242 < r.
