"""
Producer for khz_twotone.npz, recovered from the cache itself, with a comparison mode.

The committed cache (added in a7d6e6f, July 22, 2026) holds Hann amplitude spectra of
the applied two-tone field (fI, PI) and of the Jansen-Rit read-out v = y1 - y2 (fV, PV),
with the tone frequencies f1, f2 and the beat F0. The arrays fix the run: 133334 bins
means 266666 samples; the top frequency 33333.3 Hz means dt = 1.5e-5 s; the bin width
0.250001 Hz means 4.0 s of data; F0 = 10.914393 Hz is the imaginary part of the leading
eigenvalue at the khz_direct.py operating point (p = 400, C = 135), and f1,2 = 2000 -/+
F0/2. The per-tone amplitude follows from the input peaks: 0.4927 and 0.4883 mV are a
0.5 mV tone after Hann scalloping at the two bin offsets. The remaining choices (fast
element tau = 0.2 ms as a first-order state before the pyramidal sigmoid, RK4, zero
initial state, plain-mean removal of both signals before the Hann window, amplitude
normalization 2|X|/sum(w)) are those of khz_direct.py's panel (b) trace with the AM
surrogate replaced by two tones. Two of them were identified from the cache rather than
from khz_direct.py: the settling time is 4.0 s, not 5.0 s, and the field and read-out
samples are recorded before each RK4 step (the convention of lanmm_field_tongues.py),
not after. With those settings --compare reproduces both cached spectra exactly
(maximum absolute difference 0.0 in every bin, October 4, 2026); with 5.0 s settling
and after-step sampling the differences are 2e-5 (input) and 1.4e-3 (output line)
relative. --write saves a fresh file under a new name; the committed cache is never
overwritten.

Model: 7-state JR column of khz_direct.py (6 JR states plus the filtered field x_f,
dx_f/dt = (E - x_f)/tau; the sigmoid of the pyramidal output sees y1 - y2 + x_f),
JR constants from timing_not_rate.py, p = 400 /s, C = 135.
Field: E(t) = eps [cos(2 pi f1 t) + cos(2 pi f2 t)], eps = 0.5 mV per tone.
"""
import os, sys, json, time, argparse
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import khz_direct as K                      # rhs7 and the operating point p, C
from timing_not_rate import jac_eig


def field2(t, f1, f2, eps):
    return eps * (np.cos(2 * np.pi * f1 * t) + np.cos(2 * np.pi * f2 * t))


def step2(Y, t, dt, f1, f2, eps, tau, direct):
    k1 = K.rhs7(Y, field2(t, f1, f2, eps), tau, direct)
    k2 = K.rhs7(Y + .5 * dt * k1, field2(t + .5 * dt, f1, f2, eps), tau, direct)
    k3 = K.rhs7(Y + .5 * dt * k2, field2(t + .5 * dt, f1, f2, eps), tau, direct)
    k4 = K.rhs7(Y + dt * k3, field2(t + dt, f1, f2, eps), tau, direct)
    return Y + (dt / 6) * (k1 + 2 * k2 + 2 * k3 + k4)


def amp_spectrum(x, dt, demean="plain"):
    w = np.hanning(len(x))
    if demean == "plain":
        xb = x - x.mean()
    elif demean == "hann":
        xb = x - (w * x).sum() / w.sum()
    else:
        xb = x
    X = np.abs(np.fft.rfft(xb * w))
    return np.fft.rfftfreq(len(x), dt), 2 * X / w.sum()


def run(fc=2000.0, eps=0.5, tau=0.2e-3, dt=1.5e-5, t_set=4.0, t_meas=4.0, sample="before"):
    vfp, g0, w0 = jac_eig(K.p, K.C); F0 = w0 / (2 * np.pi)
    f1, f2 = fc - F0 / 2, fc + F0 / 2
    Y = np.zeros((1, 7)); t = 0.0
    ns, nm = int(t_set / dt), int(t_meas / dt)
    tau_a = np.array([tau]); direct = np.array([False])
    t0 = time.perf_counter()
    for _ in range(ns):
        Y = step2(Y, t, dt, f1, f2, eps, tau_a, direct); t += dt
    vv = np.empty(nm); tt = np.empty(nm)
    for k in range(nm):
        if sample == "before":
            tt[k] = t; vv[k] = Y[0, 1] - Y[0, 2]
        Y = step2(Y, t, dt, f1, f2, eps, tau_a, direct); t += dt
        if sample == "after":
            tt[k] = t; vv[k] = Y[0, 1] - Y[0, 2]
    EE = field2(tt, f1, f2, eps)
    return dict(f1=f1, f2=f2, F0=F0, vfp=vfp, gamma=g0, t=tt, v=vv, E=EE,
                wall_s=time.perf_counter() - t0, fc=fc, eps=eps, tau=tau, dt=dt,
                t_set=t_set, t_meas=t_meas, ns=ns, nm=nm)


