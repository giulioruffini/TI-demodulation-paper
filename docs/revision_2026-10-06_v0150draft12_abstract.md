# TN0484 / WP0185: the mesoscale model connects three stages

Date: October 6, 2026. Version: 0.15.0-draft12. Starting commit: `01f4cbb`.
Authorization: Giulio's approved abstract, relayed by Klaus at 13:41 CEST.

The shared abstract now identifies the paper as a mesoscale model with access,
detection, and amplification in series. Each stage has a measurable contribution
and a test. The four macros in `planning/tn0484_abstract.tex` contain the approved
text, with only the scope additions requested in the handoff:

- Independent control of gain is limited to the Jansen--Rit column with its
  field-free operating point held fixed. Methods and Results hold the background
  sigmoid curvature fixed in that sweep; the finite stimulation-induced mean
  shift remains part of the response.
- The montage statement is limited to a homogeneous tissue compartment with
  uniform access and detection. The body proves the absence of a strict interior
  maximum for the intensity map in a homogeneous, isotropic, source-free
  conductor with spatially fixed coupling. It explicitly separates that map
  from a physiological response with spatially varying access, orientation, or
  curvature. The abstract therefore includes uniformity as well as homogeneity.

The Introduction's closing paragraph maps carrier-frequency measurements of
membrane polarization to access, independent variation of the local amplitudes
to detection, and beat-frequency sweeps across operating states to amplification.
Equal-power carrier controls separate the steady shift from beat-locked activity.
The storyline loads the same abstract and now states this test mapping in its
opening argument and Introduction row. Its abstract type size and leading were
adjusted from 12/15.4 pt to 11.5/14.2 pt to keep the abstract and explanatory note
together on the first page.

No title or heading changed. Everything from Theory through the end of the
manuscript is byte-identical to `01f4cbb`, including the membrane-once argument,
coupling-sweep separation, and near-Hopf TI/tACS ratio details. All figure
captions, labels, and cited keys are unchanged. Numerical code, caches, figures,
and bibliography are unchanged. The citation metadata now matches draft12;
no release date has been assigned.

TeXcount gives 321 abstract words, up from 285. The Introduction, including its
heading and figure caption, grows from 905 to 958 words. The article totals
13,766 words, up 89; the supplement remains at 4,457. These counts include text,
headings, and captions, and exclude math, bibliography, and front matter.
`word_counts_draft11_to_draft12.json` records the section counts. The approved
abstract was checked word for word after removing the two scope additions.

All five builds pass with zero errors, undefined references or citations,
overfull boxes, and duplicate labels:

- JNE working article: 36 pages, `TN0484_jne.pdf`.
- TN validation: 54 pages, `/tmp/tn0484_draft12_abstract/tn/tn_validation.pdf`.
- Supplement validation: 20 pages, `/tmp/tn0484_draft12_abstract/supp/supp_validation.pdf`.
- Storyline: 10 pages, `build/storyline/tn0484_storyline.pdf`.
- Current redline: 39 pages, `docs/redline_last_read.pdf`, against the unchanged
  draft9 baseline `8016065`.

The rendered abstract is identical across the JNE article, TN, and storyline.
Visual checks covered the article abstract and Introduction closing paragraph,
the TN abstract, the storyline opening pages, and the redline abstract. The prose
checker reports no findings for the manuscript, abstract, or storyline.
`validation_current.json` records output hashes, logs, and retention checks,
while preserving the earlier numerical fidelity and published PEIX reviews.
No numerical rerun was needed for these text changes.

Author review, declarations, and length review remain pending. No push, archive
cut, Overleaf synchronization, or coauthor message was sent. The TN and supplement
above are private validation builds; the JNE article remains the working edition.
