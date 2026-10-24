"""Recompute spatial statistics from exported per-node fields using only NumPy.

Run: python code/fem_portable.py fields.npz --output results.json
See docs/fem_portable.md for the schema and the still-pending IXI002 export.
The existing sagittal image cache is separate: this program recomputes nodal
maps, contrasts, current-ratio sweeps, and centroid displacements, not FEM solves.
"""
import argparse
import json
from pathlib import Path
import numpy as np

MAPS = ('env', 'quad', 'msp', 'iso')
SHARES = np.round(np.arange(.1, .9001, .025), 3)
TOPS = (.05, .10, .25, .50)


def maps(e1, e2, direction, share, coupling=.5, total_a=.004):
    """Fields are (V/m)/A, coupling is mV/(V/m), output mV or mV squared."""
    i1, i2 = total_a * (1-share), total_a * share
    a = coupling * i1 * np.einsum('ij,ij->i', e1, direction)
    b = coupling * i2 * np.einsum('ij,ij->i', e2, direction)
    return dict(env=2*np.minimum(abs(a), abs(b)), quad=2*abs(a*b),
                msp=(a*a+b*b)/2,
                iso=(2/3)*coupling**2*i1*i2*abs(np.einsum('ij,ij->i', e1, e2)))


def contrast(values, roi, reference):
    denominator = float(np.percentile(values[reference], 95))
    if denominator <= 0:
        raise ValueError('Reference percentile must be positive')
    mean, p95 = float(values[roi].mean()), float(np.percentile(values[roi], 95))
    return dict(roi_mean=mean, roi_p95=p95, reference_p95=denominator,
                tc_mean=mean/denominator, tc_p95=p95/denominator)


def table(values, roi, reference):
    result = {}
    for key, value in values.items():
        result[key] = contrast(value, roi, reference)
        if key != 'env':
            result[key]['degree_matched'] = contrast(np.sqrt(value), roi, reference)
    return result


def focus(xyz, value, fraction):
    """Unweighted centroid of ceil(fraction*N) highest nodes; stable index ties.

    The exporter checks agreement with the original library for all analyzed
    masks and fractions. It aborts if the original selection differs.
    """
    n = max(1, int(np.ceil(fraction * len(value))))
    selected = np.argsort(value, kind='stable')[-n:]
    return xyz[selected].mean(axis=0), selected


def axis(xyz):
    centered = xyz - xyz.mean(axis=0)
    _, _, vt = np.linalg.svd(centered, full_matrices=False)
    vector = vt[0]
    return vector if vector[1] >= 0 else -vector


def read_bundle(path):
    with np.load(path, allow_pickle=False) as src:
        meta = json.loads(str(src['metadata']))
        arrays = {key: src[key] for key in src.files if key != 'metadata'}
    if meta['schema'] != 'tn0484-fields-v1':
        raise ValueError('Unsupported field bundle schema')
    for montage in meta['montages']:
        h = {key: arrays[f'{montage}__{key}'] for key in
             ('xyz_mm', 'E1_per_A', 'E2_per_A', 'n_star', 'gm', 'wm', 'aseg', 'atlas')}
        n = len(h['xyz_mm'])
        for key in ('xyz_mm', 'E1_per_A', 'E2_per_A', 'n_star'):
            if h[key].shape != (n, 3) or not np.isfinite(h[key]).all():
                raise ValueError(f'Invalid {montage}/{key}')
        for key in ('gm', 'wm', 'aseg', 'atlas'):
            if h[key].shape != (n,) or h[key].dtype != np.bool_:
                raise ValueError(f'Invalid mask {montage}/{key}')
        norm = np.linalg.norm(h['n_star'], axis=1)
        # A zero direction is valid only where the fields yield no envelope.
        if not np.all(np.isclose(norm, 1) | np.isclose(norm, 0)):
            raise ValueError('Projection directions must be unit vectors or zero')
    return meta, arrays


def analyze(meta, arrays):
    out = dict(schema='tn0484-statistics-v1', source=meta, montages={})
    for montage in meta['montages']:
        h = {key: arrays[f'{montage}__{key}'] for key in
             ('xyz_mm', 'E1_per_A', 'E2_per_A', 'n_star', 'gm', 'wm', 'aseg', 'atlas')}
        xyz, e1, e2 = h['xyz_mm'], h['E1_per_A'], h['E2_per_A']
        brain = h['gm'] | h['wm']
        radial = xyz - xyz[brain].mean(axis=0)
        radial /= np.maximum(np.linalg.norm(radial, axis=1, keepdims=True), 1e-300)
        results = {}
        for direction_name, direction in [('n_star', h['n_star']), ('radial', radial)]:
            for label in ('aseg', 'atlas'):
                for tissue in ('gm_wm', 'gm'):
                    roi = h[label] & (brain if tissue == 'gm_wm' else h['gm'])
                    reference = h['gm'] & ~roi
                    if roi.sum() < 3 or not reference.any():
                        raise ValueError('Empty or insufficient target/reference mask')
                    long_axis = axis(xyz[roi])
                    baseline = maps(e1, e2, direction, .5)
                    centroids = {k: {str(t): focus(xyz[roi], v[roi], t)[0]
                                     for t in TOPS} for k,v in baseline.items()}
                    sweep = []
                    for share in SHARES:
                        values = maps(e1, e2, direction, share)
                        foci = {}
                        for key, value in values.items():
                            foci[key] = {}
                            for t in TOPS:
                                c, selected = focus(xyz[roi], value[roi], t)
                                d = c-centroids[key][str(t)]
                                foci[key][str(t)] = dict(centroid_mm=c.tolist(),
                                    displacement_axis_mm=float(d@long_axis),
                                    displacement_norm_mm=float(np.linalg.norm(d)),
                                    n_selected=len(selected))
                        sweep.append(dict(share=float(share), statistics=table(values, roi, reference),
                                          foci=foci))
                    results[f'{direction_name}/{label}/{tissue}'] = dict(
                        n_roi=int(roi.sum()), n_reference=int(reference.sum()),
                        axis_anterior=long_axis.tolist(), sweep=sweep)
        out['montages'][montage] = results
    return out


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('bundle', type=Path)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    meta, arrays = read_bundle(args.bundle)
    args.output.write_text(json.dumps(analyze(meta, arrays), indent=2)+'\n')

if __name__ == '__main__':
    main()
