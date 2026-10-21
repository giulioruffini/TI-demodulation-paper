# Joint plan for the journal article's prose and placement (Klaus + Kaiti, 2026-10-21)

Reconciles notes/2026-10-21_klaus/prose_structure_review.md (6c0e23a, bf58c1a) with
notes/2026-10-21_kaiti/prose_structure_review.md (76aca88). Bounded to the items in those notes.
No manuscript edits; for Giulio's decision.

## Shared verdict

Clear locally, not succinct overall. Current count 14,977 words (13,332 text + 227 headings +
1,418 captions, math excluded; Kaiti's script) against JNE's normal 12,000. The repeated
explanation of access / source / response, interleaved with procedure and qualification, is the
structural problem. A content-preserving first pass is agreed; its word saving is measured after
the pass, not promised before.

## First pass, agreed (retentions per Kaiti's tables)

1. Procedure to the supplement: FEM electrode recipe, solver and recovery settings, mesh counts,
   atlas/tissue/focus-fraction sensitivities (P1); per-run step/window catalogue and vectorized
   implementation (P2); AM/two-tone agreement values as one supplement table (R7). Main text
   keeps subject, montage, conductivities, current convention, fixed projection, ROI/reference
   definitions, degree matching, focus definition, integrator and convergence criterion, the
   lock-in mean-subtraction sentence, and the sentence that displacement directions persist
   across all tested choices.
2. Auxiliary derivations to the supplement: full harmonic Fourier series, mixed-family inversion
   and branch footnote (P4); envelope-norm proof and orientation-average derivation (P5).
   Main text keeps the 1/5 ratio, the vanishing weak-quadratic ratio, amplitude laws, network
   correction, the one-line subharmonic identity with all uniformity assumptions, the beat
   product's unrestricted Laplacian, and the beat-cancels/intensity-remains outcome.
3. Repeated explanation removed, one home each: stages defined in the Introduction, synthesized
   in the Conclusion, Discussion opener keeps only the prior-work comparison (R1); access
   calibration consolidated in 2.7/5.1 with the Intro assumption, the 2.2 AIS qualification and
   the measured/assumed distinction at Table 2 kept (R2, R3, P6; Table 2 stays in the article);
   one numbered receiver equation in 2.6, a short spatial statement with signed projections in
   2.3 (R4, C1); 5.3 reduced to implications and scope (R5); harmonic logic once in Theory,
   implementation in Methods, off-resonance example with the test (R6); FEM numbers once in 4.4
   as a table, 5.2 keeps only the mean-map ordering (R8, C3); 2.5 holds the matching conventions
   and 2-5%, 5.4 names the total-peak convention and cites 2.5 (R9); applied-field/source/response
   distinction stated once (R10); vocabulary definitions at first use, criteria in App. F (R13,
   P3); C2 prose shortened, no new display; 4.9 internal repetition and 2.9 adjacent sentences
   merged; Intro final paragraph reduced to the model progression; 3.4 names which procedure
   gives which diagram; 3.3 uses the literal reference definition (Kaiti's additions).
4. tDCS/tACS comparison becomes its own Theory subsection (P5).
5. Main notation appendix stays in the article (Giulio, October 6).

## Resolved after discussion

- R11 cutoff: one-clause qualification stays beside the weak-drive result and in the caption;
  the numerical cutoff range moves to the supplement table (Kaiti's version adopted).
- R12/P7 equations: Eqs. 17-18 (MPR with its quadratic voltage mixer, F(Q)) stay in Theory;
  Eq. 19 is stated in words there with the display in App. B (Klaus concedes the mechanism
  argument). The full PING system (Eq. 22) is a separate optional move, below.
- P8 bound: compact statement of the 0.348 supremum, its class and the QIF exclusion stays;
  threshold-shape detail joins App. D (Kaiti's version adopted).
- P9, P10: shorten, do not delete; evidence cells keep observation + interpretive limit +
  citation (Kaiti's version adopted).

## Decisions for Giulio

D1. Violante block (5.2): both of us now recommend removing the duplicated displacement values
    and keeping the mean-map ordering and qualifications; shortening it was deferred on
    October 20, so it needs your yes.
D2. Full PING system (Eq. 22) to App. B, with E/I coupling and forcing definitions kept in
    Methods: optional; saves ~150 words of main text.
D3. Vieira's numbers (footnote 5) to the supplement, with the unmatched-polarization statement
    kept in 5.4: new placement choice.
D4. Appendix and supplement layout, agreed (Kaiti ac246f4, IOP policy verified by both):
    article appendices = A notation; B model equations and parameters (JR, PING, MPR) plus a
    compact crossover derivation (today's B.2/B.3 core), because Fig. 11 and the dynamic-sign
    claim rest on it; the supplement is topic-organized by stage (access / detection / spatial
    maps / amplification / laminar / vocabulary and settings), takes the extended exponent
    catalogue, the full LaNMM study (a one-paragraph pointer stays in the article), and all
    procedure and sensitivity material; one source, \ifjne routes each block. Article-appendix
    moves do not reduce the article count.
    D4b, the one open difference: the 0.348 memoryless supremum (5.4, App. D, ~600 words).
    Kaiti: if the claim stays, its compact argument is integral and belongs in an article
    appendix. Klaus: the bound supports a Discussion comparison, not a figure or result; keep
    the one-sentence claim in 5.4 and put the derivation in the supplement. Your call.
D5. Length target: aim at the 12,000 norm, or accept IOP's "longer when the content justifies
    it" and stop at the first pass. We recommend the first pass, recount, then decide.

## Process

Kaiti updates planning/tn0484_storyline.tex first, implements the approved pass on
two-tone-validation, rebuilds article and supplement, and recounts; Klaus runs the fidelity and
reference check against the retention lists above. Journal edition only; the TN regenerates.

## Giulio's decisions (2026-10-21 14:55)

"ok, but keep the ping system": first pass and layout approved. D2: the full PING system
(Eq. 22) stays in Methods 3.5, not an appendix. Read as approving D1 (shorten the Violante block,
keep the mean-map ordering), D3 (Vieira numbers to the supplement, unmatched-polarization
statement kept) and D5 (first pass, recount, then decide) as recommended; Giulio to say if D1
should stay deferred. D4b (0.348 bound placement) still his pick; the pass does not wait on it.
