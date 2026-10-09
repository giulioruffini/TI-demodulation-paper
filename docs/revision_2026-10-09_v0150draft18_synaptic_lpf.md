# Figure 2 shows the synaptic low-pass stage

October 9, 2026. Giulio's schematic revision was relayed by `giulio-shell` at
10:00 CEST. The integration starts from `0d15d14` on `two-tone-validation` and
uses the TikZ source and assets from `fig-models-ti`, commit `423dba3`.
The working edition remains v0.15.0-draft18.

Panel (a) places the excitatory synaptic filter between the pyramidal firing
rate and the filtered potential y0. Panel (b) labels the AMPA and GABA filters
on the E–I pathways. Both panels identify synapses as the low-pass stage.
The second-order filter equations agree with these placements: the synapses
act on the output of the nonlinear populations.

The caption adds the requested explanation after the modal-gain sentence. It
says that the filters attenuate the carrier more strongly than the beat and
transmit the steady shift into the recurrent loop. This replaces “remove,”
which would imply an exact rejection at finite carrier frequency. It also
avoids calling h_i a separate LPF box: that return kernel is labeled in the
diagram but is not boxed. The existing explanations of filtered y0, inverse
times a and b, membrane time tau_X, frequency f0, and arrow colors are retained.

The upstream figure had a small overlap between the rate r_E output label
and the word “after” in the detection annotation. Their PDF word boxes
overlapped by 25% of the smaller box. Moving only the rate label 4 mm left
removed it. The regenerated figure retains its 506.21 × 353.09 pt size.
The remaining two bounding-box intersections are the superscript/subscript
parts of v_E squared; visual inspection confirms that they are intentional
mathematical typesetting. No word is clipped. The LPF labels print at 6.40 pt
base size in the article, with smaller mathematical subscripts.

The JNE article and the redline against draft13 `c620335` were rebuilt, with
40 and 48 pages. The logs contain no errors, undefined references, overfull
boxes, or duplicate labels. Figure 2 and its caption were inspected on the
rendered article page 7 and the corresponding redline page. Figure and
equation numbering are unchanged. The main manuscript source, abstract,
references, simulation code, and caches are unchanged. The supplement, TN
validation snapshot, and storyline are retained from the authorship pass;
this update refreshes the working article and redline only.

The current-ratio steering assessment is recorded separately in
`current_ratio_steering_review_2026-10-09.md`. Its manuscript insertion still
awaits Giulio's go. GitHub push, the Calliope/Zenodo cut, Overleaf
synchronization, and coauthor circulation remain on hold.
