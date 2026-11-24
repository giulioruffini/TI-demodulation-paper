# Draft25 succinctness pass: eight compressions and relocations

Klaus, 2026-10-30, for Kaiti's handoff of 16:35. Baseline 8ecc70a; line numbers refer to
`TN0484_envelope_demodulation.tex` at that commit (identical to the draft24 reading content
of 30ed891), JNE article edition. Read-only: no edit, build, or push. Each item gives the
source, the destination, the action, and the content and qualifiers that must survive.
Word figures are estimates for the article main text; "relocated" words stay in the article
appendix or the supplement, "removed" words are duplicates.

Nothing below touches the five items the handoff protects (full PING in Methods, notation
appendix, the 2--5% comparison, the dynamic-sign crossover, kHz feasibility), the three
draft24 corrections, or the seven draft24 restorations (fixed-curvature inference, weak-drive
scope, envelope-following assumption, negative JR curvature at the pinned state, purpose of
the spiking comparison, PEIX motivation, network-effect sentence). Overlaps with Giulio's
undecided list of October 6 (C1--C7) are marked.

| # | Source (section, lines, first words) | Destination | Action | Words |
|---|---|---|---|---|
| 1 | Results 4.9 QIF, 1558--1561, 1563--1566, 1577--1584, 1623--1627 | supplement S-amplification, Fig. 13 caption | merge two threshold paragraphs; move leakage check and the eta=1.5 description | ~140 removed/relocated |
| 2 | Theory 2.7/2.8, 722 and 807; 2.8, 757 and Results 4.2, 1269--1270; Discussion 5.3, 1739--1746 | none (keep one copy) | delete three duplicated statements, recast one | ~70 removed |
| 3 | Theory 2.8, Table 2 (tab:doors), 761--798; refs at 753 and 1648 | supplement S-access | move the table; keep one main-text sentence with its citations | ~250 relocated |
| 4 | Results 4.8 NMM2, 1481--1491 and 1538--1542 | Theory 2.10 (pointer); supplement S-ping-runs | remove the re-derivation; move the amplitude check | ~80 removed/relocated |
| 5 | Theory 2.3, 493--503; Theory 2.5, 547--556 | Appendix B (models); supplement S-envelope-proof | move the bilinear source paragraph and the envelope-mean integral | ~85 relocated |
| 6 | Methods 3.6 QIF, 1133--1136, 1140--1141, 1147--1151 | supplement S-qif-checks | move run-level settings and checks; keep design, observables, criteria | ~70 relocated |
| 7 | Results 4.6, 1436--1443 | none | compress the transfer paragraph to two sentences | ~45 removed |
| 8 | Theory 2.4, 518--523 | supplement S-harmonics | move the rectifier catalogue; keep the threshold case | ~45 relocated |

Total about 785 words out of the main text (6.5% of 11,958), of which roughly 400 are duplicates
and 385 move to the supplement or appendix; about a page and a half of the 40-page article.

## 1. Results 4.9, QIF responses (lines 1546--1643)

The longest Results subsection (about 800 words) states the Hopf-threshold argument twice and
describes the eta = 1.5 panel in prose that the Fig. 13 caption already carries.

