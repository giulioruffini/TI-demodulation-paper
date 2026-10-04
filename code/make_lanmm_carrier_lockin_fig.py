"""
Render the phase-sensitive LaNMM carrier maps produced by lanmm_carrier_lockin.py
(review item R6). One figure per window length: for each drive target (P2 at 1.5 mV,
P1 at 0.5 mV), the lock-in amplitude of v_P1 at Delta f over (f_c, Delta f), the
band-power change (the quantity in the published maps), and the per-carrier ridge
of the lock-in with the field-free leakage floor. Captured grid points (dominant
output frequency within 0.3 Hz of Delta f) are hatched. Output goes to docs/, not to
figures/: this is review evidence, not a manuscript figure.

Usage: python make_lanmm_carrier_lockin_fig.py [--tag _tmeas10]
"""
import os, argparse
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
DOCS = os.path.join(os.path.dirname(HERE), "docs")


def main(tag):
    fig, ax = plt.subplots(2, 3, figsize=(14, 8), constrained_layout=True)
    for r, tgt in enumerate(("P2", "P1")):
        o = np.load(os.path.join(HERE, f"lanmm_carrier_lockin_{tgt}_twotone{tag}.npz"))
        fc, df, L1, Pc1, F1c, L1b = o["fc"], o["df"], o["L1"], o["Pc1"], o["F1c"], o["L1_base"]
        ext = [df[0], df[-1], fc[0], fc[-1]]
        cap = np.abs(F1c - df[None, :]) < 0.3
        a = ax[r, 0]
        im = a.imshow(L1, origin="lower", aspect="auto", extent=ext, cmap="viridis")
        a.contourf(df, fc, cap.astype(float), levels=[0.5, 1.5], colors="none", hatches=["//"])
        a.axvline(float(o["f_alpha_base"]), color="w", ls=":", lw=1)
        plt.colorbar(im, ax=a, label="lock-in amplitude of $v_{P1}$ at $\\Delta f$ (mV)")
        a.set_title(f"{tgt} drive, $\\varepsilon$={float(o['eps_c'])} mV: lock-in (hatched = dominance-captured)")
        a.set_xlabel("$\\Delta f$ (Hz)"); a.set_ylabel("$f_c$ (Hz)")
        a = ax[r, 1]
        lim = np.percentile(np.abs(Pc1), 99.5)
        im = a.imshow(Pc1, origin="lower", aspect="auto", extent=ext, cmap="RdBu_r", vmin=-lim, vmax=lim)
        plt.colorbar(im, ax=a, label="alpha band-power change (on$-$off, a.u.)")
        a.set_title("band power (as in the published maps)")
        a.set_xlabel("$\\Delta f$ (Hz)"); a.set_ylabel("$f_c$ (Hz)")
        a = ax[r, 2]
        ridge = L1.max(axis=1)
        near = np.abs(df - float(o["f_alpha_base"])) <= 1.0 / float(o["t_meas"])
        L1_free = np.where(cap | near[None, :], -np.inf, L1)
        ridge_free = L1_free.max(axis=1)
        a.plot(fc, ridge, "k-", label="max over $\\Delta f$ (all)")
        a.plot(fc, ridge_free, "C0-", label="max over $\\Delta f$, excluding captured\nand leakage-prone beats")
        a.axhline(L1b.max(), color="C3", ls="--", label=f"field-free leakage floor (max over $\\Delta f$ = {L1b.max():.2f} mV)")
        a.set_xlabel("$f_c$ (Hz)"); a.set_ylabel("lock-in amplitude (mV)"); a.set_ylim(bottom=0)
        a.legend(fontsize=8, loc="best"); a.set_title("per-carrier ridge")
    fig.suptitle(f"LaNMM carrier dependence read with the lock-in at $\\Delta f$ (two tones, "
                 f"window {float(o['t_meas']):.0f} s, settle {float(o['t_settle']):.0f} s)")
    os.makedirs(DOCS, exist_ok=True)
    out = os.path.join(DOCS, f"r6_lanmm_carrier_lockin{tag}.png")
    fig.savefig(out, dpi=150); plt.close(fig); print("wrote", out)


if __name__ == "__main__":
    ap = argparse.ArgumentParser(); ap.add_argument("--tag", default="")
    main(ap.parse_args().tag)
