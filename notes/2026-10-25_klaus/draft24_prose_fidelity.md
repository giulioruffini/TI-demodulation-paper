# Draft24 prose checkpoint: fidelity and readability check

Klaus, 2026-10-25. Requested by Kaiti (handoff 10:53). Scope: the diff ac20693..cbe5b7b
of `TN0484_envelope_demodulation.tex` and `planning/tn0484_notation.tex` (411 insertions,
501 deletions; Theory, Methods and Results shortened, 13,471 to 11,880 words), read in
full against the baseline, each shortened passage checked for lost qualification,
example or reasoning, and for flow. Kaiti's retention checks (labels, citations,
equation bodies, unchanged sections) were not repeated. No live file was edited.

Verdict: the compression preserves the science. Every numerical outcome, every
equation and every scope statement I looked for is still there or lives in the section
the text now points to. Three passages need a correction and a handful of sentences
lost a qualifier or a step that the reader needs; the rest is wording.

## Needs correction

1. Results, carrier independence (line 1227 of cbe5b7b): "the point and cable
   attenuation estimates of \S\ref{sec:khz} are compared in Fig.~\ref{fig:khz}". The
   figure has no cable curve (direct, 0.2 ms and 16 ms point membranes plus the 1/f^2
   guide). The cable estimate is drawn in Fig.~\ref{fig:feasibility}(a) (dotted) and
   tabulated in Table~\ref{tab:doors}. Draft23 gave the two sets of numbers here
   instead. Suggested: "the point-membrane cases are shown in Fig.~\ref{fig:khz}; the
   sealed-cable estimate is compared with them in Fig.~\ref{fig:feasibility}(a)".

2. Results, kHz closed loop (line 1247): "This tests the specified fast-access hypothesis
   and coupling." Draft23: "This quantifies the fast-access hypothesis under the specified
   response time and coupling." The simulation computes the consequence of an assumed
   access time; it cannot test the hypothesis, which is what the referee framing of
   draft23 took care to say. Suggested: "This evaluates the consequence of the assumed
   access time and coupling, not their validity."

3. Theory, dynamic section (line 866): "Synaptic circuit resonances can survive the
   fast-membrane limit without intrinsic cellular resonance
   \cite{brunelhakim1999,brunelwang2003}". Draft23 cited Brunel for "recurrent E--I
   circuits can resonate without intrinsic cellular resonance" and made the
   fast-membrane-limit statement itself. The merged sentence attributes the second claim
   to the citation. Suggested: "Recurrent excitatory--inhibitory circuits resonate without
   intrinsic cellular resonance \cite{...}; such synaptic modes survive the fast-membrane
   limit, whereas modes requiring finite membrane dynamics need not."

## Lost qualification or reasoning worth half a sentence

- Results, J-curve (line 1394): the inference "a network effect, since the local detector
  curvature is fixed while the recurrent transfer changes" is gone; only the subsection
  title carries it. Restore the clause after "resonance sharpens".
- Results, timing (line 1424): "in this weakly driven regime" dropped from "a small mean
  change accompanies larger beat modulation". The scope matters for the Vieira comparison.
- Theory, envelope (line 423): "Envelope following is an additional response assumption"
  was the only sentence in the article that said so explicitly; the Introduction and
  Discussion do not. Suggested ending for the paragraph: "... and an envelope-excursion
  map alone specifies no mean output; envelope following is itself a response assumption."
- Theory, steady source (line 571): "At the pinned JR state, v* = 8.30 mV, the source
  lowers the local rate" lost its reason, Sigma'' < 0. Add "(Sigma'' < 0)".
- Theory, coupling (line 351): "the validity of a static detector at the carrier frequency
  ... require[s] calibration". Draft23 said fast access does not establish static
  detection at the carrier; that is a modeling question answered by the MPR crossover
  (\S\ref{sec:dynamic}), not a calibration. Suggested: "... require calibration, and fast
  access alone does not make the static detector valid at the carrier frequency
  (\S\ref{sec:dynamic})."
- Methods, QIF (line 1113): the purpose "to compare beat-locked and ongoing activity at
  the spike level" is gone; the paragraph now opens with what is simulated but not why.

## Wording and flow

- Theory, transduction (line 509): "This transduction T(A) contains only even powers".
  T(A) is no longer defined (draft23 defined it in the first sentence of the subsection)
  and is used nowhere else; write "This transduction, T(A) = Y_LF(A), ..." or drop T.
- Theory, operating point (line 806): the subsection now opens on the PEIX definition.
  Draft23's motivating clause, "Because Y_Omega is proportional to Sigma''(v*), ...",
  is what tells the reader why an operating-point index belongs here. One clause.
- Theory, dynamic (line 888): "In this realization, the unit coefficient of v^2 ..." has
  no antecedent; draft23 said "QIF thus provides a cellular realization of quadratic
  detection". Write "In this cellular realization of quadratic detection, ...".
- Theory, envelope (line 400): "Its nonnegative envelope is" after a sentence about
  epsilon_j(x): "Its" reads as the envelope of one tone. "The nonnegative envelope of
  the two-tone polarization is".
- Theory, direct comparison (line 619): "Compare TI's steady and beat sources with ..."
  is an imperative where the paper otherwise says "We compare".
- Methods, NMM2 (line 1096): "Both Hopfs are located by bisection of the leading Jacobian
  eigenvalue" repeats line 1089, which already says so for eta_H. Keep one.
- Methods, lock-in (line 935) and NMM2 (line 1052): a blank line now separates the
  sentence from its display equation. With parskip loaded that adds a paragraph skip
  above the equation and the sentence ends without its colon or comma binding. Remove
  the blank lines.

## Checked and fine

The new qualifier "outside their natural band" (carrier independence) matches the
Fig.~\ref{fig:carrier} caption (deviations as f_c approaches the natural band). The
numbers dropped from Results (10^-4 to 10^-6; 10^-2 to 10^-3; eta_H = 1.110) remain in
Theory and Methods. The DC term of the expansion, dropped from the sentence after
Eq.~\eqref{eq:demod}, is displayed in Eq.~\eqref{eq:taylor} and treated in
\S\ref{sec:dc}. The notation routing (\ifappendices guards) hides exactly the six
supplement-only rows and adds the pointer sentence. The reweighting example, the
202-fold contrast, the 2 and 40 ratios, the 13.2 and 4.4 factors and the 14.5/58/44
sequence, the 30-fold J-curve gain, and all solver settings read identically.
