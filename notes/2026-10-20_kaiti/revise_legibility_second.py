"""Second source-only pass: captions and connected prose."""
from pathlib import Path
import re
ROOT=Path(__file__).resolve().parents[2]
P=ROOT/"TN0484_envelope_demodulation.tex"
s=P.read_text()
def rep(a,b):
    global s
    assert a in s, a[:100]
    s=s.replace(a,b,1)
def block(a,b,new):
    global s
    i,j=s.index(a),s.index(b)
    s=s[:i]+new+s[j:]
def caption(label,new):
    global s
    end=s.index(r"\label{"+label+"}")
    start=s.rfind(r"\caption{",0,end)
    s=s[:start]+r"\caption{"+new+"}\n"+s[end:]

rep("dimensionless connectivity scale\n. \n", "dimensionless connectivity scale.\n\n")
rep("For fast-carrier QIF in the normalized units of Eq.~\\eqref{eq:mpr}, $D=1$ for\n"
    "the $v^2$ source and $G$ includes its conversion through the voltage and rate\n"
    "dynamics. Thus the population readout is included once.",
    "In membrane-time units, the fast-carrier QIF voltage source has $D=1$;\n"
    "$G$ then includes its conversion through the voltage and rate dynamics.")
rep("The passive compartment equations in\nApp.~\\ref{app:access} give both factors from the same voltage response.\n", "")
rep("The geometric maps precede detector\n"
    "gains: an ideal envelope follower multiplies $\\mathcal A$ by its specified gain\n"
    "$c_1$, whereas the weak quadratic response change is $g''(v^*)\\mathcal A^2/4$\n"
    "(Eq.~\\eqref{eq:cycavg}); for the JR column, $g=\\Sig$.",
    "The geometric maps precede detector gains: an ideal envelope follower has\n"
    "response $c_1\\mathcal A$ for a specified gain $c_1$. A smooth transfer $g$\n"
    "with nonzero curvature gives the weak response $g''(v^*)\\mathcal A^2/4$;\n"
    "for the JR column, $g=\\Sig$.")
rep("The square-law signature is a\n\\emph{vanishing} ratio in the weak-field limit, not an exact zero.",
    "The square-law signature is a harmonic ratio tending to zero with input strength.")
rep(" (App.~\\ref{app:bound})", "")
rep("\n(App.~\\ref{app:sl}).", ".")
rep("(App.~\\ref{app:access}, Eq.~\\eqref{eq:lambda}).",
    "for a sufficiently long, sealed cable in a uniform axial field.")
rep("Equation~\\eqref{eq:crossover} gives the QIF realization of this response.\n", "")
rep("A gate\nfilter added outside the detector must not duplicate dynamics the detector already\n"
    "contains, and where the detector lacks them, as QIF lacks sodium-channel kinetics,\n"
    "the filter needs its own model or measurement; neither a static sigmoid nor QIF\n"
    "specifies a universal $1$~kHz gate cutoff.",
    "Any separate gate filter needs a model or measurement and must represent\n"
    "kinetics absent from the detector. QIF, for example, lacks explicit sodium-channel\n"
    "kinetics. Neither QIF nor a static sigmoid specifies a universal $1$~kHz cutoff.")
rep("The field acts directly on soma, dendrites, AIS, nodes, and terminals,\n"
    "each with its own coupling and frequency response. In a reduced description, their\n"
    "contributions to the effective input are represented by parallel entry points.",
    "Soma, dendrites, AIS, nodes, and terminals have different couplings and\n"
    "response times. We represent their contributions as parallel inputs.")
rep("Fast axonal access motivates\nthis limit; compartment anatomy enters the reduced model through\n"
    "the coupling and response time, which must be calibrated for the preparation.",
    "Fast axonal compartments motivate the direct-coupling approximation\n"
    "$\\lambda_f\\approx\\lambda_0$; their coupling and response time require\n"
    "calibration in the preparation.")

