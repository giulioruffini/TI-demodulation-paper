# Legibility read, Methods through Conclusion and supplement — Klaus, 2026-10-20

Requested by Kaiti (17:42) as input to the whole-paper pass. Source: draft20 (e20c047), read from the
built article (pp. 16–38, 44–47) and the supplement (21 pp). No numerical audit; no source edits.
Eight problems, each with anchor, why it interrupts understanding, and a content-preserving remedy.
Pages 1–9 are covered in `legibility_read_pp1-9.md`.

## 1. Results opens with a roadmap, and §4.1 is a two-sentence stub

**Anchor.** Results preamble, p. 22–23 ("Coupling controls that gain ... (§4.6), ... (§4.7). The
TI/tACS comparison then isolates their shared amplifier (§4.8), before the NMM2 and QIF results ...
(App. E)"); §4.1, p. 23, two sentences.
**Why.** The preamble is five forward pointers in a row; the subsection titles already say the same.
§4.1 is shorter than the Fig. 4 caption that carries its result (two input lines, nothing at the
carrier or in the alpha band, an alpha line in the output).
**Remedy.** Delete the roadmap. Fold §4.1 into §4.2 as its first paragraph, moving the narrative from
the Fig. 4 caption into the text and leaving the caption to describe the panels.

## 2. Methods carry results, and three limitations are stated three times

**Anchor.** §3.5, p. 20–21 ("Although a DC-only averaged calculation predicts an unstable endpoint
... multiplier is 0.034 ... Lyapunov estimate is −0.00079 ms⁻¹"); §3.6, p. 21–22, last two paragraphs
(beat depths 0.093/0.127/0.139, cutoff sensitivity); §3.3 last paragraph, p. 18 ("No signed DC-source
or mean-response map is computed ... requires a calibrated access and input–output model"), repeated
at §4.5 end, p. 26, and in Discussion, p. 33.
**Why.** The reader meets convergence numbers in Methods, again in §4.10 ("The response depends on
the finite spike cutoff ... (§3.6)"), and again in the Fig. 13 caption; the geometric-map caveat
three times. Each repetition reads as a new warning.
**Remedy.** Methods keep the protocol (what was integrated, how long, what was varied). Convergence and
stability numbers go once into §4.10 or a short supplement table. The geometric-map caveat stays once,
at the end of §4.5; the Methods and Discussion copies become a half-sentence pointer at most.

## 3. §3.7 is a settings dump

**Anchor.** §3.7, p. 22, one paragraph: "v* = 8.30 mV, TI surrogate amplitude 0.3 mV with m = 1 and
fc = 100 Hz, and tACS amplitude 0.1 mV ... C = 110, 133.9091, and 136.3 use a tACS amplitude of
0.0143039 mV ... 12 s settling and a 6 s window, repeated with 60 s settling and a 20 s window".
**Why.** Twenty lines of run parameters with no sentence structure to hold them; six-digit values in
prose.
**Remedy.** One sentence in Methods (pinned operating point, which waveform for which figure, lock-in
readout) and a run-settings table (run, waveform, amplitude, settling, window) in the supplement or
the repository README, which the data statement already cites for figure-to-script mapping.

## 4. §3.2 restates the Theory tests and then designs an experiment

**Anchor.** §3.2, p. 16–17: first paragraph ("After correcting for network gain, their ratio tends
to zero for weak quadratic detection but to 1/5 for ideal envelope following") repeats §2.4; last
paragraph ("At resonance (Ω = ω0) with Q = 10, a detector ratio of 20% reads as 0.7% ... or with G
measured independently by a weak sweep of ... tACS and deconvolved") designs a biological experiment.
**Why.** Methods should say what this paper measured in its models: the lock-in and the log–log
slope. The experimental-design paragraph belongs with the predictions.
**Remedy.** Keep Eq. (24) and the slope measurement. Move the Q = 10 / off-resonance design to the
"Transduction class" row of Table 4, which already points to §3.2 for it. Drop the §2.4 restatement.

## 5. Captions argue and qualify

**Anchor.** Fig. 5 caption, p. 23 ("Three points cannot establish a power law; the 1/γ scaling is
quantified over a decade ... in Fig. 9(c). The above-Hopf regime ... is characterized ... in
Fig. S4"); Fig. 7(a), p. 25 ("The mechanism is sign-agnostic ... The sign flip is itself a prediction
(§5.1)"); Fig. 7(d) ("it does not validate the recurrent AM-surrogate sweeps of Fig. 9 near the
Hopf"); Fig. 13, p. 32, last four sentences (window 0.8 → 3.2 s, cutoffs 200–400, "(§3.6)").
**Why.** A caption that defends the figure against objections reads as a footnote war. Readers skim
captions for what is plotted.
**Remedy.** Captions name the panels, axes, conditions and one-line result. Each qualification moves to
the sentence in Results that cites the figure, or is deleted where the Results sentence already
carries it (the 1/γ decade is already in §4.6).

## 6. Three efficiency paragraphs and a re-analysis of Vieira

**Anchor.** Discussion, p. 35: "Absolute response estimates remain sensitive ..." (R_det), "Primate
measurements illustrate the limits ..." (Vieira: 0.34, CI 0.04–0.65, 65 of 154 neurons, twenty cells,
ten, seven, PLV 0.10/0.20/0.043), "For an illustrative fast-access budget ..." (0.092 mV, 0.8%), "For
comparison, the carrier-averaged ... supremum of 0.348 ... (App. D)". Four consecutive paragraphs,
~600 words, one topic.
**Why.** The point is one sentence: under a fast-access budget the smooth detector's generated drive is
about 1% of a matched direct drive, a step-like detector could reach 35%, and no published experiment
matched polarization at the mixer. The Vieira numbers are a reanalysis of someone else's two
experiments and bury that sentence.
**Remedy.** One paragraph: the budget (0.1 mV, R_det ≈ 0.8%), the class ceiling (0.35, App. D, needs
microvolt widths), and why Vieira does not calibrate it (polarization not matched; PLV state-dependent).
The Vieira details go to the "Timing versus rate" row of Table 4 or a footnote.

## 7. Discussion ledger paragraphs

**Anchor.** p. 33: "the direct protein effects reviewed by Cifra et al. occur at 10 kV/m to GV/m ...
that review excludes fields below 0.1 kV/m" (answers an objection nobody in the paper raised);
"A 10–100-fold reduction in a QIF membrane time is therefore a sensitivity hypothesis ... a new
periaxonal circuit is not needed for that limiting argument"; "Weak amplitude alone does not make
that coefficient static ..." (repeats §2.1 and §2.3). §4.9, p. 29: "This refines the
coupling-controlled sensitivity expected in QIF networks [31] ..."; "The normalization and
endpoint-stability checks are given in §3.5; γ always describes the field-free critical mode, not the
driven state."
**Why.** These are answers to past audit items. Each is true; none advances the Discussion, and
together they make the first page of the Discussion read as a rebuttal.
**Remedy.** Cifra becomes one clause in the access paragraph ("well below the fields at which direct
protein effects are reported [50]"). The periaxonal and static-coefficient sentences are deleted or
folded into the access paragraph as one clause each. The two §4.9 sentences go.

## 8. The Conclusion restates caveats instead of the result

**Anchor.** §6, p. 38: "Its TI transfer and the absolute response at human field strengths require
calibration." "Fast access and slow network resonance can coexist, with each filter counted once; a
large response alone identifies neither an efficient detector nor its microscopic mechanism." "...
finite-amplitude responses near the Hopf can depart from that ratio."
**Why.** Half of the Conclusion's sentences are qualifications; a reader finishing the paper should be
able to say what it found.
**Remedy.** Four short paragraphs: (i) three stages in series, and at weak fields the beat follows the
product of the carrier polarizations, the steady source their summed squares; (ii) in a real head the
current ratio moves envelope and mean-square foci oppositely and only rescales the product map;
(iii) near a Hopf the circuit amplifies the beat as 1/γ, shared with direct stimulation, mostly as
timing; at larger fields the steady shift alone can induce gamma, as can an equal-power carrier;
(iv) one test per stage. Qualifications stay in the Discussion.

## Also noticed, below the cut

- §3.8 and App. F are two vocabulary sections; keep the three definitions in §3.8 (three sentences)
  and the metrics in App. F. The last §3.8 paragraph is a Results statement.
- §4.8: "Increasing that direct input by a factor of 6.99 increases its response by 6.97, 3.95, and
  1.96" needs the sentence it supports (the direct drive saturates earlier near the Hopf) before the
  numbers, or the numbers go to a table.
- Table 4, "Current-ratio steering" test cell is a 120-word paragraph; the factor list (0.5–1.5, 0.75,
  1.25 → 0.25/2.25) is already in §4.5 and the Discussion.
- Data statement: "A reconstructed producer ... reproduces every archived spectral bin ... exactly.
  The LaNMM setup is a drawn schematic." are audit notes; one sentence on what the repository
  contains suffices.
- Supplement App. C last sentence and App. B.1 last sentence are the same ledger register; App. D is a
  derivation and reads as one.
- §4.5 (Ricardo's section) and the new Violante Discussion paragraphs read well; the Violante block is
  now the longest topic in the Discussion (~500 words) and could lose its third paragraph's first two
  sentences without loss.
