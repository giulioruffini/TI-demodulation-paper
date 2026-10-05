# v0.15.0-draft6: half-step cutoff checks

The baseline is draft5 (`20a8f82`). Klaus's `f1831cd` is integrated as `5ecc5ac`.
The Methods, QIF Results, S13 caption, and storyline now include the half-step
comparison. Abstracts, figures, equations, citations, section order, and original
caches remain unchanged.

At drive 0.85, amplitude 10 per tone, N=8000, with the same settling and windows:

| Cutoff | Depth at dt=0.0025 ms | Depth at dt=0.00125 ms | Change on halving dt |
|---:|---:|---:|---:|
| 100 | 0.0926385 | 0.0927872 | +0.16% |
| 200 | 0.1269358 | 0.1207956 | -4.84% |
| 400 | 0.1393291 | 0.1408129 | +1.06% |

The mean-field depth is 0.1277363. Field-free rates remain unchanged to four
significant digits, and the rate rises remain 2.8–2.9%. Cutoff dependence persists
after this time-step refinement. The overshoot at 400 therefore cannot be assigned
to the original Euler step on the available evidence. Klaus has withdrawn that
attribution in his note. The manuscript had not adopted it and now states the
refinement result directly.

The higher-cutoff range is 0.121–0.141 across the two tested steps; it is not a
convergence interval or an uncertainty estimate for the ideal limit. The original
cutoff 100 and its depth 0.093 remain in the rasters. The figure caption points
to the sensitivity comparison, and the text keeps quantitative convergence open
at this finite population size. No replacement cutoff is chosen for its agreement
with the mean field.

`code/verify_r7_cutoff_leakage.py --timesteps-only --json
 docs/r7_cutoff_timestep_independent_2026-10-05.json` independently recomputes
six cache summaries and matches the reported rate and depth values within 1e-10.
The JSON records cache hashes and the changes in depth. This is a data audit,
not a fresh spiking-network run. The previously reproduced carrier-leakage and
S10 stability results are unchanged.

The requested R7 diagnostics are complete at the retained claim scope. No further
simulation is required to state the measured forced/induced-gamma distinction and
its numerical limits. Author declarations and approval, optional placement
decisions, and release coordination remain open. GitHub push, Calliope/Zenodo
release, Overleaf sync, and coauthor email remain held.

The builds contain 50 TN pages, 32 article pages, 20 supplementary pages,
50 redline pages, and eight storyline pages, with no errors, undefined
references/citations, or overfull boxes. The unchanged abstracts, 32 labeled
equations, 23 figures, and citation sequence are verified against draft5.
Output hashes are in `validation_2026-10-05_v0150draft6.json`.

The changed caption, Results redline, and storyline page were rendered and inspected.
