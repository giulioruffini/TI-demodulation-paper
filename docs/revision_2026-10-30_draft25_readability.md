# Draft25 — readability and supporting-detail relocation

Giulio requested another revision for succinctness, clarity, and readability
before sharing with the team, allowing supporting material to move to appendices.
The editing baseline is `8ecc70a` (draft24 manuscript content at `30ed891`).
The recorded reading baseline remains draft20, `e20c047`. The journal edition is
the deliverable; canonical TN artifacts and the annotated draft20 are preserved.

## Argument and placement

The Results now distinguishes the lower-amplitude QIF response from induced
gamma before introducing the equal-RMS carrier control and individual locking.
Repeated threshold explanations, detector derivations, and control recitals are
consolidated. The Introduction, selected captions, Discussion opening, and
Conclusion are shorter. Scope remains local: the spiking response is quantitatively
unconverged, the carrier control is mean-field only, and assumed access times
quantify model consequences rather than establish physiological access.

| Material | Main-text content retained | Supporting destination |
|---|---|---|
| Operating-point index (PEIX) | Definition in words, sign convention, curvature interpretation, physiological contexts, dynamic limitation | Appendix B, `planning/parts/peix_definition.tex`: definition and exact identities |
| Envelope mean | Matched-tone means and single-carrier interpretation | S3.1, `envelope_proof.tex`: integral and theorem assumptions |
| Rectifier catalogue | Threshold response, amplitude and harmonic predictions | S2.2, `harmonic_details.tex`: full/half-wave and diode examples |
| FEM current-ratio sweep | Direction of centroid motion, mechanism, invariant quadratic pattern, contrast limit; Table 3 numerical comparisons | S3.4, `fem_sensitivities.tex`: exact breakpoints, extrema, and posterior-share values |
| QIF numerical protocol | Populations, inputs, observables, control design, convergence criterion and failure | S4, `qif_protocol.tex`: integration, windows, cutoff settings, and leakage numbers |
| PING coupling sweep | Two modes, near-Hopf and full-sweep exponents, finite-amplitude departure, attracting endpoint | S4, `ping_coupling_results.tex`: mode intervals and amplitude-check values |
| TI/tACS saturation | Ratio law, linear prediction, matched-source agreement, matching convention | S4, `tacs_saturation.tex`: numerical saturation factors, linked to the existing S2 comparison table |
| Violante ratio conditions | Hypothesis, statistics, possible envelope increase, measurement proposal | S3.5, `steering_algebra.tex`: envelope inequalities beside the existing mean-square calculation |

Shared modules appear inline in the full TN and at the stated destination in
the journal article/supplement. The full PING system remains in Methods; the
access-evidence table remains in Theory. Every figure and numerical input is
unchanged. Float barriers keep the last QIF figures within Results and the
prediction table before the Conclusion. No figure typography or plotting data
changes in this revision.

Klaus's proposal is `notes/2026-10-30_klaus/draft25_compression_proposal.md`
(`b60dbed`). Items 1, 2, 4, 5b, 6, 7, and 8 are adopted with the destinations
above. Item 3 is declined because the access-evidence table remains part of
the article. Item 5a is declined because the multicompartment bilinear source
and its definitions support the main spatial claim. The detailed FEM sweep
moves despite Klaus's proposed retention: the principal displacement and
mean-change values remain in Table 3, with its interpretation in Results.
The PEIX relocation and reordered QIF narrative supplement that proposal.

A separate read-through restored PEIX's sign convention at first mention,
the static scalar/nonzero-curvature scope in the Conclusion, and the distinction
between testing assumed access and quantifying its consequences. It also removed
a suggestion that rectification starts only after the beat response: its
contribution grows continuously with the amplified oscillation.

## Length

| Section | Draft24 | Draft25 | Reduction |
|---|---:|---:|---:|
| Introduction | 688 | 665 | 23 |
| Theory | 3,216 | 3,155 | 61 |
| Methods | 1,703 | 1,641 | 62 |
| Results | 3,170 | 2,682 | 488 |
| Discussion | 1,460 | 1,443 | 17 |
| Conclusion | 224 | 179 | 45 |
| Article appendices | 1,497 | 1,532 | −35 |
| Total | 11,958 | 11,297 | 661 |

