# v0.15.0-draft7: access, detection, and amplification

Baseline: draft6 (`be8cb21`). Klaus's ratio analysis `5732fec` is integrated as
`94439d3`, and his matched-source controls `84b2ba3` as `f0bba54`.

Giulio asked for the physical logic to organize the Introduction and abstract,
and for Cohen's periaxonal paper (reference 40 in draft6) to appear where access
and time constants are discussed. The previous ending treated access as wholly
unresolved, obscuring the candidate explanation already present in the paper.

## Argument and references

The abstract and Introduction now distinguish the field-to-membrane transfer,
nonlinear difference-frequency generation, and amplification. The Introduction
places references at the stage they support. Cohen motivates distinct axonal
voltage dynamics and the periaxonal candidate; Kole et al. supplies direct evidence
for high AIS sodium-channel density. Luff supplies evidence for a cellular mixer,
without assigning its anatomical location. Raul's unpublished WP0242 is cited
for cellular frequency selectivity, distinguished from recurrent resonance.

Cohen now appears in the Introduction, access theory, Table 2, and Discussion.
Table 2 distinguishes somatic measurements, a minimum fitted axonal decay near
1 ms, the assumed 0.2 ms fast-access model, strong-pulse charging, channel mixing,
and downstream synaptic filtering. The 1 ms fitted decay is not called a TI
transfer measurement; the 0.2 ms value is not attributed to Cohen or the AIS study.
Neither a high sodium-channel density nor nanometer geometry alone supplies a
charging time. The fast-membrane NMM2 limit and the stronger carrier-relaxation
condition remain explicit.

Primary sources checked on October 5:

- [Cohen et al., Cell 2020](https://pmc.ncbi.nlm.nih.gov/articles/PMC6978798/):
  periaxonal conduction, distinct myelin/axolemma potentials, and the minimum
  fitted axonal decay in Methods. This is the reference formerly numbered 40.
- [Kole et al., Nature Neuroscience 2008](https://pubmed.ncbi.nlm.nih.gov/18204443/):
  AIS sodium-channel density and spike initiation. Added as `kole2008ais`, with
  DOI 10.1038/nn2040, volume 11, issue 2, pages 178-186.
- [Luff et al., Cell Reports 2024](https://synthneuro.org/wp-content/uploads/2024/08/2406luff.pdf):
  extracellular near-5-kHz mixing, persistence under synaptic blockade, and
  suppression under TTX. The low-frequency intracellular control is distinct.

The Discussion now begins with access and follows it with cellular mixing and
the population reduction. The Conclusion follows the same physical sequence and
identifies field-transfer and human-field calibration as the missing quantitative
steps. The Introduction and Discussion paragraphs were reorganized; no section,
figure, or labeled equation was removed or reordered. The original 59 cited works
remain, with the AIS paper added. Earlier optional section/figure placement choices
remain Giulio's; this revision does not execute them.

The mathematical order remains: define the population transfer, specify its field
input and quadratic source, connect static and dynamic mixing, derive transduction
signatures and recurrent gain, quantify access, then state operating-point effects.
The opening now supplies the physical map before these definitions. Results test
generation, resonance, access attenuation, curvature, QIF dynamics, coupling, timing,
and the change in regime. This is an argument map rather than a new anatomical model.

## TI/tACS ratio and its scope

The common linear network transfer cancels from the response ratio at matched
state, input entry, readout, and beat frequency. With the existing amplitudes,
the predicted ratio is 0.1430395. Independent derivative and interpolation
calculations reproduce all 12 cached ratios within 6e-17, with no extrapolation.
The observed ratios are about 0.14 far from the Hopf, 0.24 at damping 1.07/s,
and 0.47 at 0.12/s. These compare the stated unequal input amplitudes, not equal
power. TI is the AM surrogate used in Figure 9.

Klaus's controls match the direct input to the leading TI beat source at three
couplings. The long-window TI/matched-tACS output ratios are 0.989, 0.941, and
0.919. Raising that tACS input by 6.991 times gives output factors 6.973, 3.949,
and 1.957. This supports earlier saturation of the larger response. Mean shifts
accompany the response and are not canceled by field-free pinning. The manuscript
does not claim that these controls isolate mean-shift feedback as the sole cause
of saturation. The matched controls sample three couplings, not the entire sweep.

The longer settling/window check changes stimulated lock-ins by at most 0.101%.
The unstimulated endpoint retains a 0.0936 mV transient after the short settling,
falling to 0.000114 mV in the longer run; the stimulated ratio persists. Klaus's
note says better than 0.1%, a slightly stricter rounding than the recorded result.
His source tables contain all 19 arrays from the two caches and match their binary
values exactly; hashes and derived controls are audited in
`ti_tacs_controls_audit_2026-10-05.json`. The small tACS cache is preserved as well.

The analytic result and cache arithmetic were independently checked here. The
new control trajectories are Klaus's calculations; their protocol, code, portable
inputs, and numerical summary are retained. This pass did not repeat all of those
trajectories or infer an equal-power efficiency gain.

## Validation and release state

The paper, JNE article, supplement, redline against draft6, and storyline are
rebuilt and inspected. Counts, hashes, retention checks, and log results are
recorded in `validation_2026-10-05_v0150draft7.json`. The prose checker is clean. The builds have 52 TN pages, 34 article pages,
20 supplementary pages, 53 redline pages, and nine storyline pages; the JNE
abstract has 277 words. There are no LaTeX errors, undefined references or
citations, or overfull boxes. Rendered abstracts, introductory mechanism
paragraphs, access table, Discussion, Conclusion, redline, and storyline were
visually inspected.
No figure data or original simulation parameters changed. Author approval and
declarations remain outstanding. GitHub push, Calliope/Zenodo, Overleaf, and
coauthor email remain held.
