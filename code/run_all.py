#!/usr/bin/env python3
"""Run the available TN0484 figure calculations in dependency order.

``--only`` selects figure generators and their data dependencies. ``--from-cache``
replots selected figures without running any data producer or inline simulation;
all required caches must already exist. ``--dry-run`` prints the resolved plan
without writing files. Figure output honors TN_FIGDIR or --figdir; simulations
still write their caches in code/, so use a separate checkout to protect those.

The hand-drawn LaNMM schematic has no generator. The two-tone kHz spectrum can be
replotted, but its original data-producing run is absent from the repository.
"""
import argparse
import importlib.util
import os
import subprocess
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
DEFAULT_FIGDIR = os.path.join(HERE, "..", "figures")

# (label, script, args, [figures produced], note). Order = dependency order:
# data producers (.npz) first, then the generators that consume them.
STEPS = [
    # --- data producers (no figure output; write .npz consumed downstream) ---
    ("data: analyses_v2",   "analyses_v2.py",   [],        [], "-> analyses_v2.npz (feeds figures_v2)"),
    ("data: run_jcurve",    "run_jcurve.py",    [],        [], "-> jcurve_main.npz (feeds make_jfig)"),
    ("data: run_res",       "run_res.py",       [],        [], "-> jcurve_res.npz  (feeds make_jfig)"),
    ("data: qif_raster",    "qif_raster.py",    [],        [], "-> qif_raster.npz  (feeds make_qif_figs)"),
    ("data: nmm2_jcA",      "nmm2_jcA.py",      [],        [], "-> nmm2_jcA.npz (engine)"),
    ("data: nmm2_jcD",      "nmm2_jcD.py",      [],        [], "-> nmm2_jcD.npz (feeds make_nmm2_jfig)"),
    ("data: timing_not_rate","timing_not_rate.py",[],       [], "-> timing_not_rate.npz (feeds make_timing_fig; slow lock-in sweep)"),
    ("data: entrain",       "entrain.py",       [],        [], "-> entrain.npz, entrain_b.npz (tongue, locking; slow)"),
    ("data: entrain_crit",  "entrain_crit.py",  [],        [], "-> entrain_crit.npz (criticality sweep; slow)"),
    # --- genuine two-tone producers (the manuscript's published waveform; added 2026-09-22) ---
    ("data: lanmm_field P2", "lanmm_field_tongues.py", ["--target", "P2", "--wave", "twotone"], [],
        "-> lanmm_field_P2_twotone.npz (slow)"),
    ("data: lanmm_field P1", "lanmm_field_tongues.py", ["--target", "P1", "--wave", "twotone"], [],
        "-> lanmm_field_P1_twotone.npz (slow)"),
    ("data: qif_raster twotone", "qif_raster.py", ["--twotone"], [],
        "-> qif_raster_twotone.npz (N=8000, settle 800 ms + integer-cycle windows; slow)"),
    ("data: ping_fast_carrier_check", "ping_fast_carrier_check.py", [], [],
        "-> ping_fast_carrier_check.json (MPR crossover + PING fast-carrier source error; ~10 s)"),

    # --- figure generators (write to FIGDIR) ---
    ("figures_v2",  "figures_v2.py", [], [
        "fig_concept", "fig_bifurcation_sigmoid", "fig_resonance_map",
        "fig_carrier_independence", "fig_operating_point"], "needs analyses_v2.npz"),
    ("make_figures",     "make_figures.py",    [], ["fig_demodulation", "fig_verification"], ""),
    ("data: resonance stable", "rerun_resonance.py", ["stable"], [],
        "stable branch; long lock-in (slow)"),
    ("data: resonance cycle", "rerun_resonance.py", ["cycle"], [], "legacy cycle branch; not used by fig_resonance"),
    ("rerun_resonance", "rerun_resonance.py", ["plot"], ["fig_resonance"], "needs sweep_hi_stable.npz"),
    ("khz_analysis",     "khz_analysis.py",    [], ["fig_khz"], "membrane-filtered kHz roll-off"),
    ("khz_direct",       "khz_direct.py",      [], ["fig_khz_direct"], "scipy-free; imports timing_not_rate"),
    ("nmm2_ping",        "nmm2_ping.py",       [], ["fig_nmm2_map", "fig_nmm2_resonance"], "grid (slow)"),
    ("lanmm_resonance",  "lanmm_resonance.py", [], ["fig_lanmm_map", "fig_lanmm_resonance"], "grid (slow)"),
    ("lanmm_arnold",     "lanmm_arnold_tongues.py", [], ["fig_lanmm_arnold_p1", "fig_lanmm_arnold_p2"],
        "NEEDS external lanmmv11; auto-skipped if absent"),
    ("make_jfig",        "make_jfig.py",       [], ["fig_jcurve"], "needs jcurve_main/res.npz"),
    ("tacs_jsweep",      "tacs_jsweep.py",     [], ["fig_tacs_jcurve"], "pure numpy"),
    ("make_nmm2_jfig",   "make_nmm2_jfig.py",  [], ["fig_nmm2_jcurve"], "needs nmm2_jcD.npz"),
    ("make_entrain_fig", "make_entrain_fig.py", [], ["fig_entrainment"], "needs entrain*.npz"),
    ("sl_dissociation",  "sl_dissociation.py", [], ["fig_sl_dissociation"], "Stuart-Landau control (pure numpy)"),
    ("make_timing_fig",  "make_timing_fig.py", [], ["fig_timing_not_rate"], "needs timing_not_rate.npz"),
    ("make_qif_figs",    "make_qif_figs.py",   [], ["fig_qif_raster_twotone", "fig_qif_timing_twotone"],
        "needs qif_raster_twotone.npz (legacy AM fallback is not used by run_all)"),
    # --- genuine two-tone figures (2026-09-22) ---
    ("jr_twotone_figs",  "jr_twotone_figs.py", [], ["fig_demodulation_twotone", "fig_curvature_twotone"],
        "pure numpy via jr_demod; no cache"),
    ("make_lanmm_field_figs", "make_lanmm_field_figs.py", ["--wave", "twotone"],
        ["fig_lanmm_field_p1_twotone", "fig_lanmm_field_p2_twotone"], "needs lanmm_field_{P1,P2}_twotone.npz; signed maps"),
    ("make_nmm2_twotone_fig", "make_nmm2_twotone_fig.py", [], ["fig_nmm2_resonance_twotone"],
        "computes the curves via nmm2_ping.lockin_curve (no cache)"),
    ("make_khz_twotone_fig", "make_khz_twotone_fig.py", [], ["fig_khz_twotone"],
        "renders khz_twotone.npz; see GAPS for its producer"),
    ("mpr_crossover_fig", "mpr_crossover_fig.py", [], ["fig_mpr_crossover"],
        "needs ping_fast_carrier_check.json"),
]

