# Ricardo’s orientation and interface results: integration decision

20 October 2026. Scientific base: `9181d2d`; Ricardo’s verbatim report and
Klaus’s consistency check are in `e375fa4` and `7b472cb`. The private
`ricardo/fem` tree was checked through the GitHub API: it remains `d779094`;
no `points_2_3.json` or orientation/interface producer is present.

Prepare the additions now and integrate their numerical claims once the JSON,
producer or archived producer revision, and HippUnfold version are available.
The manuscript currently attributes every FEM Results number to
`code/fem_quadmaps.py`; the new analysis has a different producer. Nothing in
the present manuscript needs retraction. Its numerical content and PDFs remain
unchanged during this preparation.

## Scientific scope

The orientation result changes the anatomical interpretation: being transverse
to the long axis does not establish alignment with a laminar detector. Report
angles separately for each carrier and the envelope-maximizing direction.
Angles to the laminar field use its valid coverage, not the entire 1,568-node
ROI. The reported laminar fractions use each map’s own orientation maximum;
the quadratic and mean-square denominators are not automatically the values
at the envelope-optimal direction used in Figure 8. A product of median cosine
factors is only an illustration; use the reported nodewise ratios for results.

The near-interface statistics do not show that every point near CSF is dimmer.
They compare gray-matter 99th percentiles in two node sets. Likewise, maxima
at boundary nodes and values within 2 mm of an interface are different tests.
The almost identical boundary-maxima fractions for the beat and mean-square
maps make the FEM observation nondiscriminating here. Preserve the fixed
spatial projection used for that check, rather than substituting the spatially
varying envelope-optimal direction.

The proposed numerical lower/upper-bound interpretation needs correction.
For isotropic conductivities, continuity of tangential electric field and
normal current gives

    E_low = T E_high,  T = I + (r - 1) nu nu^T,
    r = sigma_high / sigma_low >= 1.

Here `nu` is the unit interface normal, `I` is the identity matrix, and the
subscripts identify the low- and high-conductivity sides. Consequently
`|E_low| / |E_high| <= r`: this is a norm bound. It does not bound the ratio
of arbitrary fixed projections. With `nu = (1,0)`, `E_high = (1,1)`,
`n = (1,-0.9)/sqrt(1.81)`, and `r = 1.79/0.40 = 4.475`, the projected
amplitude ratio is `(r - 0.9)/(1 - 0.9) = 35.75`, while the norm ratio is
3.2423. Cancellation in the denominator invalidates the projected bound.
Identical carrier vectors supply the same example for the projected envelope
and the square of that ratio for the quadratic maps. This example concerns
an arbitrary fixed projection; the low-side envelope-optimal direction also admits violations, as shown by
the exact example below. Do not attach a universal 4.5/20 upper-bound label
to the reported projected jumps.

The 20% and 46% normal fractions give `j = 2.538` if treated as the fractions
at one paired location with a continuous tangential component. They are
reported marginal medians. Their inversion neither measures the median of
paired normal-component ratios nor establishes a one-sided numerical error.
With the exact constant ratio 4.475, a 0.20 normal fraction would map to 0.6744
under the ideal local relation. The mismatch warrants paired residuals; it
does not prove that all recovered map jumps underestimate the continuum
answer. Use “mesh-dependent recovered jumps; convergence not established,”
not “resolution-limited lower bounds.”

