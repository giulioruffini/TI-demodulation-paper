# Pairs: results

## Pair 1

**Original**

\section{Results}
\subsection{The JR column generates and resonantly amplifies the beat}
An input containing only the two tones $f_c\mp\Delta f/2$ produces an output
oscillation at their $11.1$~Hz beat, near the column's alpha resonance
(Fig.~\ref{fig:bif}). The alpha peak is absent from the input spectrum
(Fig.~\ref{fig:demod}).

**Proposed**

\section{Results}
\subsection{The JR column generates and resonantly amplifies the beat}
Driven only by the two tones $f_c\mp\Delta f/2$, the column oscillates at
their $11.1$~Hz beat, near its alpha resonance (Fig.~\ref{fig:bif}),
although the input spectrum has no alpha peak (Fig.~\ref{fig:demod}).

*Script: claim-strength changes ['no +1']; quantity changes ({}, {}, False)*

## Pair 2

**Original**

In the stable-focus regime ($p>p_H$), the response is approximately Lorentzian
and its peak grows from $0.23$ to $0.43$ to $0.70$~mV toward the Hopf
(Fig.~\ref{fig:res}), as expected from the
$1/\gamma$ susceptibility. Without a drive the focus is silent at $\Omega$;
the nonlinearity generates that component and recurrence amplifies it.
The peak shifts with the driven operating state; the near-Hopf law gives
its leading gain, not its exact frequency. The coupling sweep tests that law
over a decade of damping.
On the alpha branch below $p_H$, the column free-runs at $f_0$, so the lock-in
can contain both driven and autonomous activity. The dominant output frequency
$f_{\rm out}$ then identifies a frequency-dominance region
(Fig.~\ref{fig:entrain}), without establishing phase capture.

**Proposed**

In the stable-focus regime ($p>p_H$), the response is approximately
Lorentzian, and its peak grows from $0.23$ to $0.43$ to $0.70$~mV toward the
Hopf (Fig.~\ref{fig:res}), as expected from the $1/\gamma$ susceptibility.
The field-free focus is silent at $\Omega$, so the nonlinearity generates
that component and recurrence amplifies it. The near-Hopf law gives the
leading gain but not the exact peak frequency, which shifts with the driven
operating state; the coupling sweep tests the law over a decade of damping.

On the alpha branch below $p_H$, the column free-runs at $f_0$, so the
lock-in can contain driven and autonomous activity. The dominant output
frequency $f_{\rm out}$ then identifies a frequency-dominance region
(Fig.~\ref{fig:entrain}) without establishing phase capture.

*Script: claim-strength changes ['without -1']; quantity changes ({}, {}, False)*

## Pair 3

**Original**

\subsection{Carrier independence and the kHz roll-off}
At fixed post-access polarization, the open-loop detector and near-Hopf
JR column are carrier-independent outside their natural band
(Fig.~\ref{fig:carrier}). At fixed applied field, the point-membrane
response instead falls as $1/f_c^2$ above its corner
(Fig.~\ref{fig:khz}); the sealed-cable estimate is compared with the
point-membrane cases in Fig.~\ref{fig:feasibility}a.

**Proposed**

\subsection{Carrier frequency acts through access}
At fixed post-access polarization, the open-loop detector and the near-Hopf
JR column are carrier-independent outside their natural band
(Fig.~\ref{fig:carrier}). At fixed applied field, the point-membrane
response instead falls as $1/f_c^2$ above its corner (Fig.~\ref{fig:khz});
Fig.~\ref{fig:feasibility}a compares the sealed-cable estimate with the
point-membrane cases.

*Script: claim-strength changes none; quantity changes ({}, {}, False)*

## Pair 4

**Original**

With an explicit first-order access state per modeled compartment before
the sigmoid, the full JR column demodulates and resonates in the assumed
$\tau=0.2$~ms case (Fig.~\ref{fig:khz_direct}a). Genuine tones centered
at $2$~kHz generate the absent $10.914$~Hz beat, with analytic access
factor $|H_m|^2=0.137$ (Fig.~\ref{fig:khz_twotone}). These are consequences
of the assumed access time and coupling; neither is calibrated by the simulation.

