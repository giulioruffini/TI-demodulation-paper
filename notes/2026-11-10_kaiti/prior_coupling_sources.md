# Prior field-to-population coupling argument

Source audit for Kaiti, November 10, 2026. Read-only searches of the active NE TN and BCOM working-draft trees found the explicit antecedent through the local Rosetta Stone sources, then verified it in Ruffini's original NMM2 preprint. No manuscript or simulation was changed.

## Ruffini's NMM2 preprint states the proposed bridge explicitly

**Giulio Ruffini, _Analysis and extension of exact mean-field theory with dynamic synaptic currents_, bioRxiv 2021.09.01.458563, version 7, posted February 14, 2022.** The first posting is from 2021; the inspected PDF is v7, not the first version. [Version-specific PDF](https://www.biorxiv.org/content/10.1101/2021.09.01.458563v7.full.pdf), [DOI](https://doi.org/10.1101/2021.09.01.458563). The downloaded 50-page source is `/private/tmp/ruffini_nmm2_v7.pdf`. Page anchors below are printed pages, which match PDF page numbers.

- **Page 3, Eqs. (5)–(6):** a heuristic NMM places `lambda_n · E` in the mean-voltage argument of a static sigmoid. The text expressly notes that knowing a detailed single-neuron dipole coefficient does not establish how it should enter a neural mass. The linearized coupling impact contains the product of the cellular coefficient, interpopulation connectivity, and local sigmoid slope. This is the stated opacity K recalls.
- **Page 4, Eqs. (7)–(13):** the QIF neuron has common input `I(t) = p(t) + P · E(t)`; `P` is called a dipole conductance and may be computed from realistic compartment models in the weak, subthreshold regime. The same common input survives in the MPR voltage equation. Equal orientation and a spatially uniform input are explicit assumptions. The paper says orientation differences can be absorbed into quenched heterogeneity for a constant field; this does not establish a general time-dependent heterogeneous-input closure.
- **Page 9, Fig. 5 and Eqs. (36)–(39):** the paper already varies self-coupling `J` and the synaptic rate `a` under weak sinusoidal input. It reports the ratio of voltage standard deviation to input amplitude, resonance frequency, and bandwidth. Within the displayed regime, increasing `J` raises and sharpens the resonance; slower synapses enhance it. Longer transients accompany greater gain. These are regime-specific results, not a theorem that all responses grow monotonically with connectivity.
- **Page 10, Discussion:** the paper says the compartment-derived coefficient should enter NMM2 “without any scaling.” The immediately following argument assigns variation in the population response to `J`, excitability/heterogeneity, and the synaptic rate. This supports retaining a calibrated cellular input coefficient while allowing the network transfer to vary. It does not license omitting physical unit conversions.
- **Pages 12–13, SI A, Eqs. (SI-1)–(SI-13):** the compartmental cable equation has field-dependent axial forcing. Linearization gives a matrix equation of the form `C dV/dt + A V = b + B E`, so steady-state compartment responses and linear averages of them are linear functions of the field. The text includes averages over somatic or apical-dendritic compartments. At a nonlinear operating point it proposes local linearization about the zero-field state.
- **Pages 48–49, SI O, Eqs. (85)–(99):** the dimensional-to-natural-unit map is explicit. With voltage scale `dV = V_t - V_r`, membrane time `tau_m = c/g_L`, and current scale `g_L dV`, the reduced input is `I = I_phys/(g_L dV)` after shifting the baseline. The paper explicitly warns that field and interpopulation coupling constants change under this change of units.

### The original notation needs a distinction in the new note

The main text uses `lambda` for a **voltage-response coefficient** in Eq. (5), but uses `P` for a **current-input coefficient** in Eq. (8). Its dimensional Eq. (96), p. 49, puts `P · E` inside a current bracket multiplied by `1/c` in the voltage equation. SI A then reuses `P_k` for the **voltage response** after inversion of the compartmental operator, `P_k = -sum_j (A^-1)_{kj} p_j`, Eqs. (SI-10)–(SI-11). The notation therefore does not by itself justify treating the two coefficients as identical.

Use distinct symbols in the new note: `lambda_V = delta V/E` has units of length, whereas `kappa_I = delta I/E` has units `A m/V`. Equivalence requires a defined cell model, readout, operating point, and frequency. For a scalar linearized cell, `kappa_I(omega) = Z_cell(omega)^-1 lambda_V(omega)`. For a dimensional QIF cell linearized about a stable subthreshold voltage `v_0`, this becomes `(i omega c - 2 k v_0) lambda_V(omega)`; that is a new derivation, not a formula printed in the prior paper. The subsequent nondimensionalization divides `kappa_I` by `g_L dV`. No extra fitted population amplification is required when the calibrated common current is propagated through the same exact QIF/MPR model.

## The Rosetta Stone repeats this route

Local source: `/Users/giulio/Claude/NMM-Beats/arXiv-2512.10982v1/main.tex`, titled _Rosetta Stone of Neural Mass Models_, Castaldo, de Palma Aristides, Clusella, Garcia-Ojalvo, and Ruffini. The folder identifies arXiv v1; the TeX date is July 2025. This is not the final Physics Reports source. [arXiv v1](https://arxiv.org/abs/2512.10982v1).

- Lines **1920–1930** motivate MPR as a route from neuronal mechanisms to a dynamical population input–output relation and connect self-coupling with weak-field sensitivity.
- Lines **1954–1963** give the microscopic QIF equation, `I = p + lambda · E`, and the compartment-model calibration argument. Here `lambda` is explicitly a dipole conductance because it enters a current-like input.
- Lines **1971–1985** state equal orientation/common-input assumptions and show that `I(t)` enters the exact macroscopic voltage equation unchanged.
- Lines **2015–2016** say forcing and coupling inherit from the single-neuron biophysics through `I(t)`.

The bibliography at `references.bib:22743` identifies Ruffini v7 and reproduces its abstract; this led to the primary-source check above. The 2014 stimulation-optimization paper and Galan-Gadea et al. 2023 are cited as antecedents for the cellular field coefficient, but their full texts were not read during this bounded audit.

## The existing Neurotwin implementation separates voltage and current models

Read-only checkout `/Users/giulio/Claude/neurotwin`, HEAD `4b60395`:

- `docs/source/tutorials/neuron_perturbation.rst:4` describes precomputed coupling models under uniform fields with a specified magnitude and orientation; lines 19–28 describe compartment summaries and population models.
- `neurotwin/maxwell/neurons/coupling_models.py:937` defines `get_coupling_model`. Lines **943–958** distinguish nonfiring voltage models (`NFv`) from induced-current models (`NFc`), and distinguish single-cell, cell-type, and weighted population averages. Firing models are explicitly unavailable there. The docstring points to **TN160**, which was not located locally.
- Lines **973–977** show that the default predicts membrane-potential shifts in mV, whereas `model_type='NFc'` requests current changes.

This implementation provides a possible starting point for Raúl's cellular calibration. Its weighted population average is a morphological/type average; it does not include recurrent network gain. Whether its induced-current summary matches the input variable of a selected point neuron still requires an equivalence check.

## Status of the evidence

K's remembered argument is already explicit in the 2022 v7 preprint. The proposed Zhao study extends that argument to a different neuron and network model. Distinguishing microscopic coupling from the recurrent population susceptibility, identifying the effective NMM input channel, and testing transfer across network parameters are new work. No Zhao simulation or new calibration has been performed in this source audit.
