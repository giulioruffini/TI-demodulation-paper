# Slow-limit candidate check — 2026-11-24

Reviewed `build/2026-11-24_live_prose_merge/slow_limit/main_candidate.tex` and `appendix_candidate.tex` against their `slow_main_before.tex` and `slow_appendix_before.tex` snapshots. The candidate passes the algebra, units, and scope checks. No correction is required.

The JR filter's steady gain is `A/a = A tau_s`. Writing the physical PSP voltage as `P = A tau_s u` in `P'' + 2a P' + a²P = Aa r`, with `a = 1/tau_s`, gives `tau_s² u'' + 2 tau_s u' + u = r`. Thus `u` has rate units, while `r` remains firing rate throughout. The equilibrium equality `u = r` is between quantities with the same units; the physical PSP remains `A tau_s u`. The candidate removes the earlier appendix's ambiguous second division by the steady gain.

The recurrent input `tau_m J u` is dimensionless. At an equilibrium, differentiating the stationary relation gives `delta r = [F'(Q*)/tau_m][lambda_I delta E + tau_m J delta r]`, hence the displayed field susceptibility. Clamping `u` at its equilibrium value gives the stated numerator at the same total drive `Q*`. The ratio of the two susceptibilities is `1/[1 − JF'(Q*)]`.

The candidate distinguishes instantaneous use of the static curve, justified when the input changes slowly relative to local relaxation, from the exact derivative of a stationary branch, which needs no timescale separation. Synaptic dynamics remain present, and the separate carrier-tracking condition is retained. “At stable equilibria with” preserves stability as an independent qualification rather than presenting the denominator test as a complete dynamic stability criterion.

The external-drive qualification on fitted rate curves prevents automatic attribution of recurrent gain to a curve fitted against total drive or mean voltage. Input conversion, matched local slope and feedback, and the distinction between within-population recurrence and between-population connections all remain. Only this review note was written; no source edits, builds, or commits were made.
