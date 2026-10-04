# R6: the LaNMM carrier comparison read with the lock-in

> Integration status (Kaiti, October 4): this is the original R6 handoff.
> Its capture labels, exact-provenance inference, and some window/background claims
> are superseded by `r6_integration_2026-10-04.md` and
> `r6_lanmm_carrier_lockin_verified.json`. The manuscript uses the verified comparison.

Klaus, October 4, 2026, on branch `r6-lanmm-lockin` from `e34f1f8` (manuscript v0.14.6,
`9bc574c`). The task was to recover the analysis behind the Appendix E claims that the
envelope-locked response of the deep loop falls to about 7% of its peak off the gamma
resonance under superficial (P2) drive and to about 25% under direct (P1) drive, which
the text and the caption of Figure S7 attribute to a phase-sensitive lock-in. The
manuscript, figures, build outputs, and todo are unchanged by this branch.

## No lock-in calculation exists in the record

The two numbers entered the manuscript in commit `a7d6e6f` (July 22, 2026) with the
same wording as today, "falling only to ~25%" in the text and "median 25% of peak" in
the caption. That commit added `lanmm_field_tongues.py` with a `lockin` function whose
docstring explains why band power cannot see a weak coherent drive under the autonomous
alpha, but the function is never called; the carrier maps it cached
(`lanmm_field_P{1,2}_twotone.npz`) hold band-power changes and dominant frequencies
only, and `make_lanmm_field_figs.py` plots those. No script, cache, log, or changelog
entry computes a lock-in over the carrier grid. The provenance gap Kaiti reported is
confirmed.

## The sweep was re-run with the published integrator and read with the lock-in

`code/lanmm_carrier_lockin.py` imports the integrator, field, and estimators of
`lanmm_field_tongues.py` unchanged and re-runs the carrier--beat sweep exactly as
cached: two tones $\varepsilon[\cos(\omega_c-\Omega/2)t+\cos(\omega_c+\Omega/2)t]$
added inside the sigmoid argument of the target population; $\varepsilon=1.5$ mV for
P2 drive and $0.5$ mV for P1 drive; $f_c=25$--$80$ Hz in 56 steps and $\Delta f=5$--$15$ Hz
in 41 steps; RK4 with $dt=10^{-4}$ s; 2 s settling; 3 s measurement. The band-power
change computed from the re-run matches the committed caches to $3\times10^{-16}$
relative, so the trajectories are the published ones.

The read-out is the Hann-windowed quadrature lock-in of $v_{P1}$ at $\Omega=2\pi\Delta f$
over the measurement window (the `lockin` function; amplitude $\sqrt{I^2+Q^2}$, in mV),
stored with $I$ and $Q$, together with the dominant output frequency of $v_{P1}$ and the
band-power change. A field-free run gives the leakage floor: the amplitude the lock-in
reports at each $\Delta f$ from the column's own alpha when no field is applied. A
second run with a 10 s window (`--tmeas 10 --tag _tmeas10`) is the leakage control.
Outputs: `code/lanmm_carrier_lockin_{P2,P1}_twotone{,_tmeas10}.npz`, summaries in
`code/lanmm_carrier_lockin_summary{,_tmeas10}.json`, run transcripts in
`code/lanmm_carrier_lockin_run_tmeas{3,10}.txt`, per-carrier table in
`docs/r6_lanmm_carrier_lockin_table.csv`, the numbers quoted below in
`docs/r6_lanmm_carrier_lockin_numbers.json`, and maps in
`docs/r6_lanmm_carrier_lockin{,_tmeas10}.png` (`code/make_lanmm_carrier_lockin_fig.py`).

## What the lock-in shows

