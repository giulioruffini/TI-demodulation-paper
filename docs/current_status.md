# Current status — TN0484 (TI envelope demodulation)

**Snapshot date:** 2026-06-04
**One line:** Integrated three-model Technical Note (JR · LaNMM · NMM2 PING), 22 pp,
compiles clean; all three models now faithful; repo and Overleaf byte-identical.

For the detailed, dated changelog see [`current_state.md`](current_state.md); this file
is the present-tense "where things stand right now" overview.

---

## The paper
- **TN0484_envelope_demodulation** — *A neural-mass mechanism for TI envelope
  demodulation: sigmoid curvature and near-Hopf amplification.* **22 pp**, compiles clean
  (0 undefined refs, 0 missing figures, 0 errors).
- Lives in **two byte-identical copies** that must stay in sync:
  - repo: `paper/TN0484_envelope_demodulation.tex` + `paper/figures/`
  - Overleaf (Dropbox): `…/Neuroelectrics Team Dropbox/Giulio Ruffini/Apps/Overleaf/TN0484 - Temporal Interference (TI) NMM demodulation/`
- Thesis: the population firing-rate nonlinearity square-law–demodulates an AM (TI) field,
  and a second-order-synapse network near a **supercritical Hopf** resonantly amplifies the
  recovered envelope. Carried by a minimal Jansen–Rit column, confirmed in the laminar
  **LaNMM** and the exact mean-field **NMM2 PING**.
- **Authors complete:** Giulio Ruffini, Raul de Palma, Borja Mercadal, Alex Just, Ricardo Salvador, Francesca Castaldo (filled in both copies).

## The three models — each shows the same (resonance curve + map) pair
| Model | Role | Bifurcation | Natural freq | Status |
|---|---|---|---|---|
| **JR** (Jansen–Rit, NMM1 single column) | reference / analysis | supercritical Hopf at input `p≈315` | alpha `f₀≈11.1 Hz` | faithful, unchanged |
| **LaNMM** (NMM1 laminar, P1 driven) | biophysical realization | alpha Hopf at drive `≈390` | alpha `~10 Hz` | faithful; figures regenerated with long windows (8 s settle / 16 s measure) + finer grids |
| **NMM2 PING** (exact next-gen mean field) | derived-nonlinearity test | supercritical Hopf at **η̄≈1** | gamma `f₀≈54 Hz`, peak `rₑ≈0.53` at η̄≈11 | **FIXED** to Raul's authoritative model; §4.6 faithful and back in |

NMM2 detail: the bifurcation parameter is the common background drive **η̄** (both
populations — there is no separate input current `I`); the model is Raul Palma's dimensional
MPR PING (`../raul code/qifnmm.f90`, AUTO), with `Δ=1`, `C=15`, `A=(1,1,1,2)`,
`τ=(15,10,7.5,2.5)`. Stable side (η̄<1) = forced gamma resonance growing toward the Hopf;
cycle side (η̄>1) = entrainment along a diagonal ridge (state-dependent transfer). A small
double-peak (~50/54 Hz) on the stable side is the PING's two coupled modes (genuine,
window- and carrier-invariant).

## Code (`code/`, run from there; figures → `../paper/figures/`)
- Self-contained generators (numpy + matplotlib only): `rerun_resonance.py` (JR),
  `lanmm_resonance.py` (LaNMM alpha), `nmm2_ping.py` (NMM2 PING).
- Engine + analysis: `jr_demod.py`, `jr_analysis.py`, `analyses_v2.py`, `figures_v2.py`,
  `make_figures.py`, `khz_analysis.py`, `test_jr_demod.py` (`ALL TESTS PASSED`).
- `lanmm_arnold_tongues.py` — needs `scipy` **and** external `lanmmv11.py`; optional.
- **Local env note:** `scipy` is **not installed** on this machine; only
  `lanmm_arnold_tongues.py` depends on it. The three main generators do not.

## Sync state
- repo ↔ Overleaf **byte-identical**: `code/` (11 scripts), `docs/`, `figures/`,
  `README.md`, `.tex`, `references.bib`. Both PDFs compile to the same byte size.
- The Overleaf `code/` mirror is now complete (was missing `lanmm_resonance.py`,
  `nmm2_ping.py` — added).

## Open items
- [x] ~~`git init` + first commit~~ — **done**: under version control on GitHub, [`giulioruffini/TN0484...NMM-demodulation`](https://github.com/giulioruffini/TN0484---Temporal-Interference-TI-NMM-demodulation), synced from the Overleaf copy.
- [x] ~~Fill the author line~~ — **done** (full author list present in both copies).
- [ ] (optional) Decide stable-side NMM2 figure presentation (keep the genuine 50/54 Hz
      double-peak, or show only the dominant 54 Hz mode).
- [ ] (optional) Install `scipy` if the LaNMM Arnold-tongue figures need regenerating.
- [ ] (science, future) realistic field-to-nonlinearity coupling `κ(f_c)`; coupled, noisy columns.

## Pointers
- `../raul code/` — authoritative NMM2 source (qifnmm.f90 AUTO, ping_nmm2.py, qif_bif2.py).
- `current_state.md` — full dated changelog (latest entry v1.3).
- `NMM2_question_for_Raul.{md,tex,pdf}` — retained for the record (now resolved).
- `README.md` (repo root) — repository layout + reproduce instructions.
