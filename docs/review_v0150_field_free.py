"""Field-free LaNMM spectral/background check for the R6 integration.

Run with .venv/bin/python -B docs/review_v0150_field_free.py.
One 12-second simulated trajectory; no files are written.
"""
from pathlib import Path
import sys,time
sys.dont_write_bytecode=True
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'code'))
import numpy as np
import lanmm_field_tongues as L
start=time.perf_counter()
t,v1,v2=L.integrate(0.,np.array([25]),np.array([5]),wave='twotone',target='P2',dt=1e-4,t_settle=2.,t_meas=10.)
for v,label in [(v1,'P1'),(v2,'P2')]:
 w=np.hanning(len(v));x=v[:,0]-(v[:,0]*w).sum()/w.sum();amp=2*np.abs(np.fft.rfft(x*w))/w.sum();freq=np.fft.rfftfreq(len(v),1e-4)
 maxima=np.flatnonzero((amp[1:-1]>amp[:-2])&(amp[1:-1]>amp[2:]))+1
 maxima=maxima[(freq[maxima]>1)&(freq[maxima]<100)]
 ranked=maxima[np.argsort(amp[maxima])[::-1]][:15]
 print(label,'top spectral peaks (Hz,mV)',[(round(freq[i],4),round(amp[i],6)) for i in ranked])
 for beat in [8.,13.,10.5,10.6]:
  for a,b in [(0,3),(0,10),(4,10),(6,10)]:
   sel=(t>=2+a-1e-6)&(t<2+b-1e-6)
   print(label,'beat',beat,'window',a,b,'amplitude',L.lockin(v[sel],t[sel],np.array([beat]))[0])
print('walltime',time.perf_counter()-start)
