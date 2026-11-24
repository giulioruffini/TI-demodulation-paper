"""Landau finding 5 (2026-10-05): the S10 endpoint stability check of nmm2_jcD_endpoint_check.py
repeated with genuine two tones (amplitude A each at fc -/+ Df/2, matched beat source to the
A(1+cos)cos surrogate; DC source 4/3 larger), at the last couplings, with 5 s settling.
Writes ../docs/landau5_s10_endpoint_twotone_<i>.json."""
import os, sys, json, numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import nmm2_jcA as J
import nmm2_jcD_endpoint_check as K
_rhs = J.rhs
def rhs_twotone(y, t, eta, C, Amp, wO, wc):
    # surrogate rhs evaluated with zero field, plus the two-tone field in the v_E equation
    d = _rhs(y, t, eta, C, 0.0 * np.asarray(Amp), wO, wc)
    F = Amp * (np.cos((wc - wO / 2) * t) + np.cos((wc + wO / 2) * t))
    d[1] = d[1] + F / J.TAU_E
    return d
J.rhs = rhs_twotone
i = int(sys.argv[1])
cache = np.load(os.path.join(HERE, "nmm2_jcD.npz"))
C, fpk = float(cache["C"][i]), float(cache["fpk"][i])
r = K.diagnose(C, fpk, t_set=5000.0, t_meas=1200.0, t_long=8000.0)
r["waveform"] = "two tones, amplitude 8 each, fc 300 Hz"; r["index"] = i
print(json.dumps({k: (round(v, 6) if isinstance(v, float) else v) for k, v in r.items()}))
json.dump(r, open(os.path.join(HERE, "..", "docs", f"landau5_s10_endpoint_twotone_{i}.json"), "w"), indent=1)
