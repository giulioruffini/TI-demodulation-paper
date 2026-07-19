# TN0484 → Journal of Neural Engineering: gap analysis and revision plan

Target: **JNE Paper** (IOP Publishing, ISSN 1741-2552).
Baseline: repo v0.11.0, commit `0355817`, 35 pp, 13,252 words (texcount), 25 figures.
Requirements verified against official IOP pages on 2026-07-19 (URLs at foot).

## Scope fit

Not a concern. JNE names both *neuromodulation* and *theoretical and computational
neuroscience* in its stated scope, and TI is non-invasive neuromodulation. The journal's
stricter bar ("a modest increase in classification…is generally not sufficient") applies to
decoding/classifier papers, not to mechanistic modeling, so it does not bite here.

## Hard requirements, and where we stand

| # | Requirement | Status | Action |
|---|---|---|---|
| 1 | Paper ≤ 12,000 words (≈14 journal pages) | **Under** — main text 11,162 | Designate appendices as supplementary (see below) |
| 2 | Structured abstract: Objective / Approach / Main results / Significance, ≤300 w | **Missing structure** — 270 w of continuous prose | Rewrite under the four headings |
| 3 | Section order: Intro → Method → Results → Discussion → Conclusion | **Deviates** — a `Theory` section sits between Intro and Methods | Decide: fold, or keep and justify |
| 4 | Competing-interests statement (**mandatory**, in Acknowledgements) | **Absent** | Add; needs input from all seven authors |
| 5 | Funding disclosure with agency + grant number (**mandatory**) | **Partial** — ERC GALVANI No 855109 covers GR, BM, AJ, FC only | Canals and Mirasso must supply theirs |
| 6 | Generative-AI declaration in Acknowledgements | **Present**, near-compliant | IOP wants tool *and version*; "Claude and ChatGPT" is unversioned |
| 7 | Numeric (Vancouver) references | **Effectively met** — `\bibliographystyle{unsrt}` | No structural change needed |
| 8 | Keywords | Present but thin | Expand to ~6 aligned with JNE indexing |
| 9 | ORCID per author | **Absent** | Collect all seven |
| 10 | Ethics statement | **Not applicable** — no human or animal data | State N/A if asked |
| 11 | Data availability | Present and strong (repo + Zenodo concept DOI) | Keep; not mandatory at IOP but helps |

## Correction on length, 2026-07-19

An earlier version of this document said the paper was over the word limit and needed a
1,500–2,000 word cut. That was wrong, and the error was measuring the whole `.tex` file
with `texcount` rather than the main text. The real split:

| | words |
|---|---|
| Main text, through the Conclusion and declarations | **11,162** |
| Appendices A–D (notation, Stuart–Landau, vocabulary, supplementary figures) | 2,729 |
| Whole file | 13,891 |

Main text is comfortably under 12,000, with ~840 words of headroom — which is roughly what
the Discussion needs in order to absorb the amplitude budget.

The remaining question is whether the appendices count. For IOP an appendix is part of the
article, whereas supplementary material hosted as a separate file is not. **Designating
Appendices A–D as supplementary material is therefore the whole solution**, and no further
cutting is required. JNE accepts supplementary files up to 50 MB.

Cuts made before this was noticed (§3.6 moved to Appendix C behind a stub, prose trims) are
still worth keeping — they tightened the paper — but they were not necessary and further
cutting should stop.

## The remaining real problem

Item 3 below. Item 1 is resolved by the paragraph above.

**Figure load.** 14 main-text figures against ~14 journal pages is roughly double what the
format carries; JNE papers typically run 6–10. The supplementary apparatus already exists
(11 appendix figures, numbered S1–S11), so the fix is demotion, not deletion. Target 8 main
figures. The four-model ladder (Jansen–Rit → LaNMM → NMM2 → QIF) is what generates the
figure count, and it is also the paper's main claim to generality, so the cut has to be made
without collapsing the ladder.

**Under-citation.** 40 distinct works cited is low for a JNE paper and is the most likely
referee complaint after length. The TI experimental and modeling literature in particular
is thinly represented relative to how central it is to the framing. This needs a deliberate
expansion pass, not incidental additions — target 70–90 references, weighted toward TI
mechanism and dosing work and toward competing accounts of the demodulation problem, since
the paper's contribution is defined against those.

## Format

Initial submission needs only a single legible PDF — `iopart.cls` is explicitly *not*
required until production, so the class file is a post-acceptance concern. What must go is
the Neuroelectrics/BCOM Technical Note furniture: running headers, the blue rules, and the
Document/Version/DOI title block. Plan is a separate `jne` build of the same source rather
than a fork, so the TN and the manuscript cannot drift.

Peer review: IOP is transitioning to double-anonymous, with single-anonymous available at
author discretion. JNE also supports opt-in transparent peer review (published referee
reports). Both are choices to make at submission.

## Open decisions

1. **Length strategy** — cut to 12,000, or submit over-length with justification (IOP allows
   this "provided the length is clearly justified by the scientific content").
2. **The `Theory` section** — fold into Introduction and Methods to match house order, or
   retain as a distinct section.
3. **Which 8 figures are main text**, and what gets demoted to supplementary.
4. **Anonymity** — double- or single-anonymous; and whether to opt into transparent review.
5. **Open access** — hybrid journal; subscription publication is free, gold OA is
   £1960/$2700/€2250 + VAT under CC BY. ERC funding may mandate OA; check GALVANI terms.

## Author admin to collect

- ORCID for all seven authors.
- Competing-interests declaration from each.
- Funding/grant numbers for Canals (IN, UMH-CSIC) and Mirasso (IFISC, UIB-CSIC).
- Confirm the affiliation line, which was reconstructed from the Overleaf edit plus the
  Zenodo deposit and has not been checked by those two authors.
- CRediT contribution statement (optional at IOP, but cheap and increasingly expected).

## Zenodo

The deposit's author list carries the same truncated "Palma, Raul" that was fixed in the
repo; the record needs a metadata correction. Cite the **concept DOI**
`10.5281/zenodo.21009618`, which always resolves to the latest version — currently record
`21305555` (v0.11.0, 2026-07-11).

## Sources

- https://publishingsupport.iopscience.iop.org/journals/journal-of-neural-engineering/about-journal-neural-engineering/
- https://publishingsupport.iopscience.iop.org/publishing-support/authors/authoring-for-journals/
- https://publishingsupport.iopscience.iop.org/questions/structure-and-format-of-your-journal-article/
- https://publishingsupport.iopscience.iop.org/questions/generative-ai-tools/
- https://publishingsupport.iopscience.iop.org/ethical-policy-journals/
- https://iopscience.iop.org/journal/1741-2552/page/Open%20access%20information
