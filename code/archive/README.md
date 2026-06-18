# Archived scripts

Superseded or dead code, kept for provenance but **not part of the live figure
pipeline** (`code/run_all.py`). Nothing here is imported by an active script or
produces a current manuscript figure.

| script | why archived | live replacement |
|---|---|---|
| `jr_analysis.py` | Dead: prints a Hopf/fixed-point table, writes no figure, imported by nothing. | Hopf logic lives in `jr_demod.py` (the shared JR engine). |
| `nmm2_jc.py` | Superseded NMM2 J-curve data producer (wrote `nmm2_jcurve.npz`). | `nmm2_jcA.py` (engine) + `nmm2_jcD.py` (→ `nmm2_jcD.npz`), plotted by `make_nmm2_jfig.py` for `fig_nmm2_jcurve`. |

(`make_timing_fig.py` was briefly archived here by mistake and restored to `code/`: it is
the *only* plotter for `fig_timing_not_rate` — `timing_not_rate.py` writes the `.npz` data
but does not plot.)

These were moved (not deleted) on 2026-06-18 during the repository cleanup; git
history is intact. The orphaned `nmm2_jcurve.npz` data file remains under `code/`
(harmless; the live `fig_nmm2_jcurve` uses `nmm2_jcD.npz`).
