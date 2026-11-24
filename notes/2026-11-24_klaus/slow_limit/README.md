# Theory 2.9 slow limit: replacement fragments (Klaus, 2026-11-24)

K, via Kaiti 15:05: "fix the slow limit, ask Klaus to revise". Base: live text after efa3802
plus my uncommitted r_syn -> u rename (K: "just don't use r for a voltage!!").

- sec29_before.tex / sec29_after.tex: from "If relaxation is faster than synaptic variation"
  up to (not including) "Outside the adiabatic limit". Replace the whole span.
- slow_synapse_before.tex (efa3802) / slow_synapse_after.tex (= current live, u rename).

Sequence in sec29_after: synaptic drive held fixed -> r and v relax -> r ≃ F(Q)/tau_m;
tau_rel << tau_s -> eliminate fast variables, keep dynamic synapses -> NMM2 static curve with
filtered recurrence; separate condition omega_c tau_rel << 1 for carriers; Brunel resonance
sentences kept. Field paragraph: current/voltage conversion kept; new linearization
delta r = (F'/tau_m)(lambda_I dE + tau_m J dr), then eq:slow-field-gain (label kept);
stationary derivative does not require slow synapses; clamped (u fixed) vs closed at the same
Q*; amplification 1/[1-JF'] on a stable equilibrium; JF'<1 necessary but with finite membrane
time not a complete stability test; feedback counted once; JR within- vs between-population.
No colon before displays. New unlabeled display for the linearization.

Claim to verify (my reasoning, not in the source): "JF'(Q*)<1 is necessary" on a stable
equilibrium. Argument: the Jacobian determinant of the closed (r, v, u, du/dt) system is
proportional to 1-JF'(Q*) times a positive factor, so JF'>1 gives a real positive eigenvalue.
If you cannot confirm it quickly, write "JF'(Q*)<1 does not by itself guarantee stability
with finite membrane time" instead.

Words (texcount): sec 2.9 span 203 -> 287 (+84); B6 45 -> 54 (+9). Total +93 over the article,
which is at exactly 12,000. Not cut: the added text is the explanation requested; K must
decide what to remove elsewhere.