# Shorten captions by retaining the interpretive content in neighboring prose.
caption("fig:demod", r"""\textbf{The JR column generates a beat absent from the input.}
\emph{(a)} Two equal tones at $94.45$ and $105.55$~Hz and their envelope,
$2\varepsilon|\cos(\Omega t/2)|$. \emph{(b)} Input spectrum: only the two
tones are present. The alpha-band floor is $1.6\times10^{-8}$ of their
amplitude, from finite-window leakage. \emph{(c,d)} The synaptic voltage
$v=y_1-y_2$ and its spectrum show the generated $11.1$~Hz beat.
The field-free column is a stable focus near its alpha Hopf.""")
caption("fig:res", r"""\textbf{The JR beat resonance sharpens toward the Hopf.}
Stable-focus response at $\varepsilon=0.3$~mV. \emph{(a)} Lock-in amplitude
against beat frequency; the finite-amplitude peak moves from $11.08$ to
$10.93$~Hz across the curves. \emph{(b)} Peak amplitude increases as $p$
approaches the upper Hopf from above. These three points show sharpening
and growth; the coupling sweep quantifies the $1/\gamma$ scaling and
its saturation.""")
rep("On the alpha branch below $p_H$,", 
    "The peak shifts with the driven operating state; the near-Hopf law gives\n"
    "its leading gain, not its exact frequency. The coupling sweep tests that law\n"
    "over a decade of damping.\nOn the alpha branch below $p_H$,")
caption("fig:opp", r"""\textbf{Curvature determines the JR detector.}
\emph{(a)} The signed open-loop beat follows
$\Sig''(v^*)\varepsilon^2/2$ within $0.9\%$, vanishing and reversing sign
at $v_0$. \emph{(b)} The recurrent response has amplitude slope $1.99$.
\emph{(c)} Linearizing the receiving sigmoid reduces the beat $634$-fold.
\emph{(d)} Open-loop two-tone/AM beat ratio at $v^*=8$~mV:
$1.0000$ at $0.02$~mV and $0.988$ at $1$~mV. This checks the leading
local source, not the nonlinear recurrent response near the Hopf.""")
rep("and the closed-loop operating points sit where $\\Sig''$ is large\nand negative.",
    "and the closed-loop operating points sit where $\\Sig''$ is large and negative.\n"
    "Changing its sign reverses the source phase; at matched network susceptibility,\n"
    "its magnitude sets the same resonant-gain calculation on either flank.")
