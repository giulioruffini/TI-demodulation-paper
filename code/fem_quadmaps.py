"""Realistic-head comparison of envelope and quadratic maps (Sec. 4.5, Fig. 8): data.

One open IXI subject (IXI002), the hippocampal TI montage of Violante et al.
(2023), and a native FreeSurfer hippocampal label. The inputs were made by these
tools: head model, SimNIBS 3.2.3 (headreco); hippocampal label, FreeSurfer 6.0.0
(recon-all, aseg); atlas label, SimNIBS 3.2.3 (mni2subject); electrode meshing,
SimNIBS 3.2.3; the two per-pair field solves, Neuroelectrics' temporal-
interference library
(https://gitlab.neuroelectrics.com/ricardo.salvador/temporal-interference-library),
which stores them. This script only reads them; the settings are listed in
docs/fem_ixi002_violante.md.

Maps (Table 2), from the signed local polarizations of the two tones along one
direction n, eps_j = lambda_0 I_j (E_j . n), with E_j the pair-j field per
ampere:

* envelope excursion        M[A]       = 2 min(|eps_1|, |eps_2|)    (mV)
* quadratic beat excursion  M[A^2/2]   = 2 |eps_1 eps_2|            (mV^2)
* mean-square polarization  I          = (eps_1^2 + eps_2^2) / 2    (mV^2)
* isotropic beat excursion  2 |<eps_1 eps_2>_n| = (2/3) lambda_0^2 I_1 I_2 |E_1 . E_2|
  (the signed mixing term averaged over uniformly distributed orientations
  before its magnitude is taken; no direction enters)

Direction: n*(x), the direction that maximizes the envelope excursion at the
reference ratio 1:1 (the TImax direction of Grossman et al. 2017), held fixed
at each location for every ratio and for all three maps. The radial direction
from the brain centroid is a second fixed direction, kept as a sensitivity
check only.

Ratios: total 4 mA, posterior share s = I_2 / (I_1 + I_2) from 0.1 to 0.9;
1:1 is s = 0.5 (2 + 2 mA), 1:3 is s = 0.75 (1 mA anterior + 3 mA posterior).

Sensitivity grid for the 1:1 -> 1:3 focus shift, each montage along its own
1:1 direction: two montages (Violante; its 10-10 rendering FT7-F8 / TP7-P8,
the starting montage of Yatsuda et al. 2024) x two labels (FreeSurfer aseg;
Neuromorphometrics atlas) x two ROI tissue definitions (GM + WM; GM only) x
four focus fractions = 32 shifts per map.

Run with the TI library's interpreter (numpy, scipy, nibabel), with
TI_MODEL_ROOT pointing at a checkout that holds the IXI002 outputs:

    TI_MODEL_ROOT=/path/to/temporal-interference-library python code/fem_quadmaps.py

Writes fem_quadmaps.npz (figure data) and fem_quadmaps.json (every number
quoted in Secs. 3.3 and 4.5) next to this script.
"""
import json
import os
import sys
from pathlib import Path

import nibabel as nib
import numpy as np

HERE = Path(__file__).resolve().parent
TI = os.environ.get("TI_MODEL_ROOT")
if not TI or not (Path(TI) / "ti_model").is_dir():
    raise SystemExit("set TI_MODEL_ROOT to a checkout of temporal-interference-library "
                     "(https://gitlab.neuroelectrics.com/ricardo.salvador/"
                     "temporal-interference-library) holding output/ixi002/")
TI = Path(TI)
sys.path[:0] = [str(TI), str(TI / "tools")]

import quadmaps_maps as qm  # noqa: E402
import quadmaps_package as pk  # noqa: E402
from ixi_aseg_qc import resample_nn  # noqa: E402
from ti_model.physics.metrics import focus_centroid, ti_max, ti_max_direction  # noqa: E402
from ti_model.provenance import hash_file  # noqa: E402

MONTAGE = "violante"
MONTAGES = {"violante": "Violante et al. 2023: e1-e2 (anterior), e3-e4 (posterior)",
            "yatsuda": "10-10 rendering: FT7-F8 (anterior), TP7-P8 (posterior)"}
