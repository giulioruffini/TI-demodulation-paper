"""Realistic-head comparison (Sec. 4.5): field orientation and fields at tissue interfaces.

Same subject, ROI, montage, condition and direction as code/fem_quadmaps.py:
IXI002; the GM + WM nodes inside the FreeSurfer aseg left hippocampus (label
17); the 1:1 condition (2 + 2 mA); n*, the 1:1 envelope-maximizing direction at
each node. The script reads the stored per-pair fields, the node potentials, the
head mesh, the labels and the HippUnfold laminar coordinate, and runs no new
solve. The settings, including the HippUnfold run, are listed in
docs/fem_ixi002_violante.md.

**Orientation** (both montages):

* vectors, separately: E1, E2 (each pair's field at 2 mA) and n*;
* axes: PC1, PC2, PC3 of the ROI node coordinates (PC1 anterior-oriented, as in
  the methods; PC2 lateral-oriented; PC3 = PC1 x PC2), and the HippUnfold
  laminar direction (normalized gradient of the inner-outer Laplace coordinate,
  sampled at the nearest voxel, no smoothing), over all nodes where it is defined
  and over interior nodes only;
* angles between undirected axes, folded to 0-90 degrees; median and IQR,
  per node and field-weighted (weights |E1|, |E2| and the 1:1 envelope TImax);
* the carrier separation angle(E1, E2), with the same definitions;
* what a laminar-aligned cell receives: |cos| per carrier, and the measured
  ratios M_env(laminar)/TImax, M_quad(laminar)/max-over-orientation and
  I(laminar)/max-over-orientation;
* how much the laminar field rotates: its principal axis and the angle of each
  node's laminar direction to it;
* whether the published electrode positions can coexist with a standard
  64-position cap (20 mm discs).

**Interfaces** (Violante, 1:1, maps along n*, lambda_0 = 0.5):

* interfaces from the head mesh's tetrahedral tissue tags: a face shared by two
  tetrahedra of different tags; CSF/GM, GM/WM and WM/CSF;
* distance of each node to an interface: Euclidean distance to the nearest
  interface vertex or face centroid (resolution reported);
* GM p99 within 2 mm of CSF/GM over GM p99 beyond 2 mm, and the WM analogue
  for GM/WM;
* the share of each map's top 1 % (GM + WM nodes) within 2 mm of any interface,
  beside the share of all nodes within 2 mm;
* strict local maxima of each map within GM and within WM, along one spatially
  fixed direction and along n*, and the share on a compartment boundary (Sec. 2.6);
* each map's jump across the interface at the same node and the same
  orientation, from the element fields on either side (node potentials), beside
  the jump-condition prediction E_low = A E_high, A = I + (r - 1) nu nu^T, with r
  the conductivity ratio. A has eigenvalues 1, 1, r, so r (r^2 for the
  second-order maps) bounds |E| and each map at its own orientation maximum; it
  does not bound a map along a fixed direction such as n*, whose ratio across the
  interface is unbounded (normal and tangential parts can cancel on one side).
  Reported per map: the measured ratio along n*, its tails (shares and counts
  below 1 and above the bound, with the minimum and maximum), and the ratio of
  the own-maximum maps against [1, r^deg], with the same tails;
* the field components on the two sides, per interface face (each side's element
  field, the face's own normal) and per interface node (side-mean element field,
  area-weighted normal), for E1 and E2: the tangential mismatch, which linear
  elements make zero on a shared face, and the realised normal jump against r,
  over the faces (nodes) whose high-side normal part is at least a fraction f of
  |E|, f swept over MIN_NORMAL_FRACTIONS.

Run with the TI library's interpreter (numpy, scipy, nibabel), with
TI_MODEL_ROOT pointing at a checkout that holds the IXI002 outputs:

    TI_MODEL_ROOT=/path/to/temporal-interference-library python code/fem_orientation_interface.py

Writes fem_orientation_interface.json (every orientation and interface number
quoted in Sec. 4.5) next to this script.
"""
import json
import os
import sys
from pathlib import Path
from types import SimpleNamespace

import nibabel as nib
import numpy as np
from scipy.ndimage import binary_erosion
from scipy.spatial import cKDTree

