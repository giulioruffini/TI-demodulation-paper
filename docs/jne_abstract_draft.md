# Structured abstract for JNE (draft)

JNE uses bold run-in headings — Objective / Approach / Main results / Significance — each
ending in a period, with no line breaks between them. Cap is 300 words. Draft below is 292,
which leaves little headroom — any addition during revision needs an offsetting cut.

The content is the existing abstract reorganized, not rewritten: no claim has been added,
strengthened, or dropped. The one substantive change is that the modeling ladder, which the
current version compresses to "a heuristic cortical column and an exact next-generation mean
field," is stated in full under *Approach*, since JNE referees read that heading as the
methods summary and the LaNMM and QIF layers are load-bearing for the generality claim.

---

**Objective.** Temporal-interference (TI) stimulation applies two high-frequency currents
whose amplitudes beat at a low difference frequency, offering focal, steerable stimulation
deep in the brain. A puzzle sits at its core: an amplitude-modulated field carries no
spectral power at the beat frequency, so no passive, linear element of a neuron can follow
it. Recovering the beat requires a nonlinearity, which has generally been sought in
single-cell ion channels. We ask whether demodulation and its frequency tuning are instead
properties of the neural population.

**Approach.** We treat the firing-rate nonlinearity of a neural mass, the
$\sim$$10^4$-neuron unit that generates the EEG, as an amplitude detector, and its recurrent
synaptic network poised near a Hopf bifurcation as a resonant amplifier. The account is
tested across a modeling ladder: a heuristic Jansen–Rit column, a laminar model (LaNMM), an
exact next-generation mean field (NMM2), and the QIF spiking network underlying it.

**Main results.** Sigmoid curvature acts as a square-law detector that recovers the beat,
and the network amplifies it resonantly at its own natural frequency. Detection is inherited
from the single neuron; the sharp frequency selectivity is emergent, set by proximity to
criticality and tunable by connectivity. The mechanism reproduces TI's known behavior:
independence of the carrier once membrane polarization is matched, largest response when the
beat matches a region's intrinsic rhythm, and, because the resonance amplifies oscillatory
timing far more than mean rate, realignment of spike timing without a change in firing rate,
as observed in vivo.

**Significance.** TI efficacy should be as much a property of the brain as of the device,
depending on brain state and regional connectivity. The cortical column behaves as a tuned
AM radio receiver, which reframes dose optimization around the target's dynamics and yields
falsifiable predictions listed in the paper.
