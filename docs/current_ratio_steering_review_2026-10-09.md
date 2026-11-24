# Current-ratio steering at fixed carrier field shapes

October 9, 2026. Scientific review requested by Giulio through `giulio-shell`
at 09:56 CEST. Reviewed against draft18 author commit `291a5e2`, with placement
record `e9601e1`. This note supplies the assessment before Giulio's decision;
it does not change the manuscript, bibliography, figures, or builds.

Implementation update, October 9: Klaus clarified at 10:31 CEST that Giulio's
earlier approval covered these additions. The refined argument is integrated
in draft18; see [the revision record](revision_2026-10-09_v0150draft18_steering.md).
The assessment below records the review preceding that integration.

The proposed factorization is correct. A quadratic beat map can have an
interior focus, but changing only the currents of two fixed electrode pairs
cannot move its normalized spatial pattern at a fixed operating state. The
Violante interpretation needs correction, and the FEM protocol needs an
orientation held fixed across current ratios.

## The factorization applies to the leading quadratic response

Let position be **x**, let the positive peak current in carrier channel j be
I_j, and let f_j(**x**) be its signed local membrane polarization per unit
current, for fixed electrodes, carrier frequency, and linear access. Currents
in mA and f_j in mV/mA give ε_j(**x**) = I_j f_j(**x**) in mV. For a smooth
transfer σ about a fixed local operating point v*, the cosine amplitude of the
difference-frequency source is σ″(v*) ε_1 ε_2 / 2. A fixed linear network
response therefore has

    R_Ω(x) = I_1 I_2 B_Ω(x),
    B_Ω(x) = σ″(v*_x) G_x(Ω) f_1(x) f_2(x) / 2

in the local approximation, where Ω is the difference angular frequency and
G_x is the network susceptibility. B_Ω includes all fixed spatial weights.
Consequently the normalized magnitude map, its maxima, and target-to-cortex
ratios are independent of the current ratio whenever the leading response is
nonzero. An absolute response threshold can change the extent of a detected
region under global rescaling; that is a different readout from the position
of the map's maximum.

This consequence does not require a static sigmoid or a homogeneous head.
A fixed second-order dynamical kernel is bilinear in the two first-order
carrier responses, so it retains the factor I_1 I_2. Fixed spatially varying
access, orientation, cellular mixing, and linear propagation through a network
also retain it. A changing physiological state does not.

The design conclusion is to change at least one carrier's field shape.
Redistributing current among several electrodes at one carrier frequency is
one way; several electrodes at both frequencies are not required. State the
result for fixed pairs and frequencies rather than for every possible
four-electrode arrangement.

## The DC map changes with current ratio

Before detector gain, the quadratic mean is

    D(x) = [I_1² f_1(x)² + I_2² f_2(x)²] / 2.

For the proposed comparison, (I_1,I_2) = (2,2) versus (1,3) mA, the beat
everywhere is multiplied by 3/4, whereas

    D_13 / D_11 = (f_1² + 9 f_2²) / [4(f_1² + f_2²)].

The mean increases by 25% where |f_1| = |f_2|, but increases only where
|f_2/f_1| > sqrt(3/5) and decreases on the other side of that boundary.
The two conditions have equal summed currents, not equal local RMS
polarization or necessarily equal deposited power. Under fixed total current
I_tot and ratio r = I_2/I_1, the beat scale is
I_tot² r/(1+r)², maximal at equal currents.

The DC source can change local curvature and network gain, indirectly changing
the beat pattern. In a regular weak-input expansion about a stable equilibrium,
its feedback into an already quadratic beat enters at fourth order. Close to
a bifurcation, the small stability margin can make that correction substantial.
The test therefore needs a stable operating state and a current-amplitude
sweep, not an assumption that every nominally small input leaves gain fixed.

Strong or threshold-crossing responses can also allow ratio-dependent
steering. They do not automatically follow the ideal envelope excursion
2 min(|ε_1|,|ε_2|). That law requires an envelope-following response; a general
threshold detector has its own amplitude and threshold dependence. Even an
ideal envelope follower need not move its maximum in every field geometry.

## The orientation must not change with the tested ratio

