# R7: the field-induced gamma in the QIF forced condition is the rectified DC shift

Klaus, October 5, 2026, branch `r7-field-induced-gamma` from `a2fc285` (v0.15.0-draft2).
Condition: PING mean field and QIF network of Figure 10(a,b), $\bar\eta=0.85$, two tones of
amplitude $A_f=35$ each at $300\mp27.5$ Hz entering the E voltage equation, beat 55 Hz.
Observation that prompted this: with the field on, the cached run (`code/qif_raster_twotone.npz`)
has its largest spectral line at 51.25--52.5 Hz (depth 0.6--0.7 of the mean rate) in both
the spiking network and the exact mean field, absent with the field off (0.005), while
the 55 Hz forced line has depth 0.29--0.31. No shared file is changed on this branch.

## Equations

The PING nonlinearities are the MPR quadratics ($v^2$, $r^2$, $rv$), so the carrier
average of the dynamics is exact at second order. Writing the field-free system as
$\dot x=f_0(x)$ with Jacobian $A$ and bilinear second derivative $D^2f$ at the operating
point, and the field as $F(t)=\sum_j a\cos\omega_jt$ inside the $\tau_E$-divided E voltage
equation (input vector $b=e_{v_E}/\tau_E$), the first-order carrier response is
$x_1(t)=\sum_j a\,\mathrm{Re}[q_je^{i\omega_jt}]$ with $q_j=(i\omega_jI-A)^{-1}b$, and the
DC part of $\tfrac12D^2f[x_1,x_1]$ is
$$s_{\rm DC}=\sum_j\frac{a^2}{4}\,\mathrm{Re}\,D^2f[q_j,\bar q_j].$$
The slow variables obey $\dot x=f_0(x)+s_{\rm DC}(x)$; the effective operating point
solves $f_0(x)+s_{\rm DC}(x)=0$ self-consistently, and its stability is the Jacobian
there. In the fast-carrier limit $q_j[v_E]\to1/(i\omega_j\tau_E)$, so the source sits in
the E voltage equation alone and equals an E-only drive shift
$$\delta\eta_E=\frac{a^2}{(\omega_c\tau_E)^2},\qquad \omega_c\tau_E=2\pi(0.3\ \mathrm{ms^{-1}})(15\ \mathrm{ms})=28.3,$$
that is, 1.53 at $a=35$. The exact source (full resolvent and Hessian) gives 1.65; its
components outside $v_E$ are below $10^{-5}$ of it, so "E only" holds. Script:
`code/ping_field_operating_point.py` (uses the Jacobian and Hessian of
`ping_fast_carrier_check.py` and the integrator of `nmm2_ping.py` with two tones).

## Stability evidence

| quantity | value |
|---|---|
| field-free point, $\bar\eta=0.85$ | $r_E=0.0506$; leading pair $-0.00567\pm i\,2\pi(54.06\ \mathrm{Hz})$ /ms; relaxation 176 ms (as in Methods) |
| common-drive Hopf | $\bar\eta_H=1.1104$ (distance 0.260) |
| **E-only Hopf** (shift on $\eta_E$ alone) | $\delta\eta_E^*=0.286$, crossing mode 51.4 Hz; critical amplitude $a^*=\omega_c\tau_E\sqrt{\delta\eta_E^*}\approx15$ per tone (exact source: between 10 and 15, about 14.7) |
| effective point at $a=35$ | $\delta\eta_E=1.65$ (5.8 times the critical shift); $r_E=0.0645$; leading pair $+0.032\pm i\,2\pi(54.3\ \mathrm{Hz})$ /ms, growth time 31 ms; numerical Jacobian of the averaged system agrees ($+0.0318$) |

The effective point with the field on is unstable, so the carrier-averaged dynamics sit
on a limit cycle: the 52 Hz activity is a field-induced gamma, not a forced response.
The common-drive threshold alone would have placed instability at a shift of 0.260; the
E-only threshold is 0.286. Both are far below 1.65, so the conclusion does not depend on
which threshold is used, but the E-only one is the right calculation for a field that
enters E alone.