LAMBDA0 = 0.5                    # mV per V/m, the paper's static coupling (Sec. 5)
TOTAL_A = 4e-3                   # both conditions inject 4 mA in total
SHARES = np.round(np.arange(0.10, 0.9001, 0.025), 3)
REF_SHARE, STEER_SHARE = 0.5, 0.75
TOPS = (0.05, 0.10, 0.25, 0.50)
TOP = 0.10
MAPS = ("env", "quad", "msp", "iso")
DEGREE = {"env": 1, "quad": 2, "msp": 2, "iso": 2}
GM, WM = qm.GM, qm.WM


def currents(share):
    """(anterior, posterior) pair currents in A for a posterior share of the total."""
    return (1.0 - share) * TOTAL_A, share * TOTAL_A


def maps_at(share, f1, f2, dot12):
    """The four maps per row; f1, f2 in V/m per A along n*, dot12 = E1.E2 per A^2."""
    i1, i2 = currents(share)
    a, b = LAMBDA0 * i1 * f1, LAMBDA0 * i2 * f2
    return {"env": 2.0 * np.minimum(np.abs(a), np.abs(b)),
            "quad": 2.0 * np.abs(a * b),
            "msp": 0.5 * (a * a + b * b),
            "iso": (2.0 / 3.0) * LAMBDA0 ** 2 * i1 * i2 * np.abs(dot12)}


def stats(v, roi, ctx):
    """Target-to-cortex statistics: ROI mean and p95 against cortex p95 and p99."""
    s = {"roi_mean": float(v[roi].mean()), "roi_p95": float(np.percentile(v[roi], 95)),
         "cortex_p95": float(np.percentile(v[ctx], 95)),
         "cortex_p99": float(np.percentile(v[ctx], 99))}
    s["tc_p95"] = s["roi_p95"] / s["cortex_p95"]
    s["tc_mean"] = s["roi_mean"] / s["cortex_p95"]
    return s


def table(m, roi, ctx):
    """Stats of every map, with the degree-matched (square-root) companion of degree-2 maps."""
    out = {}
    for k, v in m.items():
        out[k] = stats(v, roi, ctx)
        if DEGREE[k] == 2:
            out[k]["degree_matched"] = stats(np.sqrt(v), roi, ctx)
    return out


def foci(m, xyz_roi, roi):
    return {k: {f"top{int(round(t * 100))}": focus_centroid(xyz_roi, v[roi], t) for t in TOPS}
            for k, v in m.items()}


def sweep(f1, f2, dot12, xyz, roi, ctx, axis):
    """Every statistic over the ratio sweep, and focus displacement relative to 1:1."""
    ref = foci(maps_at(REF_SHARE, f1, f2, dot12), xyz[roi], roi)
    out = {"anterior_weaker_fraction_roi": []}
    out |= {k: {"tc_p95": [], "tc_mean": [], "tc_p95_degree_matched": [],
               "tc_mean_degree_matched": [], "roi_mean": [], "cortex_p95": [],
               **{f"disp_axis_top{int(round(t * 100))}_mm": [] for t in TOPS},
               "disp_norm_top10_mm": []} for k in MAPS}
    for s in SHARES:
        i1, i2 = currents(s)
        out["anterior_weaker_fraction_roi"].append(
            float(np.mean(np.abs(i1 * f1[roi]) < np.abs(i2 * f2[roi]))))
        m = maps_at(s, f1, f2, dot12)
        tab = table(m, roi, ctx)
        fc = foci(m, xyz[roi], roi)
        for k in MAPS:
            o, t = out[k], tab[k]
            o["tc_p95"].append(t["tc_p95"])
            o["tc_mean"].append(t["tc_mean"])
            dm = t.get("degree_matched", t)
            o["tc_p95_degree_matched"].append(dm["tc_p95"])
            o["tc_mean_degree_matched"].append(dm["tc_mean"])
            o["roi_mean"].append(t["roi_mean"])
            o["cortex_p95"].append(t["cortex_p95"])
            for key, f in fc[k].items():
                d = f["centroid_mm"] - ref[k][key]["centroid_mm"]
                o[f"disp_axis_{key}_mm"].append(float(d @ axis))
                if key == "top10":
                    o["disp_norm_top10_mm"].append(float(np.linalg.norm(d)))
            if k in ("quad", "iso"):
                # uniform factor I1 I2 / (2 mA)^2: the same rows must be selected
                for key, f in fc[k].items():
                    if not np.array_equal(np.sort(f["selected"]), np.sort(ref[k][key]["selected"])):
                        raise AssertionError(f"{k} focus moved at share {s}")
    return out


