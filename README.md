# TN0484 — A neural-mass mechanism for temporal-interference envelope demodulation

Sigmoid curvature + near-Hopf amplification as a **mesoscopic, network** mechanism
for temporal-interference (TI) stimulation. An amplitude-modulated (AM) field
carries no spectral power at its envelope frequency, so demodulation requires a
nonlinearity. We show that the population firing-rate **sigmoid** of a neural mass
is a square-law demodulator, and that a second-order-synapse network **near a Hopf
bifurcation** resonantly amplifies the recovered envelope.

> **Key message:** *wherever a fast-enough nonlinearity samples the carrier, the
> population sigmoid demodulates and the network amplifies* — the single-cell entry
> point (fast channels at nodes/AIS/terminals) supplies the carrier sampling, while
> the demodulation read-out and resonant gain are network properties.

![concept](paper/figures/fig_concept.png)
![resonance](paper/figures/fig_resonance.png)

## Repository layout

```
.
├── README.md                     # this file
├── paper/
│   ├── TN0484_envelope_demodulation.tex   # the Technical Note (\graphicspath{{figures/}})
│   ├── TN0484_envelope_demodulation.pdf
│   ├── references.bib            # BibTeX source for all references
│   └── figures/                  # fig_*.pdf (paper) + fig_*.png (preview)
├── code/                         # all simulation/analysis code (run from here)
│   ├── jr_demod.py               # core engine: JR model, sigmoid+derivatives,
│   │                             #   vectorized RK4, AM field injection, lock-in,
│   │                             #   open-loop detector, bifurcation helpers
│   ├── jr_analysis.py            # Hopf locator (fixed point + Jacobian eigenvalues)
│   ├── make_figures.py           # demodulation + verification figures
│   ├── rerun_resonance.py        # resonance curves (long 20 s lock-in window)
│   ├── analyses_v2.py            # operating-point, carrier, 2-D map (10/8 s), bifurcation
│   ├── figures_v2.py             # concept, bifurcation+sigmoid, map, carrier, op-point
│   ├── khz_analysis.py           # carrier sweep to 10 kHz (membrane low-pass)
│   ├── lanmm_arnold_tongues.py   # LaNMM Arnold tongues (needs lanmmv11.py — see note)
│   ├── lanmm_resonance.py        # LaNMM alpha resonance curve + map (self-contained, vectorized)
│   ├── nmm2_ping.py              # exact mean-field NMM2 PING (gamma): resonance curve + map (self-contained)
│   └── test_jr_demod.py          # self-checks (derivatives, fixed point, square law, control)
├── docs/
│   ├── README_Code.md            # detailed code documentation
│   └── current_state.md          # project state / changelog / next steps
└── archive/                      # superseded v1 of the note
```

## Reproduce

Requirements: Python 3.10+, `numpy`, `scipy`, `matplotlib`; a LaTeX install with
`pdflatex` for the paper.

```bash
cd code
python3 jr_analysis.py             # (optional) locate the Hopf: p~315 Hz, f0~11.1 Hz
python3 analyses_v2.py             # -> analyses_v2.npz  (carrier, 2-D map, bifurcation)
python3 figures_v2.py              # concept, bifurcation+sigmoid, 2-D map, carrier, op-point
python3 make_figures.py            # demodulation + verification figures
python3 rerun_resonance.py stable  # resonance sweep, stable side   (10 s settle / 20 s measure)
python3 rerun_resonance.py cycle   # resonance sweep, limit-cycle side
python3 rerun_resonance.py plot    # -> fig_resonance
python3 khz_analysis.py            # carrier sweep to 10 kHz
python3 test_jr_demod.py           # ALL TESTS PASSED

# jr_demod.py is the shared engine (imported by all of the above), not run directly.

cd ../paper
pdflatex TN0484_envelope_demodulation.tex
bibtex   TN0484_envelope_demodulation        # references from references.bib
pdflatex TN0484_envelope_demodulation.tex
pdflatex TN0484_envelope_demodulation.tex
```

References live in `paper/references.bib` (BibTeX, `unsrt` style) and are portable
to any other document or reference manager.

Figure scripts write both `.pdf` and `.png` into `paper/figures/`. Intermediate
`.npz` files are written in `code/` and are git-ignored (regenerated on demand).

The LaNMM Arnold-tongue figures (`fig_lanmm_*`) come from `code/lanmm_arnold_tongues.py`,
which needs the LaNMM model module `lanmmv11.py` from
[LaNMM_predictive_coding_paper](https://github.com/giulioruffini/LaNMM_predictive_coding_paper)
(`python/lanmmv11.py`, not bundled here) on the `PYTHONPATH`. Alpha-band power is
computed inline, so no other LaNMM module is required. The figures themselves are
already in `paper/figures/`.

## Verified

`test_jr_demod.py`: sigmoid derivatives match finite differences (and σ''(v₀)=0);
the field-free fixed point is an equilibrium; square-law slope ≈ 1.99 (theory 2);
linearizing the field-receiving sigmoid collapses the response ~712×.

## Status

Preprint draft (v0.6, 18 pp). Single integrated paper: the minimal Jansen–Rit
column carries the analysis, and the two-band **LaNMM** is woven in as a second
model — introduced in Theory §2.1, its drive/protocol/setup in Methods §4, and the
Arnold-tongue results in Results §5.1 (no standalone section). Compiles clean
(no undefined refs). **Author line in the `.tex` is still a placeholder
("Giulio Ruffini and ....") — fill before circulation.** Natural next step: a
realistic field-to-nonlinearity coupling κ(f_c) and coupled, noisy columns.
