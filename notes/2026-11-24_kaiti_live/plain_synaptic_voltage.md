# Plain synaptic-voltage notation — November 24, 2026

Giulio requested plain `u` instead of `u_PSP` in the synaptic filter. Klaus applied this to the main source and shared notation row. The supplementary efficiency calculation independently used `u=rho epsilon`, which would leave the shared table assigning the same symbol both voltage and dimensionless units.

The reduced amplitude is now `U=rho epsilon`: six occurrences in `supp_efficiency.tex` and one supplementary notation-table entry. Uppercase `U` was unused in the canonical source. The PSP remains `u`; the pathway-qualified `u_{X←Y}` and other subscripts that distinguish quantities are retained. No figure or numerical-code label needs changing. This is a renaming; the bound, numerical values, units, and all equation labels are unchanged.

The journal article and supplement build at 39 and 36 pages with no undefined or multiply defined references and no overfull boxes. Counts are unchanged: 11,977 article words and a 298-word abstract. The three affected source files remained unchanged during the build. Giulio's concurrent paragraph breaks and removal of redundant time arguments are preserved in the checked snapshot. No full-TN build, push, or synchronization was performed.

Exact source snapshots, before/after hashes, build output, and counts are under `build/2026-11-24_live_prose_merge/plain_synaptic_voltage/`.

## Redundant time arguments

The delayed peer handoff also covered six supplementary/model modules not yet committed: `article_models`, `figure_qif_timing`, `slow_synapse`, `supp_detection`, `supp_laminar`, and `theta_pilot`. Their diffs contain only removal of redundant `(t)` and accompanying delimiter spacing; normalization of those decorations makes the old and new sources identical. These saved files predate the already-checked journal PDFs, so that build includes them. The main-source and efficiency-module time-argument edits were already included in `53b8534`. Explicit time dependence in waveform and kernel definitions remains. Later author edits to the beat-source units sentence remain untouched in the working file.

## Total drive in the theta-neuron equation

Klaus identified the remaining population-indexed `U_X`. The theta script adds the recurrent synaptic drive and the applied field to each neuron's excitability. In the PING equations, however, `I_E=lambda_I E` denotes the applied-field contribution alone. Renaming the total drive to `I_X` would blur that distinction. The theta equation therefore uses `mathcal U_X`, consistent with the schematic's `mathcal U_j`. Its local definition names the population and total synaptic-plus-field drive in normalized units and points to the PING equations. Plain `U=rho epsilon` remains the reduced amplitude.

This decision was checked against `theta_pilot.py`'s E/I update equations and the manuscript's `eq:nmm2-ping`. Only the mathematical notation and local definition changed; no simulation or parameter changed. The 36-page supplement rebuild passes with no undefined or multiply defined references and no overfull boxes. Evidence is in `build/2026-11-24_live_prose_merge/theta_drive_notation/`.
