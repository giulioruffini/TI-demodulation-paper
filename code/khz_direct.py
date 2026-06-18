"""Direct kHz single-column run (Jansen-Rit, closed loop). Pre-empts 'the demo is
only at 100 Hz': the full recurrent column demodulates a genuine kHz-carrier AM field
and resonates at the recovered alpha envelope -- PROVIDED the field reaches the
nonlinearity through a fast element. The applied field is low-passed by an explicit
membrane filter (1st-order, time constant tau, integrated as an extra state) BEFORE
it enters the pyramidal sigmoid, for three coupling routes:
  direct (tau->0), fast element / axon-AIS-node (tau=0.2 ms), soma/dendrite (tau=16 ms).
Panel (a): closed-loop demodulated A_Omega(f_c) for the three routes -- direct flat,
fast element survives into the kHz band, soma collapses ~1/f_c^2. Panel (b): the
output spectrum for a 2 kHz carrier through the fast element -- a clean alpha line,
synthesized by the column though the input has zero alpha power.

Self-contained (pure numpy; no scipy). JR constants/operating point match the rest
of the repo; the 100 Hz demo is jr_demod.py / Fig. demodulation."""
import numpy as np, os, sys
import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
import figstyle; figstyle.apply()
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from timing_not_rate import A, a, B, b, v0, e0, rr, Sigm, jac_eig, _fp_v

HERE = os.path.dirname(os.path.abspath(__file__))
FIGS = os.path.join(os.path.dirname(HERE), "figures")
NEBLUE = "#0a4f8c"; NEGREEN = "#1a9850"; NERED = "#b3361f"; GR = "#555555"
C = 135.0; p = 400.0; m = 1.0; eps = 0.5
C1, C2, C3, C4 = C, 0.8*C, 0.25*C, 0.25*C

def rhs7(Y, E, tau, direct):
    """7-state JR: 6 JR states + filtered field xf. E = applied field at this time
    (per column). For 'direct' columns the sigmoid sees E itself (no filter state)."""
    y0, y1, y2, y3, y4, y5, xf = Y.T
    fin = np.where(direct, E, xf)                 # field reaching the nonlinearity
    d = np.empty_like(Y)
    d[:, 0] = y3; d[:, 1] = y4; d[:, 2] = y5
    d[:, 3] = A*a*Sigm(y1-y2+fin) - 2*a*y3 - a*a*y0
    d[:, 4] = A*a*(p+C2*Sigm(C1*y0)) - 2*a*y4 - a*a*y1
    d[:, 5] = B*b*(C4*Sigm(C3*y0)) - 2*b*y5 - b*b*y2
    d[:, 6] = np.where(direct, 0.0, (-xf + E)/tau)
    return d

def Efield(t, fc): return eps*(1+m*np.cos(Om*t))*np.cos(2*np.pi*fc*t)

def step(Y, t, dt, fc, tau, direct):
    k1 = rhs7(Y, Efield(t, fc), tau, direct)
    k2 = rhs7(Y+.5*dt*k1, Efield(t+.5*dt, fc), tau, direct)
    k3 = rhs7(Y+.5*dt*k2, Efield(t+.5*dt, fc), tau, direct)
    k4 = rhs7(Y+dt*k3, Efield(t+dt, fc), tau, direct)
    return Y + (dt/6)*(k1+2*k2+2*k3+k4)

def lockin_sweep(fc, tau, direct, dt, t_set, t_meas):
    N = len(fc); Y = np.zeros((N, 7)); t = 0.0
    ns = int(t_set/dt); nm = int(t_meas/dt)
    for _ in range(ns):
        Y = step(Y, t, dt, fc, tau, direct); t += dt
    w = np.hanning(nm); ws = w.sum()
    ac = np.zeros(N); as_ = np.zeros(N); av = np.zeros(N); awc = np.zeros(N); aws = np.zeros(N)
    for k in range(nm):
        Y = step(Y, t, dt, fc, tau, direct); t += dt
        v = Y[:, 1]-Y[:, 2]; co = np.cos(Om*t); si = np.sin(Om*t)
        ac += w[k]*v*co; as_ += w[k]*v*si; av += w[k]*v; awc += w[k]*co; aws += w[k]*si
    vb = av/ws; c = ac-vb*awc; s = as_-vb*aws
    return 2/ws*np.sqrt(c**2+s**2)