Boundary-condition reference, checked directly:
[Haus and Melcher, §7.2](https://web.mit.edu/6.013_book/www/chapter7/7.2.html).
These arguments qualify the interpretation, not Ricardo’s reported numerical
measurements, which cannot yet be independently recomputed from the repository.

## Proposed additions after provenance is supplied

The text below is a proposal, not manuscript content. Its numbers are those
reported by Ricardo; verify them against the forthcoming JSON before insertion.
Keep the full orientation and interface tables in the analysis record rather
than reproducing the entire email in the main article.

### Methods, sec:fem-methods

Define the local laminar direction as the normalized gradient of HippUnfold’s
inner–outer Laplace coordinate, sampled at the nearest voxel without smoothing.
Insert the actual version and invocation. Define PC1 as the anterior-positive
long axis, PC2 as lateral-positive, and PC3 as PC1 cross PC2; PC3 is normal to
the ROI’s best-fit plane. Angles are unsigned, 0–90 degrees, with nodewise
medians and interquartile ranges. Give 934 valid and 565 interior nodes and
the interior criterion. State the one-sided element-field recovery, projection
direction, paired interface sampling, distance approximation, and local-maxima
criterion from the producer. Split the provenance sentence between the existing
map producer and the new orientation/interface producer.

Reference verified in the publisher’s record:
DeKraker J, Haast RAM, Yousif MD, Karat B, Lau JC, Köhler S, Khan AR (2022).
Automated hippocampal unfolding for morphometry and subfield segmentation with
HippUnfold. *eLife* 11:e77945. https://doi.org/10.7554/eLife.77945.
The reference does not establish the version used for IXI002.

### Results, sec:fem-results: orientation

```latex
The carrier fields follow neither the hippocampal long axis nor the local
laminar direction in this subject. At 1:1, median angles to the long axis
are $71^\circ$ and $58^\circ$ for $\mathbf E_1$ and $\mathbf E_2$, and
$66^\circ$ for $\mathbf n^*$. The corresponding angles to the laminar
direction are $69^\circ$, $72^\circ$, and $69^\circ$ on the 934 nodes where
that direction is defined (59.6\% of the ROI). A laminar-aligned detector
therefore samples less than the orientation-optimal maps: median nodewise
fractions are 0.29 for envelope excursion, 0.11 for quadratic excursion,
and 0.12 for mean-square polarization, each relative to its own maximum
over orientation. Restricting the comparison to 565 interior nodes gives
0.25 and 0.08 for envelope and quadratic excursions. These are geometric
projection factors for one anatomical hypothesis, before detector gain.
```

Use a single brief cross-reference from `sec:coupling`: the laminar comparison
quantifies why an orientation maximum is a bound rather than a measured
anatomical coupling. Do not call all three denominators `n*`. The alternative
cap rendering and carrier-separation values remain in the analysis record;
any cap-compatibility statement should refer specifically to occupied
20-mm-disc positions in the studied layout, not all possible 10–10 caps.

### Results, sec:fem-results: interfaces

```latex
Recovered map jumps across tissue interfaces are modest along the same
$\mathbf n^*$. Median lower- to higher-conductivity-side ratios for envelope
excursion, quadratic excursion, and mean-square polarization are 1.17, 1.28,
and 1.25 at CSF/gray matter, and 1.13, 1.33, and 1.34 at gray/white matter.
These ratios describe the recovered fields at this mesh resolution; their
continuum limits have not been established. Gray-matter 99th percentiles
within 2~mm of CSF are 0.90, 0.86, and 0.93 times those farther away, so
this comparison shows no CSF-adjacent tail enhancement. The upper tail is
concentrated on the white-matter side of the gray/white interface.
```

Caption sentence: “In this mesh, gray-matter 99th percentiles within 2 mm of
CSF are 0.86–0.93 times those farther away; the upper tail is concentrated on
the white-matter side of the gray/white interface.” This describes calculated
statistics; it does not claim that every nearby point lacks enhancement.

Discussion sentence: “Along a spatially fixed projection, the recovered
mean-square maxima mostly lie on compartment boundaries, but so do the beat
maxima; these mesh-dependent observations are consistent with, and do not
sharply test, the restriction in Section [sec:dc].” Keep the 95%-within-2-mm
statistic as a separate proximity limitation in the analysis record.

## Items needed from Ricardo

- Commit the JSON and producer or an accessible source snapshot with its exact
  revision, invocation, settings, and input identifiers. A private solver need
  not be rerun here, but quoted summaries must be reproducible or traceable.
- Supply the HippUnfold version, command, coordinate definition, valid-node mask,
  and the masks/weights used for each reported median and fraction.
- Confirm each fraction’s denominator: its map-specific orientation optimum
  versus the common Figure 8 direction. Preserve the nodewise calculation.
- Provide paired interface residuals if interpreting the 20%/46% fractions;
  convergence is needed for a numerical lower-bound claim. Otherwise omit it.

No new email is authorized by this note. Klaus is preparing Giulio’s reply;
Giulio sends it. Public release holds remain unchanged.


## Analytic check closed

Klaus’s `c84bd01` establishes the magnitude and own-orientation-maximum bounds
and accepts the corrections to the median inversion and fraction denominators.
For a nonnegative degree-k homogeneous map f, let M be its maximum over unit
orientation. Since n dot (T E_j) = |T n| m dot E_j, where m = T n / |T n|,
`M_low <= r^k M_high`. Choosing n proportional to T-inverse times a high-side
maximizer gives `M_low >= M_high`. Thus the optimized excursion and intensity
maps have ratios in [1, r^k], under the common isotropic interface transform.
The directional-grid overshoots in Klaus’s diagnostic are numerical errors in
approximating the maxima; the analytic inequalities do not require that grid.

An exact two-dimensional example closes the special case of a projection
chosen to maximize the envelope on the low-conductivity side. Set r = 4.5,
T = diag(r, 1), n = (1,1)/sqrt(2), E1_low = n,
E1_high = T-inverse n, and E2_high = k(1,-1). Then E2_low = k(r,-1).
For k >= sqrt(2)/(r-1), n is an exact low-side envelope maximizer: its first
projection is 1 and its second is at least 1, attaining the upper bound set
by |E1_low| = 1. Held fixed on the high side, however, its second projection
is zero and its first is (1 + 1/r)/2. Small perturbations of E2_high make the
high-side envelope and quadratic excursions arbitrarily small while their
low-side values remain nonzero. Their ratios therefore have no finite bound.

For the mean-square map, the ratio in this same construction is

    [1 + k^2 (r-1)^2 / 2] / [(1 + 1/r)^2 / 4].

It grows without bound with k. At k = 2 it is 68.2809917355, above r squared
= 20.25; the high-side projections are (0.6111111111, 0), and the low-side
projections are (1, 4.9497474683). These values were checked directly with
NumPy. This is an analytic counterexample, not an estimate of the hippocampal
field distribution.

For the envelope itself, the exact low-side optimum does retain a lower bound
of one for a defined ratio: its numerator is the low-side maximum, which is at
least the high-side maximum, while its denominator is at most that high-side
maximum. This does not give a finite upper bound. The quadratic and mean-square
maps evaluated along the envelope optimum do not inherit this lower-bound
argument, because that direction need not maximize either map. Apparent envelope
ratios below one from a finite orientation grid are optimization error, not
counterexamples to the exact inequality. Klaus supplied this refinement in his
14:09 CEST addendum; it is consistent with the exact construction above.

Only signed projections or signed beat coefficients can have negative ratios.
Envelope excursion, quadratic excursion, and mean-square maps are nonnegative;
their ratios are nonnegative when defined. The correction concerns the absence
of a universal conductivity-ratio ceiling, not negative values of these maps.

The bounded analytic review is closed. Ricardo’s measured table remains a
reported numerical result awaiting its JSON/producer; no manuscript change is
needed before that provenance arrives.
