# Draft26 fidelity check (Kaiti's 0fbac10 against draft25 at 0d80796)

Scope: semantic fidelity and reference continuity of the source diff, with the
moved operating-state paragraph, the merged JR Methods and Results, and the
merged MPR appendix read in full, and the FEM additions checked against
`code/fem_quadmaps.json`. Rendered pages 8, 18, 19, 20, 28 and 37 of the
committed `TN0484_jne.pdf` were inspected. No manuscript edits, builds, pushes
or mail.

## Verdict

The science is preserved and every cross-reference resolves. No blocker. Four
compressed passages lost the explanation that made them readable on their own;
restoring each costs one clause. Two further nits.

## Verified

- **FEM values.** Table 3's mean contrasts (ROI mean over reference p95) are
  0.807/0.583, 0.607/0.607 and 0.471/0.536 in the JSON, printed as 0.81/0.58,
  0.61/0.61 and 0.47/0.54. The restored degree-matched 1:3 mean-square contrast
  is sqrt(0.903) = 0.950, printed 0.90 (0.95). The caption now defines both
  contrast kinds correctly. The table renders in width on page 19 with seven
  columns and no overfull box.
- **Tail sentence.** "The envelope nodes above the reference 95th percentile
  have an anterolateral centroid and are 52% white matter, compared with 25%
  across the ROI": `upper_tail_1to1.env` gives 93 of 180 nodes (51.7%), ROI
  394 of 1,568 (25.1%), centroid 8.6 mm anterior and 5.8 mm lateral of the ROI
  centroid. Descriptive, no causal attribution, as agreed.
- **Section 5.2.** The +24% sentence and its neighbors are untouched.
- **Fig. 9(f).** "colors as in (e)" present; rendered caption on page 20.
- **IXI.** Acknowledgment sentence on page 28; code-availability clause states
  the prospective CC BY-SA 4.0 data license with IXI attribution; README and
  `docs/fem_portable.md` say the same; `LICENSE` unchanged.
- **Operating-state relocation.** Every element of the deleted subsection
  survives: sign change across the inflection and vanishing at the inflection
  and in the saturated tails (now in the sign paragraph of 2.5), the PEIX
  definition, sign convention and pointer to Appendix B.1, the list of state
  changes that scale or reverse the static source, the absence of a universal
  PEIX rule for dynamic detectors, and the need to measure recurrent gain in
  state sweeps. Page 8 reads as one argument. `sec:opp` resolves to 2.5 and is
  not referenced anywhere.
- **JR Methods and Results.** The relocated protocol keeps the pinning rule,
  Jacobian, surrogate versus two-tone roles, tACS control and extended-window
  controls. The merged Results keep 30-fold, 1/gamma, C* about 137, 13.2-fold
  (26 to 339 mHz), 4.4-fold (-1.8 to -7.7 mHz), below 0.2%, 1/gamma^2, 0.143,
  0.90 to 0.99 and the saturation and matching conventions. Paragraph headings
  render on page 20. `sec:timing` and `sec:tacs-results` resolve to 4.5; the
  supplement's "§sec:timing to sec:qif" range in `prediction_evidence.tex`
  therefore prints 4.5 and remains correct.
- **MPR appendix.** `app:mpr-coefficients` and `app:mpr-mixing` both resolve to
  B.3; the supplement's reference in `supp_detection.tex` lands there; the
  mixing label is otherwise unreferenced. Content retained in full: unit
  convention, F as the excitability average of sqrt(q)/pi, q and eta,
  kappa_DC (B7), physical shift, eigenvalues, Jacobian, phasor, b2, mean
  correction, limits (B8), their interpretation, omega_z and the
  parameter-dependent carrier classification. Equation numbers B7 and B8 are
  unchanged. Page 37 reads in the order coefficient, derivation, limits.
- **Harmonic consolidation.** Theory carries the threshold-detector caveat,
  Methods the estimator and its assumptions, Discussion the off-resonance
  design; the predictions table dropped only its repeat.
- **Build state.** No label added or removed in the article or appendix
  sources; article log 0 undefined, 0 multiply defined, 0 overfull, 37 pages;
  supplement log the same, 32 pages.

## Restore (one clause each)

1. **JR Methods, relocated paragraph (line 1031).** The lead sentence "The JR
   sweeps vary coupling while keeping detection fixed" was dropped, so the
   paragraph now opens "For each connectivity C, we solve for p(C)..." before
   any coupling sweep has been introduced in Methods. Suggested: "The coupling
   sweeps vary C at fixed detection: for each C, we solve for the external
   drive p(C) that holds..." In the next paragraph "the timing comparison" is
   now an orphan name, since no heading uses "timing"; "the two-tone comparison
   of modulation and mean" names what follows.
2. **Results 4.5, tACS paragraph (line 1419).** The reason that matched drives
   give matched outputs, "TI and tACS share the same linear amplifier", went
   with the deleted heading. Suggested: "TI and tACS share the linear amplifier,
   so at a common state matching their generated in-band drives matches their
   linear outputs; resonance alone gives TI no efficiency advantage."
3. **Methods 3.2 opening (line 911).** "At fixed coupling and operating state,
   we measure the fundamental and second harmonic across an amplitude sweep"
   no longer says what the sweep tests. Suggested ending: "...across an
   amplitude sweep, which separates linear from quadratic scaling
   (§sec:transduction)."
4. **Fig. 10 caption (line 1391).** Panels (a,b) now say the response grows
   "on the stable-focus side of C*" without saying what varies, and panel (c)
   lost "before saturating". Suggested: "(a,b) The response grows and its
   resonance sharpens as C approaches C* on the stable-focus side (gamma > 0).
   (c) Rate-to-voltage gain A_Omega/A_open (mV s) follows 1/gamma (dashed)
   before saturating." The caption then stands alone, as the text does.

## Nits

- Line 577: "Dynamic detectors have their own coefficients and susceptibilities"
  lost "state-dependent", which is the point of the sentence.
- Line 674: the general statement "matched sources give matched leading circuit
  responses" is now implicit in "share the transfer". Acceptable.
- A doubled blank line follows the relocated JR paragraph (line 1043).

Word counts and the preservation script were not rerun; the label, citation
and log checks above are independent.
