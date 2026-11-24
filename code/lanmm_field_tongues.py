"""
LaNMM Arnold tongues with the field entering the *sigmoid argument*.

Why this file exists
--------------------
`lanmm_arnold_tongues.py` injects the TI field as an additive perturbation of the
external input *firing rate*, then clips the total at zero because rates cannot be
negative:

    e2 = mu + A(1 + cos Om t) cos(wc t);   e2 <- max(e2, 0)

With mu = 90 /s for the P2 drive and the AM term swinging to -2A, the clip engages
for A > 45 while the published sweep runs to A = 300. A hard clip is a half-wave
rectifier, i.e. a diode detector, sitting upstream of the sigmoid: it puts a large
line at Delta f into the drive *before* the population nonlinearity ever sees it.
Measured at A = 250, the clipped drive carries 66 /s at 10 Hz against a 90 /s
baseline; unclipped it carries exactly zero. The demodulation attributed to sigma''
was therefore substantially performed by the clip.

This module couples the field the way the paper's own theory specifies
(Eq. 7, phi = Sigma(v + lambda E), as the single-column JR code already does):
the field is a *membrane-potential perturbation added inside the sigmoid argument*
of the target population. Being a signed potential it carries no positivity
constraint, so no clip is needed and none is applied. External drives stay flat at
their baselines.

The field amplitude is consequently in mV and directly comparable to the JR epsilon
(the sigmoid voltage scale is 1/r = 1.79 mV in both models), which also removes the
units ambiguity in the notation table.

Both waveforms are supported on the same coupling path:

    'am'      s(t) = eps (1 + m cos Om t) cos(wc t)            [surrogate]
    'twotone' s(t) = eps [cos(w1 t) + cos(w2 t)],  w2-w1 = Om  [physical TI]

At m = 1 the two have the same peak polarization (2 eps) and the same leading
quadratic component at Omega (1/2 sigma'' eps^2), so `eps` is directly comparable
between them. They differ in DC and in the second harmonic: the AM surrogate emits
a 2*Omega line at 25% of the fundamental, genuine two tones emit exactly none.

Integration is a vectorized fixed-step RK4 advancing the whole parameter grid at
once, as in the JR sweeps.

Outputs
-------
    lanmm_field_<target>_<wave>.npz   cached grids
"""

import os
import numpy as np

# ---------------------------------------------------------------- model tables
# LaNMM v11 intrinsic parameters (values inlined so this module does not depend
# on the external lanmmv11 import path; verified against lanmmv11.get_intrinsic_params).
V0_DEFAULT, V0_P2 = 6.0, 1.0
FMAX, R_SLOPE = 5.0, 0.56

A_AMPA, A_AMPA_RATE = 3.25, 100.0
A_GABA_SLOW, A_GABA_SLOW_RATE = -22.0, 50.0
A_GABA_FAST, A_GABA_FAST_RATE = -30.0, 220.0

SYN_TYPES = {1: 'AMPA', 2: 'GABA_slow', 3: 'AMPA', 4: 'AMPA', 5: 'AMPA',
             6: 'AMPA', 7: 'GABA_fast', 8: 'AMPA', 9: 'AMPA', 10: 'GABA_fast',
             11: 'AMPA', 12: 'AMPA', 13: 'AMPA', 14: 'AMPA'}
C_VALS = {1: 108.0, 2: 33.7, 3: 1.0, 4: 135.0, 5: 33.75, 6: 70.0, 7: 550.0,
          8: 1.0, 9: 200.0, 10: 100.0, 11: 80.0, 12: 200.0, 13: 30.0, 14: 1.0}

# external drive baselines (firing rates, /s) -- held flat, never modulated
MU_E1, MU_E2, MU_PV = 270.0, 90.0, 0.0

_AV = np.array([{'AMPA': A_AMPA, 'GABA_slow': A_GABA_SLOW,
                 'GABA_fast': A_GABA_FAST}[SYN_TYPES[s]] for s in range(1, 15)])
_aV = np.array([{'AMPA': A_AMPA_RATE, 'GABA_slow': A_GABA_SLOW_RATE,
                 'GABA_fast': A_GABA_FAST_RATE}[SYN_TYPES[s]] for s in range(1, 15)])
_CV = np.array([C_VALS[s] for s in range(1, 15)])

ALPHA_BAND = (8.0, 12.0)


def _sig(v, v0):
    return FMAX / (1.0 + np.exp(R_SLOPE * (v0 - v)))


