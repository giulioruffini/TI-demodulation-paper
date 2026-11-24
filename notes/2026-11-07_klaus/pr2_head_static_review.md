# PR #2 head 6ade413 against c386e54: scripts, doc, provenance

Static review on 7 November 2026 for Kaiti's 13:35 handoff, from the fetched ref
`overleaf/ricardo/fem` (6ade413). Read-only; nothing run. The three fetched files in
`build/review_ricardo_2026-11-07/` are byte-identical to the ref's blobs. The NPZ is still
unreceived. Companion: `ricardo_2026-11-06_interface_export_check.md` (same folder), whose
"five of the six tails" is corrected there to four: the below-floor E1 normal-jump medians
exceed 1 for quad and msp at both interfaces (1.11, 1.02, 1.14, 1.12) and not for the
envelope (0.81, 0.86).

## New output definitions

`code/fem_quadmaps.py` (+86 −2 against c386e54; additive). New `steering_variants(H)`: for
each montage, label and ROI tissue (8 variants), along the montage's own n* and radially,
each map's ROI-mean change 1:1 → 1:3, the count and share of ROI nodes where it rises, and
the share of reference nodes (GM outside the ROI) where it rises, with the ROI's |f1/f2|
percentiles; a summary over variants per direction and map. It asserts, node by node on
ROI and reference nodes, that the envelope rises iff |a| > 2|b| and the mean square iff
|a/b| < √(5/3). New `conditions_gm`: the conditions table on the ROI's GM nodes, with an
assertion that the GM reference is unchanged. Both get `definitions` strings and the keys
`conditions_gm_only_roi` and `steering_1to3`.

`code/fem_orientation_interface.py` (335a65f → 6ade413). `tails()` adds `n`, `n_below_1`,
`n_above_bound`, `min` and keeps its five old keys. `jump()` adds `outside_bound_E1` per map:
for the nodes above the bound, below 1, and all, the count, the median of E1's realized
normal jump (low-side over high-side normal component on the area-weighted node normal),
the median tangential mismatch of E1's side-mean fields, and that median's percentile
among all interface nodes. The selection uses the own-maximum ratio with the nodes of zero
high-side maximum set to 1 (neither tail); the counts equal the tails' `n`, so no node was
dropped. The doc's new "Interfaces" section describes all of this; its laminar section
records the HippUnfold image digest, arguments, model file and digest.

`code/fem_export_nodes.py`: new; reviewed in the companion note.

## Old outputs preserved

Both JSON files: no existing leaf changed or removed between 335a65f and 6ade413, and the
335a65f `fem_quadmaps.json` equals the local baseline byte for byte. The script diffs are
additive. `code/fem_quadmaps.npz` and `code/make_fem_fig.py` are not in the PR, so the
figure data and Fig. 8 are untouched.

## Private dependencies

All three scripts exit at import unless `TI_MODEL_ROOT` holds the library. `fem_quadmaps.py`
imports `quadmaps_maps`, `quadmaps_package`, `ixi_aseg_qc`, `ti_model.physics.metrics`,
`ti_model.provenance`, and reads the two montages' field files, the aseg and atlas labels,
the head-model T1 and the 10-10 position file. `fem_orientation_interface.py` adds
`quadmaps_carrier_geometry`, `quadmaps_solve`, `ti_model.fem.recover`, `ti_model.io.mesh_io`,
`ti_model.spaces`, `ti_model.targets.directions`, and reads the Violante mesh, the node
potentials, the montage position files and the HippUnfold Laplace coordinate.
`fem_export_nodes.py` imports `fem_quadmaps` at module level, so its NumPy-only `check()`
cannot be reached without the library; a third party holding the NPZ and the JSON cannot run
the committed check (the fix is the pattern of `export_fem_portable.py`: import inside
`export()`, and a check-only entry). Not blocking for draft28; blocking only for any sentence
that says a reader can run the check.

## Hash labels

