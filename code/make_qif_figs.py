"""QIF spike rasters, spectra, and beat-locked rate modulation from cached runs.

The main figure uses field-free stable and oscillatory states with TI off/on. The timing
figure compares spectra and rate-modulation depth. Raw rate folding and sidebands
do not establish modulation of the autonomous gamma amplitude.
"""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import figstyle
import overlap

HERE = os.path.dirname(os.path.abspath(__file__))
FIGS = os.environ.get("TN_FIGDIR") or os.path.join(os.path.dirname(HERE), "figures")
os.makedirs(FIGS, exist_ok=True)
NEBLUE = "#0a4f8c"; NERED = "#b3361f"; NEGREEN = "#1a9850"; GR = "#555555"


# Prefer the genuine two-tone run when present: spiking/threshold dynamics are
# exactly where the AM surrogate and physical TI cannot be assumed equivalent.
_SRC = os.environ.get("QIF_SRC") or ("qif_raster_twotone.npz" if os.path.exists(
    os.path.join(HERE, "qif_raster_twotone.npz")) else "qif_raster.npz")
# QIF_SRC / QIF_TAG (review branch, 2026-10-05): render an alternative cache, e.g. the
# amplitude-10 runs of qif_raster_amp.py, under its own figure tag.
_TAG = os.environ.get("QIF_TAG") or ("_twotone" if "twotone" in _SRC else "")
print(f"  source: {_SRC}")
d = np.load(os.path.join(HERE, _SRC), allow_pickle=True)
meta = d["meta"].item(); conds = d["conds"].item()
# Cache layout: since 2026-09-22 each condition carries its own T, t_meas (integer number of
# beat cycles) and kmeas; older caches had one global window. Resolve per condition.
def _win(key):
    q = conds[key]["q"]
    if "T" in q:
        return float(q["T"]), float(q["t_meas"])
    return float(meta["T"]), float(meta["t_meas"])
T, tmeas = _win(next(iter(conds)))
t0 = float(meta.get("T_settle", T - tmeas))
DISPLAY_END = min(_win(k)[1] for k in conds)
DISPLAY_START = max(0.0, DISPLAY_END - 200.0)


def env(t, df):
    return 0.5 * (1 + np.cos(2 * np.pi * df / 1000.0 * t))


def cycle_avg(re_t, ts, df, nbin=20, t_start=None):
    """Population rate folded onto the TI-beat (Df) phase over the measure window.
    Non-beat-locked activity is suppressed, not necessarily canceled in a finite window."""
    m = ts >= (t0 if t_start is None else t_start); t = ts[m]; re = re_t[m]
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
    """Inset folded on the Df beat phase. mode='rate' folds the
    raw r_E; mode='gamma' folds the gamma-amplitude
    envelope (an optional diagnostic, not used in the paper). Both curves are normalized to their
    own mean, so the y-axis reads the relative (depth) modulation -- dimensionless and
    comparable across the two conditions. It does not show the full rate excursion."""
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
    iax.set_xlabel(r"$\Delta f$ phase (cycles)", fontsize=9.0, labelpad=1, fontweight="bold")
    ylab = r"$\gamma$ amp. (norm.)" if mode == "gamma" else r"$\langle r_E\rangle_\phi/\bar r_E$"
    iax.set_ylabel(ylab, fontsize=9.0, labelpad=1, fontweight="bold")
    iax.set_ylim(0, 2)
    iax.set_yticks([0, 1, 2])
    iax.tick_params(length=2, pad=1, labelsize=7.0, direction="in")
    # the inset's tick/axis labels fall on the busy raster; a white halo keeps
    # them legible without an opaque backing box
    halo = dict(fc="white", ec="none", alpha=0.85, pad=0.4)
    for t in list(iax.get_xticklabels()) + list(iax.get_yticklabels()):
        t.set_fontweight("bold"); t.set_bbox(halo)
    iax.xaxis.label.set_bbox(halo); iax.yaxis.label.set_bbox(halo)
    iax.legend(fontsize=9.0, frameon=False, loc="upper right", ncol=2,
               handlelength=0.9, columnspacing=0.8, handletextpad=0.4, borderpad=0.1)
    iax.patch.set_alpha(1.0); iax.patch.set_facecolor("white")
    for sp in iax.spines.values():
        sp.set_zorder(6)
    iax.set_zorder(6)
    return iax