def compare(res, cache_path, demean="plain"):
    c = np.load(cache_path)
    fI, PI = amp_spectrum(res["E"], res["dt"], demean=demean)
    fV, PV = amp_spectrum(res["v"], res["dt"], demean=demean)
    out = dict(n_bins=int(len(fI)), n_bins_cache=int(len(c["fI"])))
    if len(fI) != len(c["fI"]):
        return out
    out.update(
        f_grid_max_abs_diff=float(np.max(np.abs(fI - c["fI"]))),
        f1_diff=float(res["f1"] - float(c["f1"])), f2_diff=float(res["f2"] - float(c["f2"])),
        F0_diff=float(res["F0"] - float(c["F0"])),
        PI_max_abs_diff=float(np.max(np.abs(PI - c["PI"]))), PI_max=float(c["PI"].max()),
        PV_max_abs_diff=float(np.max(np.abs(PV - c["PV"]))), PV_max=float(c["PV"].max()),
        PV_rel_diff_at_line=float(abs(PV[c["PV"].argmax()] - c["PV"].max()) / c["PV"].max()),
        line_bin_Hz=float(fV[c["PV"].argmax()]), line_amp_mV=float(PV[c["PV"].argmax()]),
        line_amp_cache_mV=float(c["PV"].max()),
        input_8_14_max=float(PI[(fI > 8) & (fI < 14)].max()),
        input_8_14_max_cache=float(c["PI"][(c["fI"] > 8) & (c["fI"] < 14)].max()),
        PV_DC_bin=float(PV[0]), PV_DC_bin_cache=float(c["PV"][0]))
    return out


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--t-set", type=float, default=4.0)
    ap.add_argument("--eps", type=float, default=0.5)
    ap.add_argument("--sample", default="before", choices=["after", "before"])
    ap.add_argument("--demean", default="plain", choices=["plain", "hann", "none"])
    ap.add_argument("--compare", action="store_true")
    ap.add_argument("--write", default="", help="save the fresh spectra to this .npz (never khz_twotone.npz)")
    ap.add_argument("--json", default="", help="write the comparison record to this path")
    a = ap.parse_args()
    res = run(eps=a.eps, t_set=a.t_set, sample=a.sample)
    print(f"operating point v*={res['vfp']:.3f} mV, gamma={res['gamma']:.3f} s^-1, F0={res['F0']:.6f} Hz, "
          f"f1={res['f1']:.6f}, f2={res['f2']:.6f}; settle {res['ns']} steps, measure {res['nm']} steps; {res['wall_s']:.0f} s")
    if a.compare:
        out = compare(res, os.path.join(HERE, "khz_twotone.npz"), demean=a.demean)
        out.update(settings=dict(eps=a.eps, t_set=a.t_set, sample=a.sample, demean=a.demean,
                                 fc=res["fc"], tau=res["tau"], dt=res["dt"], t_meas=res["t_meas"]))
        print(json.dumps(out, indent=1))
        if a.json:
            with open(a.json, "w") as f:
                json.dump(out, f, indent=1)
    if a.write:
        assert os.path.basename(a.write) != "khz_twotone.npz"
        fI, PI = amp_spectrum(res["E"], res["dt"], demean=a.demean)
        fV, PV = amp_spectrum(res["v"], res["dt"], demean=a.demean)
        np.savez(a.write, fI=fI, PI=PI, fV=fV, PV=PV, f1=res["f1"], f2=res["f2"], F0=res["F0"],
                 eps=a.eps, tau=res["tau"], dt=res["dt"], t_set=a.t_set, t_meas=res["t_meas"],
                 p=K.p, C=K.C, sample=a.sample, demean=a.demean)
        print("wrote", a.write)
