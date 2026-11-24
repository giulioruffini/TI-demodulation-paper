"""Analytic kHz feasibility for TN0484 (referee item 1). Klaus, 2026-10-24.

Exact two-tone access through a first-order point membrane, the Jansen-Rit
(JR) quadratic source at the pinned operating point, and the equivalent
direct (tDCS/tACS) polarization, against carrier frequency, access time,
assumed coupling, and local field per tone. No simulation, no network gain.

Run:  .venv/bin/python notes/2026-10-24_klaus/feasibility_khz.py
Writes feasibility_khz.{pdf,png}, feasibility_khz_curves.csv, feasibility_khz_anchors.json
next to this file.

Formulas (manuscript Eqs. coupling, taylor, demod, khz, direct-comparison):
  tones            f_1,2 = f_c -/+ df/2, df = 10 Hz (alpha beat; the access factor is
                   insensitive to df at these carriers)
  access           H(w) = 1/(1 + i w tau);  |H|^2 = 1/(1 + w^2 tau^2)
  polarization     eps_j = lambda_0 * E * |H(w_j)|      [mV]; E per tone in V/m,
                   lambda_0 in mV per V/m, same E for both tones
  two-tone factor  P = |H(w_1)| |H(w_2)|  (equals |H(w_c)|^2 to 1e-4 here)
  JR sigmoid       Sig(v) = 2 e0 / (1 + exp(rho (v0 - v))), rho = 0.56 /mV, v0 = 6 mV,
                   e0 = 2.5 /s; pinned v* = 8.30 mV -> Sig' = 0.4745 /s/mV,
                   Sig'' = -0.1508 /s/mV^2
  beat source      Y_Omega = (1/2) Sig'' eps_1 eps_2                 [1/s]
  steady source    Y_DC    = (1/4) Sig'' (eps_1^2 + eps_2^2)         [1/s]
  equivalent       eps_eq  = Sig''/(2 Sig') eps_1 eps_2 = -0.1589 eps_1 eps_2 [mV]
  direct input     (the tDCS or tACS polarization at the same entry point that
                   gives the same leading source; Sec. 2.6)
  cable (optional) sealed long passive cable in a uniform axial field: each tone
                   acquires (1 + w^2 tau^2)^(-1/4), so P_cable = (1 + w_c^2 tau^2)^(-1/2)
Illustrative assumptions: first-order point-membrane access; uniform lambda_0
(0.5 cortical L5/6, Radman 2009; 0.15 hippocampal, Bikson 2004 / Deans 2007);
static JR detector at the pinned operating point; open-loop sources before
synaptic and recurrent gain; both tones with the same local field. The access
factor belongs to the static JR chain only: the exact mean field and the QIF
network compute access inside tau_E and must not be multiplied by it again.
Weak-input validity |eps| << 1/rho = 1.8 mV holds over the whole grid
(eps <= 0.5 mV at E = 1 V/m, lambda_0 = 0.5).
"""
import csv, json, os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
RHO, V0, E0, VSTAR = 0.56, 6.0, 2.5, 8.30
DF = 10.0                                  # Hz
TAUS_MS = [0.05, 0.2, 1.0, 15.0]
LAMBDAS = [0.15, 0.5]                      # mV per V/m
EFIELDS = [0.1, 0.3, 1.0]                  # V/m per tone
FC = np.logspace(np.log10(300.0), 4, 400)  # 0.3-10 kHz
EGRID = np.logspace(-1, 0, 200)            # 0.1-1 V/m
MARK = {"1.3 kHz": 1300.0, "2 kHz": 2000.0, "9 kHz": 9000.0}


def sig_derivs(v):
    x = RHO * (v - V0); s = 1.0 / (1.0 + np.exp(-x))
    return 2 * E0 * RHO * s * (1 - s), 2 * E0 * RHO ** 2 * s * (1 - s) * (1 - 2 * s)


SIG1, SIG2 = sig_derivs(VSTAR)
KEQ = abs(SIG2) / (2 * SIG1)              # mV^-1: |eps_eq| = KEQ eps_1 eps_2


def Habs(f_hz, tau_s):
    return 1.0 / np.sqrt(1.0 + (2 * np.pi * f_hz * tau_s) ** 2)


def two_tone(fc, tau_s):
    return Habs(fc - DF / 2, tau_s), Habs(fc + DF / 2, tau_s)


def cable(fc, tau_s):
    return (1.0 + (2 * np.pi * fc * tau_s) ** 2) ** -0.5