def raster_panel(ax, key, title, show_env, annot=None):
    global T, tmeas, t0
    T, tmeas = _win(key); t0 = float(meta.get("T_settle", T - tmeas))
    c = conds[key]; q = c["q"]; df = q["df"]; nrec = q["nrec"]
    st = q["spk_t"]; si = q["spk_id"]
    # smoothed population rate r_E(t) (right axis), drawn first (behind)
    axr = ax.twinx()
    tt = q["ts"]; measured = tt >= t0
    # Store only the visible time interval in the figure; all measurements and folds
    # still use the complete cached window. Padding preserves the curve at the axes.
    m = (tt >= t0 + DISPLAY_START - 1) & (tt <= t0 + DISPLAY_END + 1)
    dt = meta["dt"]; w = max(1, int(1.5 / dt)); ker = np.ones(w) / w
    re_s = np.convolve(q["re_t"], ker, mode="same")
    axr.fill_between(tt[m] - t0, re_s[m], color=NEBLUE, alpha=0.12, lw=0,
                     zorder=1, rasterized=True)
    axr.plot(tt[m] - t0, re_s[m], color=NEBLUE, lw=1.0, alpha=0.9, zorder=2)
    axr.set_ylim(0, max(0.12, re_s[measured].max() * 1.25)); axr.set_yticks([])
    if show_env:                                  # TI envelope (scaled to rate axis)
        x = np.linspace(0, tmeas, 600)
        axr.plot(x, 0.5 * axr.get_ylim()[1] * 2 * env(x + t0, df), color=NERED,
                 lw=1.3, alpha=0.55, zorder=3)
    # raster on top
    shown = (st >= t0 + DISPLAY_START) & (st <= t0 + DISPLAY_END)
    ax.plot(st[shown] - t0, si[shown], "|", color="k", ms=1.7, mew=0.35,
            alpha=0.7, zorder=5, rasterized=True)
    # show the last ZOOM ms of the measurement window (the folds and metrics use all of it)
    ax.set_ylim(-2, nrec + 2); ax.set_zorder(axr.get_zorder() + 1)
    ax.patch.set_visible(False)
    if annot:                                     # quantify the envelope-locked timing
        ax.text(0.025, 0.96, annot, transform=ax.transAxes, fontsize=9.0, va="top",
                color=NEGREEN, fontweight="bold",
                bbox=dict(fc="white", ec=NEGREEN, lw=0.6, alpha=0.85, pad=1.6))
    figstyle.panel(ax, title.strip("()"))
    return axr


