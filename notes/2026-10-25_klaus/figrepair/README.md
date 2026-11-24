# Figure repairs for draft24 (candidates)

Klaus, 2026-10-25. Requested by Kaiti (handoff 10:39): bounded repairs of the defects in
`notes/2026-10-25_klaus/figure_check.md` (e9fab55), prepared outside the live tree.
Baseline ac20693 (manuscript 3eceb94). Nothing under `code/`, `figures/` or the
manuscript was modified; the figure scripts are Kaiti's and this folder proposes.

## What is here

- `patches/*.diff`: unified diffs against the live `code/` scripts (apply with
  `git apply notes/2026-10-25_klaus/figrepair/patches/<name>.diff` from the repo root).
- `code/*.py`: the same eleven scripts in full, patched (alternative to the diffs).
- `figures/*.pdf, *.png`: the thirteen candidate figures, generated from the patched
  scripts with the committed data files.
- `diag/`: the S3 upturn diagnostic (script, log, JSON), the PDF text checker with its
  before/after reports and the placed widths, and the S12 overlay test document.

## Method

A staged copy of `code/` (symlinks to every live file, the eleven generators copied)
was run with `TN_FIGDIR` pointing at a scratch folder, in the repository's `.venv`
(Python 3.14.7, numpy 2.4.6, scipy 1.17.1, matplotlib 3.11.0). The unpatched copies
first reproduced all fourteen committed figures pixel for pixel at 60 dpi, so every
difference below comes from the patches. Each candidate was then measured
(`diag/pdf_textcheck.py`: line-level text boxes from PyMuPDF, collisions, clipping,
printed type size at the placed width) and inspected by eye at 110 dpi against its
caption.

## Repairs, by figure file

| file (position) | defect | change | data |
|---|---|---|---|
| fig_feasibility_khz (Fig. 7) | legend crossed by the tau = 15 ms curve | legend removed; each curve labeled along itself (`label_curve`); panel letters through `figstyle.panel`, so "(a)" like every other figure | none |
| fig_curvature_twotone (Fig. 8) | legend on the curve minimum in (a) | legend to the empty upper right | none |
| fig_fem (Fig. 9) | colorbar end labels fuse across the gutters ("0.300.000") | first and last tick label of each bar aligned inward; label pad 1 -> 2 | none |
| fig_mpr_crossover (Fig. 12) | (a) three dashed limits and the Q = 0 curve through the legend; (b) lines through the legend | (a) legend labels shortened to "Q = 0 (F'' > 0)" etc. (the caption already names below/at/above the inflection) and moved to the empty lower-left band; (b) legend to the upper right | none |
| fig_qif_raster_twotone (Fig. 13) | inset tick labels and axis labels on the raster, envelope trace through them | opaque white panel (axes fraction 0.50 to 1.0 by 0.40 to 1.0) behind the inset and its labels, zorder between raster and inset; halos dropped | none |
| fig_qif_regimes (Fig. 14) | same insets; "E rate (Hz)" touching "E neuron #" across the gutter; (d) legend on the red peak | inset fix inherited from `make_qif_figs.beat_inset`; `tight_layout(w_pad=4.5)`; (c,d) legends to the upper left | none |
| fig_qif_timing_twotone (S, qif_timing) | (b) legend over the 105 to 112 Hz lines; (a) legend crossed by the 55 Hz peak | (b) legend to the upper left; (a) legend to center right | none |
| fig_khz_twotone (S, khz_twotone) | ticks print at 5.8 pt, exponents 4.0 pt | canvas 11.0 x 3.9 -> 8.6 x 3.4 in; `scale_text` given the real placed width 0.95 and a 6.6 pt target (it does not see the 0.1 in pad that `bbox="tight"` adds); ticks now print at 6.4 pt | none |
| fig_lanmm_field_p1/p2_twotone (S, lanmm_p1/p2) | all ticks print at 4.0 pt; "1e7"/"1e8" offsets over "a.u." | canvas 11 x 9 -> 9.0 x 7.4 in; `fig.canvas.draw()` before `scale_text` so the tick labels exist when it runs (they were created later and never scaled); decade folded into the colorbar label ("10^7 a.u."); ticks now 6.1 pt | none (values divided by the stated power of ten) |
| fig_khz (S, khz) | legend names compartments; "TMS" marker not in the caption | legend entries now "direct", "assumed fast response, tau = 0.2 ms", "slow somatic membrane, tau_m = 16 ms", the caption's words; marker "3.9k" | none |
| fig_khz_direct (S, khz_direct) | soma curve leaves the 1/f^2 guide above 1.5 kHz and turns up at 4 kHz | settling 6 s -> 12 s (see diagnostic) | yes: soma route above 1 kHz |
| fig_nmm2_jcurve (S, nmm2_jcurve) | "gamma Hopf J*" touching the gray curve | label moved left and down (x = J* - 0.12, y = 0.85 of the gray maximum) | none |

Unchanged by the patches: `fig_demodulation_twotone` (same script as the curvature
figure; its output is pixel-identical and is not shipped here).

## S3 upturn: cause established, not assumed

`diag/khz_direct_upturn_diag.py` reuses the generator's solver and lock-in
(`khz_direct.rhs7/step/lockin_sweep`) with its inputs (eps = 0.5, m = 1, tau_m = 16 ms,
dt = 2e-5 s, 3 s Hann window) on the last four carriers of the grid plus 6 and 8 kHz.
Log: `diag/khz_direct_upturn_diag.log`.

- Field off (eps = 0), 6 s settling: the lock-in at Omega reads 7.73e-6 mV at every
  carrier. Every column starts at Y = 0 and rings down at the autonomous f0 = 10.914 Hz,
  which is the lock-in frequency; this residual is the floor.
