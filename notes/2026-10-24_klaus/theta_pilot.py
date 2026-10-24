"""Theta-neuron pilot of the TN0484 QIF network (referee item 5). Klaus, 2026-10-24.

The QIF network of code/qif_raster.py with the exact change of variables
V = tan(theta/2) (Ermentrout-Kopell), which removes the finite spike cutoff
V_peak that the published runs needed. Everything else is the published model:
parameters, Lorentzian excitabilities by deterministic quantiles (same seed and
permutation), second-order synapses driven by the empirical rates, Euler steps,
800 ms burn-in, integer-cycle windows, and the readouts of qif_raster.py
(lock-in at the beat, depth = lock-in / mean rate, pooled vector strength,
pairwise phase consistency). The functions lorentz_eta, lockin, and mf_run are
imported read-only from code/qif_raster.py; nothing in code/ is modified.

QIF (per neuron j, population X in {E, I}):   tau_X dV/dt = V^2 + eta_j + U_X(t)
with U_E = F(t) + tau_E C (A_EE s_e - A_EI s_i), U_I = tau_I C (A_IE s_e - A_II s_i).
Theta form:  tau_X dtheta/dt = (1 - cos theta) + (1 + cos theta)(eta_j + U_X).
A spike is an upward crossing of theta = pi; its time is linearly interpolated
inside the Euler step (theta_old < pi <= theta_new), theta is wrapped by -2 pi,
the spike is counted in that step for the empirical rate r = n_spk / (N dt) that
drives the synapses, and the interpolated time gives the beat phase for the
vector-strength and PPC accumulators. Units follow qif_raster.py: time in ms,
rates in 1/ms, dimensionless MPR voltages and drives.

Field on E only: two tones A[cos(w1 t) + cos(w2 t)] with w_{1,2} = w_c -/+ w_O/2
(the published waveform), or the equal-RMS single carrier sqrt(2) A cos(w_c t)
(same mean-square input current A^2 in model units; not a calibrated polarization).

Runs (see theta_pilot_protocol.md for the pre-registered tolerances):
  off   eta=0.85, A=0,  N=8000/pop, dt=0.0025 ms, settle 800 ms, window 44 cycles (800 ms)
  on    as off with two tones A=10 at 300 Hz, beat 55 Hz
  dt2   on with dt=0.00125 ms
  n2    on with N=16000 per population
  long  on with window 88 cycles (1600 ms); burn-in unchanged
  sc10  single carrier, A=10 (RMS-matched to 'on')
  tt35  two tones, A=35
  sc35  single carrier, A=35
Usage: .venv/bin/python theta_pilot.py --runs on,dt2 [--quick]
Writes theta_pilot_<run>.json (statistics, settings, runtime) and theta_pilot_<run>.npz
(binned E rate, mean-field E rate) next to this file, and appends to theta_pilot.log.
"""
import os, sys, json, time, argparse
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
CODE = os.path.abspath(os.path.join(HERE, "..", "..", "code"))
sys.path.insert(0, CODE)
import qif_raster as Q      # read-only import

PI = np.pi
TAU_E, TAU_A, TAU_I, TAU_G = Q.TAU_E, Q.TAU_A, Q.TAU_I, Q.TAU_G
A_EE, A_EI, A_IE, A_II = Q.A_EE, Q.A_EI, Q.A_IE, Q.A_II
C = Q.C
FC = 300.0


def field(t, A, wO, wc, wave):
    if A == 0.0:
        return 0.0
    if wave == "twotone":
        return A * (np.cos((wc - wO / 2.0) * t) + np.cos((wc + wO / 2.0) * t))
    if wave == "single":
        return np.sqrt(2.0) * A * np.cos(wc * t)
    raise ValueError(wave)


