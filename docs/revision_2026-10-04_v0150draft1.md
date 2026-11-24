# v0.15.0-draft1: carrier evidence and claim corrections

This local repair draft integrates Klaus's R6 calculation and the submission-readiness
findings against v0.14.6 (`9bc574c`). It is not a release. The weak-field effective-response
argument, both abstracts, section order, and all 22 included figure identities remain.
The three placement decisions remain with Giulio. No material is relocated or removed
to meet a length target.

Klaus's evidence commit `f65a047` is integrated as `cb37926`; the reproduction repairs
are committed as `43bdc5a`. The manuscript replaces the unsupported LaNMM 7%/25%
comparison with a defined mean lock-in over 17 beats away from alpha. A new table gives
both measurement windows and both target conditions. The interpretation concerns
carrier profiles at the specified finite amplitudes. It does not establish phase
capture, remove every autonomous component, or compare target sensitivity at equal
power. The evidence and corrections to the original handoff are recorded in
`r6_integration_2026-10-04.md` and the verified JSON summary.

## The review items are resolved at the revised claim level

| Item | Disposition in this draft |
|---|---|
| R1, R8, R11, R13 | Earlier scoped closure retained: model claim level, specified detector classes, no exponent inference from an unspecified PLV mapping, and static versus dynamic QIF mixing. |
| R2 | The one-point open-loop two-tone/AM control verifies the local source. Theory, Results, and caption no longer treat it as quantitative validation of the recurrent surrogate near Hopf. |
| R3 | A sum of compartment magnitudes is explicitly phase aligned; complex input transfers are required otherwise. Access is counted once. |
| R4 | JR curvature is fixed while damping, modal frequency, and input/output projections can change. The PING error bound applies to four tested stable points, not the complete coupling sweep. |
| R5 | QIF mean-rate changes are about 8–11%. Beat-locked modulation exceeds the mean shift; categorical timing-without-rate language is removed. |
| R6 | Unsupported percentages are replaced by the preserved lock-in calculation, defined averaging/normalization, two-window table, and background controls. |
| R7 | Maps report frequency dominance; rate folding reports beat-locked rate modulation. They do not establish phase capture or uniquely identify gamma-amplitude gating. The theoretical capture mechanism remains explained. |
| R9 | The two-pole denominator uses the eigenvalue convention consistently, including G(0). Exact network peaks also depend on the numerator. Leading inverse-damping scaling remains. |
| R10 | The corrected weak-input efficiency trend from v0.14.5 is retained. |
| R12 | Figure dependencies, scratch-output routing, and spectrum labels are repaired and checked. The unavailable kHz two-tone producer is explicitly disclosed; this illustration is replot-only. This is closure of the reproduction claim's scope, not recovery of that producer or a complete convergence audit. |

The gain audit found an additional units error. The open-loop JR detector returns a
rate in s⁻¹; the recurrent readout is a voltage in mV. Their ratio has units mV·s.
The notation table, coupling-sweep text, and gain-axis labels now say so. The
carrier-profile panel normalizes each curve by its own 300 Hz response, preserving
all numerical data while avoiding an overlay of unlike units on one axis. The caption
gives both absolute values (0.00670 s⁻¹ and 0.512 mV) and their 76.4 mV·s ratio.
The former “60×” statement is withdrawn. The detector amplitude uses absolute
curvature; signed curvature remains the coefficient for phase-sensitive mixing.

The lock-in explanation now states the finite-window limitation without asserting
exact cancellation of other frequencies. Cifra's reviewed field ranges are described
as protocol dependent. Plovie's given name is corrected to Tom. Bibliography month
macros and cross-document citation imports are repaired.

Seven figure outputs are refreshed: JR two-tone spectra, carrier profiles, coupling
gain, frequency dominance, both LaNMM signed maps, and the cached kHz spectrum.
Only labels, normalization, and layout change. The 22 figure identities and their
order are unchanged; no original simulation cache is modified. The historical QIF
step/threshold check is preserved as `qif_resolution_check_2026-09-22.txt` and is
identified as a historical run, not a new convergence test.

## Verification and remaining work

The runner's nine regression tests pass. An isolated tree assembled from tracked
inputs generated the previously missing concept/resonance dependencies and rendered
the requested figures into scratch directories. Cached LaNMM/kHz plotting and JR
spectrum labels were checked separately. The logs are preserved as
`r12_fresh_check_2026-10-04.txt` and `r12_cached_check_2026-10-04.txt`. This was a
targeted dependency/reproduction check, not a fresh execution of every simulation.

The independent R6 cache summary matches the reported table and records input hashes.
A separate 12 s field-free integration confirms the persistent 8 Hz background and
the approximately 39.7 Hz gamma peak. The JR matrix check confirms changing modal
projections with fixed local curvature. Original data remain unchanged.

The clean builds contain 48 TN pages, 31 JNE article pages, and 19 supplementary
pages. The storyline has eight pages and the redline has 49. They have no LaTeX errors, undefined references
or citations, or overfull boxes. A float-only page notice and one underfull
bibliography line remain. The redline uses the v0.14.6 baseline and the existing
CFONT/whole-math recipe. Adjacent inline-math delimiters are joined in temporary
comparison copies only. A deleted paragraph that latexdiff inserted into the new
table is moved before that table in the comparison source, preserving the deletion.
The redline shows text changes; the revised figures are present without graphical
pixel differences.

Rendered-page inspection covers both front pages, the revised gain/units and
access passages, Appendix E and its new table, the affected supplementary captions,
all eight storyline pages, and the redline equation/table/availability changes. No
clipping or overlap was found on those pages. The manuscript prose checker reports
no findings; its two review-note flags concern Markdown table separators, not prose.
The redline retains a harmless CFONT math-size warning and underfull-line notices.

Versioned review copies are exported under `build/`; the existing live source and
legacy output paths are preserved during active review. Full folder-layout migration
is deferred to the next coordinated version boundary under the
[personal handbook](../../../giulio-personal-handbook/dos-and-donts.md#paper-folder-layout-and-versions).

Giulio and Klaus should review this fixed draft before the submission decision.
Funding for Grossman, Canals, and Mirasso, remaining competing-interest declarations,
author roles/affiliations, actual historical AI-tool versions, and approval of the
submission version by all authors remain open. The original producer and complete
settings for the cached kHz two-tone illustration have not been recovered. No HH
calibration or new periaxonal model is required for the paper's scoped argument.

GitHub push, Calliope/Zenodo release, Overleaf synchronization, and coauthor email
remain held. Align the public code/archive with the approved submission version
before making the availability statement current.