**Near the column's alpha the lock-in reads the column, not the drive.** The field-free
alpha of $v_{P1}$ sits at 10.67 Hz (10.60 Hz in the 10 s window) with an amplitude of
about 2.5 mV. With the 3 s window its leakage into the lock-in is 2.50 mV at
$\Delta f=10.5$ Hz, 0.66 mV at 11.0 Hz, and 0.25 mV at 10.0 Hz; beyond 1.5 Hz from the
alpha it is below 0.02 mV (below 0.001 mV with 10 s). Under both drives the maximum of
the lock-in over $\Delta f$ lies at $\Delta f=10.25$--$10.5$ Hz for every carrier, and at
that maximum the dominant output frequency is within 0.3 Hz of the beat for every
carrier: the "ridge at $\Delta f\approx10.5$ Hz even for a 60 Hz carrier" is the
autonomous alpha captured by the beat (at 60 Hz the captured beats are 10.5--10.75 Hz
under P1 drive and 10.25--11.0 Hz under P2 drive). Its amplitude, 1.2--3.6 mV, is the
alpha limit cycle, not a demodulated component. Within about 1 Hz of the alpha the
beat pulls the rhythm even where it does not capture it, so the $\Delta f=10$ Hz column
is contaminated at any window length.

**Away from the alpha the driven component is clean and carrier dependent.** The
statistic used below is $S(f_c)$, the lock-in amplitude of $v_{P1}$ averaged over the
17 beats in 7--14 Hz that lie more than 1.5 Hz from the alpha (7.0--9.0 and 12.25--14.0
Hz); its leakage floor is below 0.02 mV and no point in it is captured. The 3 s and
10 s windows agree on it to within 0.01 of the ratios.

| Drive | $\varepsilon$ | peak of $S$ | at 25 Hz | 30--80 Hz range (median) | at 60 Hz | at 80 Hz |
|---|---|---|---|---|---|---|
| P2 (superficial) | 1.5 mV | 0.45 mV at $f_c=39$ Hz | 17% | 23--100% (43%) | 49% | 39% |
| P1 (direct) | 0.5 mV | 0.091 mV at $f_c=25$ Hz | 100% | 42--68% (53%) | 52% | 53% |

Single beats are sharper than the average. At $\Delta f=9$ Hz the P2-drive response
peaks at $f_c=34$--$36$ Hz and falls to 3--5% of that peak at 25--26 Hz (median over
carriers 40%); at $\Delta f=12$ Hz it peaks at 38--42 Hz and falls to 15% at 52--53 Hz
(median 35%). Under P1 drive the response at $\Delta f=9$ Hz falls to 22--30% of its
25 Hz value near $f_c=27$--$35$ Hz (median 48%), and at $\Delta f=12$ Hz it dips to
2--13% near $f_c=45$ Hz (median 51--58%): the carrier near the P2 gamma affects the
deep response even when the field is applied to P1.

**The quoted numbers come from the contaminated column.** With the 3 s window, the
median over carriers of the lock-in at $\Delta f=10.0$ Hz under P1 drive, divided by its
maximum (a single captured carrier at 25 Hz), is 0.250. That is the caption's "median
25%", and it is an artifact: the plateau it measures (0.31 mV) is the leakage floor at
10.0 Hz (0.25 mV) plus a small driven part, and with the 10 s window the same ratio is
0.44. For P2 drive the same column gives a minimum of 5.0% of its peak (8.0% with 10 s)
and the band-power map gives a median of 7.1% at $\Delta f=10$ Hz relative to its 44 Hz
peak; either could be the origin of "~7%", and neither is a lock-in measure of the
driven component.

## What survives, and the proposed wording

The qualitative contrast survives in the clean statistic. Under superficial drive the
envelope-locked deep response is largest for carriers near the P2 gamma (39 Hz) and
falls to 17% of that peak at 25 Hz (to 3--5% at a single 9 Hz beat) and to 39--49% at
60--80 Hz; the double resonance is real. Under direct drive the response is largest at
the lowest carriers and stays within 42--68% of that value from 30 to 80 Hz, with a dip
near 45 Hz at some beats. The specific figures 7% and 25%, the phrase "falling only to
25%", and the attribution of either to a lock-in should be withdrawn. The sentence
that "the ridge sits at $\Delta f\approx10.5$ Hz even for a 60 Hz carrier" describes
capture of the autonomous alpha and should be said as such or dropped.

