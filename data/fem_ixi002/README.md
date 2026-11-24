# Per-node fields of the realistic-head comparison (IXI002)

**Local integration status (November 7, 2026):** the exporter and this schema
are included; the reported NPZ has not been received or independently validated
here. Data release remains pending. The current portable consumer uses a
different prototype schema; see `docs/fem_portable.md`.


`fem_ixi002_nodes.npz` holds the fields behind the realistic-head comparison of the
manuscript (`sec:fem-results`, `fig:fem`) at every grey- and white-matter node of the IXI002
head model: 446,877 node–compartment rows. It contains both montages' per-pair fields, each
montage's 1:1 projection direction n* (derived from its two fields), and the FreeSurfer
left-hippocampus ROI. These are the
inputs of the FreeSurfer-label conditions, GM-only ROI contrasts, ratio sweep,
radial-direction sensitivity and steering variants in `code/fem_quadmaps.json`, which can
therefore be recomputed with NumPy alone; the check below does so for 76 numbers and 8 counts.

## Licence and attribution

- **Licence:** CC BY-SA 4.0 (see `LICENSE`). This directory is licensed separately from the
  repository's code (CC BY 4.0).
- **Source:** IXI002 from the IXI dataset, https://brain-development.org/ixi-dataset/, made
  available under CC BY-SA 3.0. The IXI data are acknowledged as their source requests. CC BY-SA
  3.0 §4(b)(ii) permits distributing this adaptation under the later BY-SA 4.0.
- **Changes made to the source** (the T1-weighted image of IXI002):
  - segmented into six tissues and meshed (SimNIBS 3.2.3 headreco, CAT12 option; 3.64 × 10^6
    linear tetrahedra for the Violante montage);
  - two electrode pairs meshed per montage and each pair solved once at 1 A, with the
    conductivities, electrodes and solver of supplement §S3.3 (Neuroelectrics'
    temporal-interference library);
  - fields recovered at GM and WM nodes by superconvergent patch recovery, separately within
    each compartment;
  - the 1:1 envelope-maximizing direction n* computed from the fields;
  - left-hippocampus label from FreeSurfer 6.0.0 recon-all (aseg 17), run on the same image.

## Contents

| key | dtype, shape | meaning |
|---|---|---|
| `node` | int32 (446877,) | head-mesh node index; a node on the GM/WM interface has one row per compartment |
| `tissue` | uint8 (446877,) | 1 = white matter, 2 = grey matter (SimNIBS tags) |
| `xyz_mm` | float32 (446877, 3) | node position, subject T1 scanner space, mm |
| `E1_violante`, `E2_violante` | float32 (446877, 3) | field of pair 1 (anterior, e1–e2) and pair 2 (posterior, e3–e4) per ampere of that pair, V/m per A |
| `E1_yatsuda`, `E2_yatsuda` | float32 (446877, 3) | the same for the 10-10 rendering, FT7–F8 and TP7–P8 |
| `pairs_violante`, `pairs_yatsuda` | str (2, 2) | electrodes of pair 1 and pair 2 |
| `n_star_violante`, `n_star_yatsuda` | float64 (446877, 3) | **derived from that montage's `E1` and `E2`**: its 1:1 envelope-maximizing direction, computed per row from the two fields; unit vector, sign arbitrary |
| `roi_aseg_left_hippocampus` | bool (446877,) | the 1,568-row ROI: GM or WM inside aseg label 17 (nearest voxel) |
| `hippocampal_axis_anterior` | float64 (3,) | first principal axis of the ROI, anterior positive (focus displacement axis) |
| `head_axis_nz_minus_iz` | float64 (3,) | unit Nz − Iz from the subject's 10-10 position file |
| `metadata` | str () | JSON: key definitions, conventions, licence, attribution, producer commits, input hashes |

- **Fields:** stored at the precision of the library's field files (float32).
- **Direction:** n* adds no information beyond the two fields. It is computed per row from that
  montage's `E1` and `E2`, as stored here, in closed form: with a the larger field and b the
  other turned to an acute angle with it, n* is along b when |b| ≤ |a| cos θ, and otherwise in
  the plane of a and b, perpendicular to a − b. It is included, in float64, so that the
  published numbers are reproduced exactly without that step; the check below recomputes it.
- **Polarization:** ε_j = λ0 I_j (E_j · n), with λ0 = 0.5 mV per V/m.
- **Conditions:** 1:1 is 2 + 2 mA and 1:3 is 1 + 3 mA.
- **Maps and statistics:** as defined in `code/fem_quadmaps.py`.

## Not included

- **The Neuromorphometrics atlas label** (the label sensitivity) is left out. It is distributed
  under CC BY-NC ("provided by Neuromorphometrics, Inc. under academic subscription";
  `labels_Neuromorphometrics.xml` in SPM12 as bundled with SimNIBS 3.2.3). A NonCommercial
  adaptation cannot be released under BY-SA. The atlas-label numbers in `fem_quadmaps.json`
  therefore cannot be recomputed from this file.
- **The HippUnfold laminar direction** is left out; Sec. 4.4 does not use it.
- **The head mesh and the T1 image** are left out. The IXI image is available from the IXI
  dataset.

## Reproduction and check

`code/fem_export_nodes.py` writes this file from the TI library's stored IXI002 outputs, with
`TI_MODEL_ROOT` set as for `code/fem_quadmaps.py` (`FEM_EXPORT_DIR` writes it elsewhere, with
this README and `LICENSE` beside it). It then reads the file back with NumPy alone and
recomputes, from it, 76 aseg numbers of `fem_quadmaps.json`:

- the conditions at 1:1 and 1:3 (30: three statistics of four maps at two ratios, and six
  degree-matched contrasts);
- the GM-only ROI contrasts (the same 30, on the 1,174 GM nodes of the ROI);
- the radial-direction contrasts (8);
- the steering variants' ROI mean changes (8), with their rising-node counts (8, compared as
  integers).

It also recomputes n* from the two fields of each montage. It stops if any number differs by
more than 1e-12 relative, if any count differs, or if the recomputed n* departs from the
stored one by more than 1e-12 in 1 − |cos|. The input
hashes (BLAKE2b-512) are in `metadata`, with each repository's commit and whether its code was
clean when the file was written: no modified, staged or untracked file under the paths the
export imports from.
