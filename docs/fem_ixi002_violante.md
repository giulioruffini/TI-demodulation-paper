# FEM contribution: IXI002, Violante montage (Sec. 3.3, Sec. 4.5, Fig. 8)

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
| maps, statistics, Fig. 8 | `code/fem_quadmaps.py`, `code/make_fem_fig.py` (this repository) |

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

## Orientation

- **Primary, held fixed:** `n*(x)`, the direction that maximizes the envelope excursion at
  1:1 (closed form, Grossman et al. 2017), chosen once per node and used for every ratio
  and all three maps. At 1:1 the envelope map along `n*` equals its maximum over
  orientation (checked to 2e-15). In the sensitivity grid each montage uses its own `n*`.
- **Sensitivity:** the radial direction from the centroid of the brain nodes.
- **Isotropic:** the signed mixing term averaged over uniform orientations before the
  magnitude, `<eps_1 eps_2>_n = lambda_0^2 I_1 I_2 (E_1 . E_2) / 3`.

## Regions

| region | definition | nodes |
|---|---|---|
| target (ROI) | GM + WM nodes inside FreeSurfer aseg label 17 (Left-Hippocampus, 3903 mm^3), run on the same T1 | 1,568 |
| target, GM only (sensitivity) | GM nodes inside the same label | 1,174 |
| cortex | GM nodes outside the ROI | 273,544 |
| atlas label (sensitivity) | Neuromorphometrics label 48, warped into the subject (Dice 0.72 with aseg, centroids 1.6 mm apart) | 1,345 (GM only: 1,013) |

Mesh-image alignment with the aseg was checked by tag volume ratio, tag centroid hit
(worst, CSF 0.852 against 0.85) and WM centroid inside the aseg brain (0.998). All passed.

## Statistics

- target-to-cortex ratio `tc_p95` = ROI p95 / cortex p95; `tc_mean` = ROI mean / cortex p95;
- degree-matched: the same statistic on the square root of each second-order map;
- focus: centroid of the top 10% of ROI nodes by the map's own value (5, 25, 50% as
  sensitivity); displacement from 1:1 along the ROI's first principal axis, anterior
  positive;
- sensitivity grid: the 1:1 to 1:3 displacement for 2 montages x 2 labels x 2 ROI tissue
  definitions x 4 focus fractions = 32 per map (`sensitivity_grid` in the JSON);
- upper tail at 1:1: the ROI nodes above the cortical p95, their white-matter fraction and
  their centroid relative to the ROI centroid (`upper_tail_1to1` in the JSON).

## Scripts and outputs

| step | script | needs | output |
|---|---|---|---|
| maps, statistics, sweep, sensitivity grid, sagittal plane | `code/fem_quadmaps.py` | the temporal-interference library with its stored IXI002 fields and labels (numpy, scipy, nibabel) | `code/fem_quadmaps.json`, `code/fem_quadmaps.npz` |
| Fig. 8 | `code/make_fem_fig.py` | the two files above; this repository's `requirements.txt` | `figures/fig_fem.pdf`, `.png` |

`fem_quadmaps.json` holds every number quoted in Secs. 3.3 and 4.5, with the definitions,
the checks, the sensitivities, and the SHA-512 hashes of the input fields and labels.
`make_fem_fig.py` needs only the two output files, so Fig. 8 can be redrawn without the
head model.

The temporal-interference library is Neuroelectrics' FEM and TI-metrics code:
https://gitlab.neuroelectrics.com/ricardo.salvador/temporal-interference-library
(not public). To recompute the numbers, check it out with its stored IXI002 outputs and run

    TI_MODEL_ROOT=/path/to/temporal-interference-library python code/fem_quadmaps.py
    python code/make_fem_fig.py
