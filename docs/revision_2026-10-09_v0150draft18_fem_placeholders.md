# FEM placeholders and the draft18 release handoff

October 9, 2026. Giulio's instruction was relayed by Klaus at 10:41 CEST.
The editing baseline is `3bfbfe2`; the preceding steering integration is
`02c26ac`. Version and title remain unchanged, and the reading redline remains
against draft13 `c620335`.

## Reserved Methods and Results

Methods Section 3.3 is titled "Head model and field computation (R. Salvador;
text to come)." Its red paragraph is marked `[PLACEHOLDER: ...]`. It reserves
the Ernie model and Violante montage specification, conductivities, currents,
solver and boundary conditions, field-to-polarization conversion, region and
summary-statistic definitions, and the focus-displacement measure. It states
that projection directions remain fixed across current ratios.

Results Section 4.5 immediately follows the JR curvature/square-law subsection.
Its red placeholder describes the three planned maps: envelope excursion,
quadratic excursion, and quadratic mean. The planned comparisons are 1:1,
1:3, and a ratio sweep, with target-to-cortex ratios and focus displacement in
millimeters relative to 1:1. All maps share the same local polarizations and a
fixed projection direction at each location. An envelope-maximizing direction,
if used, is selected at the reference ratio and then held fixed.

Figure 8 (`fig:fem`) is a framed text box reading "Figure placeholder: FEM
envelope vs quadratic maps on the Violante montage, Ernie head model
(R. Salvador)." Its red caption states that maps and results are to come.
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
  and Results/figure placeholders on page 24.
- `TN0484_jne_supplement.pdf`: 21 pages, with updated cross-references.
- `TN0484_envelope_demodulation.pdf`: 59 pages, with the same placeholders on
  pages 17 and 25.
- `docs/redline_last_read.pdf`: 51 pages against the fixed draft13 baseline.
- `build/storyline/tn0484_storyline.pdf`: 13 pages, including the reserved
  Methods and Results locations.

All final logs have zero errors, undefined references, overfull boxes, or
duplicate-label warnings. The article and TN placeholders, redline, and
storyline additions were inspected visually. The shared abstract remains
296 words by texcount after expanding its four macros. The audit with hashes
and the label-number changes is `draft18_fem_placeholder_audit_2026-10-09.json`.

## Release responsibility

Giulio authorized Klaus to push, synchronize Overleaf, and update Calliope
after receiving the final draft18 commit and PDFs. Those actions remain with
Klaus; this pass prepares the files and hands them over. No external release
is claimed by this record. Zenodo release and coauthor circulation remain held.
Ricardo's FEM methods and results are pending, as are the author confirmations
already recorded in `todo.md`.
