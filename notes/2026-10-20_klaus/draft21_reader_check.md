# Draft21 whole-paper reader check — Klaus, 2026-10-20

Target: d1ef427 (frozen), `build/review/TN0484_jne.pdf` (44 pp), supplement (23 pp), redline against
e20c047. Read front to back as a reader; no numerical audit, no source edits.

## Verdict

Not a clean pass, but the reading experience is transformed. The story now runs: rate curve → beat and
steady source → envelope and maps → detector laws → signed source → amplifier → access → operating
point → exact mean field as the extension. Forward section pointers are gone (25 → 0; label
references to later material 126 → 73, now figures and equations only). The ledger sentences are
mostly folded or cut; Results lead with the finding; captions describe; the Conclusion states results;
the tildes are gone and the physical-time MPR equations connect to the membrane-time derivation in
B.2, which states its convention in its first sentence. Six actionable problems remain, four of them
mechanical consequences of the relocation.

## 1. Cross-document equation numbers now point at the wrong equation (pp. 26, 32, 43; supplement p. 6)

The supplement numbers its equations (1)–(12+) independently, and the article cites relocated
equations by those numbers, which the article reader resolves against the main text:
- Fig. 10 caption, p. 26: "under a current carrier, Eq. (6)" — article Eq. (6) is Y_Ω; the intended
  equation is κ_DC, supplement Eq. (6).
- §5.4, p. 32: "supremum of 0.348 ... (Eq. (12))" — article Eq. (12) is H_det; intended: supplement
  Eq. (12), App. D. The following sentence, "The positive-mixture-of-steps argument extends the
  logistic result", now has no pointer to App. D at all.
- Table 4, p. 43: "κ_DC, κ_V — Eqs. (6), (8)" under a caption that says numbered references identify
  main-text definitions.
- Supplement B.2, p. 6: "the membrane filtering already represented by Eq. (4)" — supplement Eq. (4)
  is the JR ÿ₂ equation; intended: main-text Eq. (4). The supplement header says equation numbers
  follow the main text, which is not what its own equations do.
Remedy: number supplement equations (S1), (S2), … (or B.1, B.2, …), cite them as such from the
article, and cite main-text equations from the supplement as "main-text Eq. (4)".

## 2. Figure numbers do not follow first citation, and two figures are never cited (pp. 4, 9, 12, 16, 18)

First citations run Fig. 6 (§2.6, p. 9), Fig. 7 (§2.8, p. 12), Fig. 4, Fig. 5 (§4.1, p. 20), Fig. 2 (§3.4,
p. 16). Fig. 1 (receiver diagram, p. 4) and Fig. 3 (model schematic, p. 18) are never cited by
number; the schematic lost its Theory sentence when §2.1 was shortened, and now sits in §3.5 beside
the PING equations with "In the schematic, U_j(t) is ..." as its only mention. JNE numbers figures
by first citation. Remedy: cite Fig. 1 in the Introduction's three-stage paragraph and Fig. 3 at the
end of §2.1 ("Figure 3 locates the field input, the detector and the amplifier in the two circuits"),
which also restores the picture the Theory reader needs; then either renumber (6 → 2, 7 → 3, …) or
move the citations of the synaptic low-pass and curvature figures out of Theory into §4.1 and §4.3,
where the same facts are stated again.

## 3. Two sentences about the QIF detector are cryptic after the relocation (pp. 11–13)

- §2.7, p. 11: "In the latter description, the approach to a static transfer is governed by Eq. (19);
  the membrane filter must not be applied again outside the QIF equations." Eq. (19) is two pages
  ahead, and "the latter description" has lost its antecedent. Suggested: "A QIF reduction computes
  this filter inside its own membrane equation (§2.9), so it is not applied a second time."
- §2.9, p. 13: "In membrane-time units, the fast-carrier QIF voltage source has D = 1; G then includes
  its conversion through the voltage and rate dynamics." D was defined for JR as ½σ''. Suggested:
  "For the QIF mixer the role of ½σ'' is played by the unit coefficient of v² in membrane-time units;
  the voltage and rate dynamics that convert it to a rate beat then belong to G."
Everything else in §2.9 and B.2 connects: physical-time Eq. (17), the rate shift I²κ_DC/τ_m, and the
B.2 convention sentence are consistent and sufficient.

## 4. Remaining audit answers in prose (pp. 5, 13, 26, 30)

- §2.2, p. 5: "The access filter is included in the supplied polarization or computed by the membrane
  equation when its input is current; applying both would count the same attenuation twice." Fold
  into one clause of the preceding sentence or cut; §2.7 says it again.
- §3.1, p. 13, second half: "That agreement does not extend to the mean shift or second harmonic ...
  We therefore repeat the mean-shift-dependent comparisons with two tones ... The corresponding
  Results report both waveforms, whose different DC terms can shift the recurrent operating state."
  Three sentences for one rule: two tones wherever the mean shift or harmonics matter.
- §4.8, p. 26: "This refines the coupling-controlled sensitivity expected in QIF networks [33]: both
  coupling and rectifier are derived, but the dominant mode can change." and "The fully forced
  endpoint remains attracting under both waveforms, even where a DC-only approximation predicts
  instability; γ describes the field-free mode. The gain reference includes the state-dependent
  detector." Cut the first; the second is B.4's business, one clause at most.
- §5.1, p. 30: "whose population consequence follows from the slow-synapse limit without adding a
  periaxonal circuit." Cut the clause.

## 5. Methods still carry two settings blocks the supplement now holds (pp. 13, 19)

§3.5, p. 19: the endpoint-stability protocol with J = 16.5663 and 16.5901 stays in Methods while its
results moved to B.4; one sentence ("Stability of the driven endpoint was checked by Floquet
multipliers and a finite-time Lyapunov estimate, App. B.4") suffices. §3.1, p. 13, is unchanged from
draft20 apart from the pointer; it reads as a note to the authors. Both are the register Giulio
objected to, inside sections he had not reached.

## 6. The predictions table repeats the paper (pp. 33–35)

Table 3's "Current-ratio steering" test cell (120 words) restates the factor list already given in §4.4
and §5.2 (0.5–1.5, 0.75, 1.25 → 0.25 or 2.25). Keep the instructions (vary the ratio at fixed
electrodes, hold the projection direction, measure the DC shift, repeat at lower amplitude) and drop
the factors. Optional, and Giulio's call since he approved it yesterday: §5.2's Violante block is the
longest topic in the Discussion (~550 words); its third paragraph's hemodynamic sentences and the
fourth paragraph's "BOLD and functional connectivity measure neither source directly" say the same
thing once each and could merge.

## Read well

Introduction; §2.1–2.6 in the new order; §2.5's sign argument; §3.3, §3.4, §3.7 (now three
paragraphs); §4.1 merged; §4.4; §5.2 and §5.6 with the Q = 10 design where it belongs; the
Conclusion; the data statement. The abstract is unchanged.
