# NMM2 PING — question for Raul (re: TN0484)

**Context.** For TN0484 (TI envelope demodulation) we want the **NMM2 PING** as a third
model — after the heuristic Jansen–Rit single column and the LaNMM — showing the same
mechanism: a weak **AM electric field** `I(t)=p+λE(t)` driven into the excitatory
current is demodulated by the exact quadratic `v²` term and resonantly amplified near a
Hopf, read out as lock-in at the envelope frequency over a `(Δf, I)` plane.

For the resonance claims to be quantitatively honest we need the PING model to be
**faithful** — correct Hopf locations and gamma frequency. We reconstructed it from the
Rosetta Stone text (Eq. 7.9 / Eq. nmm2-EI-pushpull + Table A.1) but **our reconstruction
does not reproduce your published bifurcation diagram (Fig. 7.3)**, so we'd rather use
your actual equations/code than keep guessing the dimensional conventions.

## What Fig. 7.3 (PING) shows (our target)
SN ≈ −1; lower **HB⁺ ≈ 1**; a large gamma limit cycle peaking at **r ≈ 0.53 near I ≈ 11**;
upper **HB⁺ ≈ 68**; stable focus outside. Parameters (Table A.1, NMM2-PING):
`η_e=η_i=0, J_ee=J_ei=J_ie=1, J_ii=2, τ_e=15, τ_a=10, τ_i=7.5, τ_g=2.5, Δ_e=Δ_i=1`,
`I ∈ [−20, 75]`.

## What we have already corrected (still doesn't reproduce Fig. 7.3)
Re-reading Eq. 7.9 we fixed two genuine errors in our reconstruction:
- the `(r,v)` membrane equations are **bare** — `ṙ_x=Δ_x/π+2r_xv_x`,
  `v̇_x=v_x²+η̄_x+J_x s_x−π²r_x²−C_xy s_y+I` (we had wrongly divided them by a membrane
  time τ_e/τ_i; Eq. 7.9 has **no τ on the LHS**);
- the cross-couplings are the **off-diagonal J's**: `C_xy=J_ei` (I→E), `C_yx=J_ie` (E→I),
  with `J_x=J_ee`, `J_y=J_ii` (so all time constants live only inside the synaptic
  kernels `K_x`, `K_y`).

After these corrections it is structurally closer but **still wrong**: a long-settle
time-integration gives **no clean limit cycle** in `I∈[−20,75]`, the fixed-point firing
rate climbs to **r≈1–2** (your branch stays ≈0.1–0.15), and the integrator **diverges**
at higher `I`. We think the remaining gaps are the synaptic kernel and the integration
method (below).

## Specific questions
1. **Synaptic kernel `K_x`, `K_y`.** The review defines `K` via
   `γ⁻¹(τ² s̈ + 2τ ṡ + s) = r` (equal rise/decay) or `(τ_r, τ_d)` for distinct
   rise/decay. For NMM2-PING:
   - what is the **synaptic gain γ** for each population? (The bif-params row lists the
     J's, τ's and Δ but **no γ** — is γ=1, or a JR-style value, or folded into J?)
   - do the **two constants per population** map as `K_x` = (τ_e, τ_a) and
     `K_y` = (τ_i, τ_g), and which is rise vs decay? Is it the product/bi-exponential
     `(τ_d d/dt+1)(τ_r d/dt+1)s=γr`, or critically-damped with one τ (then what are the
     other two constants)?
   - is the DC gain of `K` unity (so `s→r` at steady state), or `γ`?
2. **Units / scale.** Units of `r` (Fig. 7.3 axis 0–0.5: kHz? normalized?) and the time
   unit, so the gamma frequency comes out right (PING ~40 Hz). Our `r` runs ~10× high,
   suggesting a missing gain/normalization.
3. **Source code (the key ask).** Fig. 7.3 looks like an **AUTO-07P continuation**, not a
   time-integration — which is likely why our RK4 blows up on the stiff MPR spikes. Could
   we get the **AUTO-07P files + constants** (the table cites
   github.com/pclus/auto-tutorial) and/or a **robust Python time-domain integrator** for
   Eq. 7.9? With that we reproduce Fig. 7.3 exactly, then add the weak-field AM-drive
   resonance analysis for TN0484.

## Status in the paper
TN0484 currently contains a §4.6 "NMM2 PING" with figures from the unfaithful
reconstruction (and an incorrect "I≈11 Hopf / entrainment" description). We are holding
that section — it should not circulate — until we have the faithful model. The NMM2
*conceptual* point (exact mean field ⇒ the demodulating nonlinearity is the derived `v²`
term, not a postulated sigmoid; §2.1 + Methods) is independent of the simulation and
stands.

— Contact: Giulio. Repo: `ti_demod_demo/` (`code/nmm2_ping.py` is the current
reconstruction; `docs/current_state.md` has the history).
