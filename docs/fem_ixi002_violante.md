# FEM contribution: IXI002, Violante montage (head-model Methods and Results, Fig. 9)

R. Salvador, Neuroelectrics. This file lists the settings behind the realistic-head
comparison, and the scripts and outputs that reproduce it.

## What is computed

From the two per-pair fields, three maps of Table 2 plus the isotropic beat map, all in
the paper's units (polarization `eps_j = lambda_0 I_j (E_j . n)`, `lambda_0 = 0.5` mV per
V/m, uniform):

| key in outputs | map | units |
|---|---|---|
| `env` | envelope excursion `2 min(|eps_1|, |eps_2|)` | mV |
| `quad` | quadratic excursion `2 |eps_1 eps_2|` | mV^2 |
| `msp` | mean-square polarization `(eps_1^2 + eps_2^2) / 2` | mV^2 |
| `iso` | isotropic beat excursion `(2/3) lambda_0^2 I_1 I_2 |E_1 . E_2|` | mV^2 |

No signed DC-source or mean-response map is computed (Sec. 3.3, last paragraph).

## Tools

| step | tool |
|---|---|
| segmentation and head-model generation | SimNIBS 3.2.3 (headreco, CAT12 option) |
| electrode placement in the mesh | SimNIBS 3.2.3 |
| hippocampal label | FreeSurfer 6.0.0 (recon-all, aseg) |
| atlas label (sensitivity) | SimNIBS 3.2.3 (mni2subject, nonlinear MNI transform) |
| FEM solves and field recovery | Neuroelectrics' temporal-interference library |
| hippocampal laminar coordinate (orientation comparison) | HippUnfold 1.5.2-pre.2 (DeKraker et al. 2022), Docker image; settings below |
| maps, statistics, Fig. 9 | `code/fem_quadmaps.py`, `code/make_fem_fig.py` (this repository) |
| field orientation and interface numbers | `code/fem_orientation_interface.py` (this repository) |

## Head model and solver

