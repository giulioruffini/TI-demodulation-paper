# Pairs: methods

## Pair 1

**Original**

\paragraph{Response terminology.}\label{sec:vocab-methods}
A \emph{forced response} is the beat-driven component measured by lock-in; a purely
forced regime requires stability under stimulation. \emph{Entrainment} means
frequency and phase capture of a self-sustained oscillator \cite{pikovsky2001}.
Our frequency-dominance screen does not establish that capture. \emph{Gating}
means modulation of a persisting rhythm's amplitude \cite{canolty2010,tort2010};
a rate fold alone does not establish it. Detailed criteria are in the supplement
(\S\ref{sec:vocab}).

\subsection{Stimulation waveforms and matched-source controls}\label{sec:waveforms}
Dense perturbative sweeps use the
three-line waveform
\begin{equation}
s(t)=\varepsilon\,[\,1+m\cos\Omega t\,]\cos\omega_c t,\qquad \omega_c=2\pi f_c ,
\label{eq:amsur}
\end{equation}
with dimensionless modulation depth $m$. This AM surrogate parameterizes dense resonance and coupling sweeps by one amplitude. It contains a central carrier line absent from genuine TI, but matches its leading beat source: $Y_\Omega=\half\Sig''\varepsilon^2m$. For matched genuine tones, $\mathrm{LPF}[s^2]=\varepsilon^2(1+\cos\Omega t)$; for the $m=1$ surrogate, $\mathrm{LPF}[s^2]=\varepsilon^2(\tfrac34+\cos\Omega t+\tfrac14\cos2\Omega t)$. Thus the mean source differs, and the surrogate adds a second harmonic at $25\%$ of the fundamental.

We use genuine tones for the demodulation, curvature, square-law, laminar, and kHz demonstrations. We also use them wherever mean shifts or harmonics enter the comparison, including timing versus rate and the TI/tACS and NMM2 endpoint controls. Open-loop agreement at the beat is checked at one operating point; it does not imply equal driven operating states.

**Proposed**

\paragraph{Response terminology.}\label{sec:vocab-methods}
A \emph{forced response} is the beat-driven component measured by lock-in
(Eq.~\eqref{eq:lockin}); a purely forced regime requires stability under
stimulation. \emph{Entrainment} means frequency and phase capture of a self-sustained
oscillator \cite{pikovsky2001}, which our frequency-dominance screen does not
establish. \emph{Gating} means modulation of a persisting rhythm's amplitude
\cite{canolty2010,tort2010}, which a rate fold alone does not establish. Detailed criteria
are in the supplement (\S\ref{sec:vocab}).

\subsection{Stimulation waveforms and matched-source controls}\label{sec:waveforms}
Dense perturbative sweeps use the three-line waveform
\begin{equation}
s(t)=\varepsilon\,[\,1+m\cos\Omega t\,]\cos\omega_c t,\qquad \omega_c=2\pi f_c ,
\label{eq:amsur}
\end{equation}
with dimensionless modulation depth $m$. This AM surrogate parameterizes dense resonance
and coupling sweeps by one amplitude. It contains a central carrier line absent from
genuine TI but matches its leading beat source, $Y_\Omega=\half\Sig''\varepsilon^2m$.
For matched genuine tones $\mathrm{LPF}[s^2]=\varepsilon^2(1+\cos\Omega t)$, whereas for
the $m=1$ surrogate
$\mathrm{LPF}[s^2]=\varepsilon^2(\tfrac34+\cos\Omega t+\tfrac14\cos2\Omega t)$, so the
surrogate changes the mean source and adds a second harmonic at $25\%$ of the
fundamental.

Genuine tones are used for the demodulation, curvature, square-law, laminar, and kHz
demonstrations, and wherever mean shifts or harmonics enter the comparison, including
timing versus rate and the TI/tACS and NMM2 endpoint controls. Open-loop agreement at
the beat is checked at one operating point and does not imply equal driven operating
states.

*Script: claim-strength changes none; quantity changes ({}, {}, False)*

## Pair 2

**Original**

