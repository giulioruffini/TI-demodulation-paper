# TN0484 draft16: readability and organization

October 6, 2026. Editing baseline: draft15 `22ce445`. Reading baseline:
draft13 `c620335`. Giulio approved Klaus's review `90273a6` at 18:43; the
later 18:55 message names the combined annotation, schematic, and readability
revision draft16. The title is unchanged, and the working PDFs retain their
stable filenames.

The preceding draft15 already incorporated Giulio's 26 annotations and the
corrected model schematic `c7ce5e0`. This revision applies the approved
readability review to that text. The original review is filed as
`readability_review_draft14_2026-10-06.md`; its line numbers refer to `a2aacd6`.

## Organization and retained content

The Results follow the JR chain, a separate TI-versus-tACS subsection (4.7),
NMM2 (4.8), and the QIF network (4.9). The shared-amplifier result leads with
linear-response equivalence, followed by the measured ratios and their
finite-amplitude limits. The timing result leads with the measured modulation
and mean-rate changes. The QIF section leads with the distinction between beat
modulation and induced gamma, immediately followed by the mean-field carrier
control; its spiking-network and cutoff qualifications remain explicit.

The AM-surrogate protocol is now Methods 3.1. The compartment matrix and cable
estimate are in Appendix B.1, and the single-cell rate and MPR Jacobian/phasor
derivation are in B.2. Theory retains their results, the time-scale conditions,
and one-filter accounting. The squared-envelope identity now introduces the
spatial comparison in 2.5. The eight-state PING agreement belongs with its
Results; endpoint-stability diagnostics belong with the Methods protocol.
The bifurcation-branch details are retained in Figure 3's caption, and the
phase-capture distinction remains in the vocabulary subsection.

Table 4 now contains the tests and qualifications formerly split between the
predictions enumeration and table. It retains polarization normalization,
independent network-gain measurement, amplitude and phase, threshold onset,
harmonic correction, finite-amplitude timing limits, and the distinction between
synaptic blockade and loss of cellular mixing. Existing carrier comparisons
remain cited. The Conclusion has one paragraph for each result: product and DC
maps, the shared amplifier, timing versus rate, and field-induced gamma.

The Introduction is shorter while retaining the access mechanisms, prior
short-time TI modeling, Raul's single-cell resonance, and cellular versus circuit
roles. Theory explicitly identifies the generic transfer with the JR sigmoid,
and the spatial paragraph states that focality must be computed from the product
map. The mean-map restriction remains conditional on uniform conductivity,
access, and detection; for a signed quadratic response it concerns magnitude.

## Review suggestions qualified or retained

The proposed universal 35% ceiling was not adopted: the computed supremum applies
to the specified matched-peak, open-loop logistic family. The Discussion states
what approaching it would require and keeps dynamic detectors outside that bound.
Follow-up at 20:23: the appendix's existing positive-mixture argument also bounds
bounded nondecreasing memoryless transfers under the same carrier-averaged
comparison. The logistic-only restriction was unnecessarily narrow; the derivation
and the next wording correction are recorded in
`detector_bound_scope_2026-10-06.md`. This follow-up does not change the manuscript
under review or make the numerical optimum a certified bound.
The proposed inference from phase-locking effects to a stronger detector was also
not adopted. PLV is an output statistic, not the generated-drive ratio; the
illustrative 0.8% estimate now ends with its consequence for the assumed JR access
budget and the measurement needed to test it. These are scope corrections to the
suggested wording, not new calculations.

The numerical JR settings remain explicit for reproduction. The operating-point
examples are retained rather than reduced to one example; psychedelic exposure
is no longer grouped under pathology. The tentative biological-rectifier list
is retained pending a decision to remove or substantiate it. The passages marked
CUT? below remain verbatim, so the proposed anatomical and time-scale
deduplication is intentionally incomplete.

## Removals requiring Giulio's decision

No listed removal has been applied.

| ID | Passage retained | Decision and consequence |
|---|---|---|
| C1 | 2.1, “The transfer curve summarizes…” | Merge with the earlier slope/curvature explanation only if its model-specific and dynamic-functional qualifications remain. |
| C2 | 2.8, “Cohen et al.'s periaxonal circuit…” | Remove the repeated anatomy paragraph only after retaining its 12 nm width, fitted decay, current-versus-field distinction, and AIS qualification in the time-scale table or a note. |
| C3 | 2.8, “Channel kinetics contribute…” | Keep the no-double-counting rule and the need to calibrate kinetics absent from QIF; a shorter version must preserve both. |
| C4 | 4.9, “At eta = 1.5, gamma activity…” | Remove this duplicate explanation only if Figure 11's caption remains the home of the gamma/fold distinction. |
| C5 | Discussion, “Table 3 summarizes…” | Condense after preserving the PWM-TI 1–100 ms sweep and strong-pulse qualification; these are not all in Table 3. |
| C6 | Discussion, “Weak amplitude alone…” | Remove the repeated slow-synapse paragraph, referring to 2.1 and 2.3 for its two time-scale conditions. |
| C7 | Discussion, “For scale, a reverberation time…” | Decide whether to retain the physiological quality-factor comparison, move it to a note, or remove it. |

The additional sentence naming channel rectification, threshold crossing, and
release events is a possible removal or citation target; it was not deleted in
this pass. No new simulation is required to decide these prose choices.

## Length and checks

Counts include text, headings, captions, and the imported model-schematic caption;
mathematical expressions are not counted as words. The shared abstract and
notation appendix are separate. The TeXcount command and complete section counts
are in `word_counts_draft16_readability.json`.

| Section | Before | After | Change |
|---|---:|---:|---:|
| Introduction | 973 | 758 | -215 |
| Theory | 5113 | 4444 | -669 |
| Methods | 2699 | 2913 | +214 |
| Results | 3232 | 3123 | -109 |
| Discussion | 1960 | 1866 | -94 |
| Conclusion | 230 | 279 | +49 |
| Main sections | 14207 | 13383 | -824 |

The shared abstract remains 296 words. The models appendix grows because it
receives the derivations; relocation is not counted as deletion of scientific
content. All 32 named equation labels, 25 figure labels including the schematic,
and 60 cited works remain. The squared-envelope equation has equivalent notation
after relocation; the other numbered equation bodies are unchanged. Figure numbers
and numerical assets are unchanged. Equation and subsection numbers necessarily
follow the approved moves; notation-table definition locations are updated, with
appendix context on references to the relocated cable equation. No glyph was
renamed; the existing E0 field amplitude is now explicitly defined.

The JNE article has 40 pages, the supplement 21, the private combined TN 57,
the storyline 11, and the redline 48. All builds have zero errors, undefined
references, overfull boxes, or duplicate labels. The manuscript and storyline
prose checks report zero findings; the note has only Markdown separator matches.
The audit is `readability_audit_draft16_2026-10-06.json`. Final build diagnostics,
hashes, inspected pages, and review status are in `validation_current.json`.
The redline stays against draft13. The combined TN is a private validation build;
the JNE article and supplement remain the working outputs. No new neural
calculation was run, because code, figure data, and simulation caches are unchanged.

GitHub push, Calliope/Zenodo cut, Overleaf synchronization, and coauthor circulation
remain on hold. This revision does not close author declarations or authorize
submission.

The combined revision is committed as `e07b44a`. A bounded read-only fidelity
check was requested from Klaus on that commit; the message was spooled, and no
verdict had been received when this record was written. It supersedes the earlier
`af29999` integration check and the separate request about Discussion wording.
