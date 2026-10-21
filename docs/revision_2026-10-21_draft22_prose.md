# Draft22: approved prose and placement revision

October 21, 2026. Giulio approved the joint first pass and appendix/supplement
layout, with the full PING system retained in Methods. Klaus recorded that decision
in `24d34c1`, the immediate editing baseline. The reading/redline baseline remains
unchanged at draft20, `e20c047`. The efficiency-bound placement remains undecided;
its Discussion block and supplementary derivation remain in their existing roles.

## Reading copies and changes

The canonical article is `../TN0484_jne.pdf` (43 pages); the supplement is
`../TN0484_jne_supplement.pdf` (27 pages). The storyline was updated and compiled
before editing. The approved abstract and author order are unchanged, including
Ricardo Salvador second. The full PING equation is byte-identical and remains in
Methods; its number changes as earlier equations are consolidated.

The prose pass removes repeated stage descriptions, access literature, harmonic
test explanations, waveform comparisons, and amplitude-ratio derivations. The
spatial receiver equation is consolidated with the general receiver equation;
its old label remains a resolving alias. The tDCS/tACS comparison is now Theory
Section 2.6. Its 2–5% result, effective-input convention, sigmoid dependence, and
source-versus-response qualifications are retained. Main-text definitions still
distinguish forced response, frequency dominance, phase capture, and gating.

The FEM numerical catalogue is now a table. The main Methods retain conductivity
values, current and projection conventions, ROI/reference definitions, degree
matching, and the focus statistic. Full electrode/solver procedures and sensitivity
ranges are in the supplement. The Violante discussion retains the biological
statistics, mean-map ordering, hemodynamic interpretation, and qualifications;
repeated displacement values and ratio algebra move out of that discussion.
Vieira's detailed numerical footnote moves to the supplementary comparison, with
the unmatched-input/readout qualification retained beside the main claim.

Article Appendix A retains notation. Appendix B contains the JR specification,
static-rate/synapse display, and compact MPR crossover calculation. The core MPR
equations and static-rate curve stay in Theory; both relaxation-time conditions
are stated there. Supplementary sections group access, detection, spatial maps,
amplification/checks, efficiency, the laminar extension, and metrics/settings.
The harmonic ladder, mixture inversion, envelope-mean proof, orientation averages,
run catalogue, and waveform-comparison table have explicit destinations.

The 35 shared blocks in `planning/parts/` keep a single source for relocated
material and figures. All 13 supplementary figure numbers are preserved, with
figures placed by topic. The article imports supplementary labels and the
supplement imports article labels. `./build.sh journal` settles both sets of
cross-references without rebuilding or replacing the canonical TN. A temporary TN
build verifies the inline route; the pre-existing canonical TN files remain untouched.

## Length

Counts combine text, headings, and captions, excluding mathematical tokens.
They are reproduced by `notes/2026-10-21_kaiti/count_prose_revision.py`.
The full raw counts are in `notes/2026-10-21_kaiti/prose_revision_wordcount.txt`.

| Section | Before | After |
|---|---:|---:|
| Introduction | 742 | 688 |
| Theory | 4,499 | 4,207 |
| Methods | 3,433 | 2,336 |
| Results | 3,409 | 3,184 |
| Discussion | 2,691 | 2,400 |
| Conclusion | 203 | 203 |
| Main narrative | 14,977 | 13,018 |
| Article appendices | 897 | 1,503 |
| Narrative plus appendices | 15,874 | 14,521 |

The narrative is 1,959 words shorter (13.1%). Restoring integral material to
article Appendix B makes the net reduction 1,353 words (8.5%). Body-text words
alone fall from 13,332 to 11,465; article-appendix text adds 1,430. These counts
exclude the abstract, declarations, and references. The complete article therefore
still exceeds JNE's normal 12,000-word length. This is the agreed recount after
the first pass, not a claim of compliance or authorization for further cuts.

## Validation and review

Article and supplement builds complete with no errors, undefined references,
multiply defined labels, or overfull boxes. The temporary TN build passes the
same checks. The retention script verifies all 104 baseline labels and 67 cited
keys, unchanged PING equation and abstract, unchanged supplementary bound
argument, main-figure citation order, and all 13 supplementary figure numbers.
The annotated draft20 PDF remains byte-identical. The deterministic prose checker
reports no findings across the main source and shared blocks.

Rendered checks covered the title/abstract, FEM table and adjacent interpretation,
article crossover appendix, supplementary waveform table, and storyline. The
current redline was rebuilt against `e20c047`. No simulation, data cache, figure
asset, or reference entry changed. Klaus's independent fidelity/reference check
is requested on the committed revision; its outcome is recorded below when received.
Public GitHub, Calliope, Zenodo, and further coauthor circulation remain held.
