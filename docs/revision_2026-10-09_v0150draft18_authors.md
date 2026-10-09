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

## Placement options for the FEM result

These are proposals for Giulio to decide once the data and their scope are known.
The scientific argument has not been reordered or expanded in draft18.

- Theory Sections 2.5 and 2.6, beside Table 2, retain the definitions of the
  envelope excursion, quadratic excursion, and quadratic mean. They can refer
  forward to the FEM comparison without repeating its methods or numerical results.
- Methods can add a short head-modeling subsection specifying the head model,
  montage and carrier currents, field-to-polarization assumptions, projection
  directions, target and cortical masks, and the target-to-cortex statistic.
- Results can add one subsection immediately before the Discussion, with a
  single figure comparing the three spatial maps and their target-to-cortex
  ratios. Detailed slices or montage sensitivity can go in the supplement.
- Discussion and Table 4 can identify what the FEM result tests about the spatial
  maps. A field calculation alone does not test the biological detector or measure
  neural focality. Any abstract or Conclusion change should follow the result.

If the FEM work arrives after this submission, the existing proposed comparison
can remain and the head-model analysis can form a companion report. The pending
placement proposal announced by `giulio-shell` is not presumed approved here.

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