def displacement(f1, f2, dot12, xyz, roi, axis, head):
    """1:1 -> 1:3 focus displacement, every top fraction."""
    a = foci(maps_at(REF_SHARE, f1, f2, dot12), xyz[roi], roi)
    b = foci(maps_at(STEER_SHARE, f1, f2, dot12), xyz[roi], roi)
    out = {}
    for k in MAPS:
        out[k] = {}
        for key in a[k]:
            d = b[k][key]["centroid_mm"] - a[k][key]["centroid_mm"]
            out[k][key] = {"anterior_along_hippocampus_mm": float(d @ axis),
                           "anterior_along_head_mm": float(d @ head),
                           "norm_mm": float(np.linalg.norm(d)),
                           "n_selected": a[k][key]["n_selected"]}
    return out, a, b


def held(montage):
    """A montage's fields and its 1:1 envelope-maximizing direction n*, per row."""
    f = np.load(qm.OUT / "fields" / f"{montage}.npz")
    E1, E2 = f["E1"].astype(float), f["E2"].astype(float)
    n_star = ti_max_direction(2e-3 * E1, 2e-3 * E2)
    return {"rows": f["rows"], "xyz": f["xyz"].astype(float), "E1": E1, "E2": E2,
            "n_star": n_star, "f1": np.einsum("ij,ij->i", E1, n_star),
            "f2": np.einsum("ij,ij->i", E2, n_star), "dot12": np.einsum("ij,ij->i", E1, E2)}


def sensitivity_grid(H):
    """1:1 -> 1:3 focus shift along the long axis for every montage, label, tissue and fraction."""
    combos = []
    for montage, h in H.items():
        xyz, tags = h["xyz"], h["rows"][:, 1]
        for lab in ("aseg", "atlas"):
            inside = qm.roi_mask(xyz, lab)
            for tissue, r in (("gm_wm", inside & np.isin(tags, (GM, WM))),
                              ("gm", inside & (tags == GM))):
                axis, head = qm.anterior_axis(xyz[r])
                d = displacement(h["f1"], h["f2"], h["dot12"], xyz, r, axis, head)[0]
                for k in MAPS:
                    for key, v in d[k].items():
                        combos.append({"montage": montage, "label": lab, "roi_tissue": tissue,
                                       "focus": key, "map": k, "n_roi_nodes": int(r.sum()),
                                       "anterior_along_hippocampus_mm":
                                           v["anterior_along_hippocampus_mm"],
                                       "norm_mm": v["norm_mm"]})
    summary = {}
    for k in MAPS:
        a = np.array([c["anterior_along_hippocampus_mm"] for c in combos if c["map"] == k])
        summary[k] = {"n": int(a.size), "n_anterior": int((a > 0).sum()),
                      "n_posterior": int((a < 0).sum()), "n_zero": int((a == 0).sum()),
                      "min_mm": float(a.min()), "max_mm": float(a.max()),
                      "by_montage": {m: [float(np.min(b)), float(np.max(b))] for m in H
                                     for b in [[c["anterior_along_hippocampus_mm"] for c in combos
                                                if c["map"] == k and c["montage"] == m]]}}
    return {"summary": summary, "combinations": combos}


