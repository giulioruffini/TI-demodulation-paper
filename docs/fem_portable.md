# Portable FEM analysis

`code/fem_portable.py` recomputes the nodal maps, target/reference contrasts,
current-ratio sweeps, and hippocampal centroid displacements using NumPy alone.
It accepts an exported bundle of the original fields and region masks. The
bundle is **not yet available in this repository**. The consumer has passed
analytic invariant checks; its IXI002 results remain unverified until export.
The existing `code/fem_quadmaps.npz` contains figure summaries and slices,
not the underlying per-node fields.

The source MRI is from the [IXI dataset](https://brain-development.org/ixi-dataset/),
licensed under [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/).
When released, the per-node export will be a separately licensed
[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) data file with
IXI attribution and a description of the processing that produced it. Its
license and attribution must accompany the data deposit. The repository's
CC BY 4.0 license remains unchanged.

## November 7 integration status

Ricardo's producer and committed outputs were imported locally from PR #2 at
`6ade413dd88b7d525466ff1eeaad003f449150cc`. His `code/fem_export_nodes.py`
reports a 45.7 MB FreeSurfer-only bundle under the schema documented in
[`data/fem_ixi002/README.md`](../data/fem_ixi002/README.md). The NPZ itself has
not been received, independently checked, or released here. Its reported
self-check covers 76 numerical values and eight rising-node counts.

That schema differs from the prototype below, whose reader requires both
`aseg` and `atlas` masks. The next step is to accept explicitly available
labels, adapt the keys without substituting an atlas mask, and validate the
received file and SHA-256. The exporter also imports the private producer at
module load; its check needs a standalone entry point before it can run with
NumPy alone. The atlas-label sensitivity, interface analysis, and FEM solve
remain outside the proposed export's reproduction scope. A separate data
record is planned; deposition remains held.

## Prototype schema and consumer

The producer's owner can create the bundle with:

```sh
TI_MODEL_ROOT=/path/to/temporal-interference-library \
  python code/export_fem_portable.py --output /path/to/ixi002_fields_v1.npz
python code/fem_portable.py /path/to/ixi002_fields_v1.npz --output /path/to/recomputed.json
```

The exporter requires the private library and original fields and labels. It
checks the independent long axis and centroid selection against the library for both
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
