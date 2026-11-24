"""Apply the approved draft24 prose consolidation; archive each replacement."""
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[2]
path = ROOT / 'TN0484_envelope_demodulation.tex'
text = path.read_text()
changes = []

def replace_between(start, stop, new):
    global text
    a = text.index(start)
    b = text.index(stop, a)
    old = text[a:b]
    new = new.strip() + '\n\n'
    changes.append(dict(anchor=start, before=old, after=new))
    text = text[:a] + new + text[b:]

replace_between('We neglect electromagnetic propagation', r'\subsection{Envelope oscillations', r'''
We neglect propagation and induction in the extracellular field $E(t)$ (V/m),
but retain finite membrane charging. The effective polarization $s(t)$ (mV)
enters the population sigmoid after cellular access:
\begin{equation}
r(t)=\Sig\!\big(v(t)+s(t)\big),\qquad
E(t)=E_1\cos\omega_1 t+E_2\cos\omega_2 t .
\label{eq:coupling}
\end{equation}
Soma, dendrites, AIS, nodes, and terminals contribute parallel inputs with
different couplings and response times. For nearby carriers centered at
$\omega_c=2\pi f_c$,
\begin{equation}
s(t)\simeq\sum_k \boldsymbol\lambda^k_f(\omega_c)\!\cdot\!\mathbf E(t),\qquad
\boldsymbol\lambda^k_f(\omega)=\boldsymbol\lambda^k_0\,\lvert H_k(\omega)\rvert,
\label{eq:doors}
\end{equation}
where $\boldsymbol\lambda^k_0$ is compartment $k$'s static polarization vector
(a length) and $H_k$ its access filter \cite{ruffini2025rosetta,galangadea2023}.
This amplitude-gain sum assumes aligned compartment phases; otherwise the
complex transfers must be summed. For one dominant entry point,
$\lambda_f=\lambda_0|H|$ and $\varepsilon_j=\lambda_f(\omega_j)E_j$.
Holding these post-access polarizations fixed isolates detection and gain;
at fixed field they inherit $H$'s frequency dependence.

Fast axonal access motivates $\lambda_f\approx\lambda_0$. At the AIS,
$\Sig(v+s)$ represents a spike-initiation threshold shifted from $v_0$ to
$v_0-s$, requiring no backward transmission to the soma. The conversion from
AIS polarization to $s$, its response time, and the validity of a static
detector at the carrier frequency each require calibration.

Expanding about the field-free voltage $v^*$ (mV)
\cite{ruffini2025ham} gives
$\Sig(v^*+s)\approx\Sig(v^*)+\Sig'(v^*)s+\half\Sig''(v^*)s^2+\dots$.
Quadratic mixing leads when $|s|\ll1/\rho\approx1.8$~mV and
$\Sig''(v^*)\ne0$; larger excursions require the full curve.
The linear term preserves the carriers, while
$2\cos\omega_1t\cos\omega_2t=\cos\Omega t+\cos(\omega_1+\omega_2)t$
generates their difference. Averaging over the carrier removes the fast terms
before applying network gain; synaptic filtering suppresses those terms
downstream of detection. Since $\langle\cos^2\omega_jt\rangle_c=\half$,
\begin{equation}
\big\langle\Sig(v^*+s)\big\rangle_c
=\Sig(v^*)+\tfrac14\Sig''(v^*)\,(\varepsilon_1^2+\varepsilon_2^2)
+\tfrac12\Sig''(v^*)\,\varepsilon_1\varepsilon_2\cos\Omega t+O(\varepsilon^4),
\label{eq:taylor}
\end{equation}
giving a signed beat-source amplitude
\begin{equation}
Y_\Omega\simeq\half\,\Sig''(v^*)\,\varepsilon_1\varepsilon_2 ,
\label{eq:demod}
\end{equation}
in s$^{-1}$ before recurrence, alongside the steady (DC) source.
Here $\varepsilon$ denotes a common small-amplitude scale and $\simeq$
denotes leading order in polarization throughout.

For a dynamic cellular response with synaptic input held fixed, define
the second-order coefficient $\chi^{(2)}$ through the complex source amplitude,
\begin{equation}
Y_\Omega\simeq\chi^{(2)}(\omega_2,-\omega_1)\,
\varepsilon_2\varepsilon_1,\qquad
r_\Omega(t)=\operatorname{Re}\!\left[Y_\Omega e^{i\Omega t}\right].
\label{eq:chi2}
\end{equation}
The generated rate $r_\Omega$ precedes recurrence, so $\chi^{(2)}$ has units
s$^{-1}$mV$^{-2}$. With this cosine-amplitude convention, its memoryless
limit is $\Sig''/2$. Cellular history, state, and response times can make
it complex and frequency-dependent; symmetry or cancellation can remove
second-order mixing, leaving higher orders.

The static detector predicts quadratic scaling, a vanishing source at the
inflection, and carrier independence at fixed polarization. At fixed field,
access attenuation raises the field required for a given source, consistent
with carrier-dependent thresholds \cite{opancar2025,peripheral2023}.
''')

