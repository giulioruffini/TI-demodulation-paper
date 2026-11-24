# v0.15.0-draft3: weak perturbations and finite-amplitude QIF activity

This local revision responds to Giulio's request for slightly more fluent prose,
an explicit weak-perturbation scope, and a clearer, lighter raster figure. The
baseline is draft2 (`a2fc285`). Section order, equations, all 22 figure identities,
and the simulation caches are retained. The QIF section is retitled to state what
its finite-amplitude simulations establish.

## The weak-input argument is separated from the raster examples

The abstracts, Introduction, gain calculation, and Conclusion now make the scope
explicit: weak perturbations of ongoing activity. Neurons may already spike.
For the linear gain calculation, the stimulation-induced mean shift must leave
the operating state stable. Direct carrier-evoked firing and block remain outside
the explanatory scope. The prose changes connect sentences and replace the
modeling-ladder language with the actual progression of the argument.

The abstract previously joined mean-field amplification and QIF timing changes
without distinguishing their amplitude regimes. It now states the near-resonance
result, then identifies the spiking simulations as finite-amplitude illustrations
of coexisting beat-locked and gamma activity. The title of section 4.8 changes
from “Microscale confirmation: TI realigns spike timing in the QIF network” to
“Finite-amplitude TI adds a beat-locked component to QIF population activity.”

At the cached amplitude, A_f = 35 per tone, the leading carrier-excursion estimate
is about 1.24 in the model's voltage units. This is not a weak-input validation.
The mean firing rate changes by 8–11%, and both field-on responses contain gamma
activity in addition to the component at the beat. Methods, Results, captions,
code documentation, and the storyline now use the background drive to identify
the conditions. The historical cache keys are preserved.

## The cache confirms the distinction between gamma and the beat component

The independent calculation is
`code/qif_cached_component_check.py --json docs/qif_cached_components_2026-10-05.json`.
It uses the stored measurement indices, a Hann lock-in, and normalization by the
window mean. It reproduces the stored beat depths to better than 10⁻¹⁰. The cache
hash is recorded in the JSON output.

For background drive 0.85, the spiking-network gamma peak is near 52.26 Hz with
depth 0.704, while the 55 Hz component has depth 0.290. The mean field likewise
has a peak near 51.86 Hz with depth 0.700 and a beat depth of 0.314. Thus panel
(b) cannot support its former purely forced interpretation. Klaus's subsequent
E-only stability calculation (`a330bde`, integrated as `3e4e85d`) supports a
rectified-DC explanation. The threshold obtained by varying the common E/I drive
is not the threshold for an E-only mean shift.

For background drive 1.5, the original gamma FFT-bin estimates reproduce Klaus's
values: about 54.35 Hz and depth 0.860 without stimulation, and 53.12 Hz and depth
0.921 with stimulation. Refining the peak between bins gives about 54.83/53.57 Hz
and depths 0.949/1.004; the difference is finite-window scalloping. The beat depth
is 0.232. Both estimators support the caption's statement that gamma is about
four times larger. The note and JSON distinguish these estimators rather than
treating their frequency grids as interchangeable.

The raster caption now explains that phase folding suppresses non-beat-locked
gamma and exposes the smaller beat component. It no longer promises exact
cancellation over a finite window or equates the fold with gamma-amplitude gating.
The panels retain the same 200 ms display interval and recorded neurons.

## The figures are lighter and their measurement windows are explicit

Dense spike marks and rate shading are rasterized at 450 dpi in the PDF; curves,
axes, and labels remain vector graphics. Only visible samples are embedded in
the display, while the full measurement window still supplies the folds and
statistics. The raster PDF decreases from 13,410,322 to 493,491 bytes, a 96.3%
reduction. Both insets use a common 0–2 scale and label the phase-averaged rate.

The S12(b) spectrum previously started at 60 ms, including much of the 800 ms
settling interval. Its renderer now uses the stored post-settling window, matching
the stated method. No data are resimulated. The S12 condition labels use background
drive rather than assuming the stimulated state is forced or oscillatory.