Figure~\ref{fig:feasibility} converts this access assumption into a source
budget. With $\varepsilon_j=\lambda_0 E_j|H_m(\omega_j)|$, the equivalent
direct beat input is $\varepsilon_{\rm eq}=Y_\Omega/\Sig'$, before recurrent
gain. At $2$~kHz, $\tau_m=0.2$~ms, $\lambda_0=0.5$~mV per V/m, and
$0.5$~V/m per tone, it has magnitude $1.36~\mu$V; the steady equivalent
is nearly identical. Reducing the assumed coupling to $0.15$ scales these
sources by $0.09$. Thus the matched-polarization $2$--$5\%$ comparison does
not carry over unchanged to matched applied fields.

At equal fields, the $0.2$~ms point-membrane model predicts a narrowband
$9/1$~kHz source ratio of $0.020$. The limit $1/81$ applies only when
both bands lie above their access corners. A sealed long cable instead
approaches a $1/9$ ratio. These calculations locate conditional input budgets;
they do not calibrate the biological transfer.

**Proposed**

With an explicit first-order access state per modeled compartment before
the sigmoid and an assumed $\tau=0.2$~ms, the full JR column demodulates and
resonates (Fig.~\ref{fig:khz_direct}a). Genuine tones centered at $2$~kHz
generate the $10.914$~Hz beat absent from the input, with analytic access
factor $|H_m|^2=0.137$ (Fig.~\ref{fig:khz_twotone}). Both results follow
from the assumed access time and coupling, which the simulation does not
calibrate.

Figure~\ref{fig:feasibility} converts this access assumption into a source
budget. With $\varepsilon_j=\lambda_0 E_j|H_m(\omega_j)|$, the equivalent
direct beat input before recurrent gain is $\varepsilon_{\rm eq}=Y_\Omega/\Sig'$.
At $2$~kHz, $\tau_m=0.2$~ms, $\lambda_0=0.5$~mV per V/m, and $0.5$~V/m per
tone, its magnitude is $1.36~\mu$V, and the steady equivalent is nearly
identical. Reducing the assumed coupling to $0.15$ scales both sources by
$0.09$, so the matched-polarization $2$--$5\%$ comparison does not
carry over unchanged to matched applied fields.

At equal fields, the $0.2$~ms point membrane predicts a narrowband source
ratio of $0.020$ between $9$ and $1$~kHz. The limit $1/81$ applies only
when both bands lie above their access corners; a sealed long cable instead
approaches $1/9$. These calculations locate conditional input
budgets but do not calibrate the biological transfer.

*Script: claim-strength changes ['neither -1', 'not +1']; quantity changes ({}, {}, True)*

## Pair 5

**Original**

\subsection{Sigmoid curvature predicts the JR beat source}\label{sec:results-curvature}
The signed open-loop beat follows $\half\Sig''(v^*)\varepsilon^2m$, vanishing
and reversing phase at the inflection (Fig.~\ref{fig:opp}). The closed-loop
examples occupy the negative-curvature flank. At matched network
susceptibility, either flank follows the same gain law, with opposite source
phase when the curvature changes sign.

**Proposed**

\subsection{Sigmoid curvature predicts the JR beat source}\label{sec:results-curvature}
The signed open-loop beat follows $\half\Sig''(v^*)\varepsilon^2m$, vanishing
and reversing phase at the inflection (Fig.~\ref{fig:opp}). The
closed-loop examples lie on the negative-curvature flank. At matched network
susceptibility, either flank obeys the same gain law, with opposite source
phase when the curvature changes sign.

*Script: claim-strength changes none; quantity changes ({}, {}, False)*

## Pair 6

**Original**

In the recurrent column, the response scales quadratically at small drive
(log--log slope $1.99$, measured as in \S\ref{sec:transduction-methods}),
and linearizing the field-receiving sigmoid reduces it
from $1.34$ to $0.0021$~mV (Fig.~\ref{fig:opp}b,c). The open-loop surrogate
comparison in panel~(d) supports its use for leading-order beat sweeps, with
the waveform and near-Hopf limitations specified in \S\ref{sec:waveforms}.

