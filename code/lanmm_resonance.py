"""
LaNMM alpha resonance under an AM field --- the resonance-curve + map analog of the
JR figures (fig_resonance / fig_resonance_map) and the NMM2 figures, for the laminar
NMM1 model. The deep P1 (alpha) loop is driven directly; its input is the bifurcation
parameter (alpha Hopf near drive 390: high drive -> stable focus, low -> alpha cycle).

This is a self-contained, vectorized fixed-step integrator of the 14-synapse / 28-state
LaNMM (model + parameters transcribed from lanmmv11.py of
github.com/giulioruffini/LaNMM_predictive_coding_paper); it needs only numpy +
matplotlib, and integrates the whole (Delta f, drive) grid in one pass. The
Arnold-tongue / carrier analysis lives separately in lanmm_arnold_tongues.py.

Outputs: fig_lanmm_resonance.{png,pdf}, fig_lanmm_map.{png,pdf} in figures/.
"""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm

FIGDIR = os.environ.get("TN_FIGDIR") or os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "figures")
PI = np.pi
# 14 synapses (s=1..14): rates a, gains A, connectivities C
aS = np.array([100,50,100,100,100,100,220,100,100,220,100,100,100,100], float)
AS = np.array([3.25,-22,3.25,3.25,3.25,3.25,-30,3.25,3.25,-30,3.25,3.25,3.25,3.25], float)
CS = np.array([108,33.7,1,135,33.75,70,550,1,200,100,80,200,30,1], float)
FMAX, RSLOPE, V0D, V0P2 = 5.0, 0.56, 6.0, 1.0
CARRIER, A_MOD, E2_MU = 100.0, 80.0, 90.0          # P1 driven directly; P2 flat
MU = np.linspace(180.0, 640.0, 41)                  # P1 drive (bifurcation parameter)
DF = np.linspace(5.0, 16.0, 45)                     # envelope-frequency sweep (Hz)
I_HOPF = 390.0                                       # approximate alpha Hopf in drive


def _sig(v, v0):
    return FMAX/(1.0+np.exp(RSLOPE*(v0-v)))


def _rhs(Y, t, mu, df):
    u = Y[0::2]; z = Y[1::2]                          # (14, n)
    vP1 = u[0]+u[1]+u[2]+u[10]; vSS = u[3]; vSST = u[4]
    vP2 = u[5]+u[6]+u[7]+u[11]; vPV = u[8]+u[9]+u[12]+u[13]
    sP1 = _sig(vP1, V0D); sSS = _sig(vSS, V0D); sSST = _sig(vSST, V0D)
    sP2 = _sig(vP2, V0P2); sPV = _sig(vPV, V0D)
    e1 = np.clip(mu + A_MOD*(1+np.cos(2*PI*df*t))*np.cos(2*PI*CARRIER*t), 0, None)
    e2 = np.full_like(e1, E2_MU); pv = np.zeros_like(e1)
    presyn = np.stack([sSS, sSST, e1, sP1, sP1, sP2, sPV, e2, sP2, sPV, sP2, sP1, sP1, pv])
    dY = np.empty_like(Y)
    dY[0::2] = z
    dY[1::2] = aS[:,None]*AS[:,None]*(CS[:,None]*presyn) - 2*aS[:,None]*z - (aS**2)[:,None]*u
    return dY