A software lock-in projects $v$ onto sine and cosine at $\Omega$.
The finite window suppresses, but does not eliminate, neighboring frequencies.
For Hann weights $w_k$, sample times $t_k$, voltages $v_k=v(t_k)$, and
weighted mean $\bar v=\sum_k w_kv_k/\sum_k w_k$, the quadratures are
\begin{equation}
\begin{gathered}
L_{\cos}=\frac{2}{\sum_k w_k}\sum_k w_k\,(v_k-\bar v)\cos\Omega t_k,\quad
L_{\sin}=\frac{2}{\sum_k w_k}\sum_k w_k\,(v_k-\bar v)\sin\Omega t_k,\\
A_\Omega=\sqrt{L_{\cos}^2+L_{\sin}^2},
\end{gathered}
\label{eq:lockin}
\end{equation}
where $k$ indexes samples. A test tone
$v=A_{\rm test}\cos(\Omega t+\theta_0)$ with amplitude $A_{\rm test}$
and phase $\theta_0$ gives
$(L_{\cos},L_{\sin})\to A_{\rm test}(\cos\theta_0,-\sin\theta_0)$
over long windows. Thus $A_\Omega$ returns physical amplitude, twice the
Fourier-coefficient magnitude. Mean subtraction suppresses leakage from
the larger baseline (supplement, \S\ref{supp:lockin}).

**Proposed**

A software lock-in projects the readout $v$ onto sine and cosine at $\Omega$; its
finite window suppresses, but does not eliminate, neighboring frequencies. For Hann
weights $w_k$, sample times $t_k$, voltages $v_k=v(t_k)$, and weighted mean
$\bar v=\sum_k w_kv_k/\sum_k w_k$, the quadratures are
\begin{equation}
\begin{gathered}
L_{\cos}=\frac{2}{\sum_k w_k}\sum_k w_k\,(v_k-\bar v)\cos\Omega t_k,\quad
L_{\sin}=\frac{2}{\sum_k w_k}\sum_k w_k\,(v_k-\bar v)\sin\Omega t_k,\\
A_\Omega=\sqrt{L_{\cos}^2+L_{\sin}^2},
\end{gathered}
\label{eq:lockin}
\end{equation}
where $k$ indexes samples. Over long windows, a test tone
$v=A_{\rm test}\cos(\Omega t+\theta_0)$ with amplitude $A_{\rm test}$
and phase $\theta_0$ gives
$(L_{\cos},L_{\sin})\to A_{\rm test}(\cos\theta_0,-\sin\theta_0)$,
so $A_\Omega$ returns physical amplitude, twice the Fourier-coefficient magnitude.
Mean subtraction suppresses leakage from the larger baseline (supplement,
\S\ref{supp:lockin}).

*Script: claim-strength changes none; quantity changes ({}, {}, False)*

## Pair 3

**Original**

A detector comparison requires both harmonics over the same settled window,
with their amplitude ratio corrected by $|G(2\Omega)/G(\Omega)|$.
Estimating a mixture coefficient through Eq.~\eqref{eq:rdet} assumes the mixed
detector family and its sign branch.

\subsection{Head model and field computation}\label{sec:fem-methods}
\ifjne
We compute maps in IXI002, an open-access T1-weighted MRI of a 35-year-old
woman, using the hippocampal montage of Violante et al.\ \cite{violante2023}.
The six-tissue SimNIBS conductor is quasi-static with no kHz dispersion correction
\cite{salvador2025}. Pair fields are solved once and scaled to peak currents
summing to $4$~mA: $2+2$~mA for 1:1 and $1+3$~mA for 1:3. The posterior share
is swept from $0.1$ to $0.9$. Conductivities, electrodes, solver settings,
and sensitivity protocols are in the supplement (\S\ref{supp:fem-protocol}).

Local polarization is $\varepsilon_j=\lambda_0 I_j^{\rm pair}\mathbf F_j\cdot\mathbf n$
with uniform $\lambda_0=0.5$~mV per V/m \cite{radman2009} and field per unit
current $\mathbf F_j$. This coupling sets absolute amplitudes but cancels from
normalized maps, focus positions, and target-to-reference ratios. It is an
assumed field-to-polarization conversion, not a measured AIS transfer.

