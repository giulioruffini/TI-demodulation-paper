"""
Exact mean-field NMM2 PING (pyramidal--interneuron gamma) under an AM field.

Third model in TN0484, after the heuristic single-column Jansen--Rit (NMM1) and the
laminar LaNMM (NMM1): here the firing-rate nonlinearity is *derived* (the quadratic
v^2 term of the Montbrio--Pazo--Roxin mean field), not a postulated sigmoid. We show
the same mechanism --- square-law demodulation of an AM field, resonantly amplified
near a Hopf bifurcation --- in the exact next-generation theory, now at gamma.

Model: two-population E--I push--pull motif with second-order (AMPA/GABA) synapses,
in the exact (dimensional) MPR form used by Raul Palma's AUTO continuation
(qifnmm.f90) and direct integration (ping_nmm2.py):

    tau_e r_e' = Delta/(pi tau_e) + 2 r_e v_e
    tau_e v_e' = eta - (pi tau_e r_e)^2 + v_e^2 + F(t)  + tau_e * C (A_ee s_e - A_ei s_i)
    tau_i r_i' = Delta/(pi tau_i) + 2 r_i v_i
    tau_i v_i' = eta - (pi tau_i r_i)^2 + v_i^2         + tau_i * C (A_ie s_e - A_ii s_i)

with tau=(tau_e,tau_a,tau_i,tau_g)=(15,10,7.5,2.5), A=(A_ee,A_ei,A_ie,A_ii)=(1,1,1,2),
global coupling C=15, Delta=1, and second-order synapses s_e=K_a[r_e] (tau_a),
s_i=K_g[r_i] (tau_g), each obeying tau^2 s'' + 2 tau s' + s = r.

IMPORTANT (vs. the earlier reconstruction): the bifurcation parameter is the common
background drive **eta** (in BOTH populations) --- there is NO separate excitatory
current "I". Sweeping eta opens a supercritical Hopf at eta ~ 1 (gamma onset f0 ~ 55 Hz,
peak r_e ~ 0.53 at eta ~ 11), reproducing Raul's published PING bifurcation. Every
tau-scaling of the canonical MPR form is kept: the (pi tau r)^2 curvature term, the
Delta/(pi tau) rate term, and the tau-scaled synaptic coupling. Time unit ~ 1 ms, so
frequencies are in Hz (cycles/time-unit x 1000). The AM electric field enters the
excitatory membrane current, F(t)=A[1+cos Omega t]cos(w_c t) (MPR coupling
delta V = lambda.E), and is rectified by the exact quadratic v_e^2 term.

State (vectorized over a parameter grid):
   0 r_e  1 v_e   2 r_i  3 v_i   4 s_e 5 z_e (AMPA, K[r_e])   6 s_i 7 z_i (GABA, K[r_i])

Self-contained: numpy + matplotlib only.
"""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm

# --- NMM2-PING parameters (Raul Palma AUTO model qifnmm.f90 / ping_nmm2.py) ---
TAU_E, TAU_A, TAU_I, TAU_G = 15.0, 10.0, 7.5, 2.5
A_EE, A_EI, A_IE, A_II = 1.0, 1.0, 1.0, 2.0      # synaptic weights A=(1,1,1,2)
C = 15.0                                          # global coupling
DEL = 1.0                                         # Delta (half-width)
PI = np.pi
FIGDIR = os.environ.get("TN_FIGDIR") or os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "figures")


def _rhs(y, t, eta, A, wO, wc):
    """RHS of the 8-D system, vectorized over the last axis. eta is the common
    background drive (bifurcation parameter); F drives the E membrane current."""
    r_e, v_e, r_i, v_i, s_e, z_e, s_i, z_i = y
    F = A*(1.0 + np.cos(wO*t))*np.cos(wc*t) if A != 0.0 else 0.0
    return np.array([
        (DEL/(PI*TAU_E) + 2*r_e*v_e)/TAU_E,
        (eta - (PI*TAU_E*r_e)**2 + v_e**2 + F)/TAU_E + C*(A_EE*s_e - A_EI*s_i),
        (DEL/(PI*TAU_I) + 2*r_i*v_i)/TAU_I,
        (eta - (PI*TAU_I*r_i)**2 + v_i**2)/TAU_I   + C*(A_IE*s_e - A_II*s_i),
        z_e/TAU_A, (r_e - 2*z_e - s_e)/TAU_A,
        z_i/TAU_G, (r_i - 2*z_i - s_i)/TAU_G,
    ])