Proposed replacement for the two sentences of the Appendix E carrier paragraph that
carry the numbers (from "the fast loop acts as a tuned radio-frequency (RF) front end"
to "as Eq. (10) predicts for direct coupling"):

> the fast loop acts as a tuned radio-frequency (RF) front end that must itself be
> excited before it can pass a demodulated envelope to $P_1$. Read with the lock-in of
> $v_{P_1}$ at beats more than 1.5 Hz from the column's own alpha (averaged over
> 7--14 Hz), the deep response peaks for carriers near 39 Hz and falls to 17% of that
> peak at 25 Hz and to 39--49% at 60--80 Hz; at a single 9 Hz beat the fall at 25 Hz is
> to 3--5%. When the field is delivered directly to the slow generator ($P_1$), the
> same read-out is largest at the lowest carriers and stays within 42--68% of that
> value from 30 to 80 Hz (median 53%), with a dip near 45 Hz at some beats
> (Fig.~\ref{fig:lanmm_p1}c): broadband in $f_c$, as Eq.~\eqref{eq:demod} predicts for
> direct coupling, up to the carrier's own effect on the gamma loop.

Proposed replacement for the following paragraph ("This contrast requires the
phase-sensitive read-out ... (Methods)."):

> The read-out matters here. Within about 1 Hz of the column's own alpha (10.7 Hz)
> the beat captures or pulls that rhythm, so both band power and the lock-in at
> $\Delta f$ report the alpha limit cycle itself; the maximum over $\Delta f$ of either
> estimator sits at $\Delta f\approx10.5$ Hz for every carrier for that reason. The
> driven component is isolated by the lock-in at beats away from the alpha, which is
> what the percentages above measure (Methods).

Proposed sentence for Methods, LaNMM paragraph, after the alpha-power estimator:

> The carrier comparison of App.~\ref{app:lanmm} reads instead the lock-in
> (Eq.~\eqref{eq:lockin}) of $v_{P_1}$ at $\Delta f$, averaged over the beats in 7--14 Hz
> more than 1.5 Hz from the column's autonomous alpha, per carrier, with the same
> settling and window; its field-free floor is below 0.02 mV.

Proposed replacement for the last two sentences of the Figure S7 caption:

> Read with the lock-in of $v_{P_1}$ at beats away from the column's alpha, the deep
> response under direct drive stays within 42--68% of its 25 Hz value across 30--80 Hz
> (median 53%), whereas under superficial drive it falls to 17% of its 39 Hz peak at
> 25 Hz. The vertical ridge at $\Delta f\approx10.5$ Hz is the column's own alpha,
> captured by the beat at every carrier.

Figure S1's caption ("a double resonance") needs no change. If the maps are to show
the lock-in rather than band power, `make_lanmm_carrier_lockin_fig.py` has the arrays;
that is a figure decision for K, not part of this branch.

## Remaining uncertainty, stated

- One amplitude per drive was run (1.5 and 0.5 mV, as published). The percentages are
  properties of those amplitudes; at 0.5 mV the P1 drive captures the alpha within
  about $\pm0.4$ Hz, at 1.5 mV the P2 drive captures it within about $\pm1$ Hz for
  carriers of 33--47 Hz.
- The sideband statistic averages 17 beats; single-beat ratios range from 3% to 30% at
  the worst carrier, as listed. The choice of a 1.5 Hz exclusion band is mine; with
  1.0 Hz the 3 s leakage floor rises to 0.25 mV at 10.0 Hz and the statistic is no
  longer clean.
- Under P1 drive the driven component (0.04--0.09 mV) is 2--4% of the alpha amplitude.
  It is far above the leakage floor, but small; any wording should quote the mV scale.
- The origin of "7%" is not recovered exactly; two candidate ad hoc statistics from the
  $\Delta f=10$ Hz column give 5% and 7%. The origin of "25%" is reproduced to three
  digits.
- No time-step or settling sensitivity was re-run here; the cache match shows the
  integrator is the published one, and the two windows give the same clean ratios.