# ---------------- curves and anchors ----------------
rows = []
anch = dict(sigma1=SIG1, sigma2=SIG2, keq_per_mV=KEQ, df_Hz=DF, ratios={}, budget={}, points={})
for tau_ms in TAUS_MS:
    tau = tau_ms * 1e-3
    h1, h2 = two_tone(FC, tau); P = h1 * h2
    for lam in LAMBDAS:
        for E in EFIELDS:
            e1, e2 = lam * E * h1, lam * E * h2
            for k in range(len(FC)):
                rows.append([tau_ms, lam, E, FC[k], P[k], e1[k], e2[k],
                             0.5 * SIG2 * e1[k] * e2[k], 0.25 * SIG2 * (e1[k] ** 2 + e2[k] ** 2),
                             -KEQ * e1[k] * e2[k]])
    # ratios between carriers, exact pairs
    def pair(f): a, b = two_tone(f, tau); return a * b
    anch["ratios"][f"tau_{tau_ms:g}ms"] = dict(
        P_9k_over_1k=float(pair(9000) / pair(1000)), P_9k_over_1p3k=float(pair(9000) / pair(1300)),
        P_2k_over_1k=float(pair(2000) / pair(1000)), P_at_1p3k=float(pair(1300)), P_at_2k=float(pair(2000)),
        P_at_9k=float(pair(9000)), field_factor_9k_vs_1p3k=float(np.sqrt(pair(1300) / pair(9000))),
        cable_P_9k_over_1p3k=float(cable(9000, tau) / cable(1300, tau)))
# Section 5.4 budget: E = 0.5 V/m per tone, lambda_0 = 0.5, 2 kHz, 0.2 ms
h1, h2 = two_tone(2000.0, 0.2e-3); e1, e2 = 0.25 * h1, 0.25 * h2
anch["budget"] = dict(E_per_tone=0.5, lambda0=0.5, fc=2000, tau_ms=0.2, eps1_mV=float(e1), eps2_mV=float(e2),
                      eps_eq_uV=float(1e3 * KEQ * e1 * e2), Y_Omega_per_s=float(0.5 * SIG2 * e1 * e2),
                      Y_DC_per_s=float(0.25 * SIG2 * (e1 ** 2 + e2 ** 2)))
for name, f in MARK.items():
    for tau_ms in TAUS_MS:
        h1, h2 = two_tone(f, tau_ms * 1e-3)
        for lam in LAMBDAS:
            for E in EFIELDS:
                anch["points"][f"{name}|tau{tau_ms:g}|lam{lam:g}|E{E:g}"] = float(1e3 * KEQ * (lam * E) ** 2 * h1 * h2)

with open(os.path.join(HERE, "feasibility_khz_curves.csv"), "w", newline="") as fh:
    w = csv.writer(fh)
    w.writerow(["tau_ms", "lambda0_mV_per_Vm", "E_per_tone_Vm", "fc_Hz", "two_tone_access_P",
                "eps1_mV", "eps2_mV", "Y_Omega_per_s", "Y_DC_per_s", "eps_eq_mV"])
    w.writerows(rows)
json.dump(anch, open(os.path.join(HERE, "feasibility_khz_anchors.json"), "w"), indent=1)

# ---------------- figure ----------------
plt.rcParams.update({"font.size": 9, "axes.labelsize": 9.5, "legend.fontsize": 8, "axes.titlesize": 9.5})
colors = {0.05: "#1b9e77", 0.2: "#d95f02", 1.0: "#7570b3", 15.0: "#444444"}
fig, ax = plt.subplots(1, 3, figsize=(12.0, 3.7))
LETTER = dict(fontsize=11, fontweight="bold", va="bottom", ha="right")
from matplotlib.ticker import FixedLocator, NullLocator, FormatStrFormatter

# (a) two-tone access factor
a = ax[0]
for tau_ms in TAUS_MS:
    h1, h2 = two_tone(FC, tau_ms * 1e-3)
    a.loglog(FC / 1e3, h1 * h2, color=colors[tau_ms], lw=1.6, label=rf"$\tau$ = {tau_ms:g} ms")
a.loglog(FC / 1e3, cable(FC, 0.2e-3), color=colors[0.2], lw=1.2, ls=":", label="sealed cable, 0.2 ms")
for name, f in MARK.items():
    a.axvline(f / 1e3, color="0.8", lw=0.8, zorder=0)
    a.text(f / 1e3, 2.2, name, ha="right" if name == "1.3 kHz" else "left", va="bottom", fontsize=7.5, color="0.4")
