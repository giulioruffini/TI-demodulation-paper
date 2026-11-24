# Ricardo Salvador joins the draft18 author list

October 9, 2026. Giulio's instruction was relayed by `giulio-shell` at 09:38 CEST.
The scientific baseline is draft17 `8dc6eca`; the repository checkpoint is
`7d0a93f`, which also retains the subsequent review records. The reading redline
remains against draft13 `c620335`.

Ricardo Salvador is included after Borja Mercadal in the article and supplement
byline, the TN authors table, and the PDF metadata. His affiliation is
Neuroelectrics, Barcelona, Spain. The ORCID list and `CITATION.cff` include
`0000-0003-1235-6533`, supplied as registry-verified in the instruction. The README
author list and working-version references agree. His position after Borja is
provisional and awaits Giulio's confirmation.

The competing-interests statement includes Ricardo among the Neuroelectrics
employees. His provisional CRediT line reads: methodology (head modeling),
software, formal analysis, visualization. The rendered declaration explicitly
marks this line for his confirmation. His funding is also pending confirmation;
the existing GALVANI acknowledgment has not been extended to him by assumption.

Ricardo will run the real-montage FEM comparison requested by Giulio on October 8.
No FEM data or result is available in this revision. The comparison remains a
proposed test, and the abstract, scientific body, and appendices are unchanged.

## Placement proposal for the FEM result

The following proposal was relayed by `giulio-shell` on October 9 at 09:38 CEST
and remains for Giulio's decision. Nothing is to be implemented until the FEM
results exist. It places the spatial consequence of the detector law directly
after the JR curvature result, replacing this note's initial suggestion of a
subsection immediately before the Discussion.

- Theory Section 2.5 retains the algebra, `eq:reweight`, and Table 2, and gains
  one forward pointer to the FEM result.
- Results gains a subsection directly after the JR curvature/square-law
  subsection (`sec:results-curvature`, currently Section 4.4). Its title states
  the finding; for example, "On a realistic montage, the product map changes the
  target-to-cortex contrast" only if the computed result supports that claim.
  One figure shows slices of the envelope excursion, quadratic excursion, and
  quadratic mean for one standard deep-target montage, with target-to-cortex
  ratios for each map.
- Methods gains "Head model and field computation," written by Ricardo. It
  specifies the model, tissues and conductivities, montage and currents,
  orientation choice, regions of interest, and percentile definitions. Any
  conversion from field projections to local polarization is stated explicitly.
- The Discussion dose-map paragraph and Table 4's independent-amplitude row cite
  the FEM numbers as model evidence. The biological detector test remains a
  proposed experiment; field maps alone do not measure neural focality.
- Further montages or orientation variants go in the supplement.
- The abstract gains at most one clause, only if the ranking change is substantial
  and the complete abstract remains within 300 words.
- The illustrative `(10,1)` versus `(0.5,0.5)` example and line profile stay.
  Relocating the example to the supplement would require Giulio's approval.

If the FEM work arrives after this submission, the existing proposed comparison
can remain and the head-model analysis can form a companion report. The manuscript,
figures, and builds are unchanged by recording this proposal.

## Validation and release status

The JNE article, supplement, fixed-baseline redline, and storyline were rebuilt.
A private TN build checks the updated authors table without replacing the held
archive edition. The article and supplement retain 40 and 21 pages; the redline
and storyline retain 48 and 11 pages. All final logs have zero LaTeX errors,
undefined references, overfull boxes, or duplicate-label warnings. The affected
title and declaration pages were inspected visually.

The abstract remains byte-identical to draft17. The scientific source from the
Introduction through Code and data availability, and the text from the AI
declaration through all appendices, are also byte-identical. All 32 equation
labels and 25 figure labels are retained. Simulation code, caches, figure assets,
references, and the seven pending CUT? passages are unchanged. These checks are
recorded in `draft18_authorship_audit_2026-10-09.json` and `validation_current.json`.

GitHub push, the Calliope/Zenodo cut, Overleaf synchronization, and coauthor
circulation remain on hold. This author update makes no external release.
