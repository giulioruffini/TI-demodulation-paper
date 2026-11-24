# Theory: prose revision log

## Verification

- Word count, prose outside math (inline math counted as one token, displays, equation and table environments excluded): original 3223, revised 3219. Cross-check with texcount (text words): original 2921, revised 2911; headers 72 and captions 118 unchanged.
- Every \cite, \ref, \eqref, \label and \input key of the original appears in the revised text with the same multiplicity; none added or lost (scripted check).
- Every number in the original appears with at least the same multiplicity; all four percentages (1.59%, 4.77%, 2–5%, 2.5%) and all value-unit pairs are present (scripted check).
- All 25 displays, equation environments and both tables, including captions, are byte-identical to the original.
- No line ends with ':' before a display. Environments are balanced, and the three \ifjne...\fi blocks are intact.
- The snapshot with this section spliced in compiles under pdflatex with 0 errors and 0 undefined references, giving 39 pages, the same as the original snapshot.

## Changes by paragraph

- "A neural mass model describes...": expanded PSP at first use, then used "PSPs"; dropped "respective"; folded "Primes denote..." into the preceding sentence. Reason: define the acronym and remove the extra short sentence.
- "The JR column couples...": the LFP proxy is now its own clause ("the local field potential (LFP) proxy is v=..."), not an appositive stacked after "field input". Reason: the original sentence packed several claims.
- "We neglect propagation...": the clause about the effective polarization now opens with "After cellular access". Reason: the mechanism now comes in causal order.
- "Soma, dendrites...": "compartment k's static polarization vector" became "the static polarization vector of compartment k"; "aligned compartment phases" became "in-phase compartments"; "H's" became "of H". Reason: readability.
- "Fast axonal access motivates...": merged the two calibration sentences; "relaxation" became "membrane relaxation". Reason: name the physical agent.
- "Expanding about the field-free voltage...": "leads" became "dominates"; ⟨·⟩_c is defined in words as the carrier-cycle average; ε is defined before the display that uses it, instead of after the next display; the synaptic-filtering clause now reads "as synaptic filtering does downstream of detection". Reason: define symbols before use.
- "For a dynamic cellular response...": the coefficient is now introduced by "the complex source amplitude defines χ(2)"; two sentences joined. Reason: flow.
- "The static detector predicts...": unchanged.
- "Envelope following and quadratic detection assign...": "it is the rectified cosine" now reads "but the envelope is not: for matched tones it is...". Reason: resolve the ambiguous referent of "it".
- "Table ... separates these geometric quantities...": the gain is defined before its use ("with gain c1 outputs"); "Thus" became "therefore" placed inside the sentence. Reason: define before use.
- "The excursion maps...are related pointwise by": "ratios are 2 ... and 40" became "ratio is ..."; "Actual contrast requires..." kept. Reason: minor grammar.
- "With fixed electrode pairs...": "peak pair current" became "peak current of pair j"; "the ratio" became "the current ratio"; "target/reference" kept. Reason: say which ratio.
- "The steady source provides a way for current-ratio changes...": rewritten as "Current-ratio changes can still reshape the beat response through the steady source, which weights...". Reason: active voice, fewer words.
- "The scalar maps use a common fixed projection...": "Let ... be" became an "If ..." clause; the conjugation overbar is marked "here" to separate it from the beat-period-mean overbar; "rank-one specialization" became "rank-one case". Reason: the overbar had two meanings.
- "For a narrowband input...": θ is defined in the lead-in ("its average over carrier phase θ"); "This transduction contains only even powers" became "which contains only even powers", so the display continues the sentence. Reason: define before use, and let the display continue the sentence.
- "At matched tones, envelope following...": "second/fundamental harmonic ratio" became "second-to-fundamental harmonic ratio"; "are supplementary" now names "the inversion for mixed detectors". Reason: unpack the jargon.
- "The network modifies these ratios...": now defines H_det (the detector's harmonic ratio) and G (the network susceptibility) at first use. Reason: these symbols were undefined.
- "Detection converts nonnegative mean-square polarization...": semicolon became a conjunction; the one-carrier clause was reordered. Reason: flow.
- "The static JR source is": "common unit cell orientation" became "the cells' common unit orientation". Reason: "unit cell" reads as crystallography.
- "The Population Excitation–Inhibition Index...": the appendix pointer is now active ("Appendix ... gives"). Reason: active voice.
- "Carrier averaging retains...": semicolon became "whereas"; the final clause is joined with "and". Reason: flow.
- "In a homogeneous, isotropic...": the colon after the inequality became "so"; "regardless of montage" became "whatever the montage", moved before the claim. Reason: flow.
- "The envelope mean is also subharmonic": "envelope mean" became "envelope's beat-period mean"; "has unrestricted sign" became "can take either sign". Reason: precision, and agreement with the Introduction.
- "With isotropic orientations...": "averaged beat" became "orientation-averaged beat". Reason: say averaged over what.
- "An unmodulated carrier at the same local RMS...": the dynamic-detector condition is joined to the claim it qualifies; "carrier interval" became "across the carrier frequencies". Reason: say what the interval is.
- "We compare TI's steady and beat sources...": dropped the re-expansion of tDCS, which the Introduction already defines. Reason: words.
- "For the JR parameters...": "source-magnitude ratio" became "TI-to-direct source-magnitude ratio"; the colon before the inline values became "which is". Reason: say the ratio of what to what.
- "Matching the total TI peak...": rewritten so the RMS reason comes first ("Because TI's RMS polarization is ε, ..."). Reason: causal order.
- Heading "Amplification: the synaptic low-pass and the network resonance" became "Synaptic filtering and network resonance select the beat". Reason: declarative heading. The label is unchanged.
- "Synaptic filtering suppresses the carrier...": "while" became "but"; "Provided ... does not" became "Unless". Reason: fewer words.
- "The recurrent circuit selects the recovered beat...": the first sentence was deleted because the new heading states it; "leading pair" became "leading eigenvalue pair". Reason: define μ± as eigenvalues.
- "Write D for...": became "Let D be the detector's beat-source coefficient"; the two sweep sentences are merged with "whereas". Reason: flow.
- "Resonance requires a beat source...": "second-order difference-frequency source" became "second-order source at the difference frequency"; "therefore" became "so"; BOLD is expanded at first use. Reason: stacked nouns and an undefined acronym.
- "Carrier independence at fixed polarization...": the point-membrane sentence is merged as an apposition; "For nearby carriers ... The quadratic beat then satisfies" became one sentence ending in "so the quadratic beat satisfies". Reason: flow.
- "A sufficiently long passive cable...": "quadratic-beat factors" is now identified with the ratio in Eq. (khz) inline. Reason: name the quantity.
- "QIF computes access...": "requiring no additional filter on current input" became "so current input needs no additional filter"; "without determining" became "but determines neither ... nor". Reason: plain construction.
- "Any additional gate filter...": "have a model or measurement behind it" became "rest on a model or measurement"; the semicolon became "and". Reason: register.
- "The exact mean field of all-to-all QIF neurons...": dropped the re-expansion of QIF, which is already defined; "low frequency" became "low carrier frequency"; "unlike the JR sigmoid" moved next to "grows without bound", which is the only property it contrasts. Reason: removes a misreading, since the JR sigmoid also exists without recurrence.
- "If relaxation is faster than synaptic variation...": the colon became "; a population can therefore track ...", stating why the two conditions differ; "; such synaptic modes" merged. Reason: make the logical link explicit.
- "The field input survives this reduction...": "λI=κE/Is: κE is" became "with κE the equivalent current per unit field"; "The bare curve F takes total drive..." merged with the next sentence through "Because". Reason: show the causal link.
- "Outside the adiabatic limit...": "At slow/fast carriers" became "For slow/fast carriers"; minor articles. Reason: grammar.
- "This fast-carrier attenuation includes membrane access...": became "The attenuation at fast carriers includes membrane access:"; the carrier-attenuation clause became "but not the generated beat"; the appendix and supplement pointers are now active. Reason: stacked nouns and redundancy.
- "In this cellular realization...": the semicolon became "and". Reason: flow.
