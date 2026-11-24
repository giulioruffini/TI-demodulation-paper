# Ricardo's November 6 FEM results

Read on November 7. Source: the Neuroelectrics Gmail thread, message
`1a1b29568bc5df98`, sent November 6 at 21:38 CET, and Giulio's preceding
November 4 reply. The manuscript baseline is `146679e` (draft27). PR #2 remains
open at `6ade413dd88b7d525466ff1eeaad003f449150cc`. The connected GitHub tools
were unavailable; the files were retrieved read-only through GitHub CLI.

## Scientific interpretation

The gray-matter-only comparison reduces the reported deep-target contrast.
At balance the envelope's ROI-p95/reference-p95 contrast is 1.086; both
quadratic beat measures are below one, including degree matching. This supports
the distinction between envelope maps and detector dose maps, while limiting
claims of hippocampal beat selectivity. It remains a geometric illustration in
one head, before detector and circuit weighting.

| Map, GM-only hippocampal ROI | Raw p95, 1:1 / 1:3 | Degree-matched p95, 1:1 / 1:3 | Raw mean contrast, 1:1 / 1:3 |
|---|---|---|---|
| Envelope | 1.086 / 0.839 | same | 0.757 / 0.547 |
| Quadratic beat | 0.935 / 0.935 | 0.967 / 0.967 | 0.508 / 0.508 |
| Isotropic beat | 0.943 / 0.943 | 0.971 / 0.971 | 0.512 / 0.512 |
| Mean square | 0.715 / 0.765 | 0.845 / 0.874 | 0.396 / 0.462 |

The mean-square increase survives all eight distinct montage × label × tissue
variants: +17.2% to +29.7%. The envelope decreases by 43.9–46.2%; both beat maps
decrease by 25%. Focus fraction does not affect an ROI mean, so eight is the
appropriate count for this result. The existing 32-combination statement about
focus displacement remains correct. The baseline +24% sentence in Discussion
also remains correct. These checks support a geometric ordering, not a
validation of the proposed BOLD interpretation.

The corrected node counts use the paper's fixed n* convention: mean square
rises at 1,353/1,568 nodes (86.3%, not about 95%), and the envelope rises at
2/1,568 (0.13%, not zero). Across variants the corresponding ranges are
80.8–90.9% and 0–0.2%. The reference is all gray matter outside the ROI, not
only cortex. Its baseline envelope-rising fraction is 8.9%. The analytic
thresholds remain |a/b| < sqrt(5/3) and |a/b| > 2. The rare local-envelope
alternative therefore remains possible; its frequency should be stated.
The earlier informal 95% and zero estimates were never inserted into draft27.

## Verification and manuscript destinations

The GM-only values and summary ranges match the committed JSON. Recomputing
the ranges from its eight variants gives the same results. A recursive
comparison against the live `code/fem_quadmaps.json` finds no changed or
removed existing leaf values. The new fields are recorded in
`ricardo_verified_values.json`, together with source hashes. This checks the
stored outputs; it does not rerun the private field solver or producer.

Table 3 can retain its width by adding an indented GM-only subrow beneath each
existing map, with the original rows identified as GM+WM. Parentheses already
denote degree matching and should keep that meaning. The new variant ranges
and node counts belong in `planning/parts/steering_algebra.tex`. The article
needs only a short statement of the GM-only contrast. No abstract change is
needed. The approved November 4 integration scope already covers these items.

The proposed PR #2 interface text must use <0.05% above the own-maximum
ceiling, 1.6–3.3% below its floor, and the actual minima, rather than “none”
or “just below.” The continuum theorem remains distinct from discrete field
recovery. Klaus independently checked the new JSON at `e6cbe69`. The tail statistics
are consistent with scatter in reconstructed normal components; conditional
medians do not by themselves identify the cause of every violation. Some
below-floor subsets have median normal ratios above one, so the text must
retain the distinction between association and explanation. The CSF comparison is a p99 comparison, so the wording must refer to
the upper tail. The unsupported attribution of remaining interior maxima to
field-recovery noise should not enter the paper. These are proposed additions,
not errors presently printed in draft27.

## Export and next actions

Ricardo reports a 45.7 MB FreeSurfer-only NPZ, with both montages' fields and
derived n*, and a check of 76 numerical values plus eight rising-node counts.
The export itself is not committed and has not been received here. Its atlas
label is omitted on Ricardo's licensing assessment. The bundle consequently
cannot reproduce the Neuromorphometrics sensitivity results or the interface
analysis, which also requires mesh/side-element information.

The current `code/fem_portable.py` requires both `aseg` and `atlas` masks and
uses a different key schema. It should accept explicitly declared available
labels and map Ricardo's keys without changing their precision or meaning.
Do not invent an atlas mask or substitute the FreeSurfer mask for it. The
independent consumer must then check the supplied file, including sweep and
centroid outputs beyond the exporter's stated 76-value check. The data
availability text must describe this partial reproduction scope accurately.

A separate Zenodo data record is the preferred eventual home: it keeps the
data license, attribution, version, and DOI together. Obtain the actual file
and SHA-256 first and validate it locally. Publication remains held. No email
has been sent, no Gmail draft created, no PR merged, and no manuscript or
scientific code changed during this assessment.

The exporter checks 76 numerical values and eight node counts, but its current
module-level import still requires the producer's private library. A standalone
check should move that import inside the export path, accept the received NPZ,
and reject nonfinite values explicitly. The existing `inputs_sha512` name is
misleading: Ricardo already confirmed on October 30 that those digests are
BLAKE2b-512. No further author clarification is needed on the algorithm.

Independent review: `notes/2026-11-07_klaus/ricardo_2026-11-06_interface_export_check.md`.
The manuscript destinations and consumer-schema mismatch were also checked
read-only by the retention reviewer. Neither check received the NPZ.