def theta_run(etabar, Af, fc, df, Ne, Ni, T, dt, t_meas, wave="twotone", seed=1):
    wc = 2 * PI * fc / 1000.0; wO = 2 * PI * df / 1000.0
    rng = np.random.default_rng(seed)
    eta_e = rng.permutation(Q.lorentz_eta(Ne, etabar))
    eta_i = rng.permutation(Q.lorentz_eta(Ni, etabar))
    th_e = np.full(Ne, 2 * np.arctan(-2.0)); th_i = np.full(Ni, 2 * np.arctan(-2.0))   # V = -2 as in qif_raster
    s_e = 0.05; z_e = 0.0; s_i = 0.05; z_i = 0.0
    nstep = int(T / dt); kmeas = int((T - t_meas) / dt)
    ts = np.empty(nstep); re_t = np.empty(nstep)
    sc = ss = ntot = 0.0
    sc_n = np.zeros(Ne); ss_n = np.zeros(Ne); n_n = np.zeros(Ne)
    rmean = 0.0; nmean = 0; max_dth = 0.0
    for k in range(nstep):
        t = k * dt
        F = field(t, Af, wO, wc, wave)
        Ie = TAU_E * C * (A_EE * s_e - A_EI * s_i)
        Ii = TAU_I * C * (A_IE * s_e - A_II * s_i)
        ce = np.cos(th_e); ci = np.cos(th_i)
        new_e = th_e + dt * ((1.0 - ce) + (1.0 + ce) * (eta_e + F + Ie)) / TAU_E
        new_i = th_i + dt * ((1.0 - ci) + (1.0 + ci) * (eta_i + Ii)) / TAU_I
        se = new_e >= PI; si = new_i >= PI
        ne = int(se.sum()); ni = int(si.sum())
        if k % 4000 == 0:                                    # largest Euler advance, any neuron
            max_dth = max(max_dth, float(np.abs(new_e - th_e).max()), float(np.abs(new_i - th_i).max()))
        if ne:
            frac = (PI - th_e[se]) / (new_e[se] - th_e[se])
            new_e[se] -= 2 * PI
        if ni:
            new_i[si] -= 2 * PI
        th_e = new_e; th_i = new_i
        r_e_emp = ne / (Ne * dt); r_i_emp = ni / (Ni * dt)
        s_e = s_e + dt * z_e / TAU_A; z_e = z_e + dt * (r_e_emp - 2 * z_e - s_e) / TAU_A
        s_i = s_i + dt * z_i / TAU_G; z_i = z_i + dt * (r_i_emp - 2 * z_i - s_i) / TAU_G
        ts[k] = t; re_t[k] = r_e_emp
        if k >= kmeas:
            if ne:
                ph = wO * (t + frac * dt); cph = np.cos(ph); sph = np.sin(ph)
                sc += cph.sum(); ss += sph.sum(); ntot += ne
                idx = np.nonzero(se)[0]
                sc_n[idx] += cph; ss_n[idx] += sph; n_n[idx] += 1
            rmean += r_e_emp; nmean += 1
    VS = np.sqrt(sc ** 2 + ss ** 2) / ntot if ntot else 0.0
    NMIN = 10; ok = n_n >= NMIN
    VS_n = np.full(Ne, np.nan); PPC_n = np.full(Ne, np.nan)
    VS_n[ok] = np.sqrt(sc_n[ok] ** 2 + ss_n[ok] ** 2) / n_n[ok]
    PPC_n[ok] = (n_n[ok] * VS_n[ok] ** 2 - 1.0) / (n_n[ok] - 1.0)
    PPC = (ntot * VS ** 2 - 1.0) / (ntot - 1.0) if ntot > 1 else 0.0
    return dict(ts=ts, re_t=re_t, VS=float(VS), PPC=float(PPC),
                VS_n_median=float(np.nanmedian(VS_n)) if ok.any() else float("nan"),
                PPC_n_median=float(np.nanmedian(PPC_n)) if ok.any() else float("nan"),
                frac_ok=float(ok.mean()), rmean=rmean / max(nmean, 1), kmeas=kmeas, max_dtheta_sampled=max_dth)


def window(df, floor_ms):
    ncyc = int(np.ceil(floor_ms * df / 1000.0))
    return ncyc * 1000.0 / df, ncyc


