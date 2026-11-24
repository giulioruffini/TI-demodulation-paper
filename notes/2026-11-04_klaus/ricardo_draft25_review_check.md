# Ricardo's review of draft25 (4 November 2026): verification and recommendations

Source: Ricardo Salvador's message of 4 November 2026, 16:45 CET, on the FEM thread
(Gmail message 1a1a73d00da3bf5c). He read draft25: his Fig. 9, Table 3, Section 5.2
and Section S3.3 references match the numbering of the draft25 PDFs built at 28d5902.
Every number below is recomputed from `code/fem_quadmaps.json` at that commit unless
stated otherwise.

## 1. Target-reference contrast (his point 1)

Verified. The mean-based companion is defined in Methods 3.3 (line 969) and in the
supplement (`planning/parts/fem_protocol.tex`, line 89) and reported nowhere.
Values from `conditions` and `upper_tail_1to1`:

| Map | ROI mean / reference p95, 1:1 | same, 1:3 | p95 contrast, 1:1 | ROI nodes above reference p95 | WM share of those nodes |
|---|---|---|---|---|---|
| Envelope | 0.807 | 0.583 | 1.221 | 11.5% | 0.517 |
| Quadratic beat | 0.607 | 0.607 | 1.167 | 7.0% | 0.587 |
| Mean square | 0.471 | 0.536 | 0.918 | 4.1% | 0.662 |

The ROI is 25.1% white matter (394 of 1,568 nodes). The envelope's upper tail sits
8.6 mm anterior and 5.8 mm lateral of the ROI centroid. The conductivities he quotes
(0.40 gray, 0.15 white, S/m) are the ones in S3.3. His tissue-asymmetry reading is
therefore consistent with the committed data: the p95 contrast above 1 rests on a
white-matter-weighted anterolateral tail, and the ROI mean sits below the reference
p95 for every map.

The gray-matter-only ROI contrast is not in the JSON. The sensitivity grid holds
128 rows (2 montages x 2 labels x 2 tissue definitions x 4 focus fractions x 4 maps)
with displacements only; the `robustness` block holds contrasts for the atlas label
and the radial direction, not for the gray-matter-only ROI. Ricardo offers the numbers.

Recommendation: add the mean-based contrasts to Table 3 (one column, 1:1 and 1:3),
add the gray-matter-only contrast when he sends it, and say in Results 4.5 that the
1.22 is a p95 contrast carried by a white-matter-weighted tail. The existing sentence
"These modest contrasts separate geometric predictions but do not establish
physiological deep selectivity" stays and gains support.

## 2. Section 5.2 and the +24% (his point 2)

Verified for the stored variants. Mean-square ROI mean rises from 0.009426 to
0.011727 mV^2, +24.4%, for the FreeSurfer label with gray and white matter along n*.
For the atlas label the JSON gives +29.7% (0.008442 to 0.010950 mV^2). The radial,
gray-matter-only and Yatsuda variants do not store ROI means at both ratios, so the
sign across all 32 combinations cannot be checked from the repository. His
confirmation is needed and he expects it to hold.

His node-level claims (envelope rises at 0% of hippocampal nodes under 1:3, mean
square at about 95%) need per-node data that the repository does not hold. The
algebra fixes what to expect. With anterior polarization a and posterior b at 1:1,
the 1:3 condition gives a/2 and 3b/2. The envelope 2 min(|a|,|b|) rises only where
|a| > 2|b|; the mean square (a^2 + b^2)/2 rises where |b| > sqrt(3/5) |a| = 0.775 |a|,
that is |a/b| < 1.29. The JSON records the ROI distribution of |a/b| as
p5/p50/p95 = 0.69/0.94/1.44, so the envelope rises at fewer than 5% of nodes and the
mean square at roughly 90 to 95%. His fractions are what the stored distribution
implies; the exact values need his script.

Recommendation: keep the 5.2 sentence, since the +24% holds for both stored labels,
and add his 32-variant confirmation and the two node fractions to the supplement's
steering-algebra section (`supp:steering-algebra`) when they arrive. The node
fractions also sharpen the caveat in 5.2: the selective-envelope route exists in
cortex, not in this hippocampus. If K prefers to wait, the sentence holds for the
days his check takes.

## 3. Smaller points (his point 3)

- Table 3, mean-square row, 1:3 column: degree-matched value missing. sqrt(0.903) =
  0.950, so the entry should read 0.90 (0.95). The quadratic row is unchanged at 1:3
  and correctly repeats 1.17 (1.08).
- Fig. 9(f): confirmed on the render of `figures/fig_fem.pdf`. Panel (f) draws the
  three map colors and two bands with no legend; the caption describes line and band
  but not the colors. Add "colors as in (e)" to the (f) caption phrase.
- Code availability: `code/fem_orientation_interface.py` and `.json` enter the
  paragraph after the PR #2 merge. Already on the list.

## 4. Licensing of the per-node export (his point 4)

Confirmed on 4 November at brain-development.org/ixi-dataset: "This data is made
available under the Creative Commons CC BY-SA 3.0 license", with a request to
acknowledge the source. The repository is CC BY 4.0 (`LICENSE`, `README.md`, and the
article's code-availability line).

CC BY-SA 3.0 lets an adaptation be licensed under a later BY-SA version, so the
per-node export can be a separately licensed CC BY-SA 4.0 data file with IXI
attribution, while the code stays CC BY 4.0. That needs a LICENSE file in the export
directory, a line in the README, and one sentence in the code-availability paragraph.

Two related facts. `code/fem_quadmaps.npz` already holds a T1 slice of IXI002
(`slice_t1`, 130 x 164) that Fig. 9 draws as background, and the supplement cites
the dataset only in a URL footnote. The paper should acknowledge the IXI dataset in
the terms it asks for, in the Acknowledgments or in S3.3.

## Decisions for K

1. Table 3: add the mean-based contrasts now and the gray-matter-only contrast when
   Ricardo sends it (recommended).
2. Section 5.2: keep the +24% sentence while his 32-variant check runs (recommended),
   or hold it.
3. Export license: CC BY-SA 4.0 data file with IXI attribution, code unchanged
   (recommended); add an IXI acknowledgment to the paper either way.
4. Reply to Ricardo: draft in `reply_ricardo_2026-11-04.md`, including an optional
   paragraph that corrects his 30 October "none above" statement.

Kaiti owns the manuscript edits; this note proposes, it does not edit.