replace_between('Envelope following and quadratic detection assign', r'\begin{table}[ht]', r'''
Envelope following and quadratic detection assign different spatial doses
to the same field. At position $\mathbf x$, let $\varepsilon_j(\mathbf x)$ be
the signed polarization of tone $j$ along a fixed direction. Its nonnegative
envelope is
\[
\mathcal A(\mathbf x,t)=\sqrt{\varepsilon_1(\mathbf x)^2+\varepsilon_2(\mathbf x)^2
+2\varepsilon_1(\mathbf x)\varepsilon_2(\mathbf x)\cos\Omega t}.
\]
At each location, carrier averaging gives
\begin{equation}
\mathrm{LPF}[s^2(t)]=\tfrac12\mathcal A^2(t)
=\frac{\varepsilon_1^2+\varepsilon_2^2}{2}+\varepsilon_1\varepsilon_2\cos\Omega t,
\label{eq:sqenv}
\end{equation}
with spatial arguments suppressed. The squared envelope is sinusoidal at
$\Omega$; the envelope itself is not. For matched tones it is the rectified
cosine $\mathcal A(t)=2\varepsilon|\cos(\Omega t/2)|$.
The conventional TI map measures its excursion,
$\mathcal M[y]\equiv\max_t y-\min_t y$ \cite{grossman2017}.

Table~\ref{tab:transduction-maps} separates these geometric quantities from
detector gains; overbars denote beat-period means. An ideal envelope follower
outputs $c_1\mathcal A$ for gain $c_1$, whereas a smooth transfer $g$ with
nonzero curvature gives $g''(v^*)\mathcal A^2/4$ at weak input ($g=\Sig$ in JR).
Thus the nonnegative mean-square map $\mathcal I$ specifies neither excitation
nor suppression, and an envelope-excursion map alone specifies no mean output.
''')

replace_between('The dominant local polarization therefore reweights', 'The scalar maps use a common fixed projection', r'''
The dominant polarization reweights the envelope map. Both maps can have a
central maximum, although the quadratic example in Fig.~\ref{fig:spatial_maps}a
is broader. A larger superficial dominant carrier degrades deep contrast:
for $(\varepsilon_1,\varepsilon_2)=(10,1)$ superficially and $(0.5,0.5)$
at depth, the superficial/deep excursion ratios are $2$ for the envelope
and $40$ for the quadratic map. A sufficiently weak second carrier can
instead suppress the superficial product. Actual contrast requires the
vector fields.

With fixed electrode pairs, frequencies, neural state, linear access, and
projection directions, write
$\varepsilon_j(\mathbf x)=I_j^{\rm pair}\mathcal P_j(\mathbf x)$,
where $I_j^{\rm pair}>0$ is peak pair current (mA) and $\mathcal P_j$ is
signed polarization per current (mV/mA). Then
\[
\mathcal M[\tfrac12\mathcal A^2]
=2I_1^{\rm pair}I_2^{\rm pair}|\mathcal P_1\mathcal P_2|.
\]
Changing the ratio therefore rescales the beat map without moving its maxima
or changing normalized maps and target/reference ratios
\cite{cassara2025part2}. Fixed detector coefficients and linear propagation
preserve the common current factor, even with dynamic mixing and heterogeneous
gains. Steering requires a changed carrier field shape, for example through
current redistribution among electrodes at one frequency.

The steady map instead weights $\mathcal P_1^2$ and $\mathcal P_2^2$ by
the squared currents. Its ratio-dependent source can shift operating points
and thereby reshape the beat response. Threshold effects also depart from
the weak quadratic regime; the $2\min$ steering law requires envelope
following. The product law itself permits an interior beat maximum.
Local detector and network factors weight this product
(Eq.~\eqref{eq:receiver}); resonance can compensate for an unfavorable
product only where the source is nonzero.
''')

