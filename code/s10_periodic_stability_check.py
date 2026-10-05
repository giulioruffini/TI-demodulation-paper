"""Independent full-period stability check of the S10 endpoint.

The AM input at carrier 300 Hz and beat 50.5 Hz repeats after 2000 ms.
After 8000 ms of settling, integrate the full variational matrix over that
period. Its eigenvalues are Floquet multipliers if the orbit closes; report
closure and repeatability alongside the largest modulus. A single finite-time
tangent-vector exponent is not used to decide stability here.
"""
import argparse
import json
from pathlib import Path

import numpy as np
import nmm2_jcD_endpoint_check as D


def check():
    cache = np.load(Path(__file__).with_name('nmm2_jcD.npz'))
    coupling, beat = float(cache['C'][-1]), float(cache['fpk'][-1])
    assert abs(beat-50.5) < 1e-12
    dt, period, settle = 0.05, 2000.0, 8000.0
    params = (0.0, coupling, 8.0, 2*np.pi*beat/1000, 2*np.pi*300/1000)
    y = D.J.init(1)[:, 0]
    for k in range(round(settle/dt)):
        y = D.J.rk4(y, k*dt, dt, *params)
    h = 1e-6
    numerical = np.column_stack([
        (D.J.rhs(y+d, settle, *params)-D.J.rhs(y-d, settle, *params))/(2*h)
        for d in np.eye(8)*h])
    jac_error = float(np.max(np.abs(numerical-D.jac(y, coupling))))
    assert jac_error < 1e-7
    rows = []
    for cycle in range(2):
        start = y.copy()
        matrix = np.eye(8)
        for k in range(round(period/dt)):
            time = settle + cycle*period + k*dt
            y, matrix = D.step_pair(y, matrix, time, dt, *params)
        multiplier = float(np.max(np.abs(np.linalg.eigvals(matrix))))
        rows.append(dict(period_start_ms=settle+cycle*period,
                         relative_closure=float(np.linalg.norm(y-start)/np.linalg.norm(start)),
                         largest_multiplier_modulus=multiplier,
                         leading_exponent_per_ms=float(np.log(multiplier)/period)))
    assert rows[-1]['relative_closure'] < 1e-6
    assert all(row['largest_multiplier_modulus'] < 1 for row in rows)
    return dict(C=coupling, eta=0.0, amplitude=8.0, carrier_Hz=300.0, beat_Hz=beat,
                dt_ms=dt, period_ms=period, settle_ms=settle,
                jacobian_max_error=jac_error, periods=rows)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--json', required=True, type=Path)
    args = parser.parse_args()
    result = check()
    args.json.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))
