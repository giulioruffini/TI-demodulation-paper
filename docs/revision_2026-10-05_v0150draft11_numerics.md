# TN0484 draft11 — Landau numerical integration

October 5, 2026. This completes the computational part of the Landau correction
split, following the text checkpoint `dc96c25`. Klaus's `139dd74` and `9190b9c`
were cherry-picked as `5336386` and `3173ac6`. The producer, raw grids, summary,
and note from `c91879f` were then integrated; the local figure renderer retains
explicit rate units and the rendered-text check. No manuscript placement changed.
The working edition remains draft11, with one JNE PDF and one redline against
the recorded reading baseline, draft9 `8016065`.

## Findings and their disposition

| Findings | Integrated correction |
|---|---|
| 1, 19 | Track the PING eigenpair continuously from the Hopf. A second mode near 55 Hz dominates the middle of the coupling range; the critical mode dominates at the low end and near the Hopf. The near-Hopf linear exponent is 1.016 over a 5.8-fold damping range, compared with 0.705 over the full sweep. Figure S10, Methods, Results, and the storyline distinguish these ranges. |
| 5, 6, 29 | Retain the AM surrogate for the dense coupling figure but repeat the mean-dependent comparisons with genuine two tones. Figure S11 now uses the two-tone timing cache. TI/tACS ratios differ by at most 2.109% across the grid, reported as at most 2.2%; source-matched ratios become 0.99, 0.93, and 0.90. The two-tone endpoint is attracting in the tested perturbation and long-window diagnostics. |
| 18, 21 | Replace the abstract's monotone growth claim. Beat modulation initially outgrows the mean shift, but rectification of the amplified oscillation produces an additional mean contribution that can grow quadratically in the response. The two-tone modulation/mean ratio rises from 14.5 to 58, then falls to 44. The Results, prediction table, caption, and storyline state that limit locally. |

No finding in the assigned numerical group is rejected. The normalized gain
comparison is described as such, and the finite-amplitude values are not used
to establish an absolute linear-response calibration.

## Follow-ups resolved during integration

The first NMM2 producer did not generate the source-corrected gain or amplitude
comparison used by its plotter. Klaus supplied one producer and raw grids in
`9190b9c`. Its fixed frequency offsets still left six main-sweep maxima and
several amplitude-check maxima on grid edges. The follow-up `c91879f` scales
the search by the linear resonance width and extends an edge maximum until it
is bracketed. Every main and amplitude-check maximum is now interior. Local
parabolic interpolation changes the sampled main peaks by at most 1.287%.
The replacement figure uses the sampled, bracketed values.

The amplitude-2 departure is 10.351%, so the manuscript says within 11%, replacing the original 10% bound. The maximum normalized excess at amplitude 8 is 48.10%.
Reducing 8 to 2 quarters the amplitude and reduces power to one sixteenth;
the initial wording confused amplitude with power. The figure's linear
reference is normalized over 14.5 < J < 16; the amplitude check uses amplitude
2 at J = 15.53. Both normalizations are stated in Methods.

The new carrier source evaluates both factors at the central frequency. Its
network resolvent is exact, but the combined source calculation uses a
nearby-carrier approximation. An independent analytical Jacobian and Hessian
check gives a maximum critical-eigenvalue discrepancy of 1.1e-10 per ms and a
0.033% discrepancy from the finite-difference source calculation. Explicit AM
sidebands change the peak linear gain by less than 0.05%, preserving the 1.016
exponent. Genuine two tones change that coefficient by up to 2.8%, with exponent
1.0155. The manuscript qualifies the approximation rather than calling the
combined source and gain exact.

The two-tone stability result is stated at the tested 50.5 Hz beat. At the
endpoint, the 8 s finite-time Lyapunov estimate is -0.000785 per ms and the
direct perturbation decay is -0.001437 per ms. The positive 1.2 s estimate is
superseded by the longer diagnostic; it is not treated as an instability. The
AM Floquet multiplier of 0.034 over 2 s remains the separate periodic-input
control. These checks do not claim a Floquet calculation for the two-tone run.

## Reproduction and presentation

`code/verify_draft11_numerics.py` reconstructs the quoted ratios from the raw
grids, verifies that the peaks are bracketed, and evaluates the carrier kernels
with analytical derivatives. Its report is
`docs/draft11_numerical_checks_2026-10-05.json`. The complete 26-point two-tone
JR timing sweep was rerun with 18 s settling, 20 s measurement, and a 0.2 ms
step; all voltage lock-ins, rate lock-ins, and means match the supplied cache
exactly. The comparison is recorded in
`docs/draft11_timing_reproduction_2026-10-05.json`.

