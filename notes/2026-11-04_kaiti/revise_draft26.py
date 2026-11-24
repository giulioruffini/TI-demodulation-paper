"""Apply approved, bounded draft26 changes and retain each replacement for review."""
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[2]
P=ROOT/'TN0484_envelope_demodulation.tex'
s=P.read_text();changes=[]
def replace(tag,old,new):
 global s
 assert s.count(old)==1,(tag,s.count(old))
 s=s.replace(old,new);changes.append({'id':tag,'before':old,'after':new})
replace('edition',r'\newcommand{\paperver}{0.15.0-draft25}',r'\newcommand{\paperver}{0.15.0-draft26}')
s=s.replace('October 30, 2026','November 4, 2026').replace('2026-10-30','2026-11-04')
replace('fem_table_caption',r'''\caption{\textbf{Hippocampal maps under current-ratio changes.} Means refer to the
ROI; contrasts are ROI/reference 95th-percentile ratios. Parentheses give
square-root, degree-matched contrasts. Focus shifts use the top 10\% of ROI
nodes, with anterior positive; ranges over other fractions are supplementary.}''',r'''\caption{\textbf{Hippocampal maps under current-ratio changes.}
Contrasts divide the ROI p95 or raw mean by the reference p95; parentheses
give square-root, degree-matched p95 contrasts. Focus shifts use the top
10\% of ROI nodes, anterior positive; ranges over other fractions are supplementary.}''')
replace('fem_table',r'''\begin{tabular}{@{}lrrrrr@{}}
\toprule
Map & Mean, 1:1 & Contrast, 1:1 & Contrast, 1:3 & Mean change & Focus shift\\
\midrule
Envelope & $0.16$ mV & $1.22$ & $0.95$ & $-45\%$ & $+2.5$ mm\\
Quadratic beat & $0.018$ mV$^2$ & $1.17$ ($1.08$) & $1.17$ ($1.08$) & $-25\%$ & $0$ mm\\
Mean square & $0.0094$ mV$^2$ & $0.92$ ($0.96$) & $0.90$ & $+24\%$ & $-4.5$ mm\\
\bottomrule
\end{tabular}''',r'''\setlength{\tabcolsep}{4pt}
\begin{tabular}{@{}lrrrrrr@{}}
\toprule
Map & \shortstack{ROI mean\\1:1} & \shortstack{p95 contrast\\1:1} &
\shortstack{p95 contrast\\1:3} & \shortstack{Mean contrast\\1:1 / 1:3} &
\shortstack{Mean\\change} & \shortstack{Focus\\shift}\\
\midrule
Envelope & $0.16$ mV & $1.22$ & $0.95$ & $0.81\,/\,0.58$ & $-45\%$ & $+2.5$ mm\\
Quadratic beat & $0.018$ mV$^2$ & $1.17$ ($1.08$) & $1.17$ ($1.08$) & $0.61\,/\,0.61$ & $-25\%$ & $0$ mm\\
Mean square & $0.0094$ mV$^2$ & $0.92$ ($0.96$) & $0.90$ ($0.95$) & $0.47\,/\,0.54$ & $+24\%$ & $-4.5$ mm\\
\bottomrule
\end{tabular}
% Ricardo's gray-matter-only contrasts will be added here once supplied and verified.''')
replace('fem_tail',r'''envelope's $1.22$, while mean-square polarization favors the reference. These modest contrasts
separate geometric predictions but do not establish physiological deep selectivity.''',r'''envelope's $1.22$, while mean-square polarization favors the reference.
The envelope's above-reference-p95 tail has an anterolateral centroid and is
52\% white matter, compared with 25\% across the ROI.
These modest contrasts separate geometric predictions but do not establish
physiological deep selectivity.''')
replace('fem_caption_colors',r'''(line), range over 5--50\% (band). \emph{(g)} Contrasts''',r'''(line), range over 5--50\% (band), colors as in (e). \emph{(g)} Contrasts''')
replace('future_data_license',r'''the per-node export and its comparison with the published statistics remain
pending. Input hashes, settings, and export instructions are recorded in''',r'''the per-node export and its comparison with the published statistics remain
pending; when released, the data file will carry a separate CC BY-SA 4.0 license
with IXI attribution. Input hashes, settings, and export instructions are recorded in''')
replace('ixi_acknowledgment',r'''GALVANI).
% RS support confirmed''',r'''GALVANI).
We acknowledge the \href{https://brain-development.org/ixi-dataset/}{IXI dataset}
(CC BY-SA 3.0) for the IXI002 MRI.
% RS support confirmed''')
# The source equation already contains both terms; name their joint interpretation once.
replace('joint_sources',r'''giving a signed beat-source amplitude''',r'''giving a steady source from the summed squares and a signed beat-source amplitude''')
replace('joint_sources_following',r'''in s$^{-1}$ before recurrence, alongside the steady (DC) source.''',r'''in s$^{-1}$ before recurrence.''')
# Move the operating-point interpretation beside the steady-source sign, preserving its examples.
a=s.index(r'\subsection{Operating-point dependence}\label{sec:opp}')
b=s.index(r'\subsection{The exact mean field extends the static detector}',a)
old=s[a:b]
peix=r'''\label{sec:opp}
The Population Excitation--Inhibition Index (PEIX) \cite{ruffini2025cfc}
measures signed departure from maximal sigmoid slope, positive above the
inflection and negative below; its definition and curvature identities are
in Appendix~\ref{app:peix}. Changes in $v^*$ through neuromodulation,
attention, arousal, psychedelic exposure, or dysfunction of PV interneurons
in Alzheimer's disease can scale or reverse the static JR source.
Dynamic detectors have their own coefficients and susceptibilities, without
a universal PEIX sign rule; state sweeps isolate detection only if recurrent
gain is also measured.

'''
s=s[:a]+s[b:];changes.append({'id':'operating_point_relocation','before':old,'after':peix,'destination':'sec:dc after static sign/polarity paragraph'})
anchor='This curvature rule applies to static detection; dynamic rectification and\nrecurrence can change the sign of the mean response.\n\n'
assert s.count(anchor)==1;s=s.replace(anchor,anchor+peix)
replace('curvature_zero_scope',r'''negative sources, respectively, with zero quadratic source at the inflection.''',r'''negative sources, respectively; the quadratic source vanishes at the inflection
and in the saturated tails.''')
# Prediction, estimation, and experimental design keep distinct jobs.
replace('harmonic_method_open',r'''We sweep amplitude at fixed coupling and operating state, measuring the
fundamental and second harmonic to test the laws of \S\ref{sec:transduction}.''',r'''At fixed coupling and operating state, we measure the fundamental and second
harmonic across an amplitude sweep.''')
replace('harmonic_method_scope',r'''with their amplitude ratio corrected by $|G(2\Omega)/G(\Omega)|$. The amplitude sweep tests
linear versus quadratic scaling. Estimating a mixture coefficient through
Eq.~\eqref{eq:rdet} assumes the mixed detector family and its
sign branch; a threshold detector can match one harmonic ratio.''',r'''with their amplitude ratio corrected by $|G(2\Omega)/G(\Omega)|$.
Estimating a mixture coefficient through Eq.~\eqref{eq:rdet} assumes the mixed
detector family and its sign branch.''')
replace('harmonic_prediction_ambiguity',r'''therefore needed; one harmonic ratio cannot identify the detector.''',r'''therefore needed; a threshold detector can match one harmonic ratio, so that
ratio alone cannot identify the detector.''')
replace('harmonic_discussion_setup',r'''Network filtering must be separated from the harmonic signature. At resonance
with $\mathcal Q=10$,''',r'''At resonance with $\mathcal Q=10$,''')
replace('test_table_harmonic_repeat',r'''resonance or correct their network gains; a single harmonic ratio is insufficient.''',r'''resonance or correct their network gains.''')
# Keep all JR protocol facts, alongside the model they concern.
a=s.index(r'\subsection{Coupling sweeps, timing, and the tACS control (Jansen--Rit)}')
b=s.index(r'\section{Results}',a);old=s[a:b]
new=old[old.index('For each\nconnectivity'):]
new=new.replace('For each\nconnectivity','For each connectivity',1)
s=s[:a]+s[b:]
anchor=r'\subsection{Exact next-generation mean field (NMM2 PING)}';assert s.count(anchor)==1;s=s.replace(anchor,new+'\n'+anchor)
changes.append({'id':'jr_methods_relocation','before':old,'after':new,'destination':'end of sec:jr-methods'})
replace('jr_results_heading',r'''\subsection{Coupling sets the gain at fixed detection}\label{sec:jcurve}''',r'''\subsection{JR gain, mean shifts, and the tACS comparison}\label{sec:jcurve}''')
replace('jr_timing_heading',r'''\subsection{Resonance favors beat modulation over the mean shift}\label{sec:timing}''',r'''\paragraph{Beat modulation and mean rate.}\label{sec:timing}''')
replace('jr_tacs_heading',r'''\subsection{TI and tACS share the linear amplifier}\label{sec:tacs-results}''',r'''\paragraph{Comparison with tACS.}\label{sec:tacs-results}''')
replace('jr_gain_open',r'''With $v^*=8.30$~mV pinned by adjusting $p(C)$, the curvature and open-loop
beat $A_{\rm open}\simeq\half|\Sig''(v^*)|\varepsilon^2m$ stay fixed.
As $C\to C^*\approx137$, the damping tends to zero, the beat response
grows about $30$-fold, and its resonance sharpens (Fig.~\ref{fig:jcurve}a,b).
This is a network effect: the local detector curvature is fixed while
the recurrent transfer changes.''',r'''Pinning $v^*=8.30$~mV through $p(C)$ fixes the curvature and open-loop
beat $A_{\rm open}\simeq\half|\Sig''(v^*)|\varepsilon^2m$.
As $C\to C^*\approx137$, damping tends to zero, the response grows about
$30$-fold, and resonance sharpens (Fig.~\ref{fig:jcurve}a,b).
This isolates a network effect: recurrent transfer changes at fixed detector curvature.''')
replace('jr_timing_open',r'''In the pinned JR coupling sweep, genuine two tones at $\Delta f=f_0$''',r'''With genuine two tones at $\Delta f=f_0$, the same pinned sweep''')
# Correct agreement after the shorter subject.
replace('jr_timing_verb',r'''the same pinned sweep
increase modulation''',r'''the same pinned sweep
increases modulation''')
replace('tacs_setup',r'''TI and direct low-frequency stimulation share the same linear amplifier.
Matching their generated in-band drives therefore matches their linear outputs;
resonance alone gives TI no efficiency advantage.''',r'''At a common state, matching the generated in-band TI and tACS drives matches
their linear outputs; resonance alone gives TI no efficiency advantage.''')
replace('tacs_transfer_repeat',r'''The common transfer cancels when both responses are linear about the same
state. For the stated unequal inputs, the predicted ratio is $0.143$;''',r'''The common linear transfer cancels. For the stated unequal inputs the ratio is $0.143$;''')
replace('jr_caption_role',r'''AM surrogate, Eq.~\eqref{eq:amsur}; adjusting $p(C)$ pins the field-free
state, curvature $\Sig''(v^*)=-0.151$~s$^{-1}$mV$^{-2}$, and open-loop
source $A_{\rm open}$. \emph{(a,b)} The response grows and sharpens as
$C$ approaches the Hopf $C^*$ from the stable-focus side ($\gamma>0$).
\emph{(c)} Rate-to-voltage gain $A_\Omega/A_{\rm open}$ (mV\,s) follows
$1/\gamma$ (dashed) before saturating.''',r'''AM surrogate, Eq.~\eqref{eq:amsur}, with $p(C)$ pinning the field-free state,
curvature $\Sig''(v^*)=-0.151$~s$^{-1}$mV$^{-2}$, and source $A_{\rm open}$.
\emph{(a,b)} Response magnitude and resonance width on the stable-focus side
of $C^*$ ($\gamma>0$). \emph{(c)} Rate-to-voltage gain
$A_\Omega/A_{\rm open}$ (mV\,s); dashed: $1/\gamma$.''')
# Keep unique comparison and numerical statements; shorten only their repeated setup.
replace('direct_shared_transfer',r'''At a common state and entry point, matched sources give matched leading
circuit responses. Steady sources share the zero-frequency transfer; beat
and tACS sources share the transfer at $\Omega$. These transfers differ,
and rectification of the amplified TI beat can add a mean shift.
The local source comparison therefore specifies
neither a universal physiological-effect ratio nor equal spatial responses.''',r'''At a common state and entry point, matched steady sources share the
zero-frequency transfer, and matched beat and tACS sources share the transfer
at $\Omega$. These differ, and the amplified TI beat can rectify further.
Source ratios therefore imply neither universal physiological-effect ratios
nor equal spatial responses.''')
P.write_text(s)
(ROOT/'notes/2026-11-04_kaiti/draft26_replacements.json').write_text(json.dumps(changes,indent=2)+'\n')
print(f'Applied {len(changes)} bounded replacements/relocations; full before/after record retained.')
