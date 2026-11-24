# Approved figure-label repairs

The five approved figures were regenerated, checked, and installed in `figures/`. The generator changes affect labels and coupling-value formatting only. No model equations, input parameters, plotted arrays, axis limits, or layout calls were changed. The source changes are relative to `0f9ecca`.

| Figure | Installed change | Minimum drawn text at 465.1 pt width | Visible overlap findings |
|---|---|---:|---:|
| 1, `fig_concept` | “Local polarization” and `s(t)` replace “AM field”. | 6.20 pt | 0 |
| 4, `fig_demodulation_twotone` | “Polarization s (mV)” replaces “field (mV)”. | 6.20 pt | 0 |
| 8, `fig_curvature_twotone` | Panels b/d identify polarization amplitude. | 6.20 pt | 0 |
| 10, `fig_jcurve` | The last legend entry shows the actual C=135.8 instead of rounding to 136. | 6.27 pt | 0 |
| 11, `fig_nmm2_resonance_twotone` | The ordinate identifies excitatory-rate amplitude in ms⁻¹. | 6.20 pt | 0 |

The `figcheck` skill was applied. Every repaired PDF was rendered individually at its manuscript width and viewed. Labels fit, panel letters remain intact, and no visible text overlaps or clipping were found. No manual layout adjustment was needed. The repository overlap checker initially reported hidden ticks on the axis-free concept diagram and log ticks outside displayed limits; `verify_labels.py` excludes precisely those undrawn tick objects before repeating the same bounding-box check. The raw reports are retained alongside that check.

Numerical preservation was checked against a render of the unchanged `0f9ecca` generator source. All 76 plotted data arrays and bar/patch geometry arrays are exactly equal between baseline and repaired renders. The concept and coupling figures used existing caches. The JR two-tone and PING two-tone generators have no historical numerical cache; their unchanged deterministic calculations ran once into this scratch directory, and both generator versions reused the identical saved return values. Existing `code/` data caches were not modified. All reported JR and PING numerical summaries agree with the existing captions, including slope 1.99, the 634-fold tangent control, PING peaks 0.0014/0.0030/0.0055 ms⁻¹, and autonomous-regime peaks at 56/65/83 Hz.

The baseline rerenders are not pixel-identical to the preexisting PNGs even without these label edits; their canvas dimensions differ by at most 14 pixels. The current rendering environment therefore produces small typographic/padding differences. The exact-data comparison is against the baseline source, not a claim of pixel identity with the historical rasters. The original PDF/PNG files are retained in `original_files/`. Installed files were hash-checked against `verification.json`.

## Caption facts for the root editor

- Figure 1 starts with local polarization after access; the diagram's topology is unchanged.
- Figure 4 uses genuine equal tones, ε=1 mV per tone, fc=100 Hz, beat 11.1 Hz, p=330 s⁻¹, C=135; settling 10 s, measurement 3 s, dt=0.2 ms.
- Figure 8a uses genuine tones with ε=0.3 mV per tone, fc=100 Hz and beat 11.1 Hz. Panel b uses p=395 s⁻¹, beat 10.9 Hz and ε=0.05, 0.1, 0.2, 0.4, 0.8 mV per tone. Panel c uses p=330 s⁻¹ and ε=1 mV per tone. Panel d compares AM with m=1 against equal true tones at v*=8 mV over ε=0.02–1 mV. C=135 throughout the closed-loop tests.
- Figure 10 uses the AM surrogate with ε=0.3 mV, m=1, fc=100 Hz, and field-free v*=8.30 mV. The resonance curves use C=118, 126, 132, 135.8. Their damping values are 7.53270, 4.26616, 1.83700, 0.321234 s⁻¹. The current one-decimal damping labels remain correct.
- Figure 11 uses genuine equal tones with Af=8 per tone in normalized drive units, fc=300 Hz, dt=0.05 ms, settling 800 ms, measurement 1500 ms. Its plotted rate amplitudes are ms⁻¹ without rescaling. Background values are −2, 0, 0.7, 0.9 below the Hopf and 2, 5, 11 above it.
- Figure 5 was not edited in this task. Its existing generator uses the AM surrogate with m=1, ε=0.3 mV, fc=100 Hz and p=330, 355, 395 s⁻¹.

## Exact manuscript-resource files changed

- `code/figures_v2.py`
- `code/jr_twotone_figs.py`
- `code/make_jfig.py`
- `code/make_nmm2_twotone_fig.py`
- `figures/fig_concept.pdf`
- `figures/fig_concept.png`
- `figures/fig_demodulation_twotone.pdf`
- `figures/fig_demodulation_twotone.png`
- `figures/fig_curvature_twotone.pdf`
- `figures/fig_curvature_twotone.png`
- `figures/fig_jcurve.pdf`
- `figures/fig_jcurve.png`
- `figures/fig_nmm2_resonance_twotone.pdf`
- `figures/fig_nmm2_resonance_twotone.png`

All additional files created by this repair are under this `figure_repairs/` directory. `touched_files.txt` lists them. No TeX, abstract, references, data-availability text, project records, TODO, or commit was changed by this subtask.
