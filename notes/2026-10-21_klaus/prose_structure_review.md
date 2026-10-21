# Journal article: succinctness, repetition, placement (Klaus read, 2026-10-21)

Read: TN0484_jne.pdf at 62772c7/4132ada, 44 pp, all sections. Three questions from Giulio: is it
succinct and clear; are repetitions minimal; does everything belong in the main paper.

## Verdict

Clear sentence by sentence (the October 20 legibility passes hold), but not succinct and not
minimal in repetition. The main text is ~12.9k words plus ~1.3k in captions (TeXcount, draft21,
before the tDCS comparison added ~0.5k); JNE's norm is "not normally more than 12 000 words
(14 journal pages)". The central claims are each stated three to five times, so the paper reads
longer than its content. About 3-4k words can move to the supplement or be merged without
removing any result. Nothing below is applied; every relocation needs Giulio's approval.

## Repetitions (where, how many times)

R1. Three stages + their tests: Intro l.129-134 and l.189-198, Results opener (4.0), 5.1 opener,
    Conclusion, Table 3. Keep Intro (definition) and Conclusion; cut the Results and 5.1 openers.
R2. Fast-access calibration caveat: Intro, 2.2 end, 2.7 (twice), Table 2, 5.1 (two paragraphs),
    Conclusion. Six places; Table 2 + one sentence in 2.7 + Conclusion suffice.
R3. Access time-constant numbers (16 ms, 1 ms, 0.2 ms, 0.4/1 ms, 0.7 us) and the 1e-4..1e-6
    attenuation: 2.7 prose, Table 2, 4.2, 5.1. Table 2 carries all of it.
R4. Receiver equation stated twice: Eq. 10 (2.3, with position) and Eq. 14 (2.6, with access)
    are the same product G x D x e1 e2. Merge into one, in 2.6.
R5. TI/tACS shared amplifier and "resonance gives no efficiency advantage": 4.7 first sentences
    and 5.3 second paragraph say it in the same words; Conclusion again.
R6. Harmonic test logic (1/5 ratio, square law vanishing, threshold class, network correction):
    2.4, 3.2, 5.6 first paragraph, Table 3 row. Four places.
R7. Surrogate-vs-two-tone agreement checks reported in 4.3 (Fig. 7d), 4.6, 4.7, 4.8, Fig. 10
    caption: five separate verifications in the main text. One sentence + a supplement table.
R8. Current-ratio result numbers (2.5 mm, 24%, 4.5 mm, 45%, 25%): 4.4, 5.2 (restated), Conclusion,
    Table 3. The 5.2 restatement can cite 4.4.
R9. 2-5% comparison: 2.5 derivation + numbers, 5.4 restates numbers, then adds the 0.8% matched-
    peak and the 0.348 bound. Three conventions in two places; 5.4 should state one and cite 2.5.
R10. "DC-like refers to the detected source, not the field" and "The applied field has no DC
    component": 2.5, ten lines apart.
R11. QIF cutoff non-convergence: 3.6 last paragraph, 4.9, Fig. 13 caption. One place (3.6).
R12. MPR/PING model equations: 2.9 (Eqs. 17-19), 3.5 (Eq. 22), App. B. Theory needs only F(Q)
    and the slow-synapse condition; the equations belong in Methods or the appendix, once.
R13. Vocabulary: 3.8 in Methods and App. F "Vocabulary and metrics" in the supplement.

## Placement: candidates for the supplement (estimated main-text saving)

P1. 3.3 head model: electrode recipe, mesh counts, solver/residual, SPR recovery, 10-10 montage,
    atlas-label and tissue sensitivities, focus-fraction sensitivity -> supplement; keep subject,
    montage, conductivities, projection direction, ROI, the two statistics (~700 of 1100 words).
    With it, the 4.4 sensitivity paragraph (atlas, radial, 32 combinations) -> supplement table.
P2. 3.4 step-size catalogue and the vectorized-sweep sentence; 3.2 lock-in DC-leakage paragraph
    (~250).
P3. 3.8 vocabulary -> merge into App. F (~165).
P4. 2.4 harmonic ladder, Eq. 12 and its footnote -> supplement; keep the three-class statement
    (~200).
P5. 2.5: envelope-mean subharmonic paragraph and isotropic-orientation averages -> supplement
    (~200). Promote the tDCS/tACS comparison to its own subsection (it is now in the abstract).
P6. 2.7 prose on time constants -> Table 2 + three sentences (~250); Table 2 itself could go to
    the supplement if the three sentences carry the numbers.
P7. 2.9 model equations -> Methods/App. B (~250).
P8. 5.4 bound paragraph (0.348 supremum) -> two sentences citing App. D; footnote 5 (Vieira
    details) -> supplement (~250).
P9. 4.9 second half (Af = 35 finite-amplitude analysis, delta-eta thresholds) overlaps 5.3 first
    paragraph; keep the numbers in 4.9, drop the restatement in 5.3 (~100).
P10. Table 3 "Existing evidence" column could shrink to citations (~300).

Sum of P1-P10 ~2.7k words plus R1-R13 merges ~0.8k: main text near 11k, within the JNE norm.

## Clarity (local)

C1. 2.3 does three jobs (maps and Table 1; current-ratio product law; three-factor response).
    Move the three-factor response to 2.6 (with R4); 2.3 then reads as one argument.
C2. 3.5 relative-weights sentence ("set the E and I rows ... the only asymmetry being") is hard
    to parse; a two-line display of the two drive terms would replace it.
C3. 4.4 third paragraph: eleven numbers in six lines. A small table (map x {ratio, focus shift,
    hippocampal mean change}) would carry them.
C4. Discussion 5.2 Violante paragraph is good; its third paragraph repeats 4.4 (R8).
