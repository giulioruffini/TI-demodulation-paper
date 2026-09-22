# Readability and notation review — TN0484 / WP0185 v0.13.0

Date 2026-09-22. Source `TN0484_envelope_demodulation.tex` at commit 072d2dc (2307 lines).
Line numbers refer to that file. Scope is prose and notation only: nothing here checks
arithmetic, references, or theorem validity, which is the `landau` pass. Spot checks of
the filter numbers in sec:khz and the harmonic ratios in sec:transduction were made while
reading and agree with the text; they are not reported as findings.

No edit has been applied to the manuscript. Every item below is a proposal.

## Summary

The paper is in good shape structurally: the title states the result, the abstracts
lead with the outcome, headings are declarative, and the argument does not depend on
prominence it has not earned. The defects are of two kinds. The prose leans on the
em-dash as its default connective (43 paragraphs carry two or more, nine carry four), and a
handful of moves are made several times over (the two-tone versus AM-surrogate point, the
detection-inherited/amplification-emergent slogan, the vocabulary of entrainment). The
notation reuses eleven glyphs for unrelated quantities, two of which collide inside the
same section (λ₀ as DC coupling and as DC space constant; ω_c as carrier mean and as one of
the two tones), and one symbol (δ, the threshold offset) is never defined.

Order of work, if the fixes are taken in one pass:

1. Notation renames and the missing definition (section 5.1, 5.2). Mechanical, no
   argument touched.
2. Abbreviations defined at first use (section 3.3).
3. The duplicated vocabulary section and the repeated moves (section 3.1, 3.2).
4. Em-dash sweep on the nine four-dash paragraphs and the Conclusion (section 4.1).
5. The defensive cluster in the Discussion (section 4.3).
6. The TN abstract's 62-word sentence (section 2).

Word count: TN main text (Introduction through the AI declaration, appendices excluded)
is about 14,300 words by `detex`; the JNE build drops the appendices but not the Discussion,
so the 12,000-word guideline is still open (see todo).

## 1. Mechanical pass

`tells.py` reports 52 findings: 43 em-dash paragraphs, 7 filler words, 2 "not merely X but Y".

| Class | Count | Disposition |
|---|---|---|
| EMDASH (≥2 per paragraph) | 43 | Real. Four-dash paragraphs at lines 235, 279, 356, 443, 805, 1166, 1247, 1341, 1850. |
| FILLER "rather" | 5 | False positives: each is a line-wrapped "rather than" (200, 287, 323, 1692, 2289). |
| FILLER "very" | 1 | Real, line 2086: "the very line the odd cubic cannot make". Delete "very". |
| FILLER "essentially" | 1 | Real, line 2211: "captures essentially the whole Δf sweep". Delete. |
| NOTJUST | 2 | Line 1685 "not reachable by this route rather than merely expensive"; line 1811 "not merely conceptually separable but experimentally separable". Rewrite flat. |

## 2. Messaging

**Title.** States the result. No change.

