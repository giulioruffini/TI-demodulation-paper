"""Screen existing NMM2 sweep states for the second-order rectified DC shift.

S10 uses the AM surrogate A(1+cos(Omega*t))*cos(omega_c*t), so its three
tone amplitudes are A, A/2, A/2. The resonance examples use two equal tones.
This DC-only screen does not establish stability of the full periodically
forced solution, which requires a separate dynamic calculation.
"""
import argparse
import json
from pathlib import Path

import numpy as np
from scipy.optimize import root

import ping_field_operating_point as K


def evaluate(coupling, eta, beat, am):
    K.C = float(coupling)

    def source(x):
        jac = K.P.ping_jacobian(x, coupling)
        b = np.eye(8)[1] / K.TE
        value = np.zeros(8)
        tones = ([(300, 8), (300-beat, 4), (300+beat, 4)] if am
                 else [(300-beat/2, 8), (300+beat/2, 8)])
        for frequency, amplitude in tones:
            q = np.linalg.solve(1j*2*np.pi*frequency/1000*np.eye(8)-jac, b)
            value += (amplitude**2/4)*K.P.ping_hessian(q, q.conj()).real
        return value

    baseline = K.fixed_point(eta, eta)
    fun = lambda x: K.f0(x, eta, eta) + source(x)
    sol = root(fun, baseline, tol=1e-11)
    assert np.linalg.norm(fun(sol.x)) < 1e-9
    h = 1e-6
    jac = np.column_stack([(fun(sol.x+d)-fun(sol.x-d))/(2*h)
                           for d in np.eye(8)*h])
    return dict(C=float(coupling), eta=float(eta), beat_Hz=float(beat),
                waveform='AM' if am else 'two-tone',
                free_growth=float(K.leading_mode(baseline)[0]),
                averaged_growth=float(np.linalg.eigvals(jac).real.max()),
                shift=float(K.TE*source(sol.x)[1]))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--json', required=True, type=Path)
    args = parser.parse_args()
    cache = np.load(Path(__file__).with_name('nmm2_jcD.npz'))
    rows = [evaluate(c, 0, beat, True) for c, beat in zip(cache['C'], cache['fpk'])]
    resonance = [evaluate(15, eta, 55, False) for eta in (0, .7, .9, 1.0)]
    output = dict(scope='second-order DC stability screen; no finite-amplitude periodic-orbit test',
                  jcurve=rows, resonance_states=resonance)
    args.json.write_text(json.dumps(output, indent=2) + '\n')
    print(f"S10: {sum(row['averaged_growth'] > 0 for row in rows)}/{len(rows)} averaged states unstable")
