"""QIF microscale of the NMM2 PING gamma generator: spike rasters and rate modulation.

NMM2 (Montbrio-Pazo-Roxin) is the EXACT mean field of an all-to-all network of QIF
neurons with Lorentzian-distributed excitabilities (Rosetta Stone / Clusella). Here we
integrate that underlying spiking network directly, with the SAME parameters as the
mean-field model (nmm2_ping.py). The finite-amplitude examples contain a beat-locked
rate component alongside gamma activity, with an 8--11% mean-rate increase. Their
historical 'forced'/'entrain' keys identify the field-free state only; field-on
activity at eta=0.85 is not a purely beat-forced response (October 5, 2026 review).

QIF neuron j of population alpha in {E,I}:
    tau_a Vdot_j = V_j^2 + eta_j + [F(t) on E only] + tau_a C (A.s)
spike + reset at V_j >= Vpeak (-> -Vpeak); eta_j ~ Lorentzian(etabar, Delta=1) sampled
by the deterministic quantile rule (low finite-size noise). Second-order synapses
s_e=K_a[r_e], s_i=K_g[r_i] are driven by the EMPIRICAL population rates. The mean field
of this network is exactly Eq. (nmm2-ping). Time unit ~ 1 ms; frequencies in Hz.

Self-contained: numpy only (no scipy). Saves qif_raster.npz for make_qif_figs.py.
"""
import os, sys
import numpy as np

# --- parameters: identical to nmm2_ping.py ---
TAU_E, TAU_A, TAU_I, TAU_G = 15.0, 10.0, 7.5, 2.5
A_EE, A_EI, A_IE, A_II = 1.0, 1.0, 1.0, 2.0
C = 15.0; DEL = 1.0; PI = np.pi
VPEAK = 100.0
HERE = os.path.dirname(os.path.abspath(__file__))


def lorentz_eta(n, etabar, delta=DEL):
    """Deterministic Lorentzian quantiles (Montbrio 2015): low finite-size noise."""
    j = np.arange(1, n + 1)
    return etabar + delta * np.tan((PI / 2) * (2 * j - n - 1) / (n + 1))


# ---- exact mean field (Eq. nmm2-ping; copied from nmm2_ping.py for the overlay) ----

# --- applied-field waveform -------------------------------------------------
# 'am'      : A(1 + cos Om t) cos(wc t)        -- the modulated-carrier surrogate
# 'twotone' : A[cos(w1 t) + cos(w2 t)],  w2-w1 = Om  -- the physical TI waveform
# At m = 1 the two share their peak amplitude (2A) and their leading quadratic
# component at Omega; they differ in DC and in the second harmonic (the surrogate
# emits a 2*Omega line at 25% of the fundamental, two tones emit none).
WAVE = 'am'

def _field(t, A, wO, wc):
    if A == 0.0:
        return 0.0
    if WAVE == 'am':
        return A*(1.0 + np.cos(wO*t))*np.cos(wc*t)
    if WAVE == 'twotone':
        return A*(np.cos((wc - wO/2.0)*t) + np.cos((wc + wO/2.0)*t))
    raise ValueError(f"unknown WAVE {WAVE!r}")

def _mf_rhs(y, t, eta, Af, wO, wc):
    r_e, v_e, r_i, v_i, s_e, z_e, s_i, z_i = y
    F = _field(t, Af, wO, wc)
    return np.array([
        (DEL / (PI * TAU_E) + 2 * r_e * v_e) / TAU_E,
        (eta - (PI * TAU_E * r_e) ** 2 + v_e ** 2 + F) / TAU_E + C * (A_EE * s_e - A_EI * s_i),
        (DEL / (PI * TAU_I) + 2 * r_i * v_i) / TAU_I,
        (eta - (PI * TAU_I * r_i) ** 2 + v_i ** 2) / TAU_I + C * (A_IE * s_e - A_II * s_i),
        z_e / TAU_A, (r_e - 2 * z_e - s_e) / TAU_A,
        z_i / TAU_G, (r_i - 2 * z_i - s_i) / TAU_G])