def upper_tail(m, xyz, tags, roi, ctx, axis):
    """Which ROI nodes exceed the cortical p95, at 1:1: how many, how much WM, and where."""
    c = xyz[roi].mean(axis=0)
    lateral = np.array([np.sign(c[0]), 0.0, 0.0])
    out = {}
    for k, v in m.items():
        above = v[roi] > np.percentile(v[ctx], 95)
        d = xyz[roi][above].mean(axis=0) - c
        out[k] = {"roi_mean_over_cortex_p95": float(v[roi].mean() / np.percentile(v[ctx], 95)),
                  "fraction_roi_nodes_above_cortex_p95": float(above.mean()),
                  "wm_fraction_of_those": float(np.mean(tags[roi][above] == WM)),
                  "wm_fraction_roi": float(np.mean(tags[roi] == WM)),
                  "their_centroid_anterior_of_roi_centroid_mm": float(d @ axis),
                  "their_centroid_lateral_of_roi_centroid_mm": float(d @ lateral)}
    return out


def sagittal(rows, xyz, cols, fc11, fc13):
    """The maps on the T1 sagittal plane through the hippocampal centroid, anterior left.

    Same P1 interpolant and voxel centres as the TI library's NIfTI exports.
    """
    ref = nib.load(pk.T1)
    tissue = np.asarray(nib.load(pk.TISSUE).dataobj)
    hip = resample_nn(nib.load(qm.LABELS["aseg"][0]), ref) == 17
    shape = ref.shape[:3]
    cimg = nib.as_closest_canonical(nib.Nifti1Image(
        np.arange(np.prod(shape), dtype=np.int32).reshape(shape), ref.affine))
    cidx, caff = np.asarray(cimg.dataobj), cimg.affine
    c = np.rint(np.argwhere(hip.ravel()[cidx]).mean(axis=0)).astype(int)
    plane = cidx[c[0], :, :]
    mesh = pk.load_mesh(MONTAGE, {"rowmaps": {MONTAGE: {"rows": rows, "xyz": xyz}}})
    idx, vals, _, rep = pk.voxelise(mesh, rows, cols, ref, tissue, only=np.unique(plane))
    lut = np.full((np.prod(shape), cols.shape[1]), np.nan)
    lut[idx] = vals

    def img(a):
        return a[plane].T[:, ::-1]          # rows: z, origin lower; columns: anterior left

    brain = img(np.isin(tissue.ravel(), (GM, WM)))
    ii, jj = np.nonzero(brain)
    r0, c0 = max(ii.min() - 4, 0), max(jj.min() - 4, 0)
    crop = np.s_[r0:ii.max() + 5, c0:jj.max() + 5]
    ny = cidx.shape[1]

    def display(p):
        ijk = np.linalg.inv(caff) @ np.r_[p, 1.0]
        return np.array([(ny - 1) - ijk[1] - c0, ijk[2] - r0])

    out = {"t1": img(np.asarray(ref.dataobj, float).ravel())[crop].astype(np.float32),
           "hip": img(hip.ravel())[crop].astype(np.uint8),
           "brain": brain[crop].astype(np.uint8),
           "maps": np.stack([img(lut[:, j])[crop] for j in range(cols.shape[1])]).astype(np.float32),
           "foci_1to1": np.array([display(p) for p in fc11]),
           "foci_1to3": np.array([display(p) for p in fc13]),
           "voxel_mm": float(np.mean(np.sqrt((ref.affine[:3, :3] ** 2).sum(axis=0)))),
           "plane_x_mm": float((caff @ np.r_[c, 1.0])[0])}
    return out, rep