At each node, $\mathbf n$ maximizes the envelope at 1:1 and is then held fixed
for every ratio and every map. This geometric direction need not match a cell's
orientation. Radial, laminar, and isotropically averaged projections provide
sensitivity comparisons (supplement, \S\ref{supp:fem-sensitivities} and \S\ref{supp:fem-orientation}); the latter averages the signed beat before taking its magnitude,
allowing cancellation across orientations.

The target is the left hippocampus segmented with FreeSurfer (1,568 gray- and
white-matter nodes). The reference comprises 273,544 gray-matter nodes outside
that ROI, including other deep gray matter. The target-to-reference contrast
is the ROI 95th percentile divided by the reference 95th percentile; the
mean-based companion replaces the numerator by the ROI mean. Nodes receive
equal weight. Square roots of second-order maps provide degree-matched geometric
contrasts; the raw maps remain the detector predictions before gain.

The focus is the centroid of the top 10\% of ROI nodes ranked by each map.
Displacement is measured along the hippocampal long axis, with anterior positive.
Sensitivity checks vary montage, atlas label, gray/white-matter inclusion,
focus fraction, and orientation. These geometric maps precede detection and
recurrence: $Y_{\rm DC}=\Sig''(v^*)\mathcal I/2$ is a signed rescaling only
for uniform curvature. The head model does not specify the operating states.

**Proposed**

Comparing detectors requires both harmonics over the same settled window, with their
amplitude ratio corrected by $|G(2\Omega)/G(\Omega)|$. Estimating a mixture coefficient
through Eq.~\eqref{eq:rdet} assumes the mixed detector family and its sign branch.

\subsection{Head model and field computation}\label{sec:fem-methods}
\ifjne
Maps are computed in IXI002, an open-access T1-weighted MRI of a 35-year-old
woman, with the hippocampal montage of Violante et al.\ \cite{violante2023}.
The six-tissue SimNIBS conductor is quasi-static, without kHz dispersion correction
\cite{salvador2025}. Each pair's field is solved once and scaled to peak currents
summing to $4$~mA, $2+2$~mA for 1:1 and $1+3$~mA for 1:3, and the posterior share is
swept from $0.1$ to $0.9$. Conductivities, electrodes, solver settings, and sensitivity
protocols are in the supplement (\S\ref{supp:fem-protocol}).

Local polarization is $\varepsilon_j=\lambda_0 I_j^{\rm pair}\mathbf F_j\cdot\mathbf n$,
with field per unit current $\mathbf F_j$ and uniform $\lambda_0=0.5$~mV per V/m
\cite{radman2009}. This assumed field-to-polarization conversion, not a measured AIS
transfer, sets absolute amplitudes but cancels from normalized maps, focus positions,
and target-to-reference ratios.

At each node, the unit vector $\mathbf n$ maximizes the envelope at 1:1 and is held
fixed for every ratio and map; this geometric direction need not match a cell's
orientation. Radial, laminar, and isotropically averaged projections provide
sensitivity comparisons (supplement, \S\ref{supp:fem-sensitivities} and
\S\ref{supp:fem-orientation}); the isotropic average is taken over the signed beat before its
magnitude, allowing cancellation across orientations.

The target region of interest (ROI) is the left hippocampus segmented with FreeSurfer
(1,568 gray- and white-matter nodes). The reference comprises 273,544 gray-matter nodes
outside it, including other deep gray matter. The
target-to-reference contrast divides the ROI 95th percentile by the reference 95th
percentile, and the mean-based companion uses the ROI mean as numerator.
Nodes receive equal weight. Square roots of
second-order maps give degree-matched geometric contrasts; the raw maps remain the
detector predictions before gain.

The focus is the centroid of the top 10\% of ROI nodes ranked by each map, and
displacement is measured along the hippocampal long axis, anterior positive.
Sensitivity checks vary montage, atlas label, gray/white-matter inclusion, focus
fraction, and orientation. These geometric maps precede detection and recurrence:
$Y_{\rm DC}=\Sig''(v^*)\mathcal I/2$ is a signed rescaling only for uniform
curvature. The head model does not specify the operating states.