Direct integration of the mean field confirms the picture at every amplitude
(dt 0.05 ms, 800 ms settling, 800 ms window, 44 beat cycles):

| $a$ per tone | $\delta\eta_E$ | Re leading eigenvalue (/ms) | mean $r_E$ (integration / effective point) | beat line depth (55 Hz) | largest other line in 40--60 Hz |
|---:|---:|---:|---|---:|---|
| 35 | 1.65 | $+0.0321$ | 0.0566 / 0.0645 | 0.30 | 0.61 at 51.25 Hz |
| 30 | 1.21 | $+0.0253$ | 0.0559 / 0.0614 | 0.26 | 0.60 at 51.25 Hz |
| 25 | 0.84 | $+0.0179$ | 0.0553 / 0.0585 | 0.22 | 0.51 at 51.25 Hz |
| 20 | 0.53 | $+0.0098$ | 0.0547 / 0.0560 | 0.27 | 0.35 at 51.25 Hz |
| 15 | 0.30 | $+0.0007$ (marginal) | 0.0537 / 0.0538 | 0.24 | 0.04 at 51.25 Hz |
| **10** | 0.13 | $-0.0090$ | 0.0521 / 0.0521 | 0.13 | none ($<10^{-4}$) |
| 5 | 0.03 | $-0.0062$ | 0.0510 / 0.0510 | 0.03 | none |

At $a=35$ the integration reproduces the cache: 51.25 Hz line of depth 0.61 and beat
depth 0.30 against 0.60 and 0.31 in the archived mean-field trace. Where the effective
point is stable the integration's mean rate equals it to four digits, which validates
the averaging. The induced line sits 2--3 Hz below the linear mode frequency because the
limit cycle is far from onset at 1.65.

## A lower amplitude that stays forced

$a=10$ per tone: $\delta\eta_E=0.13$, 46% of the critical shift; the effective point is a
stable focus with Re$\,\lambda=-0.0090$ /ms (more damped than the field-free point,
because the E-only shift first moves the mode away from the Hopf before approaching it);
the mean-field spectrum has the beat line at depth 0.13 and no other line in the gamma
band; $r_E$ stays within 0.045--0.062; the mean rate rises 2.9%. This is a predominantly
beat-forced response. $a=12$ would keep a 30% margin ($\delta\eta_E\approx0.19$); $a=15$
is marginal and should not be used. The beat-locked modulation at $a=10$ is 0.13 of the
mean against 0.30 in Figure 10(b), so the spiking-network raster at this amplitude will
show weaker bunching; with $N=8000$ it should still be visible in the folded rate.
Only the mean field was run here; the spiking network at $a=10$ remains to be run before
the figure is remade.

## Interpretation

The forced condition of Figure 10(a,b) was not weakly forced. The carrier excursion per
tone, $a/(\omega_c\tau_E)=1.24$ in mean-field voltage units, is rectified by $v_E^2$ into
a constant drive on E that is six times the distance to the E-only Hopf. The bunching in
panel (b) is therefore largely a field-induced gamma near 52 Hz, with the 55 Hz forced
component on top; the two beat at 2.5--3.75 Hz, which is the slow variation of burst
heights visible in the panel. The text's "below the Hopf, forced" label applies to the
field-free operating point, not to the field-on one. The remedy is to lower the tone
amplitude to about 10, where the averaged point is stable and the response is forced,
and to state in Methods that the rectified DC term shifts the E operating point by
$a^2/(\omega_c\tau_E)^2$. The same shift exists in the oscillatory condition
($\bar\eta=1.5$, $a=35$), where it moves the system further above the Hopf; it does not
change that panel's qualitative reading but belongs in the same Methods sentence.

Commands:
```sh
.venv/bin/python -B code/ping_field_operating_point.py     # about 1 minute; writes docs/r7_ping_field_operating_point_2026-10-05.json and the spectra figure
```
