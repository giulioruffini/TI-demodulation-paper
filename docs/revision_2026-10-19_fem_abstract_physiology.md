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


## Encoding-stage readout clarification

Klaus’s 20:09 CEST message specifies the experimental readout. Checked against
the published PDF (article page 1995 and reporting-summary design specification):
TI was confined to the 32 s encoding stage of each task block, with ramping at
the ends. The Discussion now describes the contrast as encoding-evoked BOLD
and the steady source as a slow shift during that window, which can add to the
evoked response or alter its operating point. The low-pass comparison is with
the 5 Hz beat. This is a local scope clarification; the 299-word abstract,
figures, numerical outputs, and reported statistics are unchanged.
Source: https://synthneuro.org/wp-content/uploads/2023/12/2310violanteFULL.pdf

After this clarification the passage is 525 words. The article remains
47 pages and the redline 55, with clean final logs; article pages 33–34
were inspected. The abstract remains 299 words.


## Fidelity pass and exact envelope threshold

Klaus reported PASS on `111f7ab` at 20:13 CEST: the approved abstract sentence,
retained scope conditions, all four regional ratios, the squared-beat factor,
and the physiological qualifications match the sources. His plain abstract
count is 297; texcount gives 299. The encoding clarification in `c632c7e` was
sent separately and is not covered by that verdict.

His optional threshold precision is adopted. For r = |P1|/|P2|, the envelope
excursion ratio is min(r, 3) / [2 min(r, 1)]. It is 0.5 for r at most 1,
r/2 between 1 and 3, and 1.5 from 3 onward. It therefore exceeds one only for
r > 2 and reaches 1.5 at r >= 3. The revised sentence states both thresholds.
This does not change any FEM value or interpretation.

Final threshold wording: 524 words in the full Violante passage; article and
redline remain 47 and 55 pages, with clean logs. Article page 34 checked.
