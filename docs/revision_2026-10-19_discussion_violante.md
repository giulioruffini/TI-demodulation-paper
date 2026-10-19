# Current-ratio evidence and detector predictions

Giulio requested a plain-logic Discussion through Klaus's October 19, 18:31
message. The proposal is committed in `c97746e`, in
`notes/2026-10-19_klaus/discussion_violante_rewrite.md`. The revision replaces
the existing current-ratio paragraph with two paragraphs: the measured
physiological effects, followed by the geometric predictions and what would
distinguish their neural consequences. The working edition remains draft20.

The experimental statistics and voxel fractions were checked against the
[published article and supplement](https://synthneuro.org/wp-content/uploads/2023/12/2310violanteFULL.pdf),
especially article page 1998 and Figure 3. The current conditions and geometric
steering are described on pages 1995 and 1997. The citation remains
`violante2023`. The FEM mean-square factor and focus displacements were
recomputed from `code/fem_quadmaps.npz`; no simulation was rerun.

The ratio formula implies an increase in mean-square polarization precisely
where `5 P_2^2 > 3 P_1^2`, giving the threshold `sqrt(3/5) = 0.7745966692`.
The new text uses the exact threshold and an explicit approximation, replacing
the previous example restricted to equal per-current polarizations.

The proposal required several scope refinements. A change in each geometric
map does not guarantee a BOLD change under every physiological model. A
posterior mean-square focus does not imply a posterior beat focus, nor does a
larger nonnegative mean-square map establish excitation. Detector curvature
and recurrence remain necessary to obtain a signed physiological response.
Thresholded BOLD voxels also cannot be compared directly with the geometric
maps without a neural and hemodynamic readout model. The revised ending pairs
a spatially resolved beat measurement with an equal-power carrier control,
under the paper's existing second-order matching conditions.

The previous direct contrast, region interaction, functional-connectivity
qualification, ratio formula, RMS mismatch, geometric displacements, and
controlled-state test are retained. The storyline changes its remaining
generic “DC map” wording here to “mean-square map.” No figure, numerical
output, equation label, or scientific result is removed.

The abstract is held at Giulio's request. Before a FEM sentence is added, its
“steady-source foci” should become “mean-square foci,” and the proposed cut
of the pinned JR operating-point condition should be avoided: independence
of gain and detection was established with that condition. The FEM sentence
and compensating cuts remain for Giulio's decision.

The passage grows from 195 to 295 words by texcount. The article, fixed-draft13
redline, and storyline build to 46, 55, and 13 pages, with no errors, undefined
references, overfull boxes, duplicate labels, or outstanding rerun requests.
Article pages 33--34 and redline page 41 were inspected. The abstract is
byte-identical to the preceding version; the supplement and numerical files
are unchanged. Klaus accepted the scope correction in `fa21fa1`; the final
committed wording will receive a bounded read-only check.
