"""
QIF spiking network and exact mean field at a chosen two-tone amplitude (review brief,
October 5, 2026). Same model, population size, time step, settling, integer-cycle
windows, and statistics as qif_raster.py (its functions are imported unchanged);
only the per-tone amplitude and the window floor are parameters. Writes
qif_raster_twotone_a<Af><tag>.npz with the layout of the published cache, never the
published cache itself.

    python qif_raster_amp.py --af 10                       # both conditions, off/on, 800 ms floor
    python qif_raster_amp.py --af 10 --floor-ms 1600 --conditions forced --tag _long
"""
import os, sys, argparse, time
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import qif_raster as Q
Q.WAVE = 'twotone'

ap = argparse.ArgumentParser()
ap.add_argument('--af', type=float, required=True)
ap.add_argument('--floor-ms', type=float, default=800.0)
ap.add_argument('--settle-ms', type=float, default=800.0)
ap.add_argument('--conditions', default='forced,entrain')
ap.add_argument('--n', type=int, default=8000)
ap.add_argument('--dt', type=float, default=0.0025)
ap.add_argument('--tag', default='')
a = ap.parse_args()
Ne = Ni = a.n; dt = a.dt; fc = 300.0
regimes = dict(forced=(0.85, 55.0), entrain=(1.5, 42.0))


def window(df, floor_ms):
    ncyc = int(np.ceil(floor_ms * df / 1000.0))
    return ncyc * 1000.0 / df, ncyc


conds = {}; meta_w = {}
for reg in a.conditions.split(','):
    eta, df = regimes[reg]
    t_meas, ncyc = window(df, a.floor_ms); T = a.settle_ms + t_meas; kmeas = int((T - t_meas) / dt)
    meta_w[reg] = dict(T=T, t_meas=t_meas, ncyc=ncyc, kmeas=kmeas)
    for fld, Afv in (('off', 0.0), ('on', a.af)):
        t0 = time.perf_counter()
        q = Q.qif_run(eta, Afv, fc, df, Ne, Ni, T, dt, t_meas)
        tm, rm = Q.mf_run(eta, Afv, fc, df, T, dt)
        q['AC'] = Q.lockin(q['ts'], q['re_t'], df, kmeas)
        q['df'] = df; q['T'] = T; q['t_meas'] = t_meas; q['kmeas'] = kmeas
        conds[f'{reg}_{fld}'] = dict(q=q, mf_t=tm, mf_re=rm)
        print(f"{reg:8s} {fld:3s}: Af={Afv:g} T={T:.1f} window={t_meas:.1f} ms ({ncyc} cycles) <r_e>={q['rmean']:.4f} "
              f"AC@{df:.0f}Hz={q['AC']:.4f} depth={q['AC']/q['rmean']:.4f} VS={q['VS']:.3f} PPC={q['PPC']:.4f} "
              f"PPC/neuron median={q['PPC_n_median']:.4f} spikes(rec)={q['spk_t'].size}  [{(time.perf_counter()-t0)/60:.1f} min]", flush=True)
out = os.path.join(HERE, f"qif_raster_twotone_a{a.af:g}{a.tag}.npz")
np.savez(out, meta=dict(Ne=Ne, Ni=Ni, dt=dt, T_settle=a.settle_ms, windows=meta_w, fc=fc, Af=a.af,
                        eta_forced=0.85, df_forced=55.0, eta_entrain=1.5, df_entrain=42.0, VPEAK=Q.VPEAK,
                        floor_ms=a.floor_ms, wave='twotone'),
         conds=conds, allow_pickle=True)
print('saved', out)
