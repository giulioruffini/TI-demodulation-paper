"""Read-only JR matrix check for the v0.14.6 submission-readiness review.

Run from the repository root with:
    .venv/bin/python -B docs/review_v0146_jr_matrix.py

Uses an analytic Jacobian and existing cache; no ODE integration or project writes.
The input is a generated rate entering the pyramidal synapse. The output is y1-y2.
"""

import sys
from pathlib import Path

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "code"))

import numpy as np
from scipy.optimize import minimize_scalar

import jr_jsweep_engine as E


def jac_at_v(v, coupling):
    """JR Jacobian in state order (y0, y1, y2, y3, y4, y5)."""
    y0 = (E.A / E.a) * E.Sigm(v)

    def sigmoid_slope(x):
        z = np.exp(E.rr * (E.v0 - x))
        return 2 * E.e0 * E.rr * z / (1 + z) ** 2

    jac = np.zeros((6, 6))
    jac[:3, 3:] = np.eye(3)
    jac[3, 0] = -E.a**2
    jac[3, 1] = E.A * E.a * sigmoid_slope(v)
    jac[3, 2] = -jac[3, 1]
    jac[3, 3] = -2 * E.a
    jac[4, 0] = E.A * E.a * 0.8 * coupling**2 * sigmoid_slope(coupling * y0)
    jac[4, 1] = -E.a**2
    jac[4, 4] = -2 * E.a
    jac[5, 0] = E.B * E.b * 0.0625 * coupling**2 * sigmoid_slope(0.25 * coupling * y0)
    jac[5, 2] = -E.b**2
    jac[5, 5] = -2 * E.b
    return jac


b = np.array([0, 0, 0, E.A * E.a, 0, 0])
c = np.array([0, 1, -1, 0, 0, 0])

print("Analytic JR Jacobian; generated-rate input b; LFP readout c; no integration")
for coupling in (110.0, 120.0, 130.0):
    jac = jac_at_v(8.30, coupling)
    eigenvalues, vectors = np.linalg.eig(jac)
    k = np.argmax(eigenvalues.real)
    if eigenvalues[k].imag < 0:
        k = np.argmin(abs(eigenvalues - eigenvalues[k].conjugate()))
    eigenvalue = eigenvalues[k]
    residue = (c @ vectors[:, k]) * (np.linalg.inv(vectors)[k, :] @ b)
    print(
        f"pinned C={coupling:.1f}: gamma={-eigenvalue.real:.6f}, "
        f"f0={eigenvalue.imag / (2 * np.pi):.6f}, "
        f"residue_abs={abs(residue):.6f}, residue_phase={np.angle(residue):.6f}"
    )

for drive in (330.0, 355.0, 395.0):
    jac = jac_at_v(E._fp_v(drive, 135.0), 135.0)
    eigenvalues = np.linalg.eigvals(jac)
    eigenvalue = eigenvalues[np.argmax(eigenvalues.real)]
    gamma, nu = -eigenvalue.real, abs(eigenvalue.imag)

    def gain(omega):
        return abs(c @ np.linalg.solve(1j * omega * np.eye(6) - jac, b))

    peak = minimize_scalar(
        lambda omega: -gain(omega),
        bounds=(2 * np.pi * 9, 2 * np.pi * 13),
        method="bounded",
    )
    caption_peak = np.sqrt(nu**2 - 2 * gamma**2) / (2 * np.pi)
    constant_numerator_peak = np.sqrt(nu**2 - gamma**2) / (2 * np.pi)
    print(
        f"p={drive:.0f}: gamma={gamma:.6f}, eigen_f={nu / (2 * np.pi):.6f}, "
        f"true_linear_peak={peak.x / (2 * np.pi):.6f}, "
        f"caption_peak={caption_peak:.6f}, "
        f"constant_numerator_peak={constant_numerator_peak:.6f}"
    )

with np.load(ROOT / "code" / "sweep_hi_stable.npz") as cache:
    for drive, response in zip(cache["p"], cache["rs"]):
        print(
            f"cached nonlinear p={drive:.0f}, "
            f"peak_grid_Hz={cache['f_om'][response.argmax()]:.6f}, "
            f"peak_mV={response.max():.6f}"
        )
