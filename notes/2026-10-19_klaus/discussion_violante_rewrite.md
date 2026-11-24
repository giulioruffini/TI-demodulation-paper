# Proposed rewrite of the Discussion current-ratio paragraph (draft20)

Giulio asked (2026-10-19) for the plain logic to go into the Discussion: what Violante et al.
showed, what each account predicts for 1:3, and why the BOLD difference does not pick a detector.
The text below replaces the paragraph beginning "Current-ratio experiments separate envelope
geometry" and ending "the BOLD contrast does not choose among them." Kaiti owns the file; this is a
proposal. Sources: Violante 2023 full text (PMC10620081) for P = 0.006 (sham vs 1:3), P = 0.953
(sham vs 1:1), P = 0.015 (1:1 vs 1:3), the voxel percentages (sham > TI 1:3: Ant 30%, Mid 2%,
Post 25%), and "larger nominal magnitude in the Ant region"; the P = 0.76 interaction is the value
already in the manuscript; 24% and the displacements are from code/fem_quadmaps.npz
(msp roi_mean ratio 1.244, env +2.54 mm, msp -4.49 mm, quad 0.00 mm). The 0.77 threshold is
(P1^2 + 9 P2^2)/[4(P1^2 + P2^2)] > 1  <=>  |P2| > sqrt(3/5) |P1|.

```latex
Current-ratio experiments separate envelope geometry from the neural response
map only if the response is resolved in space. Violante et al.\
\cite{violante2023} compared $2+2$~mA (1:1) with $1+3$~mA (1:3) through the same
electrode pairs. Field models and cadaver measurements showed that 1:3 moves the
envelope peak from the middle to the anterior hippocampus. The 1:3 condition
reduced the encoding-stage blood-oxygen-level-dependent (BOLD) response of the
hippocampus relative to sham ($P=0.006$) and to 1:1 ($P=0.015$), whereas 1:1 did
not differ from sham ($P=0.95$). The reduction was nominally largest anteriorly
but significant across the hippocampus, with no stimulation-by-region
interaction ($P=0.76$); the affected voxels lay at both ends, 30\% of the
anterior and 25\% of the posterior segment against 2\% of the middle.

A difference between 1:1 and 1:3 is expected under every account, so by itself
it does not identify the detector. On one anatomy the three maps of
\S\ref{sec:fem-results} respond to the ratio change in three ways
(Fig.~\ref{fig:fem}). The envelope focus moves 2.5~mm anteriorly, the direction
of their steering. The quadratic beat keeps its pattern and falls to $3/4$ of its
value everywhere. The mean-square polarization, which weights the steady source,
changes by $\mathcal I_{1:3}/\mathcal I_{1:1}
=(\mathcal P_1^2+9\mathcal P_2^2)/[4(\mathcal P_1^2+\mathcal P_2^2)]$, which
exceeds one only where $|\mathcal P_2|>0.77|\mathcal P_1|$; in this head its
hippocampal mean rises by 24\% and its focus moves 4.5~mm posteriorly. An
envelope-following detector therefore predicts an anterior effect, a square-law
detector the same spatial pattern with a weaker beat, and a steady-source route a
stronger effect shifted posteriorly. Equal summed currents hold the local
polarization fixed under none of them. The observed pattern, both ends and not
the middle, matches none of the three cleanly, and BOLD measures neither the beat
nor the steady source. The discriminating experiment is a spatially resolved beat
measurement at controlled state, whose focus either moves anteriorly, stays fixed,
or moves posteriorly.
```

Net length: about +110 words over the current paragraph.

## Correction (Kaiti, 2026-10-19 18:45, accepted)

The closing sentence overstated: a beat measurement has two outcomes under the two detector
laws (focus moves anteriorly, or stays fixed at three quarters strength). The posterior shift
belongs to the mean-square polarization, which weights the steady source and is not a beat
focus; the steady-source route is tested separately, by an equal-power unmodulated carrier
control. The mean-square focus is also not a neural-response focus without detector and
network assumptions, and the three maps changing does not by itself guarantee a BOLD
condition difference under every account. Kaiti integrates with these scopes.