def fig_raster():
    fig, axs = plt.subplots(2, 2, figsize=(10, 6), sharex=True)
    raster_panel(axs[0, 0], "forced_off", "(a)", False)
    raster_panel(axs[0, 1], "forced_on",
                 "(b)", True)
    raster_panel(axs[1, 0], "entrain_off",
                 "(c)", False)
    raster_panel(axs[1, 1], "entrain_on",
                 "(d)", True)
    beat_inset(axs[0, 1], "forced_off", "forced_on")
    # 2026-09-22 (review R7): the gamma-amplitude estimator (45-70 Hz band-pass + Hilbert,
    # fold from 40 ms) removed the 11 and 95 Hz sidebands that carry the envelope and
    # included the settling interval. The inset now folds the population rate over the
    # measurement window, as in (b); with 34 beat cycles the near-commensurate 53 Hz gamma
    # is strongly suppressed in the 42 Hz fold. Sidebands alone do not establish gamma-amplitude gating.
    beat_inset(axs[1, 1], "entrain_off", "entrain_on", mode="rate")
    for ax in axs[:, 0]:
        ax.set_ylabel("E neuron #")
    # show the last ZOOM ms common to all windows (folds and metrics use the whole window)
    axs[0, 0].set_xlim(DISPLAY_START, DISPLAY_END)
    for ax in axs[1, :]:
        ax.set_xlabel("time in the measurement window (ms)")
    fig.tight_layout(w_pad=2.8, h_pad=2.0)
    figstyle.thin_ticks(fig)
    for ax in axs.flat:
        ax.set_xticks(np.linspace(DISPLAY_START, DISPLAY_END, 6))
        ax.set_yticks([0, 100, 200, 300, 400])
    figstyle.scale_text(fig, placed_frac=1)
    overlap.check(fig, placed_frac=1, name="fig_qif_raster")
    for ext in ("pdf", "png"):
        fig.savefig(os.path.join(FIGS, f"fig_qif_raster{_TAG}.{ext}"),
                    dpi=450 if ext == "pdf" else 300, bbox_inches="tight")
    plt.close(fig)


def _rate_spectrum(re_t, ts, dt, t_start):
    """Hann-windowed power spectrum of r_E(t) over the post-settle tail."""
    m = ts >= t_start; x = re_t[m] - re_t[m].mean()
    f = np.fft.rfftfreq(len(x), dt / 1000.0)
    P = np.abs(np.fft.rfft(x * np.hanning(len(x)))) ** 2
    return f, P / P.max()