def field(t, eps, fc, df, wave):
    """TI field as a membrane perturbation, mV. Shapes broadcast over the grid."""
    om, wc = 2 * np.pi * df, 2 * np.pi * fc
    if wave == 'am':
        return eps * (1.0 + np.cos(om * t)) * np.cos(wc * t)
    if wave == 'twotone':
        return eps * (np.cos((wc - om / 2) * t) + np.cos((wc + om / 2) * t))
    raise ValueError(f"unknown wave {wave!r}")


def _rhs(Y, t, eps, fc, df, wave, target):
    """Y has shape (28, N). Returns dY/dt."""
    u = Y[0::2]                       # (14, N) -- u(s) at index s-1
    z = Y[1::2]

    vP1 = u[0] + u[1] + u[2] + u[10]
    vSS = u[3]
    vSST = u[4]
    vP2 = u[5] + u[6] + u[7] + u[11]
    vPV = u[8] + u[9] + u[12] + u[13]

    s = field(t, eps, fc, df, wave)
    # the field perturbs the target population's sigmoid argument only
    sP1 = _sig(vP1 + (s if target == 'P1' else 0.0), V0_DEFAULT)
    sP2 = _sig(vP2 + (s if target == 'P2' else 0.0), V0_P2)
    sSS = _sig(vSS, V0_DEFAULT)
    sSST = _sig(vSST, V0_DEFAULT)
    sPV = _sig(vPV, V0_DEFAULT)

    N = Y.shape[1]
    pre = np.empty((14, N))
    pre[0] = sSS
    pre[1] = sSST
    pre[2] = MU_E1                    # external P1 drive, flat
    pre[3] = sP1
    pre[4] = sP1
    pre[5] = sP2
    pre[6] = sPV
    pre[7] = MU_E2                    # external P2 drive, flat
    pre[8] = sP2
    pre[9] = sPV
    pre[10] = sP2
    pre[11] = sP1
    pre[12] = sP1
    pre[13] = MU_PV

    dz = (_aV[:, None] * _AV[:, None] * (_CV[:, None] * pre)
          - 2 * _aV[:, None] * z - (_aV[:, None] ** 2) * u)
    dY = np.empty_like(Y)
    dY[0::2] = z
    dY[1::2] = dz
    return dY


def integrate(eps, fc, df, wave='am', target='P2', dt=1e-4, t_settle=2.0,
              t_meas=3.0):
    """Vectorized RK4 over the whole parameter grid. Returns (t, vP1, vP2)."""
    eps, fc, df = np.broadcast_arrays(np.asarray(eps, float),
                                      np.asarray(fc, float),
                                      np.asarray(df, float))
    eps, fc, df = eps.ravel(), fc.ravel(), df.ravel()
    N = eps.size
    Y = np.zeros((28, N))
    t = 0.0
    for _ in range(int(t_settle / dt)):
        k1 = _rhs(Y, t, eps, fc, df, wave, target)
        k2 = _rhs(Y + .5 * dt * k1, t + .5 * dt, eps, fc, df, wave, target)
        k3 = _rhs(Y + .5 * dt * k2, t + .5 * dt, eps, fc, df, wave, target)
        k4 = _rhs(Y + dt * k3, t + dt, eps, fc, df, wave, target)
        Y = Y + (dt / 6) * (k1 + 2 * k2 + 2 * k3 + k4)
        t += dt

    nm = int(t_meas / dt)
    v1 = np.empty((nm, N))
    v2 = np.empty((nm, N))
    ts = np.empty(nm)
    for i in range(nm):
        u = Y[0::2]
        v1[i] = u[0] + u[1] + u[2] + u[10]
        v2[i] = u[5] + u[6] + u[7] + u[11]
        ts[i] = t
        k1 = _rhs(Y, t, eps, fc, df, wave, target)
        k2 = _rhs(Y + .5 * dt * k1, t + .5 * dt, eps, fc, df, wave, target)
        k3 = _rhs(Y + .5 * dt * k2, t + .5 * dt, eps, fc, df, wave, target)
        k4 = _rhs(Y + dt * k3, t + dt, eps, fc, df, wave, target)
        Y = Y + (dt / 6) * (k1 + 2 * k2 + 2 * k3 + k4)
        t += dt
    return ts, v1, v2


def band_power(v, dt, band=ALPHA_BAND):
    """Mean spectral power of each column of v in `band`."""
    n = v.shape[0]
    w = np.hanning(n)[:, None]
    V = np.abs(np.fft.rfft((v - v.mean(0)) * w, axis=0)) ** 2
    f = np.fft.rfftfreq(n, dt)
    m = (f >= band[0]) & (f <= band[1])
    return V[m].mean(0)