RUNS = dict(
    off=dict(Af=0.0, wave="twotone"), on=dict(Af=10.0, wave="twotone"),
    dt2=dict(Af=10.0, wave="twotone", dt=0.00125), n2=dict(Af=10.0, wave="twotone", N=16000),
    long=dict(Af=10.0, wave="twotone", floor=1600.0),
    sc10=dict(Af=10.0, wave="single"), tt35=dict(Af=35.0, wave="twotone"), sc35=dict(Af=35.0, wave="single"))

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--runs", default="on"); ap.add_argument("--quick", action="store_true")
    ap.add_argument("--no-mf", action="store_true")
    a = ap.parse_args()
    ETA, DFB = 0.85, 55.0
    for name in a.runs.split(","):
        cfg = dict(N=8000, dt=0.0025, floor=800.0, settle=800.0); cfg.update(RUNS[name])
        if a.quick:
            cfg.update(N=400, dt=0.005, floor=150.0, settle=100.0)
        t_meas, ncyc = window(DFB, cfg["floor"]); T = cfg["settle"] + t_meas
        t0 = time.perf_counter()
        r = theta_run(ETA, cfg["Af"], FC, DFB, cfg["N"], cfg["N"], T, cfg["dt"], t_meas, wave=cfg["wave"])
        rt = time.perf_counter() - t0
        AC = Q.lockin(r["ts"], r["re_t"], DFB, r["kmeas"])
        out = dict(run=name, model="theta (QIF with V=tan(theta/2), no cutoff)", eta=ETA, Af=cfg["Af"], wave=cfg["wave"],
                   fc=FC, beat_Hz=DFB, N_per_pop=cfg["N"], dt_ms=cfg["dt"], settle_ms=cfg["settle"],
                   window_ms=t_meas, cycles=ncyc, quick=a.quick,
                   rate_mean=r["rmean"], lockin=float(AC), depth=float(AC / r["rmean"]) if r["rmean"] else float("nan"),
                   VS_pooled=r["VS"], PPC_pooled=r["PPC"], VS_neuron_median=r["VS_n_median"],
                   PPC_neuron_median=r["PPC_n_median"], frac_neurons_ge10spk=r["frac_ok"],
                   max_dtheta_per_step_sampled=r["max_dtheta_sampled"], runtime_min=rt / 60.0)
        mf_re = None
        if not a.no_mf and not a.quick:
            Q.WAVE = cfg["wave"]
            Q._field = lambda t, A, wO, wc: field(t, A, wO, wc, cfg["wave"])   # in-memory only
            t1 = time.perf_counter()
            tm, rm = Q.mf_run(ETA, cfg["Af"], FC, DFB, T, cfg["dt"])
            out["mf_rate_mean"] = float(rm[r["kmeas"]:].mean())
            out["mf_depth"] = float(Q.lockin(tm, rm, DFB, r["kmeas"]) / rm[r["kmeas"]:].mean())
            out["mf_runtime_min"] = (time.perf_counter() - t1) / 60.0
            mf_re = rm
        tag = "_quick" if a.quick else ""
        json.dump(out, open(os.path.join(HERE, f"theta_pilot_{name}{tag}.json"), "w"), indent=1)
        step = max(1, int(round(0.1 / cfg["dt"])))          # store the rate at 0.1 ms resolution
        np.savez_compressed(os.path.join(HERE, f"theta_pilot_{name}{tag}.npz"), ts=r["ts"][::step], re_t=r["re_t"][::step],
                            mf_re=(mf_re[::step] if mf_re is not None else np.array([])), kmeas=r["kmeas"] // step)
        line = (f"{name:5s} A={cfg['Af']:g} {cfg['wave']:7s} N={cfg['N']} dt={cfg['dt']} window={t_meas:.1f} ms ({ncyc} cyc) "
                f"<r_e>={r['rmean']:.4f} lockin={AC:.4f} depth={out['depth']:.4f} VS={r['VS']:.3f} PPC={r['PPC']:.4f} "
                f"PPC/neuron median={r['PPC_n_median']:.4f} max_dtheta={r['max_dtheta_sampled']:.3f} [{rt/60:.1f} min]"
                + (f" MF depth={out['mf_depth']:.4f} <r>={out['mf_rate_mean']:.4f}" if "mf_depth" in out else ""))
        print(line, flush=True)
        with open(os.path.join(HERE, "theta_pilot.log"), "a") as fh:
            fh.write(time.strftime("%Y-%m-%d %H:%M:%S ") + line + "\n")
