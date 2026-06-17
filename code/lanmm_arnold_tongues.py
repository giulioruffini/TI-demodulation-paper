"""
LaNMM envelope-resonance / Arnold-tongue pipeline  (TN0484, section "Realization
in the laminar neural mass model").

Reproduces the LaNMM figures merged into TN0484:
    fig_lanmm_arnold_p2.png  -- AM drive into the superficial P2 (gamma) loop
    fig_lanmm_arnold_p1.png  -- AM drive into the deep      P1 (alpha) loop
Each is a 2x2 grid:
    (a,b)  alpha-band power of P1, P2 vs (modulation amplitude A, beat Δf)  -> Arnold tongue
    (c,d)  alpha-band power of P1, P2 vs (carrier f_c, beat Δf) at fixed A    -> carrier map
(fig_lanmm_setup.png is a hand-drawn schematic, not generated here.)

-------------------------------------------------------------------------------
DEPENDENCY (not bundled): the LaNMM model module `lanmmv11.py`
-------------------------------------------------------------------------------
The only external dependency is the LaNMM implementation from
    https://github.com/giulioruffini/LaNMM_predictive_coding_paper  (python/lanmmv11.py)
Put that file on the PYTHONPATH (or next to this script). We use exactly three
symbols from it, with the signatures verified against the repo:
    get_intrinsic_params()                       -> dict of biophysical params
    get_driving_params()                         -> dict with e1/e2/pv baselines (mu)
    lanmm_ode_unified(Y, t, params, e1, e2, pv, t_array)   -> 28-D RHS
and the column read-outs (per that ODE's docstring):
    vP1 = u(1)+u(2)+u(3)+u(11)     vP2 = u(6)+u(7)+u(8)+u(12)     u(s)=Y[2(s-1)]

Notes
- The repo's built-in `'am'` drive mode is a *noise*-modulated nested-AM signal
  (used for the HAM/CFC work). The Arnold-tongue analysis instead needs a
  *deterministic* single-tone AM, A[1+cos Ωt]cos(ω_c t), so we build that drive
  explicitly and integrate `lanmm_ode_unified` directly (as in the original
  analysis). `run_unified_simulation(...)` is the repo's wrapper for the noise-AM case.
- Alpha-band power is computed inline (band-pass + Hilbert envelope), matching the
  read-out described in the note, so no analyzer module is required.

Requirements: numpy, scipy, matplotlib (+ lanmmv11.py).
"""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from scipy.signal import butter, sosfiltfilt, hilbert, welch

try:                                   # external LaNMM model (see header)
    import lanmmv11 as lanmm
    _HAVE_LANMM = True
except ImportError:                    # allow import/inspection without the dep
    lanmm = None
    _HAVE_LANMM = False

FIGDIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "paper", "figures")
ALPHA_BAND = (8.0, 12.0)               # Hz, read-out band (deep P1 alpha)


# ============================================================
# alpha-band power: band-pass + Hilbert envelope (self-contained)
# ============================================================
def alpha_power(v, dt, band=ALPHA_BAND):
    """Time-averaged squared Hilbert envelope of v band-passed to `band`.
    Phase-robust read-out, well suited to the entrainment regime."""
    fs = 1.0/dt; nyq = 0.5*fs
    sos = butter(4, [band[0]/nyq, band[1]/nyq], btype="band", output="sos")
    env = np.abs(hilbert(sosfiltfilt(sos, v)))
    return float(np.mean(env**2))


# ============================================================
# one simulation under a deterministic AM drive
# ============================================================
def simulate_am_drive(intrinsic, driving, A_mod, f_slow, f_fast=40.0, phi=0.0,
                      tmax=3.0, dt=2e-3, discard=1.0, drive_target="P2",
                      rtol=1e-6, atol=1e-6):
    """Integrate one LaNMM column with the AM drive
        e(t) = mu + A_mod [1 + cos(2π f_slow t)] cos(2π f_fast t + phi)
    injected into `drive_target` ("P2"->e2 or "P1"->e1); other inputs stay flat.
    Returns post-transient (t, vP1, vP2)."""
    t = np.arange(0.0, tmax, dt)
    e1 = np.full_like(t, driving["e1"]["mu"])
    e2 = np.full_like(t, driving["e2"]["mu"])
    pv = np.full_like(t, driving["pv"]["mu"])

    am = A_mod*(1.0 + np.cos(2*np.pi*f_slow*t))*np.cos(2*np.pi*f_fast*t + phi)
    if drive_target == "P2":
        e2 = e2 + am
    else:
        e1 = e1 + am
    e1, e2, pv = (np.clip(x, 0.0, None) for x in (e1, e2, pv))   # firing rates >= 0

    sol = solve_ivp(lambda tt, y: lanmm.lanmm_ode_unified(y, tt, intrinsic, e1, e2, pv, t),
                    (t[0], t[-1]), np.zeros(28), method="RK45",
                    t_eval=t, rtol=rtol, atol=atol)
    X = sol.y.T
    u = lambda s: X[:, 2*(s-1)]
    vP1 = u(1) + u(2) + u(3) + u(11)            # deep pyramidal (P1) proxy
    vP2 = u(6) + u(7) + u(8) + u(12)            # superficial pyramidal (P2) proxy
    m = t >= discard
    return t[m], vP1[m], vP2[m]


