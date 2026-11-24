# TN0484 main-results presentation

The six-slide overview is the short version for a roughly five-minute talk:
[PDF](../output/pdf/TN0484_short_results.pdf) and
[editable Beamer source](tn0484_short_results.tex). Build it from the repository
root with `sh presentations/build_short_results.sh`.

It combines the receiver framework and source laws on the first slide, then
uses enlarged figure excerpts for spatial maps, recurrent gain, the dynamic
sign change, the equal-RMS carrier control, and carrier access. There are no
numerical tables or backup slides. The carrier-control legend is restored
outside its cropped panel; the gain and response-amplitude plots are labeled
separately. The figure data are unchanged. Builds and all six rendered pages
are checked; figure and scientific scopes are reviewed independently.

The short deck uses `fig_fem` (a–c), `fig_jcurve` (c), `fig_tacs_jcurve` (b),
`fig_mpr_crossover` (a), `fig_qif_regimes` (d), and `fig_feasibility_khz` (a).
Its main-body text carries each finding; brief captions identify the models
and assumptions. The full presentation below retains the supporting numbers.

## Detailed presentation

The Beamer deck contains eleven main slides and two backup slides for a roughly
12-minute scientific presentation. It uses draft28, which integrates the verified November 6 FEM outputs from
Ricardo's PR #2 (`6ade413`). The scientific editing baseline is draft27
(`146679e`); the new source and field outputs are traced in the revision record.

Build from the repository root:

```sh
sh presentations/build_main_results.sh
```

Editable source: [tn0484_main_results.tex](tn0484_main_results.tex).
Output: [presentation PDF](../output/pdf/TN0484_main_results.pdf).
LaTeX logs and review renders are kept in `build/main_results/`.
The build uses the repository's existing vector figures; it does not run
simulations or rebuild the paper.

## Source and scope

The static formulas use the local weak-field expansion of the rate curve.
The tDCS/tACS comparison matches each TI carrier to the direct polarization
amplitude, before feedback. The kHz budget is conditional on assumed access
and coupling. The dynamic sign result belongs to weak local QIF rectification
at fixed synaptic input. Equal-RMS controls are mean-field results in model
current units; finite-network modulation depth remains unconverged.

Figure excerpts preserve their original data and axes:

| Slide | Source |
|---|---|
| 4 | `figures/fig_fem.pdf`, panels (a-c), both current ratios and color scales |
| 6 | `figures/fig_jcurve.pdf`, panel (c), AM surrogate |
| 7 | `figures/fig_mpr_crossover.pdf`, panel (a) |
| 9 | `figures/fig_feasibility_khz.pdf`, panel (c) |
| 10 | `figures/fig_qif_regimes.pdf`, panels (c,d), mean-field controls |

The new contrasts and node fractions are traced in
[`ricardo_email_assessment.md`](../notes/2026-11-07_kaiti/ricardo_email_assessment.md)
and the adjacent `ricardo_verified_values.json`. Slide 5's node fractions use
the baseline GM+WM ROI, explicitly distinguished from its GM-only contrast
table. The proposed FreeSurfer data export has not been received or validated.

This is an internal working presentation. The existing publication and
circulation holds remain in force.

The MRI backdrop in slide 4 is from the IXI dataset (CC BY-SA 3.0), as
acknowledged in the article. Figure panels retain their original axes and data.
