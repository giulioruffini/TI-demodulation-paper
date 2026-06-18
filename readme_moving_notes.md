# readme_moving_notes.md — handoff for the post-Dropbox repo

**For:** the next Claude Code session (and Giulio) working in the fresh clone.
**Repo (hub of truth):** https://github.com/giulioruffini/TI-demodulation-paper (private).
**Why this file:** the project left Dropbox/Overleaf. GitHub is now the single source of
truth. This file is the operational + planning handoff so work resumes cleanly.

---

## 0. First thing every session — sync discipline
The only recurring hazard left is **two Claude surfaces editing the same paper**
(Claude Code + Claude Desktop/Cowork). Rule:

- `git pull --rebase` **before** doing anything.
- commit + push **when you finish**.
- **Never run both surfaces on the same files at once.** Pick one "active" surface per session.
- After every batch of `.tex` edits: rebuild and confirm `0 undefined refs` before committing.

## 1. One-time setup in the new clone
```bash
# clone lives at a no-spaces path, e.g. ~/dev/TI-demodulation-paper
cd ~/dev/TI-demodulation-paper
python3 -m venv .venv && source .venv/bin/activate
pip install numpy scipy matplotlib
pip freeze > requirements.txt        # commit this (see task C)
echo ".venv/" >> .gitignore
```
Why: the old Dropbox/system Python had **no scipy** (PEP 668 blocked `pip`). Several
scripts need it (`jr_demod.py`, `jr_jsweep_engine.py`, `khz_analysis.py`, `test_jr_demod.py`).
The newer scripts (`qif_raster.py`, `timing_not_rate.py`, `khz_direct.py`) are scipy-free.

## 2. Build the paper
```bash
pdflatex TN0484_envelope_demodulation && bibtex TN0484_envelope_demodulation \
  && pdflatex TN0484_envelope_demodulation && pdflatex TN0484_envelope_demodulation
```
Last known good: **29 pp, 0 undefined refs, 0 citation warnings.**
`.bbl` is committed (so a single `pdflatex` works without bibtex if refs unchanged).

## 3. Repo map
- `TN0484_envelope_demodulation.tex` — the manuscript (root).
- `references.bib`, `*.bbl` — bibliography.
- `figures/` — all figures (`.pdf` used by LaTeX; `.png` are previews).
- `code/` — simulations + figure generators (numpy/matplotlib; some need scipy).
- `docs/current_state.md` — running changelog (newest on top). **Read its top entries first.**
- `docs/plan.md`, `docs/HANDOFF.md` — older planning notes.

---

# NEXT STEPS — the three goals

> Do a **fresh full read of the `.tex` first.** It has changed a lot recently (new title,
> Nature-style abstract/intro, tACS "shares-the-amplifier" extension, QIF microscale
> appendix, entrainment figure). My earlier Landau review predates most of that.

## A. Finalize the paper — organization, logic, Landau style (crisp, logical, no bull)
1. **Logical spine check.** Confirm the ladder reads cleanly: problem (AM needs a
   nonlinearity) → factorization (sigmoid *detects*, network *amplifies*) → JR (closed
   form) → LaNMM (two bands) → NMM2 (derived rectifier) → J-curve (coupling sets gain) →
   timing-not-rate → QIF spikes (appendix) → tACS (shares the amplifier). Every section
   should earn its place; cut anything that restates a neighbor.
2. **Repetition audit (Landau).** Earlier counts: "fixed polarization" ~7×,
   "state-depend*" ~7×, "inert" ~4×, "1/γ" ~18×. State each qualifier once, sharply, then
   reuse the term. Re-count after the recent rewrites.
3. **Caption ↔ body de-echo.** Captions should be self-contained; body should add, not
   repeat. (The operating-point paragraph was a known offender; re-check after edits.)
4. **Figure organization.** ~21 figures is a lot. Decide main-text vs supplement;
   candidates to merge: the two LaNMM Arnold-tongue figures; the three "ridge sharpens
   toward the Hopf" maps (JR / LaNMM / NMM2) may not all need to be in-line.
5. **Abstract length.** Nature-style rewrite is in; check it against the target venue's
   word limit (offer a ~180-word cut if needed).
6. Verify framing stays "complementary, not alternative" throughout.

