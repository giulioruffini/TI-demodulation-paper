"""Consolidate repeated protocols and result narration for draft24."""
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parents[2]
path=ROOT/'TN0484_envelope_demodulation.tex'
text=path.read_text();changes=[]

def block(start,stop,new):
    global text
    a=text.index(start);b=text.index(stop,a)
    new=new.strip()+'\n\n'
    changes.append(dict(anchor=start,before=text[a:b],after=new))
    text=text[:a]+new+text[b:]

block('The response at the envelope frequency is read out', r'\begin{equation}'+'\n'+r'\begin{gathered}', r'''
A software lock-in projects $v(t)$ onto sine and cosine at $\Omega$.
The finite window suppresses, but does not eliminate, neighboring frequencies.
For Hann weights $w_k$, sample times $t_k$, voltages $v_k=v(t_k)$, and
weighted mean $\bar v=\sum_k w_kv_k/\sum_k w_k$, the quadratures are
''')
block('with sample index $k$, sample times', r'\ifjne\else'+'\n'+r'\input{planning/parts/lockin_details}', r'''
where $k$ indexes samples. A test tone
$v=A_{\rm test}\cos(\Omega t+\theta_0)$ with amplitude $A_{\rm test}$
and phase $\theta_0$ gives
$(L_{\cos},L_{\sin})\to A_{\rm test}(\cos\theta_0,-\sin\theta_0)$
over long windows. Thus $A_\Omega$ returns physical amplitude, twice the
Fourier-coefficient magnitude. Mean subtraction suppresses leakage from
the larger baseline (supplement, \S\ref{supp:lockin}).
''')
block('The pyramidal--interneuron network gamma (PING) circuit', r'\begin{equation}'+'\n'+r'\begin{aligned}'+'\n'+r'\tau_E', r'''
The pyramidal--interneuron network gamma (PING) circuit couples excitatory
and inhibitory MPR populations through second-order synapses
\cite{montbrio2015,ruffini2021nmm2,clusella2023}, using the Rosetta Stone
formulation shared with JR and laminar models \cite{ruffini2025rosetta}.
For population $X\in\{E,I\}$, $r_X$ is physical rate (ms$^{-1}$),
$v_X$ dimensionless mean voltage, and $\tau_X$ membrane time (ms);
dots denote physical-time derivatives:
''')
block('with second-order synaptic activations', 'We integrate with fixed-step RK4', r'''
The synaptic rates $r_E^{\rm syn}=\hat K_a[r_E]$ and
$r_I^{\rm syn}=\hat K_g[r_I]$, with times $\tau_a$ and $\tau_g$,
obey the critically damped operator
$\tau_s^2\ddot r_{\rm syn}+2\tau_s\dot r_{\rm syn}+r_{\rm syn}=r$.
Here $J$ is dimensionless global gain; weights
$(w_{EE},w_{EI},w_{IE},w_{II})=(1,1,1,2)$ use target/source indices,
with doubled inhibitory self-coupling as the only asymmetry.
In the schematic, $\mathcal U_j(t)$ denotes neuron $j$'s total synaptic
and field input, and $J^*$ the coupling-induced Hopf.

The background $\bar\eta$ controls a supercritical Hopf opening a gamma
cycle, analogous to the JR alpha Hopf. The field enters the E-voltage
equation as $I_E(t)=\lambda_I E(t)$ \cite{ruffini2021nmm2}.
The instantaneous coupling $\lambda_I$ has units of normalized drive per V/m;
two tones at $f_c\mp\Delta f/2$ have amplitude $A_f$ in the same
dimensionless drive units as $\bar\eta$. We set $f_c=300$~Hz and sweep
$\Delta f$ through gamma. The membrane integrates each tone into an
excursion $A_f/(\omega\tau_E)$, which $v_E^2$ rectifies: access uses
$\tau_m=\tau_E$, without an assumed sigmoid.
''')
block('As in JR, either background drive or coupling', r'\ifjne\else'+'\n'+r'\input{planning/parts/ping_sweep_settings}', r'''
The resonance map varies $\bar\eta$ (Fig.~\ref{fig:nmm2_map}); the
J-curve varies $J$ at fixed $\bar\eta$ toward $J^*$ and measures the
peak rate lock-in over $\Delta f$ (Fig.~\ref{fig:nmm2_jcurve}).
Both Hopfs are located by bisection of the leading Jacobian eigenvalue.
Unlike JR, the PING J-curve does not pin the operating point. At
$\bar\eta=0$, continuation tracks the critical pair defining $\gamma$,
even when another mode dominates. The linear reference includes the
state-dependent source and full transfer; grids, amplitude checks, and
normalizations are supplementary (\S\ref{supp:ping-runs}).
''')
block('NMM2 is the exact infinite-population mean field', 'We also run both conditions', r'''
We simulate the all-to-all QIF network whose infinite-population limit is
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
''')
block('The network is integrated with Euler steps', 'A cutoff-free check uses', r'''
Euler integration uses $0.0025$~ms steps and $800$~ms settling, exceeding
four field-free relaxation times at $\bar\eta=0.85$ ($176$~ms).
Measurements cover whole beat cycles to avoid phase-coverage bias:
$44$ at $55$~Hz and $34$ at $42$~Hz ($800$ and $810$~ms).
We report the rate lock-in as modulation depth
$A_\Omega/\langle r_E\rangle$; an off/on ratio would divide by the
field-free floor. Single-neuron locking is measured by pairwise phase
consistency (PPC) at $\Delta f$, unbiased in spike count
\cite{vinck2010}, for neurons with at least ten spikes per window.
''')