a.set_ylim(1e-6, 2); a.set_xlim(0.3, 10)
a.set_xlabel("carrier $f_c$ (kHz)"); a.set_ylabel(r"two-tone access factor $|H(\omega_1)||H(\omega_2)|$")
a.legend(loc="lower left", frameon=False)
a.text(-0.16, 1.03, "a", transform=a.transAxes, **LETTER)

# (b) equivalent direct polarization vs carrier, E = 0.3 V/m per tone, lambda0 = 0.5; right axis lambda0 = 0.15
b = ax[1]
E_REF, LAM_REF, LAM_ALT = 0.3, 0.5, 0.15
for tau_ms in TAUS_MS:
    h1, h2 = two_tone(FC, tau_ms * 1e-3)
    b.loglog(FC / 1e3, 1e3 * KEQ * (LAM_REF * E_REF) ** 2 * h1 * h2, color=colors[tau_ms], lw=1.6)
for name, f in MARK.items():
    b.axvline(f / 1e3, color="0.8", lw=0.8, zorder=0)
b.set_xlim(0.3, 10); b.set_ylim(1e-5, 10)
b.set_xlabel("carrier $f_c$ (kHz)")
b.set_ylabel(r"$|\varepsilon_{\rm eq}|$ ($\mu$V), $\lambda_0$ = 0.5 mV per V/m")
b.set_title(f"E = {E_REF:g} V/m per tone", loc="right", fontsize=8.5, color="0.3")
b2 = b.twinx(); b2.set_yscale("log"); lo, hi = b.get_ylim(); s = (LAM_ALT / LAM_REF) ** 2
b2.set_ylim(lo * s, hi * s); b2.set_ylabel(r"$|\varepsilon_{\rm eq}|$ ($\mu$V), $\lambda_0$ = 0.15 mV per V/m")
b.text(-0.16, 1.03, "b", transform=b.transAxes, **LETTER)
b.text(0.97, 0.93, r"$\varepsilon_{\rm eq}\propto\lambda_0^2E^2$", transform=b.transAxes, ha="right", va="top", fontsize=8, color="0.3")

# (c) equivalent direct polarization vs local field per tone at the marked carriers, tau = 0.2 ms
c = ax[2]
TAU_C = 0.2e-3
styles = {"1.3 kHz": "-", "2 kHz": "--", "9 kHz": "-."}
for name, f in MARK.items():
    h1, h2 = two_tone(f, TAU_C)
    c.loglog(EGRID, 1e3 * KEQ * (LAM_REF * EGRID) ** 2 * h1 * h2, color="#d95f02", ls=styles[name], lw=1.6,
             label=rf"{name}, $\lambda_0$ = 0.5")
    c.loglog(EGRID, 1e3 * KEQ * (LAM_ALT * EGRID) ** 2 * h1 * h2, color="#1f78b4", ls=styles[name], lw=1.2,
             label=rf"{name}, $\lambda_0$ = 0.15")
bud = anch["budget"]
c.plot([bud["E_per_tone"]], [bud["eps_eq_uV"]], "k*", ms=8, zorder=5)
c.annotate("Sec. 5.4 budget", (bud["E_per_tone"], bud["eps_eq_uV"]), xytext=(-62, 8), textcoords="offset points",
           fontsize=7.5, color="0.2")
c.set_xlim(0.1, 1.0); c.set_ylim(1e-3, 30)
c.set_xlabel("local field per tone $E$ (V/m)"); c.set_ylabel(r"$|\varepsilon_{\rm eq}|$ ($\mu$V), $\tau$ = 0.2 ms")
c.legend(loc="upper left", frameon=False, ncol=2, fontsize=7, bbox_to_anchor=(0.0, 0.99))
c.text(-0.16, 1.03, "c", transform=c.transAxes, **LETTER)
c.xaxis.set_major_locator(FixedLocator([0.1, 0.2, 0.3, 0.5, 1.0])); c.xaxis.set_minor_locator(NullLocator())
c.xaxis.set_major_formatter(FormatStrFormatter("%g"))
for axis in ax:
    axis.grid(True, which="major", color="0.92", lw=0.6)
fig.tight_layout(w_pad=1.6)
fig.savefig(os.path.join(HERE, "feasibility_khz.pdf"), metadata={"CreationDate": None})
fig.savefig(os.path.join(HERE, "feasibility_khz.png"), dpi=300)
print(json.dumps(dict(sigma1=SIG1, sigma2=SIG2, keq=KEQ, budget=anch["budget"],
                      ratios_0p2ms=anch["ratios"]["tau_0.2ms"], ratios_0p05ms=anch["ratios"]["tau_0.05ms"]), indent=1))