\subsection{Realistic-head comparison of envelope and quadratic maps}\label{sec:fem-results}
In this single-subject geometric illustration, changing the current ratio
moves the envelope and mean-square ROI centroids in opposite directions,
while the quadratic beat map only rescales. Each centroid uses the top 10\%
of hippocampal nodes; it is not a whole-brain maximum.
Figure~\ref{fig:fem} compares the maps of Table~\ref{tab:transduction-maps}
for the Violante montage in IXI002, using the same polarizations and fixed
1:1 projection (\S\ref{sec:fem-methods}).

**Proposed**

In the recurrent column, the response scales quadratically at small drive
(log--log slope $1.99$, measured as in \S\ref{sec:transduction-methods}),
and linearizing the field-receiving sigmoid reduces it from $1.34$
to $0.0021$~mV (Fig.~\ref{fig:opp}b,c). The open-loop two-tone/AM
comparison in panel~(d) supports the surrogate for leading-order
beat sweeps, within the waveform and near-Hopf limitations of
\S\ref{sec:waveforms}.

\subsection{Beat maps rescale while envelope foci move}\label{sec:fem-results}
In this single-subject geometric illustration, changing the current ratio
moves the envelope and mean-square ROI centroids in opposite directions,
while the quadratic beat map only rescales. Each centroid uses the top 10\%
of hippocampal nodes and is not a whole-brain maximum.
Figure~\ref{fig:fem} compares the maps of Table~\ref{tab:transduction-maps}
for the Violante montage in IXI002, using the same polarizations and fixed
1:1 projection (\S\ref{sec:fem-methods}).

*Script: claim-strength changes none; quantity changes ({}, {}, False)*

## Pair 7

**Original**

The pair-current product falls from $4$ to $3$~mA$^2$, so both beat maps fall to $75\%$ at every node, to machine precision, with unchanged normalized patterns, contrasts, and foci. The envelope focus moves toward the pair whose current falls; the mean-square focus moves toward the pair whose current rises. For the contrast comparison at balance, degree matching reduces the quadratic contrast to $1.08$, below the envelope's $1.22$; the isotropic beat gives $1.18$ ($1.08$ degree-matched). The envelope's anterolateral tail above the reference p95 is 52\% white matter, against 25\% in the ROI. Restricting the ROI to gray matter removes the beat preference: only the envelope exceeds one at 1:1, and no map does at 1:3 (Table~\ref{tab:fem-summary}). No mean-based contrast exceeds one. These geometric contrasts do not establish physiological deep selectivity, which also depends on detector and circuit weighting.

The envelope contrast peaks at $1.24$ near balance. Once one carrier becomes
weaker across most of the ROI, further imbalance changes amplitude more than
focus; the mean-square focus moves continuously. Across all 32 combinations
of montage, label, tissue definition, and focus fraction, the envelope shift
remains anterior, the mean-square shift posterior, and the quadratic shift
zero. Radial projections preserve these directions but change contrasts more
than the atlas label does (supplement, \S\ref{supp:fem-sensitivities}).

A laminar-aligned detector samples median fractions $0.29$, $0.11$, and $0.12$ of the envelope, quadratic, and mean-square maps' respective orientation maxima. Evaluated on 934 of 1,568 ROI nodes, these fractions quantify the anatomical access hypothesis (supplement, \S\ref{supp:fem-orientation}). The median ratios of projected maps across the tissue interfaces are $1.13$--$1.34$; mesh convergence remains untested (supplement, \S\ref{supp:fem-interfaces}).
\ifjne\else
\input{planning/parts/fem_sensitivities}
\input{planning/parts/fem_orientation}
\input{planning/parts/fem_interfaces}
\fi