# Results retain numerical outcomes; remove repeated derivation or setup.
block('At fixed post-coupling polarization the demodulated', r'\begin{figure}[t!]'+'\n'+r'\centering'+'\n'+r'\includegraphics[width=\textwidth]{fig_carrier_independence.pdf}', r'''
At fixed post-access polarization, the open-loop detector and near-Hopf
JR column are carrier-independent outside their natural band
(Fig.~\ref{fig:carrier}). At fixed applied field, the point-membrane
response instead falls as $1/f_c^2$ above its corner; the point and cable
attenuation estimates of \S\ref{sec:khz} are compared in Fig.~\ref{fig:khz}.
''')
block('We also drive the full recurrent column with a kHz field', 'Figure~\\ref{fig:feasibility} converts', r'''
With an explicit first-order access state per modeled compartment before
the sigmoid, the full JR column demodulates and resonates in the assumed
$\tau=0.2$~ms case (Fig.~\ref{fig:khz_direct}a). Genuine tones centered
at $2$~kHz generate the absent $10.914$~Hz beat, with analytic access
factor $|H_m|^2=0.137$ (Fig.~\ref{fig:khz_twotone}). This tests the
specified fast-access hypothesis and coupling.
''')
block('Changing connectivity at a fixed field-free operating point', r'\begin{figure}[t!]'+'\n'+r'\centering'+'\n'+r'\includegraphics[width=\textwidth]{fig_jcurve.pdf}', r'''
With $v^*=8.30$~mV pinned by adjusting $p(C)$, the curvature and open-loop
beat $A_{\rm open}\simeq\half|\Sig''(v^*)|\varepsilon^2m$ stay fixed.
As $C\to C^*\approx137$, the damping tends to zero, the beat response
grows about $30$-fold, and its resonance sharpens (Fig.~\ref{fig:jcurve}a,b).
The rate-to-voltage gain $A_\Omega/A_{\rm open}$ (mV\,s) follows
$1/\gamma$ before saturating (panel~c). Approaching the Hopf through $p$
gives similar leading scaling. Finite-distance gains can differ because
modal frequencies and input--output projections vary along each path.
''')
block('Pinning $v^*$ to hold the local detector', 'The demodulator feeds the network', r'''
In the pinned JR coupling sweep, genuine two tones at $\Delta f=f_0$
increase modulation of $r_P=\Sig(v+s)$ by $13.2$-fold ($26$ to $339$~mHz),
following $1/\gamma$ before saturation. The same rate's mean shift grows
$4.4$-fold ($-1.8$ to $-7.7$~mHz), remaining below $0.2\%$ of its
$3.9$~Hz baseline (Fig.~\ref{fig:timing}). Their magnitude ratio rises
from $14.5$ to $58$ near $\gamma=1$~s$^{-1}$, then falls to $44$ as
the amplified oscillation rectifies. Thus a small mean change accompanies
larger beat modulation, consistent with primate observations
\cite{vieira2024}, with both compared in rate units. The surrogate
comparison is supplementary (\S\ref{supp:waveform-checks}).
''')
block('The exact PING mean field generates and amplifies', 'This derived detector lies', r'''
With genuine $300$~Hz tones entering E current, the PING rate $r_E$
shows forced gamma resonance below the Hopf and a beat response superposed
on autonomous gamma above it (Figs.~\ref{fig:nmm2_res},~\ref{fig:nmm2_map}).
The ridge intensifies through the Hopf and shifts with state, making it
diagonal, unlike the JR example \cite{clusella2023}.
''')
block('At $\\bar\\eta=1.5$, gamma activity is already present', 'The beat and ongoing gamma mix', r'''
At $\bar\eta=1.5$, autonomous gamma near $53$--$54$~Hz remains about
four times larger than the $42$~Hz beat component with stimulation
(panel~d). Their coexistence produces slower burst-height variations.
The inset's beat-phase average suppresses non-beat-locked gamma and exposes
the smaller component; it does not show the full rate variation.
''')

path.write_text(text)
(Path(__file__).parent/'methods_results_replacements.json').write_text(json.dumps(changes,indent=2)+'\n')
print(f'Applied {len(changes)} paragraph-block replacements.')
