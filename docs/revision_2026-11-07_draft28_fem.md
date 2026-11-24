# Draft28 — Ricardo’s FEM additions and main-results presentation

Giulio authorized the manuscript integration on November 7. The editing
baseline is draft27 (`146679e`); draft20 (`e20c047`) remains the reading baseline.
The additions come from Ricardo’s November 6 email and PR #2 head `6ade413`.
The two supplied JSON files are imported unchanged. Eight producer, output,
provenance, and proposed-data-license files are imported locally; this is not a
remote PR merge or a data release.

## Manuscript changes

Table 3 adds indented GM-only contrast rows. At 1:1, only the envelope p95
contrast exceeds one; at 1:3, none does. Every ROI-mean contrast is below one.
The text retains the distinction between geometric exposure and physiological
selectivity, the white-matter contribution to the upper tail, and the original
current-ratio and centroid results. Two brief sentences introduce the laminar
projection and interface measurements. The Discussion’s +24% comparison with
Violante remains unchanged and explicitly hypothetical.

Supplement S3 contains the complete raw and degree-matched GM-only comparisons,
eight ROI-mean variants, and corrected node fractions: mean square rises at
1,353/1,568 baseline ROI nodes (86.3%), while the envelope excursion rises at
2/1,568 (0.13%). The mean-square ROI increase ranges from 17.2% to 29.7% across
variants. ROI-mean variants are distinguished from the 32 centroid checks;
these changes concern the spatial mean of the envelope excursion, not its
temporal mean.

New S3 subsections define the anatomical directions, valid laminar samples,
map-specific orientation maxima, and cap-overlap check. They derive both sides
of the continuum interface bound and distinguish own-maximum maps from fixed
projections. The text reports numerical exceptions, identifies the fields used
for direction optimization and jump measurement, and separates facewise from
node-averaged continuity. The normal-jump statistics do not establish a cause
for every bound violation. Mesh convergence remains unresolved. Both modules
are inlined once in the full-TN edition.

The producer and exporter scripts, provenance document, and availability text
now name the additional analysis. The per-node NPZ has not been received or
independently validated. The existing NumPy prototype requires adaptation to
its FreeSurfer-only labels; the private library’s exact revision and original
solver inputs remain pending. The public repository license is unchanged.

## Length and verification

The article remains 37 pages, with 11,269 words across narrative, headings,
captions, tables, and article appendices: four fewer than draft27. The unchanged
abstract adds 299 words. The supplement grows from 32 to 35 pages. Fonts,
margins, and figure sizes are unchanged.

The preservation check passes all 135 baseline labels, 67 citations, and 32
labeled equations. The abstract, full PING system, original model code, figure
sources and artifacts, all non-FEM scientific modules, and all 3,104 prior
FEM-output leaves are preserved. Both new JSON files match the supplied PR
head byte for byte. All 44 cached FEM arrays still agree exactly with their
JSON sweep values; interpolated slices retain the expected 0.75 scaling within
float32 precision. These checks do not rerun the private field solve or producers.
The three imported Python scripts pass syntax compilation.

Article, supplement, and isolated full-TN builds pass without undefined or
duplicate references, overfull boxes, or printed question-mark references.
The storyline and draft20 redline also build. Independent rendered-page review
covers article pages 19–21 and S3 pages 12–16; tables and references are legible.
Canonical full-TN PDF/bibliography and the annotated draft20 retain their
pre-edit hashes. Check scripts, counts, and source assessment are in
`notes/2026-11-07_kaiti/`; local build logs are in `build/validation_draft28/`.

## Presentation

`presentations/tn0484_main_results.tex` produces eleven main slides and two backups.
The deck covers the carrier-product law, signed steady source, single-head
geometry, fixed-detector recurrent gain, dynamic sign crossover, direct-input
comparison, conditional kHz budget, and equal-RMS mean-field control. The new
GM-only contrasts and node fractions are included. Figure excerpts retain their
axes and data; finite-network convergence remains qualified. All thirteen slides
have been rendered and inspected, with no overflow or clipping.

Remote PR merging, public push, Overleaf, Calliope, data release, and coauthor
circulation remain held. No email or draft was sent or created.

## Independent fidelity review

Klaus’s review (`81630ee`) of `b42fb1e` against draft27 and Ricardo’s PR head
found no scientific omission or numerical error. He checked every new main-text,
S3, and presentation FEM value against the supplied JSON, both sides of the
continuum bound, and the distinction between node means and face continuity.
His two clarifications are applied: the article now says mesh convergence
remains untested, and Methods points to both relevant sensitivity subsections.
The optional GM-only mean-change entries remain in S3 to keep Table 3 focused
on contrasts. The final builds and preservation checks pass after these edits.
The presentation adds a closing slide stating the conclusions, unresolved
physiological calibration, and discriminating measurements.