\subsection{JR gain, mean shifts, and the tACS comparison}\label{sec:jcurve}
For the AM surrogate, pinning $v^*=8.30$~mV through $p(C)$ fixes the curvature and open-loop
beat $A_{\rm open}\simeq\half|\Sig''(v^*)|\varepsilon^2m$.
As $C\to C^*\approx137$, damping tends to zero, the response grows about
$30$-fold, and resonance sharpens (Fig.~\ref{fig:jcurve}a,b).
This isolates a network effect: recurrent transfer changes at fixed detector curvature.
The rate-to-voltage gain $A_\Omega/A_{\rm open}$ (mV\,s) follows
$1/\gamma$ before saturating (panel~c). Approaching the Hopf through $p$
gives similar leading scaling. Finite-distance gains can differ because
modal frequencies and input--output projections vary along each path.

**Proposed**

The beat maps scale with the pair-current product, which falls from $4$ to
$3$~mA$^2$, so both fall to $75\%$ at every node, to machine precision, with
unchanged normalized patterns, contrasts, and foci. The envelope focus moves
toward the pair whose current falls, the mean-square focus toward the pair
whose current rises.

At balance, degree matching reduces the quadratic contrast to $1.08$, below
the envelope's $1.22$; the isotropic beat gives $1.18$ ($1.08$
degree-matched). The envelope's anterolateral tail above the reference p95
is 52\% white matter, against 25\% in the ROI. Restricting the ROI to gray
matter removes the beat preference: only the envelope exceeds one at 1:1,
and no map does at 1:3 (Table~\ref{tab:fem-summary}). No mean-based contrast
exceeds one. These geometric contrasts do not establish physiological deep
selectivity, which also depends on detector and circuit weighting.

Across all 32 combinations of montage, label, tissue definition, and focus
fraction, the envelope shift remains anterior, the mean-square shift
posterior, and the quadratic shift zero. Radial projections preserve these
directions but change contrasts more than the atlas label does (supplement,
\S\ref{supp:fem-sensitivities}). The envelope contrast peaks at $1.24$ near
balance; once one carrier becomes weaker across most of the ROI, further
imbalance changes amplitude more than focus, whereas the mean-square focus
moves continuously.

A laminar-aligned detector samples median fractions $0.29$, $0.11$, and
$0.12$ of the envelope, quadratic, and mean-square maps' respective
orientation maxima. Evaluated on 934 of 1,568 ROI nodes, these
fractions quantify the anatomical access hypothesis (supplement,
\S\ref{supp:fem-orientation}). Across the tissue interfaces, the median
ratios of projected maps are $1.13$--$1.34$; mesh convergence remains
untested (supplement, \S\ref{supp:fem-interfaces}).
\ifjne\else
\input{planning/parts/fem_sensitivities}
\input{planning/parts/fem_orientation}
\input{planning/parts/fem_interfaces}
\fi

\subsection{Recurrent gain is shared with tACS}\label{sec:jcurve}
For the AM surrogate, pinning $v^*=8.30$~mV through $p(C)$ fixes
the curvature and the open-loop beat
$A_{\rm open}\simeq\half|\Sig''(v^*)|\varepsilon^2m$. As $C\to C^*\approx137$, damping tends to zero, the response grows
about $30$-fold, and the resonance sharpens (Fig.~\ref{fig:jcurve}a,b).
This isolates a network effect: recurrent transfer changes at fixed detector
curvature. The rate-to-voltage gain $A_\Omega/A_{\rm open}$ (mV\,s) follows
$1/\gamma$ before saturating (panel~c). Approaching the Hopf through $p$
gives similar leading scaling, but finite-distance gains can
differ because modal frequencies and input--output projections vary along
each path.

*Script: claim-strength changes none; quantity changes ({}, {}, True)*

## Pair 8

**Original**

