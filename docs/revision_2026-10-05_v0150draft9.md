# TN0484 draft9 — DC spatial response and organization

Editing baseline: draft8, `b6fc18b`, which already integrates the single abstract and table explanations. The review redline uses `19b8f38`, the draft8 reading version identified in Giulio's October 5 instruction. These baselines serve different purposes: word counts compare the immediate source before this pass, while the redline includes all changes since the reading version.

## Revision plan and content retention

The storyline remains the organization reference. The Introduction follows access, detection, and amplification; Theory derives the local mixer before recurrent gain; Methods specifies the measurements; Results tests the stages and distinguishes weak forcing from a changed dynamical regime. Discussion interprets those results physiologically. The seven Theory subsections, LaNMM Methods, and all figures retain their positions pending Giulio's placement decisions.

Consolidate repeated derivations and explanations at their existing homes:

- The two-tone DC and beat sources remain in Eq. (9); add the spatial consequence after the reweighting example in Section 2.4. Preserve the distinct AM-surrogate DC, dynamic-QIF source, stability calculation, and mean-rate readout.
- Explain carrier-to-rate scaling beside Table 1, keeping the quadratic-term orders before it and the distinction between the uncoupled DC coefficient and finite-frequency network response after it.
- Define the envelope excursion once in Section 2.4; Discussion uses that definition to interpret dose maps without repeating the algebra.
- Keep measured and assumed access times beside Table 2. Discussion retains the additional PWM-TI model, area-independent RC argument, and physiological interpretation.
- Keep numerical results and qualifications in Results and self-contained figure captions. Shorten surrounding repetitions of Theory and Methods.
- Consolidate the laminar extension's repeated scope statement into its opening, preserving its amplitude range, sigmoid voltage scale, and comparison with the perturbative JR test.

No explanation, example, qualification, result, equation, figure, or table is approved for deletion in this pass. Optional removals will be listed separately and remain in the manuscript.

## DC argument and its scope

The new paragraph follows the reweighting example in Section 2.4. One sentence in the Discussion links it to the equal-RMS control and the operating-state shift. Klaus was asked to check the scope independently; no reply had arrived when this record was prepared.

For distinct carriers, the static quadratic expansion gives

\[
A_{\rm DC}=\frac{\Sigma''}{4}(\varepsilon_1^2+\varepsilon_2^2),\qquad
A_\Omega=\frac{\Sigma''}{2}\varepsilon_1\varepsilon_2.
\]

Carrier averaging retains the difference-frequency cross term. Averaging over many beat cycles removes it. Where the DC source is nonzero, its magnitude bounds the generated beat amplitude by the arithmetic–geometric mean inequality. This is a source comparison before the different network gains at zero and beat frequency; it does not bound the final beat/DC output ratio.

The example uses the polarization mean square, \(\mathcal I=(\varepsilon_1^2+\varepsilon_2^2)/2\), not the signed DC source itself. Its superficial/deep ratio is \(50.5/0.25=202\). The beat/DC source ratios are \(20/101=0.1980198\ldots\) and one. The source's sign follows curvature; reversing carrier polarity leaves its mean unchanged. A common access factor cancels from the local ratio. A spatially varying common factor can still change the superficial/deep contrast.

In a homogeneous, isotropic, source-free conductor, each potential satisfies \(\nabla^2\phi_j=0\). Its field components and any spatially fixed projection \(\varepsilon_j=\boldsymbol\lambda\cdot(-\nabla\phi_j)\) are harmonic. Consequently,

\[
\nabla^2\mathcal I
=\sum_j\left(|\nabla\varepsilon_j|^2+\varepsilon_j\nabla^2\varepsilon_j\right)
=\sum_j|\nabla\varepsilon_j|^2\ge0.
\]

For the unprojected field sum, the corresponding identity is \(\nabla^2\sum_j|\mathbf E_j|^2=2\sum_j\|\nabla\nabla\phi_j\|_F^2\ge0\). The maximum principle excludes a strict interior maximum of the intensity on a bounded homogeneous region; a constant map is the degenerate case. Conductivity interfaces are region boundaries. This does not imply a universal global maximum at the scalp or exclude a response peak caused by physiological weights. A constant field multiplied by a positive curvature proportional to \(e^{-|\mathbf x|^2}\) already supplies a counterexample to the latter extension.

The absence of cross-frequency cancellation does not prohibit coherent montage shaping within each carrier. Nor is the sum of intensities generally the same map as a single same-frequency field formed by coherently summing both montages. A single carrier matches the local static quadratic mean when its RMS polarization matches; field-RMS matching alone is insufficient if access differs between frequencies.

With isotropic unit orientations and orientation-independent coefficients, \(\langle n_i n_j\rangle=\delta_{ij}/3\). The squared projections average to \(|\mathbf E_j|^2/3\), and their product to \(\mathbf E_1\cdot\mathbf E_2/3\). Orthogonal fields therefore cancel the averaged beat while retaining DC. Its magnitude relative to a fixed-orientation population depends on the chosen orientation. Beyond smooth quadratic detection, neither a universal superficial DC map nor a universal minimum-amplitude beat law follows; the existing step-detector example explicitly gives a different response.

## Changes and retained locations

