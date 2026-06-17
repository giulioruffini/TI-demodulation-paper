# current_state — NMM envelope-demodulation / resonance demo

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
