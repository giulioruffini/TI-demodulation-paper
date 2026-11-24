# TN0484: response to Giulio's annotated review

October 6, 2026. The source is the 36-page `TN0484 journal (JNE)_GR review.pdf`
in `~/Claude/desk/review`, read directly with its 26 annotations. The source hash,
annotation text, highlighted passages, and page coordinates are preserved in
`gr_review_audit_2026-10-06.json`. The earlier 13- and 14-annotation harvests
were checked too; the latter's additional “relate to curvature” comment is
addressed with annotation 9 below. The annotated originals are unchanged.

| Annotation | Review page | Change in draft15 |
|---|---:|---|
| 1 | 1 | The shared abstract states that, under uniform conductivity, access, and detection, the steady drive has its largest magnitude at compartment boundaries. “Drive” identifies the generated source; its magnitude covers either curvature sign. The beat map remains distinct. |
| 2–3 | 7 | The carrier average is connected to low-pass synaptic filtering after mixing. Membrane filtering already shapes the carrier polarization; downstream gain is then applied to the generated slow source. |
| 4–5 | 10 | New Section 2.5, “Envelope oscillations and spatial weighting,” defines spatially varying polarizations and the envelope, compares the two detector laws in Table 2, then derives their different excursion maps. The two-site example remains. |
| 6 | 10 | New Section 2.6 treats the mean shift separately, including the envelope-mean integral, the two mean-map restrictions, and the distinction from the beat map. |
| 7–8 | 11 | “The mass” becomes “the JR column (node).” |
| 9 | 12 | The coefficient D is defined before the receiver equation and related explicitly to half the JR sigmoid curvature. Its QIF normalization and dynamic scope remain. |
| 10–13 | 14 | Methods 3.1 opens with the purpose: distinguish quadratic detection from envelope following. It defines the second-to-first harmonic ratio before describing the measurement, including correction for network gain. |
| 14–15 | 22 | NMM2 mean-field, resonance, mode-switching, and coupling results are grouped in Section 4.7, immediately before the QIF network. The JR results stay together. |
| 16–17 | 25 | Section 4.8 opens with beat modulation below the field-induced Hopf versus induced gamma above it. Cutoff and step diagnostics move to Methods 3.4; the Results retain the convergence caveat and the main amplitudes. |
| 18–19 | 26 | Predictions and their evidence table move to Discussion 5.1. |
| 20 | 26 | Prediction 1 credits existing carrier-frequency comparisons in Esmaeilpour 2021 and Luff 2024. It specifies the additional normalization by the product of local carrier polarizations, with fixed beat and state and controlled network gain. No priority claim is made. Follow-up: the published Luff Fig. 1 and Methods were checked directly; see [the evidence record](carrier_polarization_literature_2026-10-06.md), which distinguishes seven carrier conditions from a sweep at matched carrier polarization. |
| 21 | 28 | Section openings state their results; repeated roadmap prose is reduced; model results are grouped. Numerical qualifications and examples are retained. The new schematic and explanations make the article longer overall; this pass does not claim a net cut. |
| 22–23 | 30 | The Vieira comparison ends with its implication: test how the same timing readout scales with local polarization. A ratio at one field strength does not identify the detector law. |
| 24, 26 | 30 | The illustrative budget is identified as a generated-drive estimate, not a PLV prediction. Its consequence is a polarization-calibrated amplitude sweep using the same readout. |
| 25 | 30 | The detector-bound paragraph ends by separating local curvature, relevant to the weak-input theory, from the sharp-threshold ceiling outside that expansion. |

The separately approved model schematic is Figure 2. It uses Klaus's corrected
`c7ce5e0` source, with caption definitions reconciled to draft14 notation.
The side-by-side focality table and Figure S13 retain the earlier approved
integration. The reading redline remains against draft13, `c620335`.

## Content retained and proposed removals

No explanation, example, qualification, or numerical result was removed.
The QIF cutoff paragraph moved verbatim to Methods; the carrier-leakage window
comparison moved verbatim into the equal-RMS figure caption. Repeated window
settings were removed from the Results because they remain in Methods and the
raster caption. Generic repeated Discussion pointers were shortened. All
numbered equations, 60 cited works, and existing figures remain.

No substantive removal is proposed for approval in this pass. A further length
reduction that removes scientific material requires a separate list and Giulio's
decision. The current edition is ready for his reading, not released or submitted.
