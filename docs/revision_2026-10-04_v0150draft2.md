# v0.15.0-draft2: exact reproduction of the kHz two-tone example

This local draft integrates Klaus's reconstructed producer and closes the
remaining kHz reproduction gap. The comparison baseline is v0.15.0-draft1
(`5e9d98a`). Klaus's evidence commit `2696338` is integrated as `02bef19`.
The original cache and all figure files remain unchanged.

Klaus checked the R6 integration against his four caches and confirmed the
observable, averaging, normalization, table entries, and revised interpretation.
His maximum P1 window difference is 9.61 percentage points; Appendix E now rounds
it to 9.6. The remaining R6 qualifications are retained: the saved flag is a
frequency-dominance screen, the field-free 8 Hz component is a persistent spectral
line, and the carrier comparison applies to the specified amplitudes and beat
average. It does not isolate the driven component at every grid point.

## The reconstructed producer reproduces the archived spectra exactly

An independent run of `code/khz_twotone_producer.py --compare` reproduces all seven
stored arrays bit for bit, including their shape and dtype. Both spectral arrays
have a maximum absolute difference of 0.0. The output line is
0.07615781994611578 mV at the 11.00002750006875 Hz bin; the residual DC bin also
matches exactly. The evidence is preserved in
[r12_khz_independent_2026-10-04.json](r12_khz_independent_2026-10-04.json).

The settings are p = 400 s⁻¹, C = 135, 0.5 mV per tone, and a 0.2 ms access
filter. The tones are centered at 2 kHz with a 10.914393 Hz difference. From a
zero initial state, the integration uses nominal 4 s settling and 4 s measurement
windows at a 15 μs step, giving 266,666 steps in each window. Samples are taken
before each RK4 step. Spectra use plain-mean subtraction, a Hann window, and
amplitude normalization by twice the Fourier magnitude divided by the window sum.
Methods now states these settings and replaces its blanket settling-time claim
with the specific 10 s settling/20 s measurement settings of the resonance sweep.

The finite-window input spectrum has a maximum of 2.2430135031813757 × 10⁻¹³ mV
in the 8–14 Hz band. Relative to its largest carrier bin, the value is
4.552828733878659 × 10⁻¹³. Results and the S6 caption now give the former value
with its units, 2.2 × 10⁻¹³ mV, rather than calling it an amplitude ratio.

This establishes a reproducible calculation with explicit settings. It does not
recover the historical source file or prove that these are the only settings
that could produce the cache. Klaus's original reconstruction note is retained
as evidence of his analysis; the manuscript calls the producer reconstructed.

## Both runner modes use the intended data

`run_all.py --only fig_khz_twotone` now generates
`code/khz_twotone_reproduced.npz` and passes that file explicitly to the renderer.
With `--from-cache`, the renderer uses the preserved `code/khz_twotone.npz`.
The generated file is ignored by Git. The README, code guide, availability
paragraph, errata update, and storyline no longer describe this figure as
replot-only.

All 11 runner tests pass, including the fresh-output and archived-input cases.
Both execution paths were then run in an isolated tree. The fresh arrays match
the archive exactly, the original cache hash is unchanged, and fresh, cached,
and manuscript PNGs have the same SHA-256 hash. The execution logs are
[the fresh run](r12_khz_runner_fresh_2026-10-04.txt) and
[the cached run](r12_khz_runner_cached_2026-10-04.txt). This is a targeted
reproduction check, not a new convergence audit or a rerun of every simulation.

## The review builds preserve the paper's argument and structure

The TN, JNE article, and supplement build to 48, 31, and 19 pages, respectively.
The draft1-to-draft2 redline has 48 pages and the storyline has eight. All five
builds have no LaTeX errors, undefined references or citations, or overfull boxes.
The TN, JNE article, and redline retain a float-only-page notice and an underfull
bibliography line. The manuscript prose checker reports no findings.

Rendered-page inspection covers the front pages, revised Methods, Results,
availability, Appendix E rounding, S6 caption, all redline changes, and the three
changed storyline pages. No clipping or overlap was found on those pages. The
redline uses the existing CFONT/whole-math recipe against `5e9d98a`; adjacent
inline-math delimiters are joined only in temporary comparison copies.

Both abstracts, all 42 section and subsection headings, all 32 equation labels,
and all 22 included figure identities are unchanged from draft1. No original
simulation cache or figure file changes. The weak-field effective-response
framing, the fast-membrane NMM2 limit, and Nir Grossman's coauthorship remain.
Versioned review PDFs are exported under `build/`. This is an internal draft,
not a formal version cut or a folder-layout migration.

R6 and R12 are closed at the stated claim level, and the earlier scoped repairs
remain in force. Funding and competing-interest declarations, author roles and
affiliations, actual historical AI-tool versions, and approval by all authors
remain open. Giulio retains the optional placement decisions. GitHub push,
Calliope/Zenodo release, Overleaf synchronization, and coauthor email remain held.
The public code and archive must match the approved version before submission.
