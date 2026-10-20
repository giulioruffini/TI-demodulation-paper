# Draft21: whole-paper legibility revision

October 20, 2026. Reading baseline: draft20, `e20c047`. Giulio approved a
whole-paper revision and confirmed that annotation was finished. The annotated
root `TN0484_jne.pdf` is preserved byte-for-byte; its SHA-256 is recorded in
`notes/2026-10-20_kaiti/annotated_pdf_preservation.json`.

## Reading copies

- Article: `build/review/TN0484_jne.pdf` (44 pages; draft20: 47).
- Supplement: `build/review/TN0484_jne_supplement.pdf` (23 pages).
- Redline: `build/review/redline_draft20.pdf`, against `e20c047`.
- Storyline: `build/storyline/tn0484_storyline.pdf` (6 pages).

The abstract remains the approved 299-word text. No simulation, cached result,
reference entry, or FEM data was changed. The full TN is not regenerated during
this reading pass. Release holds remain in force.

## Organization and prose

Theory now introduces the JR population curve, derives the beat and steady source,
then explains the envelope, spatial weighting, harmonic signatures, and signed
steady response. Synaptic filtering and recurrent amplification follow. The QIF
mean field closes Theory as the extension beyond a static detector, with its
slow- and fast-carrier limits stated locally. Forward section pointers and
sentences whose sole content was a pointer were removed. Qualifications remain
attached to their physical claims.

Methods opens each procedure with its purpose. The anatomical projection choices
are with the FEM methods. The model schematic is beside the model definitions;
its caption identifies the pathways without repeating the equations. Results
leads with the finding and then its evidence. Captions retain panel definitions,
units, comparisons, and conditions; interpretation and procedural details are in
the adjacent text or the supplement. Discussion separates access, spatial
predictions, amplification, efficiency, and model limitations. Conclusion states
the supported results and their tests in connected paragraphs.

Detailed material retained in the supplement:

- the general NMM1 operator, exact MPR coefficients, crossover expressions,
  and exponent table beside the existing derivation;
- JR coupling-sweep settings, the QIF finite-cutoff checks, and PING endpoint
  stability diagnostics;
- detailed bifurcation behavior formerly embedded in a caption.

The AM-surrogate protocol has one home in Methods. Endogenous sidebands are
explained with the result that exhibits them. The harmonic-filtering example
and its off-resonance control are together with the proposed tests. Experimental
Vieira details and the direct protein-field scope remain in attached footnotes.

## Notation

The main QIF equations use physical time and rate, explicitly `tau_m r = F(Q)`.
The coefficient derivation states its local membrane-time units before using
plain symbols. This removes the tilde notation without dropping time-scale
conversions. The crossover plot and notation table follow that convention;
only plot labels and rendering were changed. The general second-order beat
coefficient now has a numbered equation. The elementary definition of the
imaginary unit was removed.

## Length

Identical `texcount -sum -sub=section` commands were run on the baseline and
revision. Counts below combine prose, headings, and captions in the main source;
shared inputs and mathematical tokens are excluded. They measure both compression
and relocation, not removal of scientific content.

| Section | Draft20 | Draft21 |
|---|---:|---:|
| Introduction | 758 | 740 |
| Theory | 4,750 | 3,968 |
| Methods | 3,961 | 3,557 |
| Results | 3,938 | 3,423 |
| Discussion | 2,773 | 2,711 |
| Conclusion | 279 | 203 |
| Total | 16,459 | 14,602 |

The main reading path is 11.3% shorter by this measure. Across the entire source,
including the relocated supplement, the reduction is about 5%; detailed evidence
has largely moved rather than disappeared. Full count outputs are in the dated
notes folder.

## Checks and limits

The article, supplement, and redline compile with no errors, undefined references,
multiply defined labels, or overfull boxes. The deterministic prose checker
reports no findings. All 99 original labels and all 67 cited keys remain; five
labels were added for the new equation and relocated material. These inventories
check retention, not scientific validity. Representative rendered pages, the
shortened captions, and the crossover plot were visually inspected. The plot's
existing tick-object overlap checker flags a tick-label collision that is not
present in the rendered image.

No new scientific removal is proposed. The seven older `CUT?` passages remain
subject to Giulio's decision. Ricardo's pending orientation/interface data remain
separate, awaiting the producer and metadata. An independent reader check by
Klaus is requested on the committed revision; it is not another numerical audit.
