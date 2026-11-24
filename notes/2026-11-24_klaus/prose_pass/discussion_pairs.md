# Pairs: discussion

## Pair 1

**Original**

\section{Discussion}\label{sec:discussion}
\subsection{Cellular access and mixing require separate calibration}
The JR and QIF models demonstrate local mixing followed by recurrent
amplification. Cellular mixing \cite{mirzakhalili2020,luff2024mixer} and network
amplification \cite{caldas2024,karimi2024,esmaeilpour2021} have complementary
experimental and modeling support, but their combined transfer at physiological
kHz fields remains unmeasured. The short-time cases in Table~\ref{tab:doors}
are access assumptions; varying the effective membrane time quantifies their
consequences.

At fields of order $1$~V/m, channels respond through membrane polarization,
well below fields associated with direct protein effects
\cite{cifra2026}.\footnote{That review describes direct effects at $10$~kV/m
to GV/m, depending on molecule and protocol; it excludes fields below
$0.1$~kV/m, where it expects direct effects to be negligible against thermal noise.}
Terminals can polarize more strongly than somata
\cite{rahman2013,aberra2023,chakraborty2018}. Small size alone does not imply
fast charging: specific membrane resistance times capacitance is area-independent;
conductance, geometry, and stimulation mode determine access. The supplementary
comparison distinguishes these mechanisms from strong-pulse charging
(\S\ref{supp:access}).
\ifjne\else
\input{planning/parts/access_literature}
\fi

Missey et al.\ \cite{missey2026} report biomarker suppression with both
low- and high-kHz carriers. Their Methods specify $1300/1430$~Hz at one
center and $9000/9130$~Hz at the other centers. For these pairs, the
$0.2$~ms point-membrane model predicts a high/low source ratio of $0.030$
at matched local fields. This comparison challenges that access hypothesis
but does not test it directly: carrier band was confounded with center,
local polarization was unmeasured, and a nonlinear or saturating physiological
readout could reconcile different sources with similar biomarker changes.

\subsection{Detector laws predict different spatial responses}
The head-model comparison separates geometric consequences of detector laws.
The product and summed-squares maps differ from the envelope map even before
state-dependent detection and network gain are applied. The fixed quadratic
pattern follows algebraically from fixed field shapes and linear access;
opposite envelope and mean-square centroid motion is a result for the tested
subject and montages, not a general steering law. A sharp rectifier can follow
the envelope over a finite amplitude range while smoothing or heterogeneity
restores quadratic behavior at smaller inputs. Amplitude and harmonic sweeps
therefore complement the spatial comparison.

The connection to Violante et al.\ \cite{violante2023} is a hypothesis generated
by these maps. Their models and cadaver recordings supported anterior envelope
steering from $2+2$~mA to $1+3$~mA. During participants' 32~s encoding blocks,
1:3 reduced the evoked blood-oxygen-level-dependent (BOLD) response relative
to sham ($P=0.006$) and 1:1 ($P=0.015$); 1:1 did not differ from sham
($P=0.953$). The stimulation-by-region interaction was nonsignificant
($P=0.76$), so the physiology did not establish spatial steering. Significant
voxelwise reductions extended beyond the anterior focus: 30\% of anterior,
25\% of posterior, and 2\% of middle hippocampal voxels.

In IXI002, mean-square polarization rises by 24\% under 1:3, while mean
envelope excursion falls by 45\% and both quadratic beat maps fall by 25\%.
At fixed uniform static curvature the steady-source magnitude therefore rises
by 24\%; a mean shift from rectification of the beat instead scales as
$(3/4)^2\approx0.56$ in the weak-response limit. The first ordering is
consistent with stronger BOLD suppression if the steady source lowers activity
and the hemodynamic response preserves that ordering. A slow linear readout
suppresses a zero-mean $5$~Hz beat while retaining a shift over the stimulation
window; nonlinear neural or vascular responses can also convert that beat into
a mean change or alter the encoding response.

This comparison does not identify the biological detector. Local envelope excursion can also increase under 1:3
(supplement, \S\ref{supp:steering-algebra}), allowing a selective or
thresholded envelope response. Equal summed currents do not match local RMS polarization,
and the nonsignificant 1:1--sham result does not establish a null effect.
Heterogeneous curvature and unknown recurrent and hemodynamic gains can change
the predicted ordering. Measuring spatially resolved steady and beat responses
at controlled polarization and state, with an equal-RMS carrier control,
would discriminate the hypotheses.
\ifjne\else
\input{planning/parts/steering_algebra}
\fi

