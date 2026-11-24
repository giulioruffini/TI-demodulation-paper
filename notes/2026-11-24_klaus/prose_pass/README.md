# TN0484 prose pass of Theory, Methods, Results, Discussion and Conclusion (Klaus, 2026-11-24)

K asked to revise the rest of the paper "for proper writing, like we did in the intro", and to
check the changes with prosai. Snapshot: live tex after bb0ea2c (sha256 eb155f8a...).

Method: one rewriting agent per section under hard constraints (no claim, number, condition,
citation, label or equation change; words <= original). Mechanical check (check.py): every
cite/ref/label/input/number/percentage preserved; equations, figures, tables byte-identical; no
colon before a display. Independent prosai reviewers (reviewer_brief.md + fidelity.md) on the
pairs files; every material and minor finding closed by restoring the author's wording or the
reviewer's wording; a second round on Methods, Results, Discussion; Theory's flagged pairs were
restored verbatim. Rewritten headings were all restored.

Merge: 18 changed paragraph blocks applied to the live file only where the original paragraph
still matched exactly (0 skipped), so later edits by K and Kaiti (feasibility caption, units
edit) are kept. Six word-adding rewordings were then reverted to K's text to hold the length.

Length: count_jne_words.py gives 12,000 article words after the merge (the file was already at
12,008 before it; the appendix count rose by 24 today). Abstract 298.

Author's calls (relation words that state what the original implied), left in for K to confirm:
see the "author's call" rows in *_review_round_*.md. Main ones: colon -> "since" (RC is
area-independent); colon -> "because" in Missey; ";" -> "whereas" (fixed quadratic pattern;
IXI002 24% vs 0.56); "the readout v" in Methods lock-in; "so access uses tau_m = tau_E";
"this gain" in the Conclusion; Eq. (khz) label added to the cable factor in Theory.
Fidelity pass by Kaiti pending before commit of the manuscript.