| item | setting |
|---|---|
| subject | IXI002, IXI dataset (https://brain-development.org/ixi-dataset/), T1, female, 35 y |
| tissues | six: scalp, skull, CSF, GM, WM, eyes |
| conductivities (S/m) | scalp 0.33, skull 0.008, CSF 1.79, GM 0.40, WM 0.15, eyes 0.33 (Salvador et al. 2025); gel 4.0, metal 10 |
| frequency | quasi-static, low-frequency conductivities, no dispersion correction |
| electrodes | 20 mm discs, 3 mm gel under 2 mm metal; each montage has its own mesh carrying only its own four electrodes |
| mesh (Violante) | 660,174 nodes, 3,637,257 linear tetrahedra |
| boundary conditions | Neumann current injection over each electrode's metal contact, weighted by nodal area; zero normal current elsewhere; one pinned node for the gauge |
| solver | P1 FEM, conjugate gradients with algebraic-multigrid preconditioning, relative residual 1e-8 |
| field recovery | superconvergent patch recovery (Zienkiewicz and Zhu 1992) at GM and WM nodes, per compartment: 446,877 node-compartment rows |
| solves | two per montage, one per pair, 1 A each; every current condition is a scaling of the two fields |

## Montages and currents

Primary: Violante et al. (2023), placed by their published recipe on the subject's
registered 10-10 positions.

| pair | electrodes | position |
|---|---|---|
| 1 (anterior) | e1 to e2 | e1: 25 mm from T9 toward FT9; e2: 10 mm from AF8 toward Fp2 |
| 2 (posterior) | e3 to e4 | e3: 25 mm from T9 toward TP9; e4: 10 mm from P8 toward PO8 |

Sensitivity: the 10-10 rendering of that montage, FT7-F8 (anterior) and TP7-P8
(posterior), the starting montage of Yatsuda et al. (2024).

Total 4 mA (peak pair currents). 1:1 = 2 + 2 mA; 1:3 = 1 mA anterior + 3 mA posterior.
Sweep (primary montage): posterior share `I_2 / (I_1 + I_2)` = 0.100 to 0.900 in steps
of 0.025.

The manuscript denotes the field per unit current by `F_j`, in (V/m)/mA, and
expresses pair currents in mA. The producer uses amperes throughout and denotes
its fields per unit current by `E_j`, in (V/m)/A. Thus the manuscript's `F_j`
equals the producer's `E_j / 1000`; multiplying by the corresponding current
gives the same applied field.

## Orientation

- **Primary, held fixed:** `n*(x)`, the direction that maximizes the envelope excursion at
  1:1 (closed form, Grossman et al. 2017), chosen once per node and used for every ratio
  and all three maps. At 1:1 the envelope map along `n*` equals its maximum over
  orientation (checked to 2e-15). In the sensitivity grid each montage uses its own `n*`.
- **Sensitivity:** the radial direction from the centroid of the brain nodes.
- **Isotropic:** the signed mixing term averaged over uniform orientations before the
  magnitude, `<eps_1 eps_2>_n = lambda_0^2 I_1 I_2 (E_1 . E_2) / 3`.
- **Laminar (orientation comparison only):** the normalized gradient of HippUnfold's
  inner-outer Laplace coordinate, below. No map or ratio of Fig. 9 uses it.

## HippUnfold run (laminar direction)

| item | setting |
|---|---|
| image | `khanlab/hippunfold@sha256:b14d6593839d09de56c21c585df2c02fe78e045d53f445f9d52727dd766a408a` |
| version | HippUnfold 1.5.2-pre.2 |
| arguments | `/bids /out participant --modality T1w --participant-label IXI002 --cores 8` |
| configuration | otherwise the image's defaults: both hemispheres, output density 0p5mm, native output space |
| input | the subject's 1 mm T1 that FreeSurfer was run on, with the same grid and affine as the head model's T1, so HippUnfold's T1w-space outputs are in the mesh coordinates |
| segmentation model | nnU-Net `trained_model.3d_fullres.Task101_hcp1200_T1w.nnUNetTrainerV2.model_best.tar`, downloaded at run time from the URL pinned in the image (Zenodo record 4508747); sha256 `d5080d795b506a635c7d52a271c6d8e43d9d05e44291187ad9b2ba45e75ae22d` |
| file used | `sub-IXI002_dir-IO_hemi-L_space-cropT1w_label-hipp_desc-laplace_coords.nii.gz` (left inner-outer Laplace coordinate, 0.2 mm grid in T1 world coordinates) |
| laminar direction | normalized gradient of that coordinate at the nearest voxel to each ROI node, no smoothing; defined at 934 of the 1,568 ROI nodes; interior nodes (voxel and its six face neighbours inside the Laplace domain): 565 |

The run, with `<bids>` a BIDS dataset holding the T1 as `sub-IXI002/anat/sub-IXI002_T1w.nii.gz`:

    docker run -e HIPPUNFOLD_CACHE_DIR=/cache \
      -v <bids>:/bids:ro -v <out>:/out -v <cache>:/cache \
      khanlab/hippunfold@sha256:b14d6593839d09de56c21c585df2c02fe78e045d53f445f9d52727dd766a408a \
      /bids /out participant --modality T1w --participant-label IXI002 --cores 8

## Regions

| region | definition | nodes |
|---|---|---|
| target (ROI) | GM + WM nodes inside FreeSurfer aseg label 17 (Left-Hippocampus, 3903 mm^3), run on the same T1 | 1,568 |
| target, GM only (sensitivity) | GM nodes inside the same label | 1,174 |
| cortex | GM nodes outside the ROI | 273,544 |
| atlas label (sensitivity) | Neuromorphometrics label 48, warped into the subject (Dice 0.72 with aseg, centroids 1.6 mm apart) | 1,345 (GM only: 1,013) |

Mesh-image alignment with the aseg was checked by tag volume ratio, tag centroid hit
(worst, CSF 0.852 against 0.85) and WM centroid inside the aseg brain (0.998). All passed.

The output key `cortex` includes deep gray matter outside the ROI. The manuscript
therefore calls it the reference region and reports target-to-reference ratios;
it is not a cortex-only mask. The output keys remain unchanged.

## Statistics

- target-to-cortex ratio `tc_p95` = ROI p95 / cortex p95; `tc_mean` = ROI mean / cortex p95;
- degree-matched: the same statistic on the square root of each second-order map;
- focus: centroid of the top 10% of ROI nodes by the map's own value (5, 25, 50% as
  sensitivity); displacement from 1:1 along the ROI's first principal axis, anterior
  positive;
- sensitivity grid: the 1:1 to 1:3 displacement for 2 montages x 2 labels x 2 ROI tissue
  definitions x 4 focus fractions = 32 per map (`sensitivity_grid` in the JSON);
- GM-only ROI contrasts: the conditions table at 1:1 and 1:3 with the ROI restricted to its
  GM nodes, against the unchanged GM reference (`conditions_gm_only_roi`);
- steering, 1:1 to 1:3: for the 8 ROI variants of the grid (the focus fraction enters neither
  statistic), each map's ROI-mean change and the share of ROI and reference nodes where it
  rises, per node, along each montage's own `n*` and radially; the envelope rises where
  `|a| > 2|b|` and the mean square where `|a/b| < sqrt(5/3)`, with `a`, `b` the anterior and
  posterior polarizations at 1:1, checked node by node (`steering_1to3`);
- upper tail at 1:1: the ROI nodes above the cortical p95, their white-matter fraction and
  their centroid relative to the ROI centroid (`upper_tail_1to1` in the JSON).

## Interfaces (`fem_orientation_interface.py`)

- interface: a face shared by two tetrahedra of different tissue tags (CSF/GM, GM/WM; this
  segmentation has no WM/CSF faces); conductivity ratio `r` from the table above
  (CSF/GM 4.475, GM/WM 2.667);
- near an interface: Euclidean distance from a node to the nearest interface vertex or face
  centroid of at most 2 mm;