HERE = Path(__file__).resolve().parent
TI = os.environ.get("TI_MODEL_ROOT")
if not TI or not (Path(TI) / "ti_model").is_dir():
    raise SystemExit("set TI_MODEL_ROOT to a checkout of temporal-interference-library "
                     "(https://gitlab.neuroelectrics.com/ricardo.salvador/"
                     "temporal-interference-library) holding output/ixi002/")
TI = Path(TI)
sys.path[:0] = [str(TI), str(TI / "tools")]

import quadmaps_carrier_geometry as cg  # noqa: E402
import quadmaps_maps as qm  # noqa: E402
import quadmaps_solve as qs  # noqa: E402
from ti_model.fem.recover import element_field  # noqa: E402
from ti_model.io.mesh_io import read_mesh  # noqa: E402
from ti_model.physics.metrics import quad_dc_max, quad_max, ti_max, ti_max_direction  # noqa: E402
from ti_model.provenance import hash_file  # noqa: E402
from ti_model.spaces import Space, SpaceRegistry  # noqa: E402
from ti_model.targets.directions import build_direction_field  # noqa: E402

RESULTS = HERE / "fem_orientation_interface.json"
MESH = qm.OUT / "mesh" / "IXI002_violante_fixth0.msh"
IO = qm.OUT / "hippunfold" / "sub-IXI002_dir-IO_hemi-L_space-cropT1w_label-hipp_desc-laplace_coords.nii.gz"
LAMBDA0 = 0.5
I_PAIR = 2e-3
NEAR_MM = 2.0
GM, WM, CSF = 2, 1, 3
MIN_NORMAL_FRACTIONS = (0.0, 0.05, 0.1, 0.2, 0.3, 0.5)   # face/node selection for the normal jump
SIGMA = {WM: 0.15, GM: 0.40, CSF: 1.79}    # S/m, the values the fields were solved with (settings document)


def wquant(v, w, qs_):
    o = np.argsort(v)
    v, w = v[o], w[o]
    c = np.cumsum(w) - 0.5 * w
    return [float(np.interp(q * w.sum(), c, v)) for q in qs_]


def angles(vec, ref, weights=None) -> dict:
    a = cg.axis_angle(vec, ref)
    out = {"per_node": cg.summary(a)}
    if weights is not None:
        p25, p50, p75 = wquant(a, np.asarray(weights, float), (0.25, 0.5, 0.75))
        out["field_weighted"] = {"median": p50, "p25": p25, "p75": p75}
    return out


def maps_along(e1, e2, n):
    a = LAMBDA0 * np.einsum("ij,ij->i", e1, n)
    b = LAMBDA0 * np.einsum("ij,ij->i", e2, n)
    return {"env": 2 * np.minimum(abs(a), abs(b)), "quad": 2 * abs(a * b), "msp": 0.5 * (a * a + b * b)}


# --------------------------------------------------------------- orientation

def laminar(g):
    rows = np.load(qm.OUT / "fields" / "violante.npz")["rows"]
    spaces = SpaceRegistry()
    spaces.add_space(Space("mesh_world", "world"))
    spaces.add_space(Space("laminar_world", "world"))
    spaces.add_transform("laminar_world", "mesh_world", np.eye(4),
                         source="HippUnfold space-T1w is the head-model T1 grid")
    nodes = np.zeros((int(rows[:, 0].max()) + 1, 3))
    nodes[rows[:, 0]] = g["xyz"]
    lam = build_direction_field("hippocampal_laminar", SimpleNamespace(nodes=nodes), rows,
                                spaces=spaces, roi_mask=g["roi"], laminar_path=IO)
    k = np.flatnonzero(lam.defined & g["roi"])
    img = nib.load(str(IO))
    interior = binary_erosion(np.asarray(img.dataobj) > 0)
    inv = np.linalg.inv(img.affine)
    vi = np.rint((inv[:3, :3] @ g["xyz"][k].T).T + inv[:3, 3]).astype(int)
    return k, lam.vectors[k], interior[vi[:, 0], vi[:, 1], vi[:, 2]]


