# current_state — NMM envelope-demodulation / resonance demo

## v1.28 — task C: reproducible repo (figure paths, run_all, verified README) (latest)
Reproducibility pass. Audited all ~25 code/ scripts and built a VERIFIED figure->script map
(24 manuscript figures). Findings were worse than the moving-notes draft: **15** figures (not 4)
were generated to the dead `../paper/figures` dir, and 2 more (fig_jcurve, fig_tacs_jcurve) were
written under bare CWD names then renamed by hand (make_jfig emitted NO pdf at all).
Fixed:
- 7 scripts redirected from `../paper/figures` -> `figures/` via the house pattern
  `FIGS = os.environ.get("TN_FIGDIR") or .../../figures` (env-overridable for safe dry-runs):
  figures_v2, make_figures, rerun_resonance, khz_analysis, nmm2_ping, lanmm_resonance,
  lanmm_arnold_tongues.
- make_jfig.py now emits fig_jcurve.{pdf,png} to figures/ (was bare jcurve.png, dpi 135, no pdf);
  tacs_jsweep.py now emits fig_tacs_jcurve.{pdf,png} (was bare tacs_jsweep.*). Both load committed
  npz, so runnable. Smoke-tested all fixes into a scratch TN_FIGDIR; committed figures untouched.
- NEW `code/run_all.py`: one-command reproduce (dependency order, per-step subprocess + summary,
  `--list/--figdir/--only`, auto-skips lanmm_arnold if lanmmv11 absent).
- Rewrote top-level README.md (was stale: pre-move `paper/` layout, 18pp/v0.6): venv setup, root-level
  build, verified figure->script table, artifact-policy note.
TWO REPRODUCIBILITY GAPS remain (no working generator):
  (1) fig_lanmm_setup -- hand-drawn schematic, by design.
  (2) fig_entrainment -- neither plotter nor data (entrain*.npz) committed; AND flagged as scientifically
      weak (coarse binary tongue, discontinuous/asymmetric locking curve, non-monotonic grid-clipped
      panel c) -> redesign candidate, not just reconstruction.
  Plus lanmm_arnold_tongues needs external lanmmv11 (LaNMM repo) to run.
  [correction: fig_nmm2_jcurve is NOT a gap -- make_nmm2_jfig.py exists (audit missed it); now
  TN_FIGDIR-aware and wired into run_all via nmm2_jcA/jcD data producers.]
