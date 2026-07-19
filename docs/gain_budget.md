# From reverberation time to an amplification factor: the gain budget

Working note, 2026-07-19. Converts the measured cortical reverberation timescale into the
resonant gain $Q$, then asks whether the full chain closes the TI dose gap.

Empirical constants marked **[V?]** are pending independent verification and should not be
quoted until confirmed.

## 1. The conversion: $Q = \pi f_0 \tau$

Linearize about the stable focus. The relevant eigenvalue pair is

$$\lambda_\pm = -\gamma \pm i\omega_0, \qquad \gamma > 0,$$

with $\gamma$ the distance to the Hopf in rate units and $\omega_0 = 2\pi f_0$ the natural
angular frequency. The impulse response is $\propto e^{-\gamma t}\cos(\omega_0 t + \phi)$,
so spontaneous fluctuations decay with envelope time constant

$$\tau = 1/\gamma .$$

That $\tau$ *is* the reverberation time. Susceptibility to weak forcing at $\Omega$:

$$\chi(\Omega) = \frac{1}{(i\Omega-\lambda_+)(i\Omega-\lambda_-)}
= \frac{1}{\bigl[\gamma + i(\Omega-\omega_0)\bigr]\bigl[\gamma + i(\Omega+\omega_0)\bigr]}.$$

Evaluating on resonance and at DC, for $\gamma \ll \omega_0$:

$$|\chi(\omega_0)| = \frac{1}{\gamma\sqrt{\gamma^2+4\omega_0^2}} \simeq \frac{1}{2\gamma\omega_0},
\qquad
|\chi(0)| = \frac{1}{\gamma^2+\omega_0^2} \simeq \frac{1}{\omega_0^2}.$$

The resonant gain over the static response of the same circuit is therefore

$$\boxed{\;Q \;\equiv\; \frac{|\chi(\omega_0)|}{|\chi(0)|} \;\simeq\; \frac{\omega_0}{2\gamma}
\;=\; \frac{\omega_0\tau}{2} \;=\; \pi f_0 \tau \;=\; \pi\,\frac{\tau}{T_0}\;}$$

with $T_0 = 1/f_0$ the period. In words: **$\pi$ times the number of cycles the ringing
survives.** This is the ordinary quality factor — the half-power width is $|\Omega-\omega_0|
= \gamma$, giving $\Delta f_{\rm FWHM} = \gamma/\pi = 1/(\pi\tau)$ and hence
$Q = f_0/\Delta f_{\rm FWHM}$, consistent with the definition above.

### Against your estimate

Your intuition — natural timescale ~100 ms, reverberation of seconds, so >10× — is right in
order of magnitude and slightly conservative, because the factor $\pi$ is missing. At
$f_0 = 10$ Hz:

| $\tau$ | $\gamma$ (s$^{-1}$) | $Q = \pi f_0\tau$ | resonance FWHM |
|---|---|---|---|
| 100 ms | 10 | 3.1 | 3.2 Hz |
| 200 ms | 5 | 6.3 | 1.6 Hz |
| 500 ms | 2 | 16 | 0.64 Hz |
| 1 s | 1 | 31 | 0.32 Hz |
| 2 s | 0.5 | 63 | 0.16 Hz |

### Directly in terms of the branching parameter

Wilting & Priesemann estimate $\tau = -\Delta t/\ln m$, which for $m\to1$ is
$\tau \simeq \Delta t/(1-m)$. Substituting:

$$Q \simeq \frac{\pi f_0 \,\Delta t}{1-m}.$$

This is the useful form: it maps a *measured* branching parameter straight onto a predicted
amplification. With $\Delta t = 4$ ms and $m = 0.98$ **[V?]**, $\tau = 200$ ms and $Q \approx 6$.
Reaching $Q \approx 30$ requires $m \approx 0.996$.

## 2. Two caveats that decide how much this is worth

**The measured $\tau$ may not be our $\gamma$.** Wilting & Priesemann's $\tau$ is the slowest
relaxation mode of population spiking, estimated from a branching-process fit to the
spike-count autocorrelation, with no oscillatory component in the fit. Our $\gamma$ is the
damping of a specific alpha-band focus. If cortex carries several modes, their estimator
tracks the slowest, which need not be the oscillatory one. Identifying the two is an
assumption, and it gives an **upper bound** on $Q$ rather than a measurement of it. This
needs saying out loud in the paper — it is exactly the kind of borrowed number a referee
will check.

**High $Q$ buys gain and spends bandwidth.** At $\tau = 1$ s the resonance is 0.32 Hz wide.
Individual alpha frequency drifts by more than that within a session, so a fixed $\Delta f$
chosen from a group mean would sit outside the resonance for much of the run and the
response would wash out on averaging.

That second point is worth more than it first appears. It converts the
occipito-parietal alpha null in Mansourinezhad et al. 2025 from a refutation into a
**design specification**: the prediction is not "TI at 10 Hz modulates alpha" but "TI at a
$\Delta f$ tracked to individual alpha within $\sim 1/(\pi\tau)$ modulates alpha, and fixed
$\Delta f$ does not." That is testable with closed-loop EEG-tracked $\Delta f$, and it is a
sharper prediction than anything currently in the table.

It must be stated carefully, though. Read cynically, "your null used the wrong $\Delta f$" is
unfalsifiable special pleading. The way to keep it honest is to state the bandwidth
quantitatively *in advance*, predict the response as a function of $\Delta f$ detuning, and
propose the closed-loop experiment — not to invoke it after the fact.

## 3. The structural point: there are two gaps, and $Q$ closes only one