def resonance_map(dt=5e-4, t_settle=8.0, t_meas=16.0):
    """Lock-in of vP1 at Delta f over the (drive, Delta f) grid."""
    II, DD = np.meshgrid(MU, DF, indexing="ij")
    mu = II.ravel(); df = DD.ravel()
    Y = np.zeros((28, mu.size)); t = 0.0
    def step(Y, t):
        k1=_rhs(Y,t,mu,df); k2=_rhs(Y+0.5*dt*k1,t+0.5*dt,mu,df)
        k3=_rhs(Y+0.5*dt*k2,t+0.5*dt,mu,df); k4=_rhs(Y+dt*k3,t+dt,mu,df)
        return Y+(dt/6)*(k1+2*k2+2*k3+k4)
    for _ in range(int(t_settle/dt)): Y = step(Y, t); t += dt
    nmeas = int(t_meas/dt); buf = np.empty((nmeas, mu.size)); ts = np.empty(nmeas)
    for k in range(nmeas):
        Y = step(Y, t); t += dt
        buf[k] = Y[0]+Y[2]+Y[4]+Y[20]                # vP1 = u1+u2+u3+u11
        ts[k] = t
    w = np.hanning(nmeas)[:,None]; bar = (w*buf).sum(0)/w.sum(); wO = 2*PI*df[None,:]
    Iq = 2*(w*(buf-bar)*np.cos(wO*ts[:,None])).sum(0)/w.sum()
    Qq = 2*(w*(buf-bar)*np.sin(wO*ts[:,None])).sum(0)/w.sum()
    return np.hypot(Iq, Qq).reshape(II.shape)


def make_figures():
    os.makedirs(FIGDIR, exist_ok=True)
    M = resonance_map()
    nearest = lambda m: int(np.argmin(np.abs(MU-m)))
    # ---- map (log scale: limit-cycle entrainment >> stable-focus forced response) ----
    fig, ax = plt.subplots(figsize=(6.4, 4.6))
    im = ax.imshow(M, origin="lower", aspect="auto", cmap="viridis",
                   norm=LogNorm(vmin=2e-3, vmax=M.max()),
                   extent=[DF[0], DF[-1], MU[0], MU[-1]])
    ax.axhline(I_HOPF, color="w", ls="--", lw=1)
    ax.text(DF[-1]-0.3, I_HOPF+10, "alpha Hopf", color="w", ha="right", fontsize=8)
    ax.set_xlabel(r"envelope frequency $\Delta f$ (Hz)")
    ax.set_ylabel(r"$P_1$ drive (bifurcation parameter)")
    ax.set_title(r"LaNMM: demodulated $P_1$ response over $(\Delta f,\,$drive$)$", fontsize=10)
    plt.colorbar(im, ax=ax, label=r"lock-in response at $\Delta f$ (mV)")
    fig.tight_layout()
    fig.savefig(os.path.join(FIGDIR, "fig_lanmm_map.png"), dpi=150)
    fig.savefig(os.path.join(FIGDIR, "fig_lanmm_map.pdf")); plt.close(fig)
    # ---- resonance curves ----
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(11, 4.2))
    for m in [600, 500, 430]:
        j = nearest(m); a1.plot(DF, M[j], label=f"drive$={MU[j]:.0f}$")
    a1.set_title(r"Stable focus (high drive $>$Hopf): forced alpha resonance", fontsize=10)
    a1.set_xlabel(r"envelope frequency $\Delta f$ (Hz)")
    a1.set_ylabel(r"lock-in response at $\Delta f$ (mV)")
    a1.legend(fontsize=8, title="approaching Hopf")
    for m in [340, 270, 210]:
        j = nearest(m); a2.plot(DF, M[j], label=f"drive$={MU[j]:.0f}$")
    a2.set_title(r"Limit cycle (low drive $<$Hopf): entrainment of alpha", fontsize=10)
    a2.set_xlabel(r"envelope frequency $\Delta f$ (Hz)"); a2.legend(fontsize=8)
    fig.suptitle(r"LaNMM alpha resonance, $P_1$ driven (carrier $f_c=100$ Hz)", fontsize=11)
    fig.tight_layout(rect=[0, 0, 1, 0.96])
    fig.savefig(os.path.join(FIGDIR, "fig_lanmm_resonance.png"), dpi=150)
    fig.savefig(os.path.join(FIGDIR, "fig_lanmm_resonance.pdf")); plt.close(fig)
    print("wrote fig_lanmm_resonance + fig_lanmm_map (peak near alpha ~10 Hz)")


if __name__ == "__main__":
    make_figures()