caption("fig:fem", r"""\textbf{Envelope and quadratic maps in IXI002.}
Violante montage; left hippocampus outlined in gold, anterior to the left.
\emph{(a--d)} Sagittal maps at $2+2$~mA (top) and $1+3$~mA (bottom):
envelope excursion, quadratic excursion, mean-square polarization, and
isotropic beat. The first three use the fixed 1:1 envelope-maximizing
direction. Each color scale ends at its 1:1 gray-matter 99th percentile.
Circles and triangles mark the projected top-10\% focus at 1:1 and 1:3.
\emph{(e)} Target-to-reference contrast; dashed curves use square-root
maps to match degree. \emph{(f)} Anterior focus displacement: top 10\%
(line), range over 5--50\% (band). \emph{(g)} Contrasts at 1:1, raw
(solid) and degree-matched (hatched).
The reference is gray matter outside the ROI. All maps precede detector
gain: $\mathcal I$ weights $Y_{\rm DC}=\Sig''\mathcal I/2$, but does not set its sign.""")
caption("fig:qif_raster", r"""\textbf{Beat-locked activity superposed on gamma.}
QIF network, $N=8000$ per population, $A_f=35$ per tone, carrier $300$~Hz.
Black ticks: 400 E neurons; blue: smoothed rate on its own scale; red:
envelope in arbitrary units. The last $200$~ms are shown.
\emph{(a,b)} Field off/on at $\bar\eta=0.85$, beat $55$~Hz: induced gamma
near $52$~Hz dominates. \emph{(c,d)} Field off/on at $\bar\eta=1.5$,
beat $42$~Hz: autonomous gamma remains dominant.
Insets fold rate on beat phase over $44$ and $34$ cycles, respectively,
normalized to each condition's mean (off gray, on blue; scale 0--2).
Folding suppresses non-beat-locked gamma and exposes the smaller beat component;
it does not establish gamma-amplitude gating or phase capture.""")
caption("fig:qif_regimes", r"""\textbf{TI and an equal-power carrier across the gamma threshold.}
Background $\bar\eta=0.85$, carrier $300$~Hz, beat $55$~Hz.
\emph{(a,b)} Spiking network at $A_f=10$ and $35$ per tone.
Black: 400 of 8000 E neurons; blue: population rate on a common scale;
red: envelope. Insets show mean-normalized phase folds (off gray, on blue).
Beat depths are $0.093$ and $0.290$, with mean-rate increases of $2.8\%$
and $10.5\%$; the larger input also induces gamma.
\emph{(c,d)} Mean-field spectra under TI (blue) and one carrier of peak
amplitude $\sqrt2 A_f$ (red), normalized to mean rate. Both induce gamma
at the larger input; TI adds the $55$~Hz beat (dashed).
Hann windows span $800$~ms after $800$~ms settling.
Spiking panels use $V_{\rm peak}=100$; weak-drive depth remains cutoff-sensitive.""")
rep("response. The control separates induction of an oscillation from its\n"
    "beat-frequency response; it has not been run in the spiking network.",
    "response. A longer window reduces the single carrier's apparent $55$~Hz\n"
    "depth from $0.011$ to $9.2\\times10^{-5}$, while TI's stays at $0.30$--$0.31$;\n"
    "the former is spectral leakage. The equal-power control separates induction\n"
    "of gamma from the beat response and has been tested only in the mean field.")
caption("fig:nmm2_jcurve", r"""\textbf{Coupling changes the dominant mode and its gain in NMM2.}
Unpinned sweep at $\bar\eta=0$, AM surrogate $A_f=8$.
\emph{(a)} Simulated rate peak (blue) and linear reference including the
second-order source (gray), normalized over $14.5<J<16$. Red dashed:
field-free Hopf. \emph{(b)} Gain against inverse damping of the critical
mode. Filled symbols: that mode carries the linear peak; open symbols:
the competing $55$~Hz mode carries it ($14.6\lesssim J\lesssim16.2$).
The dashed $1/\gamma$ guide is anchored at the last linear point.
The simulation exceeds then falls below the guide. The driven endpoint
remains attracting under both AM and genuine two-tone forcing.""")
caption("fig:timing", r"""\textbf{Beat modulation grows more than the mean-rate shift.}
JR coupling sweep with fixed field-free curvature and genuine two-tone
input, $\Delta f=f_0$. Both observables use the pyramidal rate
$r_P=\Sig(v+s)$, in mHz.
\emph{(a)} Beat amplitude (blue) follows $1/\gamma$ (dashed) before
saturating; mean-shift magnitude (red) remains smaller.
\emph{(b)} Normalization to the far-from-Hopf values gives growth factors
$13.2$ and $4.4$. Their ratio rises from $14.5$ to $58$ near
$\gamma=1$~s$^{-1}$, then falls to $44$ as the amplified response rectifies.
The AM surrogate gives ratios $19$, $66$, and $45$.""")

# Put the schematic beside the model equations. Its detailed pathway explanation
# is already supplied by the equations and definitions in Methods and Appendix B.
rep("The common background drive $\\bar\\eta$ is the bifurcation parameter:",
    "\\input{figures_src/fig_models_ti_caption.tex}\n\n"
    "The common background drive $\\bar\\eta$ is the bifurcation parameter:")
