"""Export the IXI002 fields from the private producer, checking centroid conventions.

TI_MODEL_ROOT=/path/to/library python code/export_fem_portable.py --output fields.npz
Requires the original fields, labels, and TI library. Does not alter them.
"""
import argparse
import hashlib
import json
from pathlib import Path
import numpy as np
from fem_portable import maps, focus, TOPS, SHARES, analyze


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    if args.output.suffix != '.npz':
        raise SystemExit('Output must have an .npz suffix')
    if args.output.exists():
        raise SystemExit('Output exists; choose a new path')
    # Import here so --help works without the private library or its data.
    import fem_quadmaps as original
    arrays = {}
    for montage in original.MONTAGES:
        h = original.held(montage)
        tags = h['rows'][:, 1]
        gm, wm = tags == original.GM, tags == original.WM
        labels = {lab: original.qm.roi_mask(h['xyz'], lab) for lab in ('aseg', 'atlas')}
        a = dict(xyz_mm=h['xyz'], E1_per_A=h['E1'], E2_per_A=h['E2'], n_star=h['n_star'],
                 gm=gm, wm=wm, **labels)
        arrays.update({f'{montage}__{k}': v for k,v in a.items()})
        radial = h['xyz']-h['xyz'][gm|wm].mean(axis=0)
        radial /= np.maximum(np.linalg.norm(radial, axis=1, keepdims=True), 1e-300)
        for direction in (h['n_star'], radial):
            for label in labels.values():
                for tissue in (gm|wm, gm):
                    roi = label & tissue
                    for share in SHARES:
                        for value in maps(h['E1'], h['E2'], direction, share).values():
                            for fraction in TOPS:
                                c, selected = focus(h['xyz'][roi], value[roi], fraction)
                                old = original.focus_centroid(h['xyz'][roi], value[roi], fraction)
                                if not np.array_equal(np.sort(selected), np.sort(old['selected'])):
                                    raise RuntimeError('Original focus selection differs; export stopped')
                                np.testing.assert_allclose(c, old['centroid_mm'], rtol=0, atol=1e-10)
    cached = json.loads((Path(__file__).parent/'fem_quadmaps.json').read_text())
    actual_hashes = {f'fields_{m}': original.hash_file(original.qm.OUT/'fields'/f'{m}.npz')
                     for m in original.MONTAGES}
    actual_hashes.update(aseg=original.hash_file(original.qm.LABELS['aseg'][0]),
                         atlas_label=original.hash_file(original.qm.LABELS['atlas'][0]))
    if actual_hashes != cached['provenance']['inputs_sha512']:
        raise RuntimeError('Original input hashes differ from the published analysis')
    meta = dict(schema='tn0484-fields-v1' , montages=list(original.MONTAGES),
                units=dict(xyz_mm='mm', E1_per_A='(V/m)/A', E2_per_A='(V/m)/A'),
                coupling_mV_per_Vm=.5, total_current_A=.004,
                reference='gray matter outside ROI, including deep gray matter',
                orientation='envelope-maximizing at 1:1, fixed across all current ratios',
                original_provenance=cached['provenance'], focus_selection_verified=True)
    result = analyze(meta, arrays)
    primary = result['montages']['violante']['n_star/aseg/gm_wm']['sweep']
    for ratio, share in [('1:1', .5), ('1:3', .75)]:
        row = next(r for r in primary if np.isclose(r['share'], share))
        for key in ('env', 'quad', 'msp', 'iso'):
            for stat in ('roi_mean', 'roi_p95', 'tc_mean', 'tc_p95'):
                np.testing.assert_allclose(row['statistics'][key][stat],
                    cached['conditions'][ratio][key][stat], rtol=1e-10, atol=1e-12)
    np.savez_compressed(args.output, metadata=json.dumps(meta), **arrays)
    digest = hashlib.sha256(args.output.read_bytes()).hexdigest()
    args.output.with_suffix('.sha256').write_text(f'{digest}  {args.output.name}\n')
    print(f'Exported {args.output}; centroid conventions and cached primary contrasts verified.')

if __name__ == '__main__':
    main()