*Script: claim-strength changes ['every -1', 'no -1', 'without +1']; quantity changes ({}, {}, False)*

## Pair 4

**Original**

\subsection{Single-column Jansen--Rit: integration, lock-in, and controls}\label{sec:jr-methods}
We integrate the JR column as six first-order ordinary differential equations. The TI field enters only the pyramidal output sigmoid, Eq.~\eqref{eq:jr0},
as $s$, while the readout $v=y_1-y_2$ contains only synaptic potentials.
A beat in this readout must therefore have passed through the nonlinearity
and the recurrent loop. Unless stated otherwise $f_c=100$~Hz and $m=1$.

Integration uses fixed-step fourth-order Runge--Kutta (RK4), with time steps
chosen for each carrier band. Halving each step changes the reported lock-in
amplitudes by less than $1\%$. The resonance sweep settles for $10$~s and measures
for $20$~s; run-specific steps and windows are listed in the supplement
(\S\ref{supp:jr-runs}). The quoted $10$~kHz attenuation is analytic, not simulated.
\ifjne\else
\input{planning/parts/jr_runs}
\fi

Numerical continuation gives the fixed-point and limit-cycle branches in
Fig.~\ref{fig:bif}. Independently solving the resting fixed point and tracking
the leading pair of its $6\times6$ Jacobian locates the upper Hopf at
$p_H\approx315.70$~s$^{-1}$ and $f_0\approx11.16$~Hz, consistent with
\cite{grimbert2006}. For $p>p_H$ the fixed point is stable; the $11.1$~Hz
example drives it near resonance.

**Proposed**

\subsection{Single-column Jansen--Rit: integration, lock-in, and controls}\label{sec:jr-methods}
The JR column is integrated as six first-order ordinary differential equations. The TI
field enters only the pyramidal output sigmoid, Eq.~\eqref{eq:jr0}, as $s$, whereas
the readout $v=y_1-y_2$ contains only synaptic potentials, so any readout beat must
have passed through the nonlinearity and the recurrent loop. Unless stated otherwise,
$f_c=100$~Hz and $m=1$.

Integration uses fixed-step fourth-order Runge--Kutta (RK4), with steps chosen for each
carrier band; halving each step changes the reported lock-in amplitudes by less than
$1\%$. The resonance sweep settles for $10$~s and measures for $20$~s, and run-specific
steps and windows are in the supplement (\S\ref{supp:jr-runs}). The quoted $10$~kHz
attenuation is analytic, not simulated.
\ifjne\else
\input{planning/parts/jr_runs}
\fi

Numerical continuation gives the fixed-point and limit-cycle branches of
Fig.~\ref{fig:bif}. Independently solving the resting fixed point and tracking the
leading eigenvalue pair of its $6\times6$ Jacobian locates the upper Hopf at
$p_H\approx315.70$~s$^{-1}$ and $f_0\approx11.16$~Hz, consistent with
\cite{grimbert2006}. For $p>p_H$ the fixed point is stable, and the $11.1$~Hz example
drives it near resonance.

*Script: claim-strength changes ['any +1']; quantity changes ({}, {}, False)*

## Pair 5

**Original**

The open-loop sigmoid at fixed $v^*$ isolates detection; its signed lock-in
tests the curvature law. The closed-loop column measures recurrent gain over
an $(\Omega,p)$ grid. Controls test quadratic amplitude scaling on a well-damped
focus, abolition of the beat when the pyramidal sigmoid is replaced by its
tangent, and agreement of $\Sig'$ and $\Sig''$ with finite differences.
Field-free trajectories initialized near the fixed point check the continuation.

The coupling sweep holds detection fixed: for each $C$, we solve for the external
drive $p(C)$ that holds the field-free voltage at $v^*=8.30$~mV, then obtain damping and modal frequency
from the Jacobian. This fixes the background curvature without canceling
stimulation-induced mean shifts.

