"""Reproduce the first draft21 prose/organization pass from draft20 e20c047.

This script edits source only. It never builds or replaces a PDF.
"""
from pathlib import Path
import subprocess
import re

ROOT = Path(__file__).resolve().parents[2]
P = ROOT / "TN0484_envelope_demodulation.tex"
s = subprocess.check_output(
    ["git", "show", "e20c047:TN0484_envelope_demodulation.tex"], cwd=ROOT, text=True
)

def replace(old, new):
    global s
    assert old in s, old[:120]
    s = s.replace(old, new, 1)

def between(start, end):
    return s[s.index(start):s.index(end)]

def set_between(start, end, new):
    global s
    a, b = s.index(start), s.index(end)
    s = s[:a] + new + s[b:]

# Keep the argument in the main text; move technical formulations to their homes.
qif = between("The corresponding population nonlinearity", "The JR column couples")
qif = qif[:qif.index("The transfer curve summarizes")]
dynamic = between(r"\subsection{The exact mean field", r"\subsection{Detector laws")
projection = between("It also fixes the projection direction.", "\n\nExpanding")
projection = projection[:projection.index("The FEM\ncomparison")]
nmm1 = between("For a synapse from population", "The corresponding population")
jr_def = between("The JR column couples", "\nFigure~")
laminar_start = jr_def.index("The laminar extension")
laminar_end = jr_def.index("These models retain")
laminar_def = jr_def[laminar_start:laminar_end]
jr_def = jr_def[:laminar_start].replace(
    "(App.~\\ref{app:models}). ", ". "
)
set_between("For a synapse from population", r"\subsection{From applied", jr_def + "\n")
s = s.replace(r"\subsection{Population transfer and the slow-synapse limit}",
              r"\subsection{A population rate curve supplies the nonlinearity}", 1)

# Explain the exact mean field after the static argument and access conditions.
dynamic_summary = r"""\subsection{The exact mean field extends the static detector}\label{sec:dynamic}
The static rate curve applies when population activity follows the input fast
enough. An exact mean field of quadratic integrate-and-fire (QIF) neurons makes
this condition explicit and supplies the response outside that limit.

"""
# Use physical units in the main-text MPR equations, without decorated variables.
qif = qif.replace(
    "With normalized time $\\tilde t=t/\\tau_m$ and rate $\\tilde r=\\tau_m r$, where $\\tau_m$ is the membrane time,",
    "With membrane time $\\tau_m$, physical firing rate $r$, and dimensionless voltage $v$,")
qif = qif.replace(
    r"\frac{\mathrm d\tilde r}{\mathrm d\tilde t}=\frac{\Delta}{\pi}+2\tilde r\,v,\qquad"
    "\n" + r"\frac{\mathrm dv}{\mathrm d\tilde t}=v^2+\bar\eta-\pi^2\tilde r^2+I(\tilde t),",
    r"\tau_m\dot r=\frac{\Delta}{\pi\tau_m}+2rv,\qquad"
    "\n" + r"\tau_m\dot v=v^2+\bar\eta-(\pi\tau_m r)^2+I(t),")
qif = qif.replace(
    "normalized input, including recurrent drive when present. The reduced variables are dimensionless; $r$ without a tilde denotes physical\nfiring rate.",
    "dimensionless input, including recurrent drive when present. Dots denote physical-time derivatives.")
qif = qif.replace(r"I(\tilde t)", "I(t)").replace(
    r"v=-\Delta/(2\pi\tilde r)", r"v=-\Delta/(2\pi\tau_m r)")
qif = qif.replace(r"\tilde r=F(Q)", r"\tau_m r=F(Q)")
qif = qif.replace(
    "Its curvature combines threshold recruitment and the concave rate increase of\nactive cells (App.~\\ref{app:mpr-mixing}).",
    "Below its inflection, curvature reflects recruitment of cells across threshold;\nabove it, curvature reflects the concave square-root rate of active QIF neurons.")