# Named prerequisites make subset selection include the data producer and plotter.
# nmm2_jcD imports the nmm2_jcA engine; it does not consume nmm2_jcA.npz.
DEPENDENCIES = {
    "figures_v2": ("data: analyses_v2",),
    "rerun_resonance": ("data: resonance stable",),
    "make_jfig": ("data: run_jcurve", "data: run_res"),
    "make_nmm2_jfig": ("data: nmm2_jcD",),
    "make_entrain_fig": ("data: entrain", "data: entrain_crit"),
    "make_timing_fig": ("data: timing_not_rate",),
    "make_qif_figs": ("data: qif_raster twotone",),
    "make_lanmm_field_figs": ("data: lanmm_field P2", "data: lanmm_field P1"),
    "mpr_crossover_fig": ("data: ping_fast_carrier_check",),
}

# These scripts only render existing data. Other generators run inline simulations
# and must not be selected by --from-cache, even if they also save a cache.
CACHE_INPUTS = {
    "figures_v2": ("analyses_v2.npz", "jr_bifurcation.npz"),
    "rerun_resonance": ("sweep_hi_stable.npz",),
    "make_jfig": ("jcurve_main.npz", "jcurve_res.npz"),
    "make_nmm2_jfig": ("nmm2_jcD.npz",),
    "make_entrain_fig": ("entrain.npz", "entrain_b.npz", "entrain_crit.npz"),
    "make_timing_fig": ("timing_not_rate.npz",),
    "make_qif_figs": ("qif_raster_twotone.npz",),
    "make_lanmm_field_figs": ("lanmm_field_P1_twotone.npz", "lanmm_field_P2_twotone.npz"),
    "make_khz_twotone_fig": ("khz_twotone.npz",),
    "mpr_crossover_fig": ("ping_fast_carrier_check.json",),
}

GAPS = {
    "fig_lanmm_setup": "hand-drawn schematic; no generator",
    "fig_khz_twotone": "replot only: khz_twotone.npz is committed, but its original producer and full run parameters are absent",
}


def has_lanmm():
    return importlib.util.find_spec("lanmmv11") is not None


def figure_map():
    rows = []
    for label, script, _args, figs, note in STEPS:
        deps = ", ".join(DEPENDENCIES.get(label, ()))
        for f in figs:
            details = "; ".join(x for x in (note, "prerequisites: " + deps if deps else "", GAPS.get(f, "")) if x)
            rows.append((f, script, details))
    rows.append(("fig_lanmm_setup", "(none)", GAPS["fig_lanmm_setup"]))
    return sorted(rows)


