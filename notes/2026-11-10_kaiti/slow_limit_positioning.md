# Position of the slow-input field-coupling argument

Read-only source assessment, November 10, 2026. This separates the prior derivation from a possible extension for Raúl; it does not assess a completed new experiment.

## The reduction and recurrent gain are already in the prior work

In Ruffini's _Analysis and extension of exact mean-field theory with dynamic synaptic currents_, [bioRxiv v7, February 14, 2022](https://www.biorxiv.org/content/10.1101/2021.09.01.458563v7.full.pdf), Appendix K is explicitly titled “Slow synapse/slow input limit and mapping of NMM2 to NMM parameters.” Pages 41–42, Eqs. (67)–(80), derive the stationary QIF transfer

\[
F(Q;\Delta)=\frac{1}{\pi\sqrt{2}}
\sqrt{Q+\sqrt{Q^2+\Delta^2}},\qquad Q=\eta+Js+I.
\]

Both synaptic input and external input must vary slowly relative to relaxation of the voltage–rate subsystem. The result is a static current-to-rate transfer coupled to synaptic dynamics. It is neither a universal voltage sigmoid nor a derivation valid for fast external input. Appendix L (p. 45) treats fast input separately, retaining the voltage–rate dynamics with frozen synapses.

Appendix K already defines the local differential gain `K*=F'(Q*)` and linearizes recurrence. Its Eq. (82), in synaptic-time units, is

\[
\delta s'=\delta z,\qquad
\delta z'=(JK_*-1)\delta s-2\delta z+K_*\delta I.
\]

Thus the steady response `delta s/delta I=K*/(1−JK*)` follows directly. The existing equation also supplies the slow-input frequency response. Writing those expressions out makes the earlier result easier to use, but does not establish a new amplification mechanism. Under a pinned local operating point `K*` is fixed; at fixed background input changing `J` also moves the operating point, so the two parameter sweeps answer different questions. Figure SI-25 (p. 44) already compares the static transfer to fitted sigmoids and plots fixed points, local slope, and recurrence-dependent response.

**Do not copy the printed second-order line immediately after Eq. (82):** it has `−2 delta s'`, inconsistent with Eq. (82) and the stated eigenvalues. The damping term is `+2 delta s'`. The subsequent p. 43 resonance expression should also be rederived before use. Negative self-coupling makes the two slow-limit poles complex, but an amplitude peak at a nonzero forcing frequency additionally requires `|J|K*>1` in this normalization. For positive self-coupling on a stable branch the slow-limit poles are real; the resonance of the full excitatory NMM2 model must not be attributed to this scalar static limit.

## The journal paper already places the static limit in its main text

[Clusella, Köksal-Ersöz, Garcia-Ojalvo, and Ruffini, _Comparison between an exact and a heuristic neural mass model with second-order synapses_, Biological Cybernetics 117, 5–19 (2023)](https://doi.org/10.1007/s00422-022-00952-7), published online December 1, 2022, makes the reduction a main result. Section 3.1 derives the same transfer as Eq. (17) and maps it to NMM1 through Eq. (18): `Phi=Psi_Delta/tau_m`, `K=J tau_m`, `p=eta`. That derivation sets external input to zero. Section 2.2 already introduces the field-derived current, its single-neuron origin, and its unit conversion. Sections 4.1–4.2 show where the static reduction loses the full model's dynamical behavior. Therefore, adding a slowly varying field to the established reduction is an application, not a newly discovered reduction.

## A separate working paper needs a calibrated or testable extension

A short section in the note for Raúl is warranted now. It should connect the existing equations to the present calibration problem: distinguish the field-to-voltage coefficient from the equivalent field-to-current coefficient; show where that current enters the QIF and MPR equations; then derive the recurrent susceptibility at a declared operating point. This gives him a concrete benchmark without assigning novelty to the old slow-limit result.

A dedicated working paper would be justified by results beyond that exposition. The proposed study can supply them by identifying a cellular field-equivalent input from a compartment model, preserving its units and frequency dependence, and testing whether it predicts population responses without refitting the input coefficient as recurrence changes. The useful comparison is among isolated cells, a network with prescribed or replayed synaptic input, and a recurrent network. Fit the cellular coefficient once; vary connectivity, E/I balance, synaptic kinetics, and operating state; compare predictions in both voltage and rate. A failed scalar reduction is informative if the residual identifies the missing input channels or state variables.

For a quantitative paper, the slow-limit boundary should be measured rather than stated only as `tau_m << tau_s`: compare the field and synaptic input frequencies to the local voltage–rate relaxation rates, and report prediction error as this separation is reduced. Near loss of stability, a large formal gain also narrows the linear regime and lengthens settling. The nonzero-frequency response of the full MPR model, the DC susceptibility, and a fitted NMM input coefficient should remain distinct observables.

The first deliverable can therefore be the explanatory section and a reproducible benchmark protocol. The separate paper would follow the first field-calibrated validation or a demonstrated, interpretable failure of the reduction in Zhao's model. Merely moving Appendix K into a new document would be useful teaching material, but not an independent research result.