| Affected passage | Consolidation | Retained content |
|---|---|---|
| Introduction ending | Remove the repeated population-access contribution statement | Access paragraph and model ladder in the same Introduction |
| Section 2.3 before Table 1 | Replace a second carrier/beat explanation with the quadratic-term orders and table introduction | Full row-by-row explanation after Table 1; fixed-voltage coefficient versus finite-frequency susceptibility retained |
| Section 2.4 harmonic test | Shorten the lead-in and interpretation | Higher-order harmonic, gain correction, resonance condition, numerical example, and off-resonance/deconvolution options |
| Methods | Condense repeated lock-in wording and NMM2 model introduction | Quadrature estimator, finite-window/DC cautions, model equations, variables, parameters, and sweep qualifications |
| Results 4.1–4.2 | Remove repeated bifurcation orientation and shorten the resonance account | Figure 2 and Methods; all three 0.23/0.43/0.70 mV peaks retained in Results |
| Results 4.4 | Consolidate controls and refer to their self-contained caption | 1.99 slope, 634-fold reduction, 1.34/0.0021 mV amplitudes; surrogate ratios 1.0000 and 0.988 in Figure 6, the latter equivalent to the previous 1.2% difference; recurrent near-Hopf limitation retained |
| Results 4.5 | Start with the mean-field result instead of reintroducing its full model | Methods gives the equations, Hopf, and input convention; diagonal resonance ridge and 1.1% four-point approximation limit remain in Results |
| Results 4.6 | Shorten repeated capture definitions and concluding model contrast | Definitions in Methods and Appendix F; all response ratios, nonlinear qualifications, endpoint multiplier, and settling check unchanged |
| Discussion | Use the existing envelope-map derivation; consolidate repeated access and effective-response statements | Section 2.4 map; Section 2.6 and Table 2 measured decay; PWM-TI, field-pulse, molecular-field, RC, physiological, efficiency, and human-data qualifications retained |
| Conclusion | Condense the same synthesis | Candidate access, calibration, weak-input conditions, time-scale limit, one filter per process, product law, shared linear gain, and finite-amplitude departure |
| Appendix E opening | Merge repeated scope paragraphs | Carrier and amplitude ranges, sigmoid scale, low-amplitude JR comparison, alpha/gamma populations, both field-free regimes, and code location |

The section order is unchanged. No result, explanation, or example has been moved out of the manuscript. The separate proposed-removals list recommends no scientific deletions and preserves the pending placement decisions.

## Validation and counts

TeXcount is recorded by `code/count_section_words.py`; it counts text, headings, and captions, with equations and references excluded. The raw before/after categories are preserved in `word_counts_draft8_to_draft9.json`. The counts below are source prose counts, not a claim about a journal's counting convention.

| Section | Before | After | Change |
|---|---:|---:|---:|
| Abstract | 275 | 275 | +0 |
| Introduction | 849 | 822 | -27 |
| Theory | 3996 | 4117 | +121 |
| Methods | 2537 | 2448 | -89 |
| Results | 3785 | 3383 | -402 |
| Discussion | 1460 | 1353 | -107 |
| Conclusion | 267 | 230 | -37 |
| Code and data availability | 96 | 96 | +0 |
| Acknowledgments | 30 | 30 | +0 |
| Competing interests | 26 | 26 | +0 |
| Author contributions | 71 | 71 | +0 |
| Declaration of generative AI and AI-assisted technologies in the manuscript preparation process | 62 | 62 | +0 |
| Appendix: Notation and units | 721 | 721 | +0 |
| Appendix: Simulated models: equations and parameters | 168 | 168 | +0 |
| Appendix: The cubic Hopf normal form lacks a quadratic mixer | 146 | 146 | +0 |
| Appendix: Efficiency of a memoryless transfer against a direct in-band drive | 561 | 561 | +0 |
| Appendix: Extension: the laminar column at low carriers | 957 | 860 | -97 |
| Appendix: Vocabulary and metrics | 293 | 293 | +0 |
| Appendix: Supplementary figures | 1303 | 1303 | +0 |

The article count falls from 13,454 to 12,913 words (541 words, 4.0%); the supplement falls from 4,149 to 4,052 (97 words, 2.3%). The total reduction is 638 words despite the new DC calculation. The abstract is unchanged. These totals include prose in headings, captions, and declarations; equations and references are excluded.

All 35 section/subsection headings, 23 figure labels, 32 equation labels, six table labels, and 60 cited works are retained in order where applicable. Equation, align, figure/caption, tabular, and notation-table contents are unchanged. The new DC derivation uses inline equations and does not renumber existing equations.

The JNE, TN, and supplement build with no errors, undefined references, or overfull boxes: 34, 51, and 19 pages. The current redline is 35 pages against draft8; the updated storyline is nine pages. The TN and supplement were built privately for validation, without creating additional working reading copies. Rendered pages covering the abstract, Table 1, DC paragraph, Discussion boundary, Conclusion, redline addition, and storyline were inspected. Rendered abstract text matches across JNE, TN, and storyline. No numerical simulation or cache was changed or rerun.

Commands: `./build.sh jne`; private TN/supplement builds using the same source and switches; `python3 code/build_jne_redline.py`; `python3 code/count_section_words.py --json docs/word_counts_draft8_to_draft9.json`; prose checker on the manuscript, shared abstract, and storyline; content-inventory and rendered-abstract checks recorded in `docs/validation_current.json`.

Release holds remain: no push, Calliope/Zenodo cut, Overleaf synchronization, or coauthor email.
