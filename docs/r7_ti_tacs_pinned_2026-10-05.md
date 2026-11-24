# TI versus tACS in the pinned sweep: what pinning fixes, and what makes the ratio rise near the Hopf

Klaus, October 5, 2026, branch `r7-followups`. Correction to my message of 14:59: pinning
in the J-curve sweeps fixes the field-free fixed point at $v^*=8.30$ mV through $p(C)$; it
does not cancel the stimulated mean shift. Kaiti's reading of the code is right. This note
measures the shifts and shows what the $\gamma$-dependence of the TI-to-tACS ratio is made
of. Script `code/ti_tacs_pinned_diagnostic.py`; data
`docs/r7_ti_tacs_pinned_diagnostic_2026-10-05.json`; the two J-curve caches that the ratio
of `docs/r7_ti_tacs_ratio_vs_gamma_2026-10-05.json` was read from are preserved as portable
tables with SHA-256 in `docs/r7_tacs_jsweep_table_2026-10-05.json` (the ignored
intermediate) and `docs/r7_jcurve_main_table_2026-10-05.json`.

Settings: Jansen--Rit column of `jr_jsweep_engine.py`, $p=p_{\rm of}C(8.30, C)$, beat at the
field-free modal frequency, dt $2\times10^{-4}$ s, 12 s settling and 6 s window (the
published values), repeated with 60 s settling and 20 s window. Four conditions: field off;
TI as in Figure 9 (AM surrogate, $\varepsilon=0.3$ mV, $m=1$, 100 Hz carrier); tACS as in
Figure S3 ($0.1$ mV); and tACS with the source-matched amplitude
$\varepsilon_t=\tfrac12|\Sigma''|\varepsilon^2m/\Sigma'=0.0143039$ mV, which delivers the
same leading in-band drive as TI's beat. Recorded: window mean of $v=y_1-y_2$, mean
pyramidal rate $\Sigma(v+s)$, lock-in at the beat.

| C | $\gamma$ (s$^{-1}$) | condition | $\langle v\rangle$ shift (mV) | $\langle r\rangle$ shift (s$^{-1}$) | lock-in (mV) | ratio to source-matched tACS |
|---:|---:|---|---:|---:|---:|---:|
| 110 | 10.74 | TI | +0.0073 | $-0.0016$ | 0.0235 | 0.989 |
| | | tACS 0.1 | +0.0019 | $-0.0013$ | 0.1655 | 6.97 (linear 6.99) |
| | | tACS matched | +0.00004 | $-0.00003$ | 0.0237 | 1 |
| 133.91 | 1.073 | TI | +0.0130 | $-0.0022$ | 0.2999 | 0.941 |
| | | tACS 0.1 | +0.0911 | $-0.0241$ | 1.2587 | 3.95 |
| | | tACS matched | +0.0055 | $-0.0015$ | 0.3188 | 1 |
| 136.3 | 0.123 | TI | +0.0344 | $-0.0075$ | 0.7123 | 0.919 |
| | | tACS 0.1 | +0.1321 | $-0.0324$ | 1.5168 | 1.96 |
| | | tACS matched | +0.0323 | $-0.0080$ | 0.7750 | 1 |

The 60 s / 20 s repeat reproduces every stimulated entry to better than 0.1%. The only
change is the field-off endpoint, where 12 s settling leaves a 0.094 mV transient lock-in
(relaxation time 8 s) that 60 s removes (0.0001 mV); the published sweeps therefore carry a
small undecayed field-free component at their last point, which the lock-in with the field
on does not visibly inherit (0.7115 against 0.7123 mV).

## Reading

1. **The source-matched tACS reproduces TI at every coupling.** Ratios 0.99, 0.94, 0.92:
   a direct drive with the same leading in-band amplitude gives the same response, the same
   mean shift near the Hopf, and the same growth toward it. TI is, to within 8% at the
   endpoint, a tACS of amplitude $\tfrac12|\Sigma''|\varepsilon^2m/\Sigma'$.
2. **The rise of the TI-to-tACS(0.1 mV) ratio near the Hopf is saturation of the larger
   response, and the mean shift is its mechanism.** The 0.1 mV drive is 7.0 times the
   matched one; far from the Hopf it gives 6.97 times the response, at $\gamma=1.07$ 3.95
   times, at $0.12$ 1.96 times. Where it falls short, its mean has moved by 0.09--0.13 mV
   and its mean rate by 0.6--0.8%: the $\pm1.3$--$1.5$ mV output oscillation rectifies
   through $\Sigma''$, the operating point moves, and the gain drops. TI and the matched
   tACS, with $\pm0.3$--$0.7$ mV outputs, shift by 0.005--0.03 mV and stay nearer the linear
   law. So "earlier saturation of the larger response" and "mean-shift effect" are one
   mechanism here, produced by the response, not by the carrier.
3. **TI's own carrier DC term is small and visible only far from the Hopf.** At $C=110$ TI
   shifts the mean by 0.0073 mV against 0.00004 for the matched tACS; that is the rectified
   carrier ($\tfrac14\Sigma''\varepsilon^2(1+m^2/2)$ in rate, read through $G(0)$), and it
   costs TI nothing there (ratio 0.99). Near the Hopf the response-driven shift dominates in
   both conditions, and TI's extra 0.002--0.008 mV lowers its gain by 6--8% relative to the
   matched drive. Pinning does not remove this; it is simply small at these amplitudes.

What the paper can say: within linear response the ratio is $\gamma$-independent; the
measured rise toward the Hopf in the pinned sweep (0.14 → 0.24 → 0.47) is the saturation of
the stronger-driven tACS response through its own rectified mean shift, and a tACS drive
matched to TI's beat source tracks the TI response to within 8% across the sweep.