Pending decisions for Giulio: write the nmm2_jcurve plotter? redesign fig_entrainment? archive dead/
dup scripts (jr_analysis dead; nmm2_jc/jcD vs jcA; make_timing_fig vs timing_not_rate)? No figures were
regenerated (that's task B); paper build untouched.

## v1.27 — removed WP0070 citations (internal doc), kept the criticality paragraph (latest)
WP0070 is internal/non-citable. Removed both \cite{ruffini2026criticality} from the tex and the bib entry.
The Discussion criticality paragraph stays intact, now supported only by public refs already cited
(ott2008 Ott-Antonsen, montbrio2015, clusella2023): order-parameter bridge + exact reduction are
Montbrio/OA results; mean-field caveat is textbook stat-mech. ott2008 retained as a real public citation.
Compiles clean: 29 pp, 0 undefined refs, 0 bibtex warnings; no WP0070 trace in the manuscript.

## v1.26 — WP0070 criticality connection woven into Discussion (latest)
Giulio uploaded WP0070 ("ODE Bifurcations Are Not Critical Phenomena", Ruffini & Vohryzek 2026). Added a
Discussion paragraph ("Amplification is critical slowing---and what kind of criticality") + 2 bib entries
(ruffini2026criticality WP0070; ott2008 Ott-Antonsen). Argument: our 1/gamma amplification = critical
slowing / diverging susceptibility as the leading Jacobian eigenvalue -> 0 at the Hopf. JR/LaNMM Hopf is an
ODE near-bifurcation; but in the EXACT NMM2/MPR reduction (r,v) are genuine order parameters (conformal map
to Kuramoto-Daido via Ott-Antonsen), so the Hopf is a true macroscopic transition and the 1/gamma gain is
its diverging susceptibility, with J the control parameter -> legitimizes "near criticality" precisely AND
shields against the "Hopf != criticality" referee. Honest caveat stated: mean-field critical point
(all-to-all) -> temporal critical slowing but NO diverging spatial correlation length (temporal-
susceptibility face, not scale-free spatial). Compiles clean: 29 pp, 0 undefined refs, 0 bibtex warnings.

## v1.25 — Methods paragraph for the entrainment/Arnold-tongue analysis (latest)
Added a Methods paragraph documenting the S5 construction and its subtleties: limit-cycle regime
(SNIC~115 < p < Hopf~315), direct in-band drive, dominant output frequency via Hann-windowed FFT on a
decimated buffer, 1:1 locking tolerance |f_out-Df|<0.3 Hz, definitions of the tongue / locking plateau /
locking range (width = locked points x grid spacing, grid centered on f0(p)), cycle amplitude = field-free
max-min of v. Two caveats stated: (i) finite Df window (f0+-5 Hz) -> near-Hopf locking ranges are
grid-clipped lower bounds (trend robust, absolute scale grid/tolerance-set); (ii) at onset the tongue
merges into the forced-resonance bandwidth, so supercritical locking range and subcritical 1/gamma
susceptibility coincide by construction. Code cite: entrain.py, entrain_crit.py. Compiles clean: 29 pp.

## v1.24 — S5 entrainment figure now has distance-to-Hopf as a coordinate (latest)
Giulio's point: the old S5 panels were both at a single distance to the Hopf -> nothing showed the
"near criticality" dependence. Added panel (c) (code/entrain_crit.py): sweep the autonomous operating
point p across the limit-cycle range toward the Hopf (p_Hopf~315) at fixed drive; plot LOCKING RANGE
(tongue width, Hz) vs DISTANCE TO HOPF (p_Hopf-p), with autonomous cycle amplitude on the twin axis.
Result: as distance 155->4, cycle amplitude halves (2.76->1.15 mV) and locking range ~doubles
(5.4->10.3 Hz, near-Hopf points grid-clipped lower bounds) -- entrainment is easiest near criticality,
the supercritical counterpart of the 1/gamma forced gain. S5 is now 3 panels (tongue, frequency locking,
criticality). Caption + code cite updated. Compiles clean: 28 pp, 0 undefined refs.

## v1.23 — figure triage: 18 -> 13 main; raster promoted; open/closed-loop def (latest)
- Moved 6 figures main -> Supplementary appendix: resonance_map, khz (open-loop roll-off), verification,
  lanmm_resonance, lanmm_arnold_p1, nmm2_map. All keep their body \ref (now Fig. S#).
- PROMOTED fig_qif_raster (QIF spiking, TI realigns spike timing) into the main sec:timing with an intro
  sentence; quantitative qif_timing stays in app:qif. Main text now 13 figs, appendix 11.
- DEFINED open-loop vs closed-loop explicitly in Methods (sigmoid alone at fixed v* vs full recurrent JR).
- Added fig:concept reference (was orphaned).
- S6/entrainment: added the criticality statement -- entrainment, like the 1/gamma gain, is enhanced near
  the critical point (tongue widens approaching the Hopf); the column is most responsive near criticality on
  BOTH sides (forcing below, entrainment above). [Statement added; a demonstrating panel = tongue width vs
  distance-to-Hopf is still optional/offered.]
- Compiles clean: 28 pp, 0 undefined refs. Backup /tmp/TN0484.pre_figmove.tex.

## v1.22 — above-Hopf entrainment figure (S4) (latest)
Built the oscillatory-side companion to substantiate the metrics note. code/entrain.py (pure numpy):
JR column set in its autonomous alpha limit cycle (p=250, below the input Hopf, f0~11 Hz), driven by a
direct in-band sinusoid. Fig.~S4 (fig:entrain, figures/fig_entrainment): (a) the 1:1 Arnold tongue -- a
wedge anchored at f0 widening with drive amplitude; (b) frequency locking -- output rides Delta f inside the
tongue, snaps back to f0 outside. Referenced from the sec:jcurve metrics note. Demonstrates: above the Hopf,
amplification = entrainment (tongue width, locking range), NOT the 1/gamma amplitude gain of the stable
side. Compiles clean: 27 pp, 0 undefined refs.

## v1.22 — QIF microscale: spike-timing realignment (new appendix) (latest)
Built the spiking-network ground truth beneath NMM2: TI realigns spike TIMING, not mean rate.
- **New Appendix** (`app:qif`) + 2 figures (fig_qif_raster, fig_qif_timing). Compiles clean: 27 pp,
  0 undefined refs (pdflatex+bibtex+pdflatex x2). Cross-ref added from sec:timing.
- **QIF network from scratch** (`code/qif_raster.py`, pure numpy): N=2000 E + 2000 I QIF neurons,
  tau_a V' = V^2 + eta_j + [F on E] + tau_a C(A.s); eta_j ~ Lorentzian(etabar,1) via deterministic
  quantiles; 2nd-order synapses driven by empirical rates; hard threshold/reset Vpeak=100. Params
  IDENTICAL to nmm2_ping.py. Validated: field-free <r_e> QIF=0.052 vs mean-field 0.050; matched gamma PSD.
- **Both regimes (per Giulio):** FORCED (etabar=0.85, just below the gamma Hopf ~1.1, df=55): off async/flat,
  on spikes bunch into the envelope -> timing AC@df x13.8, <r_e> x1.10. ENTRAINED (etabar=1.5, autonomous
  f0=54, df=42 DETUNED): off free gamma, on re-timed to the 42 Hz TI beat -> AC@42 x22, <r_e> x1.07.
  Timing up 14-22x, mean rate ~flat -> microscale analog of sec:timing and Vieira 2024.
- Figs via `code/make_qif_figs.py`: fig_qif_raster (4-panel raster + r_E(t) + envelope), fig_qif_timing
  (a: QIF-vs-NMM2 PSD validation + mean-rate match; b: fold-change bars rate vs timing).
- NOTE: heavy parallel Cowork work (v1.13-v1.21: new title, lmodern, Nature abstract/intro, tACS
  shares-the-amplifier extension) was uncommitted in the working tree; this commit bundles it with the QIF work.

## v1.21 — metrics note + subcritical clarifications + S3 Methods fix (latest)
- Clarified the sweeps are SUBCRITICAL (stable focus, gamma>0; approach the supercritical Hopf from below)
  in the jcurve/nmm2_jcurve/tacs/timing captions and a sentence in sec:jcurve, with the above-Hopf
  (entrainment/Arnold-tongue) regime named.
- Added the METRICS note: below the Hopf the observable is the driven lock-in (1/gamma susceptibility);
  above it, amplification must be read as entrainment (tongue width, phase-locking) + oscillation-amplitude
  modulation -- distinct metrics coinciding only at onset; weak demodulated drive biases phase (timing)
  there too, matching timing-not-rate.
- FIXED missing methods for Fig. S3 (tACS): new Methods paragraph covering all coupling sweeps (pinned-v*
  p(C) construction, Jacobian gamma/omega0, AM vs direct-sinusoid drive) + code cites jr_jsweep_engine.py,
  timing_not_rate.py, tacs_jsweep.py; S3 caption now cites tacs_jsweep.py.
- Compiles clean: 25 pp, 0 undefined refs.
OPEN: (a) optional supplementary figure for the OSCILLATORY (above-Hopf) side -- entrainment tongue +
amplitude modulation in the JR column, to substantiate the metrics note; (b) LaNMM Arnold-tongue figure
improvement/merge using github.com/giulioruffini/LaNMM_predictive_coding_paper (lanmmv11.py) -- best in Code.

## v1.20 — Nature figure pass + tACS shares-the-amplifier extension (latest)
- FIGURE PASS: declarative figure TITLES (carrier, kHz, map, demod, resonance now state the finding);
  trimmed the operating-point Results body that echoed fig:opp's caption.
- tACS EXTENSION (Giulio's idea): new supplementary sim code/tacs_jsweep.py (pure numpy) -> appendix
  Fig.~S3 (fig:tacs, figures/fig_tacs_jcurve). A DIRECT Delta f (tACS) drive skips demodulation but feeds
  the SAME near-Hopf resonator: pinning v* and sweeping coupling C(=J) toward the alpha Hopf, the tACS
  lock-in grows ~9x (gamma 10.7->0.12) as 1/gamma and the resonance sharpens -- identical network
  amplification to TI, but LINEAR in the field (vs square-law). Added a Discussion paragraph: TI = tACS +
  a sigmoid demodulation front-end; downstream both share the criticality/coupling-controlled amplifier;
  matched for effective in-band drive they should entrain alike (cites clusella2023).
- Compiles clean: 25 pp, 0 undefined refs. Backups in /tmp.

## v1.19 — Nature-editor pass: new title + intro hook/contribution/roadmap (latest)
- TITLE -> "The cortical column as a tuned receiver: a network mechanism for temporal-interference
  stimulation" (was "A neural-mass mechanism ... sigmoid curvature and near-Hopf amplification").
- INTRO: added a broad opening hook ("Reaching a deep brain target without stimulating the tissue above
  it..."); recast the contribution as "Here we show that a population-scale mechanism ... suffices";
  completed the model roadmap to all three rungs (JR -> LaNMM -> exact next-generation mean field).
- Compiles clean, 24 pp. Backup /tmp/TN0484.pre_title.tex.
Next available editor pass: declarative figure TITLES + self-contained captions (several still echo body).

## v1.18 — Nature-style abstract rewrite (latest)
Reframed the abstract for a broad readership: significance -> puzzle -> population answer ->
detection/amplification factorization -> consequences (carrier-independence, frequency-selectivity,
timing-not-rate in vivo) -> brain-state implication -> AM-radio metaphor. Removed ALL notation from the
abstract (dropped the A_Omega=1/2 Sig'' eps^2 m formula + symbol glossary, and the PEIX/CFC/HAM/LaNMM
name-drops -> these live in the body). ~252 words (offer to cut to ~180 for a hard Nature limit). Compiles
clean, 24 pp. Backup /tmp/TN0484.pre_nature.tex. Next editor passes available: intro hook + one-line
contribution; declarative figure titles + self-contained captions; results topic sentences.

## v1.17 — acted on Code's editor review (items 1-3 + de-hedge) (latest)
- FIXED grammar fragment in intro ("Writing the field as ... Its spectrum" -> "Write the field as ...;
  its spectrum"). Confirmed real.
- TITLE BLOCK refreshed: Date 2026-06-03/v0.6 -> 2026-06-17/v0.7; removed the commented-out Code: line.
- RIGOR: added a dominant-mode/center-manifold caveat to Eq.(gain) in sec:carrier; softened the
  timing-not-rate DC claim ("stays within a few mHz, consistent with zero"; dropped "even changes sign").
- Verified the DC question by re-running timing_not_rate.py: DC mean-rate shift ~+3.7 mHz for gamma>2,
  flips to -3.1 mHz ONLY at the extreme gamma=0.08 point (AC there 0.73 mV) -> non-robust (Jensen offset of
  the large near-Hopf oscillation + hardest settling), not signal. Wording now reflects this.
- DE-HEDGE: cut "precisely", "it is essential to", "subtle"x2, "plausible". ("genuinely" already absent.)
- Compiles clean: 24 pp, 0 undefined refs.
HELD per Giulio: abstract trim (he shaped it), merge of the two Arnold-tongue figures (needs image work),
deeper state-dependence/1-gamma refrain dedup (taste). Commit pending (sandbox git blocked; do from Code).

## v1.16 — supplementary appendix moved after references (latest)
Per Giulio: the \appendix "Supplementary figures" (S1 lanmm_setup, S2 lanmm_map) now follows
\bibliography{references}, before \end{document}. Cross-refs resolve; 24 pp, 0 undefined refs.

## v1.15 — Rosetta Stone citation updated to published version (latest)
ruffini2025rosetta (cited ~8x for the NMM/JR/MPR math) updated from "accepted, 2025" to the PUBLISHED
record: Castaldo, de Palma, Clusella, Garcia-Ojalvo, Ruffini, "Rosetta Stone of neural mass models",
Physics Reports 1189:1-49 (2026), doi:10.1016/j.physrep.2026.05.004 (PII S0370157326002139; verified via
Crossref). Kept the citation key unchanged so all \cite calls resolve. Renders in bbl as "Physics Reports,
1189:1--49, 2026." Rebuilt bibtex+pdflatex; clean. (unsrt style doesn't print DOI; it's in the .bib note/doi
field if a doi-aware style is later used.) Backup /tmp/references.bak.bib.

## v1.14 — Landau streamline pass #2 (latest)
Full read-through + disciplined compression (6 block edits, each verified): trimmed the Intro single-cell
hedge (dup of Theory); tightened the Theory "claim" sentence; cut the stochastic-resonance digression in
sec:khz (dropped the V(t) eq + tRNS aside, 2 now-unused refs terney2008/vandergroen2016); trimmed the
state-dependence sentence in sec:khz (full version kept in Conclusion) and the 100-Hz justification;
de-duplicated the Conclusion (was "state-dependent" 3x + a redundant closing sentence). Body 8093 -> 7832
words; 25 -> 24 pp. Rebuilt bibtex; compiles clean, 0 undefined refs, 0 bibtex warnings. Backup
/tmp/TN0484.pre_landau2.tex. Commit pending (sandbox git blocked; do from Code).

## v1.13 — classic font fix (lmodern) + figures to appendix (latest)
- FONT: the bare [T1]{fontenc} with no font package was substituting an odd CM variant (SFRM/SFBX) for
  text while math stayed plain CM -- the "awful"/mismatched look. Added \usepackage{lmodern} before
  fontenc: text+math now uniform Latin Modern (the classic Computer Modern look, vectorized/crisp). pdffonts
  confirms LMRoman/LMMath throughout.
- FIGURES: moved fig_lanmm_setup (schematic, overlaps concept) and fig_lanmm_map (redundant 3rd resonance
  map) to a new \appendix "Supplementary figures" with S-numbering (S1, S2); body refs auto-resolve.
  Kept the Arnold-tongue result figures in Results (didn't risk an image merge).
- Compiles clean: 25 pp, 0 undefined refs. Commit pending (sandbox git blocked; do from Code).

## v1.12 — notation collision fixed (r->rho) + intro/carrier compression (latest)
- Renamed the sigmoid SLOPE r -> \rho (Eq. sigmoid, Table, PEIX Eq. e_0\rho/2 and sech^2[\rho/2(...)]),
  removing the collision with the MPR firing rate r/r_E. Verified no stray slope-r remains.
- Compression (high-confidence): Intro SEC/EEC+HAM tail tightened (~15 lines -> ~8); carrier-opening
  three-item list dropped (dup of the three predictions); earlier removed 2 verbatim Results dups.
- Compiles clean: 25 pp, 0 undefined refs.
DELIBERATELY HELD (judgment/risk): deeper prose cuts the audit flagged (state-dependence stated 4x -- the
sec:khz instance now also carries the TMS expansion, so cutting needs care; op-point Results paragraph
duplicating its caption; loci-bullet trim; khz numeric litany) and the FIGURE TRIM (~20 graphics ->
move fig_lanmm_setup + fig_lanmm_map to a supplement, merge the two Arnold-tongue figures). These are the
remaining levers to reach the audit's ~22-28% reduction. Commit pending (sandbox git blocked; do from Code).

## v1.11 — final Landau/notation pass: audit + safe edits applied (latest)
Subagent read the whole manuscript. Notation verdict: clean except ONE real defect -- the symbol `r`
is both the sigmoid slope (Table, Eq. sigmoid) and the firing rate (MPR/NMM2). Spelling uniformly
American; units consistent; v* vs v_0, f_c/omega_c, gamma, A_Omega, C(=J) all consistent.
Applied (safe): expanded tES/tRNS/TMS at first use; added (MPR); Table "midpoint"->"inflection";
deleted two verbatim-duplicate sentences in Results (band-pass dup of Theory; carrier-caveat dup).
Compiles clean: 25 pp, 0 undefined refs.
OUTSTANDING DECISIONS (user): (1) the `r` collision -- rename sigmoid slope to rho (breaks JR convention)
or leave with a note; (2) figure trim -- ~20 graphics; candidates to merge/supplement: fig_lanmm_setup
(dup of concept), fig_lanmm_map (redundant 3rd map), merge the two Arnold-tongue figs, merge khz/khz_direct;
(3) deeper prose compression (~22-28% possible): carrier-caveat ~7x, state-dependence 4x, long intro tail,
Results re-narrating captions. NOTE: keep the abstract amplification/timing clause (user asked for it).

## v1.10 — abstract revised for network-amplification clarity (latest)
Restructured the abstract around the detection/amplification factorization the paper now proves:
"the sigmoid \emph{detects}" (square law, inherited curvature) vs "the network \emph{amplifies}"
(1/gamma near the Hopf). Made the new results explicit: amplification is tuned by the COUPLING at fixed
detection (J-curve), and being frequency-selective it boosts envelope-frequency TIMING far more than mean
rate (timing-not-rate). Split the old run-on sentence; NMM2 noted as confirming with "nonlinearity AND
coupling both derived". Compiles clean: 25 pp, 0 undefined refs. (Applied in Cowork via python string-
replace; backup /tmp/TN0484.pre_abstract.tex. NOT yet committed -- commit from Code/terminal: sandbox git
lacks identity/write perms on the Dropbox .git.)

## v1.9 — Phase 1 #5/#6 + Phase 2 (timing-not-rate, direct-kHz, Discussion reflow) (latest)
Closed the remaining review items.
- **#5 timing-not-rate** (new Results \ref{sec:timing} + fig_timing_not_rate): at FIXED detection
  (pinned v*, same construction as the J-curve) drive toward the Hopf via coupling; AC lock-in at
  Df=f0 grows ~17x tracking 1/gamma (saturating), while DC mean-rate shift stays flat at ~3.7 mHz.
  G(w0)~1/(2 g w0) diverges, G(0)~1/w0^2 flat -> timing entrains, rate doesn't (mesoscale analog of
  Vieira 2024). Code: `code/timing_not_rate.py` (sim, ~20s) + `code/make_timing_fig.py`.
- **#6 direct-kHz** (paragraph + fig_khz_direct in the kHz-rolloff subsection): closed-loop JR driven at
  genuine kHz carriers, field pre-filtered by an explicit membrane LP (extra ODE state) per route. Direct
  flat (carrier-independent), fast element (tau=0.2ms) survives into kHz, soma (16ms) collapses ~1/f_c^2;
  2 kHz carrier -> clean alpha line recovered (input alpha power = 0). Pre-empts "demo is only 100 Hz."
  Code: `code/khz_direct.py` (self-contained, ~90s; p=400 so the high-Q floor doesn't mask the soma rolloff).
- **Phase 2:** candidate-nonlinearity catalogue compressed 6->**3 loci** (axonal Na+, presynaptic terminals,
  threshold spiking). **Discussion reflow:** TMS/chronaxie persuasion DEMOTED from 2.5 to Discussion; 2.5
  tightened to the fast-element physics (Landau). **High-freq-tES claim VERIFIED with a real citation:**
  added `esmaeilpour2020` (eNeuro 7(6), DOI 10.1523/ENEURO.0368-20.2020 -- "Limited Sensitivity of
  Hippocampal ... to Unmodulated Kilohertz Electric Fields") supporting the inert-carrier premise; cited in
  2.5 (#6 paragraph) and Discussion.
- Compiles clean via pdflatex+bibtex+pdflatex x2: **25 pp, 0 undefined refs, 0 citation warnings**.
- ENV NOTE: scipy is NOT installed here (PEP 668 blocks pip; venv avoided). `test_jr_demod.py` and the
  scipy-based J-curve scripts can't run in this session; the two NEW scripts are deliberately scipy-free
  (pure-numpy bisection) and ran fine.

## v1.8 — Phase 1 writeup: J-curves woven into the paper
Code had finished Phase 0 #3 (Theory equations-only, PEIX formula, trimmed abstract, deduped slogan,
consolidated predictions) but the J-curves were still referenced NOWHERE. Added the missing capstone:
- New Results subsection **\ref{sec:jcurve} "What the mesoscale adds: coupling sets the gain at fixed
  detection"** (placed before Falsifiable predictions). Presents BOTH J-curves: JR (fig:jcurve, pinned v*
  -> sigma'' fixed, C->C* x27, gain ~1/gamma; input p and coupling C give the same gain-gamma relation) and
  NMM2 (fig:nmm2_jcurve, literal inter-QIF J, exact v^2 rectifier, no pinning, 1/gamma to gamma Hopf).
  Framed band-agnostic: one law in alpha (JR) and gamma (NMM2).
- Added fig_jcurve.pdf and fig_nmm2_jcurve.pdf to the .tex; Discussion tie-in sentence (amplification is
  coupling-tunable, not only state-tunable; sec:jcurve).
- Compiles clean: **24 pp, 0 undefined refs** (two pdflatex passes).
Remaining: #5 timing-not-rate result+fig, #6 direct-kHz panel, Phase 2 (Discussion reflow, compress
nonlinearity catalogue to 3 loci, VERIFY the high-freq-tES claim w/ citation, final Landau pass).

## v1.8 — Phase 0 (#3) structural reorg + PEIX + abstract/slogan/predictions (latest)
Finished the rest of Phase 0. Theory (§2) is now **equations-only**: the three results figures
(fig_carrier, fig_khz, fig_operating_point) were moved out of §2.3--2.5 into Results; Theory now
forward-references them. The dead §4.3 stub ("...shown above") is replaced by two real Results
subsections, "Carrier independence and the kHz roll-off" (hosts fig_carrier + fig_khz) and "The
operating-point law and the Σ″ control" (hosts fig_operating_point). Added a Results opening topic
sentence naming the JR→LaNMM→NMM2 progression. **PEIX defined** with the actual normalized-slope
formula in §2.4: PEIX(v*) ≡ Σ′(v*)/Σ′(v0) = sech²[(r/2)(v*−v0)] ∈ (0,1] (Eq. eq:peix), maximal at
the inflection where the demod gain ∝Σ″ vanishes; side from sign(v*−v0). **Abstract trimmed** (dropped
the 712× parenthetical and the Arnold-tongue/interpolation result-dump; now ends on the square law +
LaNMM/NMM2 confirmation). **Slogan deduped to exactly two** full "wherever a fast-enough nonlinearity…"
occurrences (abstract "samples" + conclusion "sees"); the Discussion's third copy removed and the
factorization sentence reworded so the verbatim tail isn't echoed. **Predictions consolidated** into a
new Results subsection §4.8 "Falsifiable predictions and tests" (carrier@fixed-pol, PEIX/sign-flip,
frequency-selectivity+state-dependence — each with a one-line experimental test); the Discussion
predictions paragraph is now a pointer to §sec:predictions. Author line was already filled (not a
placeholder). Compiles clean: **23 pp** (was 22; +1 from the PEIX eq + predictions list), 0 undefined
refs, 0 citation warnings. Native Edit works on the Dropbox path in Claude Code. Backup at
/tmp/TN0484_prePhase0_3.bak.tex. **Repo now on GitHub (private): github.com/giulioruffini/TI-demodulation-paper.**
Remaining Phase 0: figure→script table (#6). Then Phase 1 writeup (weave J-curves into "what the
mesoscale adds"; timing-not-rate; direct-kHz panel) and Phase 2 (Discussion reflow, catalogue compress,
verify high-freq-tES citation, final Landau pass).

## v1.7 — Phase 0 (a): carrier claim corrected throughout
Reframed "carrier independence" as **independence at fixed post-coupling polarization epsilon**, with the
applied-field threshold rising with f_c via epsilon=kappa(f_c)E_0 (reconciles with the experimental
consensus; the network signature is f_c-independence once polarization is matched). Edited 6 spots:
abstract, intro, sec 2.2 (the third prediction), sec 2.3 opening, sec 2.5 opening, Discussion falsifiable
predictions. Compiles clean: 22 pp, 0 errors/undefined refs. (Edits via python string-replace: Write/Edit
tools are blocked on the Dropbox path, only bash writes persist; backup at /tmp/TN0484.bak.tex.)
Remaining Phase 0: structural reorg (figures Theory->Results, equations-only Theory), define PEIX, trim
abstract, dedup slogan, consolidate predictions, author line, figure->script table. Then weave in J-curves.

## v1.6b — decision: J-curve bands
Keep JR at alpha (~11 Hz) and NMM2 at gamma (~50 Hz); frame the pair as ONE band-agnostic
J-amplification law shown in two native bands (mirrors the LaNMM two-band story). No retuning.

## v1.6 — NMM2 J-curve refined & well-defined (latest)
Cleaned the bumpy NMM2 J-curve. Decisions that matter for the writeup:
- **No pinning needed (key insight):** in NMM2 the field enters the v_E membrane *linearly* and the
  rectifier is the exact v_E^2 term whose quadratic coefficient = 2 is a HARD CONSTANT, independent of
  the operating point. So unlike JR (where detection = sigma''(v*) must be pinned), NMM2 detection is
  structurally fixed; we just sweep J at fixed eta and only gamma changes. (Pinning v_E* via eta(J) was
  tried and INVERTS the path -- eta swings dominate, Hopf moves to J~14 -- so we do NOT pin.)
- **Exact algebraic fixed point** (s=r, z=0; solve r_e,r_i) -> smooth, no settle transient.
- **Resonance-peak readout:** f0 drifts with J and two gamma modes (~50/55 Hz) swap which is least-damped,
  so driving at the eigenfreq (branch swap) or a fixed freq (off-resonance dip) both bump. Reading the
  PEAK lock-in over a Delta f window (40-58 Hz) is mode-agnostic -> clean monotonic curve.
- Result (eta=0): gamma Hopf at J*=16.66; sweeping J 13->16.6, gamma 0.049->0.0014, peak demodulated r_E
  grows ~13x; gain ~1/gamma then saturates. `code/nmm2_jcA.py` (engine+algebraic FP+gamma eig),
  `code/nmm2_jcD.py` (peak grid + figure) -> `figures/fig_nmm2_jcurve.{png,pdf}`.
- Infra note: background nohup runs get culled between tool calls in this session; algebraic FP makes the
  whole sweep run FOREGROUND in ~4.5 s. (Claude Code suggested for heavier compute loops -> no 45s cap.)

## v1.5 — J-curve (network amplification) prototyped in BOTH NMM1 and NMM2 (latest)
New result for the revision: **amplification is controlled by network coupling J, at fixed detection.**
- **JR (NMM1)** `code/jr_jsweep_engine.py` + `run_jcurve.py`/`run_res.py`/`make_jfig.py` -> `figures/fig_jcurve`.
  Trick: vary global connectivity C(=J) and analytically co-solve external drive p(C) to PIN the
  operating point v* (=8.30) so sigma''(v*)=-0.151 and A_open=6.74e-3 are CONSTANT. As C->C*=136.6,
  gamma 10.7->0.28, demodulated A_Omega grows 27x (0.024->0.63 mV); resonance sharpens; gain ~1/gamma then
  saturates. Input knob p and coupling knob C collapse onto ONE gain-vs-gamma curve.
- **NMM2 (exact MPR PING)** `code/nmm2_jc.py` -> `figures/fig_nmm2_jcurve`. Here J=C is the LITERAL
  inter-QIF mean coupling, and the rectifier is the exact v^2 (coefficient structurally fixed = no
  sigma'' to pin). At eta=0 the gamma Hopf in J is at C*~16.5; sweeping C 10->16.5, gamma 0.139->0.002,
  lock-in of r_E grows ~80x (1e-4->7.9e-3). Gamma eigenpair tracked (30-80 Hz band) for gamma.
  Microscale-grounded version of the JR result; parallels Clusella tACS-vs-J amplification.
- Honest scaling claim: ~1/gamma in the weakly-damped regime, saturating near the Hopf (both models).
- Status: prototypes confirmed, code+figs in repo. NOT yet woven into the .tex. Phase 0 (text) still pending.

## v1.4 — revision plan adopted (Landau reorg + new science); see docs/plan.md (latest)
Colleague review + Giulio's refinements -> revision roadmap in `docs/plan.md`.
- **Phase 0 (text):** restate carrier independence as epsilon-independence (post-membrane
  polarization), not applied-field independence; make A_Omega ~ |H_m(f_c)|^2 roll-off
  explicit (reconciles with the consensus that required field rises with f_c). Move all
  results figures out of Theory into Results (equations-only Theory). Add JR->LaNMM->NMM2
  progression sentence. Define PEIX. Trim abstract. Dedup the slogan. Consolidate
  falsifiable predictions into a Results subsection. Fix author line. Figure->script table.
- **Phase 1 (sims):** (1) network amplification vs coupling J (Clusella-style; separates
  detection sigma'' from network amplification); (2) timing-not-rate (AC at Delta f amplified
  ~omega_0/2gamma near Hopf, DC rate shift not -> matches Vieira 2024; NMM2 phase/order
  parameter); (3) direct kHz single-column run with fast-element coupling explicit.
- **Phase 2:** Discussion reflow (receive 2.5 TMS/chronaxie material), framing consistency,
  verify high-freq-tES claim w/ citation, Landau pass, recompile, commit.
- After Phase 0: submittable-correct + well-organized. Phases 1-2: strong.


## v1.3 — NMM2 fixed with Raul's authoritative model; §4.6 back in, faithful (latest)
Raul handed over the source (`../raul code/`: `qifnmm.f90` AUTO continuation + matching
`ping_nmm2.py` direct integration + `qif_bif2.py` bifurcation plot). Verified our
reconstruction was wrong in **four** ways — every τ-scaling of the canonical
(dimensional) MPR form had been dropped, *and* the wrong knob was swept:
  1. **Bifurcation parameter is η̄** (common background drive, in BOTH E and I) — there is
     NO separate excitatory current `I`. (Raul: "I don't use I, just eta".)
  2. Curvature term is `(π·τ·r)²`, not `π²r²` (τ² ≈ 225× for E was missing).
  3. Δ term in the r-equation is `Δ/(π τ)`, not `Δ/π` (one τ short).
  4. Synaptic coupling is `+C·A·s` added to dv̇ directly (C=15, A=(1,1,1,2)) ⇒ current
     `τ·C·A·s`, not `J·s/τ` with J=(1,1,1,2) (~225× too weak).
- Rewrote `code/nmm2_ping.py` to Raul's exact equations (η̄ as bifurcation axis, field as
  additive current on the E membrane). Reproduces the published bifurcation: **supercritical
  Hopf at η̄≈1, gamma onset f₀≈54 Hz, peak r_e≈0.53 at η̄≈11**, gamma limit cycle for η̄≳1.
  Independent numpy-RK4 check matched (no hysteresis → genuinely supercritical).
- Regenerated `fig_nmm2_resonance` (stable focus η̄<1: forced resonance ~54 Hz growing
  toward the Hopf; limit cycle η̄>1: entrainment, diagonal ridge 56→83 Hz) and
  `fig_nmm2_map` (log color, bright diagonal ridge from the Hopf, η̄ axis). ~52 s.
  Stable-side curves show a small genuine double-peak near 50/54 Hz (PING coupled modes —
  converged under 5× longer windows and invariant to carrier, so not an artifact).
- **Paper §4.6 + Methods updated** (both copies): Eq. (nmm2-ping) → Raul's dimensional
  form; "constant excitatory drive I" → "common background drive η̄"; `(Δf,I)`→`(Δf,η̄)`
  plane; f₀ ~70→~55 Hz; params now Δ=1, C=15, A=(1,1,1,2); captions I→η̄. §4.6 no longer
  held — it is now faithful. Repo + Overleaf recompile clean: 22 pp, 0 undefined refs.
- Supersedes the v1.2 hold below. `NMM2_question_for_Raul.{md,tex,pdf}` retained for record.

## v1.2 — NMM2 reconstruction found UNFAITHFUL; held pending Raul
- Longer-window check (Claude Code + independent long-settle scan here) vs the
  Rosetta Stone PING bifurcation (Fig. 7.3, Eq. 7.9): `nmm2_ping.py` produces NO limit
  cycle in I∈[−20,75] (published model: large gamma cycle HB⁺≈1→HB⁺≈68, peak r≈0.53 at
  I≈11) and wrong r-scale. The earlier "I≈11 Hopf, f0~70 Hz, entrainment" was a slow
  transient — INCORRECT. Reconstruction can't be pinned from the text (dimensional
  conventions of τ_e/τ_a/τ_i/τ_g, (πτr)² term, Δ vs Δ/π, coupling τ-scaling, r units).
- ACTION: do not ship NMM2 §4.6 figures; held pending exact Eq. 7.9 model + source from
  Raul. See docs/NMM2_question_for_Raul.md. NMM2 conceptual content (§2.1 + Methods,
  derived v²) is independent and stands. LaNMM + JR results unaffected (faithful).
- Paper currently still contains the unfaithful §4.6 (not yet pulled) — flagged, awaiting
  decision once Raul provides the model.
- LaNMM regenerated (the faithful part of the handoff): `lanmm_resonance.py` windows
  `t_settle 1.5→8.0 s` / `t_meas 1.5→16.0 s`, grids `MU 16→41`, `DF 23→45` (`dt=5e-4`
  kept). Smoother single-peaked stable-focus curves (~10 Hz alpha), clean limit-cycle
  side, speckle-free log ridge; ~49 s for the whole grid. Alpha Hopf re-confirmed at
  drive ≈ 390 by an independent long-window field-free scan (pk-pk vP1 ~6.4 mV @ drive
  180 → ~1.75 mV @ 352 → ~0.46 mV @ 387, stable above) — `I_HOPF=390` unchanged, no
  LaNMM caption/prose edits. `fig_lanmm_resonance.{png,pdf}` + `fig_lanmm_map.{png,pdf}`
  rewritten. `nmm2_ping.py` and `fig_nmm2_*` reverted to original short-window state so
  they stay consistent with the (not-yet-pulled) §4.6. Repo paper recompiled: 22 pp,
  0 undefined refs, 0 missing figures.


## v1.1 — three models now show the SAME resonance curve + map (latest)
- Added NMM2 PING equations to Methods (Eq. nmm2-ping, two-population E–I) and
  simplified the §2.1 single-pop MPR eq to the clean Montbrió form for consistency.
- Added LaNMM resonance curve + map (fig_lanmm_resonance, fig_lanmm_map) so JR,
  LaNMM (NMM1), and NMM2 each display the parallel pair (curve + heatmap):
  JR fig:res/map, LaNMM fig:lanmm_res/map, NMM2 fig:nmm2_res/map. LaNMM was missing
  the resonance curve (had only Arnold tongues).
- New self-contained module code/lanmm_resonance.py: vectorized fixed-step 28-state
  LaNMM (transcribed params), P1 driven directly, lock-in of vP1 at Δf over
  (Δf, P1-drive). Alpha Hopf ~ drive 390 (high drive=stable focus, low=alpha cycle);
  resonance peaks at ~10 Hz (fixed alpha, like JR — contrast NMM2's diagonal/shifting
  gamma ridge). Map uses log color (limit-cycle entrainment >> stable forced response).
  ~1.7 s for the whole grid (vs solve_ivp per-point timing out).
- Paper 22 pp, 0 undefined; Overleaf + NMM-Beats patched identically (surgical,
  anchor-based) and both compile clean.


## v1.0 — third model added: exact mean-field NMM2 PING (gamma) (latest)
- New self-contained module code/nmm2_ping.py: two-population E–I PING in the exact
  next-generation mean field (MPR + second-order AMPA/GABA synapses), parameters from
  the Rosetta Stone PING bifurcation table (eta=0, Jee=Jei=Jie=1, Jii=2, tau_E=15,
  tau_I=7.5, tau_AMPA=10, tau_GABA=2.5, Delta=1). Verified: supercritical Hopf near
  I≈11, gamma onset f0~70–75 Hz. AM field drives the excitatory current; the exact
  quadratic v^2 term is the (derived) square-law demodulator.
- Two figures (analogs of the JR resonance curve + map): fig_nmm2_resonance (stable
  focus forced resonance growing toward the Hopf + limit-cycle entrainment) and
  fig_nmm2_map (ridge along f0(I), DIAGONAL — the resonant freq rises with input I,
  a signature of NMM2's dynamic/state-dependent transfer, unlike static-sigmoid JR).
  Carrier fc=300 Hz (moved from 200 to avoid the fc/2 lock-in artifact).
- Added Results §4.6 "Exact mean-field confirmation: the NMM2 PING gamma generator"
  to TN0484 (surgical, anchor-based patch applied identically to Overleaf + NMM-Beats
  copies, which remain byte-identical). Cites montbrio2015/ruffini2021nmm2/clusella2023.
  Compiles clean, 20 pp, 0 undefined. Paper now spans JR (NMM1 single) → LaNMM (NMM1
  laminar) → NMM2 PING (exact mean-field).


## v0.9 — LaNMM fully integrated into one paper (latest)
- Restructured TN0484 from "JR paper + LaNMM addendum" into a single integrated
  study with two models. The standalone §"Realization in the LaNMM" is removed;
  its content is redistributed:
  - Theory §2.1 now introduces BOTH models (minimal JR column for analysis +
    two-band LaNMM for the biophysical realization), so both are on the table up
    front.
  - Methods §4 now carries the LaNMM protocol: the AM-drive Eq.(lanmm_drive),
    28-var integration (RK45), the alpha-band Hilbert read-out, the two sweeps
    (A×Δf tongue; f_c×Δf carrier map), and fig_lanmm_setup.
  - Results §5.1 "Confirmation in a two-band laminar column" holds the Arnold-tongue
    findings + the two tongue figures (double resonance vs carrier independence).
  - Abstract/Intro/Discussion reworded: LaNMM is a RESULT of this paper, not future
    work. Limitations updated (still phenomenological κ(f_c), single deterministic
    noiseless column). Bumped to v0.6 on the title block, 18 pp, 0 undefined refs,
    0 bibtex warnings.

## v0.8 — merged WP0040 (LaNMM Arnold tongues) into TN0484
- Folded the WP0040 note "Envelope Resonance and Nonlinear Arnold Tongues in a
  LaNMM" (Ruffini & Palma) into TN0484 as a new §"Realization in the LaNMM".
- Brought over 3 figures from WP0040 (reused PNGs as-is): fig_lanmm_setup,
  fig_lanmm_arnold_p2 (P2-stim tongues + carrier×beat map), fig_lanmm_arnold_p1
  (P1-stim). Captions rewritten; notation harmonized to TN0484 (A, Ω=2πΔf, ω_c);
  band-power (Hilbert) metric noted as the phase-robust entrainment read-out.
- Key unifying point made explicit: P2-injection needs a DOUBLE resonance
  (carrier≈40 Hz gamma AND beat≈10 Hz alpha); P1-injection is carrier-INDEPENDENT
  (broad band) — the two coupling limits of §3. Updated Discussion "extension to
  LaNMM" from future-work to realized (§ref). 18 pp, 0 undefined.
- New refs: Sanchez-Todo 2023 (LaNMM), Esmaeilpour 2021, Violante 2023, Gordon 2019.
- Stored a clean LaNMM figure script: code/lanmm_arnold_tongues.py. Aligned to the
  REAL repo API (github.com/giulioruffini/LaNMM_predictive_coding_paper): uses
  lanmmv11.get_intrinsic_params / get_driving_params / lanmm_ode_unified (verified
  signatures; readout vP1=u1+u2+u3+u11, vP2=u6+u7+u8+u12). Dropped the non-existent
  `analysis_utils` (alpha power computed inline via butter+Hilbert). Noted that the
  repo's built-in 'am' mode is noise-AM (HAM), so the deterministic single-tone AM
  for Arnold tongues drives the ODE directly. Added a carrier_map() for panels (c,d).
  Only external dep: lanmmv11.py (not bundled).
- TODO: WP0040 had a Taylor-typo (cubic vs quadratic) — our text uses the correct
  σ'' quadratic, so nothing to import. Author line still placeholder.

## v0.7 — longer lock-in windows
- Resonance figures regenerated with longer measurement windows (deterministic
  model, so this is about transient settling + lock-in/beat resolution, not noise):
  - `fig_resonance`: 10 s settle / **20 s measure** + finer Omega grid. Stable-side
    peaks unchanged (0.70/0.43/0.23 mV — confirms convergence); limit-cycle side
    de-beated and smooth. Generated by `code/rerun_resonance.py` (stable|cycle|plot).
  - `fig_resonance_map`: window 10 s / 8 s in `analyses_v2.py`; ridge sharper/
    brighter near the Hopf (max 0.828 -> 0.852 mV) — old 2.5 s window under-resolved it.
- Other figures unaffected (open-loop / field-free / robust): demodulation, carrier,
  operating-point, kHz, verification, bifurcation — re-run, identical.
- Pipeline hygiene: `make_figures.py` no longer makes fig_resonance (would clobber the
  long-window version); fig_resonance is now solely from `rerun_resonance.py`. Removed
  redundant `map_rerun.py`. Methods text updated (3–20 s window). PDF recompiled (15 pp).

## v0.6 — repo reorg + NMM primer
- Folder restructured for GitHub: `paper/` (tex+pdf, figures/ via \graphicspath),
  `code/` (all .py; run from here; figures saved to ../paper/figures/),
  `docs/`, `archive/` (superseded v1), top-level `README.md` + `.gitignore`.
- Added Theory §2.1 "Neural mass models and the Jansen–Rit circuit": NMM primer
  (linear synaptic operator L̂ / alpha function, PSP summation, sigmoid transfer
  function) borrowed from the Rosetta Stone paper; JR model + Table moved up from
  Methods to situate the theory. Field coupling tied to δV_m = λ·E (Rosetta).
- References double-checked/fixed: Opančar et al. 2025 (was mis-keyed "khatoun");
  Budde et al. 2023 (J Neural Eng) for the peripheral "no envelope" paper;
  Soroushi et al. 2025 full authors; HAM title "Neural encoding through HAM";
  added Rosetta Stone (Castaldo, de Palma, Clusella, Garcia-Ojalvo, Ruffini, arXiv:2512.10982).
- Conclusion now emphasizes the near-bifurcation requirement (gain ∝ 1/γ) and
  full state dependence (σ''(v*) and γ both state-set; efficacy is a brain-state
  property, largest near criticality, tunable/sign-reversible via operating point).
- Fixed 737× → 712× (linearization control) consistently. 15 pp, compiles clean.

**Goal.** Demonstrate that a sigmoidal (firing-rate) nonlinearity in a
second-order-synapse neural mass demodulates a high-frequency
amplitude-modulated (AM) "field" and that, near a Hopf bifurcation, the
recovered low-frequency envelope drives a sharp resonance. Motivation:
temporal interference (TI) stimulation, where the brain is exposed to a
high-frequency carrier whose envelope beats at a low (e.g. alpha) rate.

## Files
- `jr_analysis.py` — locates the Jansen-Rit (JR) Hopf in the external input `p`
  via fixed-point + Jacobian eigenvalues. Result: **supercritical Hopf at
  p ≈ 315 Hz, f₀ ≈ 11.1 Hz**.
- `jr_demod.py` — vectorized RK4 JR integrator. AM field injected into the
  pyramidal output-sigmoid argument. Hann-windowed lock-in at the envelope
  frequency Ω. Produces `sweep_results.npz`. `lin=(v_op,S1)` linearizes the
  field sigmoid (control). `steady_v` returns field-free operating point + slope.
- `make_figures.py` — builds the three figures and runs the verification suite.
- `fig_resonance.{png,pdf}` — headline: resonance curves (response @Ω vs Ω) for
  three distances to the Hopf, stable-focus side (forced resonance) and
  limit-cycle side (entrainment).
- `fig_demodulation.{png,pdf}` — sanity: input AM has lines only at f_c, f_c±Ω
  (no power in alpha); output shows a strong peak at Ω≈11 Hz.
- `fig_verification.{png,pdf}` — square-law (slope≈2) and linearized-sigmoid control.
- `TN_demod_resonance.tex` / `.pdf` — the Technical Note.

## Key settings
JR standard params (A=3.25, B=22, a=100, b=50, v0=6, e0=2.5, r=0.56, C=135).
Carrier f_c=100 Hz; modulation m=1; field ε=0.3 mV (linear regime) for sweeps,
ε=1.0 for the sanity trace. dt=2e-4 s; settle 10 s, measure 3 s.
Stable side p∈{330,355,395}; limit-cycle side p∈{310,290,265}.

## Verified
- Square-law: log–log slope of response vs ε = **1.99** (theory 2).
- Nonlinearity essential: nonlinear 1.40 mV vs linearized 0.0019 mV (**737×**).
- Resonance peak at f₀≈11.1 Hz; stable-side peak grows monotonically as p→Hopf.

## v2 additions (TN0484)
- `analyses_v2.py` + `figures_v2.py`: concept schematic (radio analogy),
  bifurcation+sigmoid panel, 2-D resonance map (Ω×p), carrier-independence
  (+ synapse transfer function), operating-point/σ'' law.
- `test_jr_demod.py`: derivatives, fixed point, square law, linear control — all pass.
- `TN0484_envelope_demodulation.tex/.pdf`: 10-page TN with full TI-literature
  background, radio analogy (Nahin 2001), carrier independence, complete methods,
  proper bioRxiv refs (LaNMM 2025.03.19.644090; HAM 2025.11.03.686310).
- `README_Code.md`: full code documentation.
- Verified v2: carrier-independent over fc=25–300 Hz; A_Ω ∝ ½σ''(v*)ε²m
  (open-loop matches theory; null at inflection).

## v0.3 additions
- E-field coupling stated explicitly: φ=σ(v+λE(t)), quasi-static, direct
  (membrane band-pass neglected) — TN §3.1.
- Lock-in metric clarified + made robust: demean before quadrature projection
  (removes DC leakage). integrate() and openloop_lockin() updated; resonance
  numbers unchanged, operating-point null cleaner.
- `khz_analysis.py` + `fig_khz` (normalized to τ→0, starts at 10^0): soma
  τ_m≈16 ms (corner ~10 Hz) → demod dead at kHz (~1e-5); axon/AIS/node
  τ≈0.2 ms (corner ~800 Hz) → still ~0.14 at 2 kHz, ~0.04 at TMS 3.9 kHz.
  Same membrane LP attenuates TMS at the soma (~-52 dB @3.9 kHz); TMS/TI both act
  via fast elements. Fast-element demodulation + near-Hopf resonance = plausible
  kHz TI. All strongly state-dependent (σ''(v*) and 1/γ). Refs: Barker 1991,
  Peterchev 2013.
- Concept figure (Fig 1) fixed: 4 distinct stage waveforms (AM→rectified→filtered→envelope).
- TN0484 v0.3 compiles with zero undefined references (12 pp).

## v0.4 additions
- New §3.5 "Subthreshold and modulatory: stochastic resonance at high-gain
  compartments": TMS (suprathreshold) vs tES/TI (subthreshold/modulatory);
  cable polarization dV~E*Leff*cos theta (terminals/AIS polarize 2–10× soma);
  SR / spike-timing bias near threshold; population sigmoid = mean-field SR
  device; evidence hierarchy (supported→plausible→unproven). 13 pp, refs clean.
- Refs added: Rahman 2013/2017, Chakraborty 2018, Aberra 2023, Liu 2018
  (NatComms — 5 tES mechanisms incl. stochastic resonance), Reato 2010,
  Terney 2008, van der Groen 2016.

## v0.5 additions (14 pp)
- KEY MESSAGE highlighted in Summary (abstract) and Conclusion: "wherever a
  fast-enough nonlinearity sees the carrier, the population sigmoid demodulates
  and the network amplifies."
- NETWORK framing throughout: each mass = ~10^4 neurons; mean-field sigmoid +
  emergent near-Hopf resonance = network read-out/amplification (not single-cell).
- New Discussion paragraph "Candidate loci for the demodulating nonlinearity
  (the 'wherever')": fast Na at nodes/AIS, Na-inactivation conduction block,
  persistent Na (NaP, axonal resonance), presynaptic terminals (capacitive
  carrier integration + nonlinear Ca-release), spike-threshold SR, cell-type/
  geometry. Refs: Wang/Aberra/Grill/Peterchev 2023 (J Neural Eng), Vieira/Krause/
  Pack 2024 (Nat Commun — TI alters spike timing in primate).

## v0.6 — editorial pass (Kaiti review) — 15 pp
- Title → conditional/professional: "A neural-mass mechanism for TI envelope
  demodulation: sigmoid curvature and near-Hopf amplification."
- Claims softened to conditional ("a neural-mass sigmoid CAN demodulate ... IF a
  residual high-frequency polarization reaches the firing-rate nonlinearity").
- Biophysical bridge made explicit (Eq): E(t) → δV_m=κ(x,θ,fc)E(t) → σ(v+δV_m)
  → resonance; ε DEFINED as post-coupling polarization, κ(fc)=λ|H_m(fc)|.
- Differentiator phrased carefully (Kaiti): population sigmoid is a coarse-grained
  summary of single-cell nonlinearities but a DISTINCT mesoscopic nonlinearity;
  consistent with Caldas-Martinez 2024 ("TI largely a network phenomenon").
- PEIX defined: normalized SLOPE index (∝σ'); distinguished from demod gain (∝σ'').
- KILLER CONTROL added: signed operating-point figure verifies A_Ω=½σ''(v*)ε²m
  incl. SIGN REVERSAL + zero at inflection (openloop_inphase()).
- 100 Hz testable-regime paragraph: accessible test (mild membrane attenuation),
  trade-off = less inert outside focus than kHz.
- New refs: Caldas-Martinez 2024 (Commun Biol), Vieira 2024, Wang/Aberra/Grill 2023.
- Added §1.5 "Prior work: neural-mass models as AM radios (SEC, EEC, HAM)":
  short background on the two Ruffini 2025 papers — CFC/predictive-coding
  (SEC = signal→envelope, EEC = envelope→envelope; error eval = demodulation)
  and HAM (nested-envelope multi-layer AM, constant-Q bands, 1/f). Framing:
  this TN turns that inward AM machinery OUTWARD to an external TI carrier.

## v0.5 — preprint editorial pass — 14 pp
- Restructured for natural reading: Introduction / Theory (3 subsecs) /
  Biophysical realization / Methods / Results / Discussion / Conclusion.
- Converted all bullet/description/enumerate lists and \paragraph-header blocks
  into flowing prose (literature mechanisms, "two ingredients", kHz/SR/Discussion).
- Figures placed [t!] near first reference (concept §1; carrier+opp §2; khz §3;
  bif §4; demod/res/map/ver §5).
- Fixed consistency: linearization control is 712x (1.40->0.0020 mV), not 737x
  (abstract + verification caption updated to match regenerated figure).
- Cited grimbert2006 (JR bifurcation) so no uncited refs.
- NOTE: author line still placeholder "Giulio Ruffini and ...." — fill before circulation.

## TODO / next
- Port the demo to the LaNMM (alpha + gamma): demodulate to either band by
  choosing Ω; sit near HB⁺₁ at μ_P1≈364 (paper TN0384 / Sanchez-Todo 2023).
- Response-vs-amplitude / modulation-depth curves; noise + heterogeneity;
  biophysical membrane pre-filter of the carrier.
- git init + commit/push.
