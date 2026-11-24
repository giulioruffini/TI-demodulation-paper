from pathlib import Path
import re
p=Path('TN0484_envelope_demodulation.tex');s=p.read_text()
def sub(a,b):
 global s
 assert a in s,a[:100]
 s=s.replace(a,b,1)
sub('Section, equation and\nfigure numbers referenced here follow the main text; supplementary figures are numbered\nS1, S2, \\dots','Supplement equations and figures are numbered S1, S2, \\dots;\nreferences to article equations are marked as main-text references.')
sub('\\ifappendices\n\\renewcommand{\\thefigure}', '\\ifappendices\n\\renewcommand{\\theequation}{S\\arabic{equation}}\n\\setcounter{equation}{0}\n\\renewcommand{\\thefigure}')
sub('Our mesoscale model separates the cellular beat source from recurrent gain.', 'Our mesoscale model separates access, the cellular beat source, and recurrent gain\n(Fig.~\\ref{fig:concept}).')
sub('\\input{figures_src/fig_models_ti_caption.tex}\n','')
anchor='\\subsection{From applied field'
pos=s.index(anchor)
s=s[:pos]+'Figure~\\ref{fig:models} locates the field input, nonlinear detector, and\nrecurrent amplifier in the JR and QIF circuits.\n\\input{figures_src/fig_models_ti_caption.tex}\n\n'+s[pos:]
sub('$(Fig.~\\ref{fig:carrier})','$') if False else None
sub('to about $2.5\\%$\n(Fig.~\\ref{fig:carrier}).','to about $2.5\\%$.')
sub('inflection (Fig.~\\ref{fig:opp}).','inflection.')
sub('In the latter description, the approach to a static transfer is governed by\nEq.~\\eqref{eq:slow_synapse}; the membrane filter must not be applied again outside\nthe QIF equations.', 'A QIF reduction computes the access filter within its membrane equation,\nso no additional membrane filter is applied to its current input.')
sub('In membrane-time units, the fast-carrier QIF voltage source has $D=1$;\n$G$ then includes its conversion through the voltage and rate dynamics.', 'For the QIF mixer, the role of $\\Sig\'\'/2$ is played by the unit coefficient\nof $v^2$ in membrane-time units. The voltage and rate dynamics that convert\nthis source into a rate beat belong to the response $G$.')
sub('The access filter is included in the supplied polarization or computed by\nthe membrane equation when its input is current; applying both would count\nthe same attenuation twice.','The supplied polarization includes the access response.')
a=s.index('with dimensionless modulation depth $m$, because');b=s.index('\\subsection{Amplitude scaling',a)
s=s[:a]+r'''with dimensionless modulation depth $m$. This AM surrogate parameterizes dense
resonance and coupling sweeps by one amplitude. It contains a central carrier
line absent from genuine TI, but matches its leading beat source:
$Y_\Omega=\half\Sig''\varepsilon^2m$. For matched genuine tones,
$\mathrm{LPF}[s^2]=\varepsilon^2(1+\cos\Omega t)$; for the $m=1$ surrogate,
$\mathrm{LPF}[s^2]=\varepsilon^2(\tfrac34+\cos\Omega t+\tfrac14\cos2\Omega t)$.
Thus the mean source differs, and the surrogate adds a second harmonic at
$25\%$ of the fundamental. We use genuine tones for the demodulation,
curvature, square-law, laminar, and kHz demonstrations, and wherever mean shifts
or harmonics enter the comparison: timing versus rate and the TI/tACS and
NMM2 endpoint controls. Open-loop agreement at the beat is checked at one
operating point; it does not imply equal driven operating states.

'''.replace('\\','\\')+s[b:]
# Protocol citations should not introduce Results figures ahead of their narrative.
sub('The resonance sweep in Fig.~\\ref{fig:res} uses','The resonance sweep uses')
sub('law\n(Figs.~\\ref{fig:carrier},~\\ref{fig:opp},~\\ref{fig:khz});','law;')
# Move detailed endpoint settings intact beside the retained stability results.
a=s.index('We check the stability of the driven $J$-curve endpoint');b=s.index('\\subsection{QIF spiking',a)
protocol=s[a:b].strip();s=s[:a]+'''Stability of the driven endpoint is checked using period-to-period perturbation
multipliers, direct perturbation decay, and a finite-time Lyapunov estimate;
settings and results are given in Appendix~\\ref{app:ping-stability}.

'''+s[b:]
sub('\\subsection{Stability of the driven PING endpoint}\\label{app:ping-stability}', '\\subsection{Stability of the driven PING endpoint}\\label{app:ping-stability}\n'+protocol+'\n')
sub('whole curve. This refines the coupling-controlled sensitivity expected in QIF\nnetworks \\cite{clusella2023}: both coupling and rectifier are derived, but the\ndominant mode can change.', 'whole curve. Coupling-dependent sensitivity \\cite{clusella2023} therefore\nincludes changes in which mode carries the peak.')
sub('The fully forced endpoint remains attracting under both waveforms, even\nwhere a DC-only approximation predicts instability; $\\gamma$ describes the\nfield-free mode. The gain reference includes the state-dependent detector.', 'The driven endpoint remains attracting under both waveforms\n(Appendix~\\ref{app:ping-stability}).')
sub('consequence follows from the slow-synapse limit without adding a periaxonal circuit.', 'consequence follows from the slow-synapse limit.')
a=s.index('Changing from $2+2$ to $1+3$~mA multiplies');b=s.index(' \\\\[4pt]',a)
s=s[:a]+s[b:]
sub('transfers (Eq.~\\eqref{eq:etasup}).','transfers (Appendix~\\ref{app:bound}, Eq.~\\eqref{eq:etasup}).')
# Disambiguate every equation reference from supplement to article.
a=s.index('\\ifappendices\n\\renewcommand{\\theequation}')
main=set(re.findall(r'\\label\{(eq:[^}]+)\}',s[:a]))
tail=s[a:]
for label in main:
 tail=tail.replace('Eq.~\\eqref{'+label+'}', '\\ifsupp main-text\\fi\\ Eq.~\\eqref{'+label+'}')
s=s[:a]+tail
p.write_text(s)
p=Path('planning/tn0484_notation.tex');s=p.read_text().replace('Numbered references\nidentify main-text definitions; lettered locations identify appendices (in the\nsupplement for the JNE edition).','Equation numbers prefixed by S identify supplement definitions; unprefixed\nnumbers identify main-text equations. Lettered locations identify appendices.');p.write_text(s)
