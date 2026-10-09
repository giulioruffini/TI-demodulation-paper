# Current-ratio steering in draft18

October 9, 2026. The editing baseline is `b8c3dd4` on `two-tone-validation`.
Giulio authorized the additions through the October 9 brief; Klaus clarified
at 10:31 CEST that the earlier approval covered implementation. The reading
redline remains against draft13 `c620335`. Version and title are unchanged.

Klaus's delayed 10:33 CEST message accepts all five scientific refinements in
`0d15d14`, including the direct Violante contrast, and confirms their inclusion
in Giulio's reply draft to Ricardo. The manuscript additions are committed in
`02c26ac`. This acceptance concerns the proposed interpretation; the separate
bounded fidelity check of the integrated passages remains pending.

## Scientific changes

Section 2.5 now states the factorization after `eq:reweight` and its spatial
example. With one fixed electrode pair per carrier, fixed frequencies, linear
access, and fixed projection directions, each local polarization is its pair
current times a fixed spatial map. The leading quadratic beat therefore has
one common current-product factor. Its normalized map, maxima, and
target-to-cortex ratios remain fixed as the ratio changes, provided the
detector coefficients and linear network response stay fixed. This also holds
for a dynamic second-order detector and heterogeneous fixed gains; it does not
require a homogeneous head or prohibit an interior beat maximum.

The design consequence is to change at least one carrier's field shape, for
example with independently weighted electrodes at that carrier frequency.
Changing the ratio also changes the DC map and can shift local operating
points, indirectly reshaping the beat. Threshold effects can break the weak
quadratic prediction; they imply the conventional minimum map only when the
response follows the envelope.

Cassarà et al. (2025), Part II, Section 5.7, already identify the product-law
steering limitation. Their paper is cited in Theory and the new Table 4 row:
[doi:10.1002/bem.22536](https://onlinelibrary.wiley.com/doi/10.1002/bem.22536).
Ricardo's CRediT line records conceptualization of the current-ratio prediction
alongside his provisional head-modeling roles. His byline position and the
complete contribution line still await the respective author confirmations.

The new test row compares normalized beat maps and target-to-cortex ratios
while varying the currents of fixed pairs. Projection directions remain fixed
at each location, including an envelope-maximizing direction selected at a
reference ratio. DC measurements and a lower-amplitude repeat check the
fixed-state assumption. The realistic-montage and physiological beat-map
comparisons remain proposed tests; no FEM result is added.

## Violante comparison

The Discussion compares the actual 2+2 mA and 1+3 mA conditions. At fixed state,
the latter gives 3/4 of the quadratic beat everywhere. The DC ratio depends on
position: it is 1.25 only where the per-current polarization magnitudes match,
and can be smaller than one elsewhere. Equal summed currents do not ensure
equal local RMS polarization.

The published paper reports a direct encoding-stage BOLD contrast between the
conditions (P = 0.015), with no stimulation-by-region interaction (P = 0.76).
This corrects the brief's claim that no direct contrast was reported. Envelope
steering also has cadaver evidence, beyond the field models. The paragraph
acknowledges the BOLD and functional-connectivity effects while distinguishing
them from a measurement of the demodulated neural beat map. It does not infer
the detector law from which condition differs from sham. Sources and the
factorization checks are in
[the scientific review](current_ratio_steering_review_2026-10-09.md), including
the [published paper and supplement](https://synthneuro.org/wp-content/uploads/2023/12/2310violanteFULL.pdf).

## Notation, retention, and validation

The new symbols are `I_j^{pair}` for physical peak electrode-pair current (mA)
and calligraphic `P_j(x)` for signed local polarization per unit current
(mV/mA). They avoid reusing the existing normalized QIF current `I_j` or carrier
frequency `f_j`. Both are defined at first use and in the shared notation table.
No existing symbol is renamed, and the new display is unnumbered.

The shared abstract is unchanged at 296 words by texcount after expanding its
four macros. All existing scientific passages, numbered equations, figure
assets, and simulation code and caches are retained. The changes are the
Theory and Discussion paragraphs, the Table 4 row, the CRediT addition, one
notation row, and the Cassarà reference. The storyline follows these additions.
The pending CUT? passages remain untouched.

The working JNE article, fixed-baseline redline, and storyline were rebuilt:
42, 49, and 12 pages. Final logs have no LaTeX errors, undefined references,
overfull boxes, or duplicate labels. Equation, figure, and table numbers are
unchanged from `b8c3dd4`; the new reference changes citation numbers. The added
text, test and notation rows, and corresponding redline and storyline pages
were inspected visually. The prose checker found no mechanical style issues.
The audit and file hashes are recorded in `validation_current.json`.

The supplement and full-TN validation copies are retained from the authorship
pass; they are not new working editions. The manuscript source remains shared,
and those editions will be regenerated at an authorized cut. GitHub push, the
Calliope/Zenodo cut, Overleaf synchronization, and coauthor circulation remain
on hold.