For Ricardo's ratio sweep, use the cortical normal or another fixed anatomical
direction at each location. If a deep-structure comparison instead uses the
direction that maximizes envelope excursion, freeze the direction selected
at a reference ratio. Reoptimizing that direction at every ratio changes the
quadratic readout as well as the stimulus and can produce apparent steering
that is absent for a fixed population orientation.

An alternative is to maximize the quadratic map itself. For real local carrier
field vectors **E**_1 and **E**_2 and a unit direction **n**,

    max_n 2 |(n·E_1)(n·E_2)| = |E_1||E_2| + |E_1·E_2|.

This follows from the eigenvalues of the symmetric matrix
(**E**_1 **E**_2ᵀ + **E**_2 **E**_1ᵀ)/2. Both sides retain the factor I_1 I_2,
and the optimizing directions are independent of positive current rescaling.
This orientation envelope is a geometric upper bound, not a specified neuronal
population. Fixed anatomical projections should remain the primary comparison.

As a numerical illustration, with per-unit field vectors (1,0) and (0.3,0.9),
the envelope-maximizing direction changes from 37.875° at currents (2,2) to
2.121° at (1,3). The quadratic excursion divided by I_1 I_2, evaluated along
those changing directions, changes from 1.246 to 0.666. A fixed direction gives
exactly the same normalized product in both conditions. The maximum formula
above agreed with direct symmetric-matrix eigenvalues to relative error
7.0e-16 for 128 Gaussian vector pairs (NumPy RNG seed 484). These are algebra
checks, not FEM results.

## The literature requires attribution and a narrower physiological claim

[Cassarà et al. (2025), Part II, §5.7](https://onlinelibrary.wiley.com/doi/10.1002/bem.22536)
already identifies the product-law steering limitation. Cite that prior result;
record Ricardo's contribution to its use and test here under conceptualization
and methodology, subject to his CRediT confirmation. The article is in
*Bioelectromagnetics* 46, e22536, DOI 10.1002/bem.22536.

[Violante et al. (2023)](https://synthneuro.org/wp-content/uploads/2023/12/2310violanteFULL.pdf)
reports a direct encoding-stage 1:1 versus 1:3 BOLD contrast, P = .015
(Fig. 3b), but no stimulation-by-region interaction, P = .76. Envelope steering
also has cadaver evidence (Fig. 1i), beyond the models. Regional FC differences
appear in Fig. 4, so avoid dismissing all spatial physiological evidence.
Fig. 1b pairs e1–e2 and e3–e4 across hemispheres; they are not separate left
and right pairs.

These observations do not identify a displacement of the demodulated neural
beat map. Inferring its amplitude law from BOLD requires an additional
observation model. A larger condition effect cannot, by itself, select
envelope following over a DC-mediated state change. The Discussion should
separate the condition contrast, envelope geometry, and the unmeasured spatial
beat response rather than infer a detector class from which condition differs
from sham.

## Proposed insertion after approval

Theory paragraph after `eq:reweight`:

> With one fixed electrode pair per carrier and linear access, the local
> polarizations take the form ε_j(**x**) = I_j f_j(**x**), where I_j is the pair
> current and f_j is its polarization per unit current. The leading quadratic
> beat response at fixed operating points is therefore I_1 I_2 times a fixed
> spatial map. Changing the current ratio rescales that map without moving its
> maxima or changing target-to-cortex contrast, as anticipated by Cassarà et al.
> This restriction also holds for a fixed dynamical quadratic detector. Steering
> then requires changing at least one carrier's field shape, for example by
> redistributing current among electrodes at that frequency. The steady source,
> proportional to I_1² f_1² + I_2² f_2², does change shape and can alter the beat
> response indirectly through operating-point shifts. Envelope-following or
> other threshold-dependent responses can permit a different dependence on the
> current ratio.

Table 4 should test the normalized beat map across current ratios at fixed
electrodes, frequencies, anatomical projections, and operating state. A
quadratic map stays fixed; an ideal envelope map can move. Measure the mean
response separately and repeat at lower amplitudes to test state dependence.
A displacement rejects the combined fixed-state quadratic prediction, not
quadratic cellular mixing irrespective of its network context.

The existing independent-amplitude row measures a local response law; this row
tests its spatial consequence. No new FEM result is claimed. The current note
and TODO are the only project changes; manuscript integration awaits Giulio's
go. All release holds remain.
