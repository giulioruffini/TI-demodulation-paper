# TN0484 / WP0185: the shared abstract is 297 words

Date: October 6, 2026. Version: 0.15.0-draft13. Starting commit: `cc0bab9`.

The four abstract macros contain the replacement supplied by Klaus through
Giulio at 13:53 CEST. TeXcount confirms 297 words, down from 321 and within
the requested 300-word limit. The three-stage framing, equal-power control,
and scope conditions on the coupling and DC claims remain. The JNE article,
TN, and storyline render the same abstract from these macros.

The manuscript source is byte-identical to `cc0bab9` after accounting for the
version number. The Introduction, all later sections, titles, captions,
equations, references, figures, caches, and numerical code are unchanged.
The storyline map is also unchanged apart from its version label. No
numerical rerun was needed for this abstract edit.

All builds pass without errors, undefined references or citations, overfull
boxes, or duplicate labels: JNE 36 pages, TN validation 54, supplement validation
20, storyline 10, and redline 39. The redline remains against draft9 `8016065`.
The TN and supplement validation builds are under `/tmp/tn0484_draft13_abstract/`;
the JNE article remains the working edition. Visual checks confirmed the
abstract layout in all three formats and the redline's Significance paragraph.
The abstract passes the prose checker.

The article count is 13,742 words, down 24; the supplement remains at 4,457.
These counts include text, headings, and captions, and exclude math,
bibliography, and front matter. Counts are in
`word_counts_draft12_to_draft13.json`; output hashes and logs are in
`validation_current.json`. The earlier Landau and published PEIX checks are
preserved in that record. Release and circulation holds remain.
