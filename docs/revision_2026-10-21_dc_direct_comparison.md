# TI steady and beat sources compared with tDCS and tACS — October 21, 2026

Giulio approved the quantitative abstract passage and its body explanation, with
the journal edition as the working output. He also confirmed Ricardo Salvador
as second author. The working version remains draft21; the reading date is
October 21. The review baseline remains draft20 at `e20c047`.

The shared abstract now states that the steady and beat sources are approximately
2–5% of the corresponding tDCS and tACS sources for 0.1–0.3 mV per TI carrier at
the pinned JR operating point. It explicitly matches the direct-input amplitude
to each TI carrier. The abstract is 299 words by TeXcount, excluding its run-in
headings (294 whitespace-separated tokens). To fit the quantitative passage,
the generic opening, repeated factorization statement, single-neuron provenance,
explicit static/mean-field agreement sentence, 24% FEM number, and detailed test
list are shortened or omitted from the abstract. Their explanations and results
remain in the body. The spatial steering result, signed source at depth, uniformity
conditions, slow-membrane condition, fixed-state gain comparison, timing result,
tACS amplifier, and oscillation threshold remain in the abstract.

Section 2.5 adds a comparison of equal-tone TI with direct DC and beat-frequency
inputs to the same sigmoid. It derives the equivalent direct polarization,
sigma'' epsilon squared / (2 sigma'), gives the logistic curvature-to-slope
ratio, and evaluates the source ratio at the pinned operating point. It
distinguishes per-carrier, total-peak, and RMS matching; explains that the tDCS
sign and tACS phase match a negative source; and distinguishes the direct steady
source from the additional mean shift produced by rectification of the amplified
beat. The Results and Discussion cross-reference this comparison. The existing
0.8% matched-total-peak example is retained with its different convention stated
explicitly. New polarization symbols are defined in the prose and notation table.
The added displays are unnumbered, preserving existing equation numbers.

For rho = 0.56 per mV, v0 = 6 mV, e0 = 2.5 per second and v* = 8.30 mV:

| Quantity | Value |
|---|---:|
| Sigmoid slope | 0.47446769698 per second per mV |
| Sigmoid curvature | −0.15081690850 per second per mV squared |
| Leading source ratio at 0.1 mV | 0.01589327466 |
| Leading source ratio at 0.3 mV | 0.04767982398 |
| Equivalent direct polarization at 0.3 mV per carrier | −0.01430394719 mV |

A separate full-sigmoid quadrature over 1,024 uniformly spaced phases for each
carrier checks the expansion. The mean and beat coefficients are obtained by
phase averaging and projection onto twice the cosine of the phase difference,
respectively. At 0.1 mV, the steady source is −0.00075362647 per second versus
−0.00075408454 from the quadratic approximation; at 0.3 mV it is −0.00674975509
versus −0.00678676088. The relative errors are 0.061% and 0.545%. The full-sigmoid
beat/tACS ratios are 1.588% and 4.734%, confirming the rounded abstract range.
This check concerns the static detector, not a new recurrent-network simulation.

Ricardo is second in both source bylines, PDF metadata, the ORCID and contribution
lists, README, and CITATION.cff. Existing contributions are unchanged.

The journal article builds to 44 pages and the redline against `e20c047` to
52 pages. Final build logs have no errors, undefined references, overfull boxes,
or multiply defined labels. The article's abstract/byline, comparison pages
10–11, Discussion page 33, and notation page 42 were inspected as rendered
images. The redline is regenerated without advancing the review baseline.
The previously modified journal PDF is preserved at
`_private/session_backups/2026-10-21_dc_comparison/TN0484_jne_before_update.pdf`.
Pre-existing changes to the full-TN PDF and bibliography are left outside this
commit. The supplement and full TN are not rebuilt. Public-release and sharing
holds remain in force.

## AIS interpretation

The follow-up clarification identifies s as the effective polarization in the
sigmoid-input coordinate. For AIS coupling, adding s is equivalent to shifting
the sigmoid's effective threshold from v0 to v0 − s; no backward transmission
to the soma is required. The access paragraph states that the conversion from
local AIS polarization and the compartment response time require calibration,
and that fast access alone does not validate static detection at the carrier
frequency. The comparison paragraph now names the effective input and the
dependence on both frequency and anatomical entry compartment. This incorporates
the compatible wording in Klaus's 1c4e4a3 note without introducing new symbols.
The abstract and numerical estimates are unchanged.

## Author-list update and abstract proposal at 12:10

Klaus's aad1ac2 removes Alex Just at Giulio's instruction from the source
bylines, PDF metadata, ORCID list, funding acknowledgment, competing-interest
statement, CRediT list, CITATION.cff, and README. The rebuilt 44-page journal
PDF contains eight authors, with Ricardo second. The commit was already in
the shared working tree. The current-state record now reflects this update;
the review redline is regenerated against the unchanged e20c047 baseline.

The proposed abstract in notes/2026-10-21_klaus/abstract_proposed_macros.tex
has not been applied. Its reader repairs restore what is detected, the
referent of frequency dependence, the source acting alone, and detector/carrier
qualifiers. Kaiti recommends retaining "resonant" and "approximately" in that
proposal. The installed 299-word abstract remains Giulio's last approved text.
The proposal with these two words is 300 words by TeXcount. The refreshed
redline builds without errors, undefined references, overfull boxes, or duplicate
labels; the article and redline author-list pages were inspected visually.

## Approved abstract reader repairs and fidelity check at 14:30

Giulio authorized the reader repairs; Klaus applied them in 62772c7, including
"resonant" gain and "approximately" 2–5%. The proposal described above is now
superseded by the installed macros. TeXcount independently returns 300 words
excluding run-in headings; the whitespace count is 296. Normalizing typography
and line wrapping, the journal PDF's abstract matches all four macros exactly.

Fidelity passes against the main text and the approved amplitude comparison:
the Objective names the difference frequency absent from the field; the source
law remains quadratic and signed; the 2–5% estimate remains at the pinned JR
operating point and matches the direct input to each TI carrier; slow-membrane
frequency dependence explicitly concerns detection; the gain is resonant and
the coupling comparison uses the same operating point; the steady source alone
can cross the gamma threshold; and detector curvature, carrier polarity, and
the uniformity conditions remain explicit. "Steady source" consistently names
the detector output. No body source, equation, parameter, or numerical-data file
changed in 62772c7. The numerical checks recorded above continue to apply.

The 44-page journal article builds without errors or undefined references. The
review redline is refreshed against the unchanged e20c047 baseline. Klaus's
separate check of IOP guidance was pending when this fidelity pass closed.

## IOP guidance verified at 14:32

Klaus supplied the result, independently checked against the
[JNE author guidance](https://publishingsupport.iopscience.iop.org/journals/journal-of-neural-engineering/)
on October 21, 2026, under Article structure / Abstract. The guidance says the
abstract should normally stay within 300 words and that longer abstracts may
be returned for rewriting. This is the working submission cap, rather than
a claim of automatic rejection at word 301. The abstract must be self-contained,
with no undefined abbreviations or references to tables, figures, equations,
or bibliography entries.

The installed abstract remains 300 words by TeXcount. "DC-like" appears before
direct current is expanded in the following sentence; Klaus has referred this
wording to Giulio. No abstract or manuscript change was made in recording the
guidance. The guidance-check TODO is closed; the DC wording decision is tracked
separately.