replace_between("The detector's transduction", r'\subsection{The steady source', r'''
For a narrowband input $s(t)=\mathcal A(t)\cos\omega_c t$, a memoryless
nonlinearity $g$ has low-frequency output given by its carrier-cycle average,
\[
Y_{\rm LF}(\mathcal A)=(2\pi)^{-1}\!\int_0^{2\pi}\!g(v^*+\mathcal A\cos\theta)\,\mathrm{d}\theta,
\]
where $\theta$ is carrier phase. This transduction $T(\mathcal A)$ contains
only even powers:
\begin{equation}
Y_{\rm LF}(\mathcal A)=g(v^*)+\tfrac14 g''(v^*)\mathcal A^2+\tfrac1{64}g^{(4)}(v^*)\mathcal A^4+\cdots
\label{eq:cycavg}
\end{equation}
Thus smooth detection with nonzero curvature is quadratic at weak input.
Other laws require different detectors: full- and half-wave rectifiers yield
$2\mathcal A/\pi$ and $\mathcal A/\pi$, a diode-and-capacitor detector
follows the peak, and a step with offset $\delta>0$ yields
$\pi^{-1}\arccos(\delta/\mathcal A)$ above threshold and zero below.
Channel rectification, threshold crossing, and release events are possible
biological implementations.

At matched tones, envelope following is linear in amplitude with
second/fundamental harmonic ratio $1/5$. Quadratic detection gives only
the steady term and fundamental; its quartic correction gives
$Y_{2\Omega}/Y_\Omega\sim(c_4/c_2)\varepsilon^2$, with
$c_2=g''/4$ and $c_4=g^{(4)}/64$. A threshold detector is silent for
$2\varepsilon\le\delta$ and has an amplitude-dependent ratio above onset.
The full harmonic series and mixed-detector inversion are supplementary
(\S\ref{supp:harmonics}).
\ifjne\else
\input{planning/parts/harmonic_details}
\fi

The network modifies these ratios through
$\mathcal H_{\rm meas}=\mathcal H_{\rm det}|G(2\Omega)/G(\Omega)|$.
Near resonance it can suppress an envelope follower's second harmonic,
making it appear quadratic. Amplitude sweeps and gain correction are
therefore needed; one harmonic ratio cannot identify the detector.
''')