def fig_timing():
    fig, (axA, axC, axB) = plt.subplots(1, 3, figsize=(13.6, 3.7))
    # (a) validation: power spectrum of r_E(t), QIF network vs exact NMM2 mean field.
    # Use the field-free autonomous gamma (entrain_off): a single clean peak in both, so the
    # QIF<->NMM2 comparison uses the field-free state. (Under strong TI forcing the spectrum is multi-
    # peak and the "dominant" peak is window-sensitive -- a poor validation condition.)
    c = conds["entrain_off"]; q = c["q"]; dt = meta["dt"]
    m = q["ts"] >= t0; x = q["re_t"][m] - q["re_t"][m].mean()
    fr = np.fft.rfftfreq(len(x), dt / 1000.0); Px = np.abs(np.fft.rfft(x * np.hanning(len(x)))) ** 2
    mm = c["mf_t"] >= t0; y = c["mf_re"][mm] - c["mf_re"][mm].mean()
    fy = np.fft.rfftfreq(len(y), dt / 1000.0); Py = np.abs(np.fft.rfft(y * np.hanning(len(y)))) ** 2
    axA.plot(fr, Px / Px.max(), color=NEBLUE, lw=1.1, label=r"QIF network ($N=%d$)" % meta["Ne"])
    axA.plot(fy, Py / Py.max(), color=NERED, lw=1.4, ls="--", label="NMM2 mean field (exact)")
    axA.set_xlim(0, 130); axA.set_xlabel("frequency (Hz)"); axA.set_ylabel("power (norm.)")
    figstyle.panel(axA, "a")
    axA.legend(fontsize=9.0, frameon=False, loc="upper right")
    axA.spines[["top", "right"]].set_visible(False)

    # (b) intermodulation: oscillatory regime, TI off vs on. The nonlinearity mixes the
    # imposed Df=42 Hz beat with the intrinsic ~53 Hz gamma -> sidebands. TI-on lights up
    # the direct Df line (42) and the SUM 53+42=95; the difference 53-42=11 is weak. This is
    # the spiking-network view of the macroscale frequency mixing (sidebands establish mixing, not its unique modulation mechanism).
    dfb = conds["entrain_on"]["q"]["df"]; fg = 53.0
    for key, col, lab in (("entrain_off", GR, "TI off"), ("entrain_on", NEBLUE, "TI on")):
        qq = conds[key]["q"]
        start = float(qq["ts"][qq["kmeas"]]) if "kmeas" in qq else t0
        fS, PS = _rate_spectrum(qq["re_t"], qq["ts"], dt, t_start=start)
        axC.semilogy(fS, PS, color=col, lw=1.2, label=lab)
    # Mark only the lines the figure can stand behind: the direct Df line and the SUM
    # sideband. The difference tone f0-Df sits at the noise floor (its small amplitude is
    # set by the network transfer function, not the mixer), so we do not flag it.
    for fr, txt in ((dfb, r"$\Delta f$"), (fg, r"$f_0$"), (fg + dfb, r"$f_0{+}\Delta f$")):
        axC.axvline(fr, ls=":", color=NERED, lw=0.8, alpha=0.7)
        axC.text(fr, 1.5, txt, rotation=90, fontsize=9.0, color=NERED, ha="right", va="bottom")
    axC.set_xlim(0, 120); axC.set_ylim(1e-4, 4)
    axC.set_xlabel("frequency (Hz)"); axC.set_ylabel("power of $r_E$ (norm.)")
    figstyle.panel(axC, "b")
    axC.legend(fontsize=9.0, frameon=False, loc="lower right")
    axC.spines[["top", "right"]].set_visible(False)

    # (c) Df modulation depth = AC(Df)/<r_E> -- a STABLE off->on metric: the amplitude
    # of the Df-locked rate oscillation as a fraction of the mean rate. Both quantities
    # are well-estimated, unlike the off/on lock-in RATIO whose denominator sits at the
    # near-zero noise floor (and so is realization-noisy). Mean rate flatness shown as text.
    # Cache keys are historical. Labels identify eta, not the stimulated regime.
    regimes = [("forced", r"$\bar\eta=0.85$"), ("entrain", r"$\bar\eta=1.5$")]
    depth_off = []; depth_on = []; rate_fc = []
    for reg, _ in regimes:
        qo = conds[f"{reg}_off"]["q"]; qn = conds[f"{reg}_on"]["q"]
        depth_off.append(qo["AC"] / qo["rmean"])
        depth_on.append(qn["AC"] / qn["rmean"])
        rate_fc.append(qn["rmean"] / qo["rmean"])
    x = np.arange(len(regimes)); bw = 0.36
    axB.bar(x - bw / 2, depth_off, bw, color=GR, label="TI off")
    axB.bar(x + bw / 2, depth_on, bw, color=NEGREEN, label="TI on")
    # Numeric bar labels removed: they print below the 6.2 pt floor once the figure is
    # scaled to its placed width, and the same values are already given in the Results
    # text and the caption. The bars carry the comparison on their own.
    axB.set_xticks(x); axB.set_xticklabels([n for _, n in regimes])
    axB.set_ylabel(r"$A_\Omega/\langle r_E\rangle$")
    figstyle.panel(axB, "c")
    axB.legend(fontsize=9.0, frameon=False, loc="upper left")
    axB.set_ylim(0, max(depth_on) * 1.18)
    axB.spines[["top", "right"]].set_visible(False)

    fig.tight_layout(w_pad=3.0)
    figstyle.thin_ticks(fig)
    figstyle.scale_text(fig, placed_frac=1)
    overlap.check(fig, placed_frac=1, name="make_qif_figs.py")
    for ext in ("pdf", "png"):
        fig.savefig(os.path.join(FIGS, f"fig_qif_timing{_TAG}.{ext}"), dpi=300, bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    fig_raster(); fig_timing()
    print("wrote fig_qif_raster and fig_qif_timing")
    for k in ("forced_off", "forced_on", "entrain_off", "entrain_on"):
        q = conds[k]["q"]
        print(f"  {k:12s}: <r_e>={q['rmean']:.4f}  AC@{q['df']:.0f}={q['AC']:.4f}  spikes={q['spk_t'].size}")