qif = qif.replace(
    "Restoring the membrane time $\\tau_m$ and physical\nfiring rate, a second-order synapse",
    "A second-order synapse")
dynamic_summary += qif + r"""
Outside the adiabatic limit, the quadratic voltage term mixes the carriers
before the rate responds. For an uncoupled population under a weak current
$I_{\rm ac}\cos\omega t$, write the mean-rate shift as
$I_{\rm ac}^2\kappa_{\rm DC}/\tau_m$. At slow carriers,
$\kappa_{\rm DC}\to F''(Q)/4$; at fast carriers,
$\kappa_{\rm DC}\sim F'(Q)/[2(\omega\tau_m)^2]$.
The slow response follows curvature and can be negative above the inflection.
The fast response follows the positive slope: voltage excursions of order
$I_{\rm ac}/(\omega\tau_m)$ generate a positive input shift through $v^2$.
A shorter membrane time can therefore change both the magnitude and sign
of the mean response at a given physical carrier frequency.

The fast-carrier attenuation already includes membrane access. Dividing by
the squared voltage excursion leaves a coefficient tending to $F'/2$.
For two nearby tones, the voltage quadratic generates a beat source proportional
to $I_1I_2/(\omega_1\omega_2\tau_m^2)$, with the same product law as the static
detector. The dynamic rate equation attenuates the carriers once more, after
this mixing; it does not add that attenuation to the generated beat.
The exact coefficients and carrier exponents are derived in the supplement.

QIF thus provides a cellular realization of quadratic detection, with its
own frequency dependence. Other smooth cellular mechanisms can contribute
to the same effective second-order coefficient. Their weak-input product law
does not fix the coefficient's magnitude, phase, or carrier dependence.

"""
replace(dynamic, "")
replace(r"\section{Methods}", dynamic_summary + r"\section{Methods}")

# Detailed mean-field algebra retains its equations and table in the supplement.
dynamic = dynamic.replace(
    r"\subsection{The exact mean field connects static and dynamic mixing}\label{sec:dynamic}",
    r"\subsection{Static and dynamic MPR mixing coefficients}\label{app:mpr-coefficients}")
dynamic = dynamic.replace(
    "The adiabatic condition in \\S\\ref{sec:nmm} determines whether the static curve describes\ncarrier mixing. Consider an uncoupled MPR population (Eq.~\\eqref{eq:mpr}, membrane\ntime units), with constant drive $Q$ and a weak added current $I_{\\rm ac}\\cos(\\tilde\\omega\\tilde t)$.\nHere $\\tilde\\omega=\\omega\\tau_m$ is the normalized carrier angular frequency.",
    "In this subsection and the derivation that follows, time is measured in units\nof $\\tau_m$, rate in units of $1/\\tau_m$, and $\\omega$ denotes angular frequency\nin membrane-time units. Thus $r^*=F(Q)$ and physical angular frequency is\n$\\omega/\\tau_m$. Consider an uncoupled MPR population at drive $Q$, with a weak\ncurrent $I_{\\rm ac}\\cos\\omega t$.")
for glyph in ("r", "t", "omega"):
    dynamic = dynamic.replace("\\tilde\\" + glyph if glyph == "omega" else "\\tilde " + glyph,
                              "\\" + glyph if glyph == "omega" else glyph)
dynamic = dynamic.replace(" (Fig.~\\ref{fig:crossover}a)", "")
dynamic = dynamic.replace("the PING circuit used below", "the PING circuit studied here")
dynamic = dynamic.replace("PING) circuit used below", "PING) circuit studied here")
dynamic = dynamic.replace(
    "The expansion about the fixed point is given in\nApp.~\\ref{app:mpr-mixing}. Its limits are",
    "Expansion about this fixed point gives the limits")
replace(r"\subsection{Single-cell rate and dynamic MPR mixing}", dynamic + "\n" +
        r"\subsection{Single-cell rate and dynamic MPR mixing}")
replace("The models are written in the NMM1 transfer-function formalism",
        nmm1 + "\nThe models are written in the NMM1 transfer-function formalism")
