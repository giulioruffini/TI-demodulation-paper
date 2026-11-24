# Introduction scope check — 2026-11-24

The reordered live Introduction preserves the intended argument: conventional stimulation and its field constraint; TI's nonlinear features; construction of the waveform; detection and circuit response. The natural-candidate sentence and the sentence about neurons and neural populations should remain as approved. The analytic-envelope definition and fixed-coupling qualification remain consistent with the Theory section.

Four local scope corrections are warranted:

- Qualify the opening as **“Conventional low-frequency transcranial electrical stimulation…”**. TI is itself transcranial electrical stimulation, so the unrestricted category should not be defined by the DC-to-hundreds-of-hertz range.
- Replace **“are not subharmonic”** with **“need not be subharmonic.”** The restriction does not hold generally for excursion or beat-amplitude maps, but individual instances can be subharmonic: with both polarizations equal to the harmonic function x, the maps are proportional to |x| and x².
- State the domain condition in the mean-value explanation: **“…its average over a sphere centered there, provided the enclosed ball lies in that homogeneous tissue region…”**. The whole enclosed ball must satisfy the field assumptions; an average crossing an interface is not covered by this proof.
- Replace **“whose direction generally rotates over the beat period”** with **“whose direction varies in time when the component fields are nonparallel.”** The instantaneous field direction can change on the carrier timescale. Slow changes of its polarization ellipse or envelope geometry are different quantities, and the Introduction need not introduce them.

No change to the approved narrative order is needed. The existing distinction between no strict interior field maximum and possible modulation maxima is correct. These comments concern scientific scope only; no live manuscript changes were made.

## Applied to the shared source

The approved opening and Giulio's saved wording were retained in the canonical manuscript. The low-frequency claim now refers to conventional protocols. The explanation of subharmonicity uses a ball contained in the uniform tissue region; the ball-average inequality is equivalent to the spherical mean-value inequality for a continuous subharmonic function. The excursion and beat maps “need not be subharmonic,” and the field direction varies in time when the component fields are nonparallel, without assigning that variation exclusively to the beat period.

The reordered opening retains the analytic-envelope definition, the reference to the local existence construction in S3.1, the natural-candidate sentence, and the sentence about neurons and neural populations. The original proof, equations, and results outside the opening were not edited. The four replacements were checked against a saved snapshot in `build/2026-11-24_live_prose_merge/intro_reorder/before_scope_corrections.tex` before writing the live file.

The new Ruffini et al. reference has the title and DOI recorded by [PubMed](https://pubmed.ncbi.nlm.nih.gov/22949089/); Klaus's source check supplied the complete Crossref metadata. This is a citation check, not a new physiological calibration. The previously checked Heller and Gabor sources remain the support for the maximum restriction and analytic-envelope definition.

The subsequent, explicitly requested equation revision is recorded in `intro_equations.md`. Its final build includes this approved opening and the added Ruffini citation; that record supersedes the intermediate build snapshots.
