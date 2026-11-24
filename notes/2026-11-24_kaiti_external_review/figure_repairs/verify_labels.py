"""Compare baseline/repaired plotted arrays and check genuinely drawn text."""
from pathlib import Path
import hashlib
import json
import os
import pickle
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
os.environ["MPLCONFIGDIR"] = str(HERE / "mplconfig")
sys.path.insert(0, str(ROOT / "code"))
import numpy as np
import matplotlib
matplotlib.use("Agg")
import fitz
import overlap
from PIL import Image

result = {}
original_boxes = overlap._boxes


def drawn_boxes(fig, renderer):
    omitted = set()
    for ax in fig.axes:
        for axis in (ax.xaxis, ax.yaxis):
            low, high = sorted(axis.get_view_interval())
            if not ax.axison:
                omitted.update((id(axis.label), id(axis.offsetText)))
            for tick in list(axis.majorTicks) + list(axis.minorTicks):
                if not ax.axison or not low - 1e-9 <= tick.get_loc() <= high + 1e-9:
                    omitted.update((id(tick.label1), id(tick.label2)))
    return [(t, box) for t, box in original_boxes(fig, renderer) if id(t) not in omitted]


overlap._boxes = drawn_boxes
for datafile in sorted((HERE / "repaired_render").glob("*_plotted_data.npz")):
    name = datafile.name.removesuffix("_plotted_data.npz")
    before = np.load(HERE / "baseline_render" / datafile.name)
    after = np.load(datafile)
    assert before.files == after.files
    assert all(np.array_equal(before[k], after[k], equal_nan=True) for k in before.files), name
    fig = pickle.loads((HERE / "repaired_render" / (name + ".pickle")).read_bytes())
    issues = overlap.check(fig, placed_frac=1.0, min_pt=6.0, name=name)
    renderer = fig.canvas.get_renderer()
    squeeze = overlap.TEXTWIDTH_IN / fig.get_tightbbox(renderer).width
    minimum = min(t.get_fontsize()*squeeze for t, _ in drawn_boxes(fig, renderer))
    pdf = fitz.open(HERE / "repaired_render" / (name + ".pdf"))
    page = pdf[0]
    zoom = overlap.TEXTWIDTH_PT * 2 / page.rect.width
    page.get_pixmap(matrix=fitz.Matrix(zoom, zoom), alpha=False).save(HERE / "repaired_render" / (name + "_placed.png"))
    oldimage = np.asarray(Image.open(ROOT / "figures" / (name + ".png")).convert("RGBA"))
    baselineimage = np.asarray(Image.open(HERE / "baseline_render" / (name + ".png")).convert("RGBA"))
    result[name] = {
        "data_arrays_identical": True,
        "arrays_compared": len(before.files),
        "baseline_rerender_matches_existing_png_exactly": oldimage.shape == baselineimage.shape and np.array_equal(oldimage, baselineimage),
        "existing_png_shape": list(oldimage.shape),
        "baseline_png_shape": list(baselineimage.shape),
        "minimum_drawn_text_at_465_1pt_width": minimum,
        "visible_text_issues": issues,
        "pdf_sha256": hashlib.sha256((HERE / "repaired_render" / (name + ".pdf")).read_bytes()).hexdigest(),
        "png_sha256": hashlib.sha256((HERE / "repaired_render" / (name + ".png")).read_bytes()).hexdigest(),
    }
(HERE / "verification.json").write_text(json.dumps(result, indent=2))
print(json.dumps(result, indent=2))