We use the AM surrogate for the gain sweep and genuine two tones to compare
modulation and mean of the same pyramidal rate
$r_P=\Sig(v+s)$. The tACS control uses a direct sinusoid at the same beat
frequency and reads the same voltage lock-in as TI. Further controls match
tACS to TI's generated beat source and repeat the comparison with longer
settling and measurement windows. Waveforms, amplitudes, and run windows
are recorded together in the supplement.

\subsection{Exact next-generation mean field (NMM2 PING)}\label{sec:nmm2-methods}
The pyramidal--interneuron network gamma (PING) circuit couples excitatory
and inhibitory MPR populations through second-order synapses
\cite{montbrio2015,ruffini2021nmm2,clusella2023}, using the Rosetta Stone
formulation shared with JR and laminar models \cite{ruffini2025rosetta}.
For population $X\in\{E,I\}$, $r_X$ is physical rate (ms$^{-1}$),
$v_X$ dimensionless mean voltage, and $\tau_X$ membrane time (ms).
With dots denoting physical-time derivatives,
\begin{equation}
\begin{aligned}
\tau_E\dot r_E&=\Delta/(\pi\tau_E)+2r_Ev_E, &\quad
\tau_E\dot v_E&=v_E^2+\bar\eta-(\pi\tau_E r_E)^2+\tau_E J\,(r_E^{\rm syn}-r_I^{\rm syn})+I_E,\\[2pt]
\tau_I\dot r_I&=\Delta/(\pi\tau_I)+2r_Iv_I, &\quad
\tau_I\dot v_I&=v_I^2+\bar\eta-(\pi\tau_I r_I)^2+\tau_I J\,(r_E^{\rm syn}-2r_I^{\rm syn}),
\end{aligned}
\label{eq:nmm2-ping}
\end{equation}
The synaptic rates $r_E^{\rm syn}=\hat K_a[r_E]$ and
$r_I^{\rm syn}=\hat K_g[r_I]$, with times $\tau_a$ and $\tau_g$,
obey the critically damped operator
$\tau_s^2\ddot r_{\rm syn}+2\tau_s\dot r_{\rm syn}+r_{\rm syn}=r$.
Here $J$ is dimensionless global gain; weights
$(w_{EE},w_{EI},w_{IE},w_{II})=(1,1,1,2)$ use target/source indices,
with doubled inhibitory self-coupling as the only asymmetry.
In the schematic, $\mathcal U_j$ denotes neuron $j$'s total synaptic
and field input, and $J^*$ the coupling-induced Hopf.

The background $\bar\eta$ controls a supercritical Hopf opening a gamma
cycle, analogous to the JR alpha Hopf. The field enters the E-voltage
equation as $I_E=\lambda_I E$ \cite{ruffini2021nmm2}.
The instantaneous coupling $\lambda_I$ has units of normalized drive per V/m;
two tones at $f_c\mp\Delta f/2$ have amplitude $A_f$ in the same
dimensionless drive units as $\bar\eta$. We set $f_c=300$~Hz and sweep
$\Delta f$ through gamma. The membrane integrates each tone into an
excursion $A_f/(\omega\tau_E)$, which $v_E^2$ rectifies: access uses
$\tau_m=\tau_E$, without an assumed sigmoid.

We integrate with fixed-step RK4 ($\Delta t=0.05$~ms) and read out the lock-in
(Eq.~\eqref{eq:lockin}) of $r_E$ at $\Delta f$ over the $(\Delta f, \bar\eta)$ plane.
Parameters (Rosetta Stone PING \cite{ruffini2025rosetta}): $\Delta=1$, global coupling
$J=15$, $\tau_E=15$, $\tau_I=7.5$, $\tau_a=10$, $\tau_g=2.5$~ms, with $\bar\eta$ swept
through the supercritical Hopf at $\bar\eta_H=1.110$ ($f_0=54.0$~Hz), located by bisection
on the leading eigenvalue of the mean-field Jacobian. The simulations retain these
finite membrane times; Eq.~\eqref{eq:slow_synapse} characterizes the fast-membrane limit.