def lockin(v, t, df):
    """Quadrature lock-in amplitude of each column of v at df (Eq. 12 of the paper).

    Band power cannot see a weak coherent drive underneath a strong autonomous
    rhythm: the P1 loop free-runs at ~10 Hz, so its alpha power is dominated by an
    oscillation that is not phase-locked to the beat, and the stimulation-induced
    change is buried in run-to-run variability. The lock-in is referenced to the
    drive phase, so the unlocked autonomous alpha averages away and only the
    envelope-locked component survives.
    """
    w = np.hanning(v.shape[0])[:, None]
    om = 2 * np.pi * np.atleast_1d(df)[None, :]
    tt = t[:, None]
    vb = v - (w * v).sum(0) / w.sum()
    I = 2 * (w * vb * np.cos(om * tt)).sum(0) / w.sum()
    Q = 2 * (w * vb * np.sin(om * tt)).sum(0) / w.sum()
    return np.hypot(I, Q)


def dominant_freq(v, dt, band=(4.0, 20.0)):
    n = v.shape[0]
    w = np.hanning(n)[:, None]
    V = np.abs(np.fft.rfft((v - v.mean(0)) * w, axis=0))
    f = np.fft.rfftfreq(n, dt)
    m = (f >= band[0]) & (f <= band[1])
    return f[m][np.argmax(V[m], axis=0)]


# ------------------------------------------------------------------- the maps
def tongue(eps_grid, df_grid, fc=40.0, wave='am', target='P2', **kw):
    """Alpha enhancement over the eps=0 baseline, on the (eps, df) grid."""
    E, D = np.meshgrid(eps_grid, df_grid, indexing='ij')
    dt = kw.get('dt', 1e-4)
    t, v1, v2 = integrate(E, fc, D, wave=wave, target=target, **kw)
    P1 = band_power(v1, dt).reshape(E.shape)
    P2 = band_power(v2, dt).reshape(E.shape)
    F1 = dominant_freq(v1, dt).reshape(E.shape)
    ref1, ref2 = P1[0].copy(), P2[0].copy()          # eps = 0 row
    return P1 - ref1, P2 - ref2, F1


def carrier_map(fc_grid, df_grid, eps, wave='am', target='P2', **kw):
    """Alpha enhancement over the eps=0 baseline, on the (fc, df) grid."""
    F, D = np.meshgrid(fc_grid, df_grid, indexing='ij')
    dt = kw.get('dt', 1e-4)
    _, v1, v2 = integrate(eps, F, D, wave=wave, target=target, **kw)
    P1 = band_power(v1, dt).reshape(F.shape)
    P2 = band_power(v2, dt).reshape(F.shape)
    _, b1, b2 = integrate(0.0, F, D, wave=wave, target=target, **kw)
    return P1 - band_power(b1, dt).reshape(F.shape), \
           P2 - band_power(b2, dt).reshape(F.shape)


if __name__ == '__main__':
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument('--target', default='P2', choices=['P1', 'P2'])
    ap.add_argument('--wave', default='am', choices=['am', 'twotone'])
    ap.add_argument('--quick', action='store_true')
    # The two loops have different sensitivities: the deep P1 alpha generator is
    # captured by a far weaker field than the superficial P2 gamma loop, so a range
    # that is perturbative for P2 saturates P1. Defaults are per target.
    ap.add_argument('--eps-max', type=float, default=None)
    ap.add_argument('--eps-carrier', type=float, default=None)
    a = ap.parse_args()

    n = 9 if a.quick else 31
    nd = 13 if a.quick else 41
    nc = 12 if a.quick else 56
    eps_max = a.eps_max if a.eps_max is not None else (1.0 if a.target == 'P1' else 3.0)
    eps_c = a.eps_carrier if a.eps_carrier is not None else (0.5 if a.target == 'P1' else 1.5)
    eps_g = np.linspace(0, eps_max, n)
    df_g = np.linspace(5, 15, nd)
    fc_g = np.linspace(25, 80, nc)

    kw = dict(dt=1e-4, t_settle=1.5 if a.quick else 2.0,
              t_meas=2.0 if a.quick else 3.0)

    print(f'tongue: target={a.target} wave={a.wave} grid={n}x{nd}')
    Pt1, Pt2, F1 = tongue(eps_g, df_g, wave=a.wave, target=a.target, **kw)
    print(f'carrier map: grid={nc}x{nd} at eps={eps_c}')
    Pc1, Pc2 = carrier_map(fc_g, df_g, eps_c, wave=a.wave, target=a.target, **kw)

    out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       f'lanmm_field_{a.target}_{a.wave}.npz')
    np.savez(out, Pt1=Pt1, Pt2=Pt2, F1=F1, eps=eps_g, df=df_g,
             Pc1=Pc1, Pc2=Pc2, fc=fc_g, eps_c=eps_c)
    print('wrote', out)
