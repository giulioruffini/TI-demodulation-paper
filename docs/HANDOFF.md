# HANDOFF — TN0484 (what's left)

Living handoff between the Cowork session and Claude Code (and Giulio).
Full chronological detail is in `docs/current_state.md` (newest on top, now v1.21).
Last manuscript state: **25 pp, compiles clean (pdflatex x2 + bibtex), 0 undefined refs,
0 bibtex warnings.** Latin Modern (classic) font; supplementary figures appendix AFTER
the bibliography.

## 0. DO THIS FIRST — commit & push
The entire Cowork session's edits are ON DISK but **NOT committed** (the Cowork sandbox
git is blocked on the Dropbox `.git`; all edits were made via verified python
string-replace, with backups in `/tmp/TN0484.*.tex`). From Code/terminal:

    git add -A
    git commit -m "Session: Nature-style abstract+title, tACS supplement (Fig S3), metrics/subcritical notes, Rosetta cite, Landau pass"
    git push

GitHub currently has only up to `246afa9` (pre this session). Push before migrating
(see section 4) or work will be stranded in the Dropbox copy.

## 1. Open tasks (priority order)

1. **[DONE v1.22] Above-Hopf entrainment supplementary figure (S4).** (`code/entrain.py` -> Fig.~S4 `fig:entrain`.) Originally: The new metrics note in
   sec:jcurve and the Discussion assert the supercritical behavior but we don't show it
   in our own column. Build, in the JR engine (`code/jr_jsweep_engine.py` /
   `tacs_jsweep.py` style): push the column ABOVE the alpha Hopf (autonomous limit
   cycle), drive with a direct Delta f sinusoid, sweep (Delta f, amplitude).
   - Panel (a): the 1:1 Arnold tongue (locking region where dominant output freq = Delta f),
     a wedge anchored at the Hopf, widening with drive.
   - Panel (b): oscillation-amplitude modulation vs locking range -> shows that above the
     Hopf "amplification" = entrainment, not 1/gamma.
   Add as Fig. S4 in the appendix; one sentence in sec:jcurve. (Cowork can do this; ~1 fig.)

2. **[P1] LaNMM Arnold-tongue figures (re-render / restyle / merge).** Source module
   `lanmmv11.py` is in https://github.com/giulioruffini/LaNMM_predictive_coding_paper
   (`python/lanmmv11.py`). `code/lanmm_arnold_tongues.py` needs it on PYTHONPATH.
   - Re-render `fig_lanmm_arnold_p1.png` and `fig_lanmm_arnold_p2.png` in the paper style
     (Latin Modern, neblue), ideally MERGED into one 2x2-of-2 figure so the two main-text
     floats become one (the merge we could not do in Cowork for lack of data/runtime).
   - **Do this in Code** (28-var column, 2-D sweeps, external module -> exceeds Cowork's
     45 s shell limit).

3. **[P2] Final read-through / QA.** One whole-`.tex` pass to catch anything the many
   string-edits left rough (broken sentences, dangling refs, doubled words). Recommend a
   subagent. Then a clean compile.

4. **[P3] Optional polish.**
   - Abstract is ~252 words (Nature-accessible but long); can cut to ~180 if a hard limit.
   - Figure->script reproducibility table (maps each fig to its generating script).
   - Orphaned bib entries `terney2008`, `vandergroen2016` (citations removed in the Landau
     pass; harmless, unsrt drops them) -- delete from `references.bib` if tidying.

## 2. What's DONE this session (don't redo)
- Carrier claim reframed: independence **at fixed polarization**; applied-field threshold
  rises with f_c (reconciles with consensus). Theory is equations-only; figures in Results.
- New science woven in: **J-curve** (coupling sets the gain at fixed detection: JR pinned-v*
  Fig `jcurve`, NMM2 literal-J Fig `nmm2_jcurve`); **timing-not-rate** (Fig `timing`);
  **direct-kHz** run (Fig `khz_direct`); **tACS shares the amplifier** (Fig S3 `tacs`,
  `code/tacs_jsweep.py`) + Discussion paragraph.
- Notation: sigmoid slope renamed `r -> \rho` (was colliding with firing rate); PEIX defined;
  units/American-English uniform.
- Nature-editor pass: accessible **abstract** (no notation), new **title** ("The cortical
  column as a tuned receiver: ..."), intro hook + "Here we show..." + full 3-model roadmap,
  declarative figure titles.
- Subcritical clarifications (stable focus, gamma>0) + the metrics note (entrainment vs
  forced-response lock-in) in jcurve/tacs/timing captions and sec:jcurve.
- Methods paragraph added for the coupling sweeps (pinned-v* p(C), Jacobian) covering
  Figs jcurve/timing/tacs (fixes the missing S3 methods).
- Rosetta Stone cite updated to PUBLISHED: Physics Reports **1189**, 1--49 (2026),
  doi:10.1016/j.physrep.2026.05.004 (Crossref-verified). Key `ruffini2025rosetta` kept.
- Title block refreshed (Date 2026-06-17, v0.7); intro grammar fragment fixed;
  dominant-mode (center-manifold) caveat added; de-hedged.
- Figures moved to a **Supplementary appendix AFTER references** (S1 lanmm_setup, S2
  lanmm_map, S3 tacs). Font fixed to Latin Modern via `\usepackage{lmodern}`.

## 3. Workflow notes
- Cowork edits: python string-replace (Edit/Write blocked on the Dropbox path); pdflatex
  available in-sandbox; background processes get culled between calls (run foreground or
  poll within one call). In **Code**, native Edit + git + long runs all work -- prefer it
  for heavy sims and bulk edits.
- Reproduce coupling-sweep figs (fast, foreground): `cd code` then `python3 run_jcurve.py`
  / `run_res.py` / `make_jfig.py` (JR J-curve, needs scipy); `python3 nmm2_jcD.py` (NMM2);
  `python3 tacs_jsweep.py` (tACS, pure numpy); `python3 timing_not_rate.py` (pure numpy).
  NOTE: `scipy` may be absent in some envs -> `pip install --user scipy` or a venv.

## 4. Migration out of Dropbox (Giulio asked)
Dropbox + git is fragile (sync races, `.git` object corruption -- the very reason Cowork's
git was blocked). Move to a plain local dir backed by GitHub:

1. **Commit & push first** (section 0). Confirm GitHub has the latest.
2. Clone fresh OUTSIDE Dropbox, to a path WITHOUT spaces:
       cd ~/repos      # or any non-Dropbox location
       git clone git@github.com:<you>/<repo>.git tn0484-ti-demod
3. Verify it builds: `cd tn0484-ti-demod && pdflatex ... && bibtex ... && pdflatex x2`.
4. Stop using the Dropbox copy (archive or delete it) so you never edit two trees.
5. (Optional) keep Overleaf in sync via its GitHub integration instead of Dropbox.

Do NOT just `mv` the live folder while uncommitted changes exist and Dropbox is mid-sync;
commit/push, then clone clean. Check `code/nmm2_ping.py` FIGDIR (`../paper/figures`) vs the
actual `figures/` layout after migration and fix if needed.