## B. Redo figures at higher resolution + consistent style
- **Vector PDFs are already resolution-independent** — the crisp wins are: (i) the
  **raster PNG** figures embedded in LaTeX (`fig_lanmm_setup.png`,
  `fig_lanmm_arnold_p1.png`, `fig_lanmm_arnold_p2.png`) — re-render at **300 dpi** or, better,
  vectorize to PDF; (ii) bump all `savefig(dpi=150)` → **300** for any PNG that ends up in
  the document.
- **Adopt one shared style** (a `code/figstyle.py` or `matplotlibrc`): fonts/sizes,
  the house palette (neblue `#0a4f8c`, nered `#b3361f`, negreen `#1a9850`), consistent
  panel labels `(a)(b)(c)`, axis label sizes, and a standard text-width figure size.
- Regenerate everything through the scripts (needs the venv from §1).

## C. Beautiful, documented, reproducible code repo
- **Top-level `README.md`**: what the paper is, how to set up (venv), how to build the PDF,
  and a **figure → script table** (the long-standing TODO). Draft table + status below.
- **Fix stale output paths.** Several older scripts still `savefig("../paper/figures/...")`
  — that directory no longer exists. Point everything at `figures/` (use the
  `FIGS = os.path.join(os.path.dirname(__file__), "..", "figures")` pattern the newer
  scripts use). `make_jfig.py` and `tacs_jsweep.py` write to the CWD — redirect to `figures/`.
- **One-command reproduce.** Add `code/run_all.py` (or a `Makefile`) that regenerates every
  figure in order, so the figure→script mapping is executable, not just documented.
- **Audit for dead/duplicate scripts** before polishing: e.g. `nmm2_jc.py` vs `nmm2_jcA.py`
  vs `nmm2_jcD.py`; `analyses_v2.py`/`figures_v2.py`/`jr_analysis.py`/`make_figures.py`/
  `rerun_resonance.py` (old single-column pipeline) — keep the live ones, archive the rest.
- **`.gitignore` policy:** decide on build artifacts. Candidates to ignore (regenerable):
  the main `.pdf` (~5 MB, re-committed each build → history bloat) and `code/*.npz`.
  Keep `.bbl` (collaborators may not run bibtex). Confirm with Giulio before changing,
  since co-authors may want the rendered PDF in-repo.
- **`requirements.txt`** committed; keep `test_jr_demod.py` green (needs scipy).

### Figure → script table (draft — verify + complete as task C)
| figure | script | status |
|---|---|---|
| fig_demodulation, fig_verification | `make_figures.py` | path `../paper/figures` STALE — fix |
| fig_concept, fig_bifurcation_sigmoid, fig_resonance_map, fig_carrier_independence, fig_operating_point | `figures_v2.py` | path STALE — fix |
| fig_resonance | `rerun_resonance.py` | path STALE — fix |
| fig_khz | `khz_analysis.py` | path STALE + uses scipy — fix |
| fig_khz_direct | `khz_direct.py` | OK (scipy-free) |
| fig_jcurve | `run_jcurve.py`→`run_res.py`→`make_jfig.py` (`jr_jsweep_engine.py`) | make_jfig writes CWD — verify/redirect |
| fig_nmm2_resonance, fig_nmm2_map | `nmm2_ping.py` | path `../paper/figures` STALE — fix |
| fig_nmm2_jcurve | `nmm2_jcD.py` (`nmm2_jcA.py`) | verify |
| fig_lanmm_resonance, fig_lanmm_map | `lanmm_resonance.py` | OK (FIGDIR) |
| fig_lanmm_arnold_p1, fig_lanmm_arnold_p2 | `lanmm_arnold_tongues.py` | OK; **PNG raster → re-render 300 dpi** |
| fig_lanmm_setup | (external/hand-made?) | **PNG raster** — locate source or vectorize |
| fig_timing_not_rate | `timing_not_rate.py` + `make_timing_fig.py` | OK (scipy-free) |
| fig_qif_raster, fig_qif_timing | `qif_raster.py` + `make_qif_figs.py` | OK (scipy-free) |
| fig_tacs_jcurve | `tacs_jsweep.py` | writes CWD — redirect to figures/ |
| fig_entrainment | `entrain.py` (`entrain_crit.py`?) | verify |

---

## Suggested order of attack
1. §1 setup (venv) + §C path fixes + figure→script table → repo is reproducible.
2. Fresh read + §A logical/Landau pass → paper is tight.
3. §B style + 300-dpi re-render → figures are publication-grade.
Commit + push after each coherent step. Keep `docs/current_state.md` updated (newest on top).