\subsection{Field-induced oscillations and resonant amplification}
At stronger fields, TI and unmodulated carriers can have similar excitation
thresholds \cite{opancar2025,semenov2025}, and peripheral responses need not
extract the envelope \cite{peripheral2023}. Our weak-input calculation concerns
modulation of ongoing activity \cite{vieira2024}; the finite-amplitude
QIF examples instead show a mean shift crossing a circuit Hopf. That boundary
depends on amplitude and initial state, and supplies no physiological threshold.
The supplementary laminar extension tests two resonant bands at low carriers
(\S\ref{app:lanmm}), outside TI's kHz regime.

**Proposed**

\section{Discussion}\label{sec:discussion}
\subsection{Cellular access and mixing require separate calibration}
Cellular mixing \cite{mirzakhalili2020,luff2024mixer} and network amplification
\cite{caldas2024,karimi2024,esmaeilpour2021} have complementary experimental and
modeling support, but their combined transfer at physiological kHz fields remains
unmeasured. The JR and QIF models demonstrate local mixing followed by recurrent
amplification. The short-time cases in Table~\ref{tab:doors} are access
assumptions; varying the effective membrane time quantifies their consequences.

At fields of order $1$~V/m, channels respond through membrane polarization,
well below fields associated with direct protein effects
\cite{cifra2026}.\footnote{That review places direct effects at $10$~kV/m
to GV/m, depending on molecule and protocol, and excludes fields below
$0.1$~kV/m, where it expects them to be negligible against thermal noise.}
Terminals can polarize more strongly than somata
\cite{rahman2013,aberra2023,chakraborty2018}. Small size alone does not imply
fast charging, since specific membrane resistance times capacitance is
area-independent; conductance, geometry, and stimulation mode determine access.
The supplementary comparison distinguishes these mechanisms from strong-pulse
charging (\S\ref{supp:access}).
\ifjne\else
\input{planning/parts/access_literature}
\fi

Missey et al.\ \cite{missey2026} report biomarker suppression with both low- and
high-kHz carriers ($1300/1430$~Hz at one center and $9000/9130$~Hz at the others,
per their Methods). For these pairs, the $0.2$~ms point-membrane
model predicts a high/low source ratio of $0.030$ at matched local fields. The
comparison challenges that access hypothesis but does not test it directly, because
carrier band was confounded with center, local polarization was unmeasured, and a
nonlinear or saturating physiological readout could reconcile different sources
with similar biomarker changes.

\subsection{Detector laws predict different spatial responses}
The head-model comparison separates geometric consequences of detector laws:
the product and summed-squares maps differ from the envelope map before
state-dependent detection and network gain enter. The fixed quadratic
pattern follows algebraically from fixed field shapes and linear access, whereas
opposite envelope and mean-square centroid motion is a result for the
tested subject and montages, not a general steering law. Because a sharp rectifier
can follow the envelope over a finite amplitude range while smoothing or
heterogeneity restores quadratic behavior at smaller inputs, amplitude and
harmonic sweeps complement the spatial comparison.

The connection to Violante et al.\ \cite{violante2023} is a hypothesis that these maps generate. Their models and cadaver recordings supported anterior envelope
steering from $2+2$~mA to $1+3$~mA. During participants' 32~s encoding blocks,
1:3 reduced the evoked blood-oxygen-level-dependent (BOLD) response relative
to sham ($P=0.006$) and to 1:1 ($P=0.015$); 1:1 did not differ from sham
($P=0.953$). The stimulation-by-region interaction was nonsignificant
($P=0.76$), so the physiology did not establish spatial steering. Significant
voxelwise reductions extended beyond the anterior focus: 30\% of anterior,
25\% of posterior, and 2\% of middle hippocampal voxels.

In IXI002, mean-square polarization rises by 24\% under 1:3, while mean
envelope excursion falls by 45\% and both quadratic beat maps by 25\%.
At fixed uniform static curvature the steady-source magnitude therefore rises
by 24\%, whereas a mean shift from rectification of the beat scales as
$(3/4)^2\approx0.56$ in the weak-response limit. The first ordering is
consistent with stronger BOLD suppression if the steady source lowers activity
and the hemodynamic response preserves that ordering. A slow linear readout
suppresses a zero-mean $5$~Hz beat but retains a shift over the stimulation
window, and nonlinear neural or vascular responses can also convert that beat
into a mean change or alter the encoding response.