**TN abstract (lines 184–210).** 337 words in one paragraph. The sentence at 197–202
("Square-law detection is generic ... present evidence does not decide which class
operates in vivo") is 62 words with three subordinate clauses and carries the paper's
most delicate claim. Split at "but": one sentence for the bound, one for the microvolt
width, one for what the evidence does not decide. The opening "Here we ask how much of
that recovery ... belongs to the population" announces an intention; the next sentence
supplies the result, so the cost is one sentence of delay. Acceptable, but "We find that"
would remove it.

**JNE structured abstract (lines 157–181).** 294 words by a plain count, within the cap.
The Main-results block carries "Detection is offered as a *candidate*"; the italics
manufacture emphasis the sentence already has. Remove the `\emph`.

**Prominence.** No boxed claims. The bold run-in paragraph leads in the Discussion
(lines 1560, 1579, 1602, 1622, 1638, 1652) label topics, not stances, and the strongest
of them ("The amplitude budget does not close at human field strengths") is also the best
supported. The bold row in Table doors (line 770, AIS) is the paper's own candidate and
the caption says the compartment is unsettled; that is consistent. One mismatch: Results
opens (line 1076) with "We present the evidence on three rungs of the modeling ladder",
which narrates structure. Replace with the result: "Each rung of the modeling ladder shows
the same pair, square-law demodulation followed by near-Hopf amplification."

## 3. Coherence

### 3.1 Duplicated section

Methods §"Vocabulary: forced response, entrainment, and gating" (lines 1064–1073) and
Appendix D "Vocabulary and metrics" (2097–2128) both open with "'Entrainment' is used in
several senses" and both define the same three terms with the same criterion
(|f_out − Δf| < 0.3 Hz). In the TN build the reader meets the definitions twice; in the
JNE build the appendix is in the supplement. Keep the Methods paragraph as the definition
and cut the appendix down to what it alone adds: the choice of f_out over PLV (2111–2115),
the folded-rate metric (2116–2121), and the Arnold-tongue protocol (2127). Delete the
repeated "The distinction is load-bearing" (1071 and 2122).

### 3.2 Moves made more than once

| Move | Where | Proposal |
|---|---|---|
| Two-tone field versus AM surrogate: same Ω line, different DC and 2Ω content, so waveform-sensitive claims use two tones | sec:coupling 532–546; LaNMM Methods 957–964; QIF Methods 1034–1036; Results 1198–1205 and 1213–1217; captions 1193–1197, 1335–1337 | State it once in sec:coupling, cite that paragraph elsewhere in a clause. The captions can say "genuine two tones" without re-arguing. |
| Detection is inherited from the single cell, amplification is emergent | 202, 292–297, 359–367, 1391–1395, 1556–1559 | Keep the abstract and the Conclusion. In sec:nmm the 90-word sentence at 359–367 makes the point three times inside one sentence; cut to one. |
| "Genuine forced gain: with no drive the focus is silent at Ω" | body 1119–1121 and caption 1136–1137 | Caption or body, not both. |
| Carrier independence holds at fixed polarization, not at fixed applied field | 556–565, 745–748, 1146–1152, 1465–1476, table row 1530 | Four of these are needed (theory, results, prediction, table). The kHz-section restatement at 745–748 can go. |

### 3.3 Abbreviations undefined at first use

| Abbreviation | First body use | Where defined | Fix |
|---|---|---|---|
| AM | 229 ("their superposition is an AM signal") | TN abstract only; not in the JNE abstract | Write "amplitude-modulated (AM)" at 229. |
| LFP | 427 ("the LFP proxy v = y₁ − y₂") | never | "local field potential (LFP)". |
| tACS | 620 ("a weak tACS sweep") | 1054 | Move the expansion to 620 or to the Introduction, where "conventional low-frequency stimulation" (280) is what tACS means. |
| SNIC | 880 | 890, in the caption | Expand in the text at 880. |
| RF | 1253 ("tuned 'RF front end'") | never | "radio-frequency (RF)". |
| PAC | 1420 | 2117, as "phase–amplitude coupling" without the acronym | Expand at 1420. |
| PLV | 1702 | never | "phase-locking value (PLV)". |

### 3.4 Cross-reference load

48 section references (`\S\ref`) and 68 figure references in the main text. Two are
forward references the reader must hold: sec:coupling defers to the Discussion for what
the rodent regime costs (491–492), and sec:transduction cites a Results slope before Results
(627–629, "the ε² control already reported in §results-curvature (measured slope 1.99)").
The second is the wrong direction: Theory should not lean on a measurement four sections
ahead. Say "verified below" without the number.

### 3.5 Local coherence

- Line 259: "Where, then, is the nonlinearity in the brain?" opens the third Introduction
  paragraph as a rhetorical question. The paragraph answers it; the question can be
  replaced by its answer ("The leading biophysical account places the nonlinearity in
  single-neuron ion channels").
- Lines 814–823: the paragraph opens with TI and TMS efficacy tracking brain state, then
  argues for a 100 Hz carrier protocol. TMS appears nowhere else in Theory; it belongs to
  the Discussion paragraph at 1575–1578. Cut "and transcranial magnetic stimulation (TMS)"
  here.
- Line 1166: "To pre-empt the objection that the demonstration runs only at 100 Hz" narrates
  the author's motive. Open with the fact: "The demonstration also runs at a kHz carrier."
- Line 358: "and, as we show, it is what makes (de)modulation possible". Delete "as we show".
- Line 552: "the two applied carriers (ω_c and ω_c + Ω)" contradicts the definition at
  234–236, where the tones are f_c ∓ Δf/2 and f_c is their mean. See 5.1.
- Citations as nouns, ten cases (296, 482, 548, 828, 879, 973, 982, 1407, 1582, 2277): with
  `unsrt` these print as "reported by [12]". Name the authors: "reported by Caldas-Martinez
  et al. [12]".
- Captions carry argument that the body also carries: fig:khz_twotone (2200–2201, "This is
  the kHz claim on the physical waveform rather than on the AM surrogate"), fig:opp
  (1193–1197), fig:res (1136–1141, including "Three points cannot establish a power law").
  A caption states what is plotted; the sentence that says why it matters belongs in the
  text, once.

## 4. Register

### 4.1 Em-dashes

The rule is one per paragraph. The nine four-dash paragraphs are the priority; each uses the
dash for four different jobs (apposition, parenthesis, list, causal link) and reads as a
single breath. The Conclusion's first paragraph (1850–1866) is the worst case: about 230
words, four dashes, six claims. Break it into three paragraphs: the parity argument
(square of the envelope, no linear term), the bound and where it is approached, and the
doors. Two paragraphs also worth doing by hand rather than by search: 235 (Introduction,
the TI promise) and 1341 (J-curve, the network effect).

### 4.2 Sentence length

- 359–367 (sec:nmm): one sentence of about 90 words with two colons and three dashes.
- 197–202 (TN abstract): 62 words.
- 1259–1268 (LaNMM results): the "This contrast requires the phase-sensitive read-out"
  sentence runs 55 words.

### 4.3 Defensive writing

A scope limit stated as authorial restraint reads as a confession. Each of the following
becomes a fact when the "we do not" is removed.

| Line | Text | Rewrite |
|---|---|---|
| 650 | "The product law is thus not an account of TI focality, and we do not offer it as one." | "The product law is not an account of TI focality." |
| 1777 | "we do not offer it as a measured single-cell property, real thresholds being themselves noisy and state-dependent" | "Real thresholds are noisy and state-dependent, so the microvolt width is an idealization, not a measured single-cell property." |
| 1785–1787 | "The ceiling (eq) should not be compared statistically with any particular reported response ratio: the numerical proximity of the two would be neither support nor exclusion" | "The ceiling is a supremum over a family, not a prediction for any one preparation; its numerical proximity to a reported ratio is neither support nor exclusion." |
| 1820 | "We therefore do not claim that square-law transduction is what operates in the human brain at safe field strengths." | "Whether square-law transduction operates in the human brain at safe field strengths is open." |
| 1698 | "the per-current figure is therefore transduction-class-dependent and we do not use it" | "the per-current figure is transduction-class-dependent." |
| 529 | "The distinction is not cosmetic, because" | "The distinction matters because" |
| 1611 | "That coupling controls this gain is not itself new:" | "Coupling-controlled gain is known:" |

### 4.4 Word tics

| Word | Count | Note |
|---|---|---|
| genuine | 17 | Doing three jobs: "genuine two tones" (the waveform), "genuine forced gain", "genuine entrainment". Keep it for the waveform, where it contrasts with the surrogate; drop it elsewhere. |
| exactly | 16 | About half are mathematical ("exactly sinusoidal", "exact"). The rest ("exactly what a diode does", "exactly as Eq. predicts", "exactly what the amplitude sweep is built to decide") are emphasis. |
| sharp | 9 | "sharp resonance", "sharper still", "sharp test", "sharp new prediction". The resonance is sharp; the prediction and the test are not. |
| clean | 6 | "clean 11 Hz line", "clean supercritical Hopf", "clean near-term test", "cleanly". Delete outside the spectra. |
| load-bearing | 2 | Both in the duplicated vocabulary passage. |

### 4.5 Enumeration for cadence

- 930–943: "Three auxiliary constructions support the main results" followed in the same
  paragraph by "We verify the mechanism three ways." The counts match their lists, but two
  counted lists in one paragraph is rhythm. Drop the second count.
- 1764: "Two features of that limit decide the reading." The two features are not then
  numbered; the sentence is a drumroll. Delete it and let the paragraph begin "Such a
  detector is not weak."
- 1652: "Two hurdles stand between a transcranial field and a response" is content-bearing
  (the paragraph is organized around the pair). Keep.

### 4.6 American English

- 2212: "Colour:" in the fig:lanmm_p1 caption; fig:lanmm_p2 (1287) says "Color shows".
- 1166: "pre-empt" → "preempt" (moot if the sentence goes, 3.5).
- "programme" at 1896 is the Horizon 2020 program's proper name; keep.

### 4.7 Claim kind

Where `≃` appears (eq:demod 519, eq:khz 733, eq:khz text) it means "to leading order in
ε". Say so once, at eq:demod, and the later uses inherit it. The text otherwise uses ≈
for numerical values and ∼ for orders of magnitude consistently.

## 5. Notation

### 5.1 One glyph, several quantities

The head note of Table notation (1952–1964) already disambiguates A and C. The table below
lists the remaining reuses. "Fix" proposes the smallest rename; the last column marks
whether the two meanings ever meet on the same page.

| Glyph | Meaning 1 (line) | Meaning 2 (line) | Meaning 3 | Same page? | Fix |
|---|---|---|---|---|---|
| φ | firing-rate output, eq:coupling 450 and eq:lanmm_drive 952 | — | — | — | The rate is r everywhere else (eq:nmm1 377, table 1979). v0.13.0 changed φ→r in Table doors but not in these two equations. Write r(t) = Σ(v + s) and r_X(t). |
| λ₀, λ(ω) | DC field coupling λ^c₀ (462) and bare λ₀ (477, 1469) | AC space constant λ(ω) = λ₀(1 + ω²τ_m²)^(−1/4), eq:lambda 790 | — | Yes: 477 and 790 are one page apart and both write λ₀ | Rename the space constant ℓ(ω), ℓ₀ (or Λ_s). |
| λ | field coupling (461–466) | Jacobian eigenvalue λ± = −γ ± iω₀ (692, table 2004) | — | Yes, sec:carrier follows sec:coupling | Eigenvalue → μ± or σ ± iω₀ (σ is taken by Σ; use μ). |
| ω_c | carrier, the mean of the two tones (234–236, caption 1101: f_{1,2} = f_c ∓ Δf/2) | one of the two applied carriers, "(ω_c and ω_c + Ω)" (552) | — | Yes | At 552 write "(ω_c ∓ Ω/2)". |
| η | excitability η_j, η̄ (391, 999–1016, table 2028) | TI/tACS efficiency η = Σ''ε/4Σ' (1681, eq:etabound 1733, eq:etasup 1759) | — | No, but both appear in the Discussion's neighborhood and the table lists only the first | Efficiency → κ (or ε_TI is taken; κ is free). |
| s | field perturbation s(t) reaching the nonlinearity (240, 461) | NMM2 synaptic activations s_E, s_I (1001–1004, table 2032) | normalized transfer s = Σ/2e₀ (1726) | Meaning 3 sits in the same Discussion paragraph that uses ε; s(t) appears on the previous page | Rename meaning 3 to σ̃ or y = Σ/2e₀; leave s_E, s_I (subscripted, conventional). |
| x | PSP x(t) = K̂[r] (342) | reduced operating point x = ρ(v* − v₀) (1747) | location 𝐱 (656–668, bold) | No | Meaning 1 is used once; write x_s → u (see next row) or simply "a PSP". |
| u | PSP u_{m←n} (374–379) | reduced field u = ρε (1747) | dummy in \|cos u\| (597) | No | Dummy → θ (597; θ is already the cycle variable at 578). |
| p | JR external input, bifurcation parameter (throughout) | amplitude exponent in ΔPLV = Ψ(aI^p) (1794–1797) | summation index in k = l − p + q (2080) | 1794 is in the Discussion, far from the JR sweeps, but p ≈ 1 vs p ≈ 2 reads as an input rate | Exponent → β; SL index triple → (j, k, l). |
| a | JR synaptic rate (349, table 2054) | Stuart–Landau linear coefficient, γ ≡ −a (2075) | scale in Ψ(aI^p) (1794) | No | SL coefficient → α; scale → c. |
| I | lock-in in-phase component (906–912) | applied current I(t) in eq:mpr (386) | current in aI^p (1794); population label I | No | Lock-in components → I_Ω, Q_Ω; or leave and note that I(t) in eq:mpr is the MPR convention. |
| F | transduction F(A) (569, 600) | Stuart–Landau forcing F(t) (2075) | — | No | Forcing → 𝓕(t). |
| H | synaptic transfer H(ω) = Aa/(iω + a)² (686), caption 1160 | door access filters H_c, H_m, H_gate (466, 728, 800) | bare "\|H(f_c)\|²" (479) and "λ_f = λ₀\|H(f_c)\|" (1469) | Yes: 479 precedes 686 and the reader cannot tell which H is meant | Synaptic transfer → H_s(ω); the bare H at 479 and 1469 → H_c. |
| m | modulation depth (238) | synapse index m ← n (374–379) | — | Same page (eq:nmm1 follows the Introduction's eq:am by four pages; both are Theory) | Index → i ← j. |
| f | frequency everywhere | generic periodic function in 𝓜[f] ≡ max f − min f (633) | — | Yes, 𝓜[A] follows immediately | 𝓜[y]. |
| τ | fast-element time constant (742, table 2009) | reverberation time τ = 1/γ (1662, table 2006 "𝒬 = πf₀τ") | τ_E, τ_I, τ_a, τ_g, τ_m, τ_gate | The table defines τ twice on adjacent rows | Reverberation → τ_r or write 𝒬 = πf₀/γ and drop the second τ. |
| δ | threshold offset δ/2ε = 0.523 (1761, 1768, 1773) | weak-field polarization δV = λ·E (463) and NMM2 field term δV(t) (1002) | — | — | δ is never defined; see 5.2. |
| E | Ê with hat in Λ[Ê] (375, 2038) | 𝐄 bold vector (461, 663) | E(t), E₀ scalars (451, 474) | Yes, all in Theory | One typography: 𝐄(t) for the vector, E for its projection, E₀ for the amplitude. Λ[Ê] → Λ[𝐄]. |
| ε = λ_f E₀ vs ε = λ_f E | 474, 562, 1466 | 1716 | — | — | E₀ throughout. |
| Y_Ω, A_Ω | Y_LF, Y_Ω, Y_2Ω for the detector's baseband output (577–618, predictions 1483–1489, table 1519) | A_Ω for the lock-in amplitude at Ω (519 onward) | — | Both appear in sec:transduction | Either state once that Y_Ω is the open-loop (pre-network) amplitude and A_Ω the closed-loop one, or use A_open and A_Ω throughout. |

Two further points inside eq:doors (461–466): the left-hand side is a vector product
𝛌^c_f · 𝐄(t) while the right-hand definition λ^c_f = λ^c₀ \|H_c(ω_c)\| is scalar; say the
filter acts on the magnitude, or write 𝛌^c_f = 𝛌^c₀ \|H_c\|. And the door superscript is
dropped without notice at 477 ("λ_f ≈ λ₀"); one clause, "door index suppressed when only
the open door matters", licenses it.

### 5.2 Undefined at first use

| Symbol | Line | Note |
|---|---|---|
| δ | 1761 | "at a threshold offset δ/2ε = 0.523". Presumably δ = v₀ − v* = −x/ρ at the optimum. Define it in the sentence. |
| Ψ, a, p | 1794 | "ΔPLV = Ψ(aI^p)": Ψ a monotone link, a a scale, p the amplitude exponent, I the applied current. None is named; p and a collide (5.1). |
| c₁, c₂ | 600 | Defined in passing as the mixed-detector coefficients; fine. |
| g | 575 | Defined ("a memoryless nonlinearity g"); fine. |
| L(z) | 1750 | Defined; fine. |
| K̂, L̂ | 341–345 | Defined; the hats are not in the notation table. |

### 5.3 Missing from Table notation (App. A)

The table covers the simulation parameters well and the Theory and Discussion symbols
poorly. Add, at least: Y_Ω / Y_LF (detector output), the efficiency (η today, κ proposed),
𝓜[·] (excursion), R_Ω(𝐱) and G_𝐱(Ω) (spatial response and local susceptibility), δ
(threshold offset), u and x (reduced variables, eq:reduced), the AC space constant
(eq:lambda), ε_eff (sec:khz), ε₁, ε₂ (per-tone polarizations), H_s(ω) (synaptic transfer),
r_det and r_meas (harmonic ratios), f_out, PLV. Appendix-only symbols (z, Z_k, α, 𝓕) can
stay local if the appendix defines them, which it does.

The table's own head note says the units are "nominal"; the row for Σ', Σ'' gives
"s⁻¹mV^{−1,−2}", which is compact but not a unit. Two rows, or "s⁻¹ mV⁻¹ and s⁻¹ mV⁻²".

### 5.4 Units and precision in the text

| Line | Text | Issue |
|---|---|---|
| 1373 | "Σ''(v*) = −0.151" (fig:jcurve caption) | No unit. s⁻¹ mV⁻². |
| 645 | "(ε₁, ε₂) = (10, 1) superficially against (0.5, 0.5)" | No unit; the argument is a ratio, so say "in arbitrary units" or give mV. |
| 1330 | NMM2 peaks "0.0014 → 0.0030 → 0.0055" | r_E is dimensionless in MPR units here (the text says only v_E is); the table says s⁻¹. State the unit once in Methods NMM2. |
| 1173–1174, 2196 | tones at 1994.5 and 2005.5 Hz "beating at 10.9 Hz"; output "clean line at 11.0 Hz" | 2005.5 − 1994.5 = 11.0. Either the tones or the beat is misquoted; check the script and quote one number. |
| 1104, 1108 | tones "94.5 and 105.6 Hz", output "Ω = 11.0 Hz" | 105.6 − 94.5 = 11.1, consistent with Δf = f₀ = 11.1 and f_c ∓ 5.55 rounded; the output line then reads 11.0. Quote Δf once to one decimal and let the tones follow. |
| 880, 1090 | "p ≈ 315", "p > 315" | The unit (Hz, or s⁻¹ in the table) is given at 878 and then dropped; acceptable, but the table (2058) says "0–400 Hz" and the notation table says s⁻¹. Pick one. |

### 5.5 What is consistent and should stay

Σ for the sigmoid with ' and '' for its derivatives; ε for the polarization in JR/LaNMM
and A_f in NMM2/QIF, with the head note explaining why they are not interchangeable; Ω and
Δf as the pair (rad/s, Hz) with ω_c and f_c likewise; γ and ω₀ from the eigenvalue; 𝒬
calligraphic against the lock-in Q; C ≡ J with the identity stated at each use; the door
notation λ^c₀, λ^c_f, H_c after v0.13.0; Table doors with "rate r" and "field ε".

## 6. Not checked here

Arithmetic beyond the spot checks named at the top, bibliography entries, the theorem in
App. C, and corpus consistency with the CFC and HAM papers. Those are `landau` items.
