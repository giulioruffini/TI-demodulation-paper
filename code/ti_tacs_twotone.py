"""Landau finding 5 (2026-10-05): TI/tACS response ratios of the pinned JR sweep with genuine two
tones instead of the m=1 AM surrogate, at matched beat source (two tones of amplitude eps at
fc -/+ Df/2; DC source eps^2 instead of 3 eps^2/4). (i) ratio sweep at the cached tACS couplings
(12 s settling, 6 s window, as published); (ii) the three source-matched controls of
ti_tacs_pinned_diagnostic.py (60 s settling, 20 s window). Writes
../docs/landau5_ti_tacs_twotone_2026-10-05.json."""
import os, sys, json, numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import jr_jsweep_engine as E
VSTAR, EPS, FC = 8.30, 0.3, 100.0
am = E.field
def twotone(t, eps, m, Om, fc):
    wc = 2 * np.pi * fc
    return eps * (np.cos((wc - Om / 2) * t) + np.cos((wc + Om / 2) * t))
tab = json.load(open(os.path.join(HERE, "..", "docs", "r7_tacs_jsweep_table_2026-10-05.json")))["arrays"]
Cs, gam, w0, Atacs = (np.array(tab[k]) for k in ("Cs", "gam", "w0", "A"))
ps = np.array([E.p_of_C(VSTAR, C) for C in Cs])
out = {"C": Cs.tolist(), "gamma": gam.tolist(), "tACS_0p1": Atacs.tolist()}
for name, f in (("AM", am), ("twotone", twotone)):
    E.field = f
    A = E.closed_lockin(ps, Cs, w0.copy(), EPS, 1.0, FC, 12.0, 6.0, 2e-4)
    out["TI_" + name] = A.tolist(); out["ratio_" + name] = (A / Atacs).tolist()
print("  C      gamma   TI/tACS AM   TI/tACS two-tone")
for i in range(len(Cs)):
    print(f"{Cs[i]:7.2f}{gam[i]:8.3f}{out['ratio_AM'][i]:11.3f}{out['ratio_twotone'][i]:13.3f}")
# (ii) source-matched controls, long settling
def Sig1(v):
    s = 1 / (1 + np.exp(E.rr * (E.v0 - v))); return 2 * E.e0 * E.rr * s * (1 - s)
eps_t = 0.5 * abs(E.Sigm2(VSTAR)) * EPS ** 2 / Sig1(VSTAR)
Csel = np.array([110.0, 133.9090909, 136.3]); psel = np.array([E.p_of_C(VSTAR, C) for C in Csel])
osel = np.array([E.jac_eig(p, C)[2] for p, C in zip(psel, Csel)])
E.field = twotone
Ati = E.closed_lockin(psel, Csel, osel.copy(), EPS, 1.0, FC, 60.0, 20.0, 2e-4)
E.field = lambda t, eps, m, Om, fc: eps * np.cos(Om * t)          # direct tACS at the beat
Ata = E.closed_lockin(psel, Csel, osel.copy(), eps_t, 0.0, FC, 60.0, 20.0, 2e-4)
Ata7 = E.closed_lockin(psel, Csel, osel.copy(), 0.1, 0.0, FC, 60.0, 20.0, 2e-4)
out["matched"] = {"C": Csel.tolist(), "eps_tACS_matched": eps_t, "TI_twotone": Ati.tolist(),
                  "tACS_matched": Ata.tolist(), "tACS_0p1": Ata7.tolist(),
                  "TI_over_matched": (Ati / Ata).tolist(), "gain_0p1_over_matched": (Ata7 / Ata).tolist(),
                  "input_factor": 0.1 / eps_t}
print("matched controls (two tones):", np.round(Ati / Ata, 3), " 6.99x input gives", np.round(Ata7 / Ata, 2))
json.dump(out, open(os.path.join(HERE, "..", "docs", "landau5_ti_tacs_twotone_2026-10-05.json"), "w"), indent=1)