The comparison does not identify the biological detector. Local envelope excursion
can also increase under 1:3 (supplement, \S\ref{supp:steering-algebra}), allowing
a selective or thresholded envelope response. Equal summed currents do not match
local RMS polarization, and the nonsignificant 1:1--sham result does not establish
a null effect. Heterogeneous curvature and unknown recurrent and hemodynamic gains
can change the predicted ordering. Spatially resolved steady and beat responses,
measured at controlled polarization and state with an equal-RMS carrier control,
would discriminate the hypotheses.
\ifjne\else
\input{planning/parts/steering_algebra}
\fi

\subsection{Field-induced oscillations and resonant amplification}
At stronger fields, TI and unmodulated carriers can have similar excitation
thresholds \cite{opancar2025,semenov2025}, and peripheral responses need not
extract the envelope \cite{peripheral2023}. Our weak-input calculation concerns
modulation of ongoing activity \cite{vieira2024}; the finite-amplitude QIF examples
instead show a mean shift crossing a Hopf bifurcation of the circuit. That
boundary depends on amplitude and initial state and supplies no physiological
threshold. The supplementary laminar extension tests two resonant bands at low
carrier frequencies (\S\ref{app:lanmm}), outside TI's kHz regime.

*Script: claim-strength changes none; quantity changes ({}, {}, False)*

## Pair 2

**Original**