def orientation(G) -> dict:
    g0 = G["violante"]
    fr, roi = g0["fr"], np.flatnonzero(g0["roi"])
    k, L, inner = laminar(g0)
    ev, V = np.linalg.eigh(L.T @ L)
    principal = V[:, -1]
    out = {"roi_nodes": int(len(roi)), "laminar_defined_nodes": int(len(k)),
           "laminar_interior_nodes": int(inner.sum()),
           "laminar_coverage": float(len(k) / len(roi)),
           "pc_axes": {"PC1_long": fr["long"].tolist(), "PC2": fr["trans"].tolist(),
                       "PC3": fr["normal"].tolist(), "sd_mm": fr["sd_mm"].tolist()},
           "laminar_rotation": {
               "principal_axis": principal.tolist(),
               "principal_axis_eigenvalue_fraction": float(ev[-1] / ev.sum()),
               "angle_to_principal_axis_deg": cg.summary(cg.axis_angle(L, principal)),
               "principal_axis_vs_PC3_deg": float(cg.axis_angle(principal, fr["normal"])[0])},
           "laminar_vs_pc_axes_deg": {
               sub: {ax: cg.summary(cg.axis_angle(L[m], v)) for ax, v in
                     (("PC1_long", fr["long"]), ("PC2", fr["trans"]), ("PC3", fr["normal"]))}
               for sub, m in (("all_defined", slice(None)), ("interior", inner))},
           "montages": {}}
    for mname, g in G.items():
        e1, e2 = g["E1"][roi], g["E2"][roi]
        n1, n2 = np.linalg.norm(e1, axis=1), np.linalg.norm(e2, axis=1)
        nstar = ti_max_direction(e1, e2)
        tmax = ti_max(e1, e2)
        vecs = {"E1": (e1, n1), "E2": (e2, n2), "n_star": (nstar, tmax)}
        m = {"carrier_separation_deg": angles(e1, e2, np.sqrt(n1 * n2)),
             "vs_PC_axes_deg": {v: {ax: angles(x, ref, w) for ax, ref in
                                    (("PC1_long", fr["long"]), ("PC2", fr["trans"]),
                                     ("PC3", fr["normal"]))} for v, (x, w) in vecs.items()},
             "vs_laminar_deg": {}, "laminar_aligned_cell": {}}
        idx = np.searchsorted(roi, k)                  # positions of the laminar nodes within roi
        for sub, msk in (("all_defined", np.ones(len(k), bool)), ("interior", inner)):
            sel = idx[msk]
            m["vs_laminar_deg"][sub] = {v: angles(x[sel], L[msk], w[sel]) for v, (x, w) in vecs.items()}
            a1 = np.abs(np.einsum("ij,ij->i", e1[sel], L[msk])) / n1[sel]
            a2 = np.abs(np.einsum("ij,ij->i", e2[sel], L[msk])) / n2[sel]
            lam_maps = maps_along(e1[sel], e2[sel], L[msk])
            env_max = LAMBDA0 * tmax[sel]
            quad_mx = LAMBDA0 ** 2 * quad_max(e1[sel], e2[sel])
            msp_mx = LAMBDA0 ** 2 * quad_dc_max(e1[sel], e2[sel])
            m["laminar_aligned_cell"][sub] = {
                "abs_cos_E1": cg.summary(a1), "abs_cos_E2": cg.summary(a2),
                "product_abs_cos": cg.summary(a1 * a2),
                "env_over_orientation_max": cg.summary(lam_maps["env"] / env_max),
                "quad_over_orientation_max": cg.summary(lam_maps["quad"] / quad_mx),
                "msp_over_orientation_max": cg.summary(lam_maps["msp"] / msp_mx)}
        out["montages"][mname] = m
    return out


# --------------------------------------------------------------- interfaces

def faces_between(mesh):
    """Faces shared by two tetrahedra of different tags: (nodes (n,3), tet a, tet b)."""
    t = mesh.tets.astype(np.int64)
    comb = ((0, 1, 2), (0, 1, 3), (0, 2, 3), (1, 2, 3))
    f = np.sort(np.concatenate([t[:, c] for c in comb]), axis=1)
    owner = np.tile(np.arange(len(t)), 4)
    key = (f[:, 0] << 42) | (f[:, 1] << 21) | f[:, 2]
    o = np.argsort(key, kind="stable")
    key, f, owner = key[o], f[o], owner[o]
    dup = np.flatnonzero(key[1:] == key[:-1])
    ta, tb = owner[dup], owner[dup + 1]
    diff = mesh.tet_tags[ta] != mesh.tet_tags[tb]
    return f[dup][diff], ta[diff], tb[diff]