- Reference run reproduces the figure: 1.62e-6 at 2.65 kHz (0.23 of the guide),
  4.04e-6 at 4 kHz (1.29 of the guide), 6.8e-6 at 8 kHz. The transient adds to the
  signal with a carrier-dependent phase, so the curve dips below and rises above the
  guide instead of sitting on a flat floor.
- dt halved: the same curve, dip and upturn included, within 0.2% at the weakest
  points. Not a time-step artifact.
- 12 s settling, and separately 6 s of field-off pre-equilibration followed by 6 s with
  the field on (a pre-equilibrated start, not an exact fixed-point initialization):
  the two agree to four digits and sit on the 1/f^2 guide within 0.1% to 4 kHz and
  1.4% at 8 kHz.

The candidate figure doubles the settling time (one constant in `khz_direct.py`).
Changed data: the soma route at 1.17, 1.76, 2.65 and 4 kHz becomes 4.43e-5, 1.95e-5,
8.61e-6 and 3.79e-6 mV (was 3.67e-5, 1.20e-5, 1.62e-6, 4.04e-6); the direct and fast
routes change by less than 0.1%, and the 100 Hz values do not change. No number in the
manuscript quotes these points; `planning/parts/jr_runs.tex` says "other runs use the
windows specified in their scripts", which stays true, and its statement that halving
the step changes lock-in amplitudes by under 1% is confirmed by the diagnostic.

## S12 (fig_lanmm_setup.png): TeX overlay, artwork untouched

The PNG carries "a)" and "b)" where every other figure has bold "(a)". The overlay below
covers the two labels with white boxes and sets the house letters; it needs no package
beyond graphicx and xcolor (the `picture` environment is in the kernel). Tested in
`diag/s12_overlay_test.tex`; the boxes cover the glyphs with margin. Replaces the
`\includegraphics` line in `planning/parts/figure_lanmm_setup.tex`:

```latex
\setlength{\unitlength}{0.85\textwidth}%
\begin{picture}(1,0.8206)% height/width of the PNG (933/1137)
  \put(0,0){\includegraphics[width=\unitlength]{fig_lanmm_setup.png}}
  \put(0,0.788){\colorbox{white}{\makebox[0.045\unitlength][l]{\rule[-0.4ex]{0pt}{2.4ex}\textbf{(a)}}}}
  \put(0,0.371){\colorbox{white}{\makebox[0.045\unitlength][l]{\rule[-0.4ex]{0pt}{2.4ex}\textbf{(b)}}}}
\end{picture}
```

## Integration

1. From the repo root, `git apply` the eleven diffs (or copy `code/*.py` over the live
   scripts). The patch to `khz_direct.py` is the only one that changes data.
2. Regenerate, from `code/` with `../.venv/bin/python`:
   `make_feasibility_fig.py` (3 s), `jr_twotone_figs.py` (40 s; also rewrites
   `fig_demodulation_twotone`, unchanged), `make_fem_fig.py` (4 s),
   `mpr_crossover_fig.py` (3 s), `make_qif_figs.py` (6 s), `make_qif_regimes_fig.py`
   (5 s), `make_khz_twotone_fig.py` (2 s), `make_lanmm_field_figs.py` (4 s; also
   rewrites the `_am` variants, not in the paper), `khz_analysis.py` (4 s),
   `khz_direct.py` (115 s), `make_nmm2_jfig.py` (2 s). Total under four minutes.
   The outputs should equal `figures/` here; or copy `figures/*` directly.
3. Optional: the S12 overlay in `planning/parts/figure_lanmm_setup.tex`.
4. Rebuild (`./build.sh journal`).

## Checks

`diag/textcheck_before.txt` and `textcheck_after.txt` list every figure's printed type
range and residual collisions. After the patches no base type prints below 6.1 pt
(the remaining "TOO SMALL" and "COLLISION" lines are mathtext sub- and superscripts and
fraction numerators inside one label, which the line grouping cannot merge). Every
candidate was viewed at 110 dpi; the flagged regions of the audit are clear, no text is
clipped, panel letters match the captions.

## For the captions (Kaiti's call)

- Fig. 7: "dotted, sealed-cable approximation at 0.2 ms" still matches the figure (label
  "cable, 0.2 ms"); panel letters are now "(a)" as in the caption.
- Fig. 12: the legend no longer says "below/at/above inflection"; the caption does.
- Figs. 13, 14: "Insets" still correct. The white panel hides the upper-right part of
  the "on" rasters (about the last 100 ms for neurons 240 to 400) that the inset body
  already hid in part. If the raster data must stay visible, the alternative is a
  separate fold axes beside each "on" panel; not done, since it changes the layout.
- S, lanmm_p1/p2: colorbars now read "10^7 a.u." / "10^8 a.u."; captions say "arbitrary
  units", consistent.
- S, khz_direct: the soma curve now follows the stated 1/f_c^2 roll-off; `jr_runs.tex`
  could add "12 s of settling for the kHz sweep" if Kaiti wants the window on record.

## Unresolved

- The inset panels of Figs. 13 and 14 hide raster data (above).
- `fig_mpr_crossover` carries one unit-level collision in Kaiti's `overlap.py` output
  ('10^3' x '300'), present before the patch; the two labels belong to different panels
  and do not touch in the render (an off-view tick, a known false-positive class).
- `figstyle.scale_text` is sensitive to call order (tick labels created after the call
  are never scaled) and ignores the 0.1 in pad of `bbox="tight"`; two scripts work
  around it here. A general fix belongs in `figstyle.py`, outside this handoff.

Runtime of this task: baseline reproduction 2.7 min, patched runs 4.5 min, diagnostic
4.5 min (all on the laptop, single process).
