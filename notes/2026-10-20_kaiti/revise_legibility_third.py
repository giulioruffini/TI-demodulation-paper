"""Apply the later-section reader review without changing numerical evidence."""
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
p=ROOT/"TN0484_envelope_demodulation.tex";s=p.read_text()
def rep(a,b):
    global s
    assert a in s,a[:100]
    s=s.replace(a,b,1)
def move(a,b,destination,summary):
    global s
    i,j=s.index(a),s.index(b)
    text=s[i:j];s=s[:i]+summary+s[j:]
    s=s.replace(destination,text+"\n"+destination,1)
def caption(label,text):
    global s
    e=s.index(r"\label{"+label+"}");a=s.rfind(r"\caption{",0,e)
    s=s[:a]+r"\caption{"+text+"}\n"+s[e:]

# Run-specific settings belong in a compact supplementary record; the main
# method states what the comparison holds fixed and what is measured.
a=s.index("The coupling sweeps of Figs.")
b=s.index(r"\subsection{Vocabulary:",a)
settings=s[a:b]
summary=r"""The JR sweeps vary coupling while keeping detection fixed. For each
connectivity $C$, we solve for the external drive $p(C)$ that holds the
field-free voltage at $v^*=8.30$~mV, then obtain damping and modal frequency
from the Jacobian. This fixes the background curvature without canceling
stimulation-induced mean shifts.

The gain sweep uses the AM surrogate; the timing comparison uses genuine
two tones and measures modulation and mean of the same pyramidal rate
$r_P=\Sig(v+s)$. The tACS control uses a direct sinusoid at the same beat
frequency and reads the same voltage lock-in as TI. Further controls match
tACS to TI's generated beat source and repeat the comparison with longer
settling and measurement windows. Waveforms, amplitudes, and run windows
are recorded together in the supplement.

"""
s=s[:a]+summary+s[b:]
anchor=r"\section{The cubic Hopf"
s=s.replace(anchor,r"\subsection{JR coupling-sweep settings}\label{app:jr-sweep-settings}"+"\n"+settings+"\n"+anchor,1)
move("Although a DC-only averaged calculation predicts an unstable endpoint,",
     r"\subsection{QIF spiking network",r"\subsection{Finite-network numerical checks}",
     "")
# The moved paragraph is a stability result: give it its own home and keep
# interpretation explicit in Results.
rep("Although a DC-only averaged calculation predicts an unstable endpoint,",
    r"\subsection{Stability of the driven PING endpoint}\label{app:ping-stability}"+"\n"
    "Although a DC-only averaged calculation predicts an unstable endpoint,")
rep("As in the stability controls, $\\gamma$ always describes the field-free critical mode, not the driven state.",
    "The fully forced endpoint remains attracting under both waveforms, even\n"
    "where a DC-only approximation predicts instability; $\\gamma$ describes the\n"
    "field-free mode. The gain reference includes the state-dependent detector.")

# Experimental-design material joins the predictions rather than sitting among
# simulation protocols.
a=s.index("At resonance ($\\Omega=\\omega_0$) with")
b=s.index(r"\subsection{Head model",a)
design=s[a:b]
s=s[:a]+s[b:]
pos=s.index(r"\begingroup\small",s.index(r"\subsection{Falsifiable"))
s=s[:pos]+design+"\n"+s[pos:]
# Clarify the antecedent and the comparison.
rep("The test therefore requires an \\emph{off-resonance} drive:",
    "A harmonic test therefore requires either an \\emph{off-resonance} drive,")
rep("measured independently by a weak sweep", "measured independently by a weak sweep")

# Merge the demonstration stub with its resonance result; preserve both figures.
rep(r"\subsection{The Jansen--Rit sigmoid demodulates: an alpha line from a carrier-only input}",
    r"\subsection{The JR column generates and resonantly amplifies the beat}")
rep(r"\subsection{Near the Hopf, the demodulated beat drives a sharp resonance}"+"\n", "")

# Caption-only bifurcation detail moves beside the equations that define it.
detail=r"""The alpha limit cycle lies between Hopf points near $p=90$ and
$316$~s$^{-1}$. It coexists with a lower stable fixed point up to the
saddle-node on an invariant circle (SNIC, $p\approx114$), then with a
large-amplitude cycle up to its saddle-node near $p=137$. The SNIC
terminates the large-amplitude branch, not the alpha cycle.

"""
rep(r"\subsection{Compartment access",detail+r"\subsection{Compartment access")
caption("fig:bif",r"""\textbf{JR operating states and sigmoid curvature.}
\emph{(a)} Numerical continuation of fixed points (blue) and cycle extrema
(red) against external drive $p$; solid branches are stable, faded branches
unstable. The alpha cycle lies between Hopf points near $90$ and
$316$~s$^{-1}$. Beyond the upper Hopf the fixed point is a stable focus,
with $f_0\approx11.16$~Hz. Markers identify saddle-nodes (SN), Hopf points
(HB$^\pm$), the saddle-node on an invariant circle (SNIC), and the
saddle-node of limit cycles (SNLC).
\emph{(b)} Sigmoid and curvature; dots mark the modeled operating points.""")

