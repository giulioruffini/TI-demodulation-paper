# plan — TN0484 revision (Landau-style reorganization + new science)

Working spec for the v0.6 → v0.7 revision. Driven by a colleague review
(Theory/Results split, model progression, carrier dependence, spike-timing,
PEIX, framing, predictions) plus Giulio's refinements. Goal: terse, clearly
organized, scientifically tightened.

---

## Thesis (adopt as organizing principle)

Division of labor, stated once and kept consistent:

- **Single neuron** sets *why the carrier matters* (membrane low-pass → required
  field rises with f_c) and seeds *demodulation* (a fast nonlinearity samples the
  carrier).
- **Network (mesoscale)** supplies *amplification*, *frequency-selectivity*,
  *entrainment-vs-power*, and *state-dependence*.

Complementary to single-neuron ion-channel rectification, not an alternative.

---

## A. Target structure (reorganization)

**Theory = equations + stated predictions, NO figures.** All results-bearing
figures move to Results. Fixes the §2-introduces / §4.3-restates duplication.

- **Intro** — add one sentence naming the JR→LaNMM→NMM2 progression and why each
  rung matters: JR = closed form; LaNMM = two native resonances + genuine carrier
  dependence; NMM2 = nonlinearity *derived* (exact v^2), not postulated. State the
  division-of-labor thesis.
- **2.2** — sharpen epsilon as *post-coupling polarization* where A_Omega = 1/2 sigma'' epsilon^2 m appears.
- **2.4** — **define PEIX** (the actual normalized-slope formula).
- **2.5 (carrier)** — keep the meat, tightened (see B); move fig_khz to Results.

**Results = all evidence, once, in order:**
JR demodulation -> carrier independence & roll-off -> operating-point law ->
near-Hopf resonance -> **network amplification vs coupling J (new)** ->
**timing-not-rate (new)** -> square-law / linearization control -> LaNMM tongues ->
NMM2 -> **Predictions & tests (new, consolidated)**.

**Discussion** receives the TMS/chronaxie persuasion demoted from 2.5;
candidate-nonlinearity catalogue compressed to the 3 best-supported loci; framing
made consistent (no residual "alternative" tonality).

---

## B. 2.5 carrier argument — what to keep (Giulio's refinement)

State crisply, in order:

1. Demodulation is **carrier-independent at fixed polarization epsilon** — no omega_c in
   A_Omega. *This is the claim — not applied-field independence.*
2. Real membranes low-pass: at fixed *applied* field, A_Omega ~ |H_m(f_c)|^2 rolls off
   as 1/f_c^2 above the corner -> required field rises with f_c (reconciles with
   consensus); somatic demodulation dies at kHz -> real kHz-TI must demodulate at
   **fast elements** (AIS/nodes).
3. We simulate at **100 Hz** because it is convenient and consistent with the
   model's time constants — *but the result is generic.*
4. **kHz is a focality/engineering choice, not a demodulation requirement.** Two
   kHz beams keep the bare carrier subthreshold everywhere except the beat zone ->
   focal, steerable, deep. Buys selectivity, nothing mechanistic.
5. **100–200 Hz works as well or better for the mechanism** — the carrier reaches
   the nonlinearity more strongly (|H_m|^2 ~ 0.98 fast element vs ~1e-4 somatic at
   1 kHz). Only cost: off-target carrier activity — and that cost is *empirically
   questionable* (no demonstrated tES effects at those frequencies — **needs a
   citation / lit check**). So 100–200 Hz with Delta f swept through a region's band is
   the cleanest near-term test; kHz optimizes focality at the cost of mechanistic
   strength.

Net: kHz is for spatial selectivity; the envelope-recovery mechanism is
carrier-generic and in fact stronger at lower f_c.

---

## C. New simulations / figures (the meat we add)

1. **Network amplification vs coupling J** (highest value; Clusella-style). Sweep
   self-coupling (JR C, and/or NMM2 global C) toward the Hopf at fixed sigma''; show
   demodulated amplitude / Q growing as criticality is approached. Cleanly
   separates **detection (sigma'', single-cell, fixed)** from **amplification
   (network, J-dependent)**. Answers "what does the network add."
2. **Timing, not rate.** Envelope-locked AC response at Delta f amplified ~omega_0/2gamma
   near the Hopf while DC mean-rate shift is not (G(0) ~ 1/omega_0^2) -> near criticality
   timing entrains, mean rate stays flat (matches Vieira 2024). In NMM2, read the
   population phase/order parameter directly: phase locks at Delta f with r-bar flat.
   New Results subsection.
3. **Direct kHz single-column run.** One panel: demodulation at a kHz carrier with
   fast-element coupling explicit (direct vs soma vs fast element). Extends
   khz_analysis.py; merges into the carrier figure. Pre-empts "carrier is only
   100 Hz."

---



> **Update (v1.6):** J-curve done in BOTH models. JR (NMM1): pin v* via p(C) so sigma'' fixed; C->C*=136.6,
> A_Omega grows 27x; p and C knobs collapse onto one gain-vs-gamma curve. NMM2 (exact): J=C is the literal
> inter-QIF coupling; detection is structurally fixed (v_E^2 coeff = 2), so NO pinning -- sweep J at eta=0,
> read resonance peak; J*=16.66, gain ~1/gamma saturating. Combined "what the mesoscale adds" figure for
> Results. Code: jr_jsweep_engine.py/run_jcurve.py; nmm2_jcA.py/nmm2_jcD.py. Figs: fig_jcurve, fig_nmm2_jcurve.

