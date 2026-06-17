"""
v2 analyses: carrier independence, operating-point (sigma'') law,
2-D resonance map, and the JR bifurcation diagram.
Saves everything to analyses_v2.npz for the figure script.
"""
import time, numpy as np
from jr_demod import (integrate, steady_v, openloop_lockin, openloop_inphase,
                      freefield_minmax, Sigm, Sigm1, Sigm2, e0, v0, r)

t0 = time.time()
F0 = 11.1                      # natural (Hopf) frequency [Hz]
m  = 1.0
out = {}

# ---- (1) Operating-point law: open-loop A_Omega vs v*  ~ (1/2)|sigma''| eps^2 m
eps_ol = 0.5
vgrid  = np.linspace(-4.0, 18.0, 221)
A_ol   = openloop_lockin(vgrid, eps_ol, m, 2*np.pi*F0, fc=100.0, dt=2e-4, T=2.0)
A_theory = 0.5*np.abs(Sigm2(vgrid))*eps_ol**2*m
# SIGNED in-phase component -> verifies A_Omega ~ (1/2) sigma''(v*) eps^2 m incl. sign reversal
A_ol_signed     = openloop_inphase(vgrid, eps_ol, m, 2*np.pi*F0, fc=100.0, dt=2e-4, T=2.0)
A_theory_signed = 0.5*Sigm2(vgrid)*eps_ol**2*m
out.update(vgrid=vgrid, A_ol=A_ol, A_theory=A_theory, eps_ol=eps_ol,
           A_ol_signed=A_ol_signed, A_theory_signed=A_theory_signed)
print(f"[1] operating-point law done ({time.time()-t0:.0f}s). "
      f"peak A_ol={A_ol.max():.3f} at v*={vgrid[A_ol.argmax()]:.1f}; "
      f"min near inflection v0={v0}: A_ol={A_ol[np.argmin(np.abs(vgrid-v0))]:.4f}")

# operating points reached by the closed-loop JR for reference p-values
p_ref = np.array([265.,290.,310.,330.,355.,395.])
v_ref, _ = steady_v(p_ref)
out.update(p_ref=p_ref, v_ref=v_ref)

# ---- (2) Carrier independence (closed-loop JR + open-loop overlay)
fc_grid = np.geomspace(25., 300., 22)
p_ci    = np.full_like(fc_grid, 345.0)
Om_ci   = np.full_like(fc_grid, 2*np.pi*F0)
eps_ci  = 0.3
A_ci_cl = integrate(p_ci, Om_ci, eps_ci, m, fc_grid, t_settle=6.0, t_meas=3.0, dt=1e-4)
vop_ci, _ = steady_v(np.array([345.0]))
A_ci_ol = openloop_lockin(np.full(fc_grid.shape, vop_ci[0]), eps_ci, m,
                          2*np.pi*F0, fc_grid, dt=1e-4, T=3.0)
out.update(fc_grid=fc_grid, A_ci_cl=A_ci_cl, A_ci_ol=A_ci_ol, eps_ci=eps_ci, F0=F0)
print(f"[2] carrier sweep done ({time.time()-t0:.0f}s). closed-loop range "
      f"{A_ci_cl.min():.3f}-{A_ci_cl.max():.3f} mV over fc=25-300 Hz")

# ---- (3) 2-D resonance map: response @Omega vs (envelope freq, p)
f_map = np.arange(8.5, 13.51, 0.1)
p_map = np.linspace(318., 400., 12)
FF, PP = np.meshgrid(f_map, p_map)             # (np, nf)
A_map = integrate(PP.ravel(), 2*np.pi*FF.ravel(), 0.3, m, 100.0,
                  t_settle=10.0, t_meas=8.0, dt=2e-4).reshape(PP.shape)
out.update(f_map=f_map, p_map=p_map, A_map=A_map)
print(f"[3] 2-D map done ({time.time()-t0:.0f}s). max={A_map.max():.3f} mV")

# ---- (4) JR bifurcation diagram (field-free min/max of LFP vs p)
p_bif = np.linspace(0., 400., 161)
vmin, vmax, vmean = freefield_minmax(p_bif, dt=2e-4, t_settle=12.0, t_meas=2.0,
                                     seed_kick=1e-3)
out.update(p_bif=p_bif, vmin=vmin, vmax=vmax, vmean=vmean)
print(f"[4] bifurcation done ({time.time()-t0:.0f}s).")

np.savez("analyses_v2.npz", **out)
print(f"saved analyses_v2.npz  (total {time.time()-t0:.0f}s)")
