# Draft26 read as a Journal of Neural Engineering reader (5 November 2026)

Read: the whole article PDF at d6805f1, pages 1 to 37, as a neural-engineering
reader who knows tES and neural mass models but has not followed this project.
Question asked by Giulio: does it make sense? Length is settled (11,235 words
against the 12,000 guideline), so this is about comprehension and flow only.
No manuscript edits; proposals for Kaiti after Giulio's decision.

## Verdict

The paper makes sense and holds together. The three-stage frame (access,
detection, amplification) is stated on page 3, drawn on page 4, and carried
through Theory, Results, Discussion and the Conclusion without a gap. The main
results a JNE reader will take away are reachable: the beat follows the carrier
product, so the current ratio rescales but cannot move the beat map; a signed
steady source accompanies the beat and has no interior maximum in uniform
tissue; the network resonance amplifies TI and tACS alike; at fast carriers the
sign of the steady source follows the slope of the rate curve rather than its
curvature. The derivations are short and each ends in a number.

What costs the reader effort is not length but texture. Many paragraphs are
stacks of true one-sentence statements with no connective tissue, the article
sends the reader to the supplement 30 times, and it hedges often enough that
the reader starts to doubt what the authors do claim. Section 4.7 is a wall of
numbers. The fixes below are de-duplication and one-clause bridges; none
removes a result.

## Where a reader stalls, in reading order

1. **Introduction, last paragraph (p. 4).** The contribution is stated as a
   list of operations ("we derive ... separate ... derive ... compares"). A
   reader wants the findings in one sentence each before Theory begins. The
   abstract's Significance already has them; two sentences of preview here
   would let the reader know what the nine Theory subsections are for.
2. **Section 2.3, paragraph beginning "The steady map instead weights"
   (p. 7).** Five independent caveats, one sentence each (ratio-dependent
   source shifts operating points; thresholds depart from the quadratic
   regime; the 2 min law needs envelope following; the product law permits an
   interior maximum; resonance cannot compensate a zero source). The reader
   cannot tell what the paragraph is for. One lead sentence ("Three things
   qualify the fixed-pattern result") or merging each caveat into the sentence
   it qualifies would fix it. The closing bilinear paragraph (B_kl) is the
   hardest in Theory for this readership; it stays by Giulio's decision, so
   a first sentence saying why it is there ("The product law does not depend
   on a single projection vector:") would help.
3. **Section 2.5, last two sentences (p. 9).** "An unmodulated carrier at the
   same local RMS polarization gives the same second-order mean shift..." is
   the setup for the equal-RMS control of Sections 3.6 and 4.7, but nothing
   says so. Add "which motivates the equal-RMS carrier control of §3.6".
4. **Section 2.9 (p. 11 to 12).** The hardest section for a JNE reader: MPR
   equations, the inflection at Δ/√3, the adiabatic limit, κ_DC. The payoff
   sentence (fast carriers follow the positive slope F', so the PEIX sign rule
   does not transfer) arrives at the end of the second paragraph on page 12.
   Stating it in the subsection's first sentence would carry the reader
   through the equations.
5. **Methods opening paragraph (p. 12).** Definitions of forced response,
   entrainment and gating appear before any model, under no heading. Give
   them a paragraph heading ("Terminology.") or move the sentence to 3.6
   where the terms are first needed.
6. **Section 4.6, first paragraph (p. 21).** "The ridge intensifies through
   the Hopf and shifts with state, making it diagonal" describes the
   two-dimensional map of Fig. S8, which the article reader does not see;
   Fig. 11 shows line cuts. Either say "in the (Δf, η̄) plane of Fig. S8" or
   drop "making it diagonal". Later, "a fitted damping exponent of 1.02"
   needs "(the 1/γ law)" for the reader to connect it to the JR result.
7. **Section 4.7 (p. 23 to 24).** The message is clear in its first sentence
   and is lost by the third paragraph. The section carries about twenty-five
   numbers, including convergence diagnostics (depths 0.09 to 0.16, the 12%
   population-doubling change) and the Hopf-threshold symbol δη*_E, which the
   article defines only in the notation table. Proposal: keep two numbers per
   condition in the article (beat depth and mean-rate change at each
   amplitude, the gamma line, the PPC before and after), define δη*_E in
   words at first use ("the rectified drive shift that would carry the E
   population across its Hopf"), and move the convergence numbers to the
   §S4.8 pointer that already exists. This is de-duplication: every number is
   in the supplement already.
8. **Section 5.3 (p. 26).** "Near-Hopf temporal slowing does not by itself
   establish a diverging spatial correlation length" answers a question the
   article never raises; only the keyword "criticality" hints at it. Give the
   reason in half a sentence or cut it.
9. **Section 5.4, the 0.348 paragraph (p. 26).** "A positive mixture of step
   responses extends the logistic calculation to this class" and "microvolt
   logistic widths at the illustrative polarizations" are unreadable without
   §S5. The reader needs one sentence: no bounded memoryless detector gives a
   matched-peak open-loop TI/direct ratio above about 0.35, so the 0.8%
   illustrative value sits far below the ceiling. The rest belongs in §S5.
   This is the open decision on the todo list; the reader's pass favors the
   one-sentence version.

## Texture, with counts (article body, pages 1 to 28)

| Pattern | Count |
|---|---:|
| "does not / do not / without establish(ing)" | 9 |
| "remains uncalibrated / unmeasured / unestablished / unconverged" | 5 |
| "requires calibration / measurement" | 5 |
| "neither ... nor" | 7 |
| "assumed / assumption" | 15 |
| Pointers to the supplement (§S) | 30 |

The hedges are each correct. Their density is the problem: a reader meets a
"does not establish" on average every 1,400 words and reads the paper as
defensive. Section 5.5 ("Limits of the population description") is the natural
home for the scope statements; Results could keep one per subsection. The 30
supplement pointers cluster in Methods (pages 12 to 16, eleven pointers) and
Discussion (pages 25 to 27, six). Methods can carry one pointer per subsection
("settings in §S4") instead of one per sentence.

## Terms a reader meets undefined in the article

- LaNMM (page 28, code availability; notation table): defined only in the
  supplement. Write "laminar model (LaNMM, supplement §S6)" at the first use
  or drop the acronym from the article.
- LPF[·] (Eq. 8, §3.1): used as the carrier-cycle average without saying so;
  not in the notation table.
- δη*_E (Section 4.7): see item 7.
- "J-curve" (§3.5) and "ridge" (§4.6): understandable in context, but a
  JNE reader would rather read "coupling sweep" and "resonance peak".

## What reads well and should not be touched

The Introduction's first page; Table 1 and the surrounding product-law
argument; Section 2.5's subharmonic result and the relocated PEIX paragraph;
Section 2.6's numbers; Sections 4.1 to 4.5 and their figures; Section 5.2's
Violante argument; Table 4; the Conclusion.

## Proposed order of work, if Giulio agrees

Items 1, 3, 5, 6, 8 and the undefined terms are one-line edits. Items 2 and 4
are one lead sentence each. Item 7 moves numbers to a pointer that exists.
Item 9 and the hedge consolidation are Giulio's decisions. None changes a
result, a figure or an equation.
