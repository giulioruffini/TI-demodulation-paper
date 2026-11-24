# v0.15.0-draft4: QIF amplitude comparison and equal-power carrier controls

The baseline is draft3 (`669128b`). Klaus's isolated R7 follow-ups (`5e5921d`,
`cecb707`) are integrated as `0b46d91` and `6f6d5bf`. The revision retains every
original figure and its order, all 32 labeled equations and 59 citation keys, and the section order.
Figure S13 adds the lower-amplitude comparison and mean-field carrier controls.
No original simulation cache is replaced.

## The amplitude comparison distinguishes modulation from gamma induction

At background drive 0.85 and amplitude 10 per tone, the N=8000 spiking network
has a 55 Hz depth of 0.09264 and a mean-rate increase of 2.7649%. Their ratio is
3.3506. The mean field gives depth 0.12774. Doubling N gives about 0.083 and
halving the integration step gives about 0.093; these checks do not close the
difference. The finite implementation uses spike/reset voltages of ±100, whereas
the exact mean field describes the ideal QIF limit. A further cutoff check is
requested from Klaus, separately from this integration.

The pooled vector strength is 0.046. Median per-cell pairwise phase consistency
remains negative, as without the field; that median does not establish absence
of locking in every neuron. Extending the window from 44 to 88 cycles gives a
similar beat depth and a smaller residual off-beat peak, consistent with noise
averaging but insufficient to prove its origin or a scaling law.

At background drive 1.5, amplitude 10 produces a 42 Hz depth of 0.02298 and a
mean-rate increase of 1.5771%. The autonomous gamma remains dominant. The old
amplitude-35 examples remain in Figure 10 and S12, including the autonomous-gamma
condition that would have been lost by replacing the figure with only drive 0.85.
The original convergence statements are now explicitly scoped to amplitude 35.

## Equal-RMS mean-field controls separate state change from the beat response

A single 300 Hz carrier with peak amplitude sqrt(2) times the TI tone amplitude
has the same mean-square input over the 800 ms measurement window. Both waveforms
start at the field-free equilibrium, settle for 800 ms, and are measured for
800 ms at dt=0.05 ms. The mean-field control is not a new spiking-network run.

At amplitude 10, the second-order E shifts are 0.13251 for TI and 0.12896 for the
carrier. Their mean rates rise 2.90% and 2.80%; neither induces gamma, and the
resolved beat belongs to TI. At amplitude 35, the shifts are 1.65254 and 1.60579,
and mean rates rise 11.78% and 12.00%. Both induce gamma near the 51.25 Hz FFT
bin. TI additionally has a 55 Hz depth of 0.2997. The carrier's finite-window
lock-in at 55 Hz is 0.0110; it is not reported as an exactly zero line. A longer
window check is requested to quantify residual spectral leakage.

The new S13 uses the original amplitude-35 and new amplitude-10 spiking caches
in its upper panels, with common scales and phase folds. Its lower panels show
the two mean-field spectra at each amplitude on a common scale. Dense spike marks
are rasterized; labels and curves remain vector graphics. Original Figure 10 and
S12 are untouched in this revision. A future promotion or rearrangement remains
Giulio's choice.

## S10's endpoint is stable under the full periodic forcing

Klaus reproduced the cached lock-ins and found negative long-window perturbation
growth. The independent calculation in `code/s10_periodic_stability_check.py`
integrates all eight variational directions, rather than one tangent vector.
The AM forcing at carrier 300 Hz and beat 50.5 Hz repeats every 2000 ms.
After 8000 ms settling, two successive periods have relative closure errors
7.9e-7 and 2.7e-8. The largest multiplier moduli are 0.03419383 and 0.03419381,
corresponding to a leading exponent of -0.001687855 per ms. The analytic Jacobian
matches a finite-difference check within 1.1e-10.

This establishes an attracting periodic endpoint. The DC-only equilibrium screen
omits feedback from the beat response and does not decide its stability. The
manuscript and caption retain the measured curve, identify gamma as field-free
damping, and distinguish the final nonlinear response from linear gain about the
DC-shifted equilibrium. Increasing settling from 0.6 to 3 s changes the endpoint
lock-in by 0.8%, as Klaus's preserved comparison records.

## Reproduction and inspection

`code/verify_r7_followups.py` independently recomputes rate lock-ins, pooled vector
strength and phase consistency, and per-cell phase-consistency summaries for five
QIF caches. The summaries agree within 1e-10. It also reproduces the four carrier
controls using the original `nmm2_ping._rk4` integrator and matches the recorded
means and spectral depths within 1e-7. The original field cache hashes are saved.
The four traces are preserved in `code/ping_carrier_control_traces.npz`.

Evidence files:

- `docs/r7_followups_independent_2026-10-05.json`
- `docs/r7_s10_periodic_check_2026-10-05.json`
- `docs/r7_followups_2026-10-05.md` and its referenced Klaus caches and JSON records

The figure runner includes both amplitude producers and the carrier-control
producer for S13. Its cache-only mode runs the renderer alone. All 12 runner tests
pass, and the cached S13 renderer passes the collision check. The manuscript prose
check reports no mechanical findings. These checks do not amount to rerunning
all historical simulations or a new audit of the complete manuscript.

Adding S13 exposed an ordering issue in the split build: the article could fail
before the supplement exported its new label. `build.sh all` now bootstraps the
article's labels without publishing its temporary PDF, builds the supplement,
and then publishes both with settled cross-references. This succeeds in a
scratch build started without auxiliary files; its temporary unresolved labels
are never published as a PDF. Complete PDFs are still
published by rename, so the review shelf cannot copy an in-progress build.

The TN abstract has about 254 words; the structured JNE abstract has about 291,
including its run-in headings. The abstract specifies that the carrier control
is mean-field evidence. The storyline carries the same abstract and the new
figure's place in the argument.

Author declarations and approval, optional placement decisions, and release
coordination remain open. GitHub push, Calliope/Zenodo release, Overleaf sync, and
coauthor email remain held.

The final clean manuscript builds contain 50 TN pages, 32 article pages, and
20 supplementary pages, with no errors, undefined references or citations, or
overfull boxes. The existing float-placement notice remains. The new figure and
the changed Results pages were rendered and inspected. The redline has 50 pages and the storyline eight. The redline marks text
changes against draft3 and includes the current graphics without pixel-level
difference marking.

Build sizes, hashes, and retention checks are in `validation_2026-10-05_v0150draft4.json`.
