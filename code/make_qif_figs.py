"""Two appendix figures from qif_raster.npz:
  fig_qif_raster      -- spike rasters (forced & entrained, field off/on): TI realigns
                         spike timing into the envelope while the mean rate is flat.
  fig_qif_timing      -- (a) QIF population rate vs the exact NMM2 mean field (validation
                         of the QIF<->NMM2 link); (b) fold-change off->on of mean rate
                         vs envelope-locked timing (rate ~flat, timing up).
"""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
FIGS = os.path.join(os.path.dirname(HERE), "figures")
NEBLUE = "#0a4f8c"; NERED = "#b3361f"; NEGREEN = "#1a9850"; GR = "#555555"

d = np.load(os.path.join(HERE, "qif_raster.npz"), allow_pickle=True)
meta = d["meta"].item(); conds = d["conds"].item()
T = meta["T"]; tmeas = meta["t_meas"]; t0 = T - tmeas


def env(t, df):
    return 0.5 * (1 + np.cos(2 * np.pi * df / 1000.0 * t))


def raster_panel(ax, key, title, show_env):
    c = conds[key]; q = c["q"]; df = q["df"]; nrec = q["nrec"]
    st = q["spk_t"]; si = q["spk_id"]
    # smoothed population rate r_E(t) (right axis), drawn first (behind)
    axr = ax.twinx()
    tt = q["ts"]; m = tt >= t0
    dt = meta["dt"]; w = max(1, int(1.5 / dt)); ker = np.ones(w) / w
    re_s = np.convolve(q["re_t"], ker, mode="same")
    axr.fill_between(tt[m] - t0, re_s[m], color=NEBLUE, alpha=0.12, lw=0, zorder=1)
    axr.plot(tt[m] - t0, re_s[m], color=NEBLUE, lw=1.0, alpha=0.9, zorder=2)
    axr.set_ylim(0, max(0.12, re_s[m].max() * 1.25)); axr.set_yticks([])
    if show_env:                                  # TI envelope (scaled to rate axis)
        x = np.linspace(0, tmeas, 600)
        axr.plot(x, 0.5 * axr.get_ylim()[1] * 2 * env(x + t0, df), color=NERED,
                 lw=1.3, alpha=0.55, zorder=3)
    # raster on top
    ax.plot(st - t0, si, "|", color="k", ms=2.6, mew=0.5, alpha=0.85, zorder=5)
    ax.set_xlim(0, tmeas); ax.set_ylim(-2, nrec + 2); ax.set_zorder(axr.get_zorder() + 1)
    ax.patch.set_visible(False)
    ax.set_title(title, fontsize=9)
    return axr


def fig_raster():
    fig, axs = plt.subplots(2, 2, figsize=(10, 6), sharex=True)
    raster_panel(axs[0, 0], "forced_off", "(a) Forced (below Hopf), TI OFF: asynchronous", False)
    raster_panel(axs[0, 1], "forced_on",
                 f"(b) Forced, TI ON ($\\Delta f$={conds['forced_on']['q']['df']:.0f} Hz): timing bunched", True)
    raster_panel(axs[1, 0], "entrain_off", "(c) Entrained (above Hopf), TI OFF: free gamma", False)
    raster_panel(axs[1, 1], "entrain_on",
                 f"(d) Entrained, TI ON ($\\Delta f$={conds['entrain_on']['q']['df']:.0f} Hz): re-timed to TI", True)
    for ax in axs[:, 0]:
        ax.set_ylabel("E neuron #")
    for ax in axs[1, :]:
        ax.set_xlabel("time (ms)")
    fig.suptitle("QIF spiking network (microscale of NMM2 PING): TI realigns spike timing, "
                 "not mean rate\n(black: E spikes; blue: population rate $r_E(t)$; red: TI envelope)",
                 fontsize=10)
    fig.tight_layout(rect=[0, 0, 1, 0.95])
    for ext in ("pdf", "png"):
        fig.savefig(os.path.join(FIGS, f"fig_qif_raster.{ext}"), dpi=150, bbox_inches="tight")
    plt.close(fig)