Both figure collision checks pass. Rendered figures and manuscript pages were
inspected, including the full raster and its caption, S12, both abstracts, the
revised Methods, Results, and Discussion, the redline, and the changed storyline
pages. The manuscript prose checker reports no findings. The executable QIF
simulation code is unchanged, verified by comparing its abstract syntax tree
after excluding its module docstring.

The builds contain 49 TN pages, 32 JNE article pages, 19 supplementary pages,
49 redline pages, and eight storyline pages. There are no LaTeX errors, undefined
references or citations, or overfull boxes. A float placement notice and an
underfull bibliography line remain. The journal PDF is reduced from 14.52 MB to
1.60 MB. The redline shows text changes against draft2 and includes the revised
figures; it does not mark graphical differences pixel by pixel.

The independent calculation `code/ping_field_operating_point_check.py` uses a
finite-difference Jacobian and averages the published quadratic right-hand side
over complete carrier cycles. It reproduces the second-order DC source to
7e-13 in the model's numerical units, the E-only Hopf shift of 0.285776, and the
original-integrator results at amplitudes 10 and 35. The averaged equilibrium
residual is below 6e-13. Evidence is saved in `r7_independent_check_2026-10-05.json`.

At amplitude 35, the predicted E-drive shift is 1.653, and the averaged system's
leading eigenvalue has real part +0.0318/ms. Direct mean-field integration gives
an off-beat gamma depth of 0.605 and a beat depth of 0.300. At amplitude 10, the
shift is 0.1325 and the averaged state is stable (leading real part -0.00874/ms
including source dependence); the direct beat depth is 0.1278 and the mean rate
rises 2.9%. These are mean-field results. The manuscript now gives the mechanism
and the lower-amplitude control with that scope.

The Hessian is exact for the quadratic vector field; the carrier-averaged model
is a second-order approximation and omits feedback from the slow beat response.
The source's E-rate component is about 1.2e-4 of its E-voltage component in the
code's numerical units, not below 1e-5 as stated in Klaus's note; the components
also have different physical units. The manuscript states the E-only shift as
the leading fast-carrier approximation, without that component-ratio claim.

Giulio then stressed the relevance of near-threshold behavior, including Raul's
single-neuron work. The plan retains the amplitude-35 example and adds a
complementary amplitude-10 comparison. The tasks offered for Klaus are both
spiking conditions at amplitude 10 with their own statistics, and an equal-RMS
unmodulated-carrier control at amplitudes 10 and 35, beginning with the mean field.
Whether that control reproduces the induced gamma is a prediction, not a result.
The current draft is an intermediate correction. No unrun spiking result is
substituted, and the new figures will carry statistics recomputed from their own
runs. A cell's firing threshold and a population Hopf remain distinct transitions.

A follow-up screen of the NMM2 coupling curve found that S10 uses the AM surrogate
with amplitudes 8, 4, and 4, rather than two tones of amplitude 8. Its last five
couplings have unstable DC-averaged equilibria. At C = 16.59013865, the E shift is
0.06423 and the leading real part changes from -0.001379/ms without the field to
+0.001142/ms in the averaged system. This is a screen, not a stability result for
the full beat-forced solution. The text now identifies gamma as field-free damping
and does not attribute the endpoint solely to linear amplification. A bounded
dynamic check is offered for Klaus. Source and evidence:
`code/ping_other_sweeps_screen.py`, `r7_other_sweeps_screen_2026-10-05.json`.
The sampled two-tone resonance states at background drives 0, 0.7, 0.9, and 1.0
remain stable under the same DC screen; this does not constitute a check of the
entire carrier/beat grid.

Author declarations and approval, the optional placement decisions, and release
coordination remain open. GitHub push, Calliope/Zenodo release, Overleaf sync, and
coauthor email remain held.

During compilation, the review shelf copied an incomplete TN PDF and repeatedly
filed it as an annotated copy. Those files have no PDF end marker and cannot be
opened by the PDF parser. They are preserved; the shelf's reading copy is restored
from the validated 48-page TN. The restoration record is
`review_shelf_restore_2026-10-05.json`. `build.sh` now compiles in a staging
directory, stops on errors or unresolved references, and publishes each complete
PDF by rename. The three manuscript targets test this production change.
