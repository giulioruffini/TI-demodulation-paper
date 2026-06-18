"""Figures + verification for the JR envelope-demodulation/resonance demo."""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from jr_demod import integrate, steady_v, Sigm
import os
FIGS = os.environ.get("TN_FIGDIR") or os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "figures")
os.makedirs(FIGS, exist_ok=True)

F0 = 11.1                      # natural (Hopf) frequency, Hz
fc, m, dt = 100.0, 1.0, 2e-4

# NOTE: fig_resonance is produced by rerun_resonance.py (long 20 s lock-in window);
# this script makes only the demodulation-sanity and verification figures.

# ---------- Figure: demodulation sanity (time + spectra) ----------
p0 = np.array([330.0]); Om0 = np.array([2*np.pi*F0])
amp, t, v, s = integrate(p0, Om0, eps=1.0, m=m, fc=fc,
                         t_settle=10.0, t_meas=3.0, dt=dt, record=True)
fs = 1.0/dt
def spec(x):
    x = x - x.mean(); w = np.hanning(len(x)); X = np.fft.rfft(x*w)
    f = np.fft.rfftfreq(len(x), dt); P = np.abs(X)/ (w.sum()/2)
    return f, P
fI, PI = spec(s); fV, PV = spec(v)

fig2, ax = plt.subplots(2, 2, figsize=(11, 6))
w0 = (t >= t[0]) & (t <= t[0]+0.5)
ax[0,0].plot(t[w0]-t[0], s[w0], color="#888", lw=0.6)
env = 1.0*(1+m*np.cos(2*np.pi*F0*t[w0]))
ax[0,0].plot(t[w0]-t[0], env, color="#c44", lw=1.5, label="envelope $1+m\\cos\\Omega t$")
ax[0,0].set_title("Input AM field $s(t)$  ($f_c=100$ Hz, $\\Omega/2\\pi=11.1$ Hz)", fontsize=10)
ax[0,0].set_xlabel("time (s)"); ax[0,0].set_ylabel("mV"); ax[0,0].legend(fontsize=8, frameon=False)

ax[1,0].plot(t[w0]-t[0], v[w0], color="#1b3a6b", lw=1.2)
ax[1,0].set_title("Output $v=y_1-y_2$ : oscillates at the envelope freq", fontsize=10)
ax[1,0].set_xlabel("time (s)"); ax[1,0].set_ylabel("mV")

ax[0,1].semilogy(fI, PI+1e-9, color="#888")
ax[0,1].set_xlim(0,130); ax[0,1].set_ylim(1e-4, None)
ax[0,1].axvspan(8,13, color="#c44", alpha=0.12)
ax[0,1].set_title("Input spectrum: lines at 100, 100$\\pm$11 Hz only", fontsize=10)
ax[0,1].set_xlabel("Hz")
for fline in [fc-F0, fc, fc+F0]:
    ax[0,1].axvline(fline, color="#bbb", ls="--", lw=0.7)

ax[1,1].semilogy(fV, PV+1e-9, color="#1b3a6b")
ax[1,1].set_xlim(0,130); ax[1,1].set_ylim(1e-4, None)
ax[1,1].axvspan(8,13, color="#c44", alpha=0.12)
ax[1,1].set_title("Output spectrum: strong peak at $\\Omega\\approx11$ Hz (demodulated)", fontsize=10)
ax[1,1].set_xlabel("Hz")
fig2.tight_layout(); fig2.savefig(f"{FIGS}/fig_demodulation.png", dpi=150); fig2.savefig(f"{FIGS}/fig_demodulation.pdf")
print("wrote fig_demodulation")

# ---------- Verification ----------
print("\n=== VERIFICATION ===")
# (1) square law: response ~ eps^2 at small drive (well-damped p=395)
epsv = np.array([0.05,0.1,0.2,0.4,0.8])
pv = np.full_like(epsv, 395.0); Omv = np.full_like(epsv, 2*np.pi*10.9)
resp = np.array([integrate(np.array([pv[i]]), np.array([Omv[i]]), epsv[i], m, fc,
                           8.0, 3.0, dt)[0] for i in range(len(epsv))])
sl = np.polyfit(np.log(epsv[:3]), np.log(resp[:3]), 1)[0]
print(f"square-law: log-log slope (small eps) = {sl:.2f}  (expect ~2)")
for e,rr in zip(epsv,resp): print(f"   eps={e:.2f}  resp={rr:.4f} mV")

# (2) linear control: linearize the field sigmoid -> demodulation must vanish
p1 = np.array([330.0]); Om1 = np.array([2*np.pi*F0])
vop, S1 = steady_v(p1)
r_nl = integrate(p1, Om1, 1.0, m, fc, 10.0, 3.0, dt)[0]
r_li = integrate(p1, Om1, 1.0, m, fc, 10.0, 3.0, dt, lin=(vop, S1))[0]
print(f"linear control @p=330, Omega=f0:  nonlinear={r_nl:.4f} mV   "
      f"linearized={r_li:.6f} mV   ratio={r_nl/max(r_li,1e-12):.0f}x")

# verification figure
fig3, ax3 = plt.subplots(1, 2, figsize=(10, 3.8))
ax3[0].loglog(epsv, resp, "o-", color="#1b3a6b")
ax3[0].loglog(epsv, resp[0]*(epsv/epsv[0])**2, "k--", lw=1, label="slope 2 (square law)")
ax3[0].set_xlabel("field amplitude $\\varepsilon$ (mV)"); ax3[0].set_ylabel("response @ $\\Omega$ (mV)")
ax3[0].set_title("Square-law demodulation\n(response $\\propto\\varepsilon^2$ at small drive)", fontsize=10)
ax3[0].legend(fontsize=8, frameon=False); ax3[0].spines[["top","right"]].set_visible(False)
ax3[1].bar(["nonlinear\nsigmoid","linearized\nsigmoid"], [r_nl, r_li],
           color=["#1b3a6b","#c44"])
ax3[1].set_ylabel("response @ $\\Omega$ (mV)")
ax3[1].set_title("Nonlinearity is essential\n(linearized sigmoid: no demodulation)", fontsize=10)
ax3[1].spines[["top","right"]].set_visible(False)
fig3.tight_layout(); fig3.savefig(f"{FIGS}/fig_verification.png", dpi=150); fig3.savefig(f"{FIGS}/fig_verification.pdf")
print("wrote fig_verification")