def fig_timing():
    fig, (axA, axB) = plt.subplots(1, 2, figsize=(10, 3.8))
    # (a) validation: power spectrum of r_E(t), QIF network vs exact NMM2 mean field
    c = conds["forced_on"]; q = c["q"]; dt = meta["dt"]
    m = q["ts"] >= t0; x = q["re_t"][m] - q["re_t"][m].mean()
    fr = np.fft.rfftfreq(len(x), dt / 1000.0); Px = np.abs(np.fft.rfft(x * np.hanning(len(x)))) ** 2
    mm = c["mf_t"] >= t0; y = c["mf_re"][mm] - c["mf_re"][mm].mean()
    fy = np.fft.rfftfreq(len(y), dt / 1000.0); Py = np.abs(np.fft.rfft(y * np.hanning(len(y)))) ** 2
    axA.plot(fr, Px / Px.max(), color=NEBLUE, lw=1.1, label=r"QIF network ($N=%d$)" % meta["Ne"])
    axA.plot(fy, Py / Py.max(), color=NERED, lw=1.4, ls="--", label="NMM2 mean field (exact)")
    axA.set_xlim(0, 130); axA.set_xlabel("frequency (Hz)"); axA.set_ylabel("power (norm.)")
    axA.set_title("(a) QIF $\\to$ NMM2: matched gamma spectrum\n"
                  r"($\langle r_E\rangle$: %.3f QIF vs %.3f mean field)"
                  % (q["rmean"], c["mf_re"][mm].mean()), fontsize=9)
    axA.legend(fontsize=7.5, frameon=False, loc="upper right")
    axA.spines[["top", "right"]].set_visible(False)

    # (b) fold-change off->on: mean rate vs envelope-locked timing
    regimes = [("forced", "Forced"), ("entrain", "Entrained")]
    rate_fc = []; tim_fc = []
    for reg, _ in regimes:
        qo = conds[f"{reg}_off"]["q"]; qn = conds[f"{reg}_on"]["q"]
        rate_fc.append(qn["rmean"] / qo["rmean"])
        tim_fc.append(qn["AC"] / max(qo["AC"], 1e-6))
    x = np.arange(len(regimes)); bw = 0.36
    axB.bar(x - bw / 2, rate_fc, bw, color=GR, label=r"mean rate $\langle r_E\rangle$")
    axB.bar(x + bw / 2, tim_fc, bw, color=NEGREEN, label=r"timing: AC at $\Delta f$")
    axB.axhline(1.0, color="k", lw=0.8, ls=":")
    for xi, (r, t) in enumerate(zip(rate_fc, tim_fc)):
        axB.text(xi - bw / 2, r + 0.05, f"${r:.2f}\\times$", ha="center", fontsize=7.5)
        axB.text(xi + bw / 2, t + 0.05, f"${t:.1f}\\times$", ha="center", fontsize=7.5)
    axB.set_xticks(x); axB.set_xticklabels([n for _, n in regimes])
    axB.set_ylabel("fold change, TI off $\\to$ on")
    axB.set_title("(b) TI multiplies envelope-locked timing,\nnot the mean rate", fontsize=9)
    axB.legend(fontsize=7.5, frameon=False, loc="upper left")
    axB.spines[["top", "right"]].set_visible(False)

    fig.tight_layout()
    for ext in ("pdf", "png"):
        fig.savefig(os.path.join(FIGS, f"fig_qif_timing.{ext}"), dpi=150, bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    fig_raster(); fig_timing()
    print("wrote fig_qif_raster and fig_qif_timing")
    for k in ("forced_off", "forced_on", "entrain_off", "entrain_on"):
        q = conds[k]["q"]
        print(f"  {k:12s}: <r_e>={q['rmean']:.4f}  AC@{q['df']:.0f}={q['AC']:.4f}  spikes={q['spk_t'].size}")
