# Internal population gain and the JR field input

Giulio clarified on November 10 that the intended JR transfer represents an internally recurrent population after it settles. The explicit JR synapses connect those effective populations. This interpretation changes which recurrence must remain active when Raul estimates the transfer.

## Source check

The latest download was `~/Downloads/dc_gain_note_source.zip`, modified November 10 at 19:17. Its four-page `dc_gain_note.pdf` and the accompanying TeX, `nmm2.py`, `verify.py`, and figure generator were inspected without changing the originals. Klaus's equilibrium gain, reported eigenvalues, fold locations, coupling sensitivities, and finite-field equilibrium responses were independently checked. No new time-domain simulation campaign was run.

The local Rosetta Stone source is `/Users/giulio/Claude/NMM-Beats/arXiv-2512.10982v1/main.tex`. The transfer section defines a population relation at lines 1291–1303; lines 1928–1930 and 2000 describe the dependence on internal self-connectivity and its replacement of the static sigmoid and self-coupling. The displayed master equations at lines 1392–1418 and 1988–1995 nevertheless retain a particular self-loop explicitly. The source therefore supports Giulio's intended population interpretation but needs an explicit partition of internal and interpopulation recurrence. The inspected copy is arXiv v1, not an independently checked final publication.

## The internal gain belongs in the effective transfer

Let F(Q) be the physical firing-rate response to total current Q with recurrent input held fixed. Let I be the current supplied from outside the effective population, including its background drive, and let J_int have units of current divided by rate. When the internal synaptic filter has unit DC gain, the settled population response R_J obeys

    R_J(I) = F(I + J_int R_J(I)).

At a stable equilibrium, with derivatives of F evaluated at the total current,

    R_J' = F' / (1 - J_int F'),
    R_J'' = F'' / (1 - J_int F')^3.

These are exact equilibrium derivatives of the specified QIF/MPR model for any synaptic time constant. Approximating the whole response by this static curve additionally requires input changes to be slow relative to internal relaxation. A large DC gain makes that condition more restrictive. Klaus's illustrative gain-20 population relaxes in about 0.53 s, so its steep DC curve cannot also be assumed instantaneous at alpha or carrier frequencies.

The negative DC feedback calculated in the pinned TN0484 JR column is the net loop between its modeled populations. It does not identify or bound the positive internal feedback that a fitted sigmoid may already contain. Comparing this outer JR loop directly with the internal scalar NMM2 loop conflates two model boundaries.

## The field enters in the transfer's input coordinate

If a physical field is represented by the equivalent current kappa_I E at the input of the effective population, then

    r = R_J(I + kappa_I E).

For a justified local input-voltage coordinate x = R_eff I, define

    Sigma_J(x) = R_J(x / R_eff),
    lambda_JR = R_eff kappa_I.

Thus

    Sigma_J' lambda_JR = R_J' kappa_I.

The internally recurrent gain is in Sigma_J'. Multiplying lambda_JR by the same gain would count it again. Interpopulation synaptic filters and feedback remain explicit. R_eff must be calibrated to the sigmoid's input coordinate; it is not automatically isolated-cell resistance, measured network voltage susceptibility, or the MPR principal-value mean voltage.

If a fixed conventional sigmoid Sigma_nom is retained instead of fitting Sigma_J, a rate-matched coefficient at one operating point would be lambda_fit = kappa_I R_J'/Sigma_nom'. Such a coefficient can absorb missing internal gain, but it is then an effective fitted parameter, not the isolated-cell polarization coefficient. Matching a slope does not match the curvature, relaxation, or other states. Under this static scalar mapping, quadratic TI source matching also requires Sigma_nom'' lambda_fit^2 = R_J'' kappa_I^2. The static relation is not a fast-carrier detector derivation; dynamic second-order response is needed outside its bandwidth.

## Raul's calibration retains the internal population loop

First calibrate field forcing and the candidate equivalent-current channel at the cellular level under a specified synaptic background. Then retain recurrence within the population represented by one sigmoid, while clamping or replaying inputs from the other populations. Sweep slow external drive and weak positive and negative fields. Measure rate as well as voltage, and estimate the effective curve, its slope and curvature, and its relaxation time. Sweep internal connectivity and background state to determine how that effective transfer changes. Finally reconnect the effective populations and test their coupled response without fitting a second copy of the same internal gain. Background conductance changes may alter cellular impedance and must be distinguished from recurrent amplification.

## Qualifications to Klaus's note

- The bound G0 <= 1/(1-J/Jc) requires 0 <= J < Jc. For J < 0 the inequality reverses, although the equilibrium remains unique.
- L0 = 1 gives a generic fold when F'' is nonzero; at the maximal slope it is the cusp. Large gain can approach the cusp from below without a fold in the fixed-J input sweep.
- Persistent switching after field offset requires bistability at the field-free input, not merely J > Jc.
- A zero multi-population determinant allows a divergent susceptibility only when the field and readout couple to the critical mode.
- The stated E_10% is a quadratic estimate. In the gain-20 example, the exact deviation at +0.10 V/m is 12.34%; the positive fold is +0.28018 V/m. A slope of 10% per V/m is not a prediction of a 10% response at 1 V/m on that branch.
- At J = 0 the full Jacobian includes a 10-ms synaptic mode that cannot feed back into rate. The observable rate relaxation is 7.07 ms, as in the table; the verification script's slowest-eigenvalue report should distinguish these.

The live article and companion LaTeX note were not edited during this discussion. Their next revision should state Giulio's intended population boundary and distinguish the exact DC derivative from the slow-dynamics approximation.
