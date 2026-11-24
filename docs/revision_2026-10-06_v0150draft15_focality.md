# TN0484 draft15: envelope and quadratic focality maps

October 6, 2026. Baseline: draft14, `a2aacd6`, on `two-tone-validation`.
Giulio's integration decision was relayed by Klaus at 17:52. The current JNE
redline remains against the last specified reading baseline, draft13 `c620335`.
This record and its source audit describe the integration committed as `972d9ea`.
The later ratio-symbol changes are recorded separately in
`notation_ratios_2026-10-06.md`.

Section 2.4 now contains the reading note's comparison table, adapted to signed
local polarizations `epsilon_1(x)` and `epsilon_2(x)`. Table 2, on article page 11,
compares the slow signal, beat-period mean, and modulation excursion before
detector gains. The text distinguishes a mean detector output from a DC electric
field and defines the envelope mean explicitly. The existing two-site example
is retained verbatim; the note's alternative example is not duplicated.

The mean-map argument on page 12 now covers the envelope mean as well as the
quadratic intensity. At fixed beat phase, the envelope is the norm of a vector
of harmonic functions. Convexity makes it subharmonic, and beat averaging
preserves that property. The stated homogeneous, source-free, fixed-access
conditions remain attached to the result. Spatial variation of cellular weights
and the distinction from physiological responses remain explicit. The beat
product has no corresponding maximum-principle restriction.

The spatial interpretation is clarified accordingly: quadratic reweighting can
change the envelope map's contrast, while a modulation maximum can survive in
both descriptions. Circuit selectivity acts on top of that spatial weighting.
These statements replace the categorical wording that could be read as excluding
spatial selectivity altogether. The finite-element comparison is stated as a
proposed test, not a completed head-model result. Giulio will request Ricardo's
comparison separately; no request or computation was made here.

Figure S13, on supplement page 19, uses the note's two-panel line profile and
caption. The amplitudes are renamed to the manuscript's notation. The length
symbol is `L_x`, since `L` already denotes a logistic function in Appendix D.
The same producer now accepts `--paper`; the curves, normalizations, and numerical
integral checks are unchanged. The note remains an internal reading document
and its PDF is unchanged. No new appendix was added.

## Validation

The article has 40 pages, the supplement 20, the private combined TN 55, and
the storyline 10. The current redline has 42 pages. All builds have zero errors,
undefined references, overfull boxes, and duplicate-label warnings. The article's
new table, mean-map argument, updated notation row, supplementary figure, and
redline were inspected in the rendered PDFs. The figure collision/size check
and the manuscript prose checker report no findings.

All 32 labeled equations and 23 existing figures retain their numbers; S13 is
the added twenty-fourth figure. Table 2 is new, so the article's access table,
prediction table, and notation table become Tables 3, 4, and 5. Supplementary
table numbers are unchanged. The cited-key set remains 60 and the 297-word
abstract is unchanged. Section 2.4 grows from 957 to 1304 words by the same
`texcount -sum -1` command, including its new table and caption.

The source audit in `focality_integration_audit_2026-10-06_draft15.json` verifies
that the body outside Section 2.4 and the added figure is unchanged, apart from
the version. Existing simulation producers, caches, and figures are untouched.
The figure producer is
`notes/2026-10-06_ti_focality/make_spatial_maps.py --paper`; its numerical checks
are in `notes/2026-10-06_ti_focality/map_checks.json`.

Klaus's earlier independent review of the reading note is recorded in its
README. A bounded check of this integration was requested; no integration
verdict had arrived when this record was written. The other harvested
annotations remain pending. All release and circulation holds remain.
