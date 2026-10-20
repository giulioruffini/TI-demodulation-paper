# Ricardo Salvador, points 2 and 3 — email of 2026-10-20 11:01 UTC (13:01 CEST)

Source: Gmail message 1a158f970b3becb8, thread "Re: FEM request: envelope vs quadratic TI dose maps
on a real montage" (thread 1a111f0bee3155d8), to Giulio, addressed "Hi Klaus, Giulio". Attachment
`points_2_3_text.md` (text/markdown; the body below reproduces the drafted text). The JSON
`points_2_3.json` is NOT attached; Ricardo offers to add it to the PR branch next to
`fem_quadmaps.json`. Saved verbatim by Klaus; nothing below is edited.

## Cover note (verbatim)

Hi Klaus, Giulio,

Points 2 and 3 below, with the definitions you asked for. The LaTeX is raw so you can paste it
straight in.

*Point 2 corrects something I got wrong in my last message.* I described the carriers as
"transverse" and implied that matched an AIS detector. Having now derived the laminar direction
with HippUnfold on this subject, the fields sit ~70° from it as well as 58–77° from the long axis —
perpendicular to the long axis is a *plane*, and the carriers lie along the mediolateral axis within
it while the laminar direction lies near the third. So the fields follow *neither* candidate
detector axis. The paragraph states it positively, since it bears directly on the §2.2 text you're
writing.

*Point 3: your instinct to ask for the measurement was right, and it falsified my estimate.* The
conductivity-ratio argument gives 4.5× and 20×, but the measured jumps are 1.13–1.34, a factor of
2.4–16 lower — the fields are largely tangential at both interfaces (normal component a median 20%
on the CSF side) and *n** sits ~64° from the interface normal. The text leads with the measurement
and keeps the estimate as the upper bound it is.

The §2.6 link is also softer than I suggested. Maxima do sit on boundaries, but the beat map does
the same at this resolution and it carries no such restriction, and 95% of brain nodes are within
2 mm of an interface anyway — so I've written "consistent with but does not sharply test" rather
than claiming support.

One practical note for the methods: *Violante's positions cannot coexist with a standard 10–10
cap* — e2 overlaps AF8 and Fp2, e4 overlaps P8 and PO8, with centres 9–19 mm apart at 20 mm
diameter. That's why the Yatsuda rendering is a separate montage rather than a relabelling.

Two small things for the port. I've used \ref where I knew your label and a literal section number
where I didn't — §2.2 is literal, so please substitute. And PC3 is described once as "normal to the
hippocampus's best-fit plane" and once as PC1 × PC2; same thing, but worth settling on one phrasing.

Ricardo

## Drafted text: field orientation (point 2) and interface brightening (point 3)

IXI002, Violante montage, 1:1 (2 + 2 mA). Every number below is in `points_2_3.json`, written by
`tools/quadmaps_orientation_interface.py` in the temporal-interference library; the provenance table
at the end maps each one to its key. LaTeX follows the manuscript's notation ($\mathbf n^*$,
$\mathcal I$).

---

### Point 2 — field orientation and candidate detector axes

