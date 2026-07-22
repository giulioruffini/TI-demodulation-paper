"""
How efficient can a sigmoid detector be? Scan the whole family.

The perturbative bound eta <= rho*eps/4 holds only at fixed slope. Since rho is a
model parameter, the fair question is what the sigmoid family can achieve when the
exact cycle response is evaluated rather than its quadratic truncation. Reproduces
the numbers quoted in the Discussion.

  eta = [Omega-component of sigma(v* + s_TI)] / [Omega-component of sigma(v* + s_tACS)]

with s_TI two genuine tones of amplitude eps each and s_tACS a single tone of
amplitude 2*eps, i.e. matched peak polarization.
"""
import numpy as np
from scipy.special import expit

E0, V0 = 2.5, 6.0
FC, DF = 2000.0, 10.0


def sigmoid(v, rho):
    return 2 * E0 * expit(rho * (v - V0))          # numerically stable at large rho


def omega_amp(x, t, w, W, om):
    xb = x - np.sum(w * x) / W
    return np.hypot(2 * np.sum(w * xb * np.cos(om * t)) / W,
                    2 * np.sum(w * xb * np.sin(om * t)) / W)


def eta(rho, eps, dt=5e-7, T=1.0, nv=61):
    t = np.arange(0, T, dt)
    w = np.hanning(len(t)); W = w.sum(); om = 2 * np.pi * DF
    ti = eps * (np.cos(2 * np.pi * (FC - DF / 2) * t) + np.cos(2 * np.pi * (FC + DF / 2) * t))
    tac = 2 * eps * np.cos(om * t)
    best = 0.0
    for v in np.linspace(V0 - 6 / rho, V0 + 6 / rho, nv):
        den = omega_amp(sigmoid(v + tac, rho), t, w, W, om)
        if den > 1e-12:
            best = max(best, omega_amp(sigmoid(v + ti, rho), t, w, W, om) / den)
    return best


if __name__ == "__main__":
    eps = 0.1                                       # Vieira-scale polarization, mV
    print(f"eps = {eps} mV;  max over v* of the TI/tACS ratio at Omega")
    print(f"{'rho (1/mV)':>11}{'width (uV)':>12}{'eta':>9}{'perturb rho*eps/4':>19}")
    for rho in [0.56, 2, 5, 10, 20, 40, 80, 160, 320]:
        print(f"{rho:>11.2f}{1000/rho:>12.1f}{eta(rho, eps):>9.4f}{rho*eps/4:>19.4f}")
    print(f"\n  half-wave rectifier constant 1/pi = {1/np.pi:.4f}")
    print("  family maximum ~0.32 near rho ~ 40-80 /mV, i.e. a 12-25 uV transfer width")
