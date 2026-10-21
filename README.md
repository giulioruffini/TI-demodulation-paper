# TN0484 / WP0185 — The cortical column as a tuned receiver

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.21009618.svg)](https://doi.org/10.5281/zenodo.21009618)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)

**Paper:** *The cortical column as a tuned receiver: a network mechanism for
temporal-interference stimulation* — G. Ruffini, R. Salvador, B. Mercadal,
R. de Palma Aristides, F. Castaldo, N. Grossman, S. Canals, C. Mirasso.
Archived at Zenodo: **[doi:10.5281/zenodo.21009618](https://doi.org/10.5281/zenodo.21009618)**.
Licensed **CC-BY-4.0** (see [`LICENSE`](LICENSE)); machine-readable citation in
[`CITATION.cff`](CITATION.cff).

The current working edition is the **JNE article, v0.15.0-draft21**:
[article](TN0484_jne.pdf), [supplement](TN0484_jne_supplement.pdf), and
[redline against draft20](docs/redline_last_read.pdf).
Run `./build.sh jne` and `./build.sh supp` to update the canonical PDFs.
Giulio's annotated draft20 is preserved in
[the review archive](notes/2026-10-20_kaiti/TN0484_jne_draft20_GR_annotated_before_root_update.pdf).
The separate `build/review/` copies remain unchanged as the completed reader-check
snapshot; the root files are the current reading copies.

The October 21 update adds the approved TI/tDCS/tACS source-amplitude comparison
to the abstract and Section 2.5, distinguishes per-carrier, total-peak, and RMS
matching, and places Ricardo Salvador second in the author records. The journal
article and review redline are rebuilt; the full TN and supplement retain their
previous compiled versions. See the
[revision record](docs/revision_2026-10-21_dc_direct_comparison.md).

Draft21 revises the whole paper for legibility, moves detailed coefficients and
run diagnostics to the supplement, and shortens captions. The approved abstract
was unchanged at that revision. The [revision record](docs/revision_2026-10-20_draft21_legibility.md)
lists the relocations and checks. One abstract and one notation source remain
shared between editions; the full TN will be regenerated at an authorized cut.
Run `python3 code/build_jne_redline.py` to update the review redline against
`e20c047` (draft20), as recorded in
[planning/review_baseline.json](planning/review_baseline.json).

Draft20 integrates Ricardo Salvador's FEM contribution from private-mirror PR #1
(`d779094`) into the reserved Methods 3.3, Results 4.5, and Figure 8. On IXI002,
changing from 2+2 to 1+3 mA moves the envelope focus 2.5 mm anterior and the
mean-square focus 4.5 mm posterior; the quadratic and isotropic beat maps only
rescale by 0.75. These directions hold in all 32 supplied sensitivity combinations.
The reference denominator is all gray matter outside the hippocampal ROI,
including other deep structures. The text and figure identify this definition.
The maps precede detector gain and do not assign excitation or suppression.
The [integration record](docs/revision_2026-10-19_v0150draft20_fem.md) gives the
scope, checks, and remaining author clarifications. The shared abstract is unchanged.
Giulio has confirmed Ricardo's CRediT roles and support through GALVANI ERC
Synergy 855109; the declarations include both without a provisional marker.

Draft19 distinguishes the nonnegative mean-square polarization map from the signed
DC source after detection and the mean response after recurrence. Table 2 includes
the signed source, and Figure S13 adds positive- and negative-curvature examples
using the same positive normalization. The FEM comparison requires detector
parameters for any physiological interpretation of the third map. See the
[signed-map revision record](docs/revision_2026-10-14_v0150draft19_signed_dc_maps.md).

As checked on October 2, [Calliope WP0185](https://calliope.bcom.one/papers/WP0185)
still lists v0.12.0 (July 21). Klaus reports the Overleaf sync completed on
October 9: draft18 source `e17e4a9` is mirrored as `7006e90`, preserving Giulio's
JNE build setting. His standalone build has 42 pages with no errors or undefined
references. On October 14, Giulio authorized sharing draft19 with Ricardo.
The [private GitHub collaboration copy](https://github.com/giulioruffini/TN0484---Temporal-Interference-TI-NMM-demodulation)
now contains draft20 scientific source `1640b2b` as mirror commit `c386e54`, with the
reviewed article, supplement, redline, and integrated FEM contribution. Ricardo's
original commit `d779094` is preserved in its history, and private PR #1 is merged.
His `ricardosalvador123` account has write access, verified October 19. The public
repository, Calliope and Zenodo releases, and circulation to other coauthors
remain held. No separate Overleaf website pull was performed. See the
[October 19 sharing record](docs/share_2026-10-19_ricardo.md).

v0.15.0-draft18 adds Ricardo Salvador (Neuroelectrics) to the author records,
provisionally after Borja Mercadal, with his ORCID and a CRediT line for confirmation.
At that cut the FEM comparison remained a proposed test; draft20 adds the results. See the
[author revision record](docs/revision_2026-10-09_v0150draft18_authors.md).

Draft18 also states the current-ratio steering restriction for the leading
quadratic beat at fixed field shapes and neural state, credits Cassarà's prior
argument, and adds its spatial test. The Violante comparison distinguishes the
reported BOLD contrast from a measured neural beat map. Ricardo's CRediT line
records his contribution to the steering prediction. See the
[steering revision record](docs/revision_2026-10-09_v0150draft18_steering.md).

Draft18 reserved red placeholders for the FEM Methods and a Results subsection immediately
after the JR curvature result, including a framed Figure 8. They described the
planned Violante-montage comparison on an open IXI subject with a FreeSurfer
hippocampal label, including a separate isotropic orientation average, without
reporting FEM findings. Table 4 compares the envelope, quadratic-beat, and DC
scaling predictions for the 1:1 to 1:3 current change. The draft18 Overleaf mirror
was updated; draft20 now fills those locations. See the
[placeholder and handoff record](docs/revision_2026-10-09_v0150draft18_fem_placeholders.md).

v0.15.0-draft14 puts the notation table in the JNE article and separates
overloaded symbols, normalized MPR variables, and physical units. Equation and
figure numbers are retained. See the [notation revision record](docs/revision_2026-10-06_v0150draft14_notation.md).

v0.15.0-draft15 integrates the focality note into Section 2.4: Table 2 compares
the slow signals, means, and excursions of envelope following and quadratic
detection. Both idealized mean maps obey the stated homogeneous-compartment
maximum principle; the supplementary line profile is Figure S13. The existing
two-site example is retained. See the [focality integration record](docs/revision_2026-10-06_v0150draft15_focality.md).

v0.15.0-draft13 uses the supplied 297-word abstract, retaining the DC and coupling
qualifications within the 300-word budget. The body is unchanged from draft12.
See the [revision record](docs/revision_2026-10-06_v0150draft13_abstract.md).

v0.15.0-draft12 installs Giulio's approved abstract framing the mesoscale model
as access, detection, and amplification in series, each with its own test.
The Introduction's closing paragraph and storyline use the same framing.
The DC spatial claim states its homogeneous-compartment and uniform-response
assumptions; independent control of gain is tied to the Jansen--Rit sweep with
a fixed field-free operating point. Theory, Results, figures, and numerical data
are unchanged. See the [revision record](docs/revision_2026-10-06_v0150draft12_abstract.md).

v0.15.0-draft11 integrates the text and numerical findings from Klaus's Landau
review of `0c394df`. It corrects PEIX, citation scope, and access geometry, then
separates the NMM2 critical mode from the competing gamma mode and repeats the
mean-shift-dependent comparisons with genuine two tones. Figure S11 now uses
the two-tone timing sweep; Figure S10 uses the refined mode analysis. The
[text record](docs/revision_2026-10-05_v0150draft11.md) and
[numerical integration record](docs/revision_2026-10-05_v0150draft11_numerics.md)
map the findings, checks, and remaining limits. Author review, declarations, and
release approval remain pending.

v0.15.0-draft10 implements the placement decisions without scientific deletions.
LaNMM methods now accompany their results in Appendix E. The transduction laws
and spatial maps remain in Theory; Methods 3.1 collects the lock-in estimator,
amplitude-slope measurement, and harmonic-gain correction. The equal-RMS carrier
control is Figure 11 in the QIF/PING results; S3, S10, and S11 remain supplementary.
All equations, figure captions, and tables are retained. The
[revision record](docs/revision_2026-10-05_v0150draft10.md) gives the relocation map
and validation; the storyline reflects these placements.

v0.15.0-draft9 adds the DC spatial-map calculation after the reweighting example,
with the homogeneous-conductor and fixed-coupling assumptions stated locally.
It consolidates repeated explanations, reducing the article by 541 prose words
and the supplement by 97 while retaining all figures, equations, tables, and results.
Clean validation builds are 51/34/19 pages (TN/JNE/supplement); only the JNE article
and the fixed-baseline redline are working reading copies. The storyline is updated.
See the [revision and section counts](docs/revision_2026-10-05_v0150draft9.md)
and [pending placement decisions](docs/proposed_removals_draft9.md).

v0.15.0-draft8 credits prior single-neuron TI work for axonal rectification and
identifies the short-time population representation as our contribution. The AIS
remains a candidate; its sodium-channel density does not locate the TI detector.
See [the draft8 record](docs/revision_2026-10-05_v0150draft8.md).

v0.15.0-draft7 organizes the abstract and Introduction around field-to-membrane
access, nonlinear detection, and amplification. Cohen's periaxonal circuit now
appears in the Introduction, access theory, Table 2, and Discussion; the AIS
candidate has a primary sodium-channel reference. Measured decays and assumed
TI parameters are distinguished. The shared-amplifier consequence is scoped to
linear response, with the cached finite-amplitude TI/tACS ratios reported separately.
Record: [docs/revision_2026-10-05_v0150draft7.md](docs/revision_2026-10-05_v0150draft7.md);
redline: [docs/redline_v0150draft6_to_v0150draft7.pdf](docs/redline_v0150draft6_to_v0150draft7.pdf).

v0.15.0-draft6 integrates the half-step cutoff checks. At cutoffs 200 and 400,
the depths become 0.121 and 0.141; the overshoot persists after refinement.
The requested R7 diagnostics are complete, with cutoff convergence retained as
a quantitative limitation. The original figures remain. Record:
[docs/revision_2026-10-05_v0150draft6.md](docs/revision_2026-10-05_v0150draft6.md);
redline: [docs/redline_v0150draft5_to_v0150draft6.pdf](docs/redline_v0150draft5_to_v0150draft6.pdf).

v0.15.0-draft5 adds the spike-cutoff and longer-window checks. At cutoff 200,
the amplitude-10 spiking depth is 0.127 against the mean-field 0.128; at cutoff
400 it is 0.139, so joint cutoff/time-step convergence remains unestablished.
The original-cutoff rasters remain. The matched carrier's apparent 55 Hz depth
falls below 0.0001 with a fourfold longer window, while TI's stays near 0.31.
Record: [docs/revision_2026-10-05_v0150draft5.md](docs/revision_2026-10-05_v0150draft5.md);
redline: [docs/redline_v0150draft4_to_v0150draft5.pdf](docs/redline_v0150draft4_to_v0150draft5.pdf).

v0.15.0-draft4 adds the lower-amplitude spiking comparison and equal-power
mean-field carrier controls as Figure S13. At 10 per tone, the spiking network
has a 55 Hz modulation depth of 0.093 and a 2.8% mean-rate increase; at 35,
rectification induces gamma under either TI or an equal-RMS carrier. The original
Figure 10 and S12 remain. A full-period stability calculation confirms that the
S10 endpoint is attracting, despite the DC-only screen. The spiking–mean-field
depth difference at amplitude 10 is stated explicitly. Record:
[docs/revision_2026-10-05_v0150draft4.md](docs/revision_2026-10-05_v0150draft4.md);
redline against draft3:
[docs/redline_v0150draft3_to_v0150draft4.pdf](docs/redline_v0150draft3_to_v0150draft4.pdf).

v0.15.0-draft3 clarifies the weak-perturbation scope, gives the prose a light
fluency pass, and relabels the QIF rasters as finite-amplitude examples. The
field-on case at background drive 0.85 contains dominant off-beat gamma, so it
is no longer called purely forced. Phase-folded insets now use a common 0–2
scale, and the spectrum uses the stated measurement window. The raster PDF
is reduced from 13.4 MB to 0.49 MB with dense layers rasterized; curves and labels
remain vector graphics. Klaus's E-only stability calculation, independently
reproduced here, attributes the new gamma to the rectified drive shift. An
amplitude-10 mean-field control remains stable. New spiking runs at that amplitude
and equal-RMS unmodulated-carrier controls are proposed to complement the
amplitude-35 threshold-crossing example, which is retained. No original cache
changes. Manuscript builds now publish complete PDFs atomically. Record:
[docs/revision_2026-10-05_v0150draft3.md](docs/revision_2026-10-05_v0150draft3.md);
redline against draft2:
[docs/redline_v0150draft2_to_v0150draft3.pdf](docs/redline_v0150draft2_to_v0150draft3.pdf).

v0.15.0-draft2 integrates the reconstructed kHz two-tone producer, which matches
all seven archived arrays bit for bit. The figure runner plots freshly generated
spectra when recomputing and uses the archived cache with `--from-cache`. It corrects
the input spectral-amplitude units, documents the 4 s settling/4 s measurement run,
and rounds the P1 window difference to 9.6 percentage points. Record:
[docs/revision_2026-10-04_v0150draft2.md](docs/revision_2026-10-04_v0150draft2.md);
redline against draft1:
[docs/redline_v0150draft1_to_v0150draft2.pdf](docs/redline_v0150draft1_to_v0150draft2.pdf).

v0.15.0-draft1 integrates Klaus's reconstructed LaNMM lock-in comparison and
corrects claim scope, gain units, and figure-reproduction paths. The old 7%/25%
claims are replaced by a defined beat average and two-window table. Its kHz producer
gap is resolved in draft2. Section order and all 22 figures are retained. Record:
[docs/revision_2026-10-04_v0150draft1.md](docs/revision_2026-10-04_v0150draft1.md);
redline against v0.14.6:
[docs/redline_v0146_to_v0150draft1.pdf](docs/redline_v0146_to_v0150draft1.pdf).
Versioned review copies are under `build/`; release and circulation remain held.

v0.14.6 reviews v0.14.5 and applies four corrections: the shared-amplifier consequence is
restored in both abstracts, the gate-filter sentence states both halves of K's position,
the Cifra clause says what it is for, and the "not competing explanations" sentence returns
to the Discussion; $\chi^{(2)}$ enters Table 4. Record:
[docs/revision_2026-10-04_v0146.md](docs/revision_2026-10-04_v0146.md); redline against
v0.14.5: [docs/redline_v0145_to_v0146.pdf](docs/redline_v0145_to_v0146.pdf).

v0.14.5 frames weak-field mixing as an effective second-order response that combines
cellular contributions, with QIF as a derived realization. It explains the single-cell
content of the static curve, distinguishes small amplitude from fast relaxation, and
places direct carrier-evoked spiking outside the explanatory scope. It adds the qualified
Cifra citation and fixes the reversed efficiency-trend sentence. All 22 figures, their
order, and the simulation code and parameters are preserved. Record:
[docs/revision_2026-10-03_v0145.md](docs/revision_2026-10-03_v0145.md); redline against
v0.14.4: [docs/redline_v0144_to_v0145.pdf](docs/redline_v0144_to_v0145.pdf).

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
Its source maps v0.15.0-draft20 and records the completed placement decisions.
The
[general practice](../../giulio-personal-handbook/dos-and-donts.md#abstract-and-storyline-planning)
is maintained in the personal handbook.

Smooth weak-input cellular responses generically generate a quadratic beat when their
second-order coefficient is nonzero. The paper represents their combined contribution
through an effective population response and examines its recurrent amplification.
The Jansen–Rit sigmoid supplies a phenomenological realization; NMM2 supplies one derived
from QIF neurons. The spiking network tests that population description, and LaNMM
extends the mechanism to two resonant bands. Direct low-frequency stimulation shares
the amplifier when effective coupling, readout, and operating state are matched.

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
├── TN0484_jne.pdf                        # current JNE working article
├── TN0484_envelope_demodulation.pdf       # TN output, regenerated at an authorized archive cut
├── TN0484_envelope_demodulation.bbl       # committed so a single pdflatex works w/o bibtex
├── references.bib                         # BibTeX source for all references
├── requirements.txt                       # pinned Python deps (numpy/scipy/matplotlib + ...)
├── figures/                               # fig_*.pdf (used by LaTeX) + fig_*.png (preview)
├── code/                                  # all simulation/analysis code
│   ├── run_all.py                         # figure runner with dependency planning
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
./build.sh all
```

Current build: **50 pp (TN), 32 pp (JNE article) + 20 pp (supplement); 0 errors,
0 undefined references or citations, and no overfull boxes.** Bibliography month
macros and shared citation-label warnings are repaired. A float-only page notice
and an underfull bibliography line remain. Builds settle the article/supplement
cross-references and publish complete PDFs by rename. The `.bbl` is committed.

## Reproduce the figures

The driver runs the available data producers before their figure generators.
Selecting a figure with `--only` includes its prerequisites. Scripts that draw a
group of figures still draw that whole group. Use `--dry-run` to inspect the plan
without running calculations or writing files:

```bash
cd code
python run_all.py --list
python run_all.py --only fig_resonance,fig_concept --dry-run
python run_all.py --only fig_resonance --figdir /tmp/tn0484-figures
python run_all.py --only fig_khz_twotone --figdir /tmp/tn0484-khz-figures
python run_all.py --from-cache --only fig_jcurve,fig_khz_twotone --figdir /tmp/tn0484-figures
python run_all.py --figdir /tmp/tn0484-figures  # all available steps; heavy
```

`--figdir` (or `TN_FIGDIR`) redirects figure files. **It does not redirect data
caches:** simulations write into `code/`, including tracked `.npz` files. Run
recomputation in a separate checkout if those files must be preserved. The default
figure directory is `figures/`, whose files are overwritten unless redirected.

`--from-cache` only runs renderers with existing inputs; it never runs an inline
simulation or a data producer. Missing inputs and requests without a cache-only
renderer fail before execution. The uncommitted `analyses_v2.npz` and
`sweep_hi_stable.npz` must first be generated to replot their figures from cache.
The reconstructed two-tone kHz producer writes `code/khz_twotone_reproduced.npz`;
the renderer uses that fresh file in recomputation mode. The archived
`code/khz_twotone.npz` is preserved and supplies `--from-cache` mode. The settings
and exact comparison are recorded in [the recovery note](docs/r12_khz_twotone_2026-10-04.md).
The LaNMM setup diagram is hand-drawn.
The dependency and failure checks run with `python code/test_run_all.py` from the
repository root.

### Figure → script table

23 figures are included by the manuscript, including the complementary Figure 11 (formerly S13). The table records the available scripts
and inputs; it does not assert a fresh rerun of every numerical calculation.
**Available** means the producer or renderer is present; it does not imply
that every simulation was rerun during this revision.

| figure | script | data dep. | scipy | status |
|---|---|---|---|---|
| fig_concept | `figures_v2.py` | analyses_v2.npz† | – | Available |
| fig_bifurcation_sigmoid | `figures_v2.py` | analyses_v2.npz†, jr_bifurcation.npz‡ | – | Available |
| fig_carrier_independence | `figures_v2.py` | analyses_v2.npz† | – | Available |
| fig_demodulation_twotone | `jr_twotone_figs.py` | (inline) | – | Available |
| fig_curvature_twotone | `jr_twotone_figs.py` | (inline) | – | Available |
| fig_resonance | `rerun_resonance.py` (stable/plot) | sweep_hi_stable.npz† | – | Available |
| fig_khz | `khz_analysis.py` | (inline) | yes | Available |
| fig_khz_direct | `khz_direct.py` (imports `timing_not_rate`) | (inline) | – | Available |
| fig_khz_twotone | `khz_twotone_producer.py` + `make_khz_twotone_fig.py` | fresh khz_twotone_reproduced.npz; archived khz_twotone.npz ‡ | – | Available; exact cache reproduction verified |
| fig_jcurve | `make_jfig.py` | jcurve_main.npz, jcurve_res.npz ‡ | (engine) | Available |
| fig_nmm2_map | `nmm2_ping.py` | (inline grid) | – | Available |
| fig_nmm2_resonance_twotone | `make_nmm2_twotone_fig.py` | (inline grid) | – | Available |
| fig_nmm2_jcurve | `make_nmm2_jfig.py` | nmm2_jcD.npz and docs/landau1_nmm2_jcurve_modes_2026-10-05.json ‡ | – | Available; critical-mode source and refined peaks |
| fig_lanmm_field_p1_twotone | `make_lanmm_field_figs.py` | lanmm_field_P1_twotone.npz ‡ | – | Available |
| fig_lanmm_field_p2_twotone | `make_lanmm_field_figs.py` | lanmm_field_P2_twotone.npz ‡ | – | Available |
| fig_timing_not_rate | `make_timing_fig.py` | timing_not_rate_twotone.npz ‡ | – | Available; genuine two-tone data |
| fig_mpr_crossover | `mpr_crossover_fig.py` | ping_fast_carrier_check.json ‡ (from `ping_fast_carrier_check.py`) | yes | Available |
| fig_qif_raster_twotone | `make_qif_figs.py` | qif_raster_twotone.npz ‡ | – | Available |
| fig_qif_timing_twotone | `make_qif_figs.py` | qif_raster_twotone.npz ‡ | – | Available |
| fig_qif_regimes | `make_qif_regimes_fig.py` | original and amplitude-10 QIF caches; ping_carrier_control_traces.npz ‡ | – | Available; controls independently reproduced |
| fig_tacs_jcurve | `tacs_jsweep.py` | tacs_jsweep.npz | – | Available |
| fig_entrainment | `make_entrain_fig.py` | entrain{,_b,_crit}.npz ‡ | – | Available |
| fig_lanmm_setup | — | — | – | **gap**: hand-drawn schematic |

Not included by the manuscript, kept in the repository only: `fig_lanmm_resonance` and
`fig_lanmm_map` (both `lanmm_resonance.py`), archived under `figures/archive/` with a note
on why; `fig_lanmm_arnold_p1`/`_p2` (`lanmm_arnold_tongues.py`), superseded by the
`fig_lanmm_field_*_twotone` maps; the `*_am` variants of the two-tone figures, retained so
the AM-surrogate control of Fig. 4d can be reproduced; and `fig_lanmm_checker.png`, a
diagnostic (gitignored).

† These caches are not committed. `run_all.py` includes their producers when
recomputing the corresponding figures, including when `--only` is used.
‡ Committed data: the corresponding renderer can reuse it without rerunning the sweep.

`khz_twotone.npz`, introduced in commit `a7d6e6f`, is reproduced bit for bit by
`khz_twotone_producer.py --compare`. The reconstructed settings are 4 s settling,
4 s measurement, a 15 μs step, and 0.5 mV per tone, recorded before each RK4 step.
The producer preserves the archive and writes a separate cache with `--write`.
`jr_bifurcation.npz` is imported AUTO continuation data; the raw branch
files and conversion script are in `code/jrnmm_plot/`, separate from the RK4 sweeps.
The legacy `fig_lanmm_arnold_p1/p2` additionally require the external `lanmmv11`
module; the current field-coupled LaNMM figures do not.

### Engines & helpers (not figure generators)

- `figstyle.py` — shared **house figure style**: the Neuroelectrics palette
  (`NEBLUE/NERED/NEGREEN/...`), an `apply()` that sets consistent type sizes / 300-dpi
  output / clean spines, and a `panel(ax,'a')` bold-label helper. Figure scripts opt in
  with `import figstyle; figstyle.apply()`.
- `jr_demod.py` — core JR engine (sigmoid + derivatives, vectorized RK4, AM field,
  lock-in, open-loop detector, Hopf helpers). Imported by the JR pipeline.
- `jr_jsweep_engine.py` — J-curve engine; imported by `run_jcurve/run_res/make_jfig`.
- `nmm2_jcA.py` — NMM2 J-curve engine (imported by `nmm2_jcD.py`).
- `nmm2_jcurve_modes.py --sim` — critical-mode continuation, linear-response grid,
  refined simulated peaks, and the amplitude comparison; consumes `nmm2_jcD.npz`
  and produces the table used by `make_nmm2_jfig.py`.
- `timing_not_rate.py` and `timing_not_rate_twotone.py` — the AM and two-tone
  sweeps; `make_timing_fig.py` renders the latter. `qif_raster.py` integrates the
  **N=8000** QIF network and feeds `make_qif_figs.py`.
- `test_jr_demod.py` — self-checks (derivatives, fixed point, square law, control).

## Numerical integration checks

`code/verify_draft11_numerics.py --json /tmp/tn0484_numerics.json` checks the raw
peak grids, reported ratios, and critical-mode eigenvalues. Its analytical
Jacobian and Hessian independently evaluate the finite-sideband AM and two-tone
beat kernels. It reads the committed caches without changing them. The full
26-point two-tone timing sweep was also rerun and matched its cache exactly;
see `docs/draft11_timing_reproduction_2026-10-05.json`.

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
