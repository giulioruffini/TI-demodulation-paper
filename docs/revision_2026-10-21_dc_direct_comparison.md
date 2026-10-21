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