def main():
    print("direction fields n* at 1:1 ...", flush=True)
    H = {m: held(m) for m in MONTAGES}
    h = H[MONTAGE]
    rows, xyz, E1, E2, n_star = h["rows"], h["xyz"], h["E1"], h["E2"], h["n_star"]
    tags = rows[:, 1]
    brainrows = np.isin(tags, (GM, WM))
    labels = {lab: qm.roi_mask(xyz, lab) & brainrows for lab in ("aseg", "atlas")}
    roi = labels["aseg"]
    ctx = (tags == GM) & ~roi
    axis, head = qm.anterior_axis(xyz[roi])

    centre = xyz[brainrows].mean(axis=0)
    radial = (xyz - centre) / np.linalg.norm(xyz - centre, axis=1, keepdims=True)
    dot12 = h["dot12"]
    proj = {"n_star_1to1": (h["f1"], h["f2"]),
            "radial": (np.einsum("ij,ij->i", E1, radial), np.einsum("ij,ij->i", E2, radial))}
    f1, f2 = proj["n_star_1to1"]

    m11, m13 = maps_at(REF_SHARE, f1, f2, dot12), maps_at(STEER_SHARE, f1, f2, dot12)
    timax = LAMBDA0 * ti_max(2e-3 * E1, 2e-3 * E2)
    checks = {
        "env_at_1to1_equals_TImax_max_relerr": float(np.max(
            np.abs(m11["env"] - timax) / np.maximum(timax, 1e-300))),
        "quad_1to3_over_1to1_minus_0.75_max_abs": float(np.nanmax(np.abs(
            m13["quad"][brainrows] / m11["quad"][brainrows] - 0.75))),
        "iso_1to3_over_1to1_minus_0.75_max_abs": float(np.nanmax(np.abs(
            m13["iso"][brainrows] / m11["iso"][brainrows] - 0.75))),
        "env_dir_change_with_ratio": (
            "n* is fixed by construction; at 1:3 the envelope along n* is below that "
            "ratio's own maximum"),
        "env_1to3_along_nstar_over_own_TImax_1to3_roi_mean": float(np.mean(
            m13["env"][roi] / (LAMBDA0 * ti_max(1e-3 * E1[roi], 3e-3 * E2[roi])))),
    }

    print("conditions, sweep, robustness ...", flush=True)
    conditions = {"1:1": table(m11, roi, ctx), "1:3": table(m13, roi, ctx)}
    disp, fa, fb = displacement(f1, f2, dot12, xyz, roi, axis, head)
    sw = sweep(f1, f2, dot12, xyz, roi, ctx, axis)

    robust = {}
    for name, (g1, g2), lab in (("atlas_label", proj["n_star_1to1"], "atlas"),
                                ("radial_direction", proj["radial"], "aseg")):
        r = labels[lab]
        c = (tags == GM) & ~r
        ax_r, head_r = qm.anterior_axis(xyz[r])
        robust[name] = {
            "1:1": table(maps_at(REF_SHARE, g1, g2, dot12), r, c),
            "1:3": table(maps_at(STEER_SHARE, g1, g2, dot12), r, c),
            "displacement_1to3": displacement(g1, g2, dot12, xyz, r, ax_r, head_r)[0],
            "n_roi_rows": int(r.sum())}
    grid = sensitivity_grid(H)
    for k in ("env", "msp"):
        s = grid["summary"][k]
        if s["n_anterior"] not in (0, s["n"]):
            raise AssertionError(f"{k}: focus-shift direction not constant across the grid")
    if grid["summary"]["quad"]["n_zero"] != grid["summary"]["quad"]["n"]:
        raise AssertionError("quadratic excursion focus moved somewhere in the grid")

    print("sagittal plane ...", flush=True)
    order = ("env", "quad", "msp", "iso")
    cols = np.column_stack([m[k] for k in order for m in (m11, m13)])
    sl, rep = sagittal(rows, xyz.astype(np.float32), cols,
                       [fa[k]["top10"]["centroid_mm"] for k in order],
                       [fb[k]["top10"]["centroid_mm"] for k in order])

    gm = tags == GM
    res = {
        "what": "TN0484 Sec. 4.5 / Fig. 8: envelope and quadratic maps, IXI002, Violante montage",
        "definitions": {
            "env": "envelope excursion 2 min(|eps1|,|eps2|), mV",
            "quad": "quadratic beat excursion 2|eps1 eps2|, mV^2",
            "msp": "mean-square polarization (eps1^2 + eps2^2)/2, mV^2",
            "iso": "isotropic beat excursion (2/3) lambda0^2 I1 I2 |E1.E2|, mV^2",
            "eps_j": "lambda0 I_j (E_j . n), lambda0 = 0.5 mV per V/m, E_j per ampere",
            "direction": "n*: TImax direction at 1:1, held fixed at each location for every ratio",
            "share": "posterior pair current / total (4 mA); 1:1 = 0.5, 1:3 = 0.75",
            "roi": "GM+WM nodes inside the native FreeSurfer 6.0 aseg Left-Hippocampus (17)",
            "cortex": "GM nodes outside the ROI",
            "tc_p95": "ROI p95 / cortex p95", "tc_mean": "ROI mean / cortex p95",
            "degree_matched": "the same statistic on sqrt(map), for the degree-2 maps",
            "focus": "centroid of the top fraction of ROI nodes by the map's own value",
            "disp_axis": "focus shift along the ROI first principal axis, anterior positive, mm",
            "lateral": "away from the midline along the scanner x axis",
            "montages": MONTAGES,
            "sensitivity_grid": ("1:1 -> 1:3 focus shift, each montage along its own n*: "
                                 "2 montages x 2 labels x 2 ROI tissue definitions (GM+WM, GM) "
                                 "x 4 focus fractions")},
        "provenance": {"ti_library_url": ("https://gitlab.neuroelectrics.com/ricardo.salvador/"
                                          "temporal-interference-library"),
                       "inputs_sha512": {
                           **{f"fields_{m}": hash_file(qm.OUT / "fields" / f"{m}.npz")
                              for m in MONTAGES},
                           "aseg": hash_file(qm.LABELS["aseg"][0]),
                           "atlas_label": hash_file(qm.LABELS["atlas"][0])}},
        "n_rows": {"brain": int(brainrows.sum()), "roi_aseg": int(roi.sum()),
                   "roi_aseg_gm": int((labels["aseg"] & (tags == GM)).sum()),
                   "roi_atlas": int(labels["atlas"].sum()),
                   "roi_atlas_gm": int((labels["atlas"] & (tags == GM)).sum()),
                   "cortex_gm": int(ctx.sum())},
        "hippocampal_axis_anterior": axis.tolist(),
        "nstar_vs_radial_abs_cos_roi_median": float(np.median(np.abs(
            np.einsum("ij,ij->i", n_star[roi], radial[roi])))),
        "carrier_balance_roi_abs_f1_over_f2_p5_p50_p95": np.percentile(
            np.abs(f1[roi] / f2[roi]), [5, 50, 95]).tolist(),
        "conditions": conditions,
        "displacement_1to3_vs_1to1": disp,
        "sweep": {"share": SHARES.tolist(), **sw},
        "robustness": robust,
        "sensitivity_grid": grid,
        "upper_tail_1to1": upper_tail(m11, xyz, tags, roi, ctx, axis),
        "checks": checks,
        "sagittal": {"plane_x_mm": sl["plane_x_mm"], "voxelise": rep},
        "gm_p99_1to1": {k: float(np.percentile(m11[k][gm], 99)) for k in order}}
    (HERE / "fem_quadmaps.json").write_text(json.dumps(res, indent=1), encoding="utf-8")

    np.savez_compressed(
        HERE / "fem_quadmaps.npz", share=SHARES, map_order=np.array(order),
        **{f"{k}__{q}": np.asarray(sw[k][q]) for k in MAPS for q in sw[k]},
        anterior_weaker_fraction_roi=np.asarray(sw["anterior_weaker_fraction_roi"]),
        slice_t1=sl["t1"], slice_hip=sl["hip"], slice_brain=sl["brain"],
        slice_maps=sl["maps"], slice_foci_1to1=sl["foci_1to1"],
        slice_foci_1to3=sl["foci_1to3"], slice_voxel_mm=sl["voxel_mm"],
        gm_p99_1to1=np.array([res["gm_p99_1to1"][k] for k in order]))
    print(f"wrote {HERE / 'fem_quadmaps.json'} and fem_quadmaps.npz", flush=True)


if __name__ == "__main__":
    main()
