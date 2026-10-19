# FEM abstract and physiological steady source — 19 October 2026

Giulio approved the FEM abstract sentence and asked that the Discussion connect
mean-square polarization to its physiological prediction (Klaus’s relay at
20:07 CEST; proposal `1c31a13`). The source remains draft20. The redline baseline
remains draft13, `c620335`.

The approved sentence is reproduced verbatim in the shared abstract. Its final
length is 299 words by texcount, after expansion of the four macros without
headings. The pinned Jansen–Rit operating-point condition and the oscillation
threshold remain. Compensating edits shorten the opening and model statement,
omit the abstract’s nodal/AIS detail (retained in the body), shorten the membrane
frequency clause, and shorten the equal-power carrier clause. No body explanation
or result is cut. The storyline uses the same abstract and records the new
physiological interpretation.

The Discussion now states the static second-order source explicitly:
Y_DC = sigma''(v*) I / 2. The FEM regional mean ratio transfers to its source
magnitude when curvature is spatially uniform and fixed. Fixed heterogeneous
curvature alone is insufficient: the curvature-weighted regional average can
have a different ratio. Recurrence determines the eventual rate response.
The figure caption now connects the geometric map to that signed source.

Recomputed directly from `code/fem_quadmaps.npz`, at shares 0.75 versus 0.50:

| Hippocampal map mean | Ratio |
|---|---:|
| Envelope excursion | 0.5531852843 |
| Projected quadratic beat | 0.7500000000 |
| Mean-square polarization | 1.2441283336 |
| Isotropic quadratic beat | 0.7500000000 |

The beat’s own weak rectified mean scales as 0.75 squared = 0.5625 at fixed
state. The larger mean-square source is consistent with greater BOLD reduction
conditional on a suppressive source and an order-preserving readout. The text
states the low-pass argument for a slow, approximately linear hemodynamic
readout, without claiming a calibrated BOLD sensitivity or identifying BOLD
with firing rate. Local envelope increases, a thresholded envelope response,
the nonsignificant 1:1–sham contrast, curvature heterogeneity, recurrence, and
the missing neural/hemodynamic readout model remain explicit. Existing empirical
statistics and the two discriminating measurements are retained.

The Violante passage grows from 295 to 492 words by texcount; the added
physiological inference and its conditions occupy two paragraphs. No numerical
producer, cache, figure image, or bibliography entry changes. Article, redline,
and storyline build to 47, 55, and 13 pages. Logs have no errors, undefined
references, overfull boxes, duplicate labels, or outstanding rerun requests.
Article pages 1, 27, and 34 and redline page 41 were inspected. The supplement
is unchanged at 21 pages. Klaus’s bounded fidelity check of this revision is
pending. The private mirror still contains the preceding FEM integration;
public-release holds are unchanged.
