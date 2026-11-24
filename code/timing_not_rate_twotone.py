"""Landau finding 5 (2026-10-05): the timing-versus-rate sweep of timing_not_rate.py rerun with
genuine two tones instead of the m=1 AM surrogate. Matched beat: two tones of amplitude eps at
fc -/+ Df/2 give the same Omega source (eps^2) as the surrogate eps(1+cos Omega t)cos(w_c t), and a
DC source eps^2 instead of 3 eps^2/4. Everything else (pinned v*, C grid, settling, window, lock-in)
is unchanged. Writes timing_not_rate_twotone.npz."""
import numpy as np, os, sys
import timing_not_rate as T

def field_twotone(t, eps, m, Om, fc):
    wc = 2 * np.pi * fc
    return eps * (np.cos((wc - Om / 2) * t) + np.cos((wc + Om / 2) * t))

if __name__ == "__main__":
    T.field = field_twotone
    HERE = os.path.dirname(os.path.abspath(__file__))
    ref = np.load(os.path.join(HERE, "timing_not_rate.npz"))
    Cs, ps, gam, om = ref["Cs"], ref["ps"], ref["gam"], ref["om"]
    eps, fc = float(ref["eps"]), float(ref["fc"]); vstar = float(ref["vstar"])
    dt, t_set, t_meas = 2e-4, 18.0, 20.0
    AC_v, AC, rate_on = T.run(ps, Cs, om.copy(), eps, 1.0, fc, t_set, t_meas, dt)
    DC = rate_on - T.Sigm(vstar)
    print("  C      gamma   AC_r two-tone  AC_r AM     DC two-tone   DC AM      ratio2T  ratioAM")
    for i in range(len(Cs)):
        print(f"{Cs[i]:7.2f}{gam[i]:8.3f}{AC[i]:13.4e}{ref['AC'][i]:12.4e}{DC[i]:13.3e}{ref['DC'][i]:12.3e}"
              f"{abs(AC[i]/DC[i]):9.1f}{abs(ref['AC'][i]/ref['DC'][i]):9.1f}")
    np.savez(os.path.join(HERE, "timing_not_rate_twotone.npz"), Cs=Cs, ps=ps, gam=gam, om=om,
             AC=AC, AC_v=AC_v, DC=DC, rate_on=rate_on, rate_off=T.Sigm(vstar), vstar=vstar, eps=eps, fc=fc)
    print("saved timing_not_rate_twotone.npz")
