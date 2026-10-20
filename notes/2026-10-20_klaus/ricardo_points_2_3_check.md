# Check of Ricardo's points 2 and 3 (email of 2026-10-20 13:01 CEST) — Klaus, for Kaiti

Base: 9181d2d. Source text, verbatim: `ricardo_points_2_3_email.md` in this folder. Read-only on all
sources. The JSON (`points_2_3.json`) and the script (`tools/quadmaps_orientation_interface.py`) are
not in the repository; the numbers below could only be checked for internal consistency and against
the manuscript, not recomputed.

## Verdict

The numbers are internally consistent, nothing in the manuscript contradicts them, and nothing has to
be retracted: the tex never said "transverse", "mediolateral", or 4.5x/20x (grep on 9181d2d). Both
points enter as new text. Three items go back to Ricardo (JSON and script into the repository,
HippUnfold version, confirmation of the effective-jump reading); the DeKraker reference we add.

## Arithmetic and consistency

| claim | check |
|---|---|
| sigma_CSF/sigma_GM = 4.5, squared 20 | 1.79/0.40 = 4.48; 20.0 |
| sigma_GM/sigma_WM = 2.67, squared 7.1 | 0.40/0.15 = 2.67; 7.1 |
| measured jumps 2.4–16 below the estimates | 2.67/1.13 = 2.36; 20/1.25 = 16.0; others 3.8, 15.6, 5.3, 5.3 |
| laminar-aligned cell receives 0.36 / 0.31 of E1 / E2 | cos 69° = 0.358; cos 72° = 0.309 |
| a ninth of the beat | 0.31 × 0.36 = 0.11 |
| laminar defined at 934 of 1,568 nodes (59.6%) | 934/1568 = 59.57% |
| earlier email: 58–77°, 21–35°, 7–14° | now per montage: 58/71/77°, 25/35/28°, 7.5/14.2°; consistent |
| ROI = 1,568 GM+WM nodes | manuscript l.1239, same |
| long axis = first principal axis of ROI nodes | manuscript l.1261, same |
| e2 near AF8/Fp2, e4 near P8/PO8 | manuscript l.1183–1185 places them 10 mm from AF8 toward Fp2 and 10 mm from P8 toward PO8; the cap-overlap sentence is consistent and explains why the Yatsuda rendering is a separate mesh (l.1191 already says each montage carries only its own four electrodes) |
| dekraker2022 | absent from references.bib; add (eLife 11:e77945, doi 10.7554/eLife.77945) |

## One physics observation

With a median normal fraction of 20% on the CSF side and 46% on the gray-matter side, and a continuous
tangential component, the effective normal-component jump at the median node is about 2.5, not 4.5:
solve 0.46 = j·0.20 / sqrt(0.98² + (j·0.20)²), which gives j ≈ 2.5. The one-sided element averages on a
1.5 mm linear-tetrahedra mesh realize about half the conductivity jump. So the measured map jumps
(1.13–1.34) are a resolution-limited lower bound, the conductivity ratios (4.5/20, 2.67/7.1) the upper
bound, and Ricardo's per-node prediction (1.26–1.80) lies between. His "not resolved at this mesh
resolution" is the same point, less explicit; one sentence saying so would make the table honest in
both directions. The Gmail draft asks him to confirm.

## Integration suggestions (Kaiti's call)

1. **sec:fem-methods.** Axes: PC1 the long axis, anterior positive; PC2 lateral positive; PC3 = PC1 × PC2,
   the normal to the best-fit plane of the ROI nodes (one phrasing). Laminar direction: HippUnfold
   inner–outer Laplace gradient at the nearest voxel, no smoothing; version and command needed from
   Ricardo; defined at 934 nodes, interior 565. Interfaces: faces shared by tetrahedra of different
   tissue tags; no WM/CSF faces; median CSF/GM edge 1.51 mm; "near" = within 2 mm, Euclidean, to the
   nearest interface vertex or face centroid; jump = ratio of one-sided mean element fields projected on
   the GM row's n*.
2. **sec:fem-results.** Two paragraphs as drafted (orientation; interfaces). `\S2.2` is literal in his
   text: substitute `\S\ref{sec:coupling}`.
3. **Fig. 8 caption.** His line: no map brightens next to the CSF (gray-matter p99 within 2 mm of the CSF
   interface is 0.86–0.93 times that further in); the upper tail lies on the white-matter side of the
   gray/white interface.
4. **sec:coupling (l.439–447) or Discussion.** One sentence: on IXI002 the fields follow neither candidate
   axis, so a laminar-aligned detector sees about a third of the envelope and a ninth of the beat that
   the envelope-maximizing direction reports (sec:fem-results); the fixed n* is an upper bound for that
   hypothesis.
5. **Discussion l.2104–2105** ("Both idealized mean maps obey the boundary-maximum restriction of
   sec:dc; the beat map does not."): add that the IXI002 maxima are consistent with but do not test this
   sharply, since 95% of nodes lie within 2 mm of an interface and the beat map's maxima also sit on
   boundaries at this resolution.
6. **Provenance sentence l.1273–1275** ("code/fem_quadmaps.py computes every map and number in
   sec:fem-results") becomes false once points 2 and 3 are in sec:fem-results unless
   `points_2_3.json` and the script join `code/`, or the sentence is qualified. The Gmail draft asks
   Ricardo to add both to the PR branch.
7. **CRediT** unchanged (methodology, software, formal analysis, data curation, visualization already
   listed).
