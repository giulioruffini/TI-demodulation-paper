# Figure 2 marks every synaptic pathway with a low-pass symbol

October 9, 2026. Giulio requested the standard low-pass symbol rather than
the letters LPF, relayed by `klaus-484-TI-helper` at 10:28 CEST. This integration
starts from `ba9bd86` on `two-tone-validation` and uses `fig-models-ti`, commit
`4626645`. The working edition remains v0.15.0-draft18. It replaces the large
filter boxes of `479dc0f` and the compact text tags of `ba9bd86` with the
conventional flat-then-descending filter icon.

Panel (a) has three symbols: the pyramidal output before the filtered potential
y0, the excitatory return after input p merges, and the inhibitory return.
Panel (b) has four: the AMPA and GABA connections between populations and
both self-loops. Kernel names and time constants are explained in the caption.
There are no LPF text tags or red low-pass stage labels. These placements agree
with the model's second-order synaptic filters.

The caption describes the symbols after the modal-gain sentence. It
retains “attenuate” rather than “remove”: the filters attenuate the carrier
more strongly than the beat and transmit the steady shift into the recurrent
loop, without an exact carrier zero. Existing explanations of filtered y0,
inverse times a and b, membrane time tau_X, frequency f0, and arrow colors
are retained.

The TikZ source and both figure assets are byte-identical to `4626645`; no
local layout adjustment was needed. All seven symbols are present and the
letters LPF are absent from the drawing. The figure retains its 506.21 ×
353.09 pt size. No words are clipped or overlap. The bounding-box check flags
only two intentional superscript/subscript intersections in v_E squared,
verified in the render. The symbols remain legible at the article's placed size.

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
