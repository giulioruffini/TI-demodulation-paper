# Abstract: the Significance paragraph (proposal for Kaiti)

Date: 2026-10-21. Baseline: `planning/tn0484_abstract.tex` at `111f7ab` (297 words).
Status: proposal only; Giulio asked for a reading, not an edit. Not yet sent to Kaiti.

## Diagnosis

Objective, Approach and Main results read well. The Significance paragraph does not:

1. Its last sentence garden-paths. "Carrier sweeps, independent-amplitude tests, beat
   sweeps across states, and equal-power controls each test one stage" parses first as
   the noun phrase "each test", then collapses. It is also inexact: four items, three
   stages; the equal-power control distinguishes the steady shift from the beat
   (Introduction, l. 272-276), it does not test a stage.
2. Five one-sentence claims with no connective tissue. After the run-in heading it reads
   as a highlights list, not a paragraph.
3. "compartment boundaries" has no referent inside the abstract. The access stage has
   just talked about membranes, so a reader takes neuronal compartments; the body means
   tissue compartments (sec:dc, l. 600-606).
4. "direct low-frequency stimulation" can be read as direct brain stimulation. The body
   and Fig. caption say tACS (sec:tacs-results).
5. Three names for two objects: "steady source" (Results), "steady drive" and "steady
   shift" (Significance). The body's chain is source -> mean response/shift.
6. The three front-loaded qualifiers in "Under uniform conductivity, access, and
   detection, the steady drive ..." are the pattern Giulio flagged on 2026-10-06.

## Proposed \absSignificance (71 words; abstract total 300)

TI efficacy factorizes into access, detection, and amplification. For weak fields, dose
follows the product of carrier amplitudes rather than the envelope minimum, and
within a region of uniform conductivity, access, and detection, the steady source's
magnitude peaks on the region's boundary. TI and transcranial alternating-current
stimulation use the same circuit amplifier. Carrier sweeps, independent-amplitude tests,
and beat sweeps across states test one stage each; equal-power controls isolate the
steady shift.

## Not fixed (needs words the budget does not have)

Approach names the column, the mean field and the spiking network but not the
finite-element head model, whose result then appears in Main results. A referee may
note it. Adding it costs about ten words; the only places to find them are the
mean-field sentence of Main results or "We build a mesoscale model."


## Addendum 09:40 — Kaiti's 260-word proposal and Giulio's "DC-like" question

Kaiti's draft (relayed by Giulio) fixes the Significance paragraph and names the head
model in Approach, but drops: the "three stages in series" sentence (Objective, approved
2026-10-06); "dose follows the product ... rather than the envelope minimum"; the tACS
amplifier-sharing result (sec:tacs-results, own figure; absent from the whole abstract);
the DC boundary scope statement; the "slow relative to input" condition; and the
oscillation-threshold wording Giulio kept on 2026-10-19.

"DC-like": usable. The body already writes Y_DC and beat/DC; the applied field has no DC
component (l. 616), so "DC-like" for the detector output is exact. Use it once at first
mention of the steady source, then "steady shift" for the circuit's mean response.

"Focused deep DC-like (signed) effect": deep and signed are supported (hippocampal I rises
24% under 1:3; sign set by curvature, polarity-independent, l. 634). "Focused" is
contradicted by sec:dc: the mean-square map is subharmonic, no interior maximum in a
uniform compartment, 202-fold superficial/deep contrast in the paper's example vs 40-fold
for the beat; "interior selectivity must come from the oscillatory response" (l. 671).
Selectivity of the steady response can only come from the target's state (curvature), the
"separately weighted map" (l. 662, 675-677): state-selected, not focused.

### Merged proposal (300 words): Kaiti's structure + restored items + DC-like sentence

Objective. Temporal-interference (TI) stimulation applies kilohertz fields whose difference frequency is absent from the applied spectrum. We develop a mesoscale model with three stages in series: field access to a nonlinear membrane, detection of the difference frequency, and amplification by the receiving circuit.

Approach. Following single-neuron models, we represent access by a short effective membrane time. We analyze detection and amplification in a Jansen–Rit column, an exact mean field of quadratic integrate-and-fire neurons, and its spiking network, and compare spatial predictions in a realistic head model.

Main results. For weak fields, quadratic detection generates a beat proportional to the product of local carrier polarizations and a signed, DC-like steady source proportional to their summed squares. The static rate curve and exact mean field share this product law, while slow membranes add frequency dependence. With a published hippocampal montage, changing the current ratio moves the envelope and mean-square foci in opposite directions but only rescales the quadratic beat map at fixed neural state. Near a Hopf bifurcation, circuit gain grows inversely with modal damping and is shared with transcranial alternating-current stimulation. At a fixed Jansen–Rit operating point, coupling changes this gain but not detection; the amplified response appears mainly in beat-locked timing, with little change in mean rate. At stronger fields the steady shift alone can induce gamma, as can an equal-power unmodulated carrier.

Significance. TI targeting depends on the detector law and the circuit's state. For weak fields, dose follows the product of carrier polarizations rather than the envelope minimum. The DC-like source reaches deep targets with a sign set by the target's state, not by electrode polarity; within a uniform compartment no montage gives it an interior maximum. Local-polarization measurements, independent variation of carrier amplitudes, and beat-frequency sweeps across states test access, detection, and amplification, respectively. Equal-power unmodulated-carrier controls separate beat from steady-shift responses.

## Addendum 09:45 — Kaiti's two DC sentences (relayed by Giulio)

Her retraction of "preferential deep stimulation" is right; "at depth" is what the FEM supports.
Her sentence 1 ("Nonlinear detection also generates a DC-like steady shift whose sign depends on the
local operating point") duplicates Main results sentence 1 (signed steady source); detection makes the
source, the circuit makes the shift (Giulio, 2026-10-19). Her sentence 2 duplicates Main results
sentence 3 (foci move in opposite directions); "steers" is Violante's envelope verb and implies focal
control that sec:dc denies; the body says "moves" (l. 1893). Net new content: "operating point".

Proposed single Significance sentence (31 words), replacing the DC sentence of the merged proposal:

Detection thus supplies a DC-like steady source at depth, signed by the local operating point rather
than by electrode polarity; in a uniform compartment no montage gives it an interior maximum.

Fits 300 with "TI targeting depends on detector law and circuit state." (8 words) as the opener.

## Addendum 09:40 — Kaiti's 295-word abstract (relayed by Giulio): agree, three fixes

Checked against the body: 24% (l. 1891), scope list (l. 657-662), "no strict interior maximum",
threshold wording, slow-membrane condition, tACS, product dose: all restored and accurate.
1. Last sentence: "direct carrier rectification" collides with the out-of-scope "direct
   carrier-evoked spiking and conduction block" (l. 259, 1929). Use the Introduction's
   wording: "distinguish the steady shift from effects requiring the beat".
2. One term for the detector output: "steady source" (Results 1, Significance 2) but "steady
   shift" (Results last). Giulio's chain 2026-10-19: I map -> Y_DC source -> mean-rate shift.
3. The 24% sentence lacks its contrast (envelope -45%, beat -25%, l. 1899), which is what ties
   it to Violante's ordering. With the five spare words: "... rises by 24% from 1:1 to 1:3
   while envelope and beat averages fall" and drop "quadratic" before "beat map": 300 words.
Optional: "Weak-field beat dose" -> "For weak fields, beat dose" (+2, needs a cut elsewhere).
