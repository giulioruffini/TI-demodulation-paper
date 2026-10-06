# Carrier comparisons do not yet isolate access from detection

October 6, 2026. Follow-up to Giulio's annotation 20 and Klaus's 19:10 literature report. Manuscript target: draft16, `e07b44a`; record baseline: `f17f278`. The manuscript and its PDFs remain unchanged during the combined fidelity review.

## The published Luff protocol

Directly checked: [Luff et al., Cell Reports 43, 114274 (2024)](https://synthneuro.org/wp-content/uploads/2024/08/2406luff.pdf), DOI [10.1016/j.celrep.2024.114274](https://doi.org/10.1016/j.celrep.2024.114274), printed pp. 2–3 and 13–15 (PDF pages 3–4 and 14–16).

Figure 1E compares seven carrier conditions, approximately 10–5,000 Hz, so “a few pairs” understates the evidence. Figure 1C uses 497/507 Hz, not 497/597 Hz; Figure 1D uses 4,997/5,007 Hz. The published C–E numbering is unchanged.

The analysis selects the largest applied stimulus without spikes for each condition. Carrier-frequency recordings are dominated by stimulation artifacts (Figure 1 caption); the reported mixing amplitude is baseline-subtracted difference-frequency RMS, compared with hardware intermodulation. The methods match artifact amplitudes between tissue and hardware controls, not true carrier polarizations across frequencies. They do not report normalization by the product of measured carrier polarizations. Subthreshold selection alone therefore does not establish the weak quadratic regime.

## Scope of the literature check

Klaus checked [Esmaeilpour 2021](https://doi.org/10.1016/j.brs.2020.11.007), [Opancar 2025](https://doi.org/10.1038/s41467-025-64059-w), Budde 2023 (`peripheral2023`), and [Semenov 2025](https://doi.org/10.1016/j.xcrp.2025.102660). His report distinguishes applied-field/current comparisons from a sweep at matched local membrane polarization. Those sources were not independently rechecked in this follow-up. This is a bounded literature check, not an exhaustive priority search.

The proposed test measures each carrier polarization at the relevant detector site and either holds both fixed or normalizes the weak beat response by their product. Beat frequency, operating state, and downstream gain must also be controlled. That normalization separates access from residual detector dynamics; a carrier sweep by itself does not. Somatic voltage is not automatically the polarization of an axonal detector.

Semenov's optical recordings motivate a possible measurement method. Their use for strong excitation and block does not by itself establish the sensitivity or artifact rejection required for weak carrier-polarization measurements. Do not describe the proposed weak-field experiment as already technically validated on that basis.

## Wording for the next manuscript checkpoint

Table 4 already specifies the required normalization and makes no priority claim. Its existing-evidence cell can be made more explicit without adding a new novelty claim:

> Carrier-frequency comparisons show changes in network sensitivity [esmaeilpour2021] and subthreshold single-cell mixing [luff2024mixer], without holding measured local carrier polarizations fixed. Excitation thresholds depend on carrier frequency [opancar2025, peripheral2023], and bare kilohertz fields have limited effects on hippocampal oscillations [esmaeilpour2020].

Retain the present test cell, including independent control of network gain. If a priority sentence is later added, limit it to the studies checked and retain “to our knowledge.” No manuscript change or rebuild was needed to record this evidence.

Integrated in draft17 after the combined draft16 fidelity report; see `revision_2026-10-06_v0150draft17_fidelity.md`.
