# TODO — TN0484 / WP0185 (TI tuned receiver)

- [ ] GALVANI deck before Thu 24 Sep: soften three frames (NMM2 "exact square-law rectifier" → quadratic mixing read through F'; Predictions row "sign flip" → JR-specific; "Timing, not rate" → timing modulation with 7–11% rate change); rehearse to 18 min; decide title
- [ ] Giulio: decide abstract retreat (keep result-first tuned-receiver abstract with two detector routes, or Kaiti's §5 text), Prediction 2 fate (JR-specific or dropped), LaNMM as labeled extension
- [ ] ask Kaiti for the v2 companion files not in Downloads: crossover_review_checks.py/.json, review_spot_checks.py, spot_checks.json, WP0185_review_notes.md (v1), package README
- [ ] Pass A numerics: rate readout σ(v+s) in timing_not_rate.py:87; per-neuron vector strength (qif_raster.py:90–116); signed LaNMM maps + estimator stated (clip at make_lanmm_field_figs.py:30, FFT band power not Hilbert); entrainment by unwrapped phase, exclude ε=0 (10.667 Hz artifact); QIF runs longer than 420 ms with dt/N/threshold convergence; Hopf paragraph: η̄_H=1.110, f=54.0 Hz, no finite-size shift; run_all.py map (8 two-tone figs missing)
- [ ] Pass B theory: two-tone derivation primary (N1); dynamic source/susceptibility for PING (N2) with 300 Hz/1 kHz/2 kHz source-error table; MPR slow-F''→fast-F' crossover figure from crossover.py; 0.3479 bound to appendix as memoryless comparator, step-detector harmonic ratio 0.151 not 0.2; Clusella Eq. 17 is a QIF transfer, not a logistic
- [ ] Pass C text: three claim levels in abstract/intro/conclusion; Table predictions revised; Discussion shortened (criticality, TMS, sigmoid family out); retrospective ΔPLV=Ψ(aI^p) fit dropped (non-identifiable); fold in docs/review_2026-09-22_readability_notation.md
- [ ] Pass D: clean rebuild ×2, disposition log R1–R13/A1–A12/K01–K15, v0.14.0, cut in Calliope, re-sync Overleaf, then send the co-author approval request (HOLD v0.13.0 email)
- [ ] Giulio: code.zip and figures.zip at repo root (09:55 today, untracked): delete or add *.zip to .gitignore
- [ ] Giulio: Preview-annotated TN PDF in the working tree: keep a copy in _private/reviews, then restore the committed build
- [ ] ask Canals and Mirasso for their funding lines; pin Claude/ChatGPT versions in the AI declaration
- [ ] re-measure JNE main-text words with texcount on a jne-expanded copy (12,000 cap)
- [ ] merge two-tone-validation into main after v0.14.0
- [x] readability + notation review written (docs/review_2026-09-22_readability_notation.md)
- [x] integrate the 2026-08-07 doors edit into abstract, conclusion, predictions (v0.13.0)
