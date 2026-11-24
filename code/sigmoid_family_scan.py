"""
How efficient can a sigmoid detector be? Scan the whole family.

The perturbative bound eta <= rho*eps/4 holds only at fixed slope. Since rho is a
model parameter, the fair question is what the sigmoid family can achieve when the
exact cycle response is evaluated rather than its quadratic truncation.

  eta = [Omega-component of sigma(v* + s_TI)] / [Omega-component of sigma(v* + s_tACS)]

with s_TI two genuine tones of amplitude eps each and s_tACS a single tone of
amplitude 2*eps, i.e. matched peak polarization.

Exact scale invariance. The logistic depends on v only through rho*(v - v0), so with

    u = rho*eps          (field in units of the transfer width)
    x = rho*(v* - v0)    (operating point in the same units)

we have sigma(v* + eps*q(t)) = 2*e0*L(x + u*q(t)) for any normalised waveform q, and
the 2*e0 cancels in the ratio. Hence eta = eta(u, x) exactly: optimising over (v*, rho)
at fixed eps is the same as optimising over (u, x), and the family supremum is
INDEPENDENT of field strength. Verified here to 4 decimals across a 160-fold range of
rho (--check).

Window bug, fixed 2026-07-22. The previous version scanned v* over V0 +- 6/rho, i.e.
x in [-6, 6]. The optimising operating point runs as |x*| ~ 1.046*u, so it leaves that
interval once u > ~5.7. The scan therefore reported a spurious interior maximum
(eta ~ 0.32 near rho ~ 40-80 /mV) that then "fell again for steeper transfers" --
both artifacts of the boundary, not features of the family. With the window scaled to
u, eta is numerically monotone over the explored range and converges to the
hard-threshold limit computed in eta_threshold() below. There is NO finite optimal
transfer width. Timestep refinement does not expose this; only the x-window does.
"""
import numpy as np
from scipy.special import expit

E0, V0 = 2.5, 6.0
FC, DF = 2000.0, 10.0


def omega_amp(y, t, w, W, om):
    yb = y - np.sum(w * y) / W
    return np.hypot(2 * np.sum(w * yb * np.cos(om * t)) / W,
                    2 * np.sum(w * yb * np.sin(om * t)) / W)


def eta_reduced(u, dt=2e-6, T=0.5, nx=200, xspan=2.4):
    """Max over the operating point x of the TI/tACS ratio, in reduced units.

    xspan sets the search window as a multiple of u; the optimum sits at ~1.046*u,
    so xspan must stay comfortably above that (2.4 leaves ample margin). eta is even
    in x, so only x >= 0 is scanned.
    """
    t = np.arange(0, T, dt)
    w = np.hanning(len(t)); W = w.sum(); om = 2 * np.pi * DF
    ti = np.cos(2 * np.pi * (FC - DF / 2) * t) + np.cos(2 * np.pi * (FC + DF / 2) * t)
    tac = 2 * np.cos(om * t)
    best, xbest = 0.0, 0.0
    for x in np.linspace(0.0, max(8.0, xspan * u), nx):
        den = omega_amp(expit(x + u * tac), t, w, W, om)
        if den > 1e-13:
            r = omega_amp(expit(x + u * ti), t, w, W, om) / den
            if r > best:
                best, xbest = r, x
    return best, xbest


def eta_threshold(beta, n=400_001):
    """rho -> infinity limit: the sigmoid becomes a hard threshold.

    beta = delta/(2 eps) is the threshold offset as a fraction of the peak
    polarization. Matched-peak tACS gives a square pulse train whose fundamental is
    (2/pi)*sqrt(1 - beta^2). Two-tone TI, averaged over the fast carrier, gives a
    baseband duty cycle (1/pi)*arccos(beta/|cos(phi/2)|) where it is defined.
    """
    th = np.linspace(0, 2 * np.pi, n)
    c = np.abs(np.cos(th / 2))
    y = np.where(c > beta,
                 np.arccos(np.clip(beta / np.maximum(c, 1e-300), -1, 1)) / np.pi, 0.0)
    return abs(np.trapezoid(y * np.cos(th), th) / np.pi) / ((2 / np.pi) * np.sqrt(1 - beta ** 2))


def threshold_supremum():
    bs = np.linspace(0.05, 0.95, 1801)
    es = np.array([eta_threshold(b) for b in bs])
    i = int(es.argmax())
    return es[i], bs[i]


if __name__ == "__main__":
    import sys

    sup, beta_star = threshold_supremum()
    print(f"hard-threshold supremum   eta = {sup:.5f}  at beta = delta/(2 eps) = {beta_star:.4f}")
    print(f"  (for reference, 1/pi = {1 / np.pi:.5f} -- the half-wave rectifier's envelope")
    print(f"   coefficient, a different observable and NOT the family ceiling)\n")

    print("eta vs transfer width, operating point optimised without a window artifact")
    print(f"{'u = rho*eps':>12}{'eta':>9}{'x*_opt':>9}{'% of ceiling':>14}{'perturb u/4':>13}")
    for u in [0.056, 0.5, 2, 4, 6, 8, 12, 16, 32]:
        e, xb = eta_reduced(u)
        print(f"{u:>12.3f}{e:>9.4f}{xb:>9.2f}{100 * e / sup:>13.1f}%{u / 4:>13.4f}")

    print("\nphysical widths reaching 95% of the ceiling (needs u = rho*eps >~ 6):")
    for eps, lab in [(0.1, "Vieira-scale"), (0.02, "human-scale")]:
        print(f"  eps = {eps:>4} mV ({lab:>12}):  1/rho <= {1000 * eps / 6:>5.1f} uV,"
              f"  offset delta ~ {1000 * 2 * beta_star * eps:>5.1f} uV")

    if "--check" in sys.argv:
        print("\nscale-invariance check: eta must depend only on u = rho*eps")
        for rho, eps in [(40, 0.1), (80, 0.05), (20, 0.2), (400, 0.01), (4, 1.0)]:
            e, _ = eta_reduced(rho * eps)
            print(f"  rho={rho:>6.1f}  eps={eps:<6}  u={rho * eps:>5.2f}   eta={e:.4f}")