replace_between('Mean-square polarization is a nonnegative geometric map.', r'\subsection{Comparison with direct', r'''
Detection converts nonnegative mean-square polarization into a signed steady
source; recurrence converts that source into a mean response. ``DC-like''
describes this source, not the applied field, which has no DC component.
For comparison, the envelope mean is
\[
\overline{\mathcal A}(\mathbf x)=\frac{1}{2\pi}\int_0^{2\pi}
\sqrt{\varepsilon_1(\mathbf x)^2+\varepsilon_2(\mathbf x)^2
+2\varepsilon_1(\mathbf x)\varepsilon_2(\mathbf x)\cos\vartheta}\,\mathrm d\vartheta,
\]
where $\vartheta$ is beat phase. At matched polarizations $\varepsilon>0$,
the envelope and quadratic means are $4\varepsilon/\pi$ and
$\varepsilon^2$, before detector gains. Either ideal detector gives a mean
output with one carrier, but no beat; adaptation can alter the mean response.

The static JR source is
\[
Y_{\rm DC}(\mathbf x,\mathbf n)
=\frac{\Sig''(v^*_{\mathbf x})}{2}\,\mathcal I(\mathbf x,\mathbf n),
\qquad
\mathcal I(\mathbf x,\mathbf n)
=\frac{\varepsilon_1(\mathbf x,\mathbf n)^2+
\varepsilon_2(\mathbf x,\mathbf n)^2}{2}\ge0,
\]
where $v^*_{\mathbf x}$ is the local baseline and $\mathbf n$ the common
unit cell orientation. Convex and concave rate curves give positive and
negative sources, respectively, with zero quadratic source at the inflection.
Reversing either carrier or $\mathbf n$ leaves the squares unchanged;
other orientations change magnitudes but not the sign at fixed curvature.
Figure~\ref{fig:spatial_maps}c shows both signs on one positive normalization.
At the pinned JR state, $v^*=8.30$~mV, the source lowers the local rate.
This curvature rule is static: fast-carrier QIF rectification follows a
positive slope (\S\ref{sec:dynamic}), and recurrence further shapes the mean.

Carrier averaging retains the beat cross term; a beat-period average removes
it, leaving intensities without cross-frequency cancellation. Where
$Y_{\rm DC}\ne0$,
$|Y_\Omega/Y_{\rm DC}|=2|\varepsilon_1\varepsilon_2|/
(\varepsilon_1^2+\varepsilon_2^2)\le1$, with equality at matched magnitudes.
A common access factor cancels. For the preceding superficial/deep example,
$\mathcal I$ is $50.5/0.25$, a $202$-fold contrast; beat/DC ratios are
$0.20$ and $1$.

In a homogeneous, isotropic, source-free conductor, the potentials $\phi_j$,
field components $\mathbf E_j=-\nabla\phi_j$, and polarizations
$\varepsilon_j=\boldsymbol\lambda\cdot\mathbf E_j$ for spatially fixed
coupling $\boldsymbol\lambda$ are harmonic. Consequently
$\nabla^2\mathcal I=\sum_j|\nabla\varepsilon_j|^2\ge0$:
the intensity is subharmonic, with no strict interior maximum. Its maximum
lies on the region's boundary, including conductivity interfaces, regardless
of montage. With spatially constant nonzero detection, the same holds for
$|Y_{\rm DC}|$; negative curvature makes the boundary source most negative.
Spatially varying access, orientation, or detector coefficients require a
weighted map, and the restriction does not extend to the physiological mean
response or an indefinite multicompartment DC form.

The envelope mean is also subharmonic: at each beat phase it is a norm of
harmonic components, and phase averaging preserves that property (supplement,
\S\ref{supp:envelope-proof}).
\ifjne\else
\input{planning/parts/envelope_proof}
\fi
By contrast,
$\nabla^2(\varepsilon_1\varepsilon_2)=2\nabla\varepsilon_1\cdot\nabla\varepsilon_2$
has unrestricted sign. Within this homogeneous scalar model, interior
selectivity must come from the oscillatory response, not either mean map.
With isotropic orientations and orientation-independent access and curvature,
orthogonal fields cancel the averaged beat while retaining steady intensity
(supplement, \S\ref{supp:orientation}).
\ifjne\else
\input{planning/parts/orientation_average}
\fi
An unmodulated carrier at the same local RMS polarization gives the same
second-order mean shift if its DC mixing coefficient equals those of both
TI carriers. For a dynamic detector, that coefficient must vary negligibly
over the carrier interval.
''')

replace_between('The steady TI source can be compared with transcranial', 'For the JR parameters', r'''
Compare TI's steady and beat sources with transcranial direct-current
stimulation (tDCS) and tACS at $\Omega$, respectively, using polarizations
at the same sigmoid entry point. For equal TI tones
$\varepsilon_1=\varepsilon_2=\varepsilon>0$,
\[
Y_{\rm DC}^{\rm TI}\simeq Y_\Omega^{\rm TI}
\simeq \frac12\Sig''(v^*)\varepsilon^2.
\]
A constant polarization $\varepsilon_{\rm D}$ or sinusoid
$\varepsilon_{\rm A}\cos\Omega t$ instead gives
\[
Y_{\rm DC}^{\rm tDCS}\simeq\Sig'(v^*)\varepsilon_{\rm D},
\qquad
Y_\Omega^{\rm tACS}\simeq\Sig'(v^*)\varepsilon_{\rm A}.
\]
Here $\varepsilon_{\rm D}$ is signed and negative $\varepsilon_{\rm A}$
denotes phase reversal. The equivalent direct polarization matching either
TI source is
\[
\varepsilon_{\rm eq}
=\frac{\Sig''(v^*)}{2\Sig'(v^*)}\,\varepsilon^2,
\qquad
\frac{\Sig''(v^*)}{\Sig'(v^*)}
=-\rho\tanh\!\left[\frac{\rho(v^*-v_0)}2\right].
\]
Sigmoid steepness and operating voltage determine the ratio; the rate ceiling
cancels, and the quadratic TI sources vanish at the inflection.
''')

