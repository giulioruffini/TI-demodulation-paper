# The steady source is physiological, not only geometric — proposal for the Violante paragraph

Klaus, 2026-10-19, for Kaiti. Base: dbc647e (Discussion Violante paragraphs). Read-only on all sources.

Giulio's instruction (20:05 CEST): the paper should state the DC effect as physiological, not only
geometric; and he approves the abstract FEM sentence (see §3).

## 1. The point

The mean-square polarization 𝓘 is a geometric map, but at second order it sets the steady rate
source Y_DC = ½σ''(v*)𝓘 of §sec:dc, a change in mean firing rate. The 1:1→1:3 change of 𝓘 is
therefore a physiological prediction at fixed curvature: a larger hippocampal mean-rate shift under
1:3 than under 1:1, in whichever direction the local curvature sets. The current text stops at
"These are geometric changes on one anatomy".

Hippocampal (FreeSurfer label 17) means along n*, 1:3 over 1:1, from `code/fem_quadmaps.npz`
(`*__roi_mean` at share 0.75 vs 0.50), verified 2026-10-19 20:04:

| map | ratio |
|---|---|
| envelope excursion | 0.553 |
| quadratic beat | 0.750 |
| mean-square 𝓘 | 1.244 |
| isotropic beat | 0.750 |

Only the mean-square map increases from 1:1 to 1:3. Violante's ordering is an effect at 1:3 and no
detectable effect at 1:1. A response linear in the beat predicts the reverse; the beat's own
rectified mean shift (§sec:timing) scales as 0.75² = 0.56 and predicts the reverse as well.
BOLD is a hemodynamic readout of mean activity, so it is more sensitive to a mean-rate shift than
to a beat-locked modulation, which averages out at first order.

Caveats that must travel with the sentence:
- envelope excursion ratio is min(P1, 3P2)/(2 min(P1, P2)): 0.5 where P1 ≤ P2, up to 1.5 where
  P1 > 3P2 (anterior, pair 1 dominant); a thresholded envelope response is not excluded;
- the 1:1 result is a nonsignificant difference from sham (P = 0.953), not a demonstrated null;
- sign and size of the rate shift depend on curvature and recurrence; the paper fixes neither for
  hippocampus; the readout model (neural and hemodynamic) is still missing.

## 2. Proposed text

Replace, in the second Violante paragraph, the two sentences

> These are geometric changes on one anatomy: the sign and spatial pattern of the steady neural
> response also depend on detector curvature and recurrence. Neither the BOLD contrast nor the
> reported functional-connectivity changes directly measure the beat or the steady source.

with

```latex
These are geometric changes on one anatomy, and the mean-square map is not
inert: at second order it sets the steady rate source
$Y_{\rm DC}=\tfrac12\Sig''(v^*)\mathcal I$ of \S\ref{sec:dc}, a change in mean
firing rate whose sign and spatial pattern depend on detector curvature and
recurrence. At fixed curvature, 1:3 therefore drives a larger hippocampal
mean-rate shift than 1:1, in the direction the local curvature sets, while the
beat falls to $3/4$ everywhere and the hippocampal envelope mean falls by 45\%.
Of the three maps, only the mean-square map increases from 1:1 to 1:3, which is
the ordering of the BOLD result. The BOLD contrast is a hemodynamic readout of
mean activity, more sensitive to a mean-rate shift than to a beat-locked
modulation, which averages out at first order and enters the mean only through
its own rectification (\S\ref{sec:timing}). The ordering is suggestive rather
than decisive: the envelope rises locally by up to $1.5\times$ where the
anterior pair's polarization exceeds three times the posterior's, the 1:1
result is a nonsignificant difference, and neither the BOLD contrast nor the
reported functional-connectivity changes measures the beat or the steady source
directly.
```

The following sentences ("The voxelwise pattern therefore cannot be matched…", the two tests)
stay as they are. Net +95 words.

Optional, Fig. 8 caption, last sentence: "All maps are geometric, before detector gain; the
mean-square polarization weights the signed steady rate source $Y_{\rm DC}$ of \S\ref{sec:dc}
and is not itself a source."

## 3. Abstract: approved by Giulio

Sentence, as agreed with Kaiti (mean-square foci):

> In a realistic head with a published hippocampal montage, changing the current ratio moves the
> envelope and mean-square foci in opposite directions and only rescales the product map.

Constraints Kaiti set and Giulio accepts: keep "with the Jansen–Rit operating point held fixed";
keep the oscillation-threshold wording. Placement suggestion: in `\absResults` after the
product-law sentence. Compensating cuts are Kaiti's call; candidates (−16 words):
"that locate rectification in nodes and the axon initial segment" (Approach, −10);
"the mean field adds frequency dependence" → "with frequency dependence" (−3);
"and an unmodulated carrier of equal power does the same" → "as can an unmodulated carrier of
equal power" (−3).
