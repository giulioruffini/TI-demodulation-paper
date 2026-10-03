# TN0484 / WP0185 — The cortical column as a tuned receiver

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.21009618.svg)](https://doi.org/10.5281/zenodo.21009618)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)

**Paper:** *The cortical column as a tuned receiver: a network mechanism for
temporal-interference stimulation* — G. Ruffini, B. Mercadal, A. Just,
R. de Palma Aristides, F. Castaldo, N. Grossman, S. Canals, C. Mirasso.
Archived at Zenodo: **[doi:10.5281/zenodo.21009618](https://doi.org/10.5281/zenodo.21009618)**.
Licensed **CC-BY-4.0** (see [`LICENSE`](LICENSE)); machine-readable citation in
[`CITATION.cff`](CITATION.cff).

The current local draft is **v0.14.4** (October 3, 2026), in
[TN0484_envelope_demodulation.pdf](TN0484_envelope_demodulation.pdf) and
[TN0484_jne.pdf](TN0484_jne.pdf). As checked on October 2,
[Calliope WP0185](https://calliope.bcom.one/papers/WP0185) still lists v0.12.0
(July 21); the newer local draft remains pending Giulio's review and release.

v0.14.4 is a readability revision of v0.14.3 with no scientific change: the abstract is
stated result-first, one slip in Results 4.1 is corrected (the two-tone input has two lines,
not the surrogate's three), the eigenvalue pair is renamed $\mu_\pm$ and the NMM1 indices
$X\leftarrow Y$, acronyms are expanded at first use, and nine long paragraphs are split.
Record: [docs/revision_2026-10-03_v0144.md](docs/revision_2026-10-03_v0144.md); redline
against v0.14.3: [docs/redline_v0143_to_v0144.pdf](docs/redline_v0143_to_v0144.pdf).

v0.14.3 (October 2) connects the fast-membrane NMM2 limit to a static population transfer
with dynamic synapses, distinguishes carrier access from cellular mixing and circuit
amplification, and adds Nir Grossman to the authors. Cohen's periaxonal study,
Luff's cellular-mixing work, and Raul's unpublished WP0242 manuscript remain cited.
The shorter effective access time is a modeling hypothesis; the plotted simulations
retain their original parameters. All 22 figures are preserved. The revision and
validation record is in [docs/revision_2026-10-02_v0143.md](docs/revision_2026-10-02_v0143.md),
with a [redline against v0.14.2](docs/redline_v0142_to_v0143.pdf).

**Abstract and storyline (October 3).** The inspection document K requested is
[planning/tn0484_abstract.tex](planning/tn0484_abstract.tex) (single-source abstract) and
[planning/tn0484_storyline.tex](planning/tn0484_storyline.tex) (section-by-section argument
map), compiled to [build/storyline/tn0484_storyline.pdf](build/storyline/tn0484_storyline.pdf)
with `~/.claude/skills/paper-storyline/scripts/build_storyline.sh planning/tn0484_storyline.tex`.
It maps the v0.14.4 organization and ends with four decisions for K; nothing is cut or
reordered before his approval. The
[general practice](../../giulio-personal-handbook/dos-and-donts.md#abstract-and-storyline-planning)
is maintained in the personal handbook.

Sigmoid curvature + near-Hopf amplification as a **mesoscopic, network** mechanism
for temporal-interference (TI) stimulation. An amplitude-modulated (AM) field
carries no spectral power at its envelope frequency, so demodulation requires a
nonlinearity. We show that the population firing-rate **sigmoid** of a neural mass
is a square-law demodulator, and that a second-order-synapse network **near a Hopf
bifurcation** resonantly amplifies the recovered envelope. The ladder runs from the
heuristic single-column Jansen–Rit (JR) model, through the laminar **LaNMM** (two
bands), to the exact mean-field **NMM2** (derived rectifier), down to a spiking
**QIF** network, and out to a **tACS** corollary that shares the same amplifier.

> **Key message:** *a nonlinearity mixes the two carriers into a difference-frequency
> component, and the recurrent network near its Hopf amplifies it selectively.* The
> static and dynamic descriptions are connected by their time scales. When membrane
> relaxation is fast relative to the input, the exact mean field reduces to a static
> rate curve; otherwise its mixing coefficient is dynamic. Generation and amplification
> remain separate contributions, with membrane access counted once.

![concept](figures/fig_concept.png)
![resonance](figures/fig_resonance.png)

## Repository layout

```
.
├── README.md                              # this file
├── LICENSE                                # CC-BY-4.0
├── CITATION.cff                           # machine-readable citation (DOI, authors)
├── TN0484_envelope_demodulation.tex       # the manuscript (\graphicspath{{figures/}})
├── TN0484_envelope_demodulation.pdf       # current build (46 pp; JNE article 30 pp + supplement 18 pp)
├── TN0484_envelope_demodulation.bbl       # committed so a single pdflatex works w/o bibtex
├── references.bib                         # BibTeX source for all references
├── requirements.txt                       # pinned Python deps (numpy/scipy/matplotlib + ...)
├── figures/                               # fig_*.pdf (used by LaTeX) + fig_*.png (preview)
├── code/                                  # all simulation/analysis code
│   ├── run_all.py                         # ONE-COMMAND reproduce of every figure
│   ├── figstyle.py                        # shared house style (palette + apply() + panel())
│   ├── archive/                           # superseded/dead scripts (not in the live pipeline)
│   └── ...                                # generators + engines (see table below)
└── docs/
    ├── current_state.md                   # running changelog (newest on top — read first)
    ├── plan.md                            # planning / roadmap
    └── README_Code.md                     # code-level notes
```

## Setup

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt          # numpy, scipy, matplotlib (+ deps)
```

## Build the paper

From the repo root (the `.tex` is at the root; `\graphicspath{{figures/}}`):

```bash
pdflatex TN0484_envelope_demodulation
bibtex   TN0484_envelope_demodulation
pdflatex TN0484_envelope_demodulation
pdflatex TN0484_envelope_demodulation
```

Current build: **46 pp (TN), 30 pp (JNE article) + 18 pp (supplement); 0 errors,
0 undefined references or citations.** Existing warnings about bibliography month
macros and shared citation labels in the split build remain
listed in `todo.md`. The `.bbl` is committed, so a single `pdflatex` rebuilds the PDF
when references are unchanged.

## Reproduce the figures

One command regenerates everything, in dependency order, into `figures/`:

```bash
cd code
python run_all.py                  # full reproduce -> ../figures/ (heavy; overwrites)
python run_all.py --figdir /tmp/f  # preview into a scratch dir (figures/ untouched)
python run_all.py --list           # print the figure->script map and exit
python run_all.py --only fig_jcurve,fig_khz   # rebuild a subset
```

Every generator honors the `TN_FIGDIR` env var (or `--figdir`) and defaults to
`../figures/`. Data producers write `.npz` into `code/`; six of these are committed
so the dependent figures can be rebuilt without re-running the (slow) sweeps.

### Figure → script table (verified)

22 figures are included by the manuscript; the table below is generated against the
`\includegraphics` list and is current as of v0.14.0 (2026-09-22). Status legend:
**OK** = generator writes to `figures/` and runs from committed inputs; **gap** = no
working generator.

| figure | script | data dep. | scipy | status |
|---|---|---|---|---|
| fig_concept | `figures_v2.py` | analyses_v2.npz† | – | OK |
| fig_bifurcation_sigmoid | `figures_v2.py` | analyses_v2.npz†, jr_bifurcation.npz‡ | – | OK |
| fig_carrier_independence | `figures_v2.py` | analyses_v2.npz† | – | OK |
| fig_demodulation_twotone | `jr_twotone_figs.py` | (inline) | – | OK |
| fig_curvature_twotone | `jr_twotone_figs.py` | (inline) | – | OK |
| fig_resonance | `rerun_resonance.py` (stable/cycle/plot) | sweep_hi_{stable,cycle}.npz | – | OK |
| fig_khz | `khz_analysis.py` | (inline) | yes | OK |
| fig_khz_direct | `khz_direct.py` (imports `timing_not_rate`) | (inline) | – | OK |
| fig_khz_twotone | `make_khz_twotone_fig.py` | khz_twotone.npz ‡ | – | OK |
| fig_jcurve | `make_jfig.py` | jcurve_main.npz, jcurve_res.npz ‡ | (engine) | OK |
| fig_nmm2_map | `nmm2_ping.py` | (inline grid) | – | OK |
| fig_nmm2_resonance_twotone | `make_nmm2_twotone_fig.py` | (inline grid) | – | OK |
| fig_nmm2_jcurve | `make_nmm2_jfig.py` | nmm2_jcD.npz ‡ | – | OK |
| fig_lanmm_field_p1_twotone | `make_lanmm_field_figs.py` | lanmm_field_P1_twotone.npz ‡ | – | OK |
| fig_lanmm_field_p2_twotone | `make_lanmm_field_figs.py` | lanmm_field_P2_twotone.npz ‡ | – | OK |
| fig_timing_not_rate | `make_timing_fig.py` | timing_not_rate.npz ‡ | – | OK |
| fig_mpr_crossover | `mpr_crossover_fig.py` | ping_fast_carrier_check.json ‡ (from `ping_fast_carrier_check.py`) | yes | OK |
| fig_qif_raster_twotone | `make_qif_figs.py` | qif_raster_twotone.npz ‡ | – | OK |
| fig_qif_timing_twotone | `make_qif_figs.py` | qif_raster_twotone.npz ‡ | – | OK |
| fig_tacs_jcurve | `tacs_jsweep.py` | tacs_jsweep.npz | – | OK |
| fig_entrainment | `make_entrain_fig.py` | entrain{,_b,_crit}.npz ‡ | – | OK |
| fig_lanmm_setup | — | — | – | **gap**: hand-drawn schematic |

Not included by the manuscript, kept in the repository only: `fig_lanmm_resonance` and
`fig_lanmm_map` (both `lanmm_resonance.py`), archived under `figures/archive/` with a note
on why; `fig_lanmm_arnold_p1`/`_p2` (`lanmm_arnold_tongues.py`), superseded by the
`fig_lanmm_field_*_twotone` maps; the `*_am` variants of the two-tone figures, retained so
the AM-surrogate control of Fig. 4d can be reproduced; and `fig_lanmm_checker.png`, a
diagnostic (gitignored).

† `analyses_v2.npz` is **not** committed — `run_all.py` regenerates it via `analyses_v2.py` first.
‡ committed `.npz` (figure rebuildable without re-running the sweep).

The only remaining **gap** is `fig_lanmm_setup`, an intentionally hand-drawn schematic.
(`fig_lanmm_arnold_p1/p2` additionally need the external `lanmmv11` module to re-run.)

### Engines & helpers (not figure generators)

- `figstyle.py` — shared **house figure style**: the Neuroelectrics palette
  (`NEBLUE/NERED/NEGREEN/...`), an `apply()` that sets consistent type sizes / 300-dpi
  output / clean spines, and a `panel(ax,'a')` bold-label helper. Figure scripts opt in
  with `import figstyle; figstyle.apply()`.
- `jr_demod.py` — core JR engine (sigmoid + derivatives, vectorized RK4, AM field,
  lock-in, open-loop detector, Hopf helpers). Imported by the JR pipeline.
- `jr_jsweep_engine.py` — J-curve engine; imported by `run_jcurve/run_res/make_jfig`.
- `nmm2_jcA.py` — NMM2 J-curve engine (imported by `nmm2_jcD.py`).
- `timing_not_rate.py` — data producer for `fig_timing_not_rate` (writes the `.npz`;
  the figure is drawn by `make_timing_fig.py`). `qif_raster.py` integrates the
  **N=8000** QIF network and feeds `make_qif_figs.py`.
- `test_jr_demod.py` — self-checks (derivatives, fixed point, square law, control).

## Verified

`test_jr_demod.py`: sigmoid derivatives match finite differences (and σ″(v₀)=0);
the field-free fixed point is an equilibrium; square-law slope ≈ 1.99 (theory 2);
linearizing the field-receiving sigmoid collapses the response ≈712×. (Needs scipy.)

## Notes on artifacts

Currently committed: the rendered `.pdf` (re-committed each build), the `.bbl`
(so collaborators need not run bibtex), and the committed `.npz` data files so the
dependent figures rebuild without re-running the slow sweeps. LaTeX build junk
(`.aux/.log/.out/.toc/.blg`), `__pycache__`, `.venv/`, and a few regenerable
intermediate `.npz` are git-ignored.