def mf_run(eta, Af, fc, df, T, dt):
    wc = 2 * PI * fc / 1000.0; wO = 2 * PI * df / 1000.0
    y = np.array([0.05, -2.0, 0.05, -2.0, 0.05, 0.0, 0.05, 0.0]); t = 0.0
    n = int(T / dt); re = np.empty(n); ts = np.empty(n)
    for k in range(n):
        k1 = _mf_rhs(y, t, eta, Af, wO, wc); k2 = _mf_rhs(y + .5 * dt * k1, t + .5 * dt, eta, Af, wO, wc)
        k3 = _mf_rhs(y + .5 * dt * k2, t + .5 * dt, eta, Af, wO, wc); k4 = _mf_rhs(y + dt * k3, t + dt, eta, Af, wO, wc)
        y = y + (dt / 6) * (k1 + 2 * k2 + 2 * k3 + k4); t += dt; re[k] = y[0]; ts[k] = t
    return ts, re


# ---- QIF spiking network (Euler; vectorized over neurons) ----
def qif_run(etabar, Af, fc, df, Ne, Ni, T, dt, t_meas, nrec=400, seed=1):
    wc = 2 * PI * fc / 1000.0; wO = 2 * PI * df / 1000.0
    rng = np.random.default_rng(seed)
    eta_e = rng.permutation(lorentz_eta(Ne, etabar))   # permute so the recorded nrec are a
    eta_i = rng.permutation(lorentz_eta(Ni, etabar))   # representative (eta-unsorted) sample
    Ve = -2.0 + np.zeros(Ne); Vi = -2.0 + np.zeros(Ni)
    s_e = 0.05; z_e = 0.0; s_i = 0.05; z_i = 0.0
    nstep = int(T / dt); kmeas = int((T - t_meas) / dt)
    ts = np.empty(nstep); re_t = np.empty(nstep)
    spk_t = []; spk_id = []
    sc = ss = ntot = 0.0                                # pooled vector-strength accumulators (E, in window)
    sc_n = np.zeros(Ne); ss_n = np.zeros(Ne); n_n = np.zeros(Ne)   # per-neuron accumulators (2026-09-22)
    rmean = 0.0; nmean = 0
    for k in range(nstep):
        t = k * dt
        F = _field(t, Af, wO, wc)
        Ie = TAU_E * C * (A_EE * s_e - A_EI * s_i)
        Ii = TAU_I * C * (A_IE * s_e - A_II * s_i)
        Ve = Ve + dt * (Ve * Ve + eta_e + F + Ie) / TAU_E
        Vi = Vi + dt * (Vi * Vi + eta_i + Ii) / TAU_I
        se = Ve >= VPEAK; si = Vi >= VPEAK
        Ve[se] = -VPEAK; Vi[si] = -VPEAK
        ne = int(se.sum()); ni = int(si.sum())
        r_e_emp = ne / (Ne * dt); r_i_emp = ni / (Ni * dt)
        s_e = s_e + dt * z_e / TAU_A; z_e = z_e + dt * (r_e_emp - 2 * z_e - s_e) / TAU_A
        s_i = s_i + dt * z_i / TAU_G; z_i = z_i + dt * (r_i_emp - 2 * z_i - s_i) / TAU_G
        ts[k] = t; re_t[k] = r_e_emp
        if k >= kmeas:
            # raster for the first nrec E neurons (a representative random sample)
            fired = np.nonzero(se[:nrec])[0]
            if fired.size:
                spk_t.extend([t] * fired.size); spk_id.extend(fired.tolist())
            # envelope-phase vector strength over ALL E spikes; mean rate
            if ne:
                ph = wO * t; cph = np.cos(ph); sph = np.sin(ph)
                sc += ne * cph; ss += ne * sph; ntot += ne
                sc_n += se * cph; ss_n += se * sph; n_n += se
            rmean += r_e_emp; nmean += 1
    VS = np.sqrt(sc ** 2 + ss ** 2) / ntot if ntot else 0.0       # pooled (population) vector strength
    # per-neuron vector strength: neurons with >= NMIN spikes in the window; the Rayleigh
    # bias floor for n random phases is ~sqrt(pi/(4 n)), so report the off-field control alongside.
    NMIN = 10
    ok = n_n >= NMIN
    VS_n = np.full(Ne, np.nan); PPC_n = np.full(Ne, np.nan)
    VS_n[ok] = np.sqrt(sc_n[ok] ** 2 + ss_n[ok] ** 2) / n_n[ok]
    # pairwise phase consistency (Vinck et al. 2010): PPC = (n R^2 - 1)/(n - 1), an unbiased
    # estimate of the squared resultant; zero in expectation for random phases, so it is
    # comparable across neurons with different spike counts.
    PPC_n[ok] = (n_n[ok] * VS_n[ok] ** 2 - 1.0) / (n_n[ok] - 1.0)
    PPC = (ntot * VS ** 2 - 1.0) / (ntot - 1.0) if ntot > 1 else 0.0
    return dict(ts=ts, re_t=re_t, spk_t=np.array(spk_t), spk_id=np.array(spk_id),
                VS=VS, PPC=PPC, VS_n=VS_n, PPC_n=PPC_n, n_spk=n_n, nmin=NMIN,
                VS_n_median=float(np.nanmedian(VS_n)) if ok.any() else np.nan,
                PPC_n_median=float(np.nanmedian(PPC_n)) if ok.any() else np.nan,
                frac_ok=float(ok.mean()),
                rmean=rmean / max(nmean, 1), nrec=nrec, etabar=etabar, Af=Af, df=df)


