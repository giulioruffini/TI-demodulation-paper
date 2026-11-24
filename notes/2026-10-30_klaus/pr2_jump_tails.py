"""Tails of the interface jumps in Ricardo's PR #2 JSON, split by map and interface.

Usage: python3 pr2_jump_tails.py <path to code/fem_orientation_interface.json>
(for the PR head: git show 335a65f:code/fem_orientation_interface.json > /tmp/foi.json).
Reads only; prints the table in pr2_jump_tails.txt. Klaus, 2026-10-30.
"""
import json
import sys

d = json.load(open(sys.argv[1]))
J = d["interfaces"]["jump_across_interface"]
print("provenance commit:", d.get("provenance", {}).get("commit", "?"))
print("n* on both sides is the GM row's n*: the less conductive side's envelope maximizer at CSF/GM,")
print("the more conductive side's at GM/WM. Continuum prediction for the envelope: floor 1 at CSF/GM,")
print("ceiling r at GM/WM; nothing for quad and msp along n*; [1, r^deg] for every own-maximum map.\n")
for iface in ("CSF/GM (GM over CSF)", "GM/WM (WM over GM)"):
    v = J[iface]
    n, r = v["n_nodes"], v["conductivity_ratio"]
    print(f"== {iface}: {n} nodes, r = {r:.3f}, r^2 = {r*r:.3f}")
    print(f"{'map':5} {'kind':8} {'median':>7} {'below 1':>9} {'p1':>7} {'above bound':>12} {'nodes':>6} {'max':>9}")
    for k in ("env", "quad", "msp"):
        m = v[k]
        deg = 1 if k == "env" else 2
        for kind, s, t in (("along n*", m["measured_lo_over_hi"], m["measured_tails"]),
                           ("own-max", m["own_maximum_lo_over_hi"], m["own_maximum_lo_over_hi"])):
            print(f"{k:5} {kind:8} {s['median']:7.3f} {100*t['share_below_1']:8.2f}% {t['p1']:7.3f}"
                  f" {100*t['share_above_bound']:11.3f}% {round(t['share_above_bound']*n):6d} {t['max']:9.3g}")
    for c in ("E1", "E2"):
        cv = v["components"][c]
        tm = cv["tangential_mismatch_over_field"]
        nj = cv["normal_jump_by_min_normal_fraction"]
        print(f"  {c}: node-level tangential mismatch / |E|: median {tm['median']:.3f}, p95 {tm['p95']:.3f}, max {tm['max']:.2f};"
              f" normal lo/hi p5 at f>=0: {nj['0.00']['normal_lo_over_hi']['p5']:.2f}, f>=0.10: {nj['0.10']['normal_lo_over_hi']['p5']:.2f},"
              f" f>=0.20: {nj['0.20']['normal_lo_over_hi']['p5']:.2f}")
    print()
v = J["GM/WM from recovered nodal fields (WM over GM)"]
print(f"== GM/WM from the two recovered nodal rows, {v['n_nodes']} nodes (n* exact for the GM row = more conductive side)")
for k in ("env", "quad", "msp"):
    s = v[k]
    print(f"{k:5} median {s['median']:.3f}  p5 {s['p5']:.3f}  p25 {s['p25']:.3f}  p95 {s['p95']:.3f}")
