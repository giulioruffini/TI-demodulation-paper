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


def panel(ax, letter, x=-0.015, y=1.04, fontsize=12.5):
    """Bold panel label, e.g. panel(ax, 'a') -> '(a)' at the axis top-left."""
    ax.text(x, y, f"({letter})", transform=ax.transAxes, fontweight="bold",
            fontsize=fontsize, va="bottom", ha="right")
