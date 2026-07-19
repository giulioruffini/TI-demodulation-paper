# Figure audit — all 25 figures

2026-07-19. Every figure rendered to PNG and inspected against its caption and the body
text. Main text reviewed directly; the fifteen supplementary figures audited in parallel and
the load-bearing claims re-verified here independently.

Two findings block submission. Three are scientific. The rest are consistency defects.

---

## BLOCKING 1 — every figure's text is below IOP's minimum

IOP requires 8–12 pt text at final printed size. Measured by taking each PDF's natural width,
the fraction of `\textwidth` it is placed at, and the `Tf` font operators in its content
streams:

| figure | scale | smallest text | largest text |
|---|---|---|---|
| `fig_qif_timing` | 0.48 | **2.3 pt** | 4.8 |
| `fig_entrainment` | 0.48 | **2.5 pt** | 5.3 |
| `fig_jcurve` (main) | 0.48 | **2.7 pt** | 5.3 |
| `fig_qif_raster` (main) | 0.65 | **2.7 pt** | 6.5 |
| `fig_bifurcation_sigmoid` (main) | 0.59 | **2.9 pt** | 7.4 |
| `fig_concept` (main) | 0.55 | 3.2 pt | 6.6 |
| `fig_operating_point` (main) | 0.64 | 3.6 pt | 7.0 |
| `fig_demodulation` (main) | 0.62 | 4.1 pt | 7.8 |
| … | … | … | … |
| `fig_resonance_map` (best case) | 0.70 | 5.9 pt | 7.7 |

**22 of 22 vector figures fail, main text included, and in every single one even the
*largest* text is under 8 pt.** Not one figure has a compliant tick label.

The cause is uniform: figures are generated at matplotlib defaults on oversized canvases
(natural widths 449–971 pt) and then squeezed into a 465 pt text block, scaling everything
by 0.48–0.75. `fig_entrainment` is worst at 0.48, printing its annotations at 2.5 pt.

The fix belongs at generation time — raise `rcParams` font sizes and shrink `figsize` so the
post-scaling result lands in 8–12 pt. Enlarging `\includegraphics` would only overflow the
page. This is one systematic pass over the plotting scripts, not 22 separate repairs.

Separately, `fig_lanmm_setup.png` is line art delivered as raster at ~207 dpi, under IOP's
300 dpi floor; line art should be vector.

## BLOCKING 2 — supplementary figures are not in citation order

IOP numbers figures by first citation. Current order of first mention:

> S15 → S7 → S12 → S2 → S9 → S3 → S11 → S13 → S14 → S4 → S6 → S5 → S8 → S10 → S1

The **first** supplementary figure the reader is sent to is **S15**, the last one in the
file; **S1** is cited last. The appendix needs reordering to match.

This is partly my doing: the four figures I demoted were appended at the end of the appendix
rather than inserted at their citation positions, which put the earliest-cited figure last.

---

## SCIENTIFIC 1 — "entrainment" is claimed three times from an observable the paper forbids

The paper's own vocabulary section (Appendix C) defines entrainment as frequency capture of
a self-sustained oscillator, tested by $|f_{\rm out}-\Delta f|<0.3$ Hz on the dominant output
frequency, and reserves lock-in amplitude for *forced response*. The `fig:res` caption states
the rule outright: the above-Hopf regime "is characterized with the appropriate observable
(output frequency $f_{\rm out}$, **not lock-in amplitude**)."

Three figures then do exactly what that sentence forbids:

- **Fig. 7 `fig:lanmm_p2` (main text)** is titled "LaNMM Arnold tongues" and plots
  alpha-band **power**.
- **S9 `fig:lanmm_res`** titles its right panel "entrainment of the autonomous alpha" and
  plots **lock-in amplitude**.
- **S11 `fig:nmm2_map`** describes entrainment above the Hopf from a **lock-in** map.