# Keep the detailed experimental comparison as a footnote to the interpretive
# point rather than another narrative detour.
a=s.index("Primate measurements illustrate")
b=s.index("For an illustrative fast-access budget,",a)
vieira=s[a:b]
intro="Vieira et al.\\ \\cite{vieira2024}"
foot=vieira[vieira.index("Their\n"):vieira.index("These weaker\n")]
foot=foot.replace("Their\n","The ",1).replace("reported two distinct experiments. ", "")
short=r"""The weaker TI effects reported by Vieira et al.\ are compatible with
a smaller generated beat drive, but their experiments did not match local
polarization at the mixer.\footnote{"""+foot.strip()+r"""}
Phase-locking value (PLV) also depends on baseline and state. These comparisons
therefore do not calibrate the detector coefficient; that requires the same
readout across a local-polarization amplitude sweep.

"""
# Preserve attribution lost when the original opening moves.
short=short.replace("Vieira et al.\\ are",r"Vieira et al.\ \cite{vieira2024} are")
s=s[:a]+short+s[b:]
# Cifra's scope detail stays in a footnote, tied to the access claim.
rep("At extracellular fields of order $1$~V/m, voltage-gated channels respond through\n"
    "membrane polarization: the direct protein effects reviewed by Cifra et al.\\\n"
    "\\cite{cifra2026} occur at $10$~kV/m to GV/m, with protocol- and molecule-dependent\n"
    "thresholds; that review excludes fields below $0.1$~kV/m, where it expects direct\n"
    "effects to be negligible against thermal noise.",
    "At fields of order $1$~V/m, channels respond through membrane polarization,\n"
    "well below the fields associated with direct protein effects\n"
    "\\cite{cifra2026}.\\footnote{The review describes direct effects at $10$~kV/m\n"
    "to GV/m, depending on molecule and protocol. It excludes fields below\n"
    "$0.1$~kV/m, where it expects direct effects to be negligible against thermal noise.}")
# The comparisons belong under a shared amplifier lead.
rep("Increasing that direct input by a factor of $6.99$ increases its response\n"
    "by $6.97$, $3.95$, and $1.96$, respectively. The larger response saturates earlier, with stimulation-induced mean shifts\n"
    "that field-free pinning does not cancel; this accounts for the finite-amplitude\n"
    "departure from the linear ratio near criticality.",
    "The stronger direct response saturates earlier near the Hopf: multiplying\n"
    "its input by $6.99$ increases the output by only $6.97$, $3.95$, and $1.96$\n"
    "at these three couplings. Stimulation-induced mean shifts, which field-free\n"
    "pinning does not cancel, account for this departure from the linear ratio.")

# The Conclusion carries results; supporting caveats remain with those results
# and in Discussion, rather than being repeated as a closing defense.
a=s.index(r"\section{Conclusion}");b=s.index(r"\section*{Code and data availability}")
s=s[:a]+r"""\section{Conclusion}
TI requires access, detection, and amplification. For weak inputs with a
nonzero second-order coefficient, detection generates a beat proportional
to the product of the local carrier polarizations and a steady source
proportional to their summed squares. Fast axonal access can be represented
by a short effective membrane time, with its transfer still requiring calibration.

The detector law changes the spatial prediction. In the realistic-head
model, changing the current ratio moves the envelope and mean-square
foci in opposite directions but only rescales the quadratic beat at fixed
neural state. Under uniform conductivity, access, and detection, the
steady-source magnitude has no strict interior maximum.

Near a Hopf bifurcation, the circuit amplifies the beat in inverse proportion
to modal damping. TI shares this linear amplifier with matched direct
low-frequency stimulation. In the pinned JR sweep, the response is expressed
mainly as beat-locked timing; its ratio to the mean shift eventually falls
as the oscillation rectifies. At larger fields, the steady shift alone can
induce gamma, as can an equal-power unmodulated carrier.

Local-polarization measurements, independent-amplitude tests, beat sweeps
across states, and equal-power controls separate these mechanisms.
Together they test whether a measured TI response reflects access,
nonlinear detection, recurrent gain, or a field-induced change of state.

"""+s[b:]
# Data access statements retain reproducibility limits, not the audit history.
rep("A reconstructed producer with explicit\n"
    "run settings reproduces every archived spectral bin of the two-tone kHz\n"
    "illustration (Fig.~\\ref{fig:khz_twotone}) exactly. The LaNMM setup\n"
    "is a drawn schematic. The LaNMM carrier comparison has both measurement-window\n"
    "caches and a reproducible summary script.",
    "The two-tone kHz example and both LaNMM carrier-measurement windows have\n"
    "cached outputs and reproduction scripts.")
# Front matter reflects the actual revision date; historical comments are intact.
s=s.replace("version \\paperver, October 19, 2026","version \\paperver, October 20, 2026")
s=s.replace(r"Working draft v\paperver\quad 2026-10-19",r"Working draft v\paperver\quad 2026-10-20")
s=s.replace(r"\textbf{Date:} & 2026-10-19",r"\textbf{Date:} & 2026-10-20")
p.write_text(s)
print("Later-section pass applied; no PDF built.")
