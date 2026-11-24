# TN0484 draft14: notation in the article and supplement

October 6, 2026. Manuscript baseline: draft13, `c620335`; working branch:
`two-tone-validation`. The redline now uses that baseline, as Giulio requested.

Appendix A and Table 4 are in the JNE article itself, on pages 37–39. The table
has columns for symbol, meaning, units, and definition location, grouped by field
and access, detection, network, and measurement. The article, supplement, and TN
load `planning/tn0484_notation.tex`. The supplement keeps its own table copy,
with distinct labels so cross-document imports do not duplicate article labels.
Pointers to supplementary model definitions identify their appendix or section.

## Renames

| Previous notation | Draft14 | Reason |
|---|---|---|
| Envelope `A(t)` | `\mathcal A(t)` | Distinguish the envelope from the JR PSP gain `A`. |
| Signed detector `A_Ω`, dynamic `r̂_Ω`, and `A_DC` | `Y_Ω`, `Y_DC` | Reserve `A_Ω` for a nonnegative measured amplitude; distinguish the local source from the recurrent response. |
| MPR coefficient `C(Q,ω)` | `κ_DC(Q,ω̃)` | Distinguish a single-tone mean-shift coefficient from connectivity and the two-tone coefficient `χ⁽²⁾`. |
| Fixed-voltage coefficient `K(ω)` | `κ_V(Q,ω̃)` | Make the operating-point dependence explicit; distinguish synaptic operators and elliptic integrals. |
| Reduced MPR `t,r,f,ω` | `t̃,r̃,f̃,ω̃` | State `t̃=t/τ_m`, `r̃=τ_m r`, and `ω̃=ωτ_m`; symbols without tildes denote physical rates and frequencies. |
| Current amplitude `a`, tone amplitudes `a_j` | `I_ac`, `I_j` | Reserve `a` for the JR inverse synaptic time. |
| PING coupling `C` and `J=C` aliases | `J` | Keep `C` for JR connectivity. |
| QIF relative weights `A_ee,…,A_ii` | `w_EE,…,w_II` | Distinguish pathway weights from PSP and stimulation amplitudes. |
| Field-to-QIF coupling `P` | `λ_I` | Identify the field-to-current conversion; retain `P_1,P_2` for populations. |
| Filtered rates `s_syn,s_E,s_I` | `r_syn,r_E^syn,r_I^syn` | Reserve `s(t)` for membrane polarization. |
| Lock-in quadratures `I,Q` | `L_cos,L_sin` | Reserve `I` for current-like input and `Q` for mean total drive. |
| Harmonic ratios `r_det,r_meas` | `𝓡_det,𝓡_meas` | Distinguish dimensionless ratios from rates. |
| Synaptic PSP `x(t)`; lock-in test `A,φ` | `u_PSP(t)`; `A_test,θ_0` | Distinguish voltage, amplitude, and phase from other uses. |
| Population index `α`; sweep size `N` | `X`; `N_grid` | Reserve `α` for Stuart–Landau growth and `N` for neurons per population. |
| Supplement offset `x`, waveform `q(t)`, elliptic `k²` | `ξ`, `ψ(t)`, `k_ell²` | Distinguish position, single-cell drive, and compartment/sample indices. |
| Stuart–Landau forcing `ε f(t)` | `ε_SL ψ_SL(t)` | Distinguish the normal-form forcing from polarization in mV. |

`G` denotes complex susceptibility; its gain formulas now display `|G|`, and the
observed amplitude is `A_Ω=|R_Ω|`. This states the existing amplitude convention
without changing the gain law. `I_h` and `I_M` are named as membrane currents.

## Units and independent check

The QIF spike cutoff is dimensionless, not mV. PING rates are integrated in
ms⁻¹ and converted to Hz where indicated; JR rates use s⁻¹. The normalized MPR
mean shift becomes a physical rate shift after division by `τ_m`. The table
states the physical units of `χ⁽²⁾`, the compartment matrices, and each readout.
Detector outputs and excursions carry output and argument units, respectively.

Klaus's independent appendix audit is preserved in
`notation_audit_appendix_2026-10-06.md` (his commit `bee566d`). Its unit and
figure-label findings are addressed. We retain the conventional, distinct full
symbols `η_det`, `S(f_c)`, and the sans-serif Jacobian `\mathsf J`, with definitions in
the table. His suggested `χ_I` is not adopted: the single-tone DC and two-tone
beat coefficients have different normalizations. The compartment index in
Eq. (8) was already `k`, distinct from the carrier subscript `c`.

## Validation

All 32 labeled equations and 23 figures retain their numbers. The 60 cited keys
and the 297-word abstract are unchanged. Simulation producers and caches are
unchanged. Figure 7 and Figure S10 are replotted only for notation; their data
and normalizations are retained. Their remaining overlap-check flags concern
tick labels outside the visible axes and were checked against the renders.

Builds: JNE 39 pages, supplement 20, full TN validation 54, storyline 10.
Build logs, artifact hashes, and the final redline page count are recorded in
`validation_current.json`; numbering checks are in
`notation_audit_2026-10-06_draft14.json`. The article and supplement are the
current files; the TN validation stays private under `/tmp/tn0484_draft14/`.
The prose checker reports no findings in the manuscript or notation source. Its
one flag in this record treats the Markdown table separator as three em dashes;
the separator is retained. The regenerated supplementary bibliography reflects
the existing published CFC entry; no reference source was changed.

The annotations harvested at 18:16 have been read and remain on the TODO list.
Their requests for a fuller envelope/DC explanation and measurement rationale
belong to the separate transduction revision. Release and circulation holds remain.
