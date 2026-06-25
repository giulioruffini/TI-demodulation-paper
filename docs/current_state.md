# current_state — NMM envelope-demodulation / resonance demo

## v1.57 — Clarify what the transfer functions represent (Kaiti's comment) (latest)
Added a short consolidating paragraph after the model definitions ("What the transfer
functions represent"): the demodulating object is a POPULATION input-output map, not a
passive somatic membrane element -- the JR/LaNMM sigmoid (effective transfer, PSP in /
rate out) and the NMM2 exact MPR quadratic play the same role; its curvature is the
mesoscopic trace of cellular nonlinearities, so using Sigma'' (or the derived v^2 term)
as a square-law detector is legitimate at this scale. The membrane low-pass bears on
ACCESS (which fast compartment lets a kHz carrier reach the nonlinear transfer, sec:khz),
not on the legitimacy of the detector. Directly answers the likely reviewer objection
("the membrane low-passes kHz, so how can the sigmoid demodulate?"). Build clean: 34 pp.

## v1.56 — Fig 4 / Fig 13-14 revision, Landau pass, repo cleanup for Zenodo
Figures:
- Fig 4 (fig:res): dropped the misleading above-Hopf lock-in panel (lock-in @ Omega conflates
  the autonomous cycle with the driven response). Now a single fixed-point forced-resonance panel
  + a 1/gamma peak-vs-distance companion. The entrainment story stays in fig:entrain (f_out).
- Fig 13 (fig:qif_raster): beat-fold insets now have proper x/y labels + ticks + off/on legend;
  both folds normalized to their own mean (relative modulation).
- Fig 14 (fig:qif_timing): NEW panel (b) intermodulation spectrum (TI off/on, oscillatory):
  TI-on lights up the direct Df line and the SUM sideband f0+Df~95 Hz; difference ~11 Hz at floor
  (set by the network transfer function, not the mixer). Depth panel renumbered (b)->(c).
Text:
- Defined "fold" at first use (vocab). Unified demodulation as the difference-frequency
  intermodulation product (one quadratic mixer, cascaded: carriers->Df, then Df x f0 -> f0+-Df).
- Clarified the negative-Sigma'' regime is where the JR resting point sits, not a constraint
  (mechanism is sign-agnostic; positive lobe already spanned open-loop in fig:opp).
- Replaced ~14 scattered inline (code: foo.py) mentions with a single "Code and data availability"
  section pointing to the public GitHub repo + Zenodo DOI (repo README has the figure->script map).
- DOI added to title block; author list extended (Palma, Castaldo).
Repo (Zenodo prep):
- Added LICENSE (CC-BY-4.0) and CITATION.cff (DOI, authors, version).
- README: DOI/license badges, citation block, page count 29->34, layout updated.
- Moved internal working notes (HANDOFF.md, stale current_status.md, NMM2_question_for_Raul.*,
  readme_moving_notes.md) to a gitignored _private/ (excluded from the public archive).
Build clean: 34 pp, 0 undefined.

## v1.55 — QIF figure/caption/text consistency audit
Audited Fig 13 (qif_raster) + caption + main-text prose (sec:qif, sec:qif-methods, vocab) for
consistency. Fixes:
- Caption "boxed value is the timing lock-in at Df, off->on" -> "Df modulation depth A_Omega/<r_E>"
  (matches the in-figure suptitle + the boxes; was mislabeled).
- Added panel (b)'s depth (0.76) to its caption sentence (was asymmetric -- only (d) stated 0.19).
- CROSS-FIGURE FIX: autonomous gamma was written ~54 Hz in Fig 13 caption + text but Fig 14a (and the
  data) give 53.3 Hz. Reconciled ALL autonomous-gamma mentions 54->53 Hz and detuning 12->11 Hz
  (53-42). Kept mean-field-Hopf 55 Hz and forced-drive Df=55 (distinct quantities; finite-size note
  explains the offset). Softened forced drive "at" -> "near" the resonance (drive 55, resonance ~53).
- Verified: depths 0.76(b)/0.19(d), 400-of-8000, Df=55/42, mean rate x1.05-1.10 all consistent across
  figure, caption, Fig 14, and prose. grep confirms no residual 54/12 in QIF context.
Build clean: 34 pp, 0 undefined.

## v1.54 — QIF panel (d) inset: proper gamma-amplitude PAC (was an unconvincing raw-rate fold)
Giulio flagged the (d) "r_E folded on Df" inset as unconvincing -- the blue (on) curve showed messy
gamma wiggles, not a clean Df-locked gating bump. Diagnosis: gamma(~54) and beat(42) are near 9:7
COMMENSURATE, so the gamma sits at fixed phases vs the beat and folding the raw rate preserves the
gamma residual no matter how long you average (averaging-more does NOT help). Fix in make_qif_figs.py:
new gamma_amp_fold() -- FFT band-pass r_E around gamma (45-70 Hz), take the Hilbert AMPLITUDE envelope
(numpy-only analytic signal), fold THAT on the beat phase. Taking the amplitude discards the gamma
carrier -> immune to the commensurability. Normalized to the mean (compare modulation depth, not level)
over a longer window (t_start=40 ms). Panel (d) now uses mode='gamma' (PAC); panel (b) keeps the raw
rate fold (forced response IS at Df). Result: (d) blue = sharp beat-phase-locked gamma-amplitude peak
(gating), gray = flat. Caption updated to describe both insets + WHY (d) uses amplitude. Build clean:
34 pp, 0 undefined.

## v1.53 — QIF raster: denser sample so spike "bunching" is visible by eye
Giulio: the QIF raster's blue rate bunched clearly but the black SPIKES read as a uniform cloud.
Cause: only 120 of 8000 neurons shown -> bursts too sparse to form visible bands. Fix in qif_raster.py:
nrec 120 -> 400 (representative random sample, kept eta-UNSORTED). [Tried eta-sorting first; it
backfired -- intrinsic eta-tonic firing makes diagonal stripes even in the OFF panels, muddying the
asynchronous-vs-bunched contrast. Reverted to representative sampling.] make_qif_figs: finer ticks
(ms 2.6->1.7, mew 0.5->0.35, alpha 0.85->0.7). Result: (a) OFF = uniform structureless cloud; (b) ON =
clear vertical spike columns under each envelope peak. Physics identical (same sim; AC/VS/depths
unchanged: forced depth 0.76, gating 0.19). Caption updated 120->400. Regenerated qif_raster.npz.
Build clean: 34 pp, 0 undefined.

## v1.52 — NMM2 two-knob criticality clarified in Methods; SL proof made explicit
- Giulio: Methods only stated eta-bar but Fig 11 shows the role of coupling J. Resolved: NMM2 has TWO
  criticality knobs (like JR's p and C) -- eta-bar (background drive, for the resonance map) and J=C
  (coupling, for the J-curve). Added the J-sweep method to the NMM2 Methods: sweep J at fixed eta-bar to
  the gamma Hopf J* (bisection on the leading eigenvalue), read the r_E lock-in peak; NO operating-point
  pinning needed because the v_E^2 rectifier coefficient is fixed by construction -> sweeping J changes
  only gamma. (The Results already explained this; the gap was Methods-only.) Code: nmm2_jcA/jcD.
- SL appendix proof made EXPLICIT (was a verbal parity argument): plugged in the carrier-harmonic ansatz
  z=sum Z_k e^{i k wc t} (slow envelopes), derived the mode equation Zdot_k=[a+i(w0-k wc)]Z_k - cubic + F_k,
  and showed the odd-k subspace is invariant+attracting (even-k modes have no source -> decay at gamma),
  so z tracks the forcing's Fourier structure (odd harmonics only) and the baseband k=0 component Z_0=0 ->
  zero weight at Df. Contrast: square-law (even) gives a k=0 term. Build clean: 34 pp, 0 undefined.

## v1.51 — predictions-vs-evidence table (honest data confrontation)
#3 (data confrontation), feasible+honest version: added Table tab:predictions to sec:predictions
mapping each prediction -> existing evidence (cited) -> sharp test. Two rows are ALREADY SUPPORTED
qualitatively: timing-not-rate (Vieira 2024, in vivo) and network-not-single-cell read-out (Caldas
2024, synaptic block in vitro); carrier-independence (opancar/peripheral/esmaeilpour) + operating-point
sign-flip (Caldas cell-type) partially supported; frequency-selectivity flagged as a new untested
prediction. Caption notes quantitative reanalysis is future work. NO fabricated data -- a real
quantitative overlay (model curve on digitized published points) would need Giulio to supply the
digitized values (e.g. Vieira fold-changes). Build clean (pdflatex x2 + bibtex): 33 pp, 0 undefined,
0 LaTeX warnings (one pre-existing 2pt overfull in the notation table, negligible).

## v1.50 — promoted QIF to a main Results subsection (resolved the appendix straddle)
Editorial review flagged that QIF straddled -- its figures (13,14) were main but its section/analysis
were in the appendix. Target venue is PLOS Comp Biol / J Neural Eng (modeling-friendly: thoroughness +
figure count are appropriate, no cutting needed). Fix:
- NEW main Results subsection "Microscale confirmation: TI realigns spike timing in the QIF network"
  (sec:qif), after sec:timing -- the full spiking-confirmation analysis (was appendix prose).
- NEW Methods subsection "QIF spiking network (microscale of NMM2)" (sec:qif-methods), after the NMM2
  PING methods -- the network setup/params/metric definition (was appendix prose).
- DELETED the appendix QIF section. Appendix is now cleanly Notation -> Stuart-Landau -> Supplementary
  figures. No dangling app:qif refs. Figs 13/14 unchanged (already main).
Full build (pdflatex x2 + bibtex): 33 pp, 0 undefined, 0 LaTeX/bibtex warnings.

## v1.49 — NEW appendix: Stuart-Landau dissociation (amplifies but cannot demodulate)
Added a tight (~half page + 1 S-figure) appendix "TI requires detection: the Stuart-Landau normal
form amplifies but cannot demodulate" (app:sl). DETECTION ONLY -- no BOLD/FC/readout (separate TN).
- Claim+proof: SL zdot=(a+iw0)z-|z|^2 z+F, AM field, stable a<0. Carrier-harmonic PARITY argument:
  field forces odd k=+-1; cubic z|z|^2 maps odd->odd; linear preserves k => z lives only at odd k,
  zero weight at Df (k=0) to all orders. Corollary: demod is the O(eps^2) square-law (1/2)sigma'' eps^2 m;
  SL has no even-order term => identically zero. SL amplifies ~1/gamma but does not detect.
- NEW code/sl_dissociation.py (pure numpy + figstyle): (a) SL forced in-band -> lock-in ~1/gamma (tACS
  works; weak drive for clean 1/gamma); (b) SL under AM carrier -> Df line at floor (~2e-8) vs square-law
  F^2 control = 0.25 -> ~1e7x gap. fig_sl_dissociation (S-numbered). Confirmed numbers: F^2@Df=2.5e-1
  (matches spec exactly), SL Re(z)@Df~2e-8.
- The dissociation isolates the paper's two ingredients: amplification = universal near-Hopf
  susceptibility (shared w/ tACS); detection = model-specific square-law SL lacks. Reinforces sec:coupling.
- Cites pikovsky2001 (already in bib). Main text UNTOUCHED. Full build (pdflatex x2 + bibtex):
  33 pp, 0 undefined, 0 LaTeX warnings, 0 bibtex warnings.

## v1.48 — strengthened the Conclusion (forward-looking close); abstract judged strong
Reviewed abstract + conclusion. Abstract = strong/near-great (clear hook, problem, population thesis,
known-behavior checklist, state-dependence + AM-radio close) -- left as-is. Conclusion was good but
mostly RESTATED and ended on a mechanism statement; added an elevating third paragraph: testable
(falsifiable predictions, sec:predictions), actionable (dose TI to brain state, not open-loop),
the unifying vision (column as AM transceiver for endogenous CFC -> TI drives it as a receiver,
bookending the intro; cites ruffini2025cfc/ham), and the next steps (realistic kappa(fc), coupled
noisy columns). Build clean: 32 pp, 0 undefined.

## v1.47 — membrane-tau citation (Eyal/Deitcher) + entrainment-vocabulary Methods paragraph
- Membrane time constant (the load-bearing kHz-roll-off number): Giulio supplied the real primary
  sources. Cited Deitcher 2017 (tau_m~12 ms human L2/3) + Eyal 2016; softened the claim to "~12 ms;
  we adopt ~16 ms for the soma" and DROPPED the unsupported ~22 ms upper end. 6 new bib entries.
- NEW Methods subsection "Forced response, entrainment, and gating: vocabulary and metrics"
  (sec:vocab): fixes the overloaded "entrainment" by mapping three distinct senses to three metrics --
  (i) forced response = lock-in/susceptibility (below Hopf: J-curve/timing/tACS); (ii) frequency
  entrainment = dominant-freq f_out pulled to Df, Arnold tongue (S5; f_out vs PLV justified);
  (iii) gating/PAC = Df-locked amplitude of a persisting rhythm (QIF panel d). Reserves "entrainment"
  for (ii), "gating" for (iii) -- self-consistent with the panel-(d) relabel done earlier. Merged the
  old entrainment-construction paragraph in (no duplication). Cites pikovsky2001, lachaux1999,
  canolty2010, tort2010. Build clean (full bibtex): 32 pp, 0 undefined.
- LANDAU logic review of Methods + Results: VERDICT = sound and well-built. The three-rung ladder
  (JR analyze -> LaNMM confirm -> NMM2 derive) is explicit; the J-curve transition names+resolves the
  p-entangles-detection-with-amplification confound; timing-not-rate rests on the G(w0)~1/g vs
  G(0)~1/w0^2 transfer asymmetry (mechanism, not assertion); Methods order matches Results, no orphan
  method/result. One improvement applied: the Results roadmap now previews the two distinctive mesoscale
  payoffs (coupling-sets-gain J-curve, timing-not-rate) instead of only "demodulation + amplification".
  No risky restructure (the argument is well-constructed). Build clean: 32 pp, 0 undefined.

## v1.46 — Fig 12 finer sampling + FIX: restored its real plotter (make_timing_fig)
Giulio: Fig 12 (timing_not_rate) needs more sampling too. While fixing it, found+fixed a bug I had
introduced: make_timing_fig.py is the ONLY plotter for fig_timing_not_rate (timing_not_rate.py writes
the .npz but does NOT self-plot) -- I had wrongly archived it in v1.32 on a bad audit, leaving Fig 12
unreproducible AND the one main figure missing figstyle.
- Restored make_timing_fig.py to code/ (git mv from archive), modernized: figstyle + house palette +
  300 dpi + TN_FIGDIR.
- Finer sampling: timing_not_rate.py C-grid linear(12) -> GEOMETRIC-toward-Hopf(26) via scipy-free
  bisection for C* (same fix as Figs 10/11). Re-ran -> timing_not_rate.npz; Fig 12 now smooth (AC~1/g
  clean; the near-Hopf DC sign-change is resolved, not a sparse jump).
- Fixed the wiring the bad archiving broke: run_all (timing_not_rate=data producer, make_timing_fig=
  plotter), archive/README, main README engine note + figure table. Build clean: 31 pp, 0 undefined.

## v1.45 — Notation/symbol/units table in appendix; notation disambiguated
Added App.~A "Notation and units" (\usepackage{longtable}, Table~\ref{tab:notation}): a full
symbol glossary grouped by category (sigmoid; Jansen-Rit; applied TI field & coupling; network
dynamics/response/bifurcation; LaNMM; NMM2/MPR & QIF), with meaning + nominal units for ~50 symbols.
Disambiguation handled in the head note + by context: A = excitatory PSP gain (JR/LaNMM synapses)
vs the field modulation amplitude (LaNMM drive e(t), and A_f in NMM2/QIF) = the counterpart of the
single-column eps; C = JR connectivity constant vs NMM2 global synaptic gain C(=J). The field-amplitude
family eps/A/A_f is listed on one row as the same physical role per model. Referenced from Methods.
(Did NOT rename A in the LaNMM drive -- the arnold figure axis shows "A" and re-rendering needs the
~2 h lanmmv11 recompute; the table + context is the clean fix.) Build clean: 31 pp, 0 undefined refs.

## v1.44 — readability/pedagogy pass (symbols defined, math intuition, consistency)
Subagent-audited the whole tex for symbols/pedagogy/refs/consistency. Applied the high-value fixes:
- Defined sigmoid params in prose at first use (2e0 max rate, inflection v0, slope rho) -- were only
  in Table 1, ~60 lines later.
- Added intuition to the heaviest math: sigma'' square-law expansion ("squaring multiplies the carrier
  by itself; cos^2 has a DC part -> rectification, like a diode in an AM radio"); the Hopf gain ("near
  the Hopf the network behaves as a single weakly damped harmonic oscillator... textbook resonance
  gain"); the lock-in ("isolates one frequency: multiply by sin/cos and average").
- Beat identity bridge: fc = (f1+f2)/2, Df = f2-f1 (the two-carriers -> AM step was implicit).
- Reconciled the gamma-Hopf numbers: QIF finite-N (eta_Hopf~1.1, f0~54) vs exact mean field (~1, ~55)
  -- now stated as a finite-size offset (was a silent inconsistency).
Build clean: 29 pp, 0 undefined refs. DEFERRED (need Giulio): a primary citation for the human L2/3
membrane time constant (~16 ms) -- none in the bib, won't fabricate; overloaded glyph A (PSP gain vs
drive amplitude) -- left as-is (each locally labeled) to avoid rename risk.

## v1.43 — Figs 10/11 finer sampling; STABLE QIF metric (modulation depth)
- #1: Figs 10 (jcurve) + 11 (nmm2_jcurve) were kinky -- the steep near-Hopf rise was linearly
  under-sampled. Switched both coupling grids to GEOMETRIC-toward-Hopf (28 points, distance-to-Hopf
  geomspace; jcurve closest Chopf-0.3, nmm2 Chopf-0.07). Re-ran run_jcurve + nmm2_jcD; both J-curves
  and their 1/gamma panels are now smooth.
- #2: replaced the realization-noisy off->on lock-in RATIO (was 15-26x, unstable because the
  field-free denominator sits at the lock-in noise floor) with the STABLE Df MODULATION DEPTH
  A_Omega/<r_E> (fractional amplitude of the Df-locked rate oscillation): off 0.01-0.03, on 0.19
  (oscillatory) / 0.76 (forced); mean rate flat x1.05-1.10. Redesigned Fig 14b (off/on depth bars +
  rate annotation), Fig 13 panel annotations (depth), and updated all captions/body + the methods
  metric definition. Build clean: 29 pp, 0 undefined refs.

## v1.42 — figstyle rolled across ALL generators; Methods updated for new params; tidy repo
Completed the artistic pass (#2) + Giulio's "well-organized/documented + Methods updated" ask.
- figstyle.apply() + 300 dpi now in ALL 9 remaining generators (make_jfig, make_nmm2_jfig,
  make_entrain_fig, tacs_jsweep, nmm2_ping, lanmm_resonance, rerun_resonance, khz_analysis,
  khz_direct). Re-rendered every figure to figures/; montage-checked -- no breakage, consistent
  type/spines/palette across the whole 24-figure set. test_jr_demod: ALL TESTS PASSED.
- METHODS updated for the new sim parameters: QIF N=2000->8000 (done v1.41); entrainment window
  f0+-5 -> f0+-12 Hz with the near-Hopf locking ranges now RESOLVED (not grid-clipped; clipped
  points flagged in the figure); the Arnold-tongue panel description updated to the continuous
  lock-in heatmap + outlined locked set.
- DOCS/tidy: README now documents figstyle.py + code/archive/ + the N=8000 QIF; .gitignore now
  excludes regenerable intermediates (analyses_v2/sweep_hi_*/tacs_jsweep .npz) and non-manuscript
  byproducts (fig_lanmm_checker, arnold .pdf). Build clean: 29 pp, 0 undefined refs.

## v1.41 — #1 QIF more neurons: N=2000 -> 8000 (cleaner Fig 13/14)
Giulio's "more neurons" ask. Bumped qif_raster.py N=2000->8000 (ran in just 41 s -- numpy vectorizes
over neurons, no scipy). Cleaner rate traces + crisper raster; qif figs now 300 dpi. Re-rendered
fig_qif_raster + fig_qif_timing, recommitted qif_raster.npz. Fold-changes shifted (the off-baseline
lock-in sits near the noise floor, so the on/off ratio is realization-sensitive): timing now 15-26x
(forced 26, oscillatory 15; was 14-22), mean rate still flat (1.05-1.10x). Updated tex consistently:
N=2000->8000 (x5), 14-22x -> 15-26x (x3), Fig 13(d) ~22x -> ~15x. NOTE: the fold-change metric is
inherently noisy at this precision (tiny off-baseline); the robust claim is timing up >order-of-mag,
rate flat. Build clean: 29 pp, 0 undefined refs.

## v1.40 — figstyle rolled into figures_v2 (5 main figs) + bifurcation declutter (#4)
Applied figstyle + house palette to figures_v2.py: fig_concept, fig_bifurcation_sigmoid,
fig_resonance_map, fig_carrier_independence, fig_operating_point. All 300 dpi, (a)/(b) panel labels
on the 2-panel figs, consistent type/spines.
- #4 DONE: fig_bifurcation_sigmoid (a) decluttered -- removed the 3 stray unlabeled vertical lines
  (incl. the mystery ~p=395); now marks only the two real boundaries SNIC (~120) + Hopf (315),
  shades the alpha-limit-cycle band between them, labels both regions ("alpha limit cycle" /
  "stable focus (resonator)"), legend moved upper-left to avoid collisions. Much cleaner.
Build clean: 30 pp, 0 undefined refs.
Still queued behind arnold (P1, >2h!): QIF N->8k (#1); figstyle on the heavy generators
(nmm2_ping, lanmm_resonance, rerun_resonance, khz_*) + the npz-backed ones (qif/jcurve/entrain/tacs).

## v1.39 — artistic pass begins: house style (figstyle.py) + fig_demodulation/verification restyled
Giulio asked for a picky/artistic figure pass (resolution, more neurons, aesthetics). Critique: palette
inconsistent (fig_demodulation/verification were off-palette #1b3a6b/#c44/#888), the keystone
fig_demodulation cramped + unlabeled, panel-label/typography drift across the 24-fig set, QIF figs run
N=2000 (visible shot noise -> N=6-8k would clean), heatmap grids coarse.
- NEW code/figstyle.py: house palette (NEBLUE/NERED/NEGREEN/NEGRAY/...) + apply() rcParams (type sizes,
  300 dpi, clean spines, frameless legends, color cycle) + panel(ax,'a') bold-label helper. Opt-in import.
- Pilot: fig_demodulation + fig_verification restyled to house style -- big lift: house colors, bold
  (a)-(d) labels, breathing room, annotations ("alpha band empty", "demodulated alpha line", "712x
  smaller"). The keystone existence-proof figure now looks publication-grade. Build clean: 30 pp.
PENDING artistic items (mostly need recompute -> queued behind the busy arnold CPU):
  (i) roll figstyle across the remaining generators; (ii) MORE NEURONS for QIF (N=2000->6-8k) for
  cleaner Fig 13/14; (iii) finer heatmap grids; (iv) declutter fig_bifurcation_sigmoid (unlabeled
  ~p=395 line). Awaiting Giulio's pick on scope/compute.

## v1.38 — Fig 8 (lanmm_arnold_p2, main) re-rendered smooth; P1/S10 still computing
The LaNMM Arnold-tongue Python re-run (with cloned lanmmv11 + bilinear/300dpi) is so slow (~7000
solve_ivp, no npz cache) it took >1 h. It does P2 then P1: fig_lanmm_arnold_p2 (MAIN text Fig 8 --
the one grainy main raster) finished and is now SMOOTH (speckle/streak gone, alpha tongue at ~10 Hz
a clean band). Committed it. fig_lanmm_arnold_p1 (supp S10) is still computing (~45 min more) -- will
commit when it lands. Reproduction note: needs PYTHONPATH=<LaNMM repo>/python and pip tqdm. [The
Julia LaNMM engine would make this seconds -- see memory.]

## v1.37 — Fig 14a QIF<->NMM2 validation: use autonomous gamma (peaks now match)
Giulio spotted that in Fig 14a the QIF peak (~53 Hz) sat ~13% ABOVE the NMM2 mean-field peak
(~47 Hz), contradicting "matched gamma spectrum". Diagnosed: QIF and MF match EXACTLY (53.3 Hz)
in every condition EXCEPT forced_on -- and the panel was built from forced_on. Cause is NOT a bug
or numerics (a fresh mf_run of forced_on gives 53.3 Hz at every dt incl. the coarse 0.05 ms in
nmm2_ping): forced_on is below the Hopf + strong fast drive -> a multi-peak FORCED spectrum where
the "dominant" peak is window-sensitive and QIF/MF can disagree on which peak wins. Fix: validate in
the field-free AUTONOMOUS condition (entrain_off), a single clean gamma in both -> peaks now overlap
at ~53 Hz (fundamental + ~107 Hz harmonic), mean rate 0.052/0.052. Updated panel-a title ("matched
autonomous gamma"), the Fig 14 caption ("field-free (autonomous) state ... both ~53 Hz"), and the
panel-b regime label "Entrained"->"Oscillatory" (consistency). No science changed; the validation is
now honest and tight. Build clean: 30 pp, 0 undefined refs.

## v1.36 — Methods subsections + MPR-equation spacing fix + explicit Rosetta cite
- Methods now has 5 subsections separating the models/methods (was one undivided wall):
  Single-column Jansen--Rit (integration, lock-in, controls); Laminar two-band (LaNMM); Exact
  next-generation mean field (NMM2 PING); Coupling sweeps/timing/tACS (JR); Entrainment above the
  Hopf (JR).
- MPR equation (eq:nmm2-ping) "weird spacing" diagnosed + fixed: (i) the \tfrac{\Delta}{\pi\tau}
  fractions rendered shrunken/text-style next to full-size display terms -> switched to inline
  \Delta/(\pi\tau_E); (ii) the two-column layout had a wide uneven mid-gap from \qquad -> tightened
  to \quad + \\[2pt] row spacing. Now clean.
- NMM2 methods now explicitly attributes the formulation to the Rosetta Stone paper
  \cite{ruffini2025rosetta} (+ Montbrio-Pazo-Roxin \cite{montbrio2015}) up front.
Build clean: 30 pp, 0 undefined refs.

## v1.35 — Q3: promoted fig_qif_timing to main; cloned LaNMM for arnold re-render
- Q3 (Giulio agreed): promoted fig_qif_timing from supp (S1) to MAIN (now Fig 14, right after the
  qif_raster Fig 13) -- the quantitative 14x/22x timing-not-rate proof belongs in main with its raster,
  not buried. Added a main-text reference in sec:timing; removed the block from app:qif (which still
  references both QIF figures). All other appendix figures shift down one S-number. Build clean: 30 pp,
  0 undefined refs.
- Q2 follow-through: cloned github.com/giulioruffini/LaNMM_predictive_coding_paper to /tmp, pip-installed
  tqdm (lanmmv11 dep), regenerating fig_lanmm_arnold_p1/p2 with PYTHONPATH=.../python -- the bilinear+300
  dpi fix now applies to the main-text grainy raster (Fig 8) too. [arnold re-render in progress]

## v1.34 — Q2 raster resolution: bilinear heatmaps + 300 dpi; Q3 main/supp audit
- Q2: root cause of "grainy" heatmaps = imshow(interpolation="nearest") -> blocky cells. Switched all
  four map generators to interpolation="bilinear" + dpi 300 (nmm2_ping, lanmm_resonance,
  lanmm_arnold_tongues, figures_v2). Regenerated the two self-contained ones: fig_nmm2_map (S11) and
  fig_lanmm_map (S3) -- now smooth (speckle gone, ridges clean). figures_v2/fig_resonance_map (S6) and
  lanmm_arnold p1/p2 (S10 + main Fig 8) got the code fix but NOT regenerated: resonance_map needs
  analyses_v2.npz (uncommitted), and the arnold tongues need external lanmmv11 (absent) -> ASKED Giulio
  to provide lanmmv11.py. fig_nmm2_resonance (main Fig 9) + fig_lanmm_resonance (S9) re-rendered as a
  side effect, identical content (deterministic, line plots).
- Q3 main/supp audit: split is 13 main + 11 supp (S1-S11). Main recommendation: fig_qif_timing (S1, the
  QUANTITATIVE 14x/22x timing-not-rate proof) is in supp while its qualitative raster (fig_qif_raster,
  Fig 13) is in main -> backwards; promote/merge. Also fig_lanmm_arnold_p2 (Fig 8) is the lone grainy
  main raster (blocked on lanmmv11) -- if uncleanable, swap LaNMM's main representative to the cleaner
  map/resonance and move tongues to supp. Rest of the split is well-judged. [pending Giulio's decision]
Build clean: 30 pp, 0 undefined refs.

## v1.33 — Fig 13 (d) relabeled: gating/PAC, NOT entrainment (Giulio's dynamical-systems catch)
Giulio's precise critique: QIF panel (d) is NOT entrainment in the dynamical-systems sense -- the
~54 Hz gamma is NOT frequency-pulled to 42 Hz (still ~8 bursts/150ms, not ~6); it persists and is
amplitude-GATED at the 42 Hz beat. The 12 Hz detuning is OUTSIDE the 1:1 Arnold tongue, so by
construction you get forced cross-frequency gating (PAC), not frequency locking. Worse, the paper used
"entrained" for BOTH this (amplitude lock) AND the S5 fig_entrainment (genuine Arnold-tongue FREQUENCY
lock) -- same word, two jobs, a referee magnet. Fix (his option 1, the stronger/more-novel framing):
- Relabeled the QIF above-Hopf regime "Entrained" -> "Oscillatory" (panels c/d, caption, methods,
  qif_timing caption, body). Effect now "the TI beat gates the gamma (Df-PAC)", explicitly "forced
  cross-frequency gating (PAC), not frequency entrainment", contrasted with the genuine locking of
  fig_entrainment (S5). Demodulation surviving above the Hopf as envelope-to-rhythm coupling -- ties to
  the HAM/CFC story.
- Reserved "entrainment" for genuine frequency locking (S5 + JR/LaNMM/NMM2 limit-cycle resonance panels).
  Changed the loose "entrains timing" -> "locks timing" in the abstract and sec:timing (forced Df-locking,
  no oscillator to entrain below the Hopf).
- Fixed two now-stale code cites exposed by the archiving: dropped jr_analysis.py (Methods) and
  make_timing_fig.py (sec:timing). Build clean: 30 pp (gating explanation added a page), 0 undefined refs.

## v1.32 — Results §4+§5 merged; dead/dup scripts archived
- Merged Results §4 (operating-point Sigma'' law) and §5 (square-law + linearization control)
  into one subsection "The nonlinearity is the detector: the Sigma'' curvature law and its
  controls" -- saves a heading, tightens the JR-verification block (fig:opp then fig:ver flow
  as one argument). Build clean: 29 pp, 0 undefined refs.
- Archived (git mv, not deleted) to code/archive/ with a README: jr_analysis.py (dead, prints
  only), nmm2_jc.py (superseded by nmm2_jcA/jcD), make_timing_fig.py (redundant with
  timing_not_rate.py). None imported or in run_all. Orphaned nmm2_jcurve.npz left in code/
  (harmless; live fig_nmm2_jcurve uses nmm2_jcD.npz).

## v1.31 — Fig 13 entrainment inset + gamma-band Df clarified; Track B reassessed (latest)
- Fig 13 (qif_raster): per Giulio, the entrained raster (c)/(d) did not make the locking
  visually obvious (gamma ~54 Hz and beat 42 Hz are close -> amplitude-gating, not a frequency
  shift). Added a beat-phase-folded inset to each TI-ON panel (b,d): r_E folded on the Df cycle,
  FLAT off (gray) vs a clear BUMP on (blue) -- the textbook "is timing locked?" view. Caption +
  methods updated; Df kept as the beat, detuning (Df-f0 ~ 12 Hz) stated as a distinct quantity.
- Discussion: added the explicit, testable band-targeting prediction -- optimal Df tracks the
  target's intrinsic rhythm (~10 Hz alpha, ~40-55 Hz gamma/PING), so TI's Df should follow
  regional spectral anatomy (justifies the large Df in the NMM2/QIF figures).
- TRACK B REASSESSED (figures already publication-grade): fig_demodulation and all vector PDFs
  are crisp at in-document size -- the earlier "cramped" critique was a low-res PNG-preview
  artifact, not a real issue. The only raster PNGs (fig_lanmm_arnold_p1/p2) are ALREADY ~300 dpi;
  their "graininess" is genuine heatmap DATA noise (would need re-running with lanmmv11, absent, to
  de-speckle). fig_lanmm_setup is a 175-dpi hand-drawn schematic (acceptable). => the moving-notes
  "re-render at 300 dpi" worry is already satisfied; Track B is effectively done/blocked.
Build clean: 29 pp, 0 undefined refs.

## v1.30 — Landau pass: de-echo (caption<->body) + cut repeated explanations (latest)
First Landau-style tightening pass (subagent-audited the whole tex for repetition/echo).
Highest-value cuts made (all verbatim/near-verbatim restatements, not term-reuse):
- sec:jcurve: the "stable-side 1/gamma vs autonomous-side entrainment" contrast was stated
  ~4x in one paragraph -> compressed to one clean statement + the timing-not-rate pointer.
- Discussion: dropped the factorization appositive (the sentence before already spelled it out).
- fig:entrain caption: cut the duplicated "entrainment enhanced near criticality" sentence.
- Body<->caption de-echo: trimmed fig:carrier, fig:khz_direct, fig:demod body sentences that
  restated their self-contained captions (the "+60x / three kHz routes / synthesized" details
  now live only in the captions).
- sec:nmm: collapsed the 3-way restatement of "curvature is cellular, network only amplifies"
  to one sentence; sec:carrier: carrier-independence re-derivation -> back-ref to sec:coupling.
Counts: "fixed polarization" 4, "inert" 4, "state-depend" 6, "1/gamma" 29->28 (bare token; the
real win is fewer repeated EXPLANATIONS). Abstract ~250 words (fine for most venues; a ~180-word
cut available if a strict limit applies). Framing "complementary not alternative" is clean (2x,
stated once sharply). Build clean: 29 pp, 0 undefined refs. Deferred (lower priority): minor
vieira/lanmm-opening near-repeats (audit line refs were stale); a deeper spine/flow pass.

## v1.29 — figure persuasiveness audit + rebuilt the two weak (entrainment) figures (latest)
Reviewed all 24 figures against the claim each carries. Verdict: the below-Hopf forcing
story (1/gamma amplification) is airtight everywhere (operating_point is the standout --
measured vs 1/2 sigma'' eps^2 m overlap exactly incl. sign flip); the WEAK figures were both
the above-Hopf ENTRAINMENT (supercritical) side, exactly as Giulio flagged. Rebuilt both:
- **fig_qif_raster (c)/(d):** the old caption oversold "gamma re-timed to the TI beat", but
  gamma persists at ~54 Hz and its bursts are amplitude-GATED at the detuned 42 Hz beat (only
  11 Hz apart -> no clean visual separation exists; a band-pass/Hilbert overlay leaks gamma).
  Honest fix: drop the misleading overlay, annotate each panel with the Df lock-in fold-change
  (forced 14x, entrained 22x off->on). Reworded caption + body: "gamma bursts gate to the TI
  beat ... intrinsic gamma persists" (no more "re-timed/realign").
- **fig_entrainment (rebuilt from scratch):** was the weakest figure AND the last repro gap
  (no committed plotter/data). New make_entrain_fig.py + upgraded sims:
  (a) CONTINUOUS lock-in Arnold tongue (was binary blocks) w/ 1:1-locked white contour;
  (b) clean SYMMETRIC frequency-locking staircase (old one had an unexplained discontinuity);
  (c) criticality sweep with a WIDE +-12 Hz Df window so near-Hopf locking ranges are NOT
  grid-clipped -> now monotonic (locking range 5.3->15 Hz as dist 100->2; cycle amp 2.96->1.06).
  entrain.py/entrain_crit.py made path-robust + finer grids; entrain*.npz now COMMITTED.
REPRO STATUS: only ONE gap left -- fig_lanmm_setup (hand-drawn by design). fig_entrainment +
fig_nmm2_jcurve both resolved. run_all/README updated. Build clean: 29 pp, 0 undefined refs.
Presentation (B-track) backlog noted: fig_demodulation cramped; lanmm_arnold p1/p2 grainy raster.

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