replace("We complement the single-column analysis with simulations of the laminar neural\nmass model (LaNMM) of \\S\\ref{sec:nmm}.",
        laminar_def + "\nWe simulate this laminar neural mass model (LaNMM).")

# Envelope geometry precedes harmonic signatures, so A is explained before use.
harmonics = between(r"\subsection{Detector laws", r"\subsection{Envelope oscillations")
replace(harmonics, "")
replace(r"\subsection{The steady source", harmonics + r"\subsection{The steady source")
replace("The coefficient depends on the detector regime. For an uncoupled QIF population\n"
        "at fast carriers, $v^2$ generates a positive effective input shift, and the\n"
        "readout through $F'>0$ gives a positive rate shift. In the slow-carrier\n"
        "(adiabatic) limit, $\\kappa_{\\rm DC}\\to F''/4$, so the rate shift is negative\n"
        "above the inflection of $F$ (Eq.~\\eqref{eq:crossover_limits}). The positive\n"
        "E-drive shift in \\S\\ref{sec:qif} is therefore a fast-carrier result for that\n"
        "model; the mean-rate response after recurrent feedback need not retain its sign.\n\n", "")

# Introduction: preview the physical argument without sending the reader ahead.
replace(r"in mV (related to the applied field in \S\ref{sec:coupling}),",
        "in mV, produced by coupling of the applied field to the membrane;")
replace("The spectrum contains only the two applied\nlines (Fig.~\\ref{fig:demod}).", "The spectrum contains only the two applied lines.")
replace("The mechanism therefore has distinct physical requirements (Fig.~\\ref{fig:concept}).",
        "The mechanism has three physical requirements.")
replace("Table~\\ref{tab:doors} distinguishes measured and assumed time scales.", "")
replace(r"The laminar extension also has a carrier-selective" + "\n" +
        r"stage (\S\ref{sec:lanmm-results}).", "")
replace("We build a mesoscale model separating access, detection, and amplification in\nseries. A Jansen--Rit column, an exact quadratic integrate-and-fire (QIF) mean\nfield, and its spiking network connect the weak-input product law to resonant\ngain, timing modulation, and the equal-power carrier control; a laminar extension\nadds two resonant bands at low carriers. Fast relaxation recovers a static\npopulation transfer with dynamic synapses, while slower membranes require a\nfrequency-dependent mixing coefficient.",
        "Our mesoscale model separates the cellular beat source from recurrent gain.\n"
        "A Jansen--Rit column establishes the weak-input product law; an exact QIF\n"
        "mean field and its spiking network test how membrane dynamics and recurrent\n"
        "activity modify the response. A laminar extension adds two resonant bands\n"
        "at low carriers. Fast population relaxation gives a static transfer curve\n"
        "with dynamic synapses; slower relaxation requires a dynamic detector.")

# Access and mixing: remove bookkeeping sentences and supply the missing explanation.
replace("We use the quasistatic electromagnetic approximation for the applied field $E(t)$\n"
        "(V/m), neglecting propagation and induction. This does not make membrane charging\n"
        "instantaneous.",
        "We neglect electromagnetic propagation and induction in the applied field\n"
        "$E(t)$ (V/m), while retaining the membrane's finite charging response.")
replace("The static gain and its frequency dependence belong to this\none response. A model driven by post-coupling polarization and a model driven by\ncurrent through its own membrane equation must therefore count that filtering once.",
        "The access filter is included in the supplied polarization or computed by\n"
        "the membrane equation when its input is current; applying both would count\n"
        "the same attenuation twice.")
replace("The direct-coupling calculation takes\n$\\lambda_f\\approx\\lambda_0$ to isolate mixing and recurrent amplification;\n"
        "\\S\\ref{sec:khz} restores frequency-dependent access.",
        "We first hold this local polarization fixed to isolate mixing and recurrent\n"
        "amplification. At fixed applied field, its frequency dependence follows $H$.")
