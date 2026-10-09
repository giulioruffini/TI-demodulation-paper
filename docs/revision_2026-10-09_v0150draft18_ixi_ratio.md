# IXI head model and current-ratio predictions

October 9, 2026. Ricardo's update was relayed by `giulio-shell` at 11:06 CEST.
The editing baseline is `29208a5`. The paper remains v0.15.0-draft18, and the
reading redline remains against draft13 `c620335`.

The planned head model is an open IXI subject with a FreeSurfer hippocampal
label. This replaces Ernie in the Methods and Results placeholders, Figure 8,
the storyline, README, and TODO. Ricardo reported that his Ernie build lacks
the hippocampal label needed for this comparison. The subject identifier,
segmentation details, and completed methods are still to come; none is inferred.

Table 4's current-ratio test now compares the predicted envelope excursion,
quadratic beat, and quadratic mean when the pair currents change from (2,2)
to (1,3) mA. The algebra uses fixed projected polarizations per unit current,
access, detector coefficients, and neural state. It supplies no FEM results.

## The scaling factors depend on different spatial quantities

Let P1 and P2 be the signed projected polarizations per unit current at a
location. Define r = |P1|/|P2| where both are nonzero; this is a local
polarization ratio, not the applied current ratio. The map factors are

    envelope excursion: min(r,3) / [2 min(r,1)]
    quadratic beat:    3/4
    quadratic mean:    (r^2+9) / [4(r^2+1)].

The envelope factor is 0.5 for r <= 1, r/2 for 1 < r < 3, and 1.5 for
r >= 3. The quadratic beat map is multiplied by 0.75 everywhere, including
at zeros, although a ratio of two zero map values is undefined.

The mean-square factor decreases with r. It is 1.25 at r = 1, 0.65 at
r = 2, and tends to 0.25 as r grows. For r < 1 it exceeds 1.25 and tends
to 2.25 as r approaches zero. Thus the proposed 1.25-to-0.25 range applies
only where |P1| >= |P2|. The table retains the full spatial range.

These predictions distinguish source maps over a spatial comparison; they
need not differ at every location. For example, the envelope and quadratic
beat factors coincide at r = 1.5. Downstream physiological effects still
require the fixed-state and readout controls already stated in the paper.

The direct map calculation was checked on 2,001 signed-polarization pairs
spanning r = 10^-9 to 10^9; the largest absolute discrepancy from the formulas
was 1.11e-16. Examples and the check are recorded in
`draft18_current_ratio_three_maps_2026-10-09.json`.

## Handoff

Both `giulio-shell` and `klaus-484-TI-helper` were asked to wait for the corrected
commit before synchronizing Overleaf. Overleaf remains the only authorized
destination. GitHub push, Calliope and Zenodo releases, and coauthor circulation
remain held. The current build hashes and inspection record are in
`draft18_fem_placeholder_audit_2026-10-09.json`.