def interface(mesh, faces, ta, tb, tag_lo, tag_hi):
    """Faces between ``tag_hi`` (higher conductivity side) and ``tag_lo``, normals hi -> lo."""
    tags_a, tags_b = mesh.tet_tags[ta], mesh.tet_tags[tb]
    sel = ((tags_a == tag_hi) & (tags_b == tag_lo)) | ((tags_a == tag_lo) & (tags_b == tag_hi))
    fc, a, b = faces[sel], ta[sel], tb[sel]
    hi = np.where(mesh.tet_tags[a] == tag_hi, a, b)
    lo = np.where(mesh.tet_tags[a] == tag_hi, b, a)
    p = mesh.nodes[fc]
    nrm = np.cross(p[:, 1] - p[:, 0], p[:, 2] - p[:, 0])
    cen = p.mean(axis=1)
    hc = mesh.nodes[mesh.tets[hi]].mean(axis=1)
    nrm = np.where(((cen - hc) * nrm).sum(1, keepdims=True) < 0, -nrm, nrm)   # hi -> lo
    return {"faces": fc, "hi": hi, "lo": lo, "normal_area": 0.5 * nrm, "centroid": cen}


def node_side_field(mesh, E_el, iface, side: str):
    """Per interface node: mean element field over that side's tets at the interface, and the normal."""
    tet = iface[side]
    nodes = iface["faces"].ravel()
    tets3 = np.repeat(tet, 3)
    uniq, inv = np.unique(nodes, return_inverse=True)
    acc = np.zeros((len(uniq), 3))
    cnt = np.zeros(len(uniq))
    np.add.at(acc, inv, E_el[tets3])
    np.add.at(cnt, inv, 1)
    nrm = np.zeros((len(uniq), 3))
    np.add.at(nrm, inv, np.repeat(iface["normal_area"], 3, axis=0))
    nrm /= np.maximum(np.linalg.norm(nrm, axis=1, keepdims=True), 1e-30)
    return uniq, acc / cnt[:, None], nrm


def components(eh, el, nu, r) -> dict:
    """Normal and tangential parts of one carrier's field on the two sides of an interface.

    ``eh``, ``el``: high- and low-conductivity side fields; ``nu``: unit normals.
    The jump condition makes the tangential part continuous and multiplies the
    normal part by r; ``flux_ratio`` = (normal ratio) / r is 1 where normal current
    is conserved.
    """
    nh, nl = np.einsum("ij,ij->i", eh, nu), np.einsum("ij,ij->i", el, nu)
    th, tl = eh - nh[:, None] * nu, el - nl[:, None] * nu
    mag_h, mag_l = np.linalg.norm(eh, axis=1), np.linalg.norm(el, axis=1)
    frac = np.abs(nh) / mag_h
    mis = np.linalg.norm(tl - th, axis=1) / mag_h
    out = {"n": int(len(nh)),
           "tangential_mismatch_over_field": {"median": float(np.median(mis)),
                                              "p95": float(np.percentile(mis, 95)),
                                              "max": float(mis.max())},
           "tangential_lo_over_hi": cg.summary(np.linalg.norm(tl, axis=1) / np.linalg.norm(th, axis=1)),
           "field_magnitude_lo_over_hi": cg.summary(mag_l / mag_h),
           "normal_fraction_hi_side": cg.summary(frac),
           "normal_fraction_lo_side": cg.summary(np.abs(nl) / mag_l),
           "normal_jump_by_min_normal_fraction": {}}
    for f in MIN_NORMAL_FRACTIONS:
        sel = (frac >= f) & (nh != 0)
        q = nl[sel] / nh[sel]
        out["normal_jump_by_min_normal_fraction"][f"{f:.2f}"] = {
            "n": int(sel.sum()), "share": float(sel.mean()),
            "normal_lo_over_hi": cg.summary(q), "flux_ratio": cg.summary(q / r)}
    return out


