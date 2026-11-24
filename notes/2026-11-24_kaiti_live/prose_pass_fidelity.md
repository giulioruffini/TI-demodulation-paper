# Independent fidelity check of the shared prose pass — November 24, 2026

The prose revisions preserve the scientific content. No material or minor change remains attributable to Klaus's pass. This check covers the actual live source, rather than the intermediate pairs alone, because the shared manuscript also contains author edits made after his snapshot.

The handoff is recorded in `notes/2026-11-24_klaus/prose_pass/` at fe3bd29. Independent Theory and Methods/Results reviews are in `theory_prose_fidelity.md` and `methods_results_prose_fidelity.md`; the separate Discussion/Conclusion review is `discussion_prose_fidelity.md`. The original and live section pairs, diffs, source snapshots, invariant comparison, counts and build logs are in `build/2026-11-24_live_prose_merge/prose_fidelity/`.

## Findings and their disposition

The Theory reviewer flagged one added citation after the equilibrium rate curve. It is absent from both `theory_orig.tex` and `theory_revised.tex`, and was already present in the live source read at 14:52 before the prose handoff. It is therefore a concurrent source edit, not a change introduced by the prose pass; it is preserved and is not counted as a prose-only change. The formula itself is unchanged. The independent review table is retained without rewriting its original finding.

The feasibility-caption expansion is the separately checked 7c2b74d change. Giulio's beat-source units edit is also preserved. The new log-rate derivation in Appendix B.3 was committed separately as b7763c5 during this check. Independent algebra verifies its exact elimination, normalized-time convention, and high-frequency beat-drive coefficient. It is not presented as a prose revision or as an already amplified rate response.

The remaining joins make existing contrasts or antecedents explicit: envelope versus squared envelope; fixed-state versus state-shift steering; waveform choices; finite-time simulations versus the slow-synapse limit; source budget versus calibration; general quadratic scaling versus subject-specific centroid motion; and “this gain” in the Conclusion. The cable paragraph now names the same normalized beat ratio used in the surrounding comparison. These clarifications preserve their conditions. None introduces a new result.

## Preservation and build checks

- All section headings and existing labels survive. No citation key or inline mathematical expression is removed. The single new citation is accounted for above; the added lock-in pointer resolves.
- Displayed equations in the prose scope are unchanged mathematically; only the separately edited equilibrium display's terminal punctuation moves. All tables are byte-identical. Figure blocks are byte-identical except the authorized feasibility caption.
- The static/dynamic detector distinction, weak-input and fixed-state restrictions, pinned field-free JR state, mean-field-only equal-RMS control, qualitative finite-network interpretation, head-model scope, Violante statistics, calibration limitations, efficiency matching and bound assumptions remain.
- Article and supplement rebuild at 39 and 36 pages. Both logs contain zero errors, undefined references, multiply defined references, or overfull boxes. Main source, abstract and model appendix remained unchanged through the check. One trailing space after the equilibrium formula was removed before commit; this whitespace-only cleanup does not change the typeset output.
- The article has exactly 12,000 words under `count_jne_words.py`, plus the 298-word abstract (12,298 combined). This is eight fewer article words than the recorded pre-pass live state; the concurrent appendix addition is included.
- Article pages 1, 11, 15, 17, 26, 27, 28 and 39 were rendered and inspected. No clipping or layout defect was found on those pages. The source/current PDF text comparison is recorded separately; this was not a fresh visual inspection of every figure.

## Remaining reader issue

Giulio's question about the slow limit is not resolved by this prose pass, which leaves that argument unchanged. The next revision should explicitly hold synaptic drive fixed, eliminate the population rate and voltage at equilibrium, retain the synaptic dynamics, and display the feedback linearization giving the stationary gain. Distinguish the local relaxation time from membrane time and network damping; distinguish the stationary derivative, which does not require slow synapses, from instantaneous tracking, which does. This is a pedagogical revision to plan separately, not a reason to undo the verified prose changes.

The shared live file remains canonical. Full-TN PDF/BBL and Klaus's separate draft-note changes are preserved. No public push, Overleaf synchronization, archive update or circulation was performed.