`fem_quadmaps.json` keeps `inputs_sha512`; the doc at head (lines 167–169) records it as a
misnomer for BLAKE2b-512 and says `hashlib.blake2b` reproduces the digests, as Kaiti's
30 October assessment already noted. `fem_orientation_interface.json` and the export README
use `inputs_blake2b512`; the field and aseg digests are identical across the two files. The
key should stay as it is unless `export_fem_portable.py` (line 54, which reads
`inputs_sha512`) changes with it. My earlier report's flag (2) is withdrawn: documented, not
wrong.

## Provenance limitations

1. The export omits the Neuromorphometrics atlas label (CC BY-NC per Ricardo's reading of
   the SPM12 file; not verified here). Unreproducible from the record: the atlas half of
   `sensitivity_grid` and of `steering_1to3` (including the +29.7% largest mean-square rise),
   `robustness/atlas_label`, `n_rows/roi_atlas*`. The FreeSurfer-label numbers are complete.
2. `fem_orientation_interface.json` needs the mesh, the node potentials and the laminar
   coordinate, none of which is exported; its numbers are reproducible only with the library.
3. The sagittal slice (`sagittal`) needs the mesh for voxelization.
4. The NPZ is not committed; its size, dtypes, metadata (hashes, commits, `clean` flags) and
   the pass of the check are Ricardo's report until the file arrives.
5. The `clean` flags cover the `code` path of this repository and `tools`, `ti_model` of the
   library; the stored fields under `output/ixi002/` are data, covered by the hashes.

## The availability paragraph (lines 1817–1836 of the baseline)

What no longer holds: "an exporter with consistency checks are included; the per-node
export and its comparison with the published statistics remain pending" names our
`export_fem_portable.py` (schema `tn0484-fields-v1`, never run on the fields), while PR #2
adds Ricardo's `fem_export_nodes.py` with its own schema and a read-back check already run
by him. Two exporters and two consumers with different schemas should not both appear. The
paragraph also says nothing about what the record omits.

Exact wording, replacing from "The FEM producer" to "\texttt{docs/fem\_portable.md}.":

> The FEM producer \texttt{code/fem\_quadmaps.py} computes the reported maps and statistics
> from the stored fields, and \texttt{code/fem\_orientation\_interface.py} the orientation
> and interface numbers; the summary arrays and \texttt{code/make\_fem\_fig.py} reproduce
> Fig.~\ref{fig:fem} without the head model. Recomputing these from the underlying fields
> requires Neuroelectrics' nonpublic TI library, the IXI002 head mesh, and the original
> fields and labels. A per-node export, \texttt{code/fem\_export\_nodes.py}, writes both
> montages' fields at every gray- and white-matter node, each montage's envelope-maximizing
> direction, and the FreeSurfer hippocampal label as a separately licensed data file
> (CC BY-SA 4.0, with IXI attribution). Read with NumPy alone, that file reproduces the
> FreeSurfer-label statistics of Table~\ref{tab:fem} [check label], the ratio sweep and the
> steering variants; the exporter's read-back check compares 76 of these numbers and 8 node
> counts with the stored values. The file omits the Neuromorphometrics atlas label
> (CC BY-NC), so the atlas-label sensitivity numbers, and the interface numbers, which need
> the mesh and node potentials, are reproducible only with the library. The data file has
> not yet been deposited. Input hashes (BLAKE2b-512), settings and export instructions are
> recorded in \texttt{docs/fem\_ixi002\_violante.md}, \texttt{code/fem\_quadmaps.json} and
> \texttt{code/fem\_orientation\_interface.json}.

Notes on it: "has not yet been deposited" stays neutral between Zenodo and in-repo until
Giulio decides; once deposited, replace it with the record's DOI. Drop the
`code/fem\_portable.py` and `docs/fem\_portable.md` mentions unless the consumer is adapted
to Ricardo's schema and run on the file, in which case one sentence can name it as the
independent consumer. "Read with NumPy alone … reproduces" is Ricardo's claim about his run;
it is a fair statement of what the committed check does, with the import barrier above
meaning that a reader must copy the check out of the script to rerun it.