The resonance map varies $\bar\eta$ (Fig.~\ref{fig:nmm2_map}); the
coupling sweep varies $J$ at fixed $\bar\eta$ toward $J^*$ and measures the
peak rate lock-in over $\Delta f$ (Fig.~\ref{fig:nmm2_jcurve}).
The $J^*$ Hopf is located by the same eigenvalue bisection.
Unlike JR, the PING coupling sweep does not pin the operating point. At
$\bar\eta=0$, continuation tracks the critical pair defining $\gamma$,
even when another mode dominates. The linear reference includes the
state-dependent source and full transfer; grids, amplitude checks, and
normalizations are supplementary (\S\ref{supp:ping-runs}).

**Proposed**

The open-loop sigmoid at fixed $v^*$ isolates detection, and its signed lock-in
tests the curvature law. The closed-loop column measures recurrent gain over an
$(\Omega,p)$ grid. Controls test quadratic amplitude scaling on a well-damped focus,
abolition of the beat when the pyramidal sigmoid is replaced by its tangent, and
agreement of $\Sig'$ and $\Sig''$ with finite differences. Field-free trajectories
started near the fixed point check the continuation.

The coupling sweep holds detection fixed. For each connectivity scale $C$, the
external drive $p(C)$ is solved to hold the field-free voltage at $v^*=8.30$~mV, and
damping and modal frequency follow from the Jacobian. This fixes the background
curvature without canceling stimulation-induced mean shifts.

The gain sweep uses the AM surrogate, while genuine two tones compare the modulation and
mean of the same pyramidal rate $r_P=\Sig(v+s)$. The tACS control applies a sinusoid
directly at the beat frequency and reads the same voltage lock-in as TI. Further
controls match tACS to the beat source TI generates and repeat the comparison with
longer settling and measurement windows. The supplement records waveforms, amplitudes,
and run windows together.

\subsection{Exact next-generation mean field (NMM2 PING)}\label{sec:nmm2-methods}
The pyramidal--interneuron network gamma (PING) circuit couples excitatory
and inhibitory MPR populations through second-order synapses
\cite{montbrio2015,ruffini2021nmm2,clusella2023}, in the Rosetta Stone
formulation shared with JR and laminar models \cite{ruffini2025rosetta}.
For population $X\in\{E,I\}$, $r_X$ is physical rate (ms$^{-1}$),
$v_X$ dimensionless mean voltage, and $\tau_X$ membrane time (ms).
With dots denoting physical-time derivatives,
\begin{equation}
\begin{aligned}
\tau_E\dot r_E&=\Delta/(\pi\tau_E)+2r_Ev_E, &\quad
\tau_E\dot v_E&=v_E^2+\bar\eta-(\pi\tau_E r_E)^2+\tau_E J\,(r_E^{\rm syn}-r_I^{\rm syn})+I_E,\\[2pt]
\tau_I\dot r_I&=\Delta/(\pi\tau_I)+2r_Iv_I, &\quad
\tau_I\dot v_I&=v_I^2+\bar\eta-(\pi\tau_I r_I)^2+\tau_I J\,(r_E^{\rm syn}-2r_I^{\rm syn}),
\end{aligned}
\label{eq:nmm2-ping}
\end{equation}
where the synaptic rates $r_E^{\rm syn}=\hat K_a[r_E]$ and
$r_I^{\rm syn}=\hat K_g[r_I]$, with times $\tau_a$ and $\tau_g$,
obey the critically damped operator
$\tau_s^2\ddot r_{\rm syn}+2\tau_s\dot r_{\rm syn}+r_{\rm syn}=r$.
The global gain $J$ is dimensionless, and the weights
$(w_{EE},w_{EI},w_{IE},w_{II})=(1,1,1,2)$, indexed target then source, make doubled
inhibitory self-coupling the only asymmetry. In the schematic, $\mathcal U_j$ denotes
neuron $j$'s total synaptic and field input, and $J^*$ the coupling-induced Hopf.

