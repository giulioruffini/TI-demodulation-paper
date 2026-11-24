"""Per-node export of the realistic-head fields, and a NumPy-only check of it.

The fields are those behind the realistic-head comparison (sec:fem-results, fig:fem).
Writes data/fem_ixi002/fem_ixi002_nodes.npz: every grey- and white-matter node of the IXI002
head model (446,877 node-compartment rows), with both montages' per-pair fields, each montage's
1:1 direction n* (derived from its two fields), and the FreeSurfer aseg left-hippocampus ROI. The data file is licensed
CC BY-SA 4.0, separately from this code (CC BY 4.0), because it is an adaptation of IXI002,
which the IXI dataset distributes under CC BY-SA 3.0; data/fem_ixi002/README.md carries the
attribution and the changes.

Not included: the Neuromorphometrics atlas label (the label sensitivity). The atlas is
distributed under CC BY-NC (labels_Neuromorphometrics.xml, SPM12 as bundled with SimNIBS
3.2.3), and a NonCommercial adaptation cannot be released under BY-SA. The atlas-label
numbers in fem_quadmaps.json therefore cannot be recomputed from this file.

Run like fem_quadmaps.py, with TI_MODEL_ROOT set; FEM_EXPORT_DIR writes the file elsewhere,
with LICENSE and README.md copied beside it. After writing, the file is read back with NumPy
alone and aseg numbers of fem_quadmaps.json (conditions, GM-only conditions, radial robustness,
steering variants) are recomputed from it and compared.

The metadata records each repository's commit and whether the code it ran was clean. Clean
means no modified, staged or untracked file under the paths the export imports from: an
untracked script leaves `git status` of the tracked tree clean, so the commit alone would not
say that the code that ran is the code at that commit.
"""
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
REPO = Path(os.environ.get("TN0484_REPO", HERE.parent))
sys.path.insert(0, str(REPO / "code"))
import fem_quadmaps as fq  # noqa: E402

OUT = Path(os.environ.get("FEM_EXPORT_DIR", REPO / "data" / "fem_ixi002"))
NPZ = OUT / "fem_ixi002_nodes.npz"
LICENSE = "CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)"
ATTRIBUTION = ("Derived from IXI002 of the IXI dataset (https://brain-development.org/ixi-dataset/), "
               "CC BY-SA 3.0. Changes: head model, two-pair field solves and node-wise field "
               "recovery, n*, and the FreeSurfer 6.0.0 aseg left-hippocampus ROI; see README.md.")


def git_state(path, *pathspecs):
    """HEAD, and whether `pathspecs` hold no modified, staged or untracked file."""
    git = ["git", "-C", str(path)]
    try:
        commit = subprocess.check_output([*git, "rev-parse", "HEAD"], text=True).strip()
        dirty = subprocess.check_output([*git, "status", "--porcelain", "--untracked-files=all",
                                         "--", *pathspecs], text=True).splitlines()
    except (OSError, subprocess.CalledProcessError):
        return {"commit": "unknown", "clean": None, "not_committed": []}
    return {"commit": commit, "clean": not dirty, "not_committed": [d[3:] for d in dirty]}