\paragraph{Beat modulation and mean rate.}\label{sec:timing}
With genuine two tones at $\Delta f=f_0$, the same pinned sweep
increases modulation of $r_P=\Sig(v+s)$ by $13.2$-fold ($26$ to $339$~mHz),
following $1/\gamma$ before saturation. The same rate's mean shift grows
$4.4$-fold ($-1.8$ to $-7.7$~mHz), remaining below $0.2\%$ of its
$3.9$~Hz baseline (Fig.~\ref{fig:timing}). Their magnitude ratio rises
from $14.5$ to $58$ near $\gamma=1$~s$^{-1}$, then falls to $44$ as
the amplified oscillation rectifies. In this weakly driven regime, a small
mean change accompanies larger beat modulation, consistent with primate observations
\cite{vieira2024}, with both compared in rate units. The surrogate
comparison is supplementary (\S\ref{supp:waveform-checks}).

The detector's steady and beat sources meet different transfers:
$|G(\omega_0)|\propto1/(2\gamma\omega_0)$ grows toward the Hopf, while
$|G(0)|\propto1/(\omega_0^2+\gamma^2)$ stays finite. The amplified beat
also rectifies, adding a mean shift quadratic in its amplitude that can
grow as $1/\gamma^2$ before saturation. A bounded zero-frequency transfer
therefore does not bound the full mean shift.