def face_components(E1_el, E2_el, iface, r) -> dict:
    """Per interface face: each side's element field and the face's own normal (hi -> lo)."""
    nu = iface["normal_area"] / np.linalg.norm(iface["normal_area"], axis=1, keepdims=True)
    return {"conductivity_ratio": float(r),
            **{lab: components(E[iface["hi"]], E[iface["lo"]], nu, r)
               for lab, E in (("E1", E1_el), ("E2", E2_el))}}


def tails(x, bound) -> dict:
    """Shares and counts outside [1, bound], with the extremes: a percentile bounds no count."""
    below, above = x < 1.0 - 1e-9, x > bound * (1.0 + 1e-9)
    return {"share_below_1": float(np.mean(below)),
            "share_above_bound": float(np.mean(above)),
            "p1": float(np.percentile(x, 1)), "p99": float(np.percentile(x, 99)), "max": float(x.max()),
            "n": int(x.size), "n_below_1": int(below.sum()), "n_above_bound": int(above.sum()),
            "min": float(x.min())}


def jump(mesh, E1_el, E2_el, iface, r, nstar_of_node):
    """Map jump lo/hi at interface nodes, along the GM row's n*; measured and predicted.

    Also the own-maximum maps' jump (bounded by [1, r^deg]) and the paired per-node
    field components (``components``). Where an own-maximum map leaves [1, r^deg], the
    E1 realised normal jump and tangential mismatch at those nodes say which component
    departs from the jump condition (``outside_bound_E1``).
    """
    u, e1h, nu = node_side_field(mesh, E1_el, iface, "hi")
    _, e2h, _ = node_side_field(mesh, E2_el, iface, "hi")
    _, e1l, _ = node_side_field(mesh, E1_el, iface, "lo")
    _, e2l, _ = node_side_field(mesh, E2_el, iface, "lo")
    n = nstar_of_node(u)
    ok = np.isfinite(n).all(axis=1)
    u, e1h, e2h, e1l, e2l, nu, n = u[ok], e1h[ok], e2h[ok], e1l[ok], e2l[ok], nu[ok], n[ok]
    pred = lambda e: e + (r - 1.0) * np.einsum("ij,ij->i", e, nu)[:, None] * nu   # noqa: E731
    mh, ml = maps_along(e1h, e2h, n), maps_along(e1l, e2l, n)
    mp = maps_along(pred(e1h), pred(e2h), n)
    cos_n = np.abs(np.einsum("ij,ij->i", n, nu))
    out = {"n_nodes": int(len(u)), "conductivity_ratio": float(r),
           "bound_field_magnitude_and_own_maximum_maps": {
               "first_order": float(r), "second_order": float(r * r),
               "note": ("|E| and each map at its own orientation maximum jump by a factor in [1, r] "
                        "([1, r^2] for second-order maps); no bound holds along a fixed direction")},
           "angle_nstar_to_interface_normal_deg": cg.summary(np.degrees(np.arccos(np.clip(cos_n, 0, 1)))),
           "field_normal_fraction_hi_side": cg.summary(
               np.abs(np.einsum("ij,ij->i", e1h, nu)) / np.linalg.norm(e1h, axis=1))}
    own_max = {"env": (ti_max, 1), "quad": (quad_max, 2), "msp": (quad_dc_max, 2)}
    tang = lambda e: e - np.einsum("ij,ij->i", e, nu)[:, None] * nu   # noqa: E731
    mismatch = np.linalg.norm(tang(e1l) - tang(e1h), axis=1) / np.linalg.norm(tang(e1h), axis=1)
    normal_jump = np.einsum("ij,ij->i", e1l, nu) / np.einsum("ij,ij->i", e1h, nu)

    def at(sel):
        return {"n": int(sel.sum()), "normal_lo_over_hi_median": float(np.median(normal_jump[sel])),
                "tangential_mismatch_median": float(np.median(mismatch[sel])),
                "tangential_mismatch_percentile_of_all": float(
                    100.0 * np.mean(mismatch <= np.median(mismatch[sel])))}

    for k in ("env", "quad", "msp"):
        good = mh[k] > 1e-12 * mh[k].max()
        meas = ml[k][good] / mh[k][good]
        fn, deg = own_max[k]
        oh, ol = fn(e1h, e2h), fn(e1l, e2l)
        own = ol[oh > 0] / oh[oh > 0]
        q = np.where(oh > 0, ol / np.where(oh > 0, oh, 1.0), 1.0)
        out[k] = {"measured_lo_over_hi": cg.summary(meas),
                  "predicted_lo_over_hi": cg.summary(mp[k][good] / mh[k][good]),
                  "measured_tails": tails(meas, r ** deg),
                  "own_maximum_lo_over_hi": {**cg.summary(own), **tails(own, r ** deg),
                                             "share_within_bound": float(np.mean(
                                                 (own >= 1.0 - 1e-9) & (own <= r ** deg * (1.0 + 1e-9)))),
                                             "outside_bound_E1": {
                                                 "above_bound": at(q > r ** deg * (1.0 + 1e-9)),
                                                 "below_1": at(q < 1.0 - 1e-9),
                                                 "all": at(np.ones(len(q), bool))}}}
    out["components"] = {"E1": components(e1h, e1l, nu, r), "E2": components(e2h, e2l, nu, r)}
    return out


