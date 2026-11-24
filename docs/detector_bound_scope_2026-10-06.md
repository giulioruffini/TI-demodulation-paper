# The step bound extends to monotone memoryless transfers

October 6, 2026. Follow-up to Klaus's 19:44 paragraph suggestions, checked against draft16 `e07b44a`, Appendix `app:bound`, and the existing `code/threshold_bound_check.py`. No manuscript or PDF was changed during the combined fidelity review.

## The extension follows from positive step weights

The comparison fixes one operating potential v* and one transfer function g of membrane potential v. Balanced TI tones each have local polarization amplitude ε; the direct in-band sinusoid has amplitude 2ε. Thus their peak polarizations match. The TI output is averaged over the fast carrier, and neither output is fed back into the input.

A bounded nondecreasing transfer g is a constant plus a positive mixture of threshold steps: g(v) = g(−∞) + ∫ H(v−θ) dμ(θ), where H is the unit step, θ is its threshold, and μ is a nonnegative weight measure. Let Aθ be the signed beat coefficient of a step and Bθ its direct-drive fundamental. For the normalized threshold offset β = (θ−v*)/(2ε), Bθ = (2/π)√(1−β²) ≥ 0 when |β| < 1. Both coefficients vanish outside that interval. The TI coefficient changes sign between positive and negative offsets; the denominator does not.

Write A[g] and B[g] for the corresponding signed coefficients of g. Fourier coefficients are linear in the transfer. If B[g] > 0, the triangle inequality therefore gives

    |A[g]| / B[g]
      = |∫ Aθ dμ| / ∫ Bθ dμ
      ≤ ∫ |Aθ| dμ / ∫ Bθ dμ
      ≤ supθ |Aθ| / Bθ.

When B[g] = 0, the beat coefficient also vanishes and the ratio is undefined. The positivity of the direct coefficient is the condition that makes this extension valid; linearity alone would not suffice.

The class-wide reduction is analytic. The value of the step optimum is numerical. Rerunning the existing producer gave β = 0.523163, a ratio of 0.347928 by both quadrature and the elliptic expression, and a second-harmonic ratio of 0.15087. This is not a certified global numerical bound. The carrier average is part of the comparison; the result does not assert an identical finite-window ratio for every carrier pair.

My earlier restriction to the logistic family was unnecessarily narrow. Appendix `app:bound` already contains the positive-mixture argument, and the Landau report had checked it. The next Discussion edit should agree with that broader result while retaining the matching, monotonicity, memorylessness, carrier averaging, and open-loop assumptions. A bound on this class is not a bound on every cellular detector or every TI response statistic.

## Consequences for the proposed endings

Suggestions A and B are consistent with draft16: PLV is not generated drive, the 0.8% figure is conditional on an assumed JR access budget, and a larger linear circuit gain multiplies both inputs. The existing wording preserves these distinctions.

Suggestion C needs a narrower final implication. Increasing the common matched peak polarization cannot exceed the optimized class bound: the threshold offset and transfer width scale with that polarization. A larger or unequal actual polarization can explain an apparent experimental violation only when the assumed matching at the membrane fails. It is not an exception under true matched-polarization conditions.

Approaching the optimum requires the active transfer transition to become sharp relative to the input excursion, beyond the smooth weak-input expansion. The quoted 3–17 μV widths come from the logistic scan at illustrative per-tone polarizations of 0.02–0.1 mV; they are not a universal width condition for all monotone transfers.

Proposed closing sentences for the next manuscript checkpoint:

> The step-mixture argument extends the numerically estimated ceiling of 0.348 to bounded nondecreasing memoryless transfers, for this carrier-averaged, matched-peak, open-loop comparison. A generated-drive ratio above it at verified matched local polarization would fall outside these assumptions. Unmeasured differences in polarization can instead invalidate the experimental matching; a PLV ratio does not measure this drive ratio.

Retain the existing explanation of the sharp-threshold limit and its illustrative widths. No new simulation is needed; the manuscript remains at the reviewed commit until the combined fidelity report arrives.

Integrated in draft17 after the combined draft16 fidelity report; see `revision_2026-10-06_v0150draft17_fidelity.md`.

Klaus independently agreed with all scope qualifications at 20:27, reviewing `dc8e3c6`. This closes the conceptual scope question; the later draft17 integration check remains separate.
