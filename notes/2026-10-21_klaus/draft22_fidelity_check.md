# Draft22 (ef0bfe4) fidelity and reference check: PASS, one bounded suggestion

Klaus, 2026-10-21 15:40. Read-only on manuscript files. Compared the draft21 article text
(62772c7) with the draft22 article and supplement texts; rebuilt independently.

## Builds and references
- `./build.sh journal` on this machine: article 43 pp, supplement 27 pp, 0 errors, 0 undefined;
  the rebuilt PDFs are byte-identical to the committed ones (git shows no change).
- `./build.sh tn`: inline edition 66 pp, 0 errors, 0 undefined; canonical TN files restored
  afterwards, not committed.
- Kaiti's `check_prose_revision.py` passes here: 104 labels, 67 cites, PING equation unchanged in
  Methods, abstract unchanged, bound derivation unchanged, figure order, 13 S-figure numbers.
- No "??" in either PDF. Article pointers to the supplement are specific (§S1-§S7, §S2.3, §S3.3,
  §S3.5, §S4.3, §S5.1, Fig. S4-S13); supplement pointers back to article equations renumbered
  consistently (access filter now Eq. 13, surrogate Eq. 17, PING Eq. 19).

## Sentence-level accounting (article draft21 -> draft22 + supplement)
1031 article sentences before, 956 after; 338 left the article: 134 found verbatim or near-verbatim
in the supplement, 80 rewritten in the article, 124 inspected by hand. Of those 124, every one is
either (a) a planned de-duplication whose content remains elsewhere (Intro roadmap and Results/
Discussion openers, Eq. 10 merged into Eq. 14, harmonic-test logic now once in 2.4, access prose
carried by Table 2 and §S1, 3.8 vocabulary now four sentences at first use + §S7, FEM numbers now
Table 3, 5.2 displacement values and ratio algebra now §S3.5, surrogate numbers now Table S2,
Vieira numbers now §S5.1, cutoff range now §S4.3), (b) a table or figure caption reflowed by the
layout, or (c) a reference-list line. No scientific statement, number, or qualification was found
missing from article + supplement.

## Retention list, verified in the article text
2.8: point-vs-cable, field-vs-current, 16 ms vs 0.2 ms factors, Table 2, "a measured decay is not a
TI cutoff". 2.10: MPR Eqs. 15-16, both conditions (tau_rel << tau_s; omega_c tau_rel << 1), Eq. 19
in words with B5 in App. B, fast-DC-follows-F' merged into one sentence. 3.2: forced response /
entrainment / gating defined at first use with pointer to §S7; lock-in definition. 3.3:
conductivities, 4 mA convention, fixed 1:1 projection, literal reference definition (deep gray
matter included; "cortical-reference proxy" gone), degree matching, focus definition, 32-combination
sensitivity. 3.6: cutoff qualification with pointer. 4.2: closed-loop kHz result (|Hm|^2 = 0.137,
Figs. S6, S9). 4.4: Table 3 (means, contrasts, mean change, focus shift) + directions-persist
sentence. 4.6/4.7: two-tone numbers in text, surrogate in Table S2, Rlin = 0.143, matched-source
0.99/0.93/0.90. 5.1: Cifra 1 V/m sentence with footnote; "terminals polarize more, small size does
not imply fast charging". 5.2: Violante statistics, mean-map ordering (+24% vs -45%/-25%),
hemodynamic reading, qualifications. 5.3: implications and scope with prior work. 5.4: couplings,
2-5% pointer, 0.092 mV budget, 0.8%, 0.348 statement (block unmoved, D4b open), Vieira unmatched
statement. App. B: JR spec (B1-B4, Table 6), B.1 slow-synapse display, B.2 crossover, B.3
single-cell. Supplement S1-S7 as planned; Table S2 waveform comparisons; §S7 vocabulary; §S7.1/S7.2
settings. Intro: LaNMM pointer (§S6). PING Eq. 19 in Methods 3.5 (Giulio's instruction).

## One bounded suggestion (placement, not content)
3.2 "Amplitude scaling and harmonic measurements" now opens with the four vocabulary sentences
(forced response, entrainment, gating) before its own subject. They read better as the closing
paragraph of 3.1 or as a short untitled paragraph opening Methods. No other change proposed.

## Count (Kaiti's script, math excluded)
Main narrative 14,977 -> 13,018 (text 13,332 -> 11,465; captions 1,418 -> 1,332); article
appendices 897 -> 1,503; narrative + appendices 14,521. Still above JNE's normal 12,000 (D5).
