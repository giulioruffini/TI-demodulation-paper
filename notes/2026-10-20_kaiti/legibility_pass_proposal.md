# Draft20 opening: proposed legibility repair

20 October 2026. Scope proposal only, awaiting Giulio’s go. Source text is
unchanged from `e20c047`; current repository head before this note is
`67a2b17`. I read the live annotated PDF through page 15 and visually checked
the marked pages 5 and 8. The PDF has uncommitted annotations and must not be
rebuilt, replaced, staged, or synchronized while Giulio is reading it.

## Diagnosis

The weak-field expansion on pages 6–7 establishes the central result, but the
following page interrupts its interpretation with the dynamic coefficient,
three unrelated side remarks, and pointers to material the reader has not seen.
The exact QIF coefficient then precedes the explanation of how the envelope
and squared envelope differ. Earlier, the opening of Theory asks the reader
to absorb several model representations before showing what they explain.
The scientific qualifications have accumulated as answers to individual review
items rather than as steps in the argument. The preceding fidelity checks
verified retention and correctness, not this reading experience.

## Proposed scope

Revise the Introduction’s transitions and Theory (current pages 3–15), plus
only the destination paragraphs in Methods/Appendix B and the model-figure
caption. Keep the approved abstract, numerical results, figures, and Discussion
outside this pass. No new science or simulations; Ricardo’s pending additions
remain separate. Propose one coherent change for review rather than a sequence
of local patches.

The main reading route should be:

1. The field establishes two local carrier polarizations. Define access once,
   with its physical meaning; distinguish the electromagnetic approximation
   from the membrane’s response in the same sentence.
2. A nonlinear rate response mixes those polarizations. Derive the product-law
   beat and accompanying mean source together, and explain their meaning before
   introducing another model. Curvature supplies mixing; slope supplies local
   gain. Keep the weak-input and static-response conditions at the expansion.
3. Envelope following and quadratic detection give different waveforms and
   spatial maps. Keep the side-by-side table, harmonic test, two-site example,
   product reweighting, and current-ratio steering argument. Put the envelope
   definition where it is used, rather than in a pointer-only paragraph.
4. The steady source has a sign and a spatial restriction. Preserve the
   distinction between geometric intensity, signed source, and recurrent mean
   response, together with the boundary theorem’s conditions.
5. Synapses suppress the carrier and the recurrent circuit amplifies the beat.
   Derive the response as access times detection times gain, state the stable
   weak-response condition, and explain which role the operating point plays.
6. The exact QIF mean field tests the static approximation and extends it when
   the membrane is slower. Keep the derived rate curve, slow-synapse logic,
   carrier-relaxation condition, and slow/fast sign distinction in the main
   argument. Place the full rational coefficient, intermediate normalized
   variables, and exponent table together in Appendix B, with the necessary
   result stated in the main text. This relocation needs Giulio’s approval.

This is a proposed dependency order, not new section numbering. Before editing,
update the existing storyline map with exact source-to-destination moves after
Giulio approves the scope. Keep measured and assumed access times, the
single-neuron interpretation of curvature, shared-amplifier qualifications,
PEIX definitions, and the fast-access sensitivity argument. Model-specific
implementation details move to their existing Methods homes.

## Local repairs within that scope

- Make Introduction and Theory readable without forward section pointers.
  A reference may supply optional supporting detail; it must not substitute
  for the explanation needed at that point. Keep bibliographic attribution.
- Integrate qualifications into the relevant physical statements. Preserve
  membrane filtering once, finite response time, the nonzero mixing condition,
  and model-specific frequency dependence; do not delete these conditions
  because their present sentences interrupt the reading.
- Move the anatomical projection choices and FEM direction convention to the
  head-model Methods. Keep the general field-to-polarization definition in Theory.
- Put the AM-surrogate protocol in Methods only. Explain endogenous sidebands
  where the corresponding result is discussed rather than between the mixing
  derivation and its interpretation.
- Number the second-order susceptibility definition and remove the explanation
  of the imaginary unit. Explain memory as dependence on the input history;
  explain a vanishing quadratic coefficient at its relevant operating point.
- Reduce the model schematic caption to approximately 100–130 words covering
  panels, field entry, the nonlinearities, synaptic filters, and the recurrent
  gain condition. Preserve detailed pathway definitions in Methods/Appendix B.
- Do not change the tilde convention yet. Recommend plain variables in a
  clearly declared membrane-time-unit MPR subsection, with one explicit
  conversion back to physical time/rate. Inspect the draft13 convention first;
  do not restore a unit ambiguity merely to remove tildes.

## Review and baseline

Use the completed draft20 reading edition as the next redline baseline once
Giulio finishes and authorizes this pass. The current manuscript text is
`e20c047`; later commits only record reviews and preparation. Preserve the
annotated PDF separately. Do not change `planning/review_baseline.json` yet.

After revision, read Introduction and Theory continuously from the rendered
PDF without jumping to Methods, appendices, or Results. Verify that each
paragraph supplies what the next needs and that each displayed equation is
introduced and interpreted. Then run notation, retention, reference, and build
checks. Give Klaus a bounded independent reader’s pass before another numerical
audit. Record every relocation and any proposed substantive deletion; keep
unapproved deletions out of the manuscript.

Approval is pending because Giulio explicitly asked for a proposed scope before
editing and is still annotating. This note authorizes no manuscript changes.
