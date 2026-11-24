# Draft27 — reader-flow revision

Giulio approved this pass on November 6 after Klaus's reader report. The
editing baseline is `8b95e2f` (draft26); the reading baseline remains draft20,
`e20c047`. The revision connects arguments, defines terms where needed, and
separates response interpretation from numerical diagnostics. It changes no
model, simulation, figure artwork, equation, or abstract.

## Changes and retained meaning

The Introduction now states findings instead of listing operations. Its static
source law, pinned JR result, dynamic QIF sign, single-head geometry, and
mean-field carrier control retain their respective scopes. The paragraph
after the product law explains how steady shifts can invalidate the fixed-state
assumption; the following paragraphs distinguish spatial weighting from the
multicompartment generalization. The equal-RMS argument points to its control.
The MPR subsection states its steady-sign result before the equations, with
weak-carrier and fixed-synaptic-input conditions.

Methods gives the response terminology a heading, expands LPF at first use,
and calls the PING parameter variation a coupling sweep. One duplicate protocol
pointer is removed. References with different destinations remain: a quota of
one supplement pointer per subsection would make the paper harder to use.
LaNMM is expanded in code availability.

The PING result identifies the plane containing the diagonal ridge and connects
the fitted exponent 1.02 to inverse damping. QIF Results retains the response
sizes, state labels, numerical limitation, and interpretation; supporting drive
and stability values are collected in S4.9. The original finite-cutoff depth is
identified as such. Quantitative weak-drive depth remains explicitly unconverged,
the equal-RMS control remains mean-field-only, and the finite-amplitude results
still do not establish an effect size under weak physiological stimulation.

| Detail removed from the article | Surviving home |
|---|---|
| Weak-drive depth range 0.09–0.16; mean-field depth about 0.13 | S4.7 gives cutoff depths 0.093, 0.127, 0.139 and mean field 0.128; S4.8 gives theta depth 0.156 and its population check. |
| About 12% change under population doubling | S4.8, Table S4: −11.9%; the article retains the convergence limitation. |
| Rectified drive 0.12, E-only threshold 0.286, voltage excursion 1.2 | S4.9, with amplitude and operating-state conditions. The threshold is now defined in words where used in Results. |
| Refined drive shift 1.65 and leading real part +0.032 ms⁻¹ | Added to S4.9 after its refinement procedure, explicitly at excitability 0.85 and amplitude 35. The article identifies instability of the averaged equilibrium. |
| Step-mixture argument, sharp-transition requirement, second harmonic near 0.15, common-amplitude invariance | Existing S5 derivation; unchanged. The unequal-polarization/protocol-matching qualification is added immediately before the Vieira comparison. |

Not every numerical detail was already supplementary. The refined shift and
eigenvalue are therefore added explicitly. The individual and pooled locking
statistics remain together in the article; moving them would separate the
evidence for its population-versus-individual interpretation.

The 0.348 paragraph now states the result and its scope: balanced TI, a direct
sinusoid, matched peak polarization, the same operating point, carrier-averaged
open-loop fundamental amplitudes, and bounded nondecreasing memoryless transfers.
The supremum remains a numerical estimate, and dynamic QIF is excluded.
S5 retains the derivation and sharp-detector consequences. This is not a
universal ceiling on TI effects.

Calibration statements are consolidated only where adjacent text repeats them.
The assumed access time, uncalibrated physiological transfer, single-subject
spatial illustration, and response limits remain beside the claims they qualify.
The spatial-correlation sentence now gives its reason: these are single-column
models. The 2–5% comparison, full PING system, access table, Violante discussion,
worked examples, and Conclusion are unchanged.

## Length, layout, and checks

The article contains 11,273 words across text, headings, captions, tables, and
article appendices, versus 11,235 in draft26. The unchanged abstract adds 299
words. The 38-word increase supplies explanatory links and local definitions;
this pass is a flow revision, not a further reduction. The article and supplement remain 37 and 32 pages, respectively. Fonts, margins, figure sizes,
and captions are unchanged. Existing figure blocks are placed earlier in their
source sections, and the Results/Discussion float barrier is removed so that
nearby text can accompany the figures.

The replacement ledger is `notes/2026-11-06_kaiti/draft27_replacements.json`;
the source diff also records float placement. The preservation script checks
equations, citations, labels, abstract, PING, figure sources/artifacts, model and
FEM inputs, edition routing, and the hashes of pre-existing TN artifacts. Final
build, rendering, redline, and independent-review results are recorded below.

Public push, PR #2, data release, Overleaf, Calliope, and coauthor circulation
remain held. Ricardo's pending inputs remain in `todo.md`.


## Final review and delivery checks

Klaus reviewed the source and supplementary changes at `cc72bad` against
`8b95e2f`; his report, `e59a2de`, finds no scientific blocker or lost content.
The budget sentence now names the sources that imply it, and the Introduction
specifies the rate curve's slope. His proposed broad “ceiling of any static
detector” gloss is not adopted: the stated monotonicity and matching conditions
remain essential. Extra blank lines are removed.

The FEM table is now introduced on page 19 with its discussion. Appendix A
follows the last reference on page 33, recovering a page otherwise occupied by
a short reference spill. Appendix B still starts a new page; the TN and
supplement retain their existing section starts. A missing space before “JR”
in the notation introduction is restored. None of these layout changes alters
content, typography, or figure dimensions.

The article, supplement, isolated full-TN routing, storyline, and redline build
successfully. The main article and supplement have no undefined or duplicate
references, overfull boxes, or printed question-mark references. The preservation
script passes all 135 baseline labels, 67 citations, and 32 labeled equations;
it also verifies unchanged abstract, full PING system, figure artifacts, QIF/FEM
inputs, recorded reading baseline, annotated draft20, and pre-existing canonical
TN artifacts. The prose checker reports no mechanical findings in the edited
scientific text. The numerical retention map was checked independently before
Klaus's full fidelity pass.

Rendered checks cover the changed article and supplementary passages, the FEM
table, Appendix A's start, the redline, and the storyline. Canonical reading
files are `TN0484_jne.pdf`, `TN0484_jne_supplement.pdf`, and
`docs/redline_last_read.pdf`. The full-TN PDF/bibliography remain untouched.