replace(projection, "")
replace("The FEM\ncomparison in \\S\\ref{sec:fem-methods} therefore holds its chosen direction fixed\nwhen changing the current ratio.\n", "")
replace("The projection direction $\\mathbf n(\\mathbf x)",
        projection.replace("It also fixes the projection direction.", "The detector compartment fixes the projection direction.") +
        "\n\nThe projection direction $\\mathbf n(\\mathbf x)")
replace("network gain (\\S\\ref{sec:carrier}).", "network gain.")
replace(r"\[" + "\n" + r"Y_\Omega\simeq\chi^{(2)}",
        r"\begin{equation}" + "\n" + r"Y_\Omega\simeq\chi^{(2)}")
replace(r"r_\Omega(t)=\operatorname{Re}\!\left[Y_\Omega e^{i\Omega t}\right]." + "\n" + r"\]",
        r"r_\Omega(t)=\operatorname{Re}\!\left[Y_\Omega e^{i\Omega t}\right]." + "\n" +
        r"\label{eq:chi2}" + "\n" + r"\end{equation}")
replace("Here $i^2=-1$, and $r_\\Omega(t)$", "Here $r_\\Omega(t)$")
set_between("Cellular processes can contribute", "Equation~\\eqref{eq:demod} carries",
    "Cellular processes contribute to this coefficient according to their state and\n"
    "response times. Weak input permits a second-order expansion, but a response\n"
    "that depends on input history retains frequency-dependent amplitude and phase.\n"
    "If symmetry or cancellation makes this coefficient zero, higher orders determine\n"
    "the leading beat.\n\nEquation~\\eqref{eq:demod} carries")
# set_between retains its endpoint; avoid duplicating its opening.
replace("Equation~\\eqref{eq:demod} carriesEquation~\\eqref{eq:demod} carries", "Equation~\\eqref{eq:demod} carries")
replace("three predictions, all verified below:", "the static detector's predictions:")
replace("so the field required for a given effect rises with $f_c$ (\\S\\ref{sec:khz}),",
        "so attenuating access raises the field required for a given effect,")
replace("Write $\\mathbf x$ for position", "Write $\\mathbf x$ for position")
replace("The finite-element comparison in \\S\\ref{sec:fem-results}\nquantifies this reweighting on one realistic TI montage: at balanced currents,\n"
        "the target-to-reference contrast is 1.22 for the envelope and 1.08 for the\n"
        "square root of the quadratic map. This is a milder change than the illustrative\n"
        "two-site contrast above; the line profile is not a head-model calculation.",
        "The line profile and two-site example illustrate the algebra; a realistic\n"
        "contrast requires fields computed on a head model.")
replace("The derivations below take the collinear,\nscalar case.", "The scalar formulas use these fixed projections.")
replace("response, together with", "response, together with") if False else None
replace("obeys the same restriction, as shown below.", "obeys the same restriction.")
replace("source and on recurrent feedback; the JR examples in \\S\\ref{sec:timing} have\n"
        "a negative mean-rate shift.", "source and on recurrent feedback.")
replace("entrainment above the Hopf instead requires a phase-capture test\n"
        "(\\S\\ref{sec:vocab-methods}).",
        "above the Hopf, entrainment means capture of an autonomous rhythm and\n"
        "requires tracking its phase relative to the drive.")
qif_receiver = between("For fast-carrier QIF", "In these limits")
replace(qif_receiver, "")
replace("In these limits $D$ is\nindependent of carrier frequency at fixed polarization; across the dynamic\ncrossover it acquires frequency dependence.",
        "A static detector has carrier-independent $D$ at fixed polarization;\n"
        "a dynamic detector can retain frequency dependence.")
replace("The resonance does not supply the quadratic mixer.", "Resonance requires a beat source.")
replace(" (App.~\\ref{app:sl})", "") if " (App.~\\ref{app:sl})" in s else None
# Preserve the exact QIF source/readout convention in its own section.
replace("QIF thus provides a cellular realization", qif_receiver +
        "\nQIF thus provides a cellular realization")