replace_between('These percentages match each TI carrier', r'\subsection{Amplification:', r'''
Matching the total TI peak instead uses direct amplitude $2\varepsilon$
and halves these ratios. RMS matching uses tACS amplitude
$\sqrt2\varepsilon$ or tDCS magnitude $\varepsilon$, because TI's RMS
polarization is $\varepsilon$. The tACS quadratic steady source,
$\Sig''\varepsilon_{\rm A}^2/4$, then equals TI's for this static detector.
Equal electrode currents need not match polarization: access differs among
DC, beat and carrier frequencies, and among entry compartments.

At a common state and entry point, matched sources give matched leading
circuit responses. Steady sources share the zero-frequency transfer; beat
and tACS sources share the transfer at $\Omega$. These transfers differ,
and rectification of the amplified TI beat can add a mean shift
(\S\ref{sec:timing}). The local source comparison therefore specifies
neither a universal physiological-effect ratio nor equal spatial responses.
''')

replace_between('What turns this recovered beat component', 'Write $D$ for the detector', r'''
The recurrent circuit selects the recovered beat. Linearizing about the JR
fixed point gives a leading pair $\mu_\pm=-\gamma\pm i\omega_0$, with
modal damping $\gamma$ and frequency $\omega_0$. Below a supercritical
Hopf, $\gamma\to0^+$ and the quality factor
$\mathcal Q=\omega_0/(2\gamma)$ grows. A constant-numerator two-pole
approximation to the complex susceptibility $G$ gives
\begin{equation}
|G(\Omega)|\propto\big[(\omega_0^2+\gamma^2-\Omega^2)^2+(2\gamma\Omega)^2\big]^{-1/2},
\qquad |G(\omega_0)|\propto\frac{1}{2\gamma\omega_0}
\quad(\gamma\ll\omega_0),
\label{eq:gain}
\end{equation}
an approximately Lorentzian power peak near $\omega_0$ with $1/\gamma$
growth at a simple Hopf with nonzero input--output projections.\footnote{
The eigenvalue frequency $\omega_0$ differs from the canonical oscillator's
undamped frequency $\sqrt{\omega_0^2+\gamma^2}$ and peak
$\sqrt{\omega_0^2-\gamma^2}$ ($\omega_0>\gamma$).
Frequency-dependent projections can further shift the peak.}
This weak-drive law requires stability after the rectified mean shift.
Above the Hopf, entrainment instead means phase capture of an autonomous rhythm.
''')

replace_between('For the illustrative somatic time', r'\begin{table}[h]', r'''
For an illustrative somatic $\tau_m=16$~ms, $|H_m|^2$ is about
$10^{-4}$, $2.5\times10^{-5}$, and $10^{-6}$ at $1$, $2$, and $10$~kHz.
The assumed $0.2$~ms case gives $0.39$ and $0.14$ at $1$ and $2$~kHz
(Fig.~\ref{fig:khz}); this transfer has not been measured under TI at an
AIS or node. Table~\ref{tab:doors} distinguishes measured responses,
assumed access, and downstream filtering. Axonal decay alone specifies
neither field coupling nor a TI cutoff.

QIF computes access in its membrane equation, requiring no additional filter
on current input. Shorter access improves transmission without determining
mixing or recurrent gain.
''')

replace_between('Channel kinetics contribute to the effective', r'\subsection{Operating-point dependence}', r'''
Any additional gate filter must represent kinetics absent from the detector
and have a model or measurement behind it. QIF lacks explicit sodium-channel
kinetics; neither it nor a static sigmoid specifies a universal $1$~kHz cutoff.
Carrier sweeps probe access and mixing together; beat sweeps probe amplification.
''')

replace_between('Because $Y_\\Omega\\propto', r'\subsection{The exact mean field', r'''
The Population Excitation--Inhibition Index (PEIX) \cite{ruffini2025cfc}
measures the operating point's signed departure from maximal sigmoid slope:
\begin{equation}
\mathrm{PEIX}(v^*)=\operatorname{sign}(v^*-v_0)
\left\{1-\operatorname{sech}^2\!\Big[\tfrac{\rho}{2}\,(v^*-v_0)\Big]\right\}.
\label{eq:peix}
\end{equation}
It is zero at $v_0$ and approaches $\pm1$ in the saturated tails, with
positive sign above $v_0$. For the logistic,
$\Sig'/\Sig'(v_0)=1-|\mathrm{PEIX}|$, $\Sig'(v_0)=e_0\rho/2$, and
$\Sig''=-\rho\Sig'\operatorname{sign}(\mathrm{PEIX})\sqrt{|\mathrm{PEIX}|}$.
Thus this measurable state index determines the side and saturation, while
mixing follows curvature: zero at the inflection and in the tails, largest
on the flanks.

Changes in $v^*$ through neuromodulation, attention, arousal, psychedelic
exposure, or PV-interneuron dysfunction in Alzheimer's disease can scale or
reverse the static JR source. Dynamic detectors have their own state-dependent
coefficients and susceptibilities, without a universal PEIX sign rule.
State sweeps therefore isolate detection only if recurrent gain is also measured.
''')