def local_maxima(mesh, rows, tags, values, comp, boundary_nodes) -> dict:
    """Strict local maxima of a nodal map within one compartment, and how many lie on its boundary.

    Neighbours are the nodes sharing a tetrahedron edge within that compartment.
    Section 2.6: with a spatially fixed coupling, the mean-square polarization is
    subharmonic in a homogeneous conductor, so it has no strict interior maximum.
    """
    tet = mesh.tets[mesh.tet_tags == comp]
    e = np.vstack([tet[:, [i, j]] for i, j in ((0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3))])
    sel = tags == comp
    nodes = rows[sel, 0]
    v = np.full(mesh.n_nodes, -np.inf)
    v[nodes] = values[sel]
    nb = np.full(mesh.n_nodes, -np.inf)
    np.maximum.at(nb, e[:, 0], v[e[:, 1]])
    np.maximum.at(nb, e[:, 1], v[e[:, 0]])
    is_max = v[nodes] > nb[nodes]
    on_b = np.isin(nodes, boundary_nodes)
    return {"n_nodes": int(len(nodes)), "boundary_fraction_of_nodes": float(on_b.mean()),
            "n_strict_local_maxima": int(is_max.sum()),
            "n_interior_maxima": int((is_max & ~on_b).sum()),
            "fraction_of_maxima_on_boundary": float(on_b[is_max].mean()) if is_max.any() else None}


