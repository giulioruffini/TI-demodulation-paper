# TI envelope demodulation in a neural mass — code

Simulation code for **TN0484**, *Cortical demodulation of temporal-interference
fields: envelope detection by a sigmoid and resonance near a Hopf bifurcation.*

A high-frequency amplitude-modulated (AM) "field" is injected into the
pyramidal output sigmoid of a Jansen–Rit (JR) neural mass. The sigmoid
demodulates it (square-law), and proximity to a supercritical Hopf bifurcation
resonantly amplifies the recovered envelope. The AM input has **no** spectral
power at the envelope frequency, so any envelope-frequency output is produced by
the nonlinearity.

## Requirements
Python 3.10+, `numpy`, `scipy`, `matplotlib`. (For the TN PDF: a LaTeX install
with `pdflatex`.)

```bash
pip install numpy scipy matplotlib
```

## Files

| File | Role |
|------|------|
| `jr_demod.py` | Core engine: JR model, sigmoid + derivatives, vectorized RK4 integrator with AM field injection, lock-in detection, open-loop detector, fixed-point/bifurcation helpers. Running it as a script produces the resonance sweep `sweep_results.npz`. |
| `jr_analysis.py` | Standalone Hopf locator: fixed point vs `p`, Jacobian eigenvalues, prints the Hopf input and natural frequency. |
| `make_figures.py` | Demodulation-sanity and verification figures (square-law + linearization control). |
| `rerun_resonance.py` | Resonance curves with a long 20 s lock-in window (10 s settle / 20 s measure). Usage: `stable`, then `plot` → `fig_resonance`; `cycle` is retained for the older analysis. |
| `analyses_v2.py` | v2 computations → `analyses_v2.npz`: operating-point law, carrier sweep, 2-D resonance map (10 s / 8 s window), bifurcation diagram. |
| `figures_v2.py` | v2 figures: concept schematic, bifurcation+sigmoid, 2-D map, carrier independence (+ synapse transfer function), operating-point law. |
| `khz_analysis.py` | Carrier-frequency sweep to 10 kHz: direct coupling (flat) vs. membrane low-pass (1/fc² rolloff) → `fig_khz`. Answers "what happens at 1k/2k/10k Hz". |
| `khz_twotone_producer.py` | Reconstructed 2 kHz two-tone run; `--compare` checks archived spectra, `--write` saves a separate fresh cache. |
| `test_jr_demod.py` | Self-checks (derivatives, fixed point, square law, linearization control). |
| `qif_short_tau_check.py` | Shorter-tau QIF/MPR comparison with fixed parameters or matched baseline rate/voltage; exact second-order beat response checked against direct integration. Run from the repository root with `.venv/bin/python code/qif_short_tau_check.py`; writes `docs/qif_short_tau_2026-10-02.json`. |
| `qif_cached_component_check.py` | Independent spectral check of the preserved two-tone QIF runs; separates beat lock-in, refined gamma peak, and the original FFT-bin estimate. Use `--json <path>` to save the result. |
| `ping_field_operating_point.py` | E-only carrier-rectified drive shift, averaged stability, and direct mean-field spectra at amplitudes 5–35; writes the dated R7 JSON and diagnostic figure in `docs/`. |
| `ping_field_operating_point_check.py` | Independent finite-difference/time-average check of the R7 source and threshold, plus original-integrator reproduction at amplitudes 10 and 35. Use `--json <path>`; no spiking cache is modified. |
| `ping_other_sweeps_screen.py` | DC-only stability screen for the S10 AM surrogate and selected two-tone resonance states; use `--json <path>`. Does not test stability of the full beat-forced solution. |
| `current_state.md` | Project state / next steps. |
| `TN0484_envelope_demodulation.tex/.pdf` | The Technical Note. |

## Reproduction entry points

Run `code/run_all.py` from the repository root; it sets each subprocess's working
directory to `code/`. `--only` includes the required data producers before plotting,
and `--dry-run` prints that plan without executing it:

```bash
.venv/bin/python code/run_all.py --only fig_resonance,fig_concept --dry-run
.venv/bin/python code/run_all.py --only fig_resonance --figdir /tmp/tn0484-figures
.venv/bin/python code/run_all.py --from-cache --only fig_jcurve,fig_khz_twotone --figdir /tmp/tn0484-figures
.venv/bin/python code/test_run_all.py
```

Figure output honors `TN_FIGDIR` or `--figdir`. Simulation data still goes into
`code/`, so use a separate checkout for recomputation if existing caches must be
preserved. `--from-cache` runs only renderers, checks their required inputs, and
rejects figures whose script also performs an inline simulation.

The current resonance figure uses the stable sweep and plot modes; the cycle mode
is retained for the older analysis but is not a prerequisite. The reconstructed
`khz_twotone_producer.py` reproduces all seven arrays of the archived two-tone kHz
cache exactly. Recomputing `fig_khz_twotone` writes a separate
`khz_twotone_reproduced.npz` and plots it; `--from-cache` uses the preserved
`khz_twotone.npz`. Settings are recorded in
[the recovery note](r12_khz_twotone_2026-10-04.md). See the [figure table and provenance limits](../README.md#reproduce-the-figures).

The draft2 check passes all 11 runner tests. Independent fresh and cached kHz runs
produce identical figure images, and the fresh data match all seven archived
arrays bit for bit. The original cache is unchanged. The comparison and runner
logs are linked from the [integration record](revision_2026-10-04_v0150draft2.md).

The October 4 reproduction check used a scratch tree containing tracked inputs.
It regenerated the missing analyses and stable-resonance caches, then rendered the
concept figure group and resonance figure through `--only`. Cached LaNMM and kHz
replots and all nine runner regression checks also passed. This was a selective
check, not a rerun of the full simulation suite. The existing concept and
bifurcation renderers still emit small-type/collision warnings; these checks do
not establish that every regenerated figure matches the manually reviewed layout.

## Model & key parameters
Standard JR (Jansen & Rit 1995): `A=3.25, B=22 mV; a=100, b=50 1/s;
v0=6 mV, e0=2.5 1/s, r=0.56 1/mV; C=135`. External input `p` (Hz) is the
bifurcation knob. Supercritical Hopf at `p≈315`, natural frequency `f0≈11.1 Hz`;
`p>315` = stable focus (forced resonance), `p<315` = alpha limit cycle
(entrainment). Default stimulus: carrier `fc=100 Hz`, modulation depth `m=1`,
field amplitude `eps` (0.3 mV for sweeps, in the linear/square-law regime).
Integrator: RK4, `dt=2e-4 s` (1e-4 for carrier sweeps), settle 6–12 s,
measure 2.5–3 s, Hann-windowed lock-in at the envelope frequency.

## Key API (`jr_demod.py`)
- `Sigm(v), Sigm1(v), Sigm2(v)` — sigmoid and its first/second derivatives
  (`Sigm2` sets the demodulation gain; zero at the inflection `v0`).
- `rhs(Y, p, sfield, lin=None)` — vectorized RHS; `Y` is `(N,6)`. `lin=(v_op,S1)`
  linearizes the field-receiving sigmoid (control: demodulation off).
- `integrate(p, Omega, eps, m, fc, t_settle, t_meas, dt, record=False, lin=None)`
  — returns the lock-in amplitude at `Omega` of `v=y1-y2`. `p, Omega` (and
  optionally `fc`) are arrays of shape `(N,)`; sweeps run in parallel.
- `steady_v(p)` — field-free operating point and sigmoid slope.
- `openloop_lockin(v_star, eps, m, Omega, fc, …)` — sigmoid-only detector.
- `fixed_point_state(p)`, `freefield_minmax(p, …)` — bifurcation diagram support.

## Verified
`test_jr_demod.py`: `Sigm1/Sigm2` match finite differences and `σ''(v0)=0`;
fixed point is an equilibrium (`max|rhs|~7e-12`); square-law slope `1.99`;
linearization collapses the response `737×`.

## Next
Port to the LaNMM (alpha + gamma; demodulate to either band; HB⁺₁ at
`μ_P1≈364`). Add response-vs-amplitude/modulation-depth curves, noise and
heterogeneity, and a more biophysical membrane pre-filter. `git init` + commit.