def export():
    H = {m: fq.held(m) for m in fq.MONTAGES}
    raw = {m: np.load(fq.qm.OUT / "fields" / f"{m}.npz") for m in fq.MONTAGES}
    rows, xyz = raw["violante"]["rows"], raw["violante"]["xyz"]
    for m, f in raw.items():
        if not (np.array_equal(f["rows"], rows) and np.array_equal(f["xyz"], xyz)):
            raise AssertionError(f"{m}: rows or coordinates differ from violante's")
    tags = rows[:, 1]
    roi = fq.qm.roi_mask(H["violante"]["xyz"], "aseg") & np.isin(tags, (fq.GM, fq.WM))
    axis, head = fq.qm.anterior_axis(H["violante"]["xyz"][roi])
    meta = {
        "what": ("IXI002 head model, Violante et al. 2023 hippocampal TI montage and its 10-10 "
                 "rendering (Yatsuda et al. 2024 starting montage): per-pair fields at every GM "
                 "and WM node, per ampere"),
        "license": LICENSE, "attribution": ATTRIBUTION,
        "keys": {
            "node": "head-mesh node index (a node on the GM/WM interface has one row per compartment)",
            "tissue": "1 = white matter, 2 = grey matter (SimNIBS tags)",
            "xyz_mm": "node position, subject T1 scanner space, mm",
            "E1_<montage>, E2_<montage>": ("field of pair 1 (anterior) and pair 2 (posterior) per "
                                           "ampere of that pair, V/m per A, recovered within the "
                                           "row's compartment (superconvergent patch recovery)"),
            "pairs_<montage>": "electrodes of pair 1 and pair 2",
            "n_star_<montage>": ("derived from E1_<montage> and E2_<montage>, not an independent "
                                 "input: the 1:1 envelope-maximizing direction (TImax direction), "
                                 "computed per row from those two fields in closed form; unit "
                                 "vector, sign arbitrary; held fixed for every ratio; stored in "
                                 "float64 so the published numbers reproduce exactly"),
            "roi_aseg_left_hippocampus": ("row inside FreeSurfer 6.0.0 aseg label 17 (nearest "
                                          "voxel) and GM or WM: the 1,568-node ROI"),
            "hippocampal_axis_anterior": "first principal axis of the ROI, anterior positive",
            "head_axis_nz_minus_iz": "unit Nz - Iz, from the subject's 10-10 position file"},
        "units_and_conventions": ("eps_j = lambda0 I_j (E_j . n), lambda0 = 0.5 mV per V/m; "
                                  "1:1 = 2 + 2 mA, 1:3 = 1 + 3 mA; maps as in fem_quadmaps.py"),
        "not_included": ("the Neuromorphometrics atlas label (CC BY-NC, incompatible with BY-SA); "
                         "the HippUnfold laminar direction; the head mesh and the T1 image"),
        "producer": {"script": "code/fem_export_nodes.py",
                     "tn0484_repo": git_state(REPO, "code"),
                     "ti_library": git_state(fq.TI, "tools", "ti_model"),
                     "inputs_blake2b512": {
                         **{f"fields_{m}": fq.hash_file(fq.qm.OUT / "fields" / f"{m}.npz")
                            for m in fq.MONTAGES},
                         "aseg": fq.hash_file(fq.qm.LABELS["aseg"][0])}}}
    OUT.mkdir(parents=True, exist_ok=True)
    np.savez_compressed(
        NPZ, node=rows[:, 0].astype(np.int32), tissue=tags.astype(np.uint8), xyz_mm=xyz,
        **{f"{e}_{m}": raw[m][e] for m in fq.MONTAGES for e in ("E1", "E2")},
        **{f"pairs_{m}": raw[m]["pairs"] for m in fq.MONTAGES},
        **{f"n_star_{m}": H[m]["n_star"] for m in fq.MONTAGES},
        roi_aseg_left_hippocampus=roi, hippocampal_axis_anterior=axis, head_axis_nz_minus_iz=head,
        metadata=np.array(json.dumps(meta, indent=1)))
    docs = REPO / "data" / "fem_ixi002"
    if OUT.resolve() != docs.resolve():
        for name in ("LICENSE", "README.md"):
            shutil.copyfile(docs / name, OUT / name)
    return meta


# ---- NumPy-only consumer: nothing below imports the TI library or fem_quadmaps

def np_maps(share, f1, f2, dot12):
    i1, i2 = (1.0 - share) * 4e-3, share * 4e-3
    a, b = 0.5 * i1 * f1, 0.5 * i2 * f2
    return {"env": 2.0 * np.minimum(np.abs(a), np.abs(b)), "quad": 2.0 * np.abs(a * b),
            "msp": 0.5 * (a * a + b * b), "iso": (2.0 / 3.0) * 0.25 * i1 * i2 * np.abs(dot12)}


def np_n_star(E1, E2):
    """The 1:1 envelope-maximizing direction from the two fields alone, in closed form.

    With a the larger field and b the other turned to an acute angle with it: n* is along b
    when b's projection does not exceed a's (|b| <= |a| cos), and otherwise in the plane of
    a and b, perpendicular to a - b. Sign arbitrary.
    """
    swap = np.linalg.norm(E2, axis=1) > np.linalg.norm(E1, axis=1)
    a, b = np.where(swap[:, None], E2, E1), np.where(swap[:, None], E1, E2)
    b = np.where((np.einsum("ij,ij->i", a, b) < 0.0)[:, None], -b, b)
    along_b = np.einsum("ij,ij->i", b, b) <= np.einsum("ij,ij->i", a, b)   # |b| <= |a| cos
    perp = np.cross(np.cross(a, b), a - b)
    n = np.where(along_b[:, None], b, perp)
    return n / np.linalg.norm(n, axis=1, keepdims=True)


def np_stats(v, roi, ctx):
    p95c = np.percentile(v[ctx], 95)
    return {"tc_p95": np.percentile(v[roi], 95) / p95c, "tc_mean": v[roi].mean() / p95c,
            "roi_mean": v[roi].mean()}