The main narrative is 696 words shorter; article appendices grow by 35 words.
The unchanged 299-word abstract gives a total of 11,596, compared with 12,257.
`code/count_jne_words.py` includes headings, captions, ordinary table bodies,
and article appendices; it excludes mathematical tokens, references, declarations,
and other front/back matter. These are comparative counts, not a certification
of a publisher's counting convention. The article is 39 pages (draft24: 40),
and the supplement 32 (draft24: 31).

## Checks and release scope

The article and supplement build with settled references. The final audit
compares labeled equation bodies, citations, labels, figures, abstract, original
QIF/FEM inputs, full PING system, reading baseline, canonical TN artifacts, and
annotated draft20. Full-TN routing is validated under an isolated job name.
The preservation check is `notes/2026-10-30_kaiti/check_draft25.py`; counts and
baseline hashes are in the same folder. Rendered pages are inspected for reading
order, legibility, and float placement. Redlines are built against draft24 and
the unchanged draft20 reading baseline. Independent fidelity review and delivery
will be recorded below when complete.

Ricardo's PR #2 is excluded. Its interface wording, library provenance, and
mesh-refinement inputs remain separate tasks. The public-release hold and push
guard remain active. No public push, PR merge, email, or coauthor circulation
is performed in this revision.

## Completed preservation and reading checks

The preservation audit passes: 131 baseline labels and 67 citation keys remain
and resolve; all 32 labeled equation bodies are unchanged apart from whitespace
and punctuation. The shared abstract, full PING system, efficiency derivation,
original QIF solver, FEM inputs, figure sources and artifacts, and reading-baseline
record are unchanged. Article, supplement, and isolated full-TN builds have no
errors, undefined or multiply defined references, or overfull boxes. Canonical
TN PDF/bibliography and annotated draft20 hashes match their preservation records.

All article and supplementary pages were reviewed in rendered contact sheets,
with enlarged inspection of revised passages, tables, captions, relocated
material, and appendix pages. The final floats remain within their scientific
sections. The six-page storyline is readable and matches the relocation map.
The prose checker reports no findings; a separate continuous read identified
and corrected the scope and antecedent issues described above.

Both reading comparisons are regenerated: `docs/redline_draft24.pdf` (42 pages)
and `docs/redline_last_read.pdf` against draft20 (53 pages). The older comparison
initially put deleted FEM prose inside a newly introduced numeric table, causing
an overfull cell. The redline helper now treats newly labeled tables as whole
additions, preserving deleted prose outside them. This changes review formatting
only. Both comparison builds pass, and the affected FEM page and selected major
changes were visually checked.


## Independent fidelity review

Klaus read the full source diff and every relocated block at `4ebe719`; his
report is `notes/2026-10-30_klaus/draft25_fidelity_check.md` (`0a5ad3b`). He
found the science preserved, verified the numerical content and scope statements,
and found the reordered QIF narrative coherent. His requested corrections are
applied: the supplementary envelope integral no longer repeats its phase
definition; the Conclusion names access, detection, and amplification and
restores the inverse-damping gain law. The PING heading now states amplification
of the dynamic beat source, the QIF integrator remains named in Methods, and
the Introduction names the framework shown in the figure. The optional repeated
forward pointers and extra crossover clause are not added: their qualifications
remain locally stated and the full crossover remains in Theory and Figure 12.

After these restorations the reduction is 661 article words, with 696 removed
from the main narrative and 35 added to the article appendices. No scientific
result or numerical input changed. Final artifacts and delivery hashes are
recorded in `notes/2026-10-30_kaiti/draft25_artifact_manifest.json`.


## Delivery

The verified reading bundle is `build/review_draft25/reading/`: article,
supplement, draft24 comparison, draft20 comparison, and storyline. Copies match
the canonical outputs byte for byte. The final build remains 39/32 pages;
all preservation and reference checks pass after Klaus's corrections.
No public push or coauthor message was sent.