- map jump across an interface: at each interface node, the mean element field over the
  adjacent tetrahedra on each side (from the node potentials), with the maps along the GM row's
  `n*`; beside it the jump-condition prediction `E_low = E_high + (r - 1)(E_high . nu) nu` with the
  area-weighted node normal `nu`, and the own-maximum maps (closed-form maxima over orientation)
  of the same side fields, whose continuum ratios obey `[1, r]` (`[1, r^2]` for second-order maps);
  the nodes outside the bound are counted, with the minimum and maximum, and the E1 normal jump
  and tangential mismatch at those nodes are given beside all nodes' (`outside_bound_E1`);
- field components: per face, each side's element field split on the face's own normal; the
  normal jump (low over high side) over the faces whose high-side normal component is at least
  a fraction `f` of `|E|`, `f` = 0, 0.05, 0.1, 0.2, 0.3, 0.5; the same per node.

## Scripts and outputs

| step | script | needs | output |
|---|---|---|---|
| maps, statistics, sweep, sensitivity grid, GM-only contrasts, steering variants, sagittal plane | `code/fem_quadmaps.py` | the temporal-interference library with its stored IXI002 fields and labels, and the subject's head-model T1 and 10-10 position file (numpy, scipy, nibabel) | `code/fem_quadmaps.json`, `code/fem_quadmaps.npz` |
| Fig. 9 | `code/make_fem_fig.py` | the two files above; this repository's `requirements.txt` | `figures/fig_fem.pdf`, `.png` |
| field orientation, laminar comparison, cap overlap, interfaces and field components | `code/fem_orientation_interface.py` | the library with its stored IXI002 fields, node potentials, Violante head mesh, aseg label, electrode positions and HippUnfold laminar coordinate, and the subject's 10-10 position file (numpy, scipy, nibabel) | `code/fem_orientation_interface.json` |
| per-node export (CC BY-SA 4.0 data, see `data/fem_ixi002/README.md`) and its NumPy-only check against `fem_quadmaps.json` | `code/fem_export_nodes.py` | as for `fem_quadmaps.py`, and `code/fem_quadmaps.json` | `data/fem_ixi002/fem_ixi002_nodes.npz` (or `FEM_EXPORT_DIR`) |

`fem_quadmaps.json` holds every map, ratio and focus number quoted in Secs. 3.3 and 4.5,
Table 3 and the supplement's steering section, with the definitions, the checks, the sensitivities, and the BLAKE2b-512 hashes of the
input fields and labels (under the key `inputs_sha512`, a misnomer; Python's
`hashlib.blake2b` reproduces them). `fem_orientation_interface.json` holds the
field-orientation and interface numbers, with the BLAKE2b-512 hashes of its inputs
(`inputs_blake2b512`); its field and label hashes equal those in `fem_quadmaps.json`.
The 10-10 position file orients the hippocampal long axis anteriorly (Nz-Iz); every
angle in `fem_orientation_interface.json` is between undirected axes and does not depend
on that sign. `make_fem_fig.py` needs only the two output files, so Fig. 9 can be
redrawn without the head model.

The temporal-interference library is Neuroelectrics' FEM and TI-metrics code:
https://gitlab.neuroelectrics.com/ricardo.salvador/temporal-interference-library
(not public). To recompute the numbers, check it out with its stored IXI002 outputs and run

    TI_MODEL_ROOT=/path/to/temporal-interference-library python code/fem_quadmaps.py
    python code/make_fem_fig.py
    TI_MODEL_ROOT=/path/to/temporal-interference-library python code/fem_orientation_interface.py
    TI_MODEL_ROOT=/path/to/temporal-interference-library python code/fem_export_nodes.py

The per-node export is licensed CC BY-SA 4.0, separately from the code (CC BY 4.0), as an
adaptation of IXI002 (CC BY-SA 3.0). It leaves out the warped Neuromorphometrics atlas label,
which is CC BY-NC; `data/fem_ixi002/README.md` gives the attribution, the changes and the
contents.

## Local import and verification scope (November 7, 2026)

The producer scripts and JSON outputs were imported from Ricardo's PR #2 at
`6ade413dd88b7d525466ff1eeaad003f449150cc`. Every old scalar/list leaf of
`fem_quadmaps.json` is preserved; the new manuscript values were checked against
the imported output. The private FEM solve and field-to-map producers were not
rerun here. The exact private-library revision for these recorded outputs remains
to be supplied; the exporter records its producing revision when run.

The manuscript distinguishes the exact continuum map bounds from their discrete
comparison, and the recovered nodal direction from the side-averaged element
fields. A generic fixed direction has neither conductivity-ratio bound, but an
exact low-side envelope maximizer retains the floor and an exact high-side
maximizer retains the ceiling. Normal-jump tail statistics are associations,
not a demonstration of the cause of each violation.

The FreeSurfer-only NPZ is reported by its producer, not yet received or validated
here. Its proposed schema, private import dependency, and consumer adaptation
are recorded in `docs/fem_portable.md`. Remote merging and release remain held.
