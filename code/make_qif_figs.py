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
from matplotlib.ticker import MaxNLocator

HERE = os.path.dirname(os.path.abspath(__file__))
FIGS = os.environ.get("TN_FIGDIR") or os.path.join(os.path.dirname(HERE), "figures")
os.makedirs(FIGS, exist_ok=True)
NEBLUE = "#0a4f8c"; NERED = "#b3361f"; NEGREEN = "#1a9850"; GR = "#555555"


d = np.load(os.path.join(HERE, "qif_raster.npz"), allow_pickle=True)
meta = d["meta"].item(); conds = d["conds"].item()
T = meta["T"]; tmeas = meta["t_meas"]; t0 = T - tmeas


def env(t, df):
    return 0.5 * (1 + np.cos(2 * np.pi * df / 1000.0 * t))


def cycle_avg(re_t, ts, df, nbin=20):
    """Population rate folded onto the TI-beat (Df) phase over the measure window.
    Flat for a free/asynchronous network; a clear bump when timing locks to the beat."""
    m = ts >= t0; t = ts[m]; re = re_t[m]
    ph = (df / 1000.0 * t) % 1.0
    bins = np.linspace(0, 1, nbin + 1); idx = np.clip(np.digitize(ph, bins) - 1, 0, nbin - 1)
    out = np.array([re[idx == k].mean() if (idx == k).any() else np.nan for k in range(nbin)])
    ker = np.array([1.0, 2.0, 1.0]); ker /= ker.sum()        # light circular smooth
    out = np.convolve(np.r_[out[-1], out, out[0]], ker, mode="same")[1:-1]
    return 0.5 * (bins[:-1] + bins[1:]), out


