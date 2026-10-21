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