replace("This relation is specific to the memoryless logistic detector. In the exact mean field at a fast carrier the rectified DC term\n"
        "follows the slope $F'$ and is largest at the inflection (\\S\\ref{sec:dynamic}), so the\n"
        "relation between PEIX and TI efficacy is model-dependent; PEIX remains a measurable\n"
        "read-out of the operating point.",
        "PEIX is a measurable operating-point index; its relation to mixing is specific\n"
        "to the memoryless logistic detector.")
replace("in\nthe dynamic detector the same shifts act through $F'$ and the susceptibility, without a\nsign rule.",
        "a dynamic detector responds through its own state-dependent coefficient and\n"
        "susceptibility, without a universal sign rule.")
replace("The state dependence is the falsifiable handle; the sign reversal is specific\n"
        "to the memoryless model.",
        "State changes therefore test detection only when changes in recurrent gain\n"
        "are measured as well.")
replace("The slow response follows curvature and can be negative above the inflection.",
        "The slow response follows curvature and can be negative above the inflection.\n"
        "The fast DC coefficient instead follows $F'$, which is largest at the inflection;\n"
        "it has no PEIX-based sign reversal.")

# Results should state findings rather than preview their section labels.
set_between("\\section{Results}\n", "\\subsection{The Jansen--Rit sigmoid",
    "\\section{Results}\n"
    "Both the JR column and the exact QIF mean field generate a beat and amplify\n"
    "it near a Hopf bifurcation. The detector law fixes the local source and its\n"
    "spatial weighting; recurrent coupling sets the gain. The spiking network\n"
    "then distinguishes modulation of ongoing firing from field-induced gamma.\n\n")
replace("All symbols and units are collected in Table~\\ref{tab:notation}\n"
        "(App.~\\ref{app:notation}). We integrate the single-column JR model of \\S\\ref{sec:nmm}\n"
        "(App.~\\ref{app:models}, Eqs.~\\eqref{eq:jr0} and Table~\\ref{tab:params}) as six first-order\nODEs.",
        "We integrate the JR column as six first-order ordinary differential equations.")
replace("as $s(t)$; the read-out $v=y_1-y_2$ is \\emph{not} fed the field directly, so any\n"
        "power at $\\Omega$ in $v$ is produced by the nonlinearity and the recurrent loop,\n"
        "not by trivial pass-through.",
        "as $s(t)$, while the readout $v=y_1-y_2$ contains only synaptic potentials.\n"
        "A beat in this readout must therefore have passed through the nonlinearity\n"
        "and the recurrent loop.")
replace("The realistic-head comparison of \\S\\ref{sec:fem-results} uses one open-access subject,",
        "To compare the spatial predictions on the same anatomy, we compute all maps\n"
        "in one open-access subject,")
replace("The script\n\\texttt{code/fem\\_quadmaps.py} computes every map and number in\n"
        "\\S\\ref{sec:fem-results} from the stored fields, and \\texttt{code/make\\_fem\\_fig.py}\n"
        "draws Fig.~\\ref{fig:fem}; \\texttt{docs/fem\\_ixi002\\_violante.md} lists every setting.",
        "")
replace("The FEM summary arrays and plotting\nscript reproduce Fig.~\\ref{fig:fem} without the head model.",
        "The FEM producer \\texttt{code/fem\\_quadmaps.py} computes the reported maps\n"
        "and statistics from the stored fields; the summary arrays and\n"
        "\\texttt{code/make\\_fem\\_fig.py} reproduce Fig.~\\ref{fig:fem} without the head model.")
replace("Parameter\nsweeps are vectorized: the state is an\n"
        "$(N_{\\rm grid},6)$ array, where $N_{\\rm grid}$ counts the parameter combinations\n"
        "advanced simultaneously, so a full\nresonance map runs in seconds.",
        "Parameter sweeps advance all $N_{\\rm grid}$ combinations simultaneously\n"
        "in a vectorized $(N_{\\rm grid},6)$ state array.")
