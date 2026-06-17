import numpy as np, jr_jsweep_engine as E
eps,m,fc=0.3,1.0,100.0; dt=2e-4; VSTAR=8.30
fdf=np.arange(8.0,13.51,0.15); Omg=2*np.pi*fdf
Csel=[118.0,126.0,132.0,135.8]
out={}
for C in Csel:
    p=E.p_of_C(VSTAR,C); g=E.jac_eig(p,C)[1]
    r=E.closed_lockin(np.full_like(Omg,p),np.full_like(Omg,C),Omg,eps,m,fc,11.0,6.0,dt)
    out[f"res_{int(round(C*10))}"]=r
    print(f"C={C:.1f} gamma={g:.2f} peak={r.max():.3f} mV at {fdf[r.argmax()]:.2f} Hz")
np.savez("jcurve_res.npz",fdf=fdf,Csel=Csel,**out)
