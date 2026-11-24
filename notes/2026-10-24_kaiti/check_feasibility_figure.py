"""Check the figure's saved curves and the largest static-input expansion error."""
from pathlib import Path
import csv,json
import numpy as np
ROOT=Path(__file__).resolve().parents[2]
rho,v0,e0,vstar=.56,6.,2.5,8.3
sig=lambda v:2*e0/(1+np.exp(rho*(v0-v)))
q=sig(vstar)/(2*e0)
slope=2*e0*rho*q*(1-q)
curvature=slope*rho*(1-2*q)
rows=list(csv.DictReader((ROOT/'code/feasibility_khz_curves.csv').open()))
for row in rows:
 f=float(row['fc_Hz']);tau=float(row['tau_ms'])/1000
 coupling=float(row['lambda0_mV_per_Vm']);field=float(row['E_per_tone_Vm'])
 amplitudes=[coupling*field/(1+(2*np.pi*(f+df)*tau)**2)**.5 for df in (-5,5)]
 np.testing.assert_allclose(float(row['eps_eq_mV']),curvature*np.prod(amplitudes)/(2*slope),rtol=1e-12)
 np.testing.assert_allclose(float(row['Y_DC_per_s']),curvature*np.sum(np.square(amplitudes))/4,rtol=1e-12)
# Largest post-access excursion in the plotted grid: fc=300 Hz, tau=.05 ms,
# lambda=.5 mV/(V/m), and E=1 V/m per tone. Integrate an exact common period.
a,b=[.5/(1+(2*np.pi*f*.00005)**2)**.5 for f in (295,305)]
t=np.arange(200000)/200000*.2
y=sig(vstar+a*np.cos(2*np.pi*295*t)+b*np.cos(2*np.pi*305*t))
dc=y.mean()-sig(vstar);beat=2*np.mean((y-sig(vstar))*np.cos(2*np.pi*10*t))
result=dict(max_grid_polarization_mV=max(a,b),
            dc_relative_error=float(dc/(curvature*(a*a+b*b)/4)-1),
            beat_relative_error=float(beat/(curvature*a*b/2)-1))
assert abs(result['beat_relative_error'])<.03
assert abs(result['dc_relative_error'])<.03
(ROOT/'notes/2026-10-24_kaiti/feasibility_quadrature.json').write_text(json.dumps(result,indent=2)+'\n')
print(f'PASS: {len(rows)} saved curves agree with independent formulas.')
print('Largest-excursion static quadrature:',result)