replace("These measurements test the smooth-transfer assumption", "These measurements test the smooth-transfer assumption") if False else None
replace("Together these\nmeasurements test the smooth-transfer assumption of \\S\\ref{sec:coupling}\n"
        "using the signatures derived in \\S\\ref{sec:transduction}.",
        "The amplitude law and harmonic ratio jointly identify the detector class.")
replace("analysis (\\S\\ref{sec:khz}).", "analysis.")
replace("The log--log slope of the envelope-locked response\nagainst field amplitude separates the linear and quadratic laws of\n"
        "\\S\\ref{sec:transduction} without requiring absolute\n"
        "calibration; the $\\varepsilon^2$ control of \\S\\ref{sec:results-curvature} is that\n"
        "measurement, performed in the model.",
        "The log--log amplitude slope distinguishes linear from quadratic scaling\n"
        "without absolute calibration.")
replace("to compare beat-locked and ongoing activity at the spike level (\\S\\ref{sec:qif}):",
        "to compare beat-locked and ongoing activity at the spike level:")
replace("The spectra and rate folds do not by themselves\nestablish phase capture (\\S\\ref{sec:vocab}).",
        "Spectra and rate folds resolve frequency components but do not establish\nphase capture.")

# Consolidate repeated narrative without changing the evidence.
replace("The resonance sweeps above drove the column toward the Hopf with the external input\n"
        "$p$, but $p$ also shifts the operating point, entangling detection ($\\Sig''$) with\n"
        "amplification. To isolate amplification, we vary the JR global connectivity $C$ and solve analytically for the drive $p(C)$ that\n"
        "\\emph{pins} the field-free operating point $v^*$, so the detection gain $\\Sig''(v^*)$ and the\n"
        "open-loop detector amplitude $A_{\\rm open}\\simeq\\half|\\Sig''(v^*)|\\varepsilon^2 m$ are held\nconstant.",
        "Changing connectivity at a fixed field-free operating point isolates recurrent\n"
        "gain from detection. We vary $C$ and adjust the external drive $p(C)$ to hold\n"
        "$v^*$, its curvature $\\Sig''(v^*)$, and the open-loop beat amplitude\n"
        "$A_{\\rm open}\\simeq\\half|\\Sig''(v^*)|\\varepsilon^2m$ constant.")
replace("The normalization and endpoint-stability checks are given in\n\\S\\ref{sec:nmm2-methods};\n",
        "As in the stability controls, ")
replace("source and on recurrent feedback.", "source and on recurrent feedback.")
replace("The spectrum has sidebands near $95$ and $11$~Hz",
        "Mixing of slow and fast inputs can generate endogenous amplitude modulation\n"
        "\\cite{ruffini2025ham}; here the recovered beat mixes with the ongoing gamma.\n"
        "The spectrum has sidebands near $95$ and $11$~Hz")
replace("The alpha JR and gamma NMM2 circuits\nshare", "The alpha JR and gamma NMM2 circuits share")

# Supplement derivation uses plain variables with an explicit local unit convention.
app_start = s.index(r"\subsection{Single-cell rate and dynamic MPR mixing}")
app_end = s.index(r"\section{The cubic Hopf")
app = s[app_start:app_end]
for old, new in [(r"\tilde r", "r"), (r"\tilde f", "f"),
                 (r"\tilde t", "t"), (r"\tilde\omega", r"\omega")]:
    app = app.replace(old, new)
s = s[:app_start]+app+s[app_end:]
replace(",\nwhere $i^2=-1$. In SI units", ". In SI units")
replace("The two-band laminar column (LaNMM, \\S\\ref{sec:nmm})", "The two-band laminar column (LaNMM)")
replace("These distinct modes motivate the compartment-specific access hypothesis; their\n"
        "implications for TI are considered in \\S\\ref{sec:discussion}.",
        "Thus cable geometry can improve carrier access without changing the somatic\n"
        "membrane time.")

# Version marker only; title and authors unchanged.
s = s.replace("v0.15.0-draft20", "v0.15.0-draft21").replace("0.15.0-draft20", "0.15.0-draft21")
P.write_text(s)
print("Source written; no PDF built.")
