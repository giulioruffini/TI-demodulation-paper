"""Check the note's transfer formula against a full linearized MPR system.

This is an algebraic check, not a neuron/network simulation. Run from the
repository root with a Python environment containing NumPy and PyMuPDF.
"""
from pathlib import Path
import hashlib
import json

import fitz
import numpy as np
from scipy.optimize import brentq


def check_transfer():
    tau, rate, delta, lam = 15.0, 0.02, 0.5, 0.7  # time in ms, rate in ms^-1
    voltage = -delta / (2 * np.pi * tau * rate)
    errors, residuals = [], []
    for syn_tau in (2.0, 10.0, 30.0):
        for coupling in (0.0, 0.5, 1.5):
            tonic = (np.pi * tau * rate) ** 2 - voltage**2 - tau * coupling * rate
            residuals.append(abs(voltage**2 + tonic - (np.pi * tau * rate) ** 2
                                 + tau * coupling * rate))
            # States (rate, voltage, synaptic rate, synaptic auxiliary state).
            jac = np.array([
                [2 * voltage / tau, 2 * rate / tau, 0, 0],
                [-2 * np.pi**2 * tau * rate, 2 * voltage / tau, coupling, 0],
                [0, 0, 0, 1 / syn_tau],
                [1 / syn_tau, 0, -1 / syn_tau, -2 / syn_tau],
            ])
            assert np.max(np.linalg.eigvals(jac).real) < 0
            forcing = np.array([0, lam / tau, 0, 0])
            for freq in (0.0, 1.0, 5.0, 10.0, 20.0, 80.0, 1000.0):
                omega = 2 * np.pi * freq / 1000
                matrix_response = np.linalg.solve(1j * omega * np.eye(4) - jac, forcing)
                z = 1j * omega * tau - 2 * voltage
                hs = (1 + 1j * omega * syn_tau) ** -2
                denominator = z**2 + 4 * (np.pi * tau * rate) ** 2 - 2 * tau * coupling * rate * hs
                formula = np.array([lam * 2 * rate / denominator, lam * z / denominator])
                errors.append(float(np.max(abs(matrix_response[:2] - formula) / abs(formula))))
    assert max(errors) < 1e-12
    assert max(residuals) < 1e-12
    return {"comparisons": len(errors), "max_relative_error": max(errors),
            "max_pinned_equilibrium_residual": max(residuals)}


def check_physical_units():
    # Consistent mV, nA, ms units: capacitance in nF; charge in nA ms = pC.
    cm, gl, us = 0.2, 0.01, 20.0
    k, current_scale, tau = gl / us, gl * us, cm / gl
    delta_i, eta_i, background_i, charge, kappa = 0.1, 0.03, -0.02, 6.0, 0.002
    delta, eta, background = delta_i / current_scale, eta_i / current_scale, background_i / current_scale
    coupling, lam = charge / (current_scale * tau), kappa / current_scale
    errors = []
    for u in (-10.0, -4.0, 3.0):
        for rate in (0.002, 0.02, 0.05):
            s, field = 0.013, 0.6
            dr_dim = k / cm * (delta_i / (np.pi * cm) + 2 * rate * u)
            du_dim = (k * u**2 - (np.pi * cm * rate)**2 / k
                      + eta_i + charge * s + background_i + kappa * field) / cm
            v = u / us
            dr_norm = (delta / (np.pi * tau) + 2 * rate * v) / tau
            dv_norm = (v**2 - (np.pi * tau * rate)**2 + eta
                       + tau * coupling * s + background + lam * field) / tau
            errors.extend([abs(dr_dim - dr_norm), abs(du_dim / us - dv_norm)])
    assert max(errors) < 1e-12
    return {"states": 9, "max_absolute_derivative_discrepancy": max(errors),
            "illustrative_current_scale_pA": current_scale * 1000,
            "illustrative_normalized_field_coefficient": lam}


def check_slow_limit():
    cm, gl, us, delta_i, kappa = 0.2, 0.01, 20.0, 0.1, 0.002
    k, scale, tau = gl / us, gl * us, cm / gl
    def physical_rate(q):
        return np.sqrt(k) / (np.pi * cm) * np.sqrt((q + np.hypot(q, delta_i)) / 2)
    gain_errors, coordinate_errors, stationarity = [], [], []
    for q in (-0.5, -0.1, 0.0, 0.1, 0.5):
        rate = physical_rate(q)
        slope = rate / (2 * np.hypot(q, delta_i))
        u = -delta_i / (2 * np.pi * cm * rate)
        stationarity.append(abs(k * u*u - (np.pi * cm * rate)**2 / k + q))
        for loop in (-2.0, 0.2, 0.9):
            charge = loop / slope
            background = q - charge * rate
            def steady(field):
                return brentq(lambda r: r - physical_rate(background + charge*r + kappa*field),
                              rate * 0.99, rate * 1.01, xtol=1e-15)
            h = 1e-4
            numerical = (steady(h) - steady(-h)) / (2*h)
            analytic = slope * kappa / (1-loop)
            gain_errors.append(abs(numerical/analytic - 1))
            reff = 100.0  # mV/nA, a chosen local coordinate conversion
            sigma_prime, lambda_x, return_x = slope/reff, reff*kappa, reff*charge
            coordinate_errors.append(abs((sigma_prime*lambda_x/(1-sigma_prime*return_x))/analytic - 1))
            # Match the manuscript's normalized rate curve and coupling convention.
            fprime = slope * tau * scale
            normalized_gain = (kappa/scale)*fprime/(tau*(1-(charge/(scale*tau))*fprime))
            coordinate_errors.append(abs(normalized_gain/analytic - 1))
    assert max(stationarity) < 1e-12
    assert max(gain_errors) < 1e-5
    assert max(coordinate_errors) < 1e-12
    return {"equilibrium_gain_cases":len(gain_errors),
            "max_relative_finite_difference_error":float(max(gain_errors)),
            "max_relative_coordinate_error":float(max(coordinate_errors)),
            "max_stationarity_current_residual":float(max(stationarity))}


if __name__ == "__main__":
    root = Path(__file__).resolve().parents[2]
    pdf = root / "output/pdf/TN0484_field_coupling_note.pdf"
    doc = fitz.open(pdf)
    text = "\n".join(page.get_text() for page in doc)
    log = (root / "build/field_coupling_note/field_coupling_note.log").read_text()
    warnings = [line for line in log.splitlines()
                if any(term in line for term in ("Overfull", "undefined", "LaTeX Error", "Warning:"))]
    assert not warnings, warnings
    assert "??" not in text
    record = {
        "algebraic_check": check_transfer(),
        "dimensional_to_normalized_check": check_physical_units(),
        "slow_limit_check": check_slow_limit(),
        "pdf_pages": len(doc), "pdf_words_whitespace": len(text.split()),
        "pdf_sha256": hashlib.sha256(pdf.read_bytes()).hexdigest(),
        "tex_warnings": warnings,
        "scope": "Source audit, derivations, equilibrium and linear-response calculations; no time-domain neuronal simulations.",
    }
    target = Path(__file__).with_name("field_coupling_note_check.json")
    target.write_text(json.dumps(record, indent=2) + "\n")
    print(json.dumps(record, indent=2))
