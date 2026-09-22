"""
Render the LaNMM Arnold-tongue / carrier-map figures from the field-coupled grids
produced by lanmm_field_tongues.py.

Replaces the rate-coupled figures fig_lanmm_arnold_{p1,p2}, which were confounded by
the zero-clip on the external input rate (see the module docstring of
lanmm_field_tongues.py). Layout matches the originals: a 2x2 panel block, P1 and P2
alpha enhancement over the epsilon = 0 baseline, tongue on top and carrier map below,
with the 1:1 frequency-capture contour drawn on panel (a).

Usage:  python make_lanmm_field_figs.py [--wave twotone|am]
"""

import os
import argparse
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import figstyle
figstyle.apply()

HERE = os.path.dirname(os.path.abspath(__file__))
FIGDIR = os.path.join(os.path.dirname(HERE), "figures")


def _imshow(ax, Z, x, y, letter, ylabel):
    """Z is already baseline-subtracted (change over the eps=0 row). Shown SIGNED on a
    zero-centered diverging scale (2026-09-22): the earlier version clipped at zero and
    displayed only the positive part, hiding the suppression that occupies most of the
    P1 grids. Scale limit: 99.5th percentile of |Z|, symmetric."""
    x, y = np.asarray(x), np.asarray(y)
    lim = np.percentile(np.abs(Z), 99.5)
    im = ax.imshow(Z, origin="lower", aspect="auto", interpolation="bilinear",
                   extent=[x[0], x[-1], y[0], y[-1]], cmap="RdBu_r",
                   vmin=-lim if lim > 0 else -1.0, vmax=lim if lim > 0 else 1.0)
    ax.axvline(10.0, color="k", ls="--", lw=1)
    figstyle.panel(ax, letter)
    ax.set_xlabel("envelope frequency $\\Delta f$ (Hz)")
    ax.set_ylabel(ylabel)
    plt.colorbar(im, ax=ax, label="alpha band-power change (on$-$off, a.u.)")


def capture_width(F1, df, eps):
    """1:1 frequency-capture width per amplitude row, in Hz."""
    step = df[1] - df[0]
    out = []
    for i in range(len(eps)):
        cap = np.abs(F1[i] - df) < 0.3
        out.append((df[cap].max() - df[cap].min() + step) if cap.any() else 0.0)
    return np.array(out)


def make(target, wave):
    d = np.load(os.path.join(HERE, f"lanmm_field_{target}_{wave}.npz"))
    Pt1, Pt2, F1 = d["Pt1"], d["Pt2"], d["F1"]
    Pc1, Pc2 = d["Pc1"], d["Pc2"]
    eps, df, fc, eps_c = d["eps"], d["df"], d["fc"], float(d["eps_c"])

    fig, ax = plt.subplots(2, 2, figsize=(11, 9), constrained_layout=True)
    _imshow(ax[0, 0], Pt1, df, eps, "a", "field amplitude $\\varepsilon$ (mV)")
    _imshow(ax[0, 1], Pt2, df, eps, "b", "field amplitude $\\varepsilon$ (mV)")

    # frequency-dominance set |f_out - df| < 0.3 Hz. The eps = 0 row is excluded: with no
    # drive the autonomous alpha (10.667 Hz on this grid) already sits within the tolerance
    # of the 10.5 and 10.75 Hz beat values, which produced a spurious 0.5 Hz "width" at
    # zero drive (review R7, 2026-09-22). This is a dominance screen, not a phase-capture test.
    LOCK = (np.abs(F1 - df[None, :]) < 0.3).astype(float)
    LOCK[0, :] = 0.0
    if LOCK.any():
        ax[0, 0].contour(df, eps, LOCK, levels=[0.5], colors="k", linewidths=1.4)

    _imshow(ax[1, 0], Pc1, df, fc, "c", "carrier frequency $f_c$ (Hz)")
    _imshow(ax[1, 1], Pc2, df, fc, "d", "carrier frequency $f_c$ (Hz)")

    out = f"fig_lanmm_field_{target.lower()}_{wave}"
    os.makedirs(FIGDIR, exist_ok=True)
    figstyle.scale_text(fig, placed_frac=0.86)
    fig.savefig(os.path.join(FIGDIR, out + ".png"), dpi=300)
    fig.savefig(os.path.join(FIGDIR, out + ".pdf"))
    plt.close(fig)

    # numbers quoted in the caption
    w = capture_width(F1, df, eps)
    j = int(np.argmin(np.abs(df - 10.0)))
    print(f"[{target} {wave}]")
    print(f"  tongue peak at eps={eps[-1]:.1f} mV: Delta f = {df[np.argmax(Pt1[-1])]:.2f} Hz")
    print(f"  dominance width (eps=0 row excluded): {w[1]:.2f} Hz at eps={eps[1]:.2f} mV  ->  {w[-1]:.2f} Hz at eps={eps[-1]:.1f} mV;"
          f"  grid step {df[1]-df[0]:.3f} Hz, autonomous f_out at eps=0: {np.unique(np.round(F1[0],3))}")
    for nm_, Z in (("Pt1", Pt1), ("Pt2", Pt2), ("Pc1", Pc1), ("Pc2", Pc2)):
        print(f"  {nm_}: min {Z.min():.3g}, max {Z.max():.3g}, negative fraction {np.mean(Z < 0):.2f}")
    print(f"  carrier-map peak at Delta f=10 Hz: f_c = {fc[np.argmax(Pc1[:, j])]:.1f} Hz  (map at eps={eps_c} mV)")
    print(f"  wrote {out}.pdf/.png")
    return w


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--wave", default="twotone", choices=["twotone", "am", "both"])
    a = ap.parse_args()
    waves = ["twotone", "am"] if a.wave == "both" else [a.wave]
    for w in waves:
        for tgt in ["P2", "P1"]:
            p = os.path.join(HERE, f"lanmm_field_{tgt}_{w}.npz")
            if os.path.exists(p):
                make(tgt, w)
            else:
                print(f"  (skipping {tgt} {w}: {os.path.basename(p)} not yet written)")
