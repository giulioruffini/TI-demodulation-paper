"""
What happens at kHz carriers? The quasi-static demo couples the field directly
into the sigmoid (no membrane filter): then A_Omega is carrier-independent up to
10 kHz. Reality adds a membrane low-pass H_m(w)=1/(1+i w tau_m) BEFORE the
nonlinearity, attenuating the carrier reaching the detector by 1/sqrt(1+(w_c tau_m)^2),
so A_Omega ~ eps_eff^2 ~ 1/f_c^2 at high carriers. This script quantifies it.
"""
import numpy as np
from scipy.signal import lfilter
import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
import figstyle; figstyle.apply()
from jr_demod import Sigm, steady_v
import os
FIGS = os.environ.get("TN_FIGDIR") or os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "figures")
os.makedirs(FIGS, exist_ok=True)

NEB="#0a4f8c"; NEB2="#2f7ec4"; NER="#b3361f"; GR="#555555"
F0=11.1; m=1.0; eps=0.5
vstar=float(steady_v(np.array([345.0]))[0][0])      # JR operating point near Hopf
dt=5e-6; T=1.0; n=int(T/dt); t=np.arange(n)*dt; Om=2*np.pi*F0
skip=int(0.3/dt); tt=t[skip:]; w=np.hanning(len(tt))  # drop filter transient
fc=np.geomspace(25., 10000., 30)

def lockin(y):                                       # demeaned Hann lock-in at Omega
    y=y[:, skip:]; y=y-y.mean(1, keepdims=True)      # remove DC (else it leaks into Omega bin)
    c=(y*(w*np.cos(Om*tt))).sum(1); s=(y*(w*np.sin(Om*tt))).sum(1)
    return 2.0/w.sum()*np.sqrt(c**2+s**2)

# AM field for every carrier (rows)
S = eps*(1+m*np.cos(Om*t))[None,:]*np.cos(2*np.pi*fc[:,None]*t)

curves={}
# tau values: direct (fast nonlinearity), axon/AIS/node (~0.2 ms), soma/dendrite (~16 ms)
taus=[0.0, 0.2e-3, 16e-3]
for tau in taus:
    if tau==0.0: Sf=S
    else:
        al=dt/(tau+dt); Sf=lfilter([al],[1,-(1-al)], S, axis=1)   # 1st-order membrane LP
    curves[tau]=lockin(Sigm(vstar+Sf))

A0=curves[0.0].copy()                                            # normalize: direct -> 1
fig, ax = plt.subplots(figsize=(8.0,4.8))
labels={0.0:"direct / fast nonlinearity ($\\tau\\!\\to\\!0$)",
        0.2e-3:"axon / AIS / node  $\\tau\\approx0.2$ ms (corner $\\approx$800 Hz)",
        16e-3:"soma / dendrite  $\\tau_m\\approx16$ ms (corner $\\approx$10 Hz)"}
cols={0.0:NEB, 0.2e-3:"#1a9850", 16e-3:NER}
for tau in taus:
    ax.loglog(fc, curves[tau]/A0, "o-", ms=3, color=cols[tau], label=labels[tau])
# 1/f^2 guide anchored to the soma curve at 1 kHz
i1k=np.argmin(np.abs(fc-1000)); base=(curves[16e-3]/A0)[i1k]
ax.loglog(fc[fc>=300], base*(fc[fc>=300]/1000.)**-2, "k--", lw=1, label="$\\propto 1/f_c^{2}$")
for f,lab in [(1000,"1k"),(2000,"2k"),(3900,"TMS\n3.9k"),(10000,"10k")]:
    ax.axvline(f, color=GR, ls=":", lw=0.7); ax.text(f*1.02, 1.3e-7, lab, fontsize=7.5, color=GR)
ax.set_ylim(1e-7, 2.0)
ax.set_xlabel("carrier frequency  $f_c$  (Hz)")
ax.set_ylabel("demodulated response @ $\\Omega$  (normalized to $\\tau\\!\\to\\!0$)")
ax.set_title("Where the nonlinearity sits decides kHz coupling (TI and TMS alike)", fontsize=10.5)
ax.legend(fontsize=8, frameon=False, loc="lower left"); ax.spines[["top","right"]].set_visible(False)
fig.tight_layout(); fig.savefig(f"{FIGS}/fig_khz.png",dpi=300); fig.savefig(f"{FIGS}/fig_khz.pdf")

# print the suppression numbers (carrier-power -> demod amplitude factor |H|^2)
def supp(tau,f): return 1.0/(1.0+(2*np.pi*f*tau)**2)
print(f"operating point v*={vstar:.2f} mV  (state-dependent: sets sigma'')")
for f in [1000,2000,3900,10000]:
    print(f"  f_c={f:5d} Hz : |H|^2  soma(16ms)={supp(16e-3,f):.2e}   AIS/node(0.2ms)={supp(0.2e-3,f):.2e}")
print("wrote fig_khz")
