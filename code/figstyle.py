"""Shared house figure style for TN0484 (Neuroelectrics).

Usage at the top of any figure script:
    import figstyle; figstyle.apply()
    ... use figstyle.NEBLUE / NERED / NEGREEN ...
    figstyle.panel(ax, "a")        # bold (a) label, top-left of an axis

Keeps the 24-figure set coherent: one palette, consistent type sizes, 300-dpi
output, clean spines. Importing does nothing until apply() is called, so scripts
that set their own rcParams are unaffected unless they opt in.
"""
import matplotlib as mpl

# --- page geometry -------------------------------------------------------
# The manuscript is a4 with margin=2.3cm, so \textwidth = 465.1 pt = 6.46 in.
# Figures are drawn on canvases much wider than that and then squeezed by
# \includegraphics, which scales the type down with everything else. A figure
# drawn 13.5 in wide and placed at \textwidth prints its 9.5 pt ticks at 4.5 pt.
# IOP requires 8-12 pt at final size, so the type has to be pre-enlarged by the
# reciprocal of that squeeze. See scale_text().
TEXTWIDTH_PT = 465.1
TEXTWIDTH_IN = TEXTWIDTH_PT / 72.0

# --- house palette ---
NEBLUE   = "#0a4f8c"     # primary
NERED    = "#b3361f"     # contrast / theory overlay
NEGREEN  = "#1a9850"     # third series (timing)
NEGRAY   = "#555555"     # neutral / secondary
NEBLUE_L = "#9ec9e8"     # light fill (oscillation range, shaded bands)
NEORANGE = "#e08214"     # fourth series
NEPURPLE = "#6a51a3"     # fifth series
CYCLE    = [NEBLUE, NERED, NEGREEN, NEORANGE, NEPURPLE, NEGRAY]


def apply():
    """Install the house rcParams (call once per script, before plotting)."""
    mpl.rcParams.update({
        "figure.dpi":       120,
        "savefig.dpi":      300,
        "savefig.bbox":     "tight",
        "font.family":      "sans-serif",
        "font.size":        11.0,
        "axes.titlesize":   11.0,
        "axes.labelsize":   11.0,
        "xtick.labelsize":  9.5,
        "ytick.labelsize":  9.5,
        "legend.fontsize":  9.0,
        "legend.frameon":   False,
        "axes.linewidth":   0.8,
        "lines.linewidth":  1.7,
        "lines.solid_capstyle": "round",
        "axes.spines.top":   False,
        "axes.spines.right": False,
        "axes.prop_cycle":   mpl.cycler(color=CYCLE),
        "grid.alpha":        0.3,
        "grid.linewidth":    0.6,
    })


def scale_text(fig, placed_frac=1.0, target_min_pt=8.5, max_scale=2.2, verbose=False):
    """Pre-enlarge every text object so it prints at journal size.

    Call once, immediately before savefig. `placed_frac` is the fraction of
    \\textwidth the figure is placed at in the manuscript, i.e. the number in
    \\includegraphics[width=0.85\\textwidth]{...}.

    Walks the whole figure, so it catches hardcoded ax.text(fontsize=...) calls
    as well as anything inherited from rcParams. Returns the factor applied.
    Never shrinks: a figure already at or below \\textwidth is left alone.

    Idempotent: calling it twice on the same figure does nothing the second
    time, so a call left inside a save loop cannot compound the scaling.

    Enlarging the type also enlarges the tight bounding box, which increases the
    squeeze and eats part of the gain, so this iterates against the measured box
    rather than applying one open-loop factor.
    """
    if getattr(fig, "_figstyle_text_scaled", False):
        return 1.0
    fig._figstyle_text_scaled = True

    texts = list({id(t): t for t in fig.findobj(mpl.text.Text)}.values())
    texts = [t for t in texts if t.get_text().strip()]
    if not texts:
        return 1.0

    total = 1.0
    for _ in range(12):
        fig.canvas.draw()
        bb = fig.get_tightbbox(fig.canvas.get_renderer())
        squeeze = (placed_frac * TEXTWIDTH_IN) / bb.width   # <1 when downscaled
        smallest_printed = min(t.get_fontsize() for t in texts) * squeeze
        if smallest_printed >= target_min_pt:
            break
        step = min(target_min_pt / smallest_printed, 1.35)   # damped
        if total * step > max_scale:                         # refuse to run away
            step = max(max_scale / total, 1.0)
            if step <= 1.0:
                break
        for t in texts:
            t.set_fontsize(t.get_fontsize() * step)
        total *= step
        if total >= max_scale:
            break
    if smallest_printed < target_min_pt:
        # Not a settings problem: the figure holds more lettering than the text
        # block can carry, and growing type only grows the bounding box with it.
        print(f"  figstyle WARNING: smallest type still prints at "
              f"{smallest_printed:.1f} pt (target {target_min_pt}); this figure "
              f"needs content removed, not larger type.")
    if verbose:
        print(f"  figstyle: type scaled x{total:.2f} "
              f"-> smallest prints at {smallest_printed:.1f} pt")
    return total


def panel(ax, letter, x=-0.015, y=1.04, fontsize=12.5):
    """Bold panel label, e.g. panel(ax, 'a') -> '(a)' at the axis top-left."""
    ax.text(x, y, f"({letter})", transform=ax.transAxes, fontweight="bold",
            fontsize=fontsize, va="bottom", ha="right")