The background $\bar\eta$ controls a supercritical Hopf that opens a gamma cycle,
analogous to the JR alpha Hopf. The field enters the excitatory voltage equation as
$I_E=\lambda_I E$ \cite{ruffini2021nmm2}, with instantaneous coupling $\lambda_I$ in
normalized drive per V/m. The two tones, at $f_c\mp\Delta f/2$, have amplitude
$A_f$ in the dimensionless drive units of $\bar\eta$; $f_c=300$~Hz, and $\Delta f$
is swept through gamma. The membrane integrates each tone into an excursion
$A_f/(\omega\tau_E)$, which $v_E^2$ rectifies, so access uses $\tau_m=\tau_E$ without
an assumed sigmoid.

Integration uses fixed-step RK4 ($\Delta t=0.05$~ms), reading out the lock-in
(Eq.~\eqref{eq:lockin}) of $r_E$ at $\Delta f$ over the $(\Delta f, \bar\eta)$ plane.
Parameters (Rosetta Stone PING \cite{ruffini2025rosetta}) are $\Delta=1$, global
coupling $J=15$, $\tau_E=15$, $\tau_I=7.5$, $\tau_a=10$, $\tau_g=2.5$~ms;
$\bar\eta$ is swept through the supercritical Hopf at $\bar\eta_H=1.110$
($f_0=54.0$~Hz), located by bisection on the leading eigenvalue of the mean-field
Jacobian. The simulations retain these finite membrane times, whereas
Eq.~\eqref{eq:slow_synapse} characterizes the fast-membrane limit.

The resonance map varies $\bar\eta$ (Fig.~\ref{fig:nmm2_map}). The coupling sweep varies
$J$ toward $J^*$ at fixed $\bar\eta$, locating $J^*$ by the same eigenvalue bisection,
and measures the peak rate lock-in over $\Delta f$ (Fig.~\ref{fig:nmm2_jcurve}). Unlike
in JR, this sweep does not pin the operating point. At $\bar\eta=0$, continuation tracks
the critical pair defining $\gamma$ even when another mode dominates. The linear
reference includes the state-dependent source and full transfer; grids, amplitude
checks, and normalizations are in the supplement (\S\ref{supp:ping-runs}).

*Script: claim-strength changes none; quantity changes ({}, {}, False)*

## Pair 6

**Original**

Stability of the driven endpoint is checked using period-to-period perturbation
multipliers, direct perturbation decay, and a finite-time Lyapunov estimate;
settings and results are given in the supplement (\S\ref{app:ping-stability}).

\subsection{QIF spiking network (microscale of NMM2)}\label{sec:qif-methods}
To compare beat-locked and ongoing activity at the spike level, we simulate
the all-to-all QIF network whose infinite-population limit is
NMM2 \cite{montbrio2015,ruffini2025rosetta,clusella2023}, with $N=8000$
neurons per population and the PING parameters of Eq.~\eqref{eq:nmm2-ping}.
Single-neuron voltages $V_j$ spike at $V_{\rm peak}=100$ and reset to
$-V_{\rm peak}$ in model units. Excitabilities follow deterministic
quantiles of Lorentzian$(\bar\eta,\Delta)$; empirical rates drive the
second-order synapses. Genuine two-tone input enters E membranes because
spiking and threshold dynamics need not preserve surrogate equivalence
beyond perturbation theory.

At $f_c=300$~Hz and amplitude $A_f=35$ per tone, we use
$\bar\eta=0.85$, beat $55$~Hz, and $\bar\eta=1.5$, beat $42$~Hz.
These lie below and above the field-free Hopf
($\bar\eta_H=1.110$, $f_0=54.0$~Hz). Condition labels refer to that
field-free state; spectra and rate folds separate components without
establishing phase capture.

We repeat both conditions at $A_f=10$ and test step, population, window,
and spike-cutoff sensitivity. An equal-RMS mean-field control replaces the
two tones by one $300$~Hz carrier of peak amplitude $\sqrt2 A_f$;
both inputs have mean-square amplitude $A_f^2$.

