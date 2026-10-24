# Portable FEM analysis

`code/fem_portable.py` recomputes the nodal maps, target/reference contrasts,
current-ratio sweeps, and hippocampal centroid displacements using NumPy alone.
It accepts an exported bundle of the original fields and region masks. The
bundle is **not yet available in this repository**. The consumer has passed
analytic invariant checks; its IXI002 results remain unverified until export.
The existing `code/fem_quadmaps.npz` contains figure summaries and slices,
not the underlying per-node fields.

The producer's owner can create the bundle with:

```sh
TI_MODEL_ROOT=/path/to/temporal-interference-library \
  python code/export_fem_portable.py --output /path/to/ixi002_fields_v1.npz
python code/fem_portable.py /path/to/ixi002_fields_v1.npz --output /path/to/recomputed.json
```

The exporter requires the private library and original fields and labels. It
checks the independent centroid selection against the library for both
montages, both fixed directions, both labels, both tissue definitions, every
current share, and every focus fraction. It also compares the primary
contrasts against the committed `fem_quadmaps.json`. A mismatch aborts export.
This prevents an assumed tie or rounding convention from silently changing
reported focus locations. The output and SHA-256 sidecar must be deposited
with the submission snapshot after the checks succeed.

The NPZ uses schema `tn0484-fields-v1`, with JSON metadata and arrays prefixed
by montage name (`violante__` or `yatsuda__`):

| Array | Meaning |
|---|---|
| `xyz_mm` | Original node coordinates, N × 3, mm |
| `E1_per_A`, `E2_per_A` | Original field vectors per ampere, N × 3, (V/m)/A |
| `n_star` | Unit projection maximizing the 1:1 envelope, fixed across ratios |
| `gm`, `wm` | Boolean tissue masks, N |
| `aseg`, `atlas` | Boolean hippocampal masks in the original coordinate frame, N |

The export retains floating-point precision. Metadata carries the original
input hashes, units, projection convention, and reference definition. The
reference includes all gray matter outside the target, including other deep
gray matter. It is not cortex-only. Coupling is 0.5 mV/(V/m); total peak pair
current is 0.004 A. The independent consumer additionally computes the radial
orientation check from the same brain-node centroid.

The export reproduces spatial statistics without regenerating the private FEM
mesh or interpolating sagittal images. The committed slice cache and
`code/make_fem_fig.py` reproduce those displayed images. A successful export
therefore enables independent analysis of the derived fields, not independent
reproduction of the field solver itself.

Validation on synthetic fields:

```sh
.venv/bin/python notes/2026-10-24_kaiti/check_portable_fem.py
```

These checks cover current-ratio invariance, carrier-polarity invariance,
rotation covariance, units, a known centroid and long axis, and degree-matched
contrasts. They do not substitute for comparison against IXI002.
