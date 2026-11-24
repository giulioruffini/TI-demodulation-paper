# Draft26 — consolidation and FEM reporting

Giulio approved Ricardo's November 4 corrections and requested a shorter,
clearer paper that preserves its key sentences and reads as connected scientific
prose. The editing baseline is draft25 at `0d80796`; the recorded reading
baseline remains draft20 (`e20c047`). This revision changes exposition and
reports existing FEM values. It changes no model, equation, simulation, or figure artwork.

## Argument and retained content

The steady and beat sources are introduced together. The operating-state
interpretation now follows the steady-source formula, keeping PEIX's sign
convention, physiological examples, and the distinction between static and
dynamic detection. The harmonic argument states the prediction in Theory,
the estimator in Methods, and the experiment in Discussion.

JR coupling methods now sit beside the JR model. The gain, mean-response,
and tACS results form one subsection, with paragraph headings for the changes
of observable and control. The text explicitly distinguishes the AM-surrogate
gain sweep from the genuine two-tone rate comparison. The MPR coefficient,
derivation, and limits share one appendix subsection and one unit convention.
No additional supporting material moves out of the article in this pass.

| Changed passage | Content that remains, and its home |
|---|---|
| Joint source introduction | The steady summed-square term and signed product term remain in Eq. (5); Eq. (6) defines the beat source before recurrence. The leading-order convention remains immediately below. |
| Operating-state subsection | All PEIX interpretation and examples move into the steady-source subsection. Zero curvature at the inflection and saturated tails, polarity invariance, negative curvature at the pinned state, dynamic exceptions, and the need to measure recurrent gain remain explicit. Exact PEIX identities remain in Appendix B.1. |
| Harmonic repetitions | Theory retains the network transfer ratio, resonance-induced harmonic suppression, amplitude sweeps, gain correction, and a threshold detector's ability to match one ratio. Methods retains the estimator, common window, mixed-family restriction and sign branch. Discussion retains the off-resonance experimental design. |
| JR protocol relocation | The complete protocol joins JR Methods: fixed voltage, Jacobian, field-free pinning, induced shifts, distinct waveforms, common rate/voltage readouts, source matching, and extended-window controls. Only its repeated introductory description is removed. |
| JR results consolidation | Fixed curvature, 30-fold amplification, inverse damping, saturation and path dependence remain. All rate-modulation and mean-shift values, their ratios, weak-drive scope, and secondary rectification remain. The tACS formula, predicted 0.143 ratio, measured 0.90–0.99 ratios, unequal inputs, and matching conventions remain. |
| JR caption | Keeps the surrogate, pinned state, curvature value, open-loop source, stable-focus scope, panel meanings, units, and inverse-damping guide. Growth and sharpening remain stated in both the paragraph and caption. |
| Direct-source comparison | Steady sources share the zero-frequency transfer; beat and tACS sources share the beat-frequency transfer. Their difference and additional rectification of the amplified beat remain explicit. |
| MPR appendix | Both former subsection labels resolve to B.3. The single-neuron rate, excitability average, normalized and physical units, coefficient, Jacobian, phasor, quadratic source, mean correction, limits, zero crossing, and parameter-dependent carrier classification remain. Only repeated setup and a heading are removed. |

The full PING equations remain in Methods, the access-evidence table remains
in Theory, and the lock-in construction remains in Methods. The efficiency
bound, worked superficial/deep examples, kHz feasibility argument, static/dynamic
sign crossover, 2–5% comparison, and qualitative finite-network interpretation
are unchanged. The abstract and every figure artifact are unchanged. The numerical
retention record is `notes/2026-11-04_kaiti/draft26_replacements.json`, supplemented
by `draft26_appendix_change.json`; source diffs remain the final text record.

## Ricardo's corrections

Table 3 adds one paired column of raw ROI-mean/reference-p95 contrasts:
0.81/0.58 (envelope), 0.61/0.61 (quadratic), and 0.47/0.54 (mean square),
for 1:1/1:3. These come from `conditions[ratio][map].tc_mean` in
`code/fem_quadmaps.json`. They are not degree-matched contrasts. The missing
square-root p95 contrast is restored as 0.90 (0.95), using
`conditions["1:3"]["msp"]["degree_matched"]["tc_p95"] = 0.950368484`.

The envelope's above-reference-p95 nodes have an anterolateral centroid and
are 52% white matter, compared with 25% across the ROI. The underlying counts
are 93/180 and 394/1568 (`upper_tail_1to1.env`). This describes the tail without
attributing the contrast causally to tissue identity. Figure 9(f)'s caption
now says “colors as in (e).” The +24% Discussion sentence remains unchanged.