This is the part I think the paper currently blurs, and it matters for how the dose argument
is written.

**Gap A — the weak-field sensitivity gap.** Bikson's coupling of $\lambda \approx 0.2$ mV per
V/m **[V?]** against a human intracranial field of order 0.8 V/m at 2 mA **[V?]** gives
$\sim$0.16 mV of somatic polarization, against the 10–20 mV **[V?]** from rest to threshold.
Two orders of magnitude short. **This gap applies to all weak transcranial stimulation,
tACS included.** It is the gap you have been chasing, and network amplification near
criticality is the answer to it.

**Gap B — the demodulation gap.** The TI field carries no spectral power at $\Delta f$, so
something must create it. This is TI-specific, and $\Sigma''$ is the answer to it.

Now the consequence. Write the baseband drive in each case, with $\varepsilon$ the membrane
polarization amplitude at the carrier and $\varepsilon_a$ the polarization for tACS applied
directly at $\Delta f$:

$$D_{\rm TI} = \tfrac{1}{2}\Sigma''(v^*)\,\varepsilon^2 \times Q,
\qquad
D_{\rm tACS} = \Sigma'(v^*)\,\varepsilon_a \times Q .$$

**$Q$ appears in both and cancels in the ratio.** So the resonance cannot be the reason TI
works where a single-cell account says it should not — it is the reason *any* weak field
does anything. Conflating the two would be a real error, and given that Karimi et al. put
the TI/tACS amplitude penalty at ~100×, a referee has a ready-made number with which to
catch it.

## 4. The gain budget, and where it binds

Setting $D_{\rm TI} = D_{\rm tACS}$:

$$\varepsilon = \sqrt{2\,\frac{\Sigma'}{\Sigma''}\,\varepsilon_a}.$$

TI's required carrier polarization scales as the **square root** of the tACS polarization it
must match, which is why the penalty is large and why it grows as fields get weaker.

Taking the Jansen–Rit sigmoid steepness $r = 0.56$ mV$^{-1}$, so
$\Sigma''/\Sigma' \sim r$ off the inflection, and $\varepsilon_a = 0.1$ mV:

$$\varepsilon = \sqrt{2 \times 0.1 / 0.56} \approx 0.6\ \text{mV}.$$

Converting to a required field through $\varepsilon = \lambda\,\kappa(f_c)\,E$ with
$\lambda = 0.2$ mV/(V/m):

$$E_{\rm req} = \frac{0.6}{0.2\,\kappa} = \frac{3}{\kappa}\ \text{V/m}.$$

Here $\kappa(f_c) = [1+(2\pi f_c\tau_m)^2]^{-1/2}$ is the membrane low-pass at the carrier.
Against the ~0.24–0.37 V/m **[V?]** that optimized human TI reaches at depth:

| compartment | $\tau_m$ | $\kappa$ at 1 kHz | $E_{\rm req}$ | shortfall vs 0.3 V/m |
|---|---|---|---|---|
| soma | 10 ms | 0.016 | 190 V/m | ~600× |
| soma | 20 ms | 0.008 | 380 V/m | ~1200× |
| fast element | 0.1 ms | 0.85 | 3.5 V/m | ~12× |
| no attenuation | — | 1 | 3.0 V/m | ~10× |

**The binding constraint is $\kappa(f_c)$, not the quadratic step and not the resonance.**
Two things follow, and both are worth acting on.

First, §khz's fast-element argument is not a refinement — it is load-bearing. With somatic
membrane filtering the budget misses by roughly three orders of magnitude; only a fast
compartment brings it within reach. The paper's most vulnerable claim is therefore the
fast-element assumption, and it should be presented as the crux rather than as a caveat.

Second, even in the best case the budget is still ~10× short of matching a tACS field that
is itself only marginally effective. That is a genuinely tight result, and I think stating it
plainly is far stronger than leaving the dose question qualitative. The defensible claim is
that the mechanism explains TI's *phenomenology* — carrier independence, $\Delta f$ tuning,
timing without rate change — and narrows the amplitude gap by the factor $Q$, without yet
closing it. Several factors could absorb the residual: a larger $\Sigma''$ at a favorable
operating point (which is the §opp argument, and makes the operating point quantitative
rather than illustrative), higher TI currents than the tACS comparison assumes **[V?]**, or
a $\lambda$ larger than the somatic value for the compartment that actually does the
detecting.

## 5. Consequences for the revision

- **The dose paragraph becomes quantitative.** State Gap A and Gap B separately, give $Q$,
  and give the residual honestly. This is what Rampersad, Vöröslakos and Huang demand.
- **`fig:jcurve` should stay in the main text.** I had it as borderline in the figure
  triage. It is the figure showing that coupling $J$ sets $\gamma$ and therefore $Q$ — the
  tunability that makes $Q$ a mesoscale variable rather than a fitted constant. That is also
  the direct line back to the $J$-tuning in the Clusella work. Promote it; demote something
  else if we need the slot.
- **Add a $\Delta f$-detuning prediction** with the $1/(\pi\tau)$ bandwidth, and the
  closed-loop individualized-$\Delta f$ experiment. Currently the predictions table has
  nothing this sharp.
- **§khz gets promoted in prominence**, since the budget identifies it as the crux.

## 6. To check before any of this goes in

The algebra above is self-contained and I am confident in it. The empirical inputs are not
yet verified and every **[V?]** must be resolved first — in particular whether human TI
studies really do use higher currents than tACS, which changes the last column of the
budget table, and whether the Wilting–Priesemann $\tau$ can bear the interpretation in §2.
