# Readability review of draft14 (a2aacd6), section by section and paragraph by paragraph

Klaus, October 6, 2026, at Giulio's request: does each section and paragraph state what it needs,
clearly and briefly, without burying the reader? Line numbers refer to
TN0484_envelope_demodulation.tex at a2aacd6. Verdicts: OK (keep), TRIM (shorten, same content),
MOVE (relocate), MERGE, RECAST (lead with the claim), CUT? (removal needs Giulio's approval).

## Global findings

1. Theory carries Methods and Results material: the AM-surrogate protocol and its two-tone
   reruns (523-546), the 8-state PING agreement numbers (630-638), the full QIF Jacobian
   derivation (584-599), the compartment matrix equation in SI units (446-452), the cable
   end-polarization estimate (971-988). Theory reads as a derivation log rather than an argument.
2. Several facts appear three times: Cohen/AIS/Kole (Introduction 227-232, Theory 908-915,
   Discussion 1876-1877), Esmaeilpour's 1 and 0.4 ms (Introduction 222-225, Table 2, Discussion
   1893-1894), Semenov and Luff time scales (Table 2 and Discussion 1895-1899), the
   slow-synapse limit (Theory 378-394, Discussion 1915-1920, Conclusion 2046-2050),
   timing versus rate (sec timing, QIF 1763-1774, predictions table, Discussion).
