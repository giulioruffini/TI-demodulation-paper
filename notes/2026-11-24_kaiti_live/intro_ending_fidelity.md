# Introduction ending: fidelity check — November 24, 2026

Giulio approved Klaus's new ending, recorded in `notes/2026-11-24_klaus/intro_ending_draft.tex` at `5f2cc8f`. The live file also contained Giulio's continuing edits. The review compares the new claims with the existing Theory, Results, Methods, and captions; it does not treat the proposed ending as evidence for those claims.

| Claim | Supporting manuscript material | Review and applied clarification |
| --- | --- | --- |
| Weak static sources follow the product and summed squares | Equations `eq:taylor`, `eq:demod`; Table `tab:transduction-maps` | Preserved. |
| Current ratio rescales a fixed beat pattern | Theory `sec:envelope`, fixed-pair-current factorization and the following state-shift qualification | Restored fixed field geometry, coupling, and neural state. |
| Steady source can act at depth; sign does not follow carrier polarity | Theory `sec:dc`; spatial maps and `tab:fem-summary` | Preserved. This makes no claim of an interior steady-source maximum or established physiological selectivity. |
| Fast QIF rectification follows slope rather than static curvature | Theory `sec:dynamic`; `fig:crossover` | Identified the weak-carrier steady **rate shift at fixed synaptic input**. |
| An equal-RMS unmodulated carrier also induces gamma | Results `sec:qif`, `fig:qif_regimes`, `app:qif-estimate` | Kept the mean-field scope and specified input current. Separated the stronger-input rectified **drive** from the preceding weak-input rate-shift result. |
| JR gain varies at fixed detection; TI and tACS share its amplifier | Methods coupling sweep; Results `sec:jcurve` and `sec:tacs-results` | Pinning now explicitly concerns the **field-free** operating point. Stimulation-induced shifts are not canceled. |
| Beat modulation exceeds the mean-rate change | Results `sec:timing` | Restored the weak-drive condition and made the response, rather than gain itself, the subject. |
| Envelope and mean-square spatial shifts differ | Methods `sec:fem-methods`; Results `fig:fem`, `tab:fem-summary` | Named centroids within the hippocampal target and described predicted targeting in one head model. These centroids use the top fraction of ROI nodes defined in Methods; they are not whole-brain maxima. |
| Tuned-receiver interpretation | The linked access, detection, and amplification results | Identified the modeled column; retained the in-vivo calibration limit. |

The attribution to Cassarà et al. is supported by [Section 5.7 of their paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC11733664/), which discusses product scaling and its current-ratio steering consequence. The attribution was retained.

Independent read-only checks covered the QIF/JR and spatial/source claims. The actual replacements are confined to the approved ending. A newer author revision replaced the first checked ending during compilation, adding access budgets, the direct-input comparison, and experimental tests. Those additions, Giulio's “steady (DC)” terminology, his network-amplification wording, and his paragraph/figure placement were retained. No numerical result, equation, or bibliography entry was changed by the fidelity edits. The exact pre-edit and revised source snapshots are under `build/2026-11-24_live_prose_merge/intro_ending/`.

## Newer ending and direct-input comparison

The later ending was checked on its own terms. Its “few percent” statement now specifies the studied JR operating point, 0.1–0.3 mV per TI carrier, and equal per-carrier/direct-input polarization amplitudes. The comparison concerns source magnitudes. Theory `sec:direct-comparison` gives 1.59% and 4.77%, rounded to 2–5%; this is not a universal ratio or an equal-total-power comparison. The conditional access budgets and proposed tests remain. The tests are described as testing detector laws and separating steady from beat responses, not as uniquely identifying every possible detector. The newer author ending omitted the earlier explicit depth sentence; the depth result remains in the article and was not deleted by this fidelity pass.

The latest fidelity snapshot and its pre-edit source are under `build/2026-11-24_live_prose_merge/intro_ending_final/`. The intermediate `intro_ending/` files record the earlier checks and the author revision that arrived between them.

The final article build passes with 39 pages, no undefined or multiply defined references, and no overfull boxes. The Introduction ending was inspected on pages 4–5. The checked main-source SHA-256 is `7d1757bc1ba349525215ae65a13e77f272e07657b018e820faccf03015ea4bb8`; it remained unchanged during the final build. Counts are 11,977 words for the article and appendices, plus the unchanged 298-word abstract (12,275 combined). The supplement was not changed. Local release and synchronization remain held.

Giulio added a paragraph break after that check and changed punctuation in the PEIX appendix. These newer working edits are preserved. The commit records the checked main-source snapshot and PDF, not a freeze of the shared working file.
