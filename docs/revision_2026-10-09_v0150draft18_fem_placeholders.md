# FEM placeholders and the draft18 Overleaf handoff

October 9, 2026. Giulio's instruction was relayed by Klaus at 10:41 CEST.
The editing baseline is `3bfbfe2`; the preceding steering integration is
`02c26ac`. Version and title remain unchanged, and the reading redline remains
against draft13 `c620335`.

The later 10:49 CEST brief narrows the handoff to Overleaf only and adds an
isotropic orientation-average comparison. It supersedes the earlier release
plan: GitHub push and Calliope remain held. This clarification was relayed
immediately to Klaus before making the additional edits. This refinement starts
from `7162eea` and does not change any label numbers.

Ricardo's head-model update, relayed at 11:06 CEST, replaces the earlier Ernie
placeholder with an open IXI subject and a FreeSurfer hippocampal label. The
additional current-ratio predictions and their scope are recorded in
`revision_2026-10-09_v0150draft18_ixi_ratio.md`.

## Reserved Methods and Results

Methods Section 3.3 is titled "Head model and field computation (R. Salvador;
text to come)." Its red paragraph is marked `[PLACEHOLDER: ...]`. It reserves
the IXI subject with its FreeSurfer hippocampal label, the Violante montage,
conductivities, currents,
solver and boundary conditions, field-to-polarization conversion, region and
summary-statistic definitions, and the focus-displacement measure. It states
that projection directions remain fixed across current ratios. The separate
isotropic comparison averages the signed quadratic mixing term over uniformly
distributed orientations before taking its magnitude.

Results Section 4.5 immediately follows the JR curvature/square-law subsection.
Its red placeholder describes the three planned maps: envelope excursion,
quadratic excursion, and quadratic mean. The planned comparisons are 1:1,
1:3, and a ratio sweep, with target-to-cortex ratios and focus displacement in
millimeters relative to 1:1. All maps share the same local polarizations and a
fixed projection direction at each location. An envelope-maximizing direction,
if used, is selected at the reference ratio and then held fixed. A separate
isotropic orientation-averaged quadratic beat map is also planned.

Figure 8 (`fig:fem`) is a framed text box reading "FEM: envelope vs quadratic
maps on the Violante montage, IXI subject (FreeSurfer hippocampal label),
R. Salvador." Its red caption states that maps and results are to come.
Neither subsection reports FEM findings or estimated FEM values. The figure
contains no simulated map. The abstract is unchanged.

The new Methods and Results subsections shift later subsection numbers by one.
The new Figure 8 shifts the previous Figures 8–12 to 9–13. Equation, table,
and supplementary-figure numbering is unchanged. Cross-references have been
rebuilt, and the storyline's section and figure numbers follow the new order.
No previous explanation, example, figure, qualification, or result was removed.
Simulation code, data caches, and existing figure assets are unchanged.

## Validated bundle

The single source builds the final local draft18 bundle:

- `TN0484_jne.pdf`: 42 pages, including the red Methods placeholder on page 16
  and the Results paragraph on page 23; Figure 8 floats to page 25.
- `TN0484_jne_supplement.pdf`: 21 pages, with updated cross-references.
- `TN0484_envelope_demodulation.pdf`: 59 pages, with the same placeholders on
  pages 17 (Methods), 24 (Results paragraph), and 26 (Figure 8).
- `docs/redline_last_read.pdf`: 51 pages against the fixed draft13 baseline.
- `build/storyline/tn0484_storyline.pdf`: 13 pages, including the reserved
  Methods and Results locations.

All final logs have zero errors, undefined references, overfull boxes, or
duplicate-label warnings. The redline retains latexdiff font-size warnings
for deleted mathematics; its cross-references have settled. The article and TN
placeholders, redline, and
storyline additions were inspected visually. The shared abstract remains
296 words by texcount after expanding its four macros. The audit with hashes
and the label-number changes is `draft18_fem_placeholder_audit_2026-10-09.json`.

## Release responsibility

The latest instruction authorizes Klaus to synchronize Overleaf only after
receiving the final draft18 commit and PDFs. This pass prepares the files and
hands them over; it performs no external synchronization or publication.
GitHub push, Calliope and Zenodo releases, and coauthor circulation remain held.
Ricardo's FEM methods and results are pending, as are the author confirmations
already recorded in `todo.md`.
