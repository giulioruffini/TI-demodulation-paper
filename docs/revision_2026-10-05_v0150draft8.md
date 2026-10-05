# v0.15.0-draft8: attribution of axonal TI mechanisms

Baseline: draft7 (`c4e6b0b`). This is an attribution correction following Klaus's
message relayed by Giulio. The draft7 abstract's “We propose fast axonal
compartments” gave the population paper credit for an existing line of TI work.

The abstracts now credit single-neuron models for axonal ion-channel rectification.
Our contribution is the representation of candidate fast access by a short
effective membrane time and its connection to population mixing and recurrent
gain. The Introduction, coupling paragraph, Discussion, Conclusion, planning
abstract, and citation summary use that attribution consistently. The positive
access hypothesis and its quantitative calibration gap remain.

## Source boundaries

- [Mirzakhalili et al., Cell Systems 2020](https://doi.org/10.1016/j.cels.2020.10.004)
  demonstrates subthreshold rectification in a myelinated-axon model. Figure 3D
  compares active and passive axons; Figure 3F examines currents at a node of
  Ranvier. The Methods specify active nodes and passive internodes. The full
  [author manuscript](https://sonar.rero.ch/documents/309379/files/bar_bti.pdf)
  was checked for this revision. The Introduction now identifies the modified
  MRG model as using Hodgkin-Huxley channel dynamics, rather than implying two
  separate axon models in this paper.
- [Wang et al., Journal of Neural Engineering](https://pmc.ncbi.nlm.nih.gov/articles/PMC9942661/)
  reports suprathreshold activation originating in the axonal arbor and conduction
  block for some TI orientations. Sampling the AIS does not establish it as the
  site of TI rectification. Its existing bibliography metadata is retained.
- [Kole et al., Nature Neuroscience 2008](https://pubmed.ncbi.nlm.nih.gov/18204443/)
  supports high AIS sodium-channel density and spike initiation. It is not a TI
  localization experiment. The AIS remains a candidate in this paper.

Klaus's proposed replacement, which identified both the AIS and nodes as established
TI rectification sites, was therefore narrowed. Cohen's periaxonal evidence still
motivates distinct axonal and somatic responses; it is not treated as a measured TI
transfer or as evidence for an AIS charging time.

## Validation

The TN, JNE article, supplement, storyline, and redline against draft7 are rebuilt.
The validation record stores page counts, file hashes, citation and structural
retention checks, and build diagnostics. No simulation, data, equation, figure,
or section order is changed. The prose checker reports no mechanical findings.
The inspected pages have no clipping or overlap. The TN, JNE article, and
supplement remain 52, 34, and 20 pages; the redline is 52 pages and the storyline
9. All builds have no errors, undefined references, or overfull boxes. The JNE
abstract is 281 words. All 35 section/subsection headings, 23 figure labels,
32 equation labels, and 60 cited works are retained. Release holds remain in force.