def interface_brightening() -> dict:
    mesh = read_mesh(MESH, tag_names=qs.tag_names(), check_quality=False)
    f = np.load(qm.OUT / "fields" / "violante.npz")
    rows, xyz = f["rows"], f["xyz"].astype(float)
    E1, E2 = I_PAIR * f["E1"].astype(float), I_PAIR * f["E2"].astype(float)
    tags = rows[:, 1]
    nstar = ti_max_direction(E1, E2)
    maps = maps_along(E1, E2, nstar)

    faces, ta, tb = faces_between(mesh)
    ifc = {"CSF/GM": interface(mesh, faces, ta, tb, GM, CSF),
           "GM/WM": interface(mesh, faces, ta, tb, WM, GM),
           "WM/CSF": interface(mesh, faces, ta, tb, WM, CSF)}
    dist = {}
    for name, d in ifc.items():
        pts = np.vstack([mesh.nodes[np.unique(d["faces"])], d["centroid"]])
        dist[name] = cKDTree(pts).query(xyz)[0]
    dist["any"] = np.minimum.reduce([dist[n] for n in ("CSF/GM", "GM/WM", "WM/CSF")])
    edge = np.linalg.norm(mesh.nodes[ifc["CSF/GM"]["faces"][:, 0]]
                          - mesh.nodes[ifc["CSF/GM"]["faces"][:, 1]], axis=1)

    gm, wm, brain = tags == GM, tags == WM, np.isin(tags, (GM, WM))
    near_csf, near_gw = dist["CSF/GM"] <= NEAR_MM, dist["GM/WM"] <= NEAR_MM
    out = {"maps": "along n* (1:1 envelope-maximizing), 1:1 = 2 + 2 mA, lambda0 = 0.5 mV per V/m",
           "interface_definition": ("faces shared by two tetrahedra of different tissue tags in the "
                                    "head mesh (headreco segmentation, linear tetrahedra)"),
           "distance_definition": (f"Euclidean distance from each node to the nearest interface vertex "
                                   f"or face centroid; near = <= {NEAR_MM} mm"),
           "csf_gm_interface_edge_mm": cg.summary(edge),
           "n_interface_faces": {k: int(len(v["faces"])) for k, v in ifc.items()},
           "near_far_p99": {}, "top_percentile_near_interface": {}, "jump_across_interface": {}}
    out["near_far_p99"]["GM_vs_CSF/GM"] = {"n_near": int((gm & near_csf).sum()),
                                           "n_far": int((gm & ~near_csf).sum())}
    out["near_far_p99"]["WM_vs_GM/WM"] = {"n_near": int((wm & near_gw).sum()),
                                          "n_far": int((wm & ~near_gw).sum())}
    for k, v in maps.items():
        for key, sel, near in (("GM_vs_CSF/GM", gm, near_csf), ("WM_vs_GM/WM", wm, near_gw)):
            a, b = np.percentile(v[sel & near], 99), np.percentile(v[sel & ~near], 99)
            out["near_far_p99"][key][k] = {"p99_near": float(a), "p99_far": float(b),
                                           "ratio": float(a / b)}
    base = {n: float(np.mean(dist[n][brain] <= NEAR_MM)) for n in dist}
    out["top_percentile_near_interface"]["baseline_all_brain_nodes"] = base
    for k, v in maps.items():
        top = brain & (v >= np.percentile(v[brain], 99))
        out["top_percentile_near_interface"][k] = {
            "n_top": int(top.sum()), **{n: float(np.mean(dist[n][top] <= NEAR_MM)) for n in dist},
            "gm_fraction_of_top": float(np.mean(tags[top] == GM))}

    # section 2.6: are the maps' local maxima on compartment boundaries?
    fixed = np.tile(np.array([1.0, 0.0, 0.0]), (len(rows), 1))    # one spatially fixed direction
    sub = {}
    for comp, cname in ((GM, "GM"), (WM, "WM")):
        other = (mesh.tet_tags[ta] == comp) != (mesh.tet_tags[tb] == comp)
        bnodes = np.unique(faces[other])
        for dname, direction in (("fixed_x", fixed), ("n_star", nstar)):
            mp = maps_along(E1, E2, direction)
            for k in ("msp", "quad", "env"):
                sub[f"{cname}/{dname}/{k}"] = local_maxima(mesh, rows, tags, mp[k], comp, bnodes)
    out["local_maxima_on_boundary"] = {
        "definition": ("strict local maxima of the nodal map among nodes sharing a tetrahedron "
                       "edge in the same compartment; boundary = nodes on a face shared with "
                       "another tissue"),
        "prediction_section_2_6": ("with a fixed direction, msp is subharmonic within each "
                                   "homogeneous compartment: no strict interior maximum; the beat "
                                   "map has no such restriction"),
        **sub}

    # jump across the interface at fixed orientation, from node potentials
    pots = np.load(qm.OUT / "fields" / "violante_potentials.npz")
    E1_el = I_PAIR * element_field(mesh, pots["phi1"])
    E2_el = I_PAIR * element_field(mesh, pots["phi2"])
    gm_row = {int(nd): i for i, nd in enumerate(rows[:, 0]) if tags[i] == GM}
    wm_row = {int(nd): i for i, nd in enumerate(rows[:, 0]) if tags[i] == WM}

    def nstar_at(table):
        def f_(u):
            idx = np.array([table.get(int(x), -1) for x in u])
            n = np.full((len(u), 3), np.nan)
            n[idx >= 0] = nstar[idx[idx >= 0]]
            return n
        return f_

    s = SIGMA
    out["conductivities_S_per_m"] = {"WM": s[WM], "GM": s[GM], "CSF": s[CSF]}
    out["jump_across_interface"]["CSF/GM (GM over CSF)"] = jump(
        mesh, E1_el, E2_el, ifc["CSF/GM"], s[CSF] / s[GM], nstar_at(gm_row))
    out["jump_across_interface"]["GM/WM (WM over GM)"] = jump(
        mesh, E1_el, E2_el, ifc["GM/WM"], s[GM] / s[WM], nstar_at(gm_row))
    # the GM/WM jump again from the recovered nodal fields (the two compartment rows at one node)
    shared = sorted(set(gm_row) & set(wm_row))
    ig, iw = np.array([gm_row[n] for n in shared]), np.array([wm_row[n] for n in shared])
    mg, mw = maps_along(E1[ig], E2[ig], nstar[ig]), maps_along(E1[iw], E2[iw], nstar[ig])
    out["jump_across_interface"]["GM/WM from recovered nodal fields (WM over GM)"] = {
        "n_nodes": int(len(shared)),
        **{k: cg.summary(mw[k] / np.maximum(mg[k], 1e-30)) for k in mg}}
    # the realised normal jump face by face (linear elements: tangential part continuous exactly)
    out["components_per_face"] = {
        "definition": ("each side's element field at an interface face, split on the face's own "
                       "normal; normal_lo_over_hi against r over the faces whose high-side normal "
                       "part is at least the given fraction of |E|; flux_ratio = that ratio / r"),
        "CSF/GM (GM over CSF)": face_components(E1_el, E2_el, ifc["CSF/GM"], s[CSF] / s[GM]),
        "GM/WM (WM over GM)": face_components(E1_el, E2_el, ifc["GM/WM"], s[GM] / s[WM])}
    return out


