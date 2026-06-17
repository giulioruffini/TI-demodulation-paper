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
| `rerun_resonance.py` | Resonance curves with a long 20 s lock-in window (10 s settle / 20 s measure). Usage: `stable`, `cycle`, then `plot` → `fig_resonance`. |
| `analyses_v2.py` | v2 computations → `analyses_v2.npz`: operating-point law, carrier sweep, 2-D resonance map (10 s / 8 s window), bifurcation diagram. |
| `figures_v2.py` | v2 figures: concept schematic, bifurcation+sigmoid, 2-D map, carrier independence (+ synapse transfer function), operating-point law. |
| `khz_analysis.py` | Carrier-frequency sweep to 10 kHz: direct coupling (flat) vs. membrane low-pass (1/fc² rolloff) → `fig_khz`. Answers "what happens at 1k/2k/10k Hz". |
| `test_jr_demod.py` | Self-checks (derivatives, fixed point, square law, linearization control). |
| `current_state.md` | Project state / next steps. |
| `TN0484_envelope_demodulation.tex/.pdf` | The Technical Note. |

## Reproduce everything

```bash
python3 jr_analysis.py            # (optional) locate the Hopf: p~315, f0~11.1 Hz
python3 analyses_v2.py            # -> analyses_v2.npz                       (~30 s)
python3 figures_v2.py             # fig_concept, fig_bifurcation_sigmoid, fig_resonance_map,
                                  #    fig_carrier_independence, fig_operating_point
python3 make_figures.py           # fig_demodulation, fig_verification
python3 rerun_resonance.py stable # resonance sweep (10 s settle / 20 s measure)
python3 rerun_resonance.py cycle
python3 rerun_resonance.py plot   # -> fig_resonance
python3 khz_analysis.py           # fig_khz (direct coupling vs membrane low-pass to 10 kHz)
python3 test_jr_demod.py          # ALL TESTS PASSED
# jr_demod.py is the shared engine (imported by all), not run directly.
pdflatex TN0484_envelope_demodulation.tex   # x2 for refs
```

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
