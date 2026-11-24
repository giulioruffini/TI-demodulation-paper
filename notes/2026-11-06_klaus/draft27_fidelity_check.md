# Draft27 reader-flow fidelity check (cc72bad against 8b95e2f)

Scope: meaning, readable continuity, local qualifications, the relocated QIF
values and the scoped 0.348 statement, read from the source diff of the article
and the two supplement modules (`qif_estimate.tex`, `supp_efficiency.tex`), with
the page map of the committed `TN0484_jne.pdf` compared against draft26's. No
manuscript edits, builds, pushes or mail.

## Verdict

No blocker. Every change reads as connected prose, every qualification still
sits beside the claim it limits, every number moved out of Section 4.7 has a
verified home in the supplement, and the 0.348 statement now carries its five
conditions. Four optional suggestions follow, one of them the layout change
Kaiti asked me to identify.

## Verified

- **Introduction findings paragraph.** Four findings replace the list of
  operations; each keeps its scope (weak static detection; pinned JR point;
  QIF mean field at fast carriers; one head model; mean-field equal-RMS
  control). Consistent with Sections 2.2, 4.5, 2.9, 4.4 and 4.7.
- **Section 2.3.** The five-caveat paragraph is now two paragraphs with lead
  sentences: the steady source as the route by which ratio changes can reshape
  the beat (state shifts fall outside the fixed-state argument), and the
  interior-maximum point with Eq. (12). Nothing dropped. The bilinear paragraph
  gains its purpose sentence ("The current-product scaling also holds when a
  detector combines input from several compartments").
- **LPF** expanded at Eq. (8); **equal-RMS** sentence in 2.5 now points to the
  control in 3.6; **Section 2.9** opens with its result under the stated
  conditions (weak carriers, fixed synaptic input).
- **Methods.** "Response terminology." heading on the definitions paragraph;
  the dropped "nor a calibrated AIS transfer" in 3.3 survives three sentences
  earlier ("not a measured AIS transfer"); "J-curve" replaced by "coupling
  sweep" twice; the duplicate §S4 pointer in 3.6 merged into the later one.
- **Section 4.6.** The ridge is placed in the (Δf, η̄) plane of Fig. S8; the
  exponent 1.02 is tied to the 1/γ law.
- **Section 4.7 relocation.** The article keeps, per condition: depth 0.09 and
  +2.8% (A_f = 10, η̄ = 0.85), depth 0.02 and +1.6% (η̄ = 1.5), depths 0.70 and
  0.29 at A_f = 35, the PPC and vector-strength values, and the unconverged
  qualification; δη*_E is defined in words at first use. Moved values and
  their homes, checked in the committed modules:
  - 0.093 (published cutoff), 0.127 and 0.139 (higher cutoffs), mean field
    0.128: `supp_amplification.tex` lines 61 to 65 (S4.7).
  - theta depth 0.156 and the −11.9% population-doubling change:
    `theta_pilot.tex` lines 29 to 45 (S4.8).
  - excursion 1.2, shifts 1.5 and 0.12, threshold 0.286, refined 1.65 and
    +0.032 ms⁻¹: `qif_estimate.tex` (S4.9). Arithmetic: ω_c τ_E = 2π·300 Hz ×
    15 ms = 28.3, so A_f/(ω_c τ_E) = 1.24 at A_f = 35, and the squares are 1.53
    and 0.125, as stated.
- **Discussion.** 5.1 reordered without loss (the calibration sentence became
  "their combined transfer at physiological kHz fields remains unmeasured").
  5.3 gives the single-column reason for the correlation-length sentence. 5.4
  states the 0.348 supremum with balanced TI, matched peak polarization, same
  operating point, carrier-averaged open-loop fundamental amplitudes, bounded
  nondecreasing memoryless transfers, and the QIF exclusion. The dropped
  sentences live in S5: step mixture (`supp_efficiency.tex` lines 7 and 80 to
  82), sharp transition and microvolt width (line 64), second-harmonic ratio
  0.151 (line 78), and the new paragraph on unequal polarizations and
  protocol matching (lines 85 to 87).
- **Code availability.** LaNMM expanded at first use.
- **Floats.** Figs. 9 and 13 moved ahead of their text with [t!]; the 4.6
  heading now follows Figs. 11 and 12; the barrier before the Conclusion
  remains. Page map: Fig. 14 on page 24, Discussion opens page 25, so no
  Results figure drifts into the Discussion.
- **Build state.** No label added or removed; article and supplement logs show
  0 undefined, 0 multiply defined, 0 overfull; 38 + 32 pages.

## Optional suggestions

1. **5.4, the 0.348 sentence** lost its link to the 0.8% two sentences above
   when "For comparison" went. One clause restores it: "By comparison, for
   balanced TI ... supremum of 0.348 ..., so the illustrative 0.8% lies far
   below the ceiling of any static detector."
2. **Introduction.** "The resulting input budget" follows a paragraph that no
   longer mentions a budget; "The input budget implied by these sources" reads
   on.
3. **Source cosmetics.** Three blank lines after the crossover paragraph in
   4.6 (around line 1500).
4. **Layout, identified only.** The 38th page is seven lines of references.
   In draft26 the AI declaration ended page 28 and the references filled pages
   29 to 32 exactly. In draft27 the Discussion grew by a few lines, the
   Conclusion starts lower, the AI declaration spills onto page 29, the
   references end seven lines into page 33, and the appendix rule
   `\renewcommand{\section}{\clearpage\ne@stdsection}` (line 1894) turns those
   seven lines into a page. Letting Appendix A start on the references' last
   page, with the clearpage kept before Appendix B, recovers the page without
   touching type: A's longtable would run from about 0.2 of page 33 to about
   0.7 of page 35, and B would fill pages 36 to 37. Longtable breaks shift on
   the rebuild, so the count needs confirming after the change. Alternatively
   any six-line saving before the declarations does the same.