def cap_overlap() -> dict:
    """Can Violante's electrodes coexist with the standard 64-position cap (20 mm discs)?"""
    def read(path):
        out = {}
        for line in path.read_text().splitlines():
            p = [s.strip() for s in line.split(",")]
            if len(p) >= 5 and p[0] in ("Electrode", "ReferenceElectrode"):
                out[p[4]] = np.array(p[1:4], float)
        return out
    cap = read(qm.OUT / "montages" / "cap64_IXI002.csv")
    vio = read(qm.OUT / "montages" / "violante_IXI002.csv")
    res = {"disc_diameter_mm": 20.0, "overlap_if_centres_closer_than_mm": 20.0, "electrodes": {}}
    for v, p in vio.items():
        d = sorted((float(np.linalg.norm(p - q)), n) for n, q in cap.items())
        res["electrodes"][v] = {"nearest_cap": [{"name": n, "distance_mm": x} for x, n in d[:3]],
                                "overlapping": [n for x, n in d if x < 20.0]}
    return res


def main() -> None:
    G = {m: cg.geometry(m) for m in cg.MONTAGES}
    inputs = {"fields_violante": qm.OUT / "fields" / "violante.npz",
              "fields_yatsuda": qm.OUT / "fields" / "yatsuda.npz",
              "potentials_violante": qm.OUT / "fields" / "violante_potentials.npz",
              "mesh_violante": MESH,
              "aseg": qm.LABELS["aseg"][0],
              "laminar_io_laplace": IO,
              "positions_violante": qm.OUT / "montages" / "violante_IXI002.csv",
              "positions_cap64": qm.OUT / "montages" / "cap64_IXI002.csv"}
    res = {"what": ("field orientation and tissue-interface numbers of the realistic-head comparison "
                    "(IXI002, Violante montage, 1:1)"),
           "provenance": {"ti_library_url": ("https://gitlab.neuroelectrics.com/ricardo.salvador/"
                                             "temporal-interference-library"),
                          "inputs_blake2b512": {k: hash_file(p) for k, p in inputs.items()}},
           "orientation": orientation(G),
           "cap_overlap": cap_overlap(),
           "interfaces": interface_brightening()}
    RESULTS.write_text(json.dumps(res, indent=1), encoding="utf-8")
    print(f"wrote {RESULTS}")


if __name__ == "__main__":
    main()
