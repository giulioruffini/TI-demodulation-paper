# Figure triage for the JNE build

14 main-text figures against ~14 journal pages is roughly double what the format carries;
JNE papers typically run 6–10. Below is a proposed cut to 9, with 5 demoted or merged. The
supplementary apparatus already exists (S1–S11), so nothing is deleted — only moved.

Selection principle: keep the figures that carry a *distinct* link in the argument, and
demote those that repeat a link already made in another model. The paper's generality claim
rests on the four-model ladder, so each rung keeps exactly one figure.

## Keep in main text (9)

| Fig | Label | Why it is load-bearing |
|---|---|---|
| 1 | `fig:concept` | Orients a readership that spans neuroscience and engineering. Cheap and does a lot of work. |
| 2 | `fig:bif` | Establishes the operating regime and the sigmoid curvature the whole mechanism runs on. Raul's continuation diagram. |
| 3 | `fig:demod` | The central demonstration: an alpha rhythm from a carrier-only input. If one figure survives, this one. |
| 4 | `fig:res` | The amplification half of the thesis — resonance sharpening toward the Hopf. |
| 5 | `fig:carrier` **+ merged `fig:khz_direct`** | Carrier independence is a headline claim in the abstract, so it cannot be supplementary. The two panels answer the same question and belong in one figure. |
| 6 | `fig:opp` | The control experiment: response tracks $\tfrac{1}{2}\Sigma''(v^*)$. This is what makes the mechanism a claim rather than a description. |
| 7 | `fig:lanmm_p2` | Laminar rung of the ladder. |
| 8 | `fig:nmm2_res` | Exact mean-field rung — answers "is this a Jansen–Rit artifact?", which a referee will ask. |
| 9 | `fig:qif_raster` | Microscale rung, and the direct link to the in vivo timing-not-rate observation. |

## Demote to supplementary (5)

| Was | Label | Reason |
|---|---|---|
| 6 | `fig:khz_direct` | Merged into the carrier figure above rather than demoted outright. |
| 10 | `fig:jcurve` | "Coupling sets gain at fixed detection" is a real and separate claim, but it is a refinement of the resonance result rather than a new link. Borderline — the most defensible figure to promote back if we end up with room. |
| 11 | `fig:nmm2_jcurve` | Same claim as `fig:jcurve` in a second model. Redundant once one survives. |
| 12 | `fig:timing` | Same claim as `fig:qif_raster`. The QIF version is more convincing and connects to the in vivo data. |
| 14 | `fig:qif_timing` | Spectral companion to the raster; merge its key panel into `fig:qif_raster` if it fits, else supplementary. |

## Consequences to handle when executing

- Renumber main figures 1–9 and supplementary S1–S16, updating every `\ref`.
- Rewrite the Results text where a demoted figure is currently the subject of a paragraph
  rather than a passing citation — §`sec:jcurve` and §`sec:timing` both need reworking, not
  just a reference swap. This is where most of the ~1,500-word cut can come from, which is
  convenient: the length and figure problems have a common solution.
- `fig:lanmm_arnold` is a PNG (`fig_lanmm_arnold_p2.png`); IOP prefers vector EPS/PDF.
  Regenerating it as PDF is worth doing, and per the memory note the Julia LaNMM engine is
  ~100x faster than the Python path for this.
- Check that every surviving caption is self-contained with no undefined acronyms, which
  IOP requires.

## Open question

Whether to keep `fig:jcurve` and drop to 8 elsewhere. The mesoscale-gain result is one of
the paper's more original claims and demoting it weakens §"What the mesoscale adds". Flagged
for Giulio rather than decided here.