def trace(fc, tau, dt, t_set, t_meas):
    Y = np.zeros((1, 7)); t = 0.0; ns = int(t_set/dt); nm = int(t_meas/dt)
    direct = np.array([False])
    for _ in range(ns):
        Y = step(Y, t, dt, np.array([fc]), np.array([tau]), direct); t += dt
    vv = np.empty(nm)
    for k in range(nm):
        Y = step(Y, t, dt, np.array([fc]), np.array([tau]), direct); t += dt
        vv[k] = Y[0, 1]-Y[0, 2]
    return vv

if __name__ == "__main__":
    quick = "--quick" in sys.argv
    vfp, g0, w0 = jac_eig(p, C); F0 = w0/(2*np.pi)
    Om = 2*np.pi*F0
    print(f"operating point v*={vfp:.2f} mV, gamma={g0:.3f}, f0={F0:.2f} Hz")

    routes = [("direct ($\\tau\\!\\to\\!0$)", 0.0, True, NEBLUE),
              ("fast element  $\\tau\\!\\approx\\!0.2$ ms", 0.2e-3, False, NEGREEN),
              ("soma  $\\tau_m\\!\\approx\\!16$ ms", 16e-3, False, NERED)]
    fcs = np.geomspace(100., 4000., 4 if quick else 10)
    dt = 2e-5; t_set = 3.0 if quick else 6.0; t_meas = 1.5 if quick else 3.0

    # one vectorized pass over all (route x carrier) columns
    nf = len(fcs)
    fc_all = np.tile(fcs, len(routes))
    tau_all = np.concatenate([np.full(nf, (tau if tau > 0 else 1.0)) for _, tau, _, _ in routes])
    dir_all = np.concatenate([np.full(nf, isdir) for _, _, isdir, _ in routes])
    A_all = lockin_sweep(fc_all, tau_all, dir_all, dt, t_set, t_meas)
    curves = {name: A_all[i*nf:(i+1)*nf] for i, (name, *_ ) in enumerate(routes)}
    for name, *_ in routes:
        print(f"  {name:32s} A_Omega(100Hz)={curves[name][0]:.3e}  "
              f"A_Omega({fcs[-1]:.0f}Hz)={curves[name][-1]:.3e}")

    # Panel (b): output spectrum, 2 kHz carrier through the fast element
    dtb = 1.5e-5; vv = trace(2000.0, 0.2e-3, dtb, 2.0 if quick else 5.0, 1.0 if quick else 4.0)
    vv = vv - vv.mean(); win = np.hanning(len(vv))
    V = np.abs(np.fft.rfft(vv*win)); fr = np.fft.rfftfreq(len(vv), dtb)
    V /= V.max()

    fig, (axA, axB) = plt.subplots(1, 2, figsize=(9.4, 3.6))
    for name, tau, isdir, col in routes:
        axA.loglog(fcs, curves[name], "o-", ms=4, color=col, label=name)
    i1k = np.argmin(np.abs(fcs-1000))
    axA.loglog(fcs[fcs >= 700], curves[routes[2][0]][i1k]*(fcs[fcs >= 700]/1000.)**-2,
               "k--", lw=0.9, label=r"$\propto 1/f_c^2$")
    for f, lab in [(1000, "1k"), (2000, "2k")]:
        axA.axvline(f, color=GR, ls=":", lw=0.7)
    axA.set_xlabel(r"carrier frequency $f_c$ (Hz)")
    axA.set_ylabel(r"closed-loop demodulated $A_\Omega$ at $\Delta f$ (mV)")
    axA.set_title("(a) the column demodulates into the kHz band\nvia a fast element", fontsize=9)
    axA.legend(fontsize=7.5, frameon=False, loc="lower left")
    axA.spines[["top", "right"]].set_visible(False)

    axB.plot(fr, V, color=NEGREEN, lw=1.3)
    axB.axvspan(8, 12, color="0.85", zorder=0)
    axB.set_xlim(0, 40); axB.set_ylim(0, 1.05)
    axB.set_xlabel("output frequency (Hz)")
    axB.set_ylabel(r"$|V(f)|$ (norm.)")
    axB.set_title(f"(b) 2 kHz carrier, fast element:\nalpha line at {F0:.0f} Hz, recovered",
                  fontsize=9)
    axB.annotate(f"carrier 2 kHz\n(input alpha power = 0)", xy=(F0, 1.0),
                 xytext=(20, 0.7), fontsize=7.5, color=GR,
                 arrowprops=dict(arrowstyle="->", color=GR, lw=0.7))
    axB.spines[["top", "right"]].set_visible(False)

    fig.tight_layout()
    for ext in ("pdf", "png"):
        fig.savefig(os.path.join(FIGS, f"fig_khz_direct.{ext}"), dpi=300, bbox_inches="tight")
    print("wrote fig_khz_direct.pdf / .png")
