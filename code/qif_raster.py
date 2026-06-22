"""QIF microscale of the NMM2 PING gamma generator: spike rasters + timing-not-rate.

NMM2 (Montbrio-Pazo-Roxin) is the EXACT mean field of an all-to-all network of QIF
neurons with Lorentzian-distributed excitabilities (Rosetta Stone / Clusella). Here we
integrate that underlying spiking network directly, with the SAME parameters as the
mean-field model (nmm2_ping.py), and show that an AM (TI) field realigns spike TIMING
into the recovered envelope while leaving the mean firing rate essentially unchanged --
the spiking-level counterpart of the mesoscale result (sec:timing) and the microscale
analog of the in-vivo finding (Vieira 2024).

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
def _mf_rhs(y, t, eta, Af, wO, wc):
    r_e, v_e, r_i, v_i, s_e, z_e, s_i, z_i = y
    F = Af * (1 + np.cos(wO * t)) * np.cos(wc * t) if Af != 0 else 0.0
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
    sc = ss = ntot = 0.0                                # vector-strength accumulators (E, in window)
    rmean = 0.0; nmean = 0
    for k in range(nstep):
        t = k * dt
        F = Af * (1 + np.cos(wO * t)) * np.cos(wc * t) if Af != 0 else 0.0
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
                ph = wO * t
                sc += ne * np.cos(ph); ss += ne * np.sin(ph); ntot += ne
            rmean += r_e_emp; nmean += 1
    VS = np.sqrt(sc ** 2 + ss ** 2) / ntot if ntot else 0.0
    return dict(ts=ts, re_t=re_t, spk_t=np.array(spk_t), spk_id=np.array(spk_id),
                VS=VS, rmean=rmean / max(nmean, 1), nrec=nrec, etabar=etabar, Af=Af, df=df)


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
    T = 250.0 if quick else 420.0
    t_meas = 150.0
    fc = 300.0; Af = 35.0
    # forced: just below the gamma Hopf (eta_Hopf~1.1); drive at the gamma resonance.
    # entrain: above the Hopf (autonomous f0~54 Hz); drive DETUNED (42 Hz) so the
    #          TI beat re-times the rhythm to its own envelope.
    ETA_FORCED, DF_FORCED = 0.85, 55.0
    ETA_ENTRAIN, DF_ENTRAIN = 1.5, 42.0
    kmeas = int((T - t_meas) / dt)

    if "--test" in sys.argv or quick:
        for name, eta, df in [("forced", ETA_FORCED, DF_FORCED), ("entrain", ETA_ENTRAIN, DF_ENTRAIN)]:
            qo = qif_run(eta, 0.0, fc, df, Ne, Ni, T, dt, t_meas)
            qn = qif_run(eta, Af, fc, df, Ne, Ni, T, dt, t_meas)
            print(f"{name:8s}: <r_e> off={qo['rmean']:.4f} on={qn['rmean']:.4f} | "
                  f"AC@df off={lockin(qo['ts'],qo['re_t'],df,kmeas):.4f} "
                  f"on={lockin(qn['ts'],qn['re_t'],df,kmeas):.4f}")
        sys.exit(0)

    # full run: 4 conditions (2 regimes x off/on) + mean-field overlays
    conds = {}
    for reg, eta, df in [("forced", ETA_FORCED, DF_FORCED), ("entrain", ETA_ENTRAIN, DF_ENTRAIN)]:
        for fld, Afv in [("off", 0.0), ("on", Af)]:
            q = qif_run(eta, Afv, fc, df, Ne, Ni, T, dt, t_meas)
            tm, rm = mf_run(eta, Afv, fc, df, T, dt)
            q["AC"] = lockin(q["ts"], q["re_t"], df, kmeas)
            q["df"] = df
            conds[f"{reg}_{fld}"] = dict(q=q, mf_t=tm, mf_re=rm)
            print(f"{reg:8s} {fld:3s}: <r_e>={q['rmean']:.4f}  AC@{df:.0f}Hz={q['AC']:.4f}  "
                  f"VS={q['VS']:.3f}  spikes={q['spk_t'].size}")
    np.savez(os.path.join(HERE, "qif_raster.npz"),
             meta=dict(Ne=Ne, Ni=Ni, dt=dt, T=T, t_meas=t_meas, fc=fc, Af=Af,
                       eta_forced=ETA_FORCED, df_forced=DF_FORCED,
                       eta_entrain=ETA_ENTRAIN, df_entrain=DF_ENTRAIN),
             conds=conds, allow_pickle=True)
    print("saved qif_raster.npz")
