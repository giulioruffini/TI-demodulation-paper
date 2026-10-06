# Envelope and quadratic TI: two-page reading note

Prepared October 6, 2026 at Giulio's request, against TN0484 manuscript commit
`c620335`. The manuscript, figures, simulation caches, and release holds are unchanged.

The note distinguishes the applied two-tone field, its positive envelope, an ideal
envelope-following output, and a weak static quadratic output. Spatial dependence
is explicit throughout. It compares DC and modulation maps, illustrates a shared
central modulation peak and a reversal of target preference, and scopes the
homogeneous-compartment maximum principle to local detector sources.

- Source: `ti_envelope_quadratic.tex`.
- Reading PDF: `../../output/pdf/ti_envelope_quadratic.pdf`.
- Figure producer: `make_spatial_maps.py`; assets: `spatial_maps.pdf` and `.png`.
- Independent numerical integral checks: `map_checks.json`.

The source cites Grossman et al., Cell 169 (2017), Figs. 1–2 and STAR Methods,
DOI 10.1016/j.cell.2017.05.024. Its envelope-excursion map is distinguished from
the additional assumption of an unadapted neural response proportional to the
positive envelope. The quadratic calculation is the static limit from TN0484,
not a claim that dynamic detectors have identical DC and beat coefficients.

For the illustrative line profile, the projected amplitudes can be obtained from
the harmonic potentials phi_1 = -E0 z (1+x/L), phi_2 = -E0 z (1-x/L), using a fixed
z-directed polarization and a0 = lambda E0. The profile is not confined in the
transverse directions and does not establish three-dimensional focusing. The
two-site numerical example specifies local amplitudes, not an electrode montage.

## Build and checks

From this directory, with NumPy, SciPy, and Matplotlib available:

```sh
MPLCONFIGDIR=/tmp/tn0484-focality-mpl python3 make_spatial_maps.py
mkdir -p /tmp/tn0484-focality-build
latexmk -pdf -interaction=nonstopmode -halt-on-error \
  -outdir=/tmp/tn0484-focality-build ti_envelope_quadratic.tex
```

The project venv `../../.venv/bin/python` was used for the figure. The generator
checks envelope means against independent temporal quadrature, verifies the
quadratic means and examples, and runs figcheck for text collisions and size.
The LaTeX build has two pages and no undefined references or overfull/underfull
boxes. The prose checker reports no findings. Both rendered pages were inspected;
PDF text coordinates confirm separation of the final body lines and footers.

Giulio authorized a direct peer check. The supplied name `klaus-282-TI-helper`
did not resolve; the live TI helper is `klaus-484-TI-helper`, who was sent the
bounded mathematical and attribution review.

## Independent review closed

Klaus returned a passing review on October 6 (message timestamp 17:14). He
independently checked signed-amplitude examples, both means and excursions, the
normalized spatial profiles, and the fivefold/twofold reversal. He confirmed the
attribution to Grossman and both Laplacian identities. The envelope-mean proof
uses A = norm(a + b cos(theta), b sin(theta)); both components are harmonic.

No corrections were required. His optional qualifications are recorded here:
the strong maximum principle excludes any interior maximum unless the map is
constant on the connected compartment; constant anisotropic conductivity is
also covered after a linear coordinate change; and spatial changes in the sign
of sigmoid curvature can produce extrema in the physiological DC response even
when the unweighted quadratic map has none. The PDF retains its narrower true
statements and its existing spatial-curvature qualification. It is unchanged
from commit `4904c6e`.
