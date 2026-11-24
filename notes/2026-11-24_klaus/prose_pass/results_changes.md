# Results revision: changes

## Verification

- Word count of prose outside math, excluding figure and table floats (unchanged): original 1,719, revised 1,714. Including the unchanged captions and table: original 2,734, revised 2,729. Counting method: strip comments, `$...$`, `\[...\]`, `\ref/\cite/\label/\input` arguments and all control words, then count tokens that contain a letter or digit.
- Token check: every `\cite{}`, `\ref{}`, `\eqref{}`, `\label{}` and `\input{}` and every number in the original (with multiplicity) appears in the revised file. Nothing is missing and nothing has been added.
- Floats: all 11 figure environments and the 1 table are byte-identical to the original. They were spliced back in programmatically.
- Displays: no line ends with ':' directly before a display. The only display, R_lin, is introduced by "...in linear response is" with no colon, as in the original.
- LaTeX: control-word usage counts are identical to the original, braces and `$`/`\[ \]` delimiters balance, and the `\ifjne\else ... \fi` blocks (3) and their `\input` lines are unchanged. No full compile was run.
- Em-dashes: none. No banned words.

## Changes by paragraph

- Heading "Carrier independence and the kHz roll-off": now "Carrier frequency acts through access", so the heading states the finding (label unchanged).
- Heading "Realistic-head comparison of envelope and quadratic maps": now "Beat maps rescale while envelope foci move", so the heading states the finding (label unchanged).
- Heading "JR gain, mean shifts, and the tACS comparison": now "Recurrent gain is shared with tACS", so the heading states the finding (label unchanged).
- Paragraph headings "Beat modulation and mean rate." and "Comparison with tACS.": now "Beat modulation outgrows mean shift." and "TI and tACS share the linear amplifier.", so both state the finding (labels unchanged).
- "An input containing only the two tones...": the two sentences are merged into one. The paragraph now opens with the driven column, and the absent input peak becomes a concessive clause.
- "In the stable-focus regime...": split into two paragraphs, with the resonance result first and the below-Hopf dominance screen second. "Without a drive" becomes "field-free", matching Methods. The peak-shift and near-Hopf-law sentences are combined into one sentence that names what the law does and does not give.
- "At fixed post-access polarization...": "the" added before "near-Hopf JR column". The semicolon clause is rephrased with the figure as subject.
- "With an explicit first-order access state...": the assumed τ moves into the opening clause. "The absent 10.914 Hz beat" becomes "the 10.914 Hz beat absent from the input". The closing sentence names what follows from which assumption, without a passive "is calibrated by".
- "Figure~feasibility converts...": the placement of "before recurrent gain" is fixed so that it modifies the equivalent input. "These sources" becomes "both sources", and the "Thus" sentence is joined with "so".
- "At equal fields, the 0.2 ms point-membrane...": "9/1 kHz source ratio" becomes "source ratio of 0.020 between 9 and 1 kHz", so both sides of the ratio are named. The cable sentence is joined by semicolon, and the closing semicolon becomes "but".
- "The signed open-loop beat...": "occupy the negative-curvature flank" becomes "lie on"; "follows the same gain law" becomes "obeys".
- "In the recurrent column...": "surrogate comparison in panel (d) supports its use" becomes "open-loop two-tone/AM comparison in panel (d) supports the surrogate", so the antecedent is named. "Specified in §" becomes "of §".
- "In this single-subject geometric illustration...": the two centroid sentences become one sentence without the semicolon.
- "The pair-current product falls...": split into two paragraphs. The first now opens with the beat maps scaling with the pair-current product, then gives the 75% rescaling and the directions of the focus shifts. The second covers the balance contrasts, the white-matter tail, the gray-matter restriction, the mean contrasts and the selectivity caveat. "For the contrast comparison at balance" is shortened to "At balance".
- "The envelope contrast peaks at 1.24...": reordered so the paragraph opens with the 32-combination robustness of the shift directions, followed by the radial projections. The 1.24 peak and the imbalance behavior close the paragraph.
- "A laminar-aligned detector...": unchanged except "The median ratios ... across the tissue interfaces" becomes "Across the tissue interfaces, the median ratios ...".
- "For the AM surrogate, pinning v*...": "damping" and "resonance" now take articles. The finite-distance sentence is joined with "but" to the leading-scaling sentence it qualifies.
- "With genuine two tones at Δf=f0...": "modulation of r_P ... by 13.2-fold" becomes "the beat modulation of r_P 13.2-fold", so the quantity is named. "With both compared in rate units" moves next to the comparison it qualifies.
- "The detector's steady and beat sources...": reordered to open with the conclusion (a finite zero-frequency transfer does not bound the full mean shift). The source order becomes "beat and steady" to match the order of |G(ω0)| and |G(0)|, and "therefore" is dropped.
- "TI and tACS share the linear amplifier...": that sentence moves into the paragraph heading. The paragraph opens with the matching consequence and the no-advantage result. The closing two sentences are joined by a semicolon, with the supplement as the location.
- "With genuine 300 Hz tones entering E current...": "E current" becomes "the excitatory current".
- "At 300 Hz, voltage excursions mix...": "it matches" becomes "this source matches", and the participial "After division ... and propagation" becomes "Divided ... and propagated".
- "The unpinned PING coupling sweep...": reordered so the shared 1/γ law and its scope limit open the paragraph, with the evidence after. "But two modes compete" becomes "with two modes competing". The supplement sentence is recast with the supplement as subject.
- "The finite QIF network shows...": "the higher amplitude" becomes "the higher one".
- "At η=0.85 and A_f=10...": "because of cutoff and population sensitivity" becomes "because it depends on cutoff and population size", which uses the caption's wording and names the dependence.
- "At A_f=35 and η=0.85...": "This is a finite-amplitude example: ..." becomes "In this finite-amplitude example, ...". The supplement sentence is now in the active voice.
- "At η=1.5, autonomous gamma...": the coexistence sentence is joined with "and" to the dominance sentence it follows from.
- "To separate steady induction...": the statement of intention ("To separate ... we compare") becomes a result ("An unmodulated carrier matched to TI ... separates ..."). The A_f=35 and A_f=10 outcomes form one sentence joined by a semicolon.
- "At A_f=35, population beat modulation...": "Individual locking remains weak" becomes "Individual neurons lock weakly", so the agent is named.