# Missing symbols from the compressed caption remain explicitly defined here.
rep("The common background drive $\\bar\\eta$ is the bifurcation parameter:",
    "In the schematic, $\\mathcal U_j(t)$ is the total synaptic and field input\n"
    "to QIF neuron $j$, and $J^*$ denotes a coupling-induced Hopf.\n"
    "The common background drive $\\bar\\eta$ is the bifurcation parameter:")
rep("integrated as six first-order ODEs; the LFP proxy is",
    "The excitatory and inhibitory impulse responses are\n"
    "$h_e(t)=Aa\\,t e^{-at}$ and $h_i(t)=Bb\\,t e^{-bt}$ for $t\\ge0$.\n"
    "The equations are integrated as six first-order ODEs; the LFP proxy is")

# Discussion: organize interpretation by the scientific question, avoiding a
# single unbroken succession of more than twenty paragraphs.
rep("\\section{Discussion}\\label{sec:discussion}",
    "\\section{Discussion}\\label{sec:discussion}\n"
    "\\subsection{Cellular access and mixing require separate calibration}")
block("Table~\\ref{tab:doors} summarizes", "A spatial TI dose map",
r"""Short access times motivate the model but remain preparation-dependent.
The $1$ and $0.4$~ms cases of \cite{esmaeilpour2021} precede our effective-time
hypothesis. Luff et al.'s pulse-width-modulated TI model uses $1$~ms within a
$1$--$100$~ms passive-time sweep \cite{luff2024}. The $0.7~\mu$s charging
measured by Semenov et al.\ under strong microsecond field pulses
\cite{semenov2025} concerns a different response mode from intracellular
current charging or periaxonal conduction. A $10$--$100$-fold reduction in
QIF membrane time is therefore a sensitivity hypothesis, whose population
consequence follows from the slow-synapse limit without adding a periaxonal circuit.

The quadratic law specifies the leading mixing operation, not its coefficient.
QIF derives one realization; cellular mixing measured or modeled in single
neurons \cite{mirzakhalili2020,luff2024mixer} can feed the recurrent
amplification seen in slices and simulations \cite{caldas2024,karimi2024}.
These are complementary stages. A static curve describes mixing only when
population relaxation is fast relative to the carrier as well as the synapses.
Otherwise the coefficient retains its own frequency dependence, while slope
converts slow input into rate and enters recurrent gain.

\subsection{Detector laws predict different spatial responses}
""")
rep("Its accompanying DC source follows the summed carrier intensities under the\n"
    "conditions of \\S\\ref{sec:dc}, providing an operating-point shift that\n"
    "the equal-RMS carrier control isolates and that can cross the population Hopf\n"
    "(\\S\\ref{sec:qif}).\nBoth idealized mean maps obey the boundary-maximum restriction of\n"
    "\\S\\ref{sec:dc}; the beat map does not.",
    "The accompanying steady source follows the summed carrier intensities,\n"
    "weighted by the local detector coefficient. Under uniform conductivity,\n"
    "access, and detection, its largest magnitude and the ideal envelope mean\n"
    "lie on compartment boundaries. The beat can instead peak inside.")
rep("The mean-square map also predicts a physiological effect: at second order it\n"
    "sets the steady rate source $Y_{\\rm DC}=\\tfrac12\\Sig''(v^*)\\mathcal I$\n"
    "(\\S\\ref{sec:dc}). With spatially uniform, fixed curvature, its 24\\% increase\n"
    "in hippocampal mean predicts a 24\\% larger mean-rate source in magnitude,\n"
    "with the sign set by the curvature. Recurrence then determines the final rate\n"
    "response.",
    "At spatially uniform, fixed curvature, the 24\\% increase in hippocampal\n"
    "mean-square polarization predicts a 24\\% increase in the magnitude of the\n"
    "steady rate source $Y_{\\rm DC}=\\Sig''(v^*)\\mathcal I/2$. Curvature sets\n"
    "its sign; recurrence determines the final rate response.")
