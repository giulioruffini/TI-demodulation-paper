"""Audit the cached TI/tACS ratio without importing its producer or rerunning trajectories.

Run from any directory: python code/verify_ti_tacs_ratio.py --json <audit.json>.
Uses an independent sigmoid-derivative ratio and explicit interpolation weights.
"""
import argparse
import hashlib
import json
from pathlib import Path

import numpy as np


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    ti_path = root / "code/jcurve_main.npz"
    ta_path = root / "code/tacs_jsweep.npz"
    report = json.loads((root / "docs/r7_ti_tacs_ratio_vs_gamma_2026-10-05.json").read_text())
    with np.load(ti_path) as ti, np.load(ta_path) as ta:
        x = ti["C"]
        assert len(report["rows"]) == len(ta["Cs"])
        assert np.all(np.diff(x) > 0)
        assert x[0] <= ta["Cs"][0] and ta["Cs"][-1] <= x[-1]
        # |sigma''|/sigma' = rho * |1 - 2u|, u = sigma/(2 e0).
        u = 1 / (1 + np.exp(-0.56 * (8.3 - 6.0)))
        predicted = 0.56 * abs(1 - 2*u) * 0.3**2 / (2 * 0.1)
        assert abs(predicted - report["linear_response_ratio"]) < 1e-14
        errors = []
        for c, amp, g, row in zip(ta["Cs"], ta["A"], ta["gam"], report["rows"]):
            k = min(max(int(np.searchsorted(x, c)), 1), len(x)-1)
            w = (c-x[k-1]) / (x[k]-x[k-1])
            ati = ti["Acl"][k-1]**(1-w) * ti["Acl"][k]**w
            ratio = ati / amp
            assert abs(row["C"]-c) < 1e-12 and abs(row["gamma_per_s"]-g) < 1e-12
            errors.append(abs(ratio-row["ratio"]))
        assert max(errors) < 1e-12
        result = {
            "linear_ratio": predicted,
            "rows_checked": len(errors),
            "max_absolute_ratio_error": max(errors),
            "interpolation_extrapolates": False,
            "source_sha256": {p.name: hashlib.sha256(p.read_bytes()).hexdigest()
                              for p in (ti_path, ta_path)},
            "scope": "Cache arithmetic verified; not a new trajectory or causal decomposition.",
        }
    if args.json:
        args.json.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