\paragraph{Comparison with tACS.}\label{sec:tacs-results}
TI and tACS share the linear amplifier, so matching their generated in-band
drives at a common state matches their linear outputs; resonance alone gives
TI no efficiency advantage.
For the AM surrogate with amplitude $\varepsilon_{\rm TI}$ and modulation depth
$m$, and a tACS input of amplitude $\varepsilon_{\rm tACS}$, the ratio of voltage
lock-in amplitudes in linear response is
\[
\mathcal R_{\rm lin}
=\frac{|\Sig''(v^*)|\,\varepsilon_{\rm TI}^2m}
{2\Sig'(v^*)\,\varepsilon_{\rm tACS}}.
\]
The common linear transfer cancels, giving a predicted ratio of $0.143$ for the original unequal-input comparison. Genuine two-tone responses depart from this prediction near the Hopf. When the leading sources are matched instead, the TI/tACS output ratios are $0.90$--$0.99$ at the three tested couplings. The larger direct input saturates earlier and shifts the operating state, which field-free pinning does not cancel. Numerical controls for these unequal-input comparisons are in the supplement (\S\ref{supp:tacs-saturation}). Equal-per-carrier, total-peak, and RMS matching are distinguished in \S\ref{sec:direct-comparison}.

**Proposed**

\paragraph{Beat modulation outgrows mean shift.}\label{sec:timing}
With genuine two tones at $\Delta f=f_0$, the same pinned sweep increases
the beat modulation of $r_P=\Sig(v+s)$ $13.2$-fold
($26$ to $339$~mHz), following $1/\gamma$ before saturation. The same rate's
mean shift grows $4.4$-fold ($-1.8$ to $-7.7$~mHz), remaining below
$0.2\%$ of its $3.9$~Hz baseline (Fig.~\ref{fig:timing}). Their
magnitude ratio rises from $14.5$ to $58$ near $\gamma=1$~s$^{-1}$,
then falls to $44$ as the amplified oscillation rectifies. In this weakly
driven regime, with both compared in rate units, a small mean change
accompanies larger beat modulation, consistent with primate observations
\cite{vieira2024}. The surrogate comparison is supplementary
(\S\ref{supp:waveform-checks}).

A finite zero-frequency transfer does not bound the full mean shift. The
detector's beat and steady sources meet different transfers:
$|G(\omega_0)|\propto1/(2\gamma\omega_0)$ grows toward the Hopf, while
$|G(0)|\propto1/(\omega_0^2+\gamma^2)$ stays finite. The amplified beat also rectifies, adding a mean shift quadratic in
its amplitude that can grow as $1/\gamma^2$ before saturation.

\paragraph{TI and tACS share the linear amplifier.}\label{sec:tacs-results}
Matching the in-band drives that TI and tACS generate at a common state
matches their linear outputs, so resonance alone gives TI no efficiency
advantage. For the AM surrogate with amplitude $\varepsilon_{\rm TI}$ and
modulation depth $m$, and a tACS input of amplitude $\varepsilon_{\rm tACS}$,
the ratio of voltage lock-in amplitudes in linear response is
\[
\mathcal R_{\rm lin}
=\frac{|\Sig''(v^*)|\,\varepsilon_{\rm TI}^2m}
{2\Sig'(v^*)\,\varepsilon_{\rm tACS}}.
\]
The common linear transfer cancels, giving a predicted ratio of $0.143$ for
the original unequal-input comparison. Genuine two-tone responses depart
from this prediction near the Hopf. When the leading sources are matched
instead, the TI/tACS output ratios are $0.90$--$0.99$ at the three tested
couplings. The larger direct input saturates earlier and shifts the
operating state, which field-free pinning does not cancel. Numerical
controls for these unequal-input comparisons are in the supplement
(\S\ref{supp:tacs-saturation}); \S\ref{sec:direct-comparison}
distinguishes equal-per-carrier, total-peak, and RMS matching.

*Script: claim-strength changes none; quantity changes ({}, {}, False)*

## Pair 9

**Original**

\subsection{PING amplifies the dynamic QIF beat source}\label{sec:nmm2-results}
With genuine $300$~Hz tones entering E current, the PING rate $r_E$
shows forced gamma resonance below the Hopf and a beat response superposed
on autonomous gamma above it (Fig.~\ref{fig:nmm2_res}).
The resonance grows through the Hopf and shifts with state, forming a diagonal
ridge in the $(\Delta f,\bar\eta)$ plane of Fig.~\ref{fig:nmm2_map}, unlike
the JR example \cite{clusella2023}.

At $300$~Hz, voltage excursions mix through $v_E^2$ on the fast side of
the detector's crossover (Fig.~\ref{fig:crossover}a). Each current tone
produces a voltage phasor $I_j/(i\omega_j\tau_E)$, giving a beat source
$I_1I_2/(\tau_E^2\omega_1\omega_2)$ in the equation for $\tau_E\dot v_E$.
After division by $\tau_E$ and propagation through the network transfer at
$\Omega$, it matches the full second-order response at four stable operating
points within $1.1\%$ at $300$~Hz, $0.1\%$ at $1$~kHz, and $0.03\%$
at $2$~kHz (Fig.~\ref{fig:crossover}b).

The unpinned PING coupling sweep also approaches a gamma Hopf, but two
modes compete for the response peak. Near the Hopf, the critical mode's
linear gain has a fitted damping exponent of $1.02$, consistent with the
$1/\gamma$ law; the full-sweep exponent is $0.71$. At finite amplitude the response departs from the linear
reference and saturates, while the driven endpoint remains attracting.
The mode tracking, amplitude checks, and their numerical ranges accompany
the coupling curve in the supplement (\S\ref{supp:ping-coupling-results}).
Thus JR and PING share the critical mode's $1/\gamma$ gain law despite
their different detectors; the law does not describe every mode or the
entire finite-amplitude sweep.

**Proposed**

\subsection{PING amplifies the dynamic QIF beat source}\label{sec:nmm2-results}
With genuine $300$~Hz tones entering the excitatory current, the PING rate
$r_E$ shows forced gamma resonance below the Hopf and a beat response
superposed on autonomous gamma above it (Fig.~\ref{fig:nmm2_res}). The
resonance grows through the Hopf and shifts with state, forming a diagonal
ridge in the $(\Delta f,\bar\eta)$ plane of Fig.~\ref{fig:nmm2_map}, unlike
the JR example \cite{clusella2023}.

At $300$~Hz, voltage excursions mix through $v_E^2$ on the fast side of the
detector's crossover (Fig.~\ref{fig:crossover}a). Each current tone produces
a voltage phasor $I_j/(i\omega_j\tau_E)$, giving a beat
source $I_1I_2/(\tau_E^2\omega_1\omega_2)$ in the equation for
$\tau_E\dot v_E$. Divided by $\tau_E$ and propagated through the network
transfer at $\Omega$, this source matches the full second-order response at
four stable operating points within $1.1\%$ at $300$~Hz, $0.1\%$ at
$1$~kHz, and $0.03\%$ at $2$~kHz (Fig.~\ref{fig:crossover}b).

JR and PING share the critical mode's $1/\gamma$ gain law despite their
different detectors, but the law does not describe every mode or the entire
finite-amplitude sweep. The unpinned PING coupling sweep also approaches a
gamma Hopf, with two modes competing for the response peak. Near the Hopf,
the critical mode's linear gain has a fitted damping exponent of $1.02$,
consistent with the $1/\gamma$ law; the full-sweep exponent is $0.71$. At
finite amplitude the response departs from the linear reference and
saturates, while the driven endpoint remains attracting. The supplement
gives the mode tracking, amplitude checks, and their numerical ranges with
the coupling curve (\S\ref{supp:ping-coupling-results}).

*Script: claim-strength changes none; quantity changes ({}, {}, True)*

## Pair 10

**Original**

\subsection{QIF responses distinguish beat modulation from field-induced gamma}\label{sec:qif}
The finite QIF network shows beat-locked modulation at the lower tested
amplitude and field-induced gamma at the higher amplitude. Its $8000$-neuron populations test
these regimes at the spike level
\cite{montbrio2015,ruffini2025rosetta,clusella2023}
(Figs.~\ref{fig:qif_raster},~\ref{fig:qif_regimes}).

At $\bar\eta=0.85$ and $A_f=10$, the original finite-cutoff run gives
beat depth $0.09$ and a $2.8\%$ mean-rate increase. Its quantitative depth
remains unconverged because of cutoff and population sensitivity (supplement,
\S\ref{app:qif-checks}--\ref{supp:theta-pilot}). The estimated rectified
E-drive shift remains below $\delta\eta_E^*$, the shift in excitatory drive
required to cross the Hopf while holding the inhibitory drive fixed.
At $\bar\eta=1.5$, the original finite-cutoff run gives a $42$~Hz depth
of about $0.02$ and a $1.6\%$ mean-rate increase, while ongoing gamma dominates.

At $A_f=35$ and $\bar\eta=0.85$, a line near $52$~Hz dominates
(depth $0.70$), alongside the $55$~Hz beat (depth $0.29$). This is a
finite-amplitude example: carrier averaging predicts that the rectified
E-drive shift exceeds $\delta\eta_E^*$ and destabilizes the averaged equilibrium.
Direct mean-field integration reproduces the off-beat line, identifying the
dominant response as field-induced gamma (Fig.~\ref{fig:qif_raster}b).
The drive and stability estimates at both amplitudes are given in the
supplement (\S\ref{app:qif-estimate}).

At $\bar\eta=1.5$, autonomous gamma near $53$--$54$~Hz remains about
four times larger than the $42$~Hz beat component (Fig.~\ref{fig:qif_raster}d).
Their coexistence produces slower burst-height variations. Mixing produces
sidebands near $95$ and $11$~Hz, as in endogenous amplitude modulation
\cite{ruffini2025ham}; these establish nonlinear mixing without distinguishing
gamma-amplitude gating from phase modulation (Fig.~\ref{fig:qif_timing}b).
Field-free gamma frequencies agree between the finite network and mean field
(Fig.~\ref{fig:qif_timing}a).

To separate steady induction from beat-dependent activity, we compare TI
with an unmodulated carrier matched in RMS input current, in model units
(Fig.~\ref{fig:qif_regimes}c,d). In the mean field, their rectified E-drive
shifts agree within $3\%$ and their mean-rate increases are similar.
At $A_f=35$, both induce gamma near $51$~Hz; TI also produces the
$55$~Hz beat. At $A_f=10$, neither induces gamma, and TI alone produces
a resolved beat response. This control has been tested only in the mean
field; its spectral-leakage check is in the supplement
(\S\ref{supp:qif-protocol}).

**Proposed**

\subsection{QIF responses distinguish beat modulation from field-induced gamma}\label{sec:qif}
The finite QIF network shows beat-locked modulation at the lower tested
amplitude and field-induced gamma at the higher one. Its $8000$-neuron
populations test these regimes at the spike level
\cite{montbrio2015,ruffini2025rosetta,clusella2023}
(Figs.~\ref{fig:qif_raster},~\ref{fig:qif_regimes}).

At $\bar\eta=0.85$ and $A_f=10$, the original finite-cutoff run gives beat
depth $0.09$ and a $2.8\%$ mean-rate increase. Its quantitative
depth remains unconverged because it depends on cutoff and population size
(supplement, \S\ref{app:qif-checks}--\ref{supp:theta-pilot}). The estimated
rectified E-drive shift remains below $\delta\eta_E^*$, the shift in
excitatory drive required to cross the Hopf while holding the inhibitory
drive fixed. At $\bar\eta=1.5$, the original finite-cutoff run gives a
$42$~Hz depth of about $0.02$ and a $1.6\%$ mean-rate increase, while
ongoing gamma dominates.

At $A_f=35$ and $\bar\eta=0.85$, a line near $52$~Hz dominates (depth
$0.70$), alongside the $55$~Hz beat (depth $0.29$). In this finite-amplitude
example, carrier averaging predicts that the rectified E-drive shift exceeds
$\delta\eta_E^*$ and destabilizes the averaged equilibrium. Direct
mean-field integration reproduces the off-beat line, identifying the
dominant response as field-induced gamma (Fig.~\ref{fig:qif_raster}b). The
supplement gives the drive and stability estimates at both amplitudes
(\S\ref{app:qif-estimate}).

At $\bar\eta=1.5$, autonomous gamma near $53$--$54$~Hz remains about four
times larger than the $42$~Hz beat component (Fig.~\ref{fig:qif_raster}d),
and their coexistence produces slower burst-height variations. Mixing
produces sidebands near $95$ and $11$~Hz, as in endogenous amplitude
modulation \cite{ruffini2025ham}; these establish nonlinear mixing without
distinguishing gamma-amplitude gating from phase modulation
(Fig.~\ref{fig:qif_timing}b). Field-free gamma frequencies agree between the
finite network and mean field (Fig.~\ref{fig:qif_timing}a).

An unmodulated carrier matched to TI in RMS input current, in model units,
separates steady induction from beat-dependent activity
(Fig.~\ref{fig:qif_regimes}c,d). In the mean field, their rectified E-drive
shifts agree within $3\%$, and their mean-rate increases
are similar. At $A_f=35$, both induce gamma near $51$~Hz and TI also
produces the $55$~Hz beat; at $A_f=10$, neither induces gamma, and TI alone
produces a resolved beat response. This control has been tested only in the
mean field; its spectral-leakage check is in the supplement
(\S\ref{supp:qif-protocol}).

*Script: claim-strength changes none; quantity changes ({}, {}, False)*

## Pair 11

**Original**

At $A_f=35$, population beat modulation exceeds the relative mean-rate
change by about threefold. Across the two conditions, mean rate rises
$8$--$11\%$, while beat depth rises from below $0.003$ to $0.29$
($\bar\eta=0.85$) and $0.23$ ($\bar\eta=1.5$)
(Fig.~\ref{fig:qif_timing}c). Individual locking remains weak: median
pairwise phase consistency rises from $-0.02$ in the field-free control
to $0.003$--$0.005$, and pooled vector strength from below $0.02$ to
$0.12$--$0.13$. Many weakly biased cells therefore produce a population
beat component. These finite-amplitude results do not establish its size
under weak physiological stimulation.

**Proposed**

At $A_f=35$, population beat modulation exceeds the relative mean-rate
change by about threefold. Across the two conditions, mean rate rises
$8$--$11\%$, while beat depth rises from below $0.003$ to $0.29$
($\bar\eta=0.85$) and $0.23$ ($\bar\eta=1.5$) (Fig.~\ref{fig:qif_timing}c).
Individual neurons lock weakly: median pairwise phase consistency rises from
$-0.02$ in the field-free control to $0.003$--$0.005$, and pooled vector
strength from below $0.02$ to $0.12$--$0.13$. Many weakly biased cells
therefore produce a population beat component. These finite-amplitude
results do not establish its size under weak physiological stimulation.

*Script: claim-strength changes none; quantity changes ({}, {}, False)*