def check():
    d = np.load(NPZ)
    ref = json.loads((REPO / "code" / "fem_quadmaps.json").read_text(encoding="utf-8"))
    tags, xyz = d["tissue"], d["xyz_mm"].astype(float)
    roi = d["roi_aseg_left_hippocampus"]
    gm = tags == 2
    worst, n, n_counts = 0.0, 0, 0
    # n* is derived: recompute it from each montage's two fields and compare, up to sign
    n_star_dev = max(float((1.0 - np.abs(np.einsum(
        "ij,ij->i", np_n_star(d[f"E1_{m}"].astype(float), d[f"E2_{m}"].astype(float)),
        d[f"n_star_{m}"]))).max()) for m in ("violante", "yatsuda"))
    if n_star_dev > 1e-12:
        raise AssertionError(f"stored n* is not the closed form of the two fields ({n_star_dev:.1e})")

    def cmp(got, want):
        nonlocal worst, n
        n += 1
        worst = max(worst, abs(got / want - 1.0))

    def proj(m, n_dir):
        E1, E2 = d[f"E1_{m}"].astype(float), d[f"E2_{m}"].astype(float)
        return (np.einsum("ij,ij->i", E1, n_dir), np.einsum("ij,ij->i", E2, n_dir),
                np.einsum("ij,ij->i", E1, E2))

    f1, f2, dot12 = proj("violante", d["n_star_violante"])
    for key, r in (("conditions", roi), ("conditions_gm_only_roi", roi & gm)):
        for cond, share in (("1:1", 0.5), ("1:3", 0.75)):
            mp = np_maps(share, f1, f2, dot12)
            for k, v in mp.items():
                s = np_stats(v, r, gm & ~roi)
                for stat in ("tc_p95", "tc_mean", "roi_mean"):
                    cmp(s[stat], ref[key][cond][k][stat])
                if k != "env":
                    s = np_stats(np.sqrt(v), r, gm & ~roi)
                    cmp(s["tc_p95"], ref[key][cond][k]["degree_matched"]["tc_p95"])
    centre = xyz[np.isin(tags, (1, 2))].mean(axis=0)
    radial = (xyz - centre) / np.linalg.norm(xyz - centre, axis=1, keepdims=True)
    g1, g2, _ = proj("violante", radial)
    for cond, share in (("1:1", 0.5), ("1:3", 0.75)):
        for k, v in np_maps(share, g1, g2, dot12).items():
            cmp(np_stats(v, roi, gm & ~roi)["tc_p95"], ref["robustness"]["radial_direction"][cond][k]["tc_p95"])
    for v in ref["steering_1to3"]["variants"]:
        if v["label"] != "aseg":
            continue
        m = v["montage"]
        r = roi if v["roi_tissue"] == "gm_wm" else roi & gm
        a1, a2, dt = proj(m, d[f"n_star_{m}"])
        a, b = np_maps(0.5, a1, a2, dt), np_maps(0.75, a1, a2, dt)
        for k in ("env", "msp"):
            cmp(b[k][r].mean() / a[k][r].mean() - 1.0, v["n_star_1to1"][k]["roi_mean_change"])
            if int((b[k][r] > a[k][r]).sum()) != v["n_star_1to1"][k]["n_roi_nodes_rising"]:
                raise AssertionError(f"{m}/{v['roi_tissue']}/{k}: rising-node count differs")
            n_counts += 1
    return {"n_compared": n, "worst_relative_difference": worst, "n_counts_equal": n_counts,
            "n_star_max_1_minus_abs_cos": n_star_dev}


if __name__ == "__main__":
    meta = export()
    res = check()
    print(f"wrote {NPZ} ({NPZ.stat().st_size / 1e6:.1f} MB)")
    print(f"NumPy-only check against fem_quadmaps.json: {res['n_compared']} numbers, worst relative "
          f"difference {res['worst_relative_difference']:.1e}; {res['n_counts_equal']} rising-node "
          f"counts, all equal; n* recomputed from the two fields, max 1 - |cos| "
          f"{res['n_star_max_1_minus_abs_cos']:.1e}")
    for repo, st in meta["producer"].items():
        if isinstance(st, dict) and "clean" in st:
            print(f"{repo}: {st['commit'][:7]}, " + ("clean" if st["clean"] else
                  f"NOT CLEAN ({len(st['not_committed'])} paths not committed)"))
    if res["worst_relative_difference"] > 1e-12:
        raise SystemExit("the export does not reproduce the published aseg numbers")