The acknowledgment credits the [IXI dataset](https://brain-development.org/ixi-dataset/)
and its CC BY-SA 3.0 license. Code availability specifies that the per-node
export, when released, will be a separately licensed CC BY-SA 4.0 data file
with IXI attribution. The portable-data instructions carry the same prospective
requirement. IXI's source license was checked against its website; the
[3.0 legal code](https://creativecommons.org/licenses/by-sa/3.0/legalcode)
permits later licenses with the same elements for adaptations, and the
[4.0 terms](https://creativecommons.org/licenses/by-sa/4.0/) govern the planned
derived export. The repository LICENSE is unchanged, and no data release is made.

The gray-matter-only contrasts await Ricardo; only a source comment reserves
their place. The wider mean-change and node-fraction checks will enter the
supplement when supplied. PR #2 remains unmerged, so its second script and
JSON are not added to the availability claim.

## Length and checks

| Section | Draft25 | Draft26 |
|---|---:|---:|
| Introduction | 665 | 665 |
| Theory | 3,155 | 3,141 |
| Methods | 1,641 | 1,614 |
| Results | 2,682 | 2,700 |
| Discussion | 1,443 | 1,428 |
| Conclusion | 179 | 179 |
| Article appendices | 1,532 | 1,508 |
| Total | 11,297 | 11,235 |

The reduction is 62 words, including the new FEM column and interpretation;
the main narrative is 38 words shorter. The unchanged 299-word abstract gives
11,534 words in total. These comparative counts include headings, captions,
and tables, but exclude mathematical tokens, references, and declarations.
The added data-license clause and acknowledgment are outside that count:
declarations grow from 380 to 411 words, leaving a net reduction of 31 words
when they are included.
The article is 37 pages (previously 39), with the same 32-page supplement.
The page reduction comes chiefly from consolidation and float placement;
fonts, margins, and figure sizes are unchanged.

The preservation script verifies all 135 baseline labels and 67 citation keys,
all 32 labeled equation bodies, the shared abstract, full PING system,
efficiency derivation, original QIF/FEM inputs, figures, repository LICENSE,
reading baseline, annotated draft20, and preexisting canonical TN artifacts.
Article, supplement, and an isolated full-TN build pass error, unresolved-reference,
and overflow checks. The canonical TN PDF and bibliography are not regenerated.
A continuous read and an independent read-only review checked the moved
operating-state argument and combined JR narrative. The latter prompted explicit
waveform and predicted-ratio wording, plus a clearer reference to the
superficial/deep example. The mechanical prose check reports no findings.

The journal PDFs, current storyline, and canonical draft20 redline are the
reading copies. Rendered-page checks and Klaus's independent fidelity
review are recorded below. Public push, Overleaf, Calliope,
PR merging, and coauthor sending remain on hold.


## Rendered reading copies

All 37 article pages were inspected in contact sheets; the changed steady-source
passage, FEM table and caption, JR narrative, and MPR derivation were also
viewed enlarged. Table 3 retains 9.96-point body text (with smaller mathematical
superscripts) and fits without scaling. The six-page storyline and the revised
FEM and MPR pages of the 53-page draft20 redline were inspected. No clipping,
collision, or overflow was found. The rendered text contains the restored
waveform cue, predicted-ratio qualifier, and all new FEM values. The render
record is `notes/2026-11-04_kaiti/draft26_render_check.json`.


## Independent fidelity review and final restorations

Klaus's review of `0fbac10` against `0d80796` is recorded in
`notes/2026-11-04_klaus/draft26_fidelity_check.md` (`79e06a8`). He found the
science preserved and references resolved, and verified every FEM addition,
the operating-state relocation, JR protocol and results, and MPR derivation.
His four explanatory restorations are applied: Methods introduces the coupling
sweep's fixed-detection purpose and the amplitude sweep's discrimination between
linear and quadratic scaling; Results explicitly names the shared TI/tACS
amplifier; the gain caption names the approach in coupling and saturation.
The dynamic detector's coefficients are again called state-dependent. The
rate comparison is named by its observables rather than the former “timing”
heading, and the FEM tail sentence explicitly limits its nodes to the ROI.
These restorations favor continuity and local explanation over a larger cut.
The final reduction is 62 article words, or 31 including declarations.

Final article, supplement, isolated-TN, storyline, and redline checks are
recorded in `notes/2026-11-04_kaiti/draft26_artifact_manifest.json` and the
associated preservation/render records. The canonical journal PDFs are the
review copies; no separate delivery bundle is made. This revision remains local
and uncirculated, with its push guard intact.
