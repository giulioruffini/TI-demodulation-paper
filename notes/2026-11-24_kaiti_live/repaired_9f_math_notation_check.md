# Repaired revision: mathematics and notation check — 2026-11-24

Compared the requested diffs and baseline/snapshot files in `build/2026-11-24_live_prose_merge/repaired_9f_fidelity/` against baseline 864121f. No mathematical regression was found. One retained sign convention should be made explicit in the harmonic derivation.

## Synaptic normalization and rate units agree

`slow_synapse.tex` now distinguishes an exact unit-gain synaptic filter from the adiabatic approximation for the population rate. For the JR excitatory filter, multiplying `P'' + 2a P' + a²P = Aa r` by `tau_s²`, with `a = 1/tau_s`, gives a steady voltage gain `A tau_s`. Defining the normalized potential `u = P/(A tau_s)` yields exactly `tau_s² u'' + 2 tau_s u' + u = r`. Thus `u` and `r` share inverse-time units; `r` remains firing rate, and `P = A tau_s u` is the physical voltage.

The revised wording correctly confines the gain `A tau_s` to the JR excitatory example. It does not assign that same physical voltage conversion to every PING pathway. PING retains unit-gain filters `u_E = K_a[r_E]` and `u_I = K_g[r_I]`, with times `tau_a` and `tau_g`; pathway gains remain in `J` and the weights. The products `tau_E J u_X` and `tau_I J u_X` are dimensionless, as required by the voltage equations. Removing `G_u` changes no equation. The two notation-table rows now distinguish NMM1 voltages from gain-normalized NMM2 potentials.

## Derivations and captions preserve their quantities

- `article_models.diff` changes fixed-point superscripts to subscripts consistently. The crossover coefficient, Jacobian, eigenvalues, and membrane-time scaling are algebraically unchanged. The local convention still converts normalized rates to physical rates by division by `tau_m`.
- `harmonic_details.diff` preserves the Fourier series and ratios `1/5`, `3/35`, and `1/21`. Its mixed-detector ratio retains the correct factor `3 pi c_2 epsilon/(4c_1)`. At snapshot `harmonic_details.tex:8`, explicitly take `epsilon_1 = epsilon_2 = epsilon > 0`: without positivity, the displayed nonnegative envelope needs `|epsilon|`, and so does the mixed-detector ratio. This scope omission existed in the baseline; adding `> 0` is the smallest repair.
- `tn0484_notation.diff` preserves rate, voltage, coefficient, and operator units. The normalized MPR derivation remains separately identified.
- `fig_models_ti_caption.diff` correctly identifies `v_E²` as the squared mean voltage and `1/gamma` as inverse modal damping. The field coupling and second-order synaptic filters retain their meanings.
- `theta_pilot.diff` changes table-header layout only; all numerical entries and the normalized total-drive equation are unchanged.
- `fem_interfaces.diff` restates the same angle between the fixed projection direction and interface normal. No bound, ratio, or numerical value changes.

## The crossover ordinate is response error

The revised label, “excitatory-rate response error (%)”, matches the actual computation. In `code/ping_fast_carrier_check.py:119–126`, the exact and approximate quadratic source vectors are both propagated through the full network resolvent at the beat frequency. Component zero is selected for the excitatory rate, and the stored error is `|y_fast − y_exact|/|y_exact|`. It is therefore a complex rate-response error, not a source-vector error or merely a magnitude-amplitude error. `code/mpr_crossover_fig.py:61–65` multiplies that quantity by 100 and plots it; the canonical script matches the snapshot.

Independently recomputing all 12 stored errors from the JSON's complex `exact_y` and `fast_y` values gives zero discrepancy. Maximum errors are 1.0698065% at 300 Hz, 0.0942882% at 1 kHz, and 0.0235357% at 2 kHz, consistent with the revised caption and text. No generator or simulation was run.

Only this review note was written. No source edits, builds, commits, or peer messages were made.
