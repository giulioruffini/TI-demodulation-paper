# Figure 2 marks every synaptic pathway with a compact LPF tag

October 9, 2026. Giulio's preference for compact tags was relayed by
`giulio-shell` at 10:20 CEST, superseding the earlier large-filter-box design.
This integration starts from `479dc0f` on `two-tone-validation` and uses
`fig-models-ti`, commit `063a493`. The working edition remains v0.15.0-draft18.
The earlier boxed version is preserved in commit `479dc0f` and is replaced
in the current article.

Panel (a) has three tags: the pyramidal output before the filtered potential
y0, the excitatory return after input p merges, and the inhibitory return.
Panel (b) has four: the AMPA and GABA connections between populations and
both self-loops. Kernel names and time constants are explained in the caption;
the repeated red low-pass stage labels are removed. These placements agree
with the model's second-order synaptic filters.

The caption describes the compact tags after the modal-gain sentence. It
retains “attenuate” rather than “remove”: the filters attenuate the carrier
more strongly than the beat and transmit the steady shift into the recurrent
loop, without an exact carrier zero. Existing explanations of filtered y0,
inverse times a and b, membrane time tau_X, frequency f0, and arrow colors
are retained.

The supplied tiny tag lettering would print at 4.57 pt. The tag font is now
scriptsize, giving 6.40 pt at its final size in the article. The two self-loop
weight labels are offset 3.5 mm rather than 2.2 mm to keep them clear of the
tags. These are the only TikZ changes relative to `063a493`. The seven tags
remain compact, and the figure retains its 506.21 × 353.09 pt size. No words
are clipped or overlap. The bounding-box check flags only two intentional
superscript/subscript intersections in v_E squared, verified in the render.

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