The paper hands a referee the objection and then commits it in three places. Either re-plot
with $f_{\rm out}$ and the $1{:}1$ criterion, as `fig:entrain` does for Jansen–Rit, or
relabel these as forced-response and gating maps.

Compounding this for Fig. 7: its caption says the tongue "widens with $A$", which is the
defining property of an Arnold tongue. Inverting the viridis colormap and measuring width
above a fixed level, the width grows from 0 to ~1.5 Hz between $A\approx60$ and $A\approx180$
and then *narrows* (1.41, 1.26 Hz). Peak intensity does grow monotonically (0.42 → 0.93), so
the body text's weaker "grows with $A$" is supported. The wedge is not.

## SCIENTIFIC 2 — Fig. 4's caption claims a law its own data contradict

`fig:res`, right panel: "the peak height grows monotonically … **i.e. gain $\propto1/\gamma$**".
The three plotted points are 0.70, 0.43, 0.23 mV at distance-to-Hopf 15, 40, 80. If gain went
as $1/\gamma$ the product would be constant; it is 10.5, 17.2, 18.4, and a log–log fit gives
$A\sim\gamma^{-0.65}$.

This is a caption defect, not a science defect: **Fig. 9(c) does the job properly**, plotting
$A_\Omega/A_{\rm open}$ against $1/\gamma$ on log–log with a reference line, and honestly
showing the law holding for a decade then saturating. Fig. 4 should defer to it. Three points
over a factor of five in $\gamma$ cannot establish a power law regardless.

## SCIENTIFIC 3 — S14's caption contradicts S14

`fig:timing`. The caption says the DC mean-rate shift "**stays flat** at a few mHz". The
plotted red curve holds ~+3.7 mHz to $\gamma\approx2$, then falls monotonically through zero
at $\gamma\approx0.7$ to −3 mHz at the Hopf: it changes sign, and it is the most conspicuous
feature in the panel. Caption (b) likewise says "the DC gain stays ~1" while the trace dips
to ~0.03, a 30× excursion.

The **body text is correct** — §sec:timing says the DC shift "stays within a few mHz of
zero", which is true and defensible. Only the captions are wrong, and the caption is what a
referee reads first. This matters because it is the paper's headline timing-not-rate result.

---

## Consistency and labeling

**Panel conventions are mixed.** Figs. 2, 3 and 5 carry (a)/(b)/(c)/(d) labels their captions
never use, referring instead to "Left/Right" and "Top left/Bottom right". Fig. 4 has no
letters at all. S8 `fig:ver` is lettered but its caption says Left/Right. S2
`fig:lanmm_setup` uses lowercase `a)` `b)` against the caption's `(a)` `(b)`. Figs. 9 and 10
are correct. Pick one convention; lettering everything is safest for a journal that may
restack panels at production.

**Captions contradicting figures.**
- S2 `fig:lanmm_setup`: caption says "$P_2$ carries the modulated fast carrier"; the figure
  draws $P_2$'s output as a flat line in both panels. The two panels also have identical
  right-hand traces, so the figure does not visually distinguish the two drive
  configurations it exists to contrast.
- S6 `fig:map`: the $y$-axis label arrow reads "→ toward Hopf" pointing at $p=400$, which the
  plot itself annotates "far from Hopf". Direct contradiction inside one panel.
- S5 `fig:entrain`: Methods promise "clipped points are flagged in Fig. S5c" — **nothing is
  flagged**; every marker is identical and the legend has one entry. Panels (a) and (b) also
  disagree at the same $\varepsilon=0.6$ mV on the tongue's low-frequency edge (~0.7 Hz) and
  symmetry, and panel (c) is non-monotone (7.0 → dips to 5.3 → 15.0) against a caption
  claiming growth.

**Broken typography.**
- S13 `fig:nmm2_jcurve` panel (b): log minor-tick labels overprint into an unreadable smear;
  the $1/\gamma$ range cannot be determined at all. Cheapest fix on the list.