def smooth(x, dt, win_ms=1.0):
    w = max(1, int(win_ms / dt)); k = np.ones(w) / w
    return np.convolve(x, k, mode="same")


def lockin(ts, x, df, kmeas):
    """Lock-in amplitude of x(t) at envelope frequency df (Hz), over the tail."""
    t = ts[kmeas:]; y = x[kmeas:] - x[kmeas:].mean(); wO = 2 * PI * df / 1000.0
    w = np.hanning(len(y))
    c = (y * w * np.cos(wO * t)).sum(); s = (y * w * np.sin(wO * t)).sum()
    return 2 * np.sqrt(c ** 2 + s ** 2) / w.sum()


if __name__ == "__main__":
    quick = "--quick" in sys.argv
    Ne = Ni = 400 if quick else 8000
    dt = 0.005 if quick else 0.0025
    # 2026-09-22 (review R12): settle 800 ms (>= 4.5 relaxation times at eta=0.85, where the
    # mean-field relaxation time is ~176 ms) and measure over an INTEGER number of beat
    # cycles (>= 800 ms), so the finite-window bias of the vector strength vanishes.
    # Previously T = 420 ms with a 150 ms window (8 cycles at 55 Hz, 6 at 42 Hz).
    T_SETTLE = 250.0 - 150.0 if quick else 800.0
    def window(df, floor_ms=150.0 if quick else 800.0):
        ncyc = int(np.ceil(floor_ms * df / 1000.0))
        return ncyc * 1000.0 / df, ncyc
    fc = 300.0; Af = 35.0
    for i, a_ in enumerate(sys.argv):                      # convergence overrides
        if a_ == "--dt": dt = float(sys.argv[i + 1])
        if a_ == "--vpeak": globals()["VPEAK"] = float(sys.argv[i + 1])
    # --twotone drives with the physical TI waveform (two tones) instead of the AM
    # surrogate. Spiking/threshold dynamics are exactly where the two cannot be
    # assumed equivalent beyond perturbation theory, so the published run uses it.
    if "--twotone" in sys.argv:
        globals()["WAVE"] = "twotone"
    # Historical cache keys: 'forced' is field-free stable, 'entrain' field-free
    # oscillatory. At Af=35, the first field-on run also develops off-beat gamma.
    # The 42 Hz beat in the second run coexists with the autonomous rhythm.
    ETA_FORCED, DF_FORCED = 0.85, 55.0
    ETA_ENTRAIN, DF_ENTRAIN = 1.5, 42.0

    if "--test" in sys.argv or quick:
        for name, eta, df in [("forced", ETA_FORCED, DF_FORCED), ("entrain", ETA_ENTRAIN, DF_ENTRAIN)]:
            t_meas, ncyc = window(df); T = T_SETTLE + t_meas; kmeas = int((T - t_meas) / dt)
            qo = qif_run(eta, 0.0, fc, df, Ne, Ni, T, dt, t_meas)
            qn = qif_run(eta, Af, fc, df, Ne, Ni, T, dt, t_meas)
            print(f"{name:8s} dt={dt} VPEAK={VPEAK} T={T:.1f} window={t_meas:.1f} ms ({ncyc} cycles): "
                  f"<r_e> off={qo['rmean']:.4f} on={qn['rmean']:.4f} | "
                  f"AC@df off={lockin(qo['ts'],qo['re_t'],df,kmeas):.4f} "
                  f"on={lockin(qn['ts'],qn['re_t'],df,kmeas):.4f} | "
                  f"VS pooled off={qo['VS']:.3f} on={qn['VS']:.3f} | "
                  f"VS per-neuron median off={qo['VS_n_median']:.3f} on={qn['VS_n_median']:.3f} | "
                  f"PPC pooled off={qo['PPC']:.4f} on={qn['PPC']:.4f} | PPC per-neuron median off={qo['PPC_n_median']:.4f} on={qn['PPC_n_median']:.4f} "
                  f"(frac>= {qo['nmin']} spikes: {qo['frac_ok']:.2f}/{qn['frac_ok']:.2f})", flush=True)
        sys.exit(0)

    # full run: 4 conditions (2 regimes x off/on) + mean-field overlays
    conds = {}
    meta_w = {}
    for reg, eta, df in [("forced", ETA_FORCED, DF_FORCED), ("entrain", ETA_ENTRAIN, DF_ENTRAIN)]:
        t_meas, ncyc = window(df); T = T_SETTLE + t_meas; kmeas = int((T - t_meas) / dt)
        meta_w[reg] = dict(T=T, t_meas=t_meas, ncyc=ncyc, kmeas=kmeas)
        for fld, Afv in [("off", 0.0), ("on", Af)]:
            q = qif_run(eta, Afv, fc, df, Ne, Ni, T, dt, t_meas)
            tm, rm = mf_run(eta, Afv, fc, df, T, dt)
            q["AC"] = lockin(q["ts"], q["re_t"], df, kmeas)
            q["df"] = df; q["T"] = T; q["t_meas"] = t_meas; q["kmeas"] = kmeas
            conds[f"{reg}_{fld}"] = dict(q=q, mf_t=tm, mf_re=rm)
            print(f"{reg:8s} {fld:3s}: T={T:.1f} window={t_meas:.1f} ms ({ncyc} cycles)  <r_e>={q['rmean']:.4f}  "
                  f"AC@{df:.0f}Hz={q['AC']:.4f}  VS pooled={q['VS']:.3f}  "
                  f"VS per-neuron median={q['VS_n_median']:.3f}  PPC pooled={q['PPC']:.4f}  PPC per-neuron median={q['PPC_n_median']:.4f} (frac>={q['nmin']} spk {q['frac_ok']:.2f})  "
                  f"spikes(rec)={q['spk_t'].size}", flush=True)
    _tag = "_twotone" if WAVE == "twotone" else ""
    np.savez(os.path.join(HERE, f"qif_raster{_tag}.npz"),
             meta=dict(Ne=Ne, Ni=Ni, dt=dt, T_settle=T_SETTLE, windows=meta_w, fc=fc, Af=Af,
                       eta_forced=ETA_FORCED, df_forced=DF_FORCED,
                       eta_entrain=ETA_ENTRAIN, df_entrain=DF_ENTRAIN, VPEAK=VPEAK),
             conds=conds, allow_pickle=True)
    print(f"saved qif_raster{_tag}.npz  (WAVE={WAVE})")