- **1a. Merge** lines 1563--1566 ("The $A_f=35$ runs are finite-amplitude illustrations ...
  as quantified below.") with lines 1577--1584 ("At the larger amplitude $A_f=35$ ... field-induced
  gamma with a smaller forced component.") into one paragraph placed where the second now
  stands. Retain: voltage excursion about 1.2 per tone; predicted E-drive shift 0.12 at
  $A_f=10$, below the E-only Hopf threshold 0.286; 1.65 at $A_f=35$, above it, with leading
  eigenvalue $+0.032$ ms$^{-1}$; dominant line near 52 Hz (depth 0.70) beside the 55 Hz beat
  (depth 0.29); direct mean-field integration reproduces the off-beat line; the reading of
  panel (b) as field-induced gamma with a smaller forced component.
- **1b. Move** lines 1558--1561 ("A longer window reduces the single carrier's apparent 55 Hz
  depth from 0.011 to $9.2\times10^{-5}$ ... spectral leakage.") to the supplement's
  finite-network checks (`supp_amplification.tex`, `app:qif-checks`), together with the 3200 ms
  window of item 6. Retain in the main text one clause: the single carrier's residual 55 Hz line
  is spectral leakage (supplement).
- **1c. Delete** lines 1623--1627 ("At $\bar\eta=1.5$, autonomous gamma near 53--54 Hz remains
  about four times larger ... does not show the full rate variation."). This is Giulio's
  undecided C4; the fold explanation is in the Fig. 13 caption ("Folding suppresses
  non-beat-locked gamma ..."). Retain the factor by extending line 1575: "... ongoing gamma near
  53--54 Hz remains about four times larger than the beat component (Fig. 13d)."

Keep unchanged: the opening paragraph, the equal-RMS control paragraph (referee deliverable,
"tested only in the mean field"), the $A_f=10$ convergence paragraph (0.09--0.16, theta 0.156
versus 0.137, 2.8%, "not converged"), the sidebands paragraph, and the PPC paragraph.

## 2. Statements made twice or three times

- **2a.** Line 807 "Carrier sweeps probe access and mixing together; beat sweeps probe
  amplification." repeats lines 722--723 ("A carrier sweep and a beat sweep therefore constrain
  different stages rather than a single effective gain."). Delete line 807's sentence.
- **2b.** The rule that QIF already contains access appears at line 757 ("QIF computes access in
  its membrane equation, requiring no additional filter on current input."), in Methods 3.5
  ("access uses $\tau_m=\tau_E$, without an assumed sigmoid") and in Results 4.2, lines 1269--1270 ("The dynamic
  QIF equations already include membrane access, so this filter must not be applied again.").
  Keep the Theory statement and the Methods implementation; delete the Results sentence. This
  honors C3 (the no-double-counting rule stays, once).
- **2c.** Lines 1739--1746 redefine the quality factor ($\mathcal Q=\pi f_0\tau_{\rm rev}$) that
  Theory 2.7 already defines as $\omega_0/(2\gamma)$. This is Giulio's undecided C7. Recast as
  one sentence: "With $\gamma=1/\tau_{\rm rev}$, a relaxation time of a few hundred
  milliseconds \cite{wilting2018} gives $\mathcal Q\approx10$ and a power bandwidth near 1 Hz at
  10 Hz, so detuning is consequential; that measured relaxation is not specific to an alpha
  mode." Retain: the citation, order-ten $\mathcal Q$, order-1 Hz bandwidth, the non-specificity
  qualifier, and the preceding sentence on spatial correlation length.

Not proposed: the matching conventions of 2.6 are restated in 5.4 (lines 1754--1757), but 5.4
holds the article's only definition of $\mathcal R_{\rm det}$ (Eq. rdet is supplement-only and
Methods line 961 cites it), so that restatement stays.

## 3. Table 2 (tab:doors, lines 761--798) to the supplement

The time-scale table is the largest block of supporting material in Theory (about 250 words
with its caption, half a page). It belongs with the access calculations of `supp_access.tex`
(`supp:access`), whose opening sentence already says it supports the distinction of 2.8.

- Move the table and caption intact as a supplementary table; keep the caption's "an axonal
  decay is not automatically a TI cutoff".
- Main text, line 753: replace "Table~\ref{tab:doors} distinguishes measured responses, assumed
  access, and downstream filtering." by one sentence that keeps the citations and the measured
  versus assumed distinction: "Measured somatic charging near 12--16.5 ms
  \cite{deitcher2017,eyal2016}, a fitted myelinated-axon decay near 1 ms
  \cite{cohen2020periaxonal}, the 1 and 0.4 ms membrane times of a prior TI network model
  \cite{esmaeilpour2021}, and the assumed 0.2 ms case are tabulated with the detection and
  synaptic time scales in the supplement (\S\ref{supp:access})." This also satisfies C2's
  request that the fitted decay and the current-versus-field qualification survive outside the
  table (the latter is already at lines 733--734).
- Discussion 5.1, line 1648: "The short-time cases in Table~\ref{tab:doors} are access
  hypotheses" becomes "The short-time access cases (0.2--1 ms; supplement, \S\ref{supp:access})
  are hypotheses".
- Every citation in the table also appears in the Introduction, so the article's reference list
  is unchanged. The table remains available to a referee in the supplement.

## 4. Results 4.8, NMM2 (lines 1474--1545)

- **4a.** Lines 1481--1491 re-derive the fast-carrier source already derived in 2.10 (lines
  884--887) and Appendix `app:mpr-coefficients`. Replace by: "At 300 Hz this detector is on the
  fast side of its crossover (\S\ref{sec:dynamic}): the fast-carrier source
  $I_1I_2/(\tau_E^2\omega_1\omega_2)$ in the $v_E$ equation, propagated through the network
  susceptibility at $\Omega$, reproduces the full second-order response within 1.1% at 300 Hz,
  0.1% at 1 kHz, and 0.03% at 2 kHz at four stable operating points
  (Fig.~\ref{fig:crossover}b)." Retain: the formula, the three percentages, four operating
  points, the figure pointer.
- **4b.** Lines 1538--1542 ("At $A_f=8$, the simulated response exceeds the normalized linear
  reference by up to 48% ... one sixteenth of the power ... within 11% at the nine tested
  couplings.") Move the 48% and the quarter-amplitude detail to `ping_sweep_settings.tex`
  (`supp:ping-runs`, which already records the $A_f=8$ sweep). Retain one sentence: "The linear
  reference holds within 11% at a quarter of the sweep amplitude, and the driven endpoint
  remains attracting under both waveforms (supplement, \S\ref{supp:ping-runs},
  \S\ref{app:ping-stability})."

## 5. Two derivation blocks in Theory

- **5a.** Lines 493--503, the bilinear multicompartment source, to Appendix B (`article_models.tex`,
  next to `app:mpr-mixing`) as a short subsection. Keep in 2.3 the first sentence (common fixed
  projection; the beat changes phase when either projection changes sign) and one sentence with
  the result: "With several compartments, a weak dynamic detector has the bilinear source
  $Y_\Omega=\sum_{kl}B_{kl}(\omega_2,-\omega_1)a_2^k\overline{a_1^l}$; linear access gives
  $a_j^k=I_j^{\rm pair}b_j^k$, so the common factor $I_1^{\rm pair}I_2^{\rm pair}$ and its fixed
  spatial pattern survive without a universal projection vector (Appendix~\ref{app:models})."
  Retain in the appendix: the definitions of $B_{kl}$ and the overbar, the rank-one
  specialization, $b_j^k$. The draft24 record lists "the multicompartment extension" as
  retained; it remains, stated once in the text and in full in the appendix.
- **5b.** Lines 547--556, the envelope-mean integral and $\vartheta$, to `envelope_proof.tex`
  (`supp:envelope-proof`), which already works with the beat phase and the norm form. Keep in
  2.5: "At matched polarizations $\varepsilon>0$, the envelope and quadratic means are
  $4\varepsilon/\pi$ and $\varepsilon^2$ before detector gains (supplement,
  \S\ref{supp:envelope-proof}). Either ideal detector gives a mean output with one carrier, but
  no beat; adaptation can alter the mean response." The first paragraph of 2.5 ("DC-like"
  describes the source) and the $\Sig''(v^*)<0$ sentence are untouched.

## 6. Methods 3.6, QIF run details (lines 1114--1164)

Move to `supp_amplification.tex` (`app:qif-checks`), which already reports these checks:
lines 1133--1136 ("For $\bar\eta=0.85$, separate checks double the population size ... raise
$V_{\rm peak}$ to 200 and 400 at both time steps."), the 3200 ms leakage window (lines
1140--1141), and lines 1147--1151 ("Euler integration uses 0.0025 ms steps ... 44 at 55 Hz and
34 at 42 Hz (800 and 810 ms).").

Retain in Methods: $N=8000$, the two conditions and amplitudes, the equal-RMS control with its
800 ms settling and measurement, modulation depth and PPC as observables (ten-spike minimum),
the theta check with the predeclared 5% tolerance and "convergence remains unestablished", and
one sentence: "Euler steps of 0.0025 ms, 800 ms settling (over four field-free relaxation
times), and whole-beat-cycle windows are used throughout; step, population, window, cutoff,
and leakage checks are listed in the supplement (\S\ref{app:qif-checks})." The cycle counts
stay in the Fig. 13 caption.

## 7. Results 4.6, the two-transfer paragraph (lines 1436--1443)

Compress to: "The detector's constant term and its beat line (Eq.~\eqref{eq:taylor}) meet
different transfers: $|G(\omega_0)|\propto1/(2\gamma\omega_0)$ grows without bound toward the
Hopf while $|G(0)|\propto1/(\omega_0^2+\gamma^2)$ stays finite. The amplified beat also
rectifies, adding a mean shift quadratic in its amplitude that can grow as $1/\gamma^2$ before
saturation, so a bounded $G(0)$ does not bound the mean shift." Retain both transfer forms and
the $1/\gamma^2$ growth. The first paragraph of 4.6, including "In this weakly driven regime",
is untouched.

## 8. Theory 2.4, the rectifier catalogue (lines 518--523)

Move "full- and half-wave rectifiers yield $2\mathcal A/\pi$ and $\mathcal A/\pi$, a
diode-and-capacitor detector follows the peak" and the sentence "Channel rectification,
threshold crossing, and release events are possible biological implementations" (flagged on
October 6 as a removal or citation target) to `harmonic_details.tex` (`supp:harmonics`), unless
already there, in which case delete. Keep the step detector with offset $\delta$, because the
following paragraph uses it ("A threshold detector is silent for $2\varepsilon\le\delta$"), and
the sentence "Other laws require different detectors", now ending with a supplement pointer.

## Considered and not proposed

- The 0.348 bound paragraph in 5.4 (lines 1765--1775): Giulio's open decision in `todo.md`. If he
  moves it, the destination is `supp:efficiency` (`app:bound`) with one sentence retained
  ("a numerically estimated supremum of 0.348 over bounded nondecreasing memoryless transfers,
  excluding dynamic QIF and general cellular mechanisms").
- The Violante statistics in 5.2 (four P values, voxel percentages): referee-facing evidence for
  "did not establish spatial steering"; moving them would weaken that paragraph.
- The posterior-share sweep paragraph in 4.4 (lines 1353--1363): its numbers support the
  opposite-motion claim of the abstract; compressing it saves under 30 words.
- The FEM orientation and interface numbers of PR #2: excluded by the handoff.