def _init(n):
    """Small-amplitude (from-rest) init on the stable-focus side."""
    y = np.zeros((8, n)); y[0]=0.05; y[1]=-2.0; y[2]=0.05; y[3]=-2.0; y[4]=0.05; y[6]=0.05
    return y


def _rk4(y, t, dt, *args):
    k1=_rhs(y,t,*args); k2=_rhs(y+0.5*dt*k1,t+0.5*dt,*args)
    k3=_rhs(y+0.5*dt*k2,t+0.5*dt,*args); k4=_rhs(y+dt*k3,t+dt,*args)
    return y+(dt/6.0)*(k1+2*k2+2*k3+k4)


# ============================================================
# field-free bifurcation scan (to locate the gamma Hopf in eta)
# ============================================================
def bifurcation(etagrid, T=2000.0, dt=0.02, t_meas=500.0):
    """Field-free min/max of r_e vs eta; returns (re_min, re_max, f_onset_Hz)."""
    etagrid = np.asarray(etagrid, float); n = len(etagrid); y = _init(n)
    nset = int((T-t_meas)/dt); nmeas = int(t_meas/dt)
    t = 0.0
    for _ in range(nset): y = _rk4(y, t, dt, etagrid, 0.0, 0.0, 0.0); t += dt
    rmin = np.full(n, np.inf); rmax = np.full(n, -np.inf); buf = []
    for k in range(nmeas):
        y = _rk4(y, t, dt, etagrid, 0.0, 0.0, 0.0); t += dt
        rmin = np.minimum(rmin, y[0]); rmax = np.maximum(rmax, y[0])
        if k % 4 == 0: buf.append(y[0].copy())
    buf = np.array(buf); amp = rmax - rmin
    # onset frequency: first oscillating eta, dominant freq of r_e
    f_onset = np.nan
    osc = np.where(amp > 1e-3)[0]
    if len(osc):
        j = osc[0]; x = buf[:, j] - buf[:, j].mean()
        fr = np.fft.rfftfreq(len(x), d=dt*4); P = np.abs(np.fft.rfft(x*np.hanning(len(x))))
        f_onset = fr[1+np.argmax(P[1:])]*1000.0
    return rmin, rmax, f_onset


# ============================================================
# AM-driven lock-in over a (Delta f, eta) grid
# ============================================================
def lockin_map(etagrid, dfgrid_Hz, A=8.0, fc_Hz=300.0, t_settle=800.0, t_meas=1500.0, dt=0.05):
    """Lock-in amplitude of r_e at the envelope frequency, over the outer grid
    (etagrid x dfgrid). Returns array of shape (len(etagrid), len(dfgrid_Hz))."""
    EE, DD = np.meshgrid(etagrid, dfgrid_Hz, indexing="ij")
    eta = EE.ravel().copy(); dfflat = DD.ravel().copy()
    n = eta.size; y = _init(n)
    wc = 2*PI*(fc_Hz/1000.0); wO = 2*PI*(dfflat/1000.0)
    nset = int(t_settle/dt); nmeas = int(t_meas/dt); t = 0.0
    for _ in range(nset): y = _rk4(y, t, dt, eta, A, wO, wc); t += dt
    buf = np.empty((nmeas, n)); ts = np.empty(nmeas)
    for k in range(nmeas):
        y = _rk4(y, t, dt, eta, A, wO, wc); t += dt
        buf[k] = y[0]; ts[k] = t
    w = np.hanning(nmeas)[:, None]
    bar = (w*buf).sum(0)/w.sum()
    c = np.cos(wO[None, :]*ts[:, None]); s = np.sin(wO[None, :]*ts[:, None])
    Iq = 2*(w*(buf-bar)*c).sum(0)/w.sum(); Qq = 2*(w*(buf-bar)*s).sum(0)/w.sum()
    return np.sqrt(Iq**2+Qq**2).reshape(EE.shape)


def lockin_curve(eta0, dfgrid_Hz, A=8.0, fc_Hz=300.0, t_settle=800.0, t_meas=1500.0, dt=0.05):
    """Resonance curve at a single eta (vectorized over Delta f)."""
    return lockin_map(np.array([eta0]), dfgrid_Hz, A=A, fc_Hz=fc_Hz,
                      t_settle=t_settle, t_meas=t_meas, dt=dt)[0]


