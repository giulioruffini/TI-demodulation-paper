"""Render only the five approved label repairs, retaining numerical-call caches.

Run with one of concept, jcurve, jr, ping and optionally --baseline. Baseline
source comes from 0f9ecca; both versions share exact cached simulation returns.
All output and audit records stay beside this script until explicitly installed.
"""
from pathlib import Path
import hashlib
import json
import os
import pickle
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
MODE = sys.argv[1]
BASELINE = "--baseline" in sys.argv
DEST = HERE / ("baseline_render" if BASELINE else "repaired_render")
CACHE = HERE / "numerical_cache"
for path in (DEST, CACHE, HERE / "mplconfig"):
    path.mkdir(exist_ok=True, parents=True)
os.environ["MPLCONFIGDIR"] = str(HERE / "mplconfig")
os.environ["TN_FIGDIR"] = str(DEST)
sys.path.insert(0, str(ROOT / "code"))
os.chdir(ROOT / "code")

import numpy as np
import matplotlib
matplotlib.use("Agg")
from matplotlib.figure import Figure
import overlap


def cached(function):
    def call(*args, **kwargs):
        key = hashlib.sha256(pickle.dumps((function.__module__, function.__name__, args, kwargs))).hexdigest()
        path = CACHE / (key + ".pickle")
        if path.exists():
            print("cache", function.__name__, key[:12], flush=True)
            return pickle.loads(path.read_bytes())
        print("compute", function.__name__, key[:12], flush=True)
        result = function(*args, **kwargs)
        path.write_bytes(pickle.dumps(result, protocol=5))
        return result
    return call


if MODE == "jr":
    import jr_demod
    jr_demod.integrate = cached(jr_demod.integrate)
    jr_demod.openloop_inphase = cached(jr_demod.openloop_inphase)
if MODE == "ping":
    import nmm2_ping
    nmm2_ping.lockin_curve = cached(nmm2_ping.lockin_curve)

savefig = Figure.savefig
recorded = set()


def audited_save(fig, filename, *args, **kwargs):
    stem = Path(filename).stem
    if stem not in recorded:
        recorded.add(stem)
        data = {}
        for ai, ax in enumerate(fig.axes):
            for li, line in enumerate(ax.lines):
                data[f"ax{ai}_line{li}_x"] = np.asarray(line.get_xdata())
                data[f"ax{ai}_line{li}_y"] = np.asarray(line.get_ydata())
            for ci, collection in enumerate(ax.collections):
                data[f"ax{ai}_collection{ci}"] = np.asarray(collection.get_offsets())
            for pi, patch in enumerate(ax.patches):
                if hasattr(patch, "get_height"):
                    data[f"ax{ai}_patch{pi}"] = np.array([patch.get_x(), patch.get_y(), patch.get_width(), patch.get_height()])
        np.savez(DEST / (stem + "_plotted_data.npz"), **data)
        issues = overlap.check(fig, placed_frac=1.0, name=stem, min_pt=6.0, quiet=False)
        renderer = fig.canvas.get_renderer()
        squeeze = overlap.TEXTWIDTH_IN / fig.get_tightbbox(renderer).width
        items = overlap._boxes(fig, renderer)
        audit = {
            "figure": stem,
            "placed_width_pt": overlap.TEXTWIDTH_PT,
            "issues": issues,
            "minimum_printed_text_pt": min(t.get_fontsize() * squeeze for t, _ in items),
            "text": [t.get_text() for t, _ in items],
        }
        (DEST / (stem + "_figcheck.json")).write_text(json.dumps(audit, indent=2))
        (DEST / (stem + ".pickle")).write_bytes(pickle.dumps(fig, protocol=5))
    return savefig(fig, filename, *args, **kwargs)


Figure.savefig = audited_save
script = {"concept": "figures_v2.py", "jcurve": "make_jfig.py", "jr": "jr_twotone_figs.py", "ping": "make_nmm2_twotone_fig.py"}[MODE]
source = subprocess.check_output(["git", "show", "0f9ecca:code/" + script], cwd=ROOT, text=True) if BASELINE else (ROOT / "code" / script).read_text()
namespace = {"__file__": str(ROOT / "code" / script), "__name__": "label_review"}
exec(compile(source, str(ROOT / "code" / script), "exec"), namespace)
if MODE == "concept":
    namespace["concept"]()
elif MODE == "jr":
    namespace["fig_demod"]()
    namespace["fig_curvature"]()
