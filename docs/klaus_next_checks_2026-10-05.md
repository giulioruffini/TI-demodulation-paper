# TN0484: comparisons around the stimulation-induced transition

For Klaus, offered through Giulio on October 5. This consolidates the handoffs
from the conversation; it does not imply that every task has been accepted.
Base: published-cache code at `a2fc285`, your R7 diagnostic `a330bde` (integrated
as `3e4e85d`), and Kaiti's local v0.15.0-draft3 correction. Work in an isolated
branch/worktree. Do not edit shared manuscript, figures, builds, or TODO; no push.
Retain all amplitude-35 evidence. Return code, separate caches, a dated note, and
proposed figures; Kaiti will integrate the reviewed results.

## Compare the spiking network at amplitude 10

Run both Figure 10 conditions at A_f = 10 per tone, carrier 300 Hz:
background drive 0.85 with beat 55 Hz, and drive 1.5 with beat 42 Hz. Keep field-off
controls and the published population size, integration, and measurement settings.
Compare the spiking network with the exact mean field. Return the four-panel
raster and S12 comparison, preserving the layout, plus a table of every dependent
statistic: mean-rate change, beat depth, largest other gamma line, per-neuron
pairwise phase consistency, pooled vector strength, and the ratio of modulation
depth to mean-rate change. Test apparent residual off-beat activity with a longer
measurement window and report finite-size uncertainty where relevant. A stable
averaged point alone does not establish square-law scaling of the finite response.

These runs complement, rather than erase, the amplitude-35 example. The updated
renderer rasterizes dense spike/shading layers at 450 dpi while keeping text and
curves vector, reducing the PDF from 13.4 MB to 0.49 MB; preserve that treatment.

## Test an equal-RMS unmodulated carrier

At background drive 0.85, compare TI at a = 10 and 35 per tone with one 300 Hz
carrier of peak amplitude sqrt(2) a. Match duration and measurement windows.
Begin with the exact mean field. Report the mean shift, gamma activity, and
55 Hz component. Matching RMS gives approximately the same rectified source
in the nearby, fast-carrier limit; finite-frequency corrections can differ.
Whether the control reproduces the induced gamma is a prediction to test.
Keep the carrier/control result distinct from any unrun spiking comparison.

## Check S10's full forced endpoint dynamics

S10's producer `nmm2_jcD.py` uses the AM surrogate, with carrier amplitude 8 and
sideband amplitudes 4/4. `code/ping_other_sweeps_screen.py` finds unstable DC-only
averaged equilibria at the last five coupling values. Its JSON is
`docs/r7_other_sweeps_screen_2026-10-05.json`.

At C = 16.59013865, background drive 0, carrier 300 Hz, and beat 50.5 Hz, the
screen gives E-drive shift 0.06423 and leading real part +0.001142/ms, compared
with -0.001379/ms field-free. Check the full periodically forced dynamics and
whether the endpoint can be interpreted as amplification about a stable driven
state. A DC-only equilibrium screen does not establish the stability of the
periodic solution. Return the stability diagnostic, measurement duration, and
recommended wording; preserve the measured curve.
