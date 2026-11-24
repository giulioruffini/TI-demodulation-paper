# Field coupling note

`field_coupling_note.tex` is the standalone report requested by Giulio on November 10, 2026. The compiled deliverable is `../../output/pdf/TN0484_field_coupling_note.pdf`. The report uses the dimensional QIF/MPR equations from Ruffini's NMM2 preprint, distinguishes cellular polarization from a current input and a recurrent response, and proposes a parameter study for Raul using Zhao's network.

The JR addition answers Giulio's follow-up about a 0.2-mV polarization. Its equilibrium calculations show modest steady rate changes and a separate effect on oscillatory stability. These calculations do not determine the attractor after the stability crossing. No time-domain neuronal simulations were run, and the Zhao protocol remains proposed.

Section 3.2 derives the physical static transfer curve from MPR, retains the field term through the slow-synapse reduction, and separates the cellular input coefficient from recurrent gain. It distinguishes the bare curve from a transfer measured after internal feedback has settled and gives the local conversion to JR-like coordinates. The source appendix records the relevant corrections to the old Appendix K. The reduction and feedback argument are prior results; `slow_limit_positioning.md` records their published placement. A dedicated research paper would require the proposed calibration and prediction tests, rather than a new claim for this reduction.

Build from the repository root with `bash notes/2026-11-10_kaiti/build_field_coupling_note.sh`. The build is isolated from the manuscript artifacts. The editable source also uses standard pdfLaTeX packages and its own bibliography.

The source audits are `prior_coupling_sources.md`, `qif_coupling_review.md`, and `zhao_protocol_review.md`. `jr_dc_response_review.md` records the equilibrium, frequency-response, and stability calculations. The public Zhao revision examined is `cd6a240`; it predates the published article and requires a small reproduction before a new simulation campaign.

Run `check_field_coupling_note.py` with NumPy, SciPy, and PyMuPDF to verify the dimensional-to-normalized mapping, compare the MPR transfer formula with a full synaptic-state Jacobian, check slow-limit equilibrium gains by finite differences, and inspect the build log and PDF. Run `check_jr_dc_response.py` with NumPy/SciPy to reproduce the JR calculations. Both scripts write JSON records. Independent scientific reviews checked the dimensional equations, JR results, slow-limit reduction, and Zhao implementation claims; their requested corrections were incorporated. The final PDF was rendered and visually inspected.

Draft29 adds the short version to manuscript Theory 2.9, with one gain equation and attribution to the prior work. Existing manuscript text, figures, model equations, and numerical results are preserved. The full derivation stays in this note. Public repositories and coauthor correspondence were not changed.
