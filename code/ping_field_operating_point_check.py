"""Check the R7 carrier-averaged estimate against the published PING RHS.

Use a finite-difference Jacobian and direct time average of the quadratic RHS
to check the resolvent/Hessian source, then integrate the original mean-field
code at a=10 and 35. This tests an averaged approximation, not its exactness at
finite amplitude. The original QIF spiking cache is neither read nor changed.
"""
import argparse
import json
from pathlib import Path

import numpy as np
from scipy.optimize import brentq, root

import ping_field_operating_point as K


def rhs(x, shift=0.0):
    value = K.M._rhs(x, 0.0, 0.85, 0.0, 0.0, 0.0)
    value[1] += shift / K.TE
    return value


def jacobian(fun, x, h=1e-6):
    eye = np.eye(len(x)) * h
    return np.column_stack([(fun(x + d) - fun(x - d)) / (2*h) for d in eye])


def e_only_point(shift):
    sol = root(lambda x: rhs(x, shift), K.P.ping_equilibrium(K.C, 0.85), tol=1e-11)
    assert np.linalg.norm(rhs(sol.x, shift)) < 1e-9
    return sol.x


def max_real(matrix):
    return float(np.linalg.eigvals(matrix).real.max())


def direct_run(a, dt=0.05):
    x = e_only_point(0.0)
    omega = 2*np.pi*55/1000
    carrier = 2*np.pi*300/1000
    values = []
    t = 0.0
    for step in range(int(1600/dt)):
        x = K.M._rk4(x, t, dt, 0.85, a, omega, carrier)
        t += dt
        if step >= int(800/dt):
            values.append(x[0])
    return np.array(values)[:, None]


def check():
    archived = json.loads((Path(__file__).resolve().parents[1] / "docs" /
                          "r7_ping_field_operating_point_2026-10-05.json").read_text())
    critical = brentq(lambda s: max_real(jacobian(rhs, e_only_point(s))), 0.15, 0.5,
                      xtol=1e-10)
    assert abs(critical - archived['E_only_critical_shift']['delta_eta_E']) < 1e-8
    result = {"E_only_critical_shift": critical, "amplitudes": [],
              "scope": "second-order DC approximation; full two-tone mean-field integration"}
    for a in (10.0, 35.0):
        x, source = K.effective_point(0.85, a, 300.0, 55.0)
        residual = np.linalg.norm(rhs(x) + K.dc_source(x, a, 300, 55))
        assert residual < 1e-10
        A = jacobian(rhs, x)
        b = np.eye(8)[1] / K.TE
        # Both tones complete whole cycles in 400 ms, so their cross term averages out.
        t = np.arange(4096)*400/4096
        excursion = np.zeros((8, len(t)))
        for frequency in (272.5, 327.5):
            w = 2*np.pi*frequency/1000
            q = np.linalg.solve(1j*w*np.eye(8) - A, b)
            excursion += a*np.real(q[:, None]*np.exp(1j*w*t))
        averaged = (rhs(x[:, None] + excursion) - rhs(x)[:, None]).mean(axis=1)
        error = float(np.max(np.abs(averaged-source)))
        assert error < 1e-10
        growth = max_real(jacobian(lambda y: rhs(y) + K.dc_source(y, a, 300, 55), x))
        mean, beat, other, frequency, _, _ = K.spectrum_lines(direct_run(a), 0.05, 55)
        old = next(row for row in archived['amplitudes'] if row['a'] == a)
        for name, value in [('mf_mean_rE', mean[0]), ('mf_beat_depth', beat[0]),
                            ('mf_other_line_depth', other[0])]:
            assert abs(value-old[name]) < 1e-9, (a, name, value, old[name])
        result['amplitudes'].append(dict(
            amplitude=a, fixed_point_residual=float(residual),
            source_max_abs_error=error, delta_eta_E=float(K.TE*source[1]),
            source_rate_E=float(source[0]), source_voltage_E=float(source[1]),
            leading_real_per_ms=growth, effective_rate=float(x[0]),
            integrated_rate=float(mean[0]), beat_depth=float(beat[0]),
            other_gamma_depth=float(other[0]), other_gamma_Hz=float(frequency[0])))
    return result


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--json', required=True, type=Path)
    args = parser.parse_args()
    output = check()
    args.json.write_text(json.dumps(output, indent=2) + '\n')
    print(json.dumps(output, indent=2))