rep("This interpretation remains conditional:\n", "The comparison has several physiological conditions. ")
rep("Neither hippocampal curvature nor the\n"
    "recurrent and hemodynamic gains are calibrated here; spatially varying\n"
    "curvature can also change the mean-source ratio. Neither the BOLD contrast\n"
    "nor the reported functional-connectivity changes directly measure the beat\n"
    "or the steady source. The voxelwise pattern therefore cannot be matched to\n"
    "one of these maps without a neural and hemodynamic readout model.",
    "Hippocampal curvature and recurrent and hemodynamic gains are uncalibrated;\n"
    "heterogeneous curvature can change the mean-source ratio. BOLD and functional\n"
    "connectivity measure neither source directly, so interpreting their spatial\n"
    "pattern requires a neural and hemodynamic readout model.")
rep("At higher intensities, TI", "\\subsection{Field-induced oscillations and resonant amplification}\nAt higher intensities, TI")
rep("Absolute response estimates remain sensitive to access and transduction.",
    "\\subsection{Efficiency depends on the generated drive}\n"
    "Absolute response estimates depend on access and transduction.")
rep("Access and mixing require calibration; their values are not fixed by the\n"
    "quadratic law, and cascading ordinary synaptic filters cannot improve access\n"
    "because they attenuate the carrier before a subsequent detector receives it.",
    "\\subsection{Limits of the population description}\n"
    "Cascading ordinary synaptic filters cannot remedy poor access: they attenuate\n"
    "the carrier before it reaches a subsequent detector.")
rep("The smooth JR detector is therefore weak under this access budget, even though\n"
    "recurrence can amplify its output. A measured PLV effect cannot be compared\n"
    "directly with this drive ratio; a polarization-calibrated amplitude sweep with\n"
    "the same readout would test the estimate.",
    "The smooth JR detector generates a small beat under this budget. Recurrence\n"
    "amplifies both TI and matched direct drives, preserving their linear-response\n"
    "ratio. Testing the estimate requires a polarization-calibrated sweep with\n"
    "the same readout; a measured PLV ratio alone does not supply it.")
rep("For scale, a reverberation time", "A reverberation time")
rep("The slope is itself a parameter, so the question is what the whole sigmoid family can do.\n",
    "Optimizing over the sigmoid slope gives a different limit from the weak-input bound.\n")
rep("Such a detector is not weak.", "The limiting detector switches across its full range.")
rep("The obstacle is the width.\nAt", "The required transfer width is small: at")

# Close with the result hierarchy, keeping the distinction between local source,
# network response, and calibrated physiological effects.
block("\\section{Conclusion}", "\\section*{Code and data availability}",
r"""\section{Conclusion}
Weak TI detection with a nonzero second-order coefficient generates a beat
proportional to the product of the local carrier polarizations and a steady
source proportional to their summed squares. At fixed electrode geometry
and neural state, changing the current ratio rescales the quadratic beat
without steering it. The realistic-head comparison separates this behavior
from envelope steering and from the changing mean-square map. Under uniform
conductivity, access, and detection, the steady-source magnitude and ideal
envelope mean have no strict interior maximum.

Fast population relaxation gives a static rate map with dynamic synapses;
static carrier mixing requires relaxation faster than the carrier too.
A short effective membrane time represents access through fast axonal
compartments, motivated by nodal, AIS, and periaxonal mechanisms. It can
coexist with slow circuit resonance, but its TI transfer and the absolute
response at human field strengths remain to be calibrated.

TI and direct low-frequency stimulation share the linear amplifier when
their generated input, observable, and operating state are matched.
Resonance alone gives TI no efficiency advantage. In the pinned JR sweep,
beat-locked rate modulation grows more than the mean shift; their ratio
peaks and then falls as the amplified oscillation rectifies. Finite-amplitude
responses therefore need not retain the linear TI/tACS ratio.

At larger fields, the steady shift can carry the QIF circuit across its
Hopf and induce gamma. An equal-power unmodulated carrier produces the same
transition in the mean-field control, while TI adds the beat response.
Measuring local polarization, generated beat, and circuit gain separately
distinguishes these mechanisms; a large output alone identifies neither
an efficient detector nor its microscopic origin.

""")