\subsection{Efficiency depends on the generated drive}
Measured DC couplings are $0.12$--$0.18$~mV per V/m in hippocampus
($0.21$ at $10$~Hz) \cite{bikson2004,deans2007} and reach $0.5$~mV per V/m
in cortical L5/6 pyramidal cells \cite{radman2009}; human cortical fields near
$0.8$~V/m have been reported at $2$~mA \cite{huang2017,huang2017corr}.
These measurements constrain illustrative input budgets, not the kHz transfer.
The $2$--$5\%$ source comparison in \S\ref{sec:direct-comparison} matches
each TI carrier's polarization to the direct input. Matching the total TI
peak instead halves the ratio to
$\mathcal R_{\rm det}\simeq|\Sig''|\varepsilon/(4\Sig')$; common recurrent
gain cancels in linear response.

For $E_j=0.5$~V/m, $\lambda_0=0.5$~mV per V/m, $f_c=2$~kHz and the assumed
$\tau_m=0.2$~ms, access gives $\varepsilon\approx0.092$~mV. Rounding to
$0.1$~mV yields $\mathcal R_{\rm det}\approx0.8\%$ at $v^*=8.30$~mV
under total-peak matching. This is an assumed input budget, not an inferred
polarization in recorded cells.

For balanced TI and a direct sinusoid matched in peak polarization at the
same operating point, the carrier-averaged open-loop fundamental-amplitude
ratio has a numerically estimated supremum of $0.348$ over bounded,
nondecreasing memoryless transfers (supplement, \S\ref{app:bound},
Eq.~\eqref{eq:etasup}). Dynamic QIF is outside this detector class.

Vieira et al.'s weaker TI effects \cite{vieira2024} are compatible with a
smaller beat source, but their local mixer polarizations were unmatched
(supplement, \S\ref{supp:vieira}). Phase-locking value (PLV) also depends on
baseline and state. A calibrated amplitude sweep with a common readout is
needed to estimate the detector coefficient.

\subsection{Limits of the population description}
Synaptic filters before a detector further attenuate its input. Model choice
also matters: Hodgkin--Huxley and Frankenhaeuser--Huxley models reproduce
stimulus-evoked firing missed by the tested leaky, exponential, and
adaptive-exponential integrate-and-fire models \cite{plovie2025}.
Noise, additional heterogeneity, and intercolumn interactions can broaden or
shift our deterministic resonances. Human findings include peripheral effects
without central effects \cite{iszak2023} and null occipito-parietal alpha-power
modulation \cite{mansourinezhad2025}. Access, generated sources, and circuit
tuning therefore need measurement in the same preparation.

\subsection{Falsifiable predictions and tests}\label{sec:predictions}
Table~\ref{tab:predictions} distinguishes the measurements needed to test each
stage. Interpreting timing and synaptic-blockade data requires independent
measurements of amplitude scaling, harmonic content, and recurrent gain.

At resonance with $\mathcal Q=10$, a detector second-harmonic/fundamental ratio of $20\%$ appears in the measured response as only $0.7\%$, which could make an envelope follower look quadratic. Driving off resonance at $\Delta f\simeq f_0/4$ places both harmonics on the flatter part of the response, where $|G(2\Omega)/G(\Omega)|\approx1.22$--$1.25$ for $\mathcal Q=3$--$30$. Alternatively, a weak direct tACS sweep can measure $G$ independently so its effect can be removed from the harmonic ratio.

**Proposed**

\subsection{Efficiency depends on the generated drive}
The $2$--$5\%$ source comparison in \S\ref{sec:direct-comparison} matches each
TI carrier's polarization to the direct input. Matching the total TI peak instead halves the
ratio to $\mathcal R_{\rm det}\simeq|\Sig''|\varepsilon/(4\Sig')$; common
recurrent gain cancels in linear response.

DC couplings are $0.12$--$0.18$~mV per V/m in hippocampus ($0.21$ at $10$~Hz)
\cite{bikson2004,deans2007} and reach $0.5$~mV per V/m in cortical L5/6 pyramidal
cells \cite{radman2009}; human cortical fields near $0.8$~V/m have been reported
at $2$~mA \cite{huang2017,huang2017corr}. These measurements constrain illustrative
input budgets, not the kHz transfer. For $E_j=0.5$~V/m,
$\lambda_0=0.5$~mV per V/m, $f_c=2$~kHz and the assumed $\tau_m=0.2$~ms, access
gives $\varepsilon\approx0.092$~mV. Rounding to $0.1$~mV yields
$\mathcal R_{\rm det}\approx0.8\%$ at $v^*=8.30$~mV under total-peak matching.
This is an assumed input budget, not an inferred polarization in recorded cells.

For balanced TI and a direct sinusoid matched in peak polarization at the same
operating point, the carrier-averaged open-loop ratio of fundamental amplitudes
has a numerically estimated supremum of $0.348$ over bounded,
nondecreasing memoryless transfers (supplement, \S\ref{app:bound},
Eq.~\eqref{eq:etasup}). Dynamic QIF lies outside this detector class.

Vieira et al.'s weaker TI effects \cite{vieira2024} are compatible with a smaller
beat source, but their local mixer polarizations were unmatched (supplement,
\S\ref{supp:vieira}), and phase-locking value (PLV) also depends on baseline and
state. Estimating the detector coefficient requires a calibrated amplitude sweep
with a common readout.

\subsection{Limits of the population description}
Synaptic filters before a detector further attenuate its input. Model choice
also matters: Hodgkin--Huxley and Frankenhaeuser--Huxley models reproduce
stimulus-evoked firing that the tested leaky, exponential, and adaptive-exponential
integrate-and-fire models miss \cite{plovie2025}. Noise, additional heterogeneity,
and intercolumn interactions can broaden or shift our deterministic resonances.
Human findings include peripheral effects without central effects \cite{iszak2023}
and null occipito-parietal alpha-power modulation \cite{mansourinezhad2025}.
Access, generated sources, and circuit tuning therefore need measurement in the
same preparation.

\subsection{Falsifiable predictions and tests}\label{sec:predictions}
Table~\ref{tab:predictions} lists the measurements needed to test each stage.
Interpreting timing and synaptic-blockade data requires independent measurements
of amplitude scaling, harmonic content, and recurrent gain.

At resonance with
$\mathcal Q=10$, a detector second-harmonic/fundamental ratio of $20\%$ appears in
the measured response as only $0.7\%$, which could make an envelope follower look
quadratic. Driving off resonance at $\Delta f\simeq f_0/4$ places both harmonics on
the flatter part of the response, where $|G(2\Omega)/G(\Omega)|\approx1.22$--$1.25$
for $\mathcal Q=3$--$30$. Alternatively, a weak direct tACS sweep can measure $G$
independently so its effect can be removed from the harmonic ratio.

*Script: claim-strength changes ['requires +1']; quantity changes ({}, {}, True)*

## Pair 3

**Original**

Near a Hopf bifurcation, gain grows inversely with modal damping and is shared
with matched direct tACS. In the pinned JR column it initially
favors beat modulation, while rectification of the amplified oscillation
increasingly contributes to the mean shift.
At stronger drive, a steady shift alone can induce gamma, including under an
equal-RMS unmodulated carrier in the mean field. Physiological kHz access remains
to be calibrated. Local-polarization measurements, independent-amplitude tests,
beat sweeps across states, and equal-RMS controls distinguish these mechanisms.

**Proposed**

Near a Hopf bifurcation, gain grows inversely with modal damping and is shared
with matched direct tACS. In the pinned JR column this gain initially
favors beat modulation, while rectification of the amplified oscillation
increasingly contributes to the mean shift.
At stronger drive, a steady shift alone can induce gamma, including under an
equal-RMS unmodulated carrier in the mean field. Physiological kHz access remains
to be calibrated. Local-polarization measurements, independent-amplitude tests,
beat sweeps across states, and equal-RMS controls distinguish these mechanisms.

*Script: claim-strength changes none; quantity changes ({}, {}, False)*