The figure runner now includes the new producers and their dependencies, and
cache mode renders S10 and S11 without running simulations. Its 12 existing
regression checks pass. The NMM2 engine and timing-engine descriptions no longer
claim that only damping changes or that the mean cannot grow resonantly.
The README's old kHz provenance limitation was also removed: its producer was
already reconstructed and verified in draft2.

Both revised figures were measured and inspected. Their only collision flags
are ticks outside the displayed limits; the rendered figures have no visible
text overlap or clipping. All panel labels and reference lines are described
in their captions, including the two linear-reference normalizations. The
NMM2 rate axis now states Hz. No original simulation cache was changed.

The final JNE article has 36 pages; private TN and supplement validation builds
have 54 and 20, the storyline 10, and the fixed-baseline redline 38. All five
builds have zero errors, undefined references, overfull boxes, or duplicate
labels. The rendered abstract is identical in the article, TN, and storyline.
All 23 figure labels, 32 equation labels, six table labels, and 60 cited works
are retained in order. `docs/validation_current.json` records the hashes and
inspected pages. The prose checker is clear on the manuscript, abstract, and
storyline; the revision note's only remaining flag is the Markdown table separator.

## Independent fidelity confirmation

Klaus's peer report of October 5 at 20:16 confirms a pass on `b436a9c` for all
his reserved passages: the abstract, timing paragraph and caption, TI/tACS
ratios, NMM2 mode intervals and exponents, amplitude comparison and normalization,
and two-tone endpoint stability. He checked these against the committed producer
outputs and reported no discrepancy. This closes the Landau correction cycle
and the temporary review freeze; the submission and release decisions remain
separate. No manuscript, figure, cache, or code change accompanied this record.

His extended report at 20:18 also confirms the Methods' linear reference,
bracketed peak search, normalizations, and endpoint controls, the prediction
table's timing row, and the S10/S11 captions. He reports byte identity of the
timing cache with his version and of the NMM2 modes cache and JSON with
`c91879f`. The plotted timing values recompute from the cache; the rate-axis
conversion to Hz and the reported rounding agree. No discrepancy or further
action was reported. The detailed values are recorded in
`docs/validation_current.json` under the independent review.

## Length and remaining review

TeXcount reports 13,677 article words and 4,457 supplementary words, excluding
math, bibliography, and front matter. Relative to the text checkpoint, the
numerical integration adds 425 article words and 90 supplementary words. The
new text supplies mode tracking, waveform-specific results, normalizations,
and the missing mean-shift mechanism. No explanation, example, equation,
table, or figure was deleted, and no new placement decision was made. A separate
length review remains on the TODO; scientific qualifications should not be
removed to meet a length target without Giulio's decision.

Klaus's follow-up confirms that the Landau reference check used bioRxiv
10.1101/2025.03.19.644090 v3, Appendix A.1, "PEIX computation." It agrees with
the local author appendix: the index is signed, zero at the inflection, and
approaches opposite signs in the two saturation limits. These were separate
checks of prepublication sources, not verification of the published supplement.
At that stage, confirmation of the published formula remained on Giulio's TODO.
The manuscript definition was unchanged.

At 20:23 Klaus reported a direct comparison with the bioRxiv v3 Appendix A.1
page supplied by Giulio: draft11's PEIX formula agrees to a maximum difference
of $7\times10^{-16}$ over $V\in[-5,20]$ mV. He also checked the normalized-slope,
curvature, and rate-fraction identities used downstream. This closes the
formula-equivalence check; confirmation of the published definition remained open.

At 20:27 Klaus confirmed the definition in the published Neural Computation
supplement supplied by Giulio. Kaiti then inspected Appendix A, pp. 1–2, in the
25-page PDF: the formula and four properties are unchanged. The identity
$4e^{-x}/(1+e^{-x})^2=\operatorname{sech}^2(x/2)$ makes its equivalence to draft11
explicit. The reference copy is filed at `_private/references/neco.a.1537-supp.pdf`;
its SHA-256 and provenance are in `docs/validation_current.json`. The published
PEIX item is closed. No manuscript edit or rebuild was needed.

Author review, missing declarations, and the submission decision
remain pending. No push, Calliope/Zenodo cut, Overleaf synchronization, or coauthor
mail was performed.
