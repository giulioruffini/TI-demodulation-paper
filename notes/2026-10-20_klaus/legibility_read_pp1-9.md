# Legibility read of draft20, pages 1–9, with Giulio's annotations — Klaus, 2026-10-20 17:30

Giulio, 17:25 CEST, while reading `TN0484_jne.pdf` (draft20, 9181d2d): "I think she's made a mess of
what I've read so far. It reads strange. This is a SCIENTIFIC PAPER, it should be readable, not
constantly referring to future sections. I think her edits damaged the storytelling and legibility."
He also dislikes the tilde notation for the reduced MPR variables (draft14, a2aacd6) and asked when
it came in. He is still reading and leaving notes in the PDF.

## His annotations so far (TN0484_jne.pdf saved 17:20; 13 annotations, pp. 5–8)

| page | where | note |
|---|---|---|
| 5 | Eq. (6) and "the slow-synapse limit ... stronger condition ω_c τ_rel ≪ 1" (highlight) | "an input I with a carrier of angular…" (truncated stamp; the passage about applying the static map to a carrier) |
| 6 | "This does not make membrane charging instantaneous." (highlight) | "(note that this does not …)." — an aside, not a sentence of the argument |
| 6 | "The FEM comparison in §3.3 therefore holds its chosen direction fixed..." and the projection-direction passage (highlight) | "consider moving this to that section" |
| 7 | Fig. 2 caption | "too much detail? Caption is too long." |
| 8 | unnumbered χ⁽²⁾ display, "Here i² = −1" (highlight) | "already known!"; "why no number for equation?" |
| 8 | "weak amplitude permits the expansion but does not remove memory, and symmetry or cancellation can make the quadratic term vanish" | "what???" |
| 8 | "Write 𝒜(t) for the nonnegative envelope ... whose temporal and spatial maps are derived in §2.5." | "what???" |
| 8 | "Dense perturbative sweeps use an AM surrogate ... specified in §3.1." | "what???" |

## My own read (pages 1–9), agreeing with him

1. **Forward pointers.** The article has 126 references to labels defined later, 25 of them to sections;
   §2.2 alone has 8 (6 to sections), the Introduction 5. In pages 4–9 the reader meets "Section 2.3
   calculates", "§2.8 restores", "App. B.2", "§3.3 therefore holds", "(§2.7)", "derived in §2.5",
   "specified in §3.1", "Fig. S12b", "§E.2" (in the Fig. 1 caption), "Table 3 distinguishes", "§4.10".
   Each one says "not here"; a reader cannot hold them.
2. **Orphan sentences.** Page 8 has two sentences whose only content is a pointer: the envelope
   definition "whose maps are derived in §2.5", and the surrogate "specified in §3.1". They should
   either carry their content or go.
3. **Ledger register.** Sentences that answer a past review rather than advance the argument:
   "This does not make membrane charging instantaneous." "Isotropic averaging is one possible
   distribution, not an anatomical consequence of choosing terminals." "A model driven by
   post-coupling polarization and a model driven by current through its own membrane equation must
   therefore count that filtering once." "Equal exponents do not imply equal amplitudes." "That
   classification is parameter-dependent." Each is true and each interrupts. They read as audit
   findings pasted into prose, which is what they are (the R1–R13 ladder).
4. **Order.** §2.1 front-loads four model definitions (JR filter, NMM1 operator form, MPR with tildes,
   the static F(Q) curve, then LaNMM) before the reader has the story; the one sentence that carries it
   ("Nonzero curvature makes this curve a mixer, while its slope sets the local gain") is buried.
   §2.3 (exact mean field, κ_DC with d, ν, tildes, the scaling-exponent table) arrives at page 8,
   before the simple detector story of §2.2 has been followed through §2.4–2.7. The reader has to
   survive the hardest section before reaching the payoff.
5. **Small things he flagged, all real.** Unnumbered χ⁽²⁾ equation and "Here i² = −1"; the Fig. 2 caption
   at ~330 words; the projection-direction paragraph in §2.2 belongs with the FEM methods; the tildes.
6. **What is fine.** The Introduction's first three paragraphs, the three-stage framing, the abstract,
   §2.2 up to Eq. (10), §2.4's opening. The science is right; the prose is the problem.

## Proposed remedy (for Kaiti; Giulio decides scope)

A legibility pass over Theory (pp. 4–15) as one revision, with a redline against draft20, not draft13:
- remove every forward pointer by moving the content, stating it in one clause, or deleting the
  pointer; target: no "§x.y" pointing forward in Introduction or Theory;
- delete the ledger sentences or fold each into the sentence it qualifies;
- number the χ⁽²⁾ equation, drop "Here i² = −1";
- cut the Fig. 2 caption to about 100 words; details to App. B or Methods;
- move the projection-direction paragraph (§2.2, "It also fixes the projection direction ... current
  ratio") to §3.3 as Giulio suggests;
- revert the reduced MPR variables to the draft13 convention (plain r, v, t and "in membrane-time
  units"; 30 occurrences, 3 notation-table rows, one figure producer), pending Giulio's word;
- consider moving §2.3 after §2.8 (access) or to App. B with a two-sentence summary in §2.2, so the
  Theory reads detection → laws → maps → steady source → amplification → access → operating point;
- then read the result as a reader, aloud if need be, before any check of numbers.

I can extract his further annotations as he goes (PyMuPDF on TN0484_jne.pdf) and keep this file
current. No source edits by me.
