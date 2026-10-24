# Theta-neuron pilot: pre-registered protocol (written before any run)

Klaus, 2026-10-24, per Kaiti's handoff (21:04). Script: `theta_pilot.py` in this
folder; it imports `code/qif_raster.py` read-only and writes only here.

**Model.** The published QIF network with the exact change of variables
$V=\tan(\theta/2)$, which removes the spike cutoff $V_{\rm peak}$. All other
settings are the published ones: $\bar\eta=0.85$, carrier 300 Hz, beat 55 Hz,
two tones of amplitude $A_f=10$ on the excitatory membranes, $N=8000$ per
population, Euler $\Delta t=0.0025$ ms, 800 ms burn-in, 44-cycle window
(800 ms), same excitability quantiles, seed, synapses, and readouts. Spike times
are linearly interpolated at the $\theta=\pi$ crossing.

**Runs and budget.** At most 8 runs or 60 min of compute, whichever comes first:
`off`, `on`, `dt2` ($\Delta t/2$), `n2` ($2N$), `long` (window doubled, burn-in
unchanged); then, only if the solver validates, `sc10`, `tt35`, `sc35` (equal-RMS
single-carrier controls, with the two-tone $A_f=35$ run as their comparison).

**Pilot criterion (rate statistics).** The theta solver validates if the beat
depth (lock-in at 55 Hz divided by mean E rate, field on) changes by less than
5% relative to `on` under each of `dt2`, `n2`, and `long`. Mean E rate is
reported alongside. Phase statistics (pooled vector strength, pairwise phase
consistency) are reported separately and carry no pass criterion.

**What is not a target.** Agreement with the exact mean field (published value
0.128 at this amplitude) is an outcome to report, not a tuning target. No
parameter is adjusted after seeing results.

**Stop rule.** If any check exceeds 5%, or the budget is exhausted, the pilot
stops, the controls are deferred, and the report states the qualitative
fallback: depths reported to one significant figure with their cutoff range.

**Limitations known in advance.** Euler in $\theta$ with the published step;
the few neurons with the largest excitabilities advance up to about 0.8 rad per
step and are the likeliest source of step dependence. Finite $N$ differs from
the mean field at order $1/\sqrt N$ in the fluctuating part. The single-carrier
control matches RMS input current in model units, not a calibrated
polarization. Rate-change percentages are given only where an `off` run at the
same settings exists (baseline settings).
