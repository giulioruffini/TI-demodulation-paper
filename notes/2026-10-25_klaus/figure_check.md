# Figure check, draft23 (3eceb94)

Klaus, 2026-10-25. Requested by K: "check the figures for text overlaps and such."

## Method

All 27 figure files included by the article (`TN0484_jne.log`, 14 figures) and the
supplement (`TN0484_jne_supplement.log`, 13 figures) were checked three ways.
A script extracted every text span from each PDF with PyMuPDF, shrank the boxes
to ink height, and reported pairwise overlaps, text outside the page box, and
printed type size (span size times the placed width over the figure width;
text width 464.9 pt). Every figure was then rendered at 70 dpi and viewed,
and each flagged region was re-rendered at 150 dpi. Captions were read against
the drawn elements and panel letters. The scratch files are in the session
scratchpad (`figchk/`); the report was not kept because the eye check supersedes
it.

No text is clipped at a page edge in any figure. Panel letters match the
captions in all 27 figures, and every drawn guide, band, contour and marker is
named in its caption except the two items under "wording" below.

## Defects confirmed by eye

Figure numbers follow the article build order (Fig. 1 concept ... Fig. 14
QIF regimes) and the supplement order (S1 kHz access ... S13 LaNMM P1).

**Legend drawn over data.**

- Fig. 7(a), `fig_feasibility_khz`: the tau = 15 ms curve runs through the
  legend block at lower left. The four curves are a decade apart at 10 kHz, so
  labels at the right ends replace the legend.
- Fig. 8(a), `fig_curvature_twotone`: the two-entry legend sits on the minimum
  of the curve (v* = 7.5 to 9.5 mV). Upper right is empty.
- Fig. 12(a), `fig_mpr_crossover`: the three dashed fast-carrier limits and the
  solid Q = 0 curve cross the legend text at upper right. The curves are
  separated at the left edge (0.014, 0, -0.003), so short labels at the left
  ends replace the legend.
- Fig. 12(b): the four error lines pass through the legend text at lower left.
  Upper right is empty.
- S10(b), `fig_qif_timing_twotone`: the 105 to 112 Hz lines pass through
  "TI off" and "TI on" at lower right. Upper left is empty.

**Inset labels drawn over data.** Fig. 13(b,d) and Fig. 14(a,b): the inset tick
labels and the "Delta f phase (cycles)" label are drawn on the raster, and the
red envelope crosses them. The inset body also hides the last 100 ms of the
raster. A padded opaque background behind the inset and its labels fixes the
legibility; moving the insets above the panels also restores the data.

**Colorbar tick labels fused.** Fig. 9, `fig_fem`: at the three colorbar
junctions the end label of one bar abuts the first label of the next and reads
as one number ("0.300.000", "0.0500.000", "0.0300.000"). Three ticks per bar, or
the first label suppressed, or the bars shortened, resolves it.

**Type below 6 pt at print size.**

- S11 and S13, `fig_lanmm_field_p2_twotone` and `_p1_twotone`: every tick label
  prints at 4.0 pt (800 pt wide figure placed at 0.86 text width; 76 spans per
  figure). Tick font times 1.6, or the figure at full width.
- S2, `fig_khz_twotone`: tick labels print at 5.8 pt and exponents at 4.0 pt
  (798 pt wide at 0.95 text width). One size step up.
- Sub- and superscripts flagged at 4.2 to 5.5 pt elsewhere are mathtext scripts
  of 6 to 8 pt base text and are acceptable.

## Wording and consistency, not overlaps

- S1, `fig_khz`: the legend names compartments ("axon / AIS / node", "soma /
  dendrite") while the caption and the text now call the access times
  assumptions, not compartments. Rename to "fast access, tau = 0.2 ms" and
  "slow access, tau_m = 16 ms". The "TMS 3.9k" marker is not explained in the
  caption; name it or drop it.
- S3(a), `fig_khz_direct`: the slow-access curve turns up at its last point
  (4 kHz, 1.7e-6 to 4e-6) against the 1/f^2 guide. If it is a resolution floor,
  say so in the caption or drop the point.
- S8(a), `fig_nmm2_jcurve`: the "gamma Hopf J*" label touches the gray
  linear-response curve. Shift it left.
- Fig. 14(a) and (b): the right-axis label "E rate (Hz)" and the left label
  "E neuron #" of the next panel touch. A wider gutter.
- S12, `fig_lanmm_setup`: panel letters "a)" and "b)" differ from "(a)" in
  every other figure. The PNG is the only non-vector figure.
- S11 and S13: the colorbars carry "1e7" and "1e8" offsets over "a.u." labels.
  Folding the power into the label reads better.

## Clean

Figs. 1, 2, 3, 4, 5, 6, 10, 11; S4, S5, S6, S7, S9. Fig. 2 (`fig_models_ti`)
was checked at 150 dpi because its base text prints at 7.3 pt with 5.5 pt
scripts; nothing overlaps.

## Ownership

The figure scripts are Kaiti's (`code/`). This note proposes; it edits nothing.