We compared the local field directions in the hippocampus with two candidate detector axes: the
long axis and the laminar (somatodendritic) axis. Over the 1{,}568 gray- and white-matter nodes of
the hippocampal ROI, at 1:1 (2 + 2 mA), each carrier field, $\mathbf E_1$ and $\mathbf E_2$, and
the envelope-maximizing direction $\mathbf n^*$ were treated separately. The reference axes are the
principal components of the ROI node coordinates (PC1, the long axis of \S\ref{sec:fem-methods};
PC2, mediolateral; PC3, normal to the hippocampus's best-fit plane) and the laminar direction, the
normalized gradient of HippUnfold's inner--outer Laplace coordinate \cite{dekraker2022}. Angles are
between undirected axes (0--90$^\circ$), given as the median and interquartile range over nodes;
weighting the nodes by field strength changes no median by more than 1.5$^\circ$.

The fields follow neither candidate axis. $\mathbf E_1$, $\mathbf E_2$ and $\mathbf n^*$ lie
71$^\circ$ (63--78$^\circ$), 58$^\circ$ (51--67$^\circ$) and 66$^\circ$ (62--71$^\circ$) from the
long axis, and 69$^\circ$ (53--80$^\circ$), 72$^\circ$ (57--81$^\circ$) and 69$^\circ$
(53--80$^\circ$) from the laminar direction. The directions perpendicular to the long axis form a
plane. Within it the fields lie along PC2, at 25$^\circ$ (17--33$^\circ$), 35$^\circ$
(27--42$^\circ$) and 28$^\circ$ (22--34$^\circ$), whereas the laminar direction lies nearest PC3,
33$^\circ$ (21--54$^\circ$) from it and 76$^\circ$ (55--83$^\circ$) from PC2. The two carriers are
nearly parallel, 14.2$^\circ$ (10.2--18.6$^\circ$) apart. The 10--10 rendering of the montage
(FT7--F8, TP7--P8) gives the same geometry with a smaller separation, 7.5$^\circ$
(4.2--11.4$^\circ$): 71$^\circ$, 77$^\circ$ and 75$^\circ$ from the long axis, and 74$^\circ$ from
the laminar direction for all three. That rendering is needed because the published positions
cannot coexist with a standard 64-position cap: e2 overlaps AF8 and Fp2, and e4 overlaps P8 and
PO8, with centres 9--19~mm apart for 20-mm discs, so the montage cannot be placed on a standard
array without substitution.

This bears directly on the laminar hypothesis of \S2.2. A cell aligned with the laminar direction
receives $|\cos\theta|\approx0.31$--$0.36$ of each carrier (medians 0.36 for $\mathbf E_1$, 0.31 for
$\mathbf E_2$). The envelope excursion is linear in the projected fields and the quadratic
excursion bilinear, so such a cell sees roughly a third of the envelope and a ninth
($0.31\times0.36\approx0.11$) of the beat available to an optimally oriented one. Measured node by
node against each map's maximum over orientation, the fractions are 0.29 (0.11--0.57) for the
envelope excursion, 0.11 (0.02--0.34) for the quadratic excursion and 0.12 (0.04--0.33) for
$\mathcal I$; for the 10--10 rendering, 0.25, 0.07 and 0.08.

Two qualifications apply. The laminar direction is a field rather than an axis: it follows the
curvature of the hippocampal cortex, spreading a median 31$^\circ$ (23--51$^\circ$) about its own
principal axis, so no spatially uniform field can be aligned with all of it. And it is defined at
only 934 of the 1{,}568 ROI nodes (59.6\%). Restricted to the 565 interior nodes, whose voxel and
six neighbours lie inside the Laplace domain, the angles to $\mathbf E_1$, $\mathbf E_2$ and
$\mathbf n^*$ are 71$^\circ$, 74$^\circ$ and 71$^\circ$, and the envelope and beat fractions 0.25
and 0.08.

*Reference to add:* DeKraker J, Haast RAM, Yousif MD, et al. (2022) Automated hippocampal unfolding
for morphometry and subfield segmentation with HippUnfold. *eLife* 11:e77945.
doi:10.7554/eLife.77945

---

### Point 3 — fields at tissue interfaces

Current continuity across a conductivity interface makes the normal field component larger on the
less conductive side by the conductivity ratio: $\sigma_{\rm CSF}/\sigma_{\rm GM}=4.5$ at the
CSF/gray-matter interface and $\sigma_{\rm GM}/\sigma_{\rm WM}=2.67$ at the gray/white interface,
or 20 and 7.1 for maps that are second order in the field. These ratios bound the brightening of a
map from above. The tangential component is continuous, and the maps project the field on
$\mathbf n^*$ rather than on the interface normal. We therefore measured each map's jump directly,
as its ratio across the interface at the same node and along the same $\mathbf n^*$, from the
element fields on the two sides (Violante montage, 1:1). Interfaces are the faces shared by
tetrahedra of different tissue tags in the head mesh (median interface edge 1.5~mm); this
segmentation has no white-matter/CSF faces.

| interface | estimate, first / second order | envelope excursion | quadratic excursion | $\mathcal I$ |
|---|---|---|---|---|
| CSF $\to$ gray matter (120,892 nodes) | 4.5 / 20 | 1.17 (1.04–1.53) | 1.28 (1.06–2.07) | 1.25 (1.04–1.97) |
| gray $\to$ white matter (126,426 nodes) | 2.67 / 7.1 | 1.13 (1.03–1.38) | 1.33 (1.08–2.01) | 1.34 (1.08–2.05) |

The measured jumps are a factor of 2.4--16 below the estimates, and the difference is geometric.
The fields are largely tangential at both interfaces: the normal component is a median 20\% of the
field magnitude on the CSF side and 46\% on the gray-matter side, and $\mathbf n^*$ lies a median
64$^\circ$ and 63$^\circ$ from the interface normal. Applying the jump condition to the local field
and normal at each node predicts medians of 1.26--1.80; the remaining difference from the
measurement is not resolved at this mesh resolution.

There is no brightening near the CSF. In gray matter, the 99th percentile within 2~mm of the CSF
interface is 0.90 (envelope excursion), 0.86 (quadratic excursion) and 0.93 ($\mathcal I$) times
that further in, so the tail is, if anything, slightly dimmer next to the CSF. It sits instead on
the white-matter side of the gray/white interface. Of each map's top 1\% of nodes, 67--73\% are
white matter and 81--82\% lie within 2~mm of the gray/white interface, against 73\% of all nodes;
only 24--31\% lie within 2~mm of CSF, against 48\%. Distances are Euclidean, to the nearest
interface vertex or face centroid.

*Suggested caption line (Fig. 8):* No map brightens next to the CSF (gray-matter p99 within 2~mm
of the CSF interface is 0.86--0.93 times that further in); the upper tail lies on the white-matter
side of the gray/white interface.

These observations are consistent with the boundary restriction of \S\ref{sec:dc} but do not test it
sharply at this resolution. Along a spatially fixed direction, 98\% of the strict local maxima of
$\mathcal I$ in gray matter and 96.5\% in white matter lie on a compartment boundary, against 90\%
and 73\% of nodes. The quadratic excursion, which carries no such restriction, behaves the same way
(97.9\% and 96.1\%), and the remaining 2--3.5\% interior maxima of $\mathcal I$ are at the level of
the field-recovery noise. With 95\% of all gray- and white-matter nodes within 2~mm of an
interface, a near-interface criterion cannot by itself separate the mean maps from the beat.

---

### Definitions, as requested

- **Vectors:** $\mathbf E_1$ (e1–e2) and $\mathbf E_2$ (e3–e4), each pair's field at 2 mA; $\mathbf n^*$,
  the 1:1 envelope-maximizing direction (closed form), the direction Fig. 8 holds fixed. Reported
  separately, never pooled.
- **Axes:** PC1/PC2/PC3 of the ROI node coordinates. PC1 is the methods' long axis, anterior positive;
  PC2 is lateral-positive; PC3 = PC1 × PC2. The laminar direction is HippUnfold's IO Laplace
  gradient, sampled at the nearest voxel, with no smoothing.
- **ROI and condition:** 1,568 GM + WM nodes inside the FreeSurfer aseg left hippocampus (label 17);
  laminar defined at 934, interior at 565; 1:1 = 2 + 2 mA.
- **Weighting:** per node. The field-weighted alternative (weights $|\mathbf E_1|$, $|\mathbf E_2|$, or
  the 1:1 envelope TImax for $\mathbf n^*$) changes no median by more than 1.5°, so only the per-node
  values appear in the text.
- **Interfaces (point 3):** faces shared by tetrahedra of different tissue tags in the head mesh
  (headreco six-tissue segmentation, linear tetrahedra; median CSF/GM interface edge 1.51 mm, IQR
  1.37–1.66). Pairs present: CSF/GM (241,780 faces) and GM/WM (253,608); WM/CSF none.
- **Distance:** Euclidean, from each node to the nearest interface vertex or face centroid; "near" means
  ≤ 2 mm. It is resolved to about half an interface edge.
- **Jump:** at each interface node, the mean element field over the adjacent tetrahedra on each side
  (from the stored node potentials), projected on the GM row's $\mathbf n^*$. The prediction applies
  $\mathbf E_{\rm low}=\mathbf E_{\rm high}+(r-1)(\mathbf E_{\rm high}\cdot\boldsymbol\nu)\boldsymbol\nu$
  with the local area-weighted normal $\boldsymbol\nu$. A check from the two SPR rows at shared GM/WM
  nodes gives 1.08 / 1.22 / 1.24.

*Provenance.* Every number above comes from points_2_3.json, written by
tools/quadmaps_orientation_interface.py. The full table maps each value to its key and also covers
quantities not quoted here — attached, and I'm happy to add the JSON to the PR branch alongside
fem_quadmaps.json if you'd rather have it in the repository. The headline keys:

| quantity | key |
|---|---|
| orientation angles, per montage | point2_orientation.montages.<montage>.vs_PC_axes_deg, .vs_laminar_deg |
| laminar-aligned fractions | point2_orientation.montages.<montage>.laminar_aligned_cell |
| laminar spread and coverage | point2_orientation.laminar_rotation, .laminar_coverage |
| cap overlap | point2_cap_overlap.electrodes |
| interface jumps | point3_interfaces.jump_across_interface |
| near/far p99 | point3_interfaces.near_far_p99 |
| top-percentile locations | point3_interfaces.top_percentile_near_interface |
| boundary maxima | point3_interfaces.local_maxima_on_boundary |
