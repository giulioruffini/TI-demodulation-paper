# Methods revision: changes

## Verification

- Prose words outside math (own counter, comments, math, displays and citation/ref commands stripped; captions included in both): original 1601, revised 1597. Cross-check with texcount (text words): original 1496, revised 1491; inline math 127 in both.
- Every `\cite`, `\ref`, `\eqref`, `\label`, `\input`, every inline math span, every number (including those with units and every percentage) in the original occurs at least as often in the revised file. One `\eqref{eq:lockin}` was added (Response terminology) so that "lock-in" points to its definition.
- All three equation environments and the figure environment, caption included, are byte-identical to the original.
- No line ends with ':' before a display. No em-dashes. None of the banned words occur.
- `\ifjne`/`\else`/`\fi` counts unchanged (6/6/6). The snapshot compiled with the revised span (pdflatex, one pass) gives 0 errors, the same as the original span; the warning lists differ only in line numbers.

## Changes by paragraph

- "A forced response is..." : linked "lock-in" to Eq. (lockin), its definition; merged the entrainment and gating sentences with their caveats into single sentences ("..., which our screen does not establish"); "a purely forced regime also requires" kept as a condition. Why: no term before its definition; fewer clipped sentences.
- "Dense perturbative sweeps use..." : "parameterizes dense resonance and coupling sweeps" became "the resonance and coupling sweeps" (dense already stated); colon before inline $Y_\Omega$ replaced by comma; the two LPF formulas joined by "whereas" and the conclusion attached with "so", replacing the semicolon chain and "Thus". Why: remove semicolon packing, connect comparison to conclusion.
- "We use genuine tones..." : two sentences merged into one list ("and wherever mean shifts or harmonics enter a comparison"); semicolon replaced by "and does not imply". Why: one statement of where genuine tones are used.
- "A software lock-in projects..." : named $v$ as the readout; joined the window caveat to the definition; moved "over long windows" to the head of the test-tone sentence and attached the conclusion with "so" instead of "Thus". Why: undefined symbol at first use; continuous reasoning.
- "A detector comparison requires..." : recast as "Comparing detectors requires". Why: less nominal phrasing.
- "We compute maps in IXI002..." : passive "Maps are computed"; "with no kHz dispersion correction" made "without"; current-scaling sentence with colon recast as one sentence ending with the posterior-share sweep. Why: colon list removed; settings grouped.
- "Local polarization is..." : the two sentences on the coupling merged ("This assumed conversion, not a measured AIS transfer, sets absolute amplitudes but cancels..."). Why: one claim about $\lambda_0$, not two.
- "At each node, n maximizes..." : named $\mathbf n$ as a unit vector; "the latter" replaced by "the isotropic average". Why: avoid backward reference across a parenthesis.
- "The target is the left hippocampus..." : defined ROI at first use; "Nodes receive equal weight" moved into the contrast definition ("With equal node weights, the contrast divides the ROI 95th percentile by the reference 95th percentile"). Why: ROI was used undefined; the weighting belongs to the definition it qualifies.
- "The focus is the centroid..." : focus and displacement in one sentence; colon before $Y_{\rm DC}$ replaced by "so"; "anterior positive" kept. Why: connect geometric maps to the curvature caveat.
- "We integrate the JR column..." : named $s$ as the TI polarization entering the sigmoid; "therefore" sentence joined with "so". Why: name the agent; continuous argument.
- "Integration uses fixed-step..." : step convergence joined to the step choice; run-specific settings pointer joined to the resonance-sweep windows. Why: group integration settings.
- "Numerical continuation gives..." : "leading pair" made "leading eigenvalue pair"; final semicolon replaced by "and". Why: name the quantity.
- "The open-loop sigmoid..." : unchanged except a semicolon replaced by ", and". Why: rhythm.
- "The coupling sweep holds..." : colon split into two sentences; named $C$ as the connectivity scale (Theory's term). Why: unnamed quantity; colon packing.
- "We use the AM surrogate..." : split the double use of "We use"; "TI's generated beat source" made "the beat source TI generates"; supplement sentence made active. Why: stacked possessive; clarity.
- "The pyramidal--interneuron network gamma..." : text after the display now continues the sentence with "where", since the display ends in a comma; "Here J is dimensionless global gain; weights ... use target/source indices" recast as "The global gain J is dimensionless, and the weights ..., indexed target then source, make doubled inhibitory self-coupling the only asymmetry". Why: the display ended mid-sentence; semicolon packing.
- "The background eta controls..." : "opening" made "that opens"; "E-voltage" made "excitatory voltage"; the instantaneous-coupling sentence joined to $I_E=\lambda_I E$; "We set $f_c$..." folded into the tone sentence; colon before "access uses" replaced by "so". Why: name the agent; remove colon and semicolon chains.
- "We integrate with fixed-step RK4..." : parameters stated as a sentence ("Parameters (...) are ...") rather than with a colon; Hopf sweep made its own clause; semicolon before the fast-membrane limit made "whereas". Why: colon list removed; contrast made explicit.
- "The resonance map varies..." : split at the semicolon; the $J^*$ bisection sentence folded into the coupling-sweep sentence; "Unlike JR, the PING coupling sweep" made "Unlike in JR, this sweep". Why: group the sweep definition; remove repetition.
- "Stability of the driven endpoint..." : "using" made "by"; semicolon replaced by "with". Why: rhythm.
- "To compare beat-locked..." : "Single-neuron voltages $V_j$" made "Each voltage $V_j$"; "follow deterministic quantiles" made "are deterministic quantiles", joined to the synapse clause; "surrogate equivalence" made "the surrogate's equivalence". Why: stacked noun modifiers.
- "At fc=300 Hz and amplitude..." : beats attached to their $\bar\eta$ values in parentheses; the below/above clause joined to that sentence. Why: pair each setting with its value.
- "We repeat both conditions..." : passive "Both conditions are repeated", sensitivity tests as a participle; "both inputs have" attached with "so". Why: connect cause and consequence.
- "The carrier-averaged stability..." : two sentences joined by a semicolon; "separately check" moved to the end. Why: one claim about calculation and its check.
- "Euler integration uses..." : settings pointer joined to the step; "an off/on ratio would divide by the field-free floor" made "not as an off/on ratio, which would ..."; PPC sentence reordered so the frequency follows "locking". Why: state the rationale as a contrast; less telegraphic.
- "A cutoff-free check..." : final semicolon made "so". Why: state the consequence.
