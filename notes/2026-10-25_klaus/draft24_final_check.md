# Draft24 integration (4a14d00): final bounded check

Klaus, 2026-10-25. Requested by Kaiti (handoff 11:19). Scope: the main-text changes
cbe5b7b..4a14d00, the thirteen repaired figures and their captions in the built article
and supplement, the schematic overlay, and the diagnostic wording in my own README.
No live file edited; nothing pushed.

## Prose corrections

All three corrections and all restorations of `draft24_prose_fidelity.md` are applied
as proposed or better: the cable comparison now points to Fig. feasibility(a) with the
point-membrane cases in Fig. khz; the kHz closed-loop sentence reads "consequences of
the assumed access time and coupling; neither is calibrated by the simulation"; the
Brunel citation is attached to circuit resonance alone and the fast-membrane statement
stands on its own. The J-curve inference, the weak-drive scope, the envelope-following
assumption, the negative curvature at the pinned state, the static-detector point in
the coupling section (now with a pointer to the dynamic section), the purpose of the
spiking run and the PEIX motivation are back; the undefined T(A), the ambiguous "Its",
the imperative "Compare", the repeated bisection sentence and the two blank lines
before displays are gone. "The population equations" for Eq. mpr is right, since the
input may include recurrence. Nothing else in the main text changed.

## Figures and captions

Every repaired figure was rendered at 110 dpi and measured again at its placed width:
base type is 6.1 pt or larger in all thirteen, 6.4 pt in the two QIF figures; no
collision outside mathtext scripts; no clipped text. Pages 19, 24, 25 and 26 of the
article and 7, 23 and 24 of the supplement were viewed as built.

- Figs. 13 and 14 (qif_raster, qif_regimes): the phase folds now have their own axes
  (right column; middle row), so the rasters are complete and the fold labels sit on
  white. The diff of `make_qif_figs.py` touches only the axes target and a tick size;
  `cycle_avg`, the smoothing, the normalization and the spectra are unchanged, as
  Kaiti's AST comparison says. Captions updated to "Right-hand panels" and "Panels
  below the rasters"; "scale 0--2" still matches the fold axes. Cosmetic only: the
  fold axes keep the bold tick and axis labels of the inset version, which no other
  panel in the set uses; regular weight would match, and nothing depends on it.
- Laminar maps (lanmm_field_p1/p2): 9.0 x 7.4 in with tight layout, ticks at 6.1 pt,
  colorbar labels "alpha power change (10^7 a.u.)"; the captions define the observable
  and the arbitrary units. Clean on the page at 0.86 text width.
- Feasibility: panel (c) has headroom for its legend (ylim to 100); curve labels and
  house panel letters as in the candidate.
- QIF timing: short legends ("QIF", "mean field"; "TI off/on") clear of peaks and bars.
- Crossover: "F''(Q)/4 (static)" annotation and the short Q legend; clean.
- Curvature, FEM, kHz two-tone, kHz access, kHz direct, NMM2 J-curve: as in the
  candidates; kHz direct's slow-access curve lies on the 1/f_c^2 guide on page 7, and
  `jr_runs.tex` now states the 12 s settling and 3 s window.
- Schematic (fig_lanmm_setup): the TeX overlay places bold "(a)" and "(b)" over the
  drawn letters on supplement page 24; the artwork is untouched.

## Diagnostic wording corrected on my side

Kaiti's two precision points are right and are now in `figrepair/README.md` and the
diagnostic's docstring: run E is six seconds of field-off pre-equilibration followed by
six seconds with the field on, not an exact fixed-point initialization; halving the
time step reproduces the dip and upturn within 0.2% at the weakest points, not to four
digits. The conclusion is unchanged: the upturn is the start-up transient at f0, and
12 s of settling removes it.

## Verdict

Nothing blocks closing draft24 on this check. Open items are Kaiti's (final page
inspection, delivery record) and Giulio's (reading, release decision).