replace_between('The static rate curve applies when population', 'If the population relaxes to this equilibrium', r'''
The exact mean field of all-to-all quadratic integrate-and-fire (QIF) neurons
with Lorentzian excitabilities supplies both a static rate curve and its
dynamic extension. The Montbri\'o--Paz\'o--Roxin (MPR) equations evolve physical
rate $r$ and dimensionless mean voltage $v$ \cite{montbrio2015}; dynamic
synapses produce a second-generation neural mass (NMM2)
\cite{ruffini2021nmm2,clusella2023}:
\begin{equation}
\tau_m\dot r=\frac{\Delta}{\pi\tau_m}+2rv,\qquad
\tau_m\dot v=v^2+\bar\eta-(\pi\tau_m r)^2+I(t).
\label{eq:mpr}
\end{equation}
Here $\tau_m$ is membrane time, dots denote physical-time derivatives,
$\bar\eta$ and $\Delta>0$ are the excitability center and half-width, and
$I(t)$ is dimensionless input, including recurrent drive when present.
For constant total drive $Q=\bar\eta+I$, equilibrium gives
$v=-\Delta/(2\pi\tau_m r)$ and
\begin{equation}
\tau_m r=F(Q)=\frac{1}{\pi}\sqrt{\frac{Q+\sqrt{Q^2+\Delta^2}}{2}} .
\label{eq:Fmpr}
\end{equation}
Primes on $F$ denote drive derivatives. Below its inflection at
$Q=\Delta/\sqrt3$, curvature reflects recruitment across threshold;
above it, the concave square-root rate of active cells. This nonlinearity
exists without recurrence and grows without bound, unlike the JR sigmoid.
''')

replace_between('If the population relaxes to this equilibrium', 'Outside the adiabatic limit', r'''
If relaxation is faster than synaptic variation, NMM2 reduces to
$r(t)\simeq F(Q(t))/\tau_m$ with dynamically filtered recurrence
\cite{ruffini2021nmm2,clusella2023}. For population relaxation time
$\tau_{\rm rel}$ and synaptic time $\tau_s$ (Eq.~\eqref{eq:slow_synapse},
Appendix~\ref{app:models}), this requires $\tau_{\rm rel}\ll\tau_s$.
Applying the static curve to carriers further requires
$\omega_c\tau_{\rm rel}\ll1$: the same population can track synaptic
input quasistatically while responding dynamically to kHz input.
Synaptic circuit resonances can survive the fast-membrane limit without
intrinsic cellular resonance \cite{brunelhakim1999,brunelwang2003}; modes
requiring finite membrane dynamics need not survive.
''')

replace_between('The fast-carrier attenuation already includes', r'\section{Methods}', r'''
This fast-carrier attenuation includes membrane access. Normalizing by the
squared voltage excursion leaves a coefficient tending to $F'/2$.
For two nearby current tones of amplitudes $I_j$, voltage squaring gives a
beat source proportional to $I_1I_2/(\omega_1\omega_2\tau_m^2)$.
The dynamic rate equation further attenuates the carriers after mixing,
but not the already-generated beat. The crossover is derived in
Appendix~\ref{app:mpr-coefficients}; fixed-voltage coefficients and carrier
exponents are supplementary (\S\ref{supp:dynamic-details}).

In this realization, the unit coefficient of $v^2$ in membrane-time units
plays the role of $\Sig''/2$; $G$ includes the voltage and rate dynamics
converting that source into a rate beat. Other smooth cellular mechanisms
share the weak-input product law without sharing its coefficient, phase,
or carrier dependence.
''')

text = text.replace(r'\newcommand{\paperver}{0.15.0-draft23}',
                    r'\newcommand{\paperver}{0.15.0-draft24}')
text = text.replace('version \\paperver, October 24, 2026',
                    'version \\paperver, October 25, 2026')
text = text.replace(r'Working draft v\paperver\quad 2026-10-24',
                    r'Working draft v\paperver\quad 2026-10-25')
path.write_text(text)
(Path(__file__).parent / 'theory_replacements.json').write_text(json.dumps(changes, indent=2)+'\n')
print(f'Applied {len(changes)} paragraph-block replacements.')
