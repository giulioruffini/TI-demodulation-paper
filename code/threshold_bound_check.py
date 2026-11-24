"""Step-detector optimum of the memoryless TI/tACS efficiency (App. bound).

For a unit step transfer at threshold offset delta, balanced tones at matched peak
post-coupling polarization eps, and beta = delta/(2 eps): the tACS fundamental coefficient is
b(beta) = (2/pi) sqrt(1 - beta^2) and the carrier-averaged TI coefficient is
a(beta) = (2/pi^2) int_0^{2 arccos(beta)} arccos(beta / cos(phi/2)) cos(phi) dphi,
which reduces by parts to a/b = 2 beta / (pi sqrt(1 - beta^2)) [K(m) - E(m)], m = 1 - beta^2
(Kaiti, review brief N3, 2026-09-22). This script maximizes a/b over beta by direct
quadrature and by the elliptic form, and computes the step's second-to-first harmonic
magnitude ratio at the optimum. Prints the three numbers quoted in the appendix."""
import numpy as np
from scipy.integrate import quad
from scipy.optimize import minimize_scalar
from scipy.special import ellipk, ellipe

def b(beta): return 2 / np.pi * np.sqrt(1 - beta ** 2)
def a_quad(beta):
    f = lambda phi: np.arccos(beta / np.cos(phi / 2)) * np.cos(phi)
    return 2 / np.pi ** 2 * quad(f, 0, 2 * np.arccos(beta), limit=200)[0]
def a2_quad(beta):
    f = lambda phi: np.arccos(beta / np.cos(phi / 2)) * np.cos(2 * phi)
    return 2 / np.pi ** 2 * quad(f, 0, 2 * np.arccos(beta), limit=200)[0]
def ratio_elliptic(beta):
    m = 1 - beta ** 2
    return 2 * beta / (np.pi * np.sqrt(1 - beta ** 2)) * (ellipk(m) - ellipe(m))

res = minimize_scalar(lambda x: -a_quad(x) / b(x), bounds=(0.05, 0.95), method="bounded", options=dict(xatol=1e-10))
beta = res.x
print(f"beta* = delta/(2 eps) = {beta:.6f}")
print(f"TI/tACS ratio at the optimum: quadrature {a_quad(beta)/b(beta):.6f}, elliptic form {ratio_elliptic(beta):.6f}")
print(f"step second-to-first harmonic magnitude ratio at the optimum: {abs(a2_quad(beta))/abs(a_quad(beta)):.5f}  (linear envelope follower: 0.2)")
