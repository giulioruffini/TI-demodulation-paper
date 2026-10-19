"""Check the FEM integration against Ricardo Salvador's preserved PR outputs.

This checks the portable arrays and summaries, not the private FEM solve.
Run from any directory with NumPy installed. The JSON report records that limit.
"""
import hashlib
import json
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "code"
r = json.loads((DATA / "fem_quadmaps.json").read_text())
d = np.load(DATA / "fem_quadmaps.npz")
share = d["share"]
i11 = int(np.flatnonzero(np.isclose(share, 0.5))[0])
i13 = int(np.flatnonzero(np.isclose(share, 0.75))[0])
array_errors = {}
for name in d.files:
    if "__" in name:
        model, observable = name.split("__", 1)
        error = float(np.max(np.abs(d[name] - r["sweep"][model][observable])))
        assert error == 0, name
        array_errors[name] = error

summary = {}
for model in ("env", "quad", "msp", "iso"):
    a, b = r["conditions"]["1:1"][model], r["conditions"]["1:3"][model]
    for i, condition in ((i11, a), (i13, b)):
        for key in ("roi_mean", "tc_p95", "tc_mean", "cortex_p95"):
            np.testing.assert_allclose(d[f"{model}__{key}"][i], condition[key],
                                       rtol=1e-13, atol=1e-15)
    displacement = float(d[f"{model}__disp_axis_top10_mm"][i13])
    np.testing.assert_allclose(displacement,
        r["displacement_1to3_vs_1to1"][model]["top10"]["anterior_along_hippocampus_mm"])
    grid = [row["anterior_along_hippocampus_mm"]
            for row in r["sensitivity_grid"]["combinations"] if row["map"] == model]
    assert len(grid) == 32
    if model == "env":
        assert all(x > 0 for x in grid)
    elif model == "msp":
        assert all(x < 0 for x in grid)
    else:
        assert all(x == 0 for x in grid)
        np.testing.assert_allclose(d[f"{model}__roi_mean"] / a["roi_mean"],
                                   4 * share * (1 - share), rtol=1e-13)
        np.testing.assert_allclose(d[f"{model}__tc_p95"], a["tc_p95"], rtol=1e-13)
    summary[model] = {
        "reference_p95_ratio_1to1": a["tc_p95"],
        "reference_p95_ratio_1to3": b["tc_p95"],
        "degree_matched_ratio_1to1": a.get("degree_matched", a)["tc_p95"],
        "roi_mean_1to1": a["roi_mean"],
        "roi_mean_1to3_over_1to1": b["roi_mean"] / a["roi_mean"],
        "focus_shift_mm": displacement,
        "sensitivity_count": len(grid),
        "sensitivity_range_mm": [min(grid), max(grid)]}

slice_errors = {}
for model, index in (("quad", 1), ("iso", 3)):
    a, b = d["slice_maps"][2 * index:2 * index + 2]
    mask = np.isfinite(a) & np.isfinite(b)
    err = float(np.max(np.abs(b[mask] - 0.75 * a[mask])))
    np.testing.assert_allclose(b[mask], 0.75 * a[mask], rtol=2e-6, atol=1e-8)
    slice_errors[model] = err  # float32 spatial interpolation, not full node fields

report = {
    "date": "2026-10-19",
    "contribution_commit": "d7790943ae8ed9186c7a6233cc7698f58efeb992",
    "scope": "Portable FEM outputs checked; private field solve and field-to-map producer not rerun.",
    "reference_mask": "All gray-matter nodes outside the hippocampal ROI, including other deep GM.",
    "file_sha256": {p.name: hashlib.sha256(p.read_bytes()).hexdigest()
                    for p in (DATA / "fem_quadmaps.json", DATA / "fem_quadmaps.npz")},
    "matching_array_count": len(array_errors),
    "max_json_array_difference": max(array_errors.values()),
    "interpolated_slice_scaling_max_abs": slice_errors,
    "summary": summary,
    "status": "pass"}
out = ROOT / "docs/fem_integration_checks_2026-10-19.json"
out.write_text(json.dumps(report, indent=2) + "\n")
print(json.dumps(report, indent=2))
