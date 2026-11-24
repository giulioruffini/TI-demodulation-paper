# TN0484 abstract and Introduction additions: content-preserving revision (Klaus, 2026-11-24)

Scope: K asked that the proposed changes not alter content and that the abstract follow
abstract form, starting with the Objective statement. Baseline is the author-edited
abstract frozen in Kaiti's proposal_v1 (baseline_abstract.md); proposals are proposal_v1
(abstract) and proposal_v2 (Introduction). Nothing here edits the manuscript.

## Abstract

Problems in the proposal, judged against the baseline:

1. Objective. "We develop a mesoscale model ... with three stages" is a method statement
   under the Objective heading. The objective (Introduction, end of first paragraph) is how
   neurons transduce the TI waveform. The model sentence moves to Approach.
2. Approach. proposal_v1 replaced "quantify conditional frequency access budgets" with
   "quantify how carrier frequency and membrane response time affect access". That drops
   both "conditional" and "budgets", which the Significance and Introduction rely on
   (the budget is conditional on the uncalibrated field-to-detector transfer). Restore,
   with K's frequency scope: "conditional, frequency-dependent access budgets".
3. Main results. proposal_v1's "the QIF mean field" for "the circuit" is kept: the
   equal-RMS gamma control was run only in the mean field (Results, QIF regimes paragraph:
   "This control has been tested only in the mean field"). This corrects a reference, it
   does not add content.
4. Significance unchanged.

Proposed text (macro bodies; JNE adds the run-in headings):

Objective. To determine how neural populations transduce temporal-interference (TI)
stimulation through three stages in series: membrane access, nonlinear detection of
envelope features, and circuit amplification.

Approach. Our mesoscale model represents access by an effective membrane
time and analyzes detection and amplification in a Jansen--Rit column, an exact mean field
of quadratic integrate-and-fire (QIF) neurons, and its spiking network. We compare spatial
maps in one head model and quantify conditional, frequency-dependent access budgets.

Main results. [baseline text, with "drives the circuit across its gamma threshold"
replaced by "drives the QIF mean field across its gamma threshold"]

Significance. [baseline text, unchanged]

## Introduction additions (proposal_v2)

The envelope definition is exact and cited (Gabor 1946); keep it.

The spatial paragraph's last sentence, "The envelope excursion and quadratic beat amplitude
can nevertheless have interior maxima (\S\ref{sec:dc})", states something \S2.5 does not
show: \S2.5 proves the restriction for intensity, |Y_DC| and the envelope mean, and says
nothing about the excursion or the product. Kaiti's local construction (notes,
envelope_boundary_scope.md) supports the claim, but it is not in the paper. Content-
preserving replacement:

"The envelope excursion and the quadratic beat amplitude are not subject to this
restriction."

Either that, or add the construction as one sentence in \S2.5 (new content: K's call).
"aims at" and "the spectrum of s(t)" are corrections and stay.

Word count: baseline 290 by whitespace split (Kaiti TeXcount 295); proposal +3, so about 298 by her count, under the JNE 300 limit.