# ============================================================
# the two map types
# ============================================================
def arnold_tongue(intrinsic, driving, f_slow=np.linspace(5, 15, 41),
                  A=np.linspace(0, 300, 31), f_fast=40.0, drive_target="P2", **kw):
    """(a,b): alpha power of P1,P2 over (A, Δf) at fixed carrier."""
    P1 = np.zeros((len(A), len(f_slow))); P2 = np.zeros_like(P1)
    for i, a in enumerate(A):
        for j, fs in enumerate(f_slow):
            t, v1, v2 = simulate_am_drive(intrinsic, driving, a, fs, f_fast,
                                          drive_target=drive_target, **kw)
            dt = t[1]-t[0]
            P1[i, j] = alpha_power(v1, dt); P2[i, j] = alpha_power(v2, dt)
    return P1, P2, f_slow, A

def carrier_map(intrinsic, driving, f_slow=np.linspace(5, 15, 41),
                f_carrier=np.linspace(25, 80, 56), A_mod=250.0, drive_target="P2", **kw):
    """(c,d): alpha power of P1,P2 over (carrier f_c, Δf) at fixed A.
    Completes the published 4-panel figure (the original sweep produced only a,b)."""
    P1 = np.zeros((len(f_carrier), len(f_slow))); P2 = np.zeros_like(P1)
    for i, fc in enumerate(f_carrier):
        for j, fs in enumerate(f_slow):
            t, v1, v2 = simulate_am_drive(intrinsic, driving, A_mod, fs, fc,
                                          drive_target=drive_target, **kw)
            dt = t[1]-t[0]
            P1[i, j] = alpha_power(v1, dt); P2[i, j] = alpha_power(v2, dt)
    return P1, P2, f_slow, f_carrier


# ============================================================
# plotting -> 4-panel figure (matches fig_lanmm_arnold_*)
# ============================================================
def _imshow(ax, M, x, y, title, ylabel):
    im = ax.imshow(M, origin="lower", aspect="auto",
                   extent=[x[0], x[-1], y[0], y[-1]], cmap="viridis")
    ax.axvline(10.0, color="w", ls="--", lw=1)
    ax.set_title(title, fontsize=10)
    ax.set_xlabel("envelope frequency $\\Delta f$ (Hz)"); ax.set_ylabel(ylabel)
    plt.colorbar(im, ax=ax, label="alpha power (8–12 Hz)")

def make_figure(intrinsic, driving, drive_target="P2", A_for_carrier=250.0):
    Pt1, Pt2, fs_t, A = arnold_tongue(intrinsic, driving, drive_target=drive_target)
    Pc1, Pc2, fs_c, fc = carrier_map(intrinsic, driving, A_mod=A_for_carrier,
                                     drive_target=drive_target)
    fig, ax = plt.subplots(2, 2, figsize=(11, 9))
    _imshow(ax[0,0], Pt1, fs_t, A,  "(a) P1 alpha-band power", "modulation amplitude $A$")
    _imshow(ax[0,1], Pt2, fs_t, A,  "(b) P2 alpha-band power", "modulation amplitude $A$")
    _imshow(ax[1,0], Pc1, fs_c, fc, "(c) P1 alpha-band power", "carrier frequency $f_c$ (Hz)")
    _imshow(ax[1,1], Pc2, fs_c, fc, "(d) P2 alpha-band power", "carrier frequency $f_c$ (Hz)")
    fig.suptitle(f"LaNMM Arnold tongues — AM drive into {drive_target}", fontsize=12)
    fig.tight_layout(rect=[0, 0, 1, 0.97])
    out = f"fig_lanmm_arnold_{'p2' if drive_target=='P2' else 'p1'}"
    os.makedirs(FIGDIR, exist_ok=True)
    fig.savefig(os.path.join(FIGDIR, out+".png"), dpi=150)
    fig.savefig(os.path.join(FIGDIR, out+".pdf"))
    print("wrote", out)


# ============================================================
# optional time/PSD sanity check
# ============================================================
def checker(intrinsic, driving, f_slow=10.0, f_fast=40.0, A_mod=250.0,
            drive_target="P2", tmax=6.0, dt=1e-3, discard=2.0):
    t, v1, v2 = simulate_am_drive(intrinsic, driving, A_mod, f_slow, f_fast,
                                  tmax=tmax, dt=dt, discard=discard, drive_target=drive_target)
    fig, ax = plt.subplots(1, 3, figsize=(15, 4))
    w = (t >= t[0]+1) & (t <= t[0]+3)
    ax[0].plot(t[w], v1[w], label="P1"); ax[0].plot(t[w], v2[w], label="P2", alpha=0.7)
    ax[0].plot(t[w], np.cos(2*np.pi*f_slow*t[w]), "k", lw=1, label="envelope")
    ax[0].set_title("time series"); ax[0].set_xlabel("t (s)"); ax[0].legend(fontsize=8)
    for a, v, c, lab in ((ax[1], v1, "g", "P1"), (ax[2], v2, "r", "P2")):
        f, p = welch(v, fs=1.0/dt, nperseg=int(4.0/dt))
        a.semilogy(f, p, color=c); a.set_xlim(0, 80); a.set_title(f"{lab} PSD"); a.set_xlabel("Hz")
    fig.tight_layout(); fig.savefig(os.path.join(FIGDIR, "fig_lanmm_checker.png"), dpi=150)
    print("wrote fig_lanmm_checker")


if __name__ == "__main__":
    if not _HAVE_LANMM:
        raise SystemExit("lanmmv11.py not found on the PYTHONPATH — clone "
                         "github.com/giulioruffini/LaNMM_predictive_coding_paper "
                         "and put python/lanmmv11.py next to this script.")
    intrinsic = lanmm.get_intrinsic_params()
    driving   = lanmm.get_driving_params()
    make_figure(intrinsic, driving, drive_target="P2")   # -> fig_lanmm_arnold_p2
    make_figure(intrinsic, driving, drive_target="P1")   # -> fig_lanmm_arnold_p1
    checker(intrinsic, driving)
