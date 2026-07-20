#!/usr/bin/env python3
"""Detect colliding, clipped and undersized text in a matplotlib figure.

Import and call check(fig) just before savefig. Everything is measured from the
rendered figure, so it catches what the eye catches: labels sitting on top of
each other, annotations running off the canvas, type too small to read at the
size the figure is actually placed at.

    import overlap
    overlap.check(fig, placed_frac=0.85, name="fig_thing")

Returns a list of findings; prints them unless quiet=True. Exit non-zero from a
build script if the list is non-empty and you want collisions to be fatal.
"""
import itertools

import matplotlib as mpl

TEXTWIDTH_PT = 465.1          # a4, margin=2.3cm; override per document
TEXTWIDTH_IN = TEXTWIDTH_PT / 72.0


def _boxes(fig, renderer):
    """Visible, non-empty text objects with their rendered pixel boxes."""
    out = []
    seen = set()
    for t in fig.findobj(mpl.text.Text):
        if id(t) in seen:
            continue
        seen.add(id(t))
        if not t.get_visible() or not t.get_text().strip():
            continue
        # tick labels belonging to an axis whose ticks were switched off are
        # still live Text objects at stale positions; they render nothing
        ax = getattr(t, "axes", None)
        if ax is not None:
            skip = False
            for axis in (ax.xaxis, ax.yaxis):
                labs = axis.get_ticklabels()
                if any(t is l for l in labs) and len(axis.get_ticklocs()) == 0:
                    skip = True
            if skip:
                continue
        try:
            bb = t.get_window_extent(renderer=renderer)
        except Exception:
            continue
        if bb.width <= 0 or bb.height <= 0:
            continue
        out.append((t, bb))
    return out


def _overlap_area(a, b):
    dx = min(a.x1, b.x1) - max(a.x0, b.x0)
    dy = min(a.y1, b.y1) - max(a.y0, b.y0)
    return dx * dy if (dx > 0 and dy > 0) else 0.0


def check(fig, placed_frac=1.0, name="figure", min_pt=6.0, tol=0.18,
          textwidth_in=TEXTWIDTH_IN, quiet=False, check_clipping=False):
    """Report text collisions, clipping and undersized type.

    `tol` is the fraction of the smaller box that must be covered before an
    overlap counts, which tolerates the incidental touching of descenders.
    `min_pt` is the printed size floor, computed from how far the figure is
    squeezed when placed at `placed_frac` of the text width.
    """
    fig.canvas.draw()
    r = fig.canvas.get_renderer()
    items = _boxes(fig, r)
    findings = []

    # how much \includegraphics will shrink this figure
    tb = fig.get_tightbbox(r)
    squeeze = (placed_frac * textwidth_in) / tb.width if tb.width else 1.0

    # 1. collisions
    for (t1, b1), (t2, b2) in itertools.combinations(items, 2):
        # a label and its own axis tick set legitimately share space
        if t1.axes is not None and t1.axes is t2.axes and t1 is t2:
            continue
        a = _overlap_area(b1, b2)
        if a <= 0:
            continue
        small = min(b1.width * b1.height, b2.width * b2.height)
        if small > 0 and a / small > tol:
            findings.append(
                f"COLLISION  {t1.get_text()[:28]!r} x {t2.get_text()[:28]!r} "
                f"({100*a/small:.0f}% of the smaller)")

    # 2. text outside the canvas. Only meaningful when the figure is saved
    # WITHOUT bbox_inches="tight" -- tight expands the saved area to include
    # overhanging tick labels, so this fires constantly and falsely otherwise.
    if check_clipping:
        fw, fh = fig.canvas.get_width_height()
        for t, b in items:
            if b.x0 < -1 or b.y0 < -1 or b.x1 > fw + 1 or b.y1 > fh + 1:
                findings.append(f"CLIPPED    {t.get_text()[:34]!r} runs off the canvas")

    # 3. type too small once placed
    for t, b in items:
        printed = t.get_fontsize() * squeeze
        if printed < min_pt:
            findings.append(
                f"TOO SMALL  {t.get_text()[:28]!r} prints at {printed:.1f} pt")

    if not quiet:
        if findings:
            print(f"  [figcheck] {name}: {len(findings)} issue(s)")
            for f in dict.fromkeys(findings):      # dedupe, keep order
                print(f"      {f}")
        else:
            print(f"  [figcheck] {name}: clean")
    return findings