The carrier-averaged stability calculation includes the drive-dependent
second-order DC source (supplement, \S\ref{app:qif-estimate}). Direct two-tone
integrations retain the beat and separately check the averaged prediction.

Euler integration uses $0.0025$~ms steps. Settling times, whole-cycle windows,
leakage checks, and sensitivity protocols are specified in the supplement
(\S\ref{supp:qif-protocol}).
We report the rate lock-in as modulation depth
$A_\Omega/\langle r_E\rangle$; an off/on ratio would divide by the
field-free floor. Single-neuron locking is measured by pairwise phase
consistency (PPC) at $\Delta f$, unbiased in spike count
\cite{vinck2010}, for neurons with at least ten spikes per window.

A cutoff-free check uses the equivalent theta-neuron equation,
$V_j=\tan(\theta_j/2)$, with interpolated crossings of $\theta_j=\pi$.
Separate step, population, and window checks test a predeclared $5\%$
rate-depth tolerance (supplement, \S\ref{supp:theta-pilot}). Quantitative
convergence remains unestablished; the finite network is interpreted qualitatively.
\ifjne\else
\input{planning/parts/theta_pilot}
\fi

**Proposed**

Stability of the driven endpoint is checked by period-to-period perturbation
multipliers, direct perturbation decay, and a finite-time Lyapunov estimate, with
settings and results in the supplement (\S\ref{app:ping-stability}).

\subsection{QIF spiking network (microscale of NMM2)}\label{sec:qif-methods}
To compare beat-locked and ongoing activity at the spike level, we simulate
the all-to-all QIF network whose infinite-population limit is
NMM2 \cite{montbrio2015,ruffini2025rosetta,clusella2023}, with $N=8000$
neurons per population and the PING parameters of Eq.~\eqref{eq:nmm2-ping}.
Each single-neuron voltage $V_j$ spikes at $V_{\rm peak}=100$ and resets to $-V_{\rm peak}$ (model
units). Excitabilities are deterministic quantiles of Lorentzian$(\bar\eta,\Delta)$,
and empirical rates drive the second-order synapses. Genuine two-tone input enters E
membranes because spiking and threshold dynamics need not preserve the surrogate's
equivalence beyond perturbation theory.

With $f_c=300$~Hz and $A_f=35$ per tone, we use $\bar\eta=0.85$ (beat $55$~Hz) and
$\bar\eta=1.5$ (beat $42$~Hz), below and above the field-free Hopf
($\bar\eta_H=1.110$, $f_0=54.0$~Hz). Condition labels refer to that field-free state;
spectra and rate folds separate components without establishing phase capture.

We repeat both conditions at $A_f=10$ and test step, population, window, and
spike-cutoff sensitivity. An equal-RMS mean-field control replaces the two tones by one
$300$~Hz carrier of peak amplitude $\sqrt2 A_f$, so both inputs have mean-square
amplitude $A_f^2$.

The carrier-averaged stability calculation includes the drive-dependent second-order DC
source (supplement, \S\ref{app:qif-estimate}); direct two-tone integrations retain the
beat and check the averaged prediction separately.

Euler integration uses $0.0025$~ms steps; settling times, whole-cycle windows, leakage
checks, and sensitivity protocols are in the supplement (\S\ref{supp:qif-protocol}).
The rate lock-in is reported as modulation depth $A_\Omega/\langle r_E\rangle$; an
off/on ratio would divide by the field-free floor. Single-neuron locking at
$\Delta f$ is measured by pairwise phase consistency (PPC), unbiased in spike count
\cite{vinck2010}, for neurons with at least ten spikes per window.

A cutoff-free check uses the equivalent theta-neuron equation,
$V_j=\tan(\theta_j/2)$, with interpolated crossings of $\theta_j=\pi$. Separate step,
population, and window checks test a predeclared $5\%$ rate-depth tolerance
(supplement, \S\ref{supp:theta-pilot}). Quantitative convergence remains unestablished;
the finite network is interpreted qualitatively.
\ifjne\else
\input{planning/parts/theta_pilot}
\fi

*Script: claim-strength changes none; quantity changes ({}, {}, False)*