# ============================================================
# figures: resonance curves (analog of JR Fig. res) + map (analog of Fig. map)
# ============================================================
def make_figures(A=8.0, fc_Hz=300.0):
    os.makedirs(FIGDIR, exist_ok=True)
    etagrid = np.linspace(-5.0, 30.0, 36)
    dfgrid = np.linspace(30.0, 110.0, 81)
    # locate Hopf (field-free) in eta
    rmin, rmax, f_onset = bifurcation(etagrid)
    amp_bif = rmax - rmin
    iH = np.where(amp_bif > 1e-3)[0]
    eta_hopf = etagrid[iH[0]] if len(iH) else np.nan
    print(f"gamma Hopf near eta={eta_hopf:.2f}, onset f0~{f_onset:.0f} Hz")
    # lock-in map
    M = lockin_map(etagrid, dfgrid, A=A, fc_Hz=fc_Hz)

    # ---- Fig.: resonance map (log scale: entrainment >> stable-focus forced response) ----
    fig, ax = plt.subplots(figsize=(6.4, 4.6))
    im = ax.imshow(M, origin="lower", aspect="auto", cmap="viridis",
                   norm=LogNorm(vmin=max(M.max()*1e-3, 1e-5), vmax=M.max()),
                   extent=[dfgrid[0], dfgrid[-1], etagrid[0], etagrid[-1]])
    if np.isfinite(eta_hopf):
        ax.axhline(eta_hopf, color="w", ls="--", lw=1)
        ax.text(dfgrid[-1]-2, eta_hopf+0.6, "Hopf", color="w", ha="right", fontsize=8)
    ax.set_xlabel(r"envelope frequency $\Delta f$ (Hz)")
    ax.set_ylabel(r"background drive $\bar\eta$ (bifurcation parameter)")
    ax.set_title("NMM2 PING: demodulated response over $(\\Delta f,\\,\\bar\\eta)$", fontsize=10)
    plt.colorbar(im, ax=ax, label=r"lock-in response at $\Delta f$ (a.u.)")
    fig.tight_layout()
    fig.savefig(os.path.join(FIGDIR, "fig_nmm2_map.png"), dpi=150)
    fig.savefig(os.path.join(FIGDIR, "fig_nmm2_map.pdf")); plt.close(fig)

    # ---- Fig.: resonance curves (stable side | limit-cycle side) ----
    stable = [-2.0, 0.0, 0.7, 0.9]
    cycle = [2.0, 5.0, 11.0]
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(11, 4.2), sharey=False)
    for e0 in stable:
        a1.plot(dfgrid, lockin_curve(e0, dfgrid, A=A, fc_Hz=fc_Hz), label=f"$\\bar\\eta={e0:g}$")
    a1.set_title(f"Stable focus ($\\bar\\eta<\\bar\\eta_{{\\rm Hopf}}\\approx{eta_hopf:.0f}$): forced resonance",
                 fontsize=10)
    a1.set_xlabel(r"envelope frequency $\Delta f$ (Hz)")
    a1.set_ylabel(r"lock-in response at $\Delta f$ (a.u.)")
    a1.legend(fontsize=8, title="approaching Hopf")
    for e0 in cycle:
        a2.plot(dfgrid, lockin_curve(e0, dfgrid, A=A, fc_Hz=fc_Hz), label=f"$\\bar\\eta={e0:g}$")
    a2.set_title(r"Limit cycle ($\bar\eta>\bar\eta_{\rm Hopf}$): entrainment of gamma", fontsize=10)
    a2.set_xlabel(r"envelope frequency $\Delta f$ (Hz)")
    a2.legend(fontsize=8)
    fig.suptitle(f"NMM2 PING gamma resonance (carrier $f_c={fc_Hz:.0f}$ Hz)", fontsize=11)
    fig.tight_layout(rect=[0, 0, 1, 0.96])
    fig.savefig(os.path.join(FIGDIR, "fig_nmm2_resonance.png"), dpi=150)
    fig.savefig(os.path.join(FIGDIR, "fig_nmm2_resonance.pdf")); plt.close(fig)
    print("wrote fig_nmm2_resonance and fig_nmm2_map")
    return eta_hopf, f_onset


if __name__ == "__main__":
    make_figures()
