"""Check arithmetic changed by the draft11 text pass; no trajectories are rerun.

Run from the project root with .venv/bin/python code/verify_draft11_text_math.py.
The JSON on stdout records the checks; all comparisons have explicit assertions.
"""
import json
from pathlib import Path

import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq

import jr_demod as jr
from ping_fast_carrier_check import C_closed, C_matrix


def jr_leading_pair(p):
    state = jr.fixed_point_state(p)[0]
    y0, y1, y2 = state[:3]
    jac = np.zeros((6, 6))
    jac[:3, 3:] = np.eye(3)
    jac[3, 0], jac[3, 3] = -jr.a**2, -2*jr.a
    jac[3, 1] = jr.A*jr.a*jr.Sigm1(y1-y2)
    jac[3, 2] = -jac[3, 1]
    jac[4, 0] = jr.A*jr.a*jr.C2*jr.C1*jr.Sigm1(jr.C1*y0)
    jac[4, 1], jac[4, 4] = -jr.a**2, -2*jr.a
    jac[5, 0] = jr.B*jr.b*jr.C4*jr.C3*jr.Sigm1(jr.C3*y0)
    jac[5, 2], jac[5, 5] = -jr.b**2, -2*jr.b
    eig = np.linalg.eigvals(jac)
    return eig[np.argmax(eig.real)]


def main():
    report = {}
    voltages = np.linspace(-10, 22, 101)
    z = jr.r*(voltages-jr.v0)
    peix = np.sign(z)*(1-4*np.exp(-z)/(1+np.exp(-z))**2)
    slope_error = float(np.max(np.abs(jr.Sigm1(voltages)/jr.Sigm1(jr.v0)-(1-np.abs(peix)))))
    predicted_curvature = -jr.r*jr.Sigm1(voltages)*np.sign(peix)*np.sqrt(np.abs(peix))
    curvature_error = float(np.max(np.abs(jr.Sigm2(voltages)-predicted_curvature)))
    assert slope_error < 1e-14 and curvature_error < 1e-14
    report['peix'] = dict(slope_identity_max_error=slope_error,
                          curvature_identity_max_error=curvature_error,
                          at_inflection=0, saturation_limits=[-1, 1])

    mixing_errors = [abs(C_closed(q, w)-C_matrix(q, w))
                     for q in (-3, 0, 1, 5) for w in (0, 0.3, 1, 4, 20)]
    assert max(mixing_errors) < 1e-14
    report['qif_second_order'] = dict(phasor_vs_closed_form_max_error=max(mixing_errors),
                                      operating_points=4, frequencies=5)

    ratios = []
    for quadratic in (-2, -0.5, 0, 0.5, 2):
        eps = 0.4
        def signal(theta):
            envelope = 2*eps*abs(np.cos(theta/2))
            return envelope+quadratic*envelope**2
        harmonics = [quad(lambda t: signal(t)*np.cos(n*t), 0, 2*np.pi,
                          points=[np.pi], epsabs=1e-12)[0]/np.pi for n in (1, 2)]
        measured = abs(harmonics[1]/harmonics[0])
        predicted = 0.2/abs(1+3*np.pi*quadratic*eps/4)
        assert abs(measured-predicted) < 1e-12
        ratios.append(dict(c2_over_c1=quadratic, quadrature=measured, formula=predicted))
    report['mixed_detector_ratio'] = ratios

    hopf = brentq(lambda p: jr_leading_pair(p).real, 310, 322, xtol=1e-10)
    frequency = abs(jr_leading_pair(hopf).imag)/(2*np.pi)
    assert abs(hopf-315.69641894) < 1e-5 and round(frequency, 2) == 11.16
    continuation = np.load(Path(__file__).parent/'jr_bifurcation.npz', allow_pickle=True)
    hopf_markers = [float(v) for k, v in zip(continuation['bif_label'], continuation['bif_value'])
                    if 'HB' in k and '+' in k]
    assert any(abs(v-89.829) < 0.002 for v in hopf_markers)
    assert any(abs(v-hopf) < 1e-5 for v in hopf_markers)
    report['jr_hopf'] = dict(upper_p_per_s=hopf, frequency_Hz=frequency,
                             cached_supercritical_markers=hopf_markers)

    access = []
    for frequency_Hz in (1000, 2000, 10000):
        factor = 1+(2*np.pi*frequency_Hz*0.016)**2
        access.append(dict(frequency_Hz=frequency_Hz,
                           point_membrane_beat=1/factor, cable_end_beat=1/np.sqrt(factor)))
    report['access_16ms'] = access
    polarization = 0.5*0.5/np.sqrt(1+(2*np.pi*2000*0.0002)**2)
    efficiency = abs(jr.Sigm2(8.30))*0.1/(4*jr.Sigm1(8.30))
    assert round(polarization, 3) == 0.092
    assert 0.0078 < efficiency < 0.0081
    report['illustrative_budget'] = dict(polarization_mV=polarization,
                                         efficiency_at_0p1mV=efficiency,
                                         width_for_eps_0p02_mV_in_microvolts=0.02/6*1000)
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