- S8 `fig:ver` panel (a): x tick labels collide, `3×10⁻¹` and `4×10⁻¹` overprinting into
  "3 × 10⁴1". Panel (b): the second bar (0.0020 vs 1.40 on a linear axis) is literally
  invisible, and neither value is printed.

**Missing scales and parameters.**
- Fig. 10 `fig:qif_raster`: the population rate $r_E(t)$ is drawn on the "E neuron #" axis
  with no second axis, no ticks and no units, so it cannot be read off. The insets are
  calibrated; the main panels are not. Also unexplained why (b) uses $\Delta f=55$ Hz and (d)
  uses 42 Hz, and panel (d) shows 1.6% gamma-amplitude modulation next to a box reading
  "depth 0.19" — two quantities differing tenfold with nothing distinguishing them.
- S10 `fig:lanmm_p1` omits the carrier for (a,b) and $A$ for (c,d) that its main-text sibling
  supplies. "The whole carrier range" in the body is 25–80 Hz, stated nowhere.
- S4 `fig:tacs` never gives $\varepsilon=0.1$ mV, without which the 1.66 mV peak has no
  interpretable gain.

**Data-quality artifacts left uncommented.**
- S11 `fig:nmm2_map`: the ridge is undersampled into disconnected tiles rather than a
  continuous ridge, and the sub-Hopf region the caption says it "intensifies through" is
  invisible — the ridge begins *at* the Hopf.
- S3 `fig:lanmm_map`: signal appears only on the entrainment side, contradicting its claim to
  be "the analog of the JR map", which demonstrates the opposite regime. Ridge is
  discontiguous, consistent with the phase-slip artifact the Methods warn about. Drive axis
  has no units. Over 40% of the panel is featureless black.
- S12 `fig:khz_direct`: the soma curve turns non-monotonic below ~5×10⁻⁶ (theory gives
  5.5×10⁻⁶ at 3 kHz and 2.0×10⁻⁶ at 5 kHz; the plot shows 1.6×10⁻⁶ then 4×10⁻⁶) — a solver
  floor, while the caption says flatly "collapses as $1/f_c^2$".

**Colour as the sole cue** in Fig. 4 (three blue shades), Fig. 9b (four viridis lines),
S9, S14a (which additionally has *no legend entry at all* for the DC series) and S15b.

---

## The demotion moved load-bearing evidence out of the body

Worth reconsidering. Three cases where the body makes a claim and its support is now in the
appendix:

- **§sec:timing** is a main-text Results subsection whose only figure (S14) is now
  supplementary.
- **S12 `fig:khz_direct`** is the rebuttal to the field's main objection — the body at line
  573 explicitly frames it as "to pre-empt the objection" that the demonstration runs at
  100 Hz — and now reads "a direct kHz-carrier run (Fig. S12) confirms it".
- **S13 `fig:nmm2_jcurve`** is the exact-mean-field J-curve the Discussion leans on for the
  criticality argument, and it is the *stronger* version of `fig:jcurve` (no operating-point
  pinning, coupling and rectifier both derived) — yet `fig:jcurve` stayed in the main text
  and this went to the appendix.

## Duplication worth cutting

- `fig:khz` and `fig:khz_direct` panel (a) plot the same three coupling routes, same colours,
  same $1/f_c^2$ guide, same log axis. Merge or cut one.
- Three near-identical resonance maps: `fig:map`, `fig:lanmm_map`, `fig:nmm2_map`.
  `fig:lanmm_map` is the weakest and the strongest candidate to cut.
- S15(c) largely duplicates the boxed modulation depths already in Fig. 10.

## What is in good shape

**Fig. 6 `fig:opp`** is the strongest figure in the paper: measured and predicted curves are
visually indistinguishable and the sign reversal at the inflection is unambiguous.
**Fig. 9 `fig:jcurve`** is the quantitative backbone of the amplification claim and earns
main-text placement outright. **S1 `fig:sl`** and **S7 `fig:khz`** had every quoted number
verified against the figure and the body. **S15(c)** prints every value it claims.