# Residual forward section references: replace with the actual content, retaining
# equation/figure citations where they accompany a self-contained explanation.
rep("The sign flip is itself a prediction (\\S\\ref{sec:predictions}). ", "") if "The sign flip is itself" in s else None
rep("Appendix~\\ref{sec:vocab} gives the metrics\nand the frequency-dominance protocol.", "")
rep("cycle and requires phase tracking (\\S\\ref{sec:vocab}).", "cycle and requires phase tracking.")
rep(" (Appendix~\\ref{sec:vocab}),", ",")
rep("The models are written in the NMM1 transfer-function formalism of Eq.~\\eqref{eq:nmm1}\n"
    "\\cite{ruffini2025rosetta}: synaptic operators $\\hat L$ transduce firing rates into PSPs, the\n"
    "PSPs sum with any direct field term $\\Lambda[E]$ in the sigmoid argument, and the sigmoid\n"
    "returns the rate. The Jansen--Rit column is given here; the laminar model is specified in\n"
    "\\cite{ruffini2025cfc,sanchezTodo2023} with its field drive in Eq.~\\eqref{eq:lanmm_drive}, and\n"
    "the NMM2 PING motif and its QIF network in Eq.~\\eqref{eq:nmm2-ping} and \\S\\ref{sec:qif-methods}.",
    "Synaptic operators convert rates into postsynaptic potentials, which sum with\n"
    "the direct field polarization before the rate curve is applied.")
# Correct changed definition locations, and remove stale normalized-coordinate claims.
s=s.replace(r"$F$ of \S\ref{sec:nmm}", r"$F$ of \S\ref{sec:dynamic}")
s=s.replace(r"Eq.~\eqref{eq:mpr}, membrane", r"Eq.~\eqref{eq:mpr}, membrane")
s=s.replace("Second-order DC rate shift of an uncoupled MPR population ($\\Delta=1$, dimensionless membrane-time variables)",
            "Second-order DC rate shift of an uncoupled MPR population ($\\Delta=1$)")
s=s.replace(r"$F'/(2\tilde\omega^2)$", r"$F'/[2(\omega\tau_m)^2]$")
s=s.replace(r"$\tilde\omega_z$", r"$\omega_z\tau_m$")
s=s.replace(r"The horizontal coordinate is $\tilde\omega=\omega\tau_m$;",
            r"The horizontal coordinate is $\omega\tau_m$;")
s=re.sub(r"\n{3,}", "\n\n", s)
s="\n".join(line.rstrip() for line in s.splitlines())+"\n"
P.write_text(s)

cap=ROOT/"figures_src/fig_models_ti_caption.tex"
cap.write_text(r"""\begin{figure}[t!]
\centering
\includegraphics[width=\textwidth]{fig_models_ti.pdf}
\caption{\textbf{Access, detection, and amplification in the two circuits.}
\emph{(a)} JR: access $\lambda_0H(\omega)$ converts the field to polarization
$s$, and sigmoid curvature mixes the tones.
\emph{(b)} NMM2 PING: current $I_E=\lambda_I E$ enters the excitatory membrane;
$v_E^2$ mixes its voltage excursions. The inset shows the QIF neurons whose
infinite-population limit gives this exact mean field.
Low-pass symbols mark second-order synapses ($h_e,h_i$ in a; AMPA and GABA
with times $\tau_a,\tau_g$ in b). They suppress carriers more strongly than
the generated beat and transmit the steady shift.
Dashed frames enclose recurrent amplifiers, with small-signal gain
proportional to $1/\gamma$ near the relevant Hopf.
Blue: excitation; red: inhibition; green: field input.}
\label{fig:models}
\end{figure}
""")
print("Second source pass written; no PDF built.")
