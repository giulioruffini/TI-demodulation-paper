# Draft8 integration: one abstract and explanations beside the tables

Klaus supplied `089e00a` on `abstract-single-source`, based on draft7 (`c4e6b0b`).
Its source changes are integrated onto draft8 (`19b8f38`) without importing its
older generated PDFs or undoing draft8's attribution correction.

The article, TN, and storyline now load the same four abstract macros from
`planning/tn0484_abstract.tex`. The JNE article adds its required run-in headings;
the wording is identical. The Approach keeps draft8's distinction between existing
axonal rectification and the candidate AIS location. The storyline reads the macros
directly instead of maintaining a text mirror.

Table 1 now has a row-by-row explanation beside it. The static curve adds no
carrier-frequency attenuation, but its slope still supplies a gain. Static mixing
acts on the attenuated voltage; dynamic QIF mixing occurs in the voltage equation
before the rate's additional integration. Both inherit the same leading access
exponent. Equal exponents do not fix the amplitudes: the prefactors include the
mixing coefficient and beat-frequency susceptibility. The coefficient K in Eq. 15
describes the uncoupled carrier-averaged response; it is not identified with the
full finite-frequency network prefactor. These qualifications refine Klaus's
proposed paragraph while preserving its explanation of the table.

Table 2 is introduced in its own section, distinguishing measured decays, assumed
filter times, field-pulse charging, the cellular detector, and downstream synapses.
Its measured axonal decay is not presented as a measured TI cutoff.
The JR parameter table also receives a local explanation of its synaptic times,
gains, sigmoid parameters, and operating-point controls. The predictions, notation,
and LaNMM tables retain their existing accompanying explanations.

At Giulio's instruction, the JNE article is the single working edition and the
default build. No new versioned PDF set is exported. The current redline is
`docs/redline_last_read.pdf`; its fixed baseline is recorded in
`planning/review_baseline.json`. `python3 code/build_jne_redline.py` updates that
comparison without advancing its baseline. Draft7 is retained from Klaus's comparison while
Giulio's last-read version is being clarified. Earlier PDFs remain historical
snapshots. TN and supplement publication wait for an authorized Calliope cut.

Validation and inspected pages are recorded in `docs/validation_current.json`.
The article and redline are 34 pages. Private validation builds of the TN and
storyline are 52 and 9 pages. Their rendered abstracts match the article after
removing the JNE headings and layout whitespace. All four builds have no errors,
undefined references, or overfull boxes; the inspected pages have no clipping or
overlap. TN and storyline validation PDFs were not exported as new reading copies.
The review shelf now shows only the JNE working article and the current redline.
No equation, numerical result, figure, or section order is changed. The source
retains all 60 cited works. GitHub push, Calliope/Zenodo, Overleaf, and coauthor
circulation remain held.