3. Many paragraphs end on a caveat rather than a conclusion ("The product law is not an account
   of TI focality"; "The linear cancellation therefore does not extend..."; "These normalizations
   compare gain variation, rather than establishing..."; "it does not establish..."). The
   caveats are correct; their position makes the paper read as defensive. Put the claim first,
   the scope in one clause.
4. Results 4.6 holds four results (JR coupling gain, TI/tACS shared amplifier, Arnold-tongue
   aside, NMM2 two-mode J-curve with endpoint stability). The TI/tACS result is one of the
   paper's three headline claims and is buried mid-section.
5. The QIF section opens with convergence numbers before saying what the reader should learn.

## Introduction

| Lines | Verdict | Note |
|---|---|---|
| 190-196 | OK | Clear problem statement. |
| 198-210 | OK | The no-new-line argument; good. |
| 212-218 | OK | Defines the three stages. |
| 220-236 Access | TRIM | Literature list (somatic times, Esmaeilpour, Cohen, Kole); message is one claim: somatic access attenuates kHz, fast axonal compartments are candidate sites, modeled by a short effective time to be calibrated. Half the length. "Axonal geometry and myelination support voltage responses distinct from those at the soma" says nothing the next sentence does not. |
| 238-249 Detection | OK | Ends well (cellular detector exists, population coefficient). |
| 251-266 Amplification | TRIM | Citation run; last sentence "Cellular mixing and circuit amplification can therefore contribute to the same response" is weak. Keep Caldas and Vieira, which carry the argument. |
| 268-275 Scope | TRIM | "linear amplification further requires stability under the rectified mean shift" is too technical for an Introduction. Two sentences. |
| 277-297 Contribution | MERGE, RECAST | The contribution sentence is buried mid-paragraph; the last paragraph repeats the three-stage framing of 212-218. One paragraph: what we build (three-stage mesoscale model, two population models plus spiking network), what it yields (product law, shared amplifier, timing over rate, carrier control), how each stage is tested. |

## Theory

| Lines | Verdict | Note |
|---|---|---|
| 318-334 NMM basics | OK | |
| 336-350 NMM1 | OK | |
| 352-376 MPR | TRIM | Three sentences restate that variables are dimensionless; the single-neuron f(q) remark can go to the appendix. |
| 378-394 slow-synapse limit | OK | Central idea (quasistatic for synapses, dynamic for kHz). |
| 396-404 | MERGE/CUT? | Restates the curvature/slope roles already given at 333 and in the Introduction. |
| 406-409 | MERGE | One-sentence point on network resonance; fold into 411-420. |
| 411-420 JR/LaNMM | OK | Place the new model figure here. |
| 423-455 Access | TRIM, MOVE | Keep the claim (access filtering is one response, counted once). Move the compartment matrix equation and SI units to the models appendix. |
| 457-463 | OK | |
| 465-490 Taylor | OK, ADD | Core. Add Giulio's point: the carrier average is what the synaptic and membrane low-pass implement (link to sec carrier). |
| 492-507 chi(2) | TRIM | Define once, units once; three caveat sentences at the end can be one. |
| 509-521 squared envelope | OK | Becomes the opening of the requested envelope subsection. |
| 523-546 AM surrogate | MOVE | Methods. Theory needs one sentence: "Dense sweeps use an AM surrogate equivalent at Omega to leading order (Methods)." |
| 548-567 | SPLIT | The HAM sideband remark (548-556) is a digression: one sentence or cut. The three predictions and the carrier-independence caveat (557-567) are good. |
| 569-613 exact mean field | TRIM, MOVE | Keep the result (static curvature at slow carriers, slope at fast carriers, crossover) and Eq. crossover_limits; move the Jacobian, phasor, and b_2 derivation (584-599) to an appendix. |
| 615-628 fixed-excursion coefficient | OK | The "membrane counted once" point; keep. |
| 630-638 8-state PING check | MOVE | Results (it is a numerical agreement). |
| 640-682 exponents table | TRIM | Table plus two explanatory paragraphs is right per Giulio's earlier request, but the paragraphs can lose a third. |
| 685-711 transduction class | OK | Clear. "Asymmetric channel rectification, threshold crossing and release events are candidate biological realizations of rectifiers of one kind or another" is vague: cut or cite. |
| 713-737 harmonic ladder | TRIM | The two-branch inverse sentence (727-728) is a footnote. |
| 739-745 amplitude sweep | OK | The primary test; state it first in Methods 3.1 too. |
| 747-766 spatial map | RECAST | Ends "The product law is not an account of TI focality". Say instead what follows: focality must be computed from the product map, which can reverse the envelope map's ranking; magnitude needs FEM (Ricardo). |
| 768-796 DC map | SPLIT, RECAST | Requested DC subsection. Lead with the claim in plain words (the steady shift adds the two carrier intensities, no interference, so no montage can focus it inside a uniform compartment), then ratio, example, proof, orientation. Currently one 29-line paragraph. |
| 798-819 dynamical selectivity | OK | Eq. spatial is a good synthesis. |
| 822-828 synaptic low-pass | OK | |
| 832-857 resonance | TRIM | Seven caveat sentences after Eq. gain (undamped frequency, peak location, projections, stability, Arnold tongue); keep two. "Linearizing the mass" -> the JR column (Giulio). |
| 859-874 receiver equation | RECAST | D undefined until after the equation (Giulio flagged D). Define D in words before Eq. receiver; drop "Their normalization depends on where the generated drive enters" or explain it. |
| 876-879 Hopf normal form | OK | |
| 882-906 point membrane | OK | |
| 908-915 Cohen/AIS | CUT? | Third appearance; keep only in the Introduction and Table 2. |
| 917-930 fast access | TRIM | Table 2 introduction sentence is long. |
| 971-988 cable | MOVE | Supplement; keep one sentence with the cable-end number. |
| 990-998 channel kinetics | RECAST/CUT? | Unclear purpose. If kept: one sentence ("gate filters must not duplicate dynamics the detector already contains; QIF lacks Na kinetics, so a gate cutoff needs its own measurement"). |
| 1001-1017 PEIX | OK | |
| 1019-1027 state dependence | TRIM | The list of conditions (psychedelics, Alzheimer's) is speculative; one example suffices. |

## Methods

| Lines | Verdict | Note |
|---|---|---|
| 1034-1037 purpose | RECAST | Giulio: "Explain WHY". Open with: the paper's mechanism predicts square-law detection; an envelope follower or threshold predicts otherwise; two measurements distinguish them: amplitude slope and second-harmonic ratio (the "harmonic test"). |
| 1039-1066 lock-in | TRIM | The test-tone derivation of the normalization (1055-1061) can be one sentence. |
| 1068-1086 slope and harmonic test | OK after 1034 fix | Define "harmonic test" by name in the opening. |
| 1090-1118 JR integration | OK | Methods detail belongs here. |
| 1120-1133 bifurcation | TRIM | SNIC/large-cycle detail is for the figure caption only. |
| 1153-1156 | MERGE | One-sentence orphan; merge into 1158. |
| 1158-1169 | OK | |
| 1172-1213 NMM2 | OK | |
| 1215-1247 J-curve methods | TRIM | Dense but appropriate; drop "These normalizations compare gain variation, rather than establishing invariance of the detector coefficient" (defensive). |
| 1250-1308 QIF | TRIM | 1261-1273 contains Results reasoning (threshold crossing); move to Results. Convergence paragraph 1304-1308 fine. |
| 1311-1334 JR sweeps | TRIM | Settings list; compress. |
| 1337-1348 vocabulary | OK | Short; duplicates the appendix but useful. |

## Results

| Lines | Verdict | Note |
|---|---|---|
| 1351-1360 roadmap | OK | Adjust to the new order. |
| 1363-1366 demod | OK | |
| 1387-1395 resonance | OK | |
| 1416-1424 carrier | OK | |
| 1440-1455 kHz | TRIM | Numbers like 2.2e-13 belong in the caption; the last sentence (Esmaeilpour 2020) dangles; connect or move to Discussion. |
| 1459-1489 curvature law | OK | |
| 1491-1505 NMM2 PING | MOVE | Giulio: next to other NMM2 material. Proposed order: JR (demod, resonance, carrier, curvature, coupling gain, timing), shared amplifier (TI vs tACS), NMM2 (resonance, two-mode J-curve), QIF. |
| 1542-1557 JR coupling gain | OK | |
| 1559-1582 TI vs tACS | MOVE, RECAST | Own subsection; lead with the claim (matched in-band input reproduces the TI response; resonance gives no TI advantage in linear response), then numbers, then the finite-amplitude departure in one sentence. |
| 1584-1588 Arnold tongue aside | MOVE | Vocabulary/appendix. |
| 1604-1631 NMM2 J-curve | TRIM | Lead with two modes and the 1.02 exponent; endpoint-stability numbers to the caption or Methods. |
| 1634-1657 timing | RECAST | Starts with three caveat sentences on rectification; lead with the result (modulation 13x, mean 4.4x, ratio 15 -> 58 -> 44), then the explanation. |
| 1660-1689 QIF | RECAST | Giulio: message unclear. Lead: "Below the induced-gamma threshold the spiking network shows beat-locked modulation with a small mean-rate change; above it the field itself induces gamma, as an equal-power unmodulated carrier does, and only TI adds the beat line." Cutoff-convergence numbers (1669-1675) to Methods or the caption. |
| 1714-1723 carrier control | OK | Key control; keep, move up to follow the lead. |
| 1750-1755 | CUT? | Duplicates the Fig. qif_raster caption. |
| 1757-1761 sidebands | TRIM | One sentence. |
| 1763-1774 per-neuron locking | TRIM | Keep the per-neuron weak-locking point; drop the repeated timing-versus-rate statement. |
| 1777-1866 predictions | MOVE, MERGE | Giulio: Discussion. The enumerated list and Table 3 repeat each other; keep the table with a two-sentence lead. |

## Discussion

| Lines | Verdict | Note |
|---|---|---|
| 1869-1877 | TRIM | Last sentence weak. |
| 1879-1889 Cifra, terminals | TRIM | Two sentences: kHz fields act through polarization, not on proteins; small terminals need not charge faster. |
| 1891-1905 access times | CUT? | Third appearance of Esmaeilpour, Luff, Semenov; keep only what Table 2 lacks. "A new periaxonal circuit is not needed for that limiting argument" is unclear. |
| 1907-1913 | OK | Good message (not competing explanations). |
| 1915-1920 | CUT? | Repeats Theory and Conclusion. |
| 1922-1933 dose map | OK | After the envelope and DC subsections, can shorten. |
| 1935-1947 intensity regimes | TRIM | |
| 1949-1963 shared amplifier | OK | One of the clearest paragraphs. |
| 1965-1976 absolute estimates | OK | |
| 1978-1984 Q scale | CUT? | Tangential. |
| 1986-1997 Vieira | RECAST | Giulio: conclusion missing. End with: the published TI/tACS ratios are consistent with a weaker beat drive than direct stimulation, as the shared-amplifier result predicts, but neither experiment matched polarization at the mixer, so they cannot calibrate the detector. |
| 1999-2007 fast budget | RECAST | Conclusion: at a plausible fast-access budget the smooth detector gives about 0.8% of a matched direct drive, so a smooth-sigmoid TI effect would be weak; observed effects of tens of percent would point to stronger rectification or larger polarization. |
| 2009-2016 supremum | RECAST | Conclusion: no memoryless population curve can exceed about 35% of direct drive, and approaching it needs microvolt thresholds, so large TI effects at weak fields imply a mechanism beyond a smooth population sigmoid. |
| 2018-2031 limitations | TRIM | Mixed list; group by access, model dependence, human evidence. |

## Conclusion

| Lines | Verdict | Note |
|---|---|---|
| 2034-2058 | RECAST | Four paragraphs restate Theory; missing the Results headlines (shared amplifier, timing over rate, field-induced gamma control). Make it one paragraph per headline result. |
