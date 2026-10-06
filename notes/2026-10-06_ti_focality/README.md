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
bounded mathematical and attribution review. Delivery was confirmed; review
completion will be recorded separately when received.
