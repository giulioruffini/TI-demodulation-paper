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
    """Z is already baseline-subtracted (enhancement over the eps=0 row)."""
    x, y = np.asarray(x), np.asarray(y)
    Z = np.clip(Z, 0.0, None)
    vmax = np.percentile(Z, 99.5)
    im = ax.imshow(Z, origin="lower", aspect="auto", interpolation="bilinear",
                   extent=[x[0], x[-1], y[0], y[-1]], cmap="viridis",
                   vmin=0.0, vmax=vmax if vmax > 0 else 1.0)
    ax.axvline(10.0, color="w", ls="--", lw=1)
    figstyle.panel(ax, letter)
    ax.set_xlabel("envelope frequency $\\Delta f$ (Hz)")
    ax.set_ylabel(ylabel)
    plt.colorbar(im, ax=ax, label="alpha enhancement (on$-$off)")


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

    LOCK = (np.abs(F1 - df[None, :]) < 0.3).astype(float)
    if LOCK.any():
        ax[0, 0].contour(df, eps, LOCK, levels=[0.5], colors="w", linewidths=1.4)

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
    print(f"  1:1 capture width: {w[0]:.2f} Hz at eps->0  ->  {w[-1]:.2f} Hz at eps={eps[-1]:.1f} mV")
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