def resolve_steps(only=(), from_cache=False):
    """Return a dependency-ordered plan; reject unknown or unsupported requests."""
    only = set(only)
    known = {f for _label, _script, _args, figs, _note in STEPS for f in figs}
    unknown = only - known
    if unknown:
        raise ValueError("No generator for: " + ", ".join(sorted(unknown)))
    if only:
        selected = {label for label, _script, _args, figs, _note in STEPS if only.intersection(figs)}
    elif from_cache:
        selected = set(CACHE_INPUTS)
    else:
        selected = {step[0] for step in STEPS}

    if from_cache:
        unsupported = selected - CACHE_INPUTS.keys()
        if unsupported:
            raise ValueError("No cache-only renderer for: " + ", ".join(sorted(unsupported)))

    by_label = {step[0]: step for step in STEPS}
    ordered, seen = [], set()

    def visit(label):
        if label in seen:
            return
        seen.add(label)
        if not from_cache:
            for dep in DEPENDENCIES.get(label, ()):
                visit(dep)
        ordered.append(by_label[label])

    for label, *_rest in STEPS:
        if label in selected:
            visit(label)
    return ordered


def missing_inputs(plan):
    return sorted({name for label, *_rest in plan
                   for name in CACHE_INPUTS.get(label, ())
                   if not os.path.isfile(os.path.join(HERE, name))})


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--figdir", default=os.environ.get("TN_FIGDIR") or DEFAULT_FIGDIR,
                    help="figure output directory (default ../figures); data caches still go to code/")
    ap.add_argument("--only", default="", help="comma-separated figure names; includes their data prerequisites")
    ap.add_argument("--from-cache", action="store_true", help="replot cached data only; never run simulations")
    ap.add_argument("--dry-run", action="store_true", help="print the resolved plan without writing or executing")
    ap.add_argument("--list", action="store_true", help="print figure->script map and dependencies")
    args = ap.parse_args(argv)

    if args.list:
        print(f"{'figure':28s} {'script':24s} note")
        for f, script, note in figure_map():
            print(f"{f:28s} {script:24s} {note}")
        return 0

    only = {x.strip() for x in args.only.split(",") if x.strip()}
    try:
        plan = resolve_steps(only, args.from_cache)
    except ValueError as exc:
        ap.error(str(exc))
    figdir = os.path.abspath(args.figdir)
    print(f"Figure directory: {figdir}")
    print("Mode: " + ("replot existing caches" if args.from_cache else "recompute available data, then plot"))
    if not args.from_cache:
        print(f"Data producers write caches in: {HERE}")
    selected_figs = {f for _label, _script, _args, figs, _note in plan for f in figs}
    for f, note in GAPS.items():
        if f in selected_figs or not only:
            print(f"LIMIT: {f}: {note}")
    if args.dry_run:
        for label, script, sargs, _figs, note in plan:
            print(f"  {label}: {script} {' '.join(sargs)}  {note}")
        if args.from_cache:
            for name in missing_inputs(plan):
                print(f"  MISSING CACHE: {name}")
        return 0

    if args.from_cache:
        missing = missing_inputs(plan)
        if missing:
            ap.error("Missing cached inputs: " + ", ".join(missing) +
                     ". Recompute the selected figures without --from-cache first.")
    os.makedirs(figdir, exist_ok=True)
    env = dict(os.environ, TN_FIGDIR=figdir)
    lanmm_ok = has_lanmm()
    results, failed_labels = [], set()
    for label, script, sargs, figs, note in plan:
        blocked = failed_labels.intersection(DEPENDENCIES.get(label, ()))
        if blocked:
            results.append((label, "FAILED (prerequisite)", 0.0))
            failed_labels.add(label)
            continue
        if script == "lanmm_arnold_tongues.py" and not lanmm_ok:
            results.append((label, "SKIP (no lanmmv11)", 0.0))
            continue
        missing = missing_inputs([(label, script, sargs, figs, note)])
        if missing:
            print(f"FAILED {label}: missing inputs {', '.join(missing)}")
            results.append((label, "FAILED (missing input)", 0.0))
            failed_labels.add(label)
            continue
        cmd = [sys.executable, os.path.join(HERE, script), *sargs]
        print(f">>> {label}: {script} {' '.join(sargs)}", flush=True)
        t0 = time.time()
        proc = subprocess.run(cmd, cwd=HERE, env=env)
        dt = time.time() - t0
        missing_figs = [f for f in figs if not os.path.isfile(os.path.join(figdir, f + ".pdf"))]
        if proc.returncode:
            status = f"FAILED (rc={proc.returncode})"
        elif missing_figs:
            status = "FAILED (missing figure)"
            print("Missing figure PDFs: " + ", ".join(missing_figs))
        else:
            status = "ok"
        if status != "ok":
            failed_labels.add(label)
        results.append((label, status, dt))
        print(f"    {status}  [{dt:.1f}s]\n")

    print("SUMMARY")
    for label, status, dt in results:
        print(f"  {status:28s} {dt:6.1f}s  {label}")
    return 1 if failed_labels else 0


if __name__ == "__main__":
    sys.exit(main())
