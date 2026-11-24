"""Analytic invariants of the independent consumer; not an IXI002 reproduction."""
from pathlib import Path
import sys
import numpy as np
sys.path.insert(0, str(Path(__file__).resolve().parents[2]/'code'))
from fem_portable import maps, contrast, focus, axis
rng = np.random.default_rng(484)
e1, e2 = rng.normal(size=(2, 80, 3))
n = rng.normal(size=(80,3)); n /= np.linalg.norm(n,axis=1,keepdims=True)
a = maps(e1,e2,n,.5); b = maps(e1,e2,n,.75)
for key in ('quad','iso'):
    np.testing.assert_allclose(b[key], .75*a[key], rtol=1e-14)
# Polarity reversal changes the signed beat phase but none of these magnitude maps.
c = maps(-e1,e2,n,.5)
for key in a: np.testing.assert_allclose(a[key],c[key])
# Rotation covariance checks all vector contractions, including isotropic averaging.
rot,_ = np.linalg.qr(rng.normal(size=(3,3)))
c = maps(e1@rot,e2@rot,n@rot,.5)
for key in a: np.testing.assert_allclose(a[key],c[key],rtol=1e-12,atol=1e-20)
# Equal fields/directions have equal beat and steady geometric amplitudes up to factor two.
e=np.tile([1000.,0.,0.],(4,1)); direction=np.tile([1.,0.,0.],(4,1))
c=maps(e,e,direction,.5)
np.testing.assert_allclose(c['env'],2.)
np.testing.assert_allclose(c['quad'],2.)
np.testing.assert_allclose(c['msp'],1.)
np.testing.assert_allclose(c['iso'],2/3)
# Centroid and PCA have a known geometric answer.
xyz=np.column_stack([np.zeros(10),np.arange(10.),np.zeros(10)])
centroid,chosen=focus(xyz,np.arange(10.),.2)
np.testing.assert_array_equal(chosen,[8,9]); np.testing.assert_allclose(centroid,[0,8.5,0])
np.testing.assert_allclose(axis(xyz),[0,1,0])
# Degree matching removes the order difference for a squared common scalar map.
v=np.arange(1.,81.); roi=np.arange(80)<20; ref=~roi
raw=contrast(v,roi,ref); matched=contrast(np.sqrt(v*v),roi,ref)
assert raw==matched
print('PASS: current-ratio invariance, polarity, rotations, units, centroid, axis, degree matching.')
print('IXI002 export and comparison remain pending the original fields and labels.')