## D. Order of operations

**Phase 0 — text only, makes it correct + organized (no sims):**
restate carrier claim as epsilon-independence everywhere; define PEIX; move all figures
to Results; add progression sentence; consolidate predictions; trim abstract
(drop 712x / result-dump); dedup slogan to two occurrences; fix author-line
placeholder; add figure->script table. -> submittable-correct + well-organized.

**Phase 1 — new science:** (1) J-sweep amplification, (2) timing-not-rate,
(3) direct-kHz panel. Keep test_jr_demod.py green; add a check per new result.
Prototype J-sweep and AC/DC separation before committing to the manuscript.

**Phase 2 — finish:** reflow Discussion (receive 2.5 persuasion); compress
catalogue; framing consistency; verify high-freq-tES claim with citation; final
Landau compression pass; recompile, confirm no undefined refs; update
current_state.md; commit + push.

---

## Open items / decisions

- Target venue? (sets how hard to push on length.)
- High-freq tES "no demonstrated effects" claim — find citation or soften.
- J-sweep: JR (vary C) vs NMM2 (vary C, exact) — likely both; decide after
  prototype.

---

## HANDOFF → Claude Code  (written 2026-06-17, from a Cowork session)

**Read first:** `docs/current_state.md` (newest entry on top: v1.7) and this file.
You are mid-revision of `TN0484_envelope_demodulation.tex` (root of repo). It compiles
clean: 22 pp, 0 undefined refs (`pdflatex` works locally; `.bbl` is committed).

### Done so far
- **Phase 1 J-curves built & in repo** (network amplification = "what the mesoscale adds"):
  - JR (NMM1, alpha): `code/jr_jsweep_engine.py` + `run_jcurve.py`/`run_res.py`/`make_jfig.py`
    -> `figures/fig_jcurve.{png,pdf}`. Pin v* via p(C) so sigma'' fixed; C->C*=136.6, A_Omega x27;
    p and C knobs collapse to one gain-vs-gamma curve.
  - NMM2 (exact MPR PING, gamma): `code/nmm2_jcA.py` (engine + algebraic fixed point + gamma eig) and
    `code/nmm2_jcD.py` (resonance-peak grid + figure) -> `figures/fig_nmm2_jcurve.{png,pdf}`.
    J=C is the literal inter-QIF coupling; detection structurally fixed (v_E^2 coeff=2), no pinning;
    eta=0, gamma Hopf J*=16.66; read resonance PEAK over Delta f (mode-agnostic). gain ~1/gamma, saturating.
  - DECISION: keep JR alpha + NMM2 gamma; frame as ONE band-agnostic J law in two native bands.
- **Phase 0(a) DONE:** carrier claim reframed as independence **at fixed polarization epsilon**, applied-field
  threshold rises with f_c (epsilon=kappa(f_c)E_0). 6 spots edited (abstract, intro, 2.2, 2.3, 2.5, Discussion).

### Next: finish Phase 0
1. **Structural reorg:** make Theory equations-only; MOVE results figures (fig_carrier, fig_operating_point,
   fig_khz) from Theory(2.3-2.5) into Results; delete/rewrite the stub 4.3 ("...shown above"). Add a topic
   sentence opening Results naming the JR->LaNMM->NMM2 progression.
2. **Define PEIX** (give the actual normalized-slope formula) where it first appears (2.4).
3. **Trim abstract** (drop the 712x / result-dump); **dedup the slogan** ("wherever a fast-enough
   nonlinearity...") to TWO occurrences (intro + conclusion).
4. **Consolidate falsifiable predictions** into one Results subsection (carrier@fixed-pol, PEIX/sign-flip,
   state-dependence), each with a line on lit + test.
5. **Author line** still a placeholder? (check title block) -- fill before circulation.
6. **Figure->script table** for reproducibility.

### Then Phase 1 writeup + Phase 2
- [DONE v1.8] Wove both J-curves into Results subsection \ref{sec:jcurve}; originally: "what the mesoscale adds" (detection sigma'' vs amplification
  1/gamma; JR pinned-v*, NMM2 literal-J exact). Add the new figures to the .tex.
- Still TODO from the review: timing-not-rate result (#5; AC at Delta f amplified ~omega0/2gamma near Hopf vs
  flat DC mean rate -> matches Vieira 2024; NMM2 order parameter), direct-kHz single-column panel (#6).
- Phase 2: Discussion reflow (receive 2.5 TMS/chronaxie persuasion), compress candidate-nonlinearity catalogue
  to 3 loci, VERIFY the "no demonstrated tES effects at 100-200 Hz" claim with a citation, final Landau pass.

### Workflow notes
- In Cowork the Write/Edit tools were blocked on this Dropbox path (edits done via python string-replace).
  In Claude Code, native Edit works directly -- use it. Backup of pre-Phase-0 tex: /tmp/TN0484.bak.tex (Cowork
  sandbox only; make your own git commit before large edits).
- Style: Landau -- terse, every sentence earns its place. American English. Compile after each batch.
- Reproduce J-curves: `cd code && python3 run_jcurve.py && python3 run_res.py && python3 make_jfig.py`
  (JR); `python3 nmm2_jcD.py` (NMM2, ~5 s, foreground).