def gamma_amp_fold(re_t, ts, df, dt, band=(45.0, 70.0), nbin=24, t_start=40.0):
    """Fold the GAMMA-band amplitude envelope of r_E on the Df beat phase (proper PAC).
    Taking the gamma *amplitude* discards the gamma carrier, so the curve is immune to the
    near-commensurability of gamma(~53~Hz) and beat(42~Hz) that contaminates a raw r_E
    fold. Flat across beat phase for a free gamma (off); a clear Df-locked bump when the
    beat gates the gamma amplitude (on)."""
    m = ts >= t_start; t = ts[m]; x = re_t[m] - re_t[m].mean()
    n = len(x); fs = 1000.0 / dt                              # dt in ms -> sample rate (Hz)
    X = np.fft.rfft(x); f = np.fft.rfftfreq(n, 1.0 / fs)      # FFT band-pass around gamma
    X[(f < band[0]) | (f > band[1])] = 0.0
    xb = np.fft.irfft(X, n)
    Xa = np.fft.fft(xb); H = np.zeros(n); H[0] = 1.0          # analytic signal (Hilbert via FFT)
    if n % 2 == 0:
        H[n // 2] = 1.0; H[1:n // 2] = 2.0
    else:
        H[1:(n + 1) // 2] = 2.0
    amp = np.abs(np.fft.ifft(Xa * H))                         # gamma amplitude envelope
    ph = (df / 1000.0 * t) % 1.0                              # beat phase
    bins = np.linspace(0, 1, nbin + 1); idx = np.clip(np.digitize(ph, bins) - 1, 0, nbin - 1)
    out = np.array([amp[idx == k].mean() if (idx == k).any() else np.nan for k in range(nbin)])
    ker = np.array([1.0, 2.0, 1.0]); ker /= ker.sum()
    out = np.convolve(np.r_[out[-1], out, out[0]], ker, mode="same")[1:-1]
    return 0.5 * (bins[:-1] + bins[1:]), out


def beat_inset(ax, off_key, on_key, mode="rate"):
    """Inset folded on the Df beat phase, TI off (flat) vs on (bump). mode='rate' folds the
    raw r_E (forced case: the response is at Df); mode='gamma' folds the gamma-amplitude
    envelope (gating case: PAC of the persisting gamma). Both curves are normalized to their
    own mean, so the y-axis reads the relative (depth) modulation -- dimensionless and
    directly comparable to the boxed Df modulation depth."""
    df = conds[on_key]["q"]["df"]; dt = meta["dt"]
    iax = ax.inset_axes([0.605, 0.55, 0.375, 0.42])
    for k, col, lab in ((off_key, GR, "off"), (on_key, NEBLUE, "on")):
        q = conds[k]["q"]
        if mode == "gamma":
            ctr, ca = gamma_amp_fold(q["re_t"], q["ts"], df, dt)
        else:
            ctr, ca = cycle_avg(q["re_t"], q["ts"], df)
        ca = ca / ca.mean()                                  # normalize -> relative modulation
        iax.plot(np.r_[ctr, ctr + 1], np.r_[ca, ca], color=col, lw=1.4, label=lab)
    iax.set_xticks([0, 1, 2]); iax.set_xticklabels(["0", "1", "2"])
    iax.set_xlabel(r"$\Delta f$ phase (cycles)", fontsize=6.0, labelpad=1)
    ylab = r"$\gamma$ amp. (norm.)" if mode == "gamma" else r"$r_E$ (norm.)"
    iax.set_ylabel(ylab, fontsize=6.0, labelpad=1)
    iax.yaxis.set_major_locator(MaxNLocator(3))
    iax.tick_params(length=2, pad=1, labelsize=5.4)
    iax.legend(fontsize=5.2, frameon=False, loc="upper right", ncol=2,
               handlelength=0.9, columnspacing=0.8, handletextpad=0.4, borderpad=0.1)
    iax.patch.set_alpha(0.92)
    return iax


def raster_panel(ax, key, title, show_env, annot=None):
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
    ax.plot(st - t0, si, "|", color="k", ms=1.7, mew=0.35, alpha=0.7, zorder=5)
    ax.set_xlim(0, tmeas); ax.set_ylim(-2, nrec + 2); ax.set_zorder(axr.get_zorder() + 1)
    ax.patch.set_visible(False)
    if annot:                                     # quantify the envelope-locked timing
        ax.text(0.025, 0.96, annot, transform=ax.transAxes, fontsize=7.6, va="top",
                color=NEGREEN, fontweight="bold",
                bbox=dict(fc="white", ec=NEGREEN, lw=0.6, alpha=0.85, pad=1.6))
    ax.set_title(title, fontsize=9)
    return axr


def fig_raster():
    fig, axs = plt.subplots(2, 2, figsize=(10, 6), sharex=True)
    depth = {k: conds[k]["q"]["AC"] / conds[k]["q"]["rmean"]
             for k in ("forced_off", "forced_on", "entrain_off", "entrain_on")}
    raster_panel(axs[0, 0], "forced_off", "(a) Forced (below Hopf), TI OFF: asynchronous", False,
                 annot="no $\\Delta f$ lock-in\n(depth %.2f)" % depth["forced_off"])
    raster_panel(axs[0, 1], "forced_on",
                 f"(b) Forced, TI ON ($\\Delta f$={conds['forced_on']['q']['df']:.0f} Hz): timing bunched",
                 True, annot="$\\Delta f$ modulation\ndepth %.2f" % depth["forced_on"])
    raster_panel(axs[1, 0], "entrain_off",
                 "(c) Oscillatory (above Hopf), TI OFF: free-running gamma", False,
                 annot="no $\\Delta f$ lock-in\n(depth %.2f)" % depth["entrain_off"])
    raster_panel(axs[1, 1], "entrain_on",
                 f"(d) Oscillatory, TI ON ($\\Delta f$={conds['entrain_on']['q']['df']:.0f} Hz):"
                 " TI beat gates the gamma ($\\Delta f$-PAC)",
                 True, annot="$\\Delta f$ modulation\ndepth %.2f" % depth["entrain_on"])
    beat_inset(axs[0, 1], "forced_off", "forced_on")                    # forced: rate folded on Df
    beat_inset(axs[1, 1], "entrain_off", "entrain_on", mode="gamma")    # gating: gamma amp vs Df phase (PAC)
    for ax in axs[:, 0]:
        ax.set_ylabel("E neuron #")
    for ax in axs[1, :]:
        ax.set_xlabel("time (ms)")
    fig.suptitle("QIF spiking network (microscale of NMM2 PING): TI realigns spike timing, "
                 "not mean rate\n(black: E spikes; blue: population rate $r_E(t)$; red: TI envelope; "
                 "boxed: $\\Delta f$ modulation depth $A_\\Omega/\\langle r_E\\rangle$)",
                 fontsize=10)
    fig.tight_layout(rect=[0, 0, 1, 0.95])
    for ext in ("pdf", "png"):
        fig.savefig(os.path.join(FIGS, f"fig_qif_raster.{ext}"), dpi=300, bbox_inches="tight")
    plt.close(fig)


def _rate_spectrum(re_t, ts, dt, t_start=60.0):
    """Hann-windowed power spectrum of r_E(t) over the post-settle tail."""
    m = ts >= t_start; x = re_t[m] - re_t[m].mean()
    f = np.fft.rfftfreq(len(x), dt / 1000.0)
    P = np.abs(np.fft.rfft(x * np.hanning(len(x)))) ** 2
    return f, P / P.max()


def fig_timing():
    fig, (axA, axC, axB) = plt.subplots(1, 3, figsize=(13.6, 3.7))
    # (a) validation: power spectrum of r_E(t), QIF network vs exact NMM2 mean field.
    # Use the field-free autonomous gamma (entrain_off): a single clean peak in both, so the
    # QIF<->NMM2 match is unambiguous. (Under strong TI forcing the forced spectrum is multi-
    # peak and the "dominant" peak is window-sensitive -- a poor validation condition.)
    c = conds["entrain_off"]; q = c["q"]; dt = meta["dt"]
    m = q["ts"] >= t0; x = q["re_t"][m] - q["re_t"][m].mean()
    fr = np.fft.rfftfreq(len(x), dt / 1000.0); Px = np.abs(np.fft.rfft(x * np.hanning(len(x)))) ** 2
    mm = c["mf_t"] >= t0; y = c["mf_re"][mm] - c["mf_re"][mm].mean()
    fy = np.fft.rfftfreq(len(y), dt / 1000.0); Py = np.abs(np.fft.rfft(y * np.hanning(len(y)))) ** 2
    axA.plot(fr, Px / Px.max(), color=NEBLUE, lw=1.1, label=r"QIF network ($N=%d$)" % meta["Ne"])
    axA.plot(fy, Py / Py.max(), color=NERED, lw=1.4, ls="--", label="NMM2 mean field (exact)")
    axA.set_xlim(0, 130); axA.set_xlabel("frequency (Hz)"); axA.set_ylabel("power (norm.)")
    axA.set_title("(a) QIF $\\to$ NMM2: matched autonomous gamma\n"
                  r"($\langle r_E\rangle$: %.3f QIF vs %.3f mean field)"
                  % (q["rmean"], c["mf_re"][mm].mean()), fontsize=9)
    axA.legend(fontsize=7.5, frameon=False, loc="upper right")
    axA.spines[["top", "right"]].set_visible(False)

    # (b) intermodulation: oscillatory regime, TI off vs on. The nonlinearity mixes the
    # imposed Df=42 Hz beat with the intrinsic ~53 Hz gamma -> sidebands. TI-on lights up
    # the direct Df line (42) and the SUM 53+42=95; the difference 53-42=11 is weak. This is
    # the spiking-network view of the macroscale frequency mixing (sideband = gating).
    dfb = conds["entrain_on"]["q"]["df"]; fg = 53.0
    for key, col, lab in (("entrain_off", GR, "TI off"), ("entrain_on", NEBLUE, "TI on")):
        qq = conds[key]["q"]; fS, PS = _rate_spectrum(qq["re_t"], qq["ts"], dt)
        axC.semilogy(fS, PS, color=col, lw=1.2, label=lab)
    # Mark only the lines the figure can stand behind: the direct Df line and the SUM
    # sideband. The difference tone f0-Df sits at the noise floor (its small amplitude is
    # set by the network transfer function, not the mixer), so we do not flag it.
    for fr, txt in ((dfb, r"$\Delta f$"), (fg, r"$f_0$"), (fg + dfb, r"$f_0{+}\Delta f$")):
        axC.axvline(fr, ls=":", color=NERED, lw=0.8, alpha=0.7)
        axC.text(fr, 1.5, txt, rotation=90, fontsize=7, color=NERED, ha="right", va="bottom")
    axC.set_xlim(0, 120); axC.set_ylim(1e-4, 4)
    axC.set_xlabel("frequency (Hz)"); axC.set_ylabel("power of $r_E$ (norm.)")
    axC.set_title("(b) Oscillatory: nonlinear mixing of\n"
                  r"$\Delta f$ and $f_0$ $\to$ intermodulation sidebands", fontsize=9)
    axC.legend(fontsize=7.5, frameon=False, loc="lower right")
    axC.spines[["top", "right"]].set_visible(False)

    # (c) Df modulation depth = AC(Df)/<r_E> -- a STABLE off->on metric: the amplitude
    # of the Df-locked rate oscillation as a fraction of the mean rate. Both quantities
    # are well-estimated, unlike the off/on lock-in RATIO whose denominator sits at the
    # near-zero noise floor (and so is realization-noisy). Mean rate flatness shown as text.
    regimes = [("forced", "Forced"), ("entrain", "Oscillatory")]
    depth_off = []; depth_on = []; rate_fc = []
    for reg, _ in regimes:
        qo = conds[f"{reg}_off"]["q"]; qn = conds[f"{reg}_on"]["q"]
        depth_off.append(qo["AC"] / qo["rmean"])
        depth_on.append(qn["AC"] / qn["rmean"])
        rate_fc.append(qn["rmean"] / qo["rmean"])
    x = np.arange(len(regimes)); bw = 0.36
    axB.bar(x - bw / 2, depth_off, bw, color=GR, label="TI off")
    axB.bar(x + bw / 2, depth_on, bw, color=NEGREEN, label="TI on")
    for xi in range(len(regimes)):
        axB.text(xi - bw / 2, depth_off[xi] + 0.012, f"{depth_off[xi]:.2f}", ha="center", fontsize=7.5)
        axB.text(xi + bw / 2, depth_on[xi] + 0.012, f"{depth_on[xi]:.2f}", ha="center", fontsize=7.5,
                 color=NEGREEN, fontweight="bold")
    axB.text(0.5, 0.90, r"mean rate $\langle r_E\rangle$ flat (off$\to$on $\times$%.2f, $\times$%.2f)"
             % (rate_fc[0], rate_fc[1]), transform=axB.transAxes, ha="center", fontsize=8, color=GR)
    axB.set_xticks(x); axB.set_xticklabels([n for _, n in regimes])
    axB.set_ylabel(r"$\Delta f$ modulation depth  ($A_\Omega/\langle r_E\rangle$)")
    axB.set_title("(c) TI imposes $\\Delta f$-locked timing, not rate", fontsize=9)
    axB.legend(fontsize=7.5, frameon=False, loc="upper left")
    axB.set_ylim(0, max(depth_on) * 1.18)
    axB.spines[["top", "right"]].set_visible(False)

    fig.tight_layout()
    for ext in ("pdf", "png"):
        fig.savefig(os.path.join(FIGS, f"fig_qif_timing.{ext}"), dpi=300, bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    fig_raster(); fig_timing()
    print("wrote fig_qif_raster and fig_qif_timing")
    for k in ("forced_off", "forced_on", "entrain_off", "entrain_on"):
        q = conds[k]["q"]
        print(f"  {k:12s}: <r_e>={q['rmean']:.4f}  AC@{q['df']:.0f}={q['AC']:.4f}  spikes={q['spk_t'].size}")
