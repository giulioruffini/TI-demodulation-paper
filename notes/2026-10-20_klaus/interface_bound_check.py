"""Interface jump: magnitude and own-maximum maps are bounded by r; a fixed projection is not.
E_low = A E_high, A = I + (r-1) nu nu^T (tangential continuous, normal current continuous)."""
import numpy as np
rng = np.random.default_rng(0)
r = 4.5
def unit(v): return v/np.linalg.norm(v)
def fib_sphere(n=4000):
    i = np.arange(n)+0.5; phi = np.arccos(1-2*i/n); th = np.pi*(1+5**0.5)*i
    return np.c_[np.cos(th)*np.sin(phi), np.sin(th)*np.sin(phi), np.cos(phi)]
N = fib_sphere()
def env_max(E1,E2):            # TImax: max_n 2 min(|n.E1|,|n.E2|)
    p = N@np.c_[E1,E2]; return 2*np.min(np.abs(p),axis=1).max()
def quad_max(E1,E2):           # max_n 2|n.E1||n.E2|
    p = N@np.c_[E1,E2]; return 2*np.abs(p[:,0]*p[:,1]).max()
def msp_max(E1,E2):            # max_n (a^2+b^2)/2 = top eigenvalue /2
    return np.linalg.eigvalsh(np.outer(E1,E1)+np.outer(E2,E2)).max()/2
def nstar(E1,E2):              # envelope-maximizing direction
    p = N@np.c_[E1,E2]; return N[np.argmax(np.min(np.abs(p),axis=1))]
worst = dict(mag=0, env=0, quad=0, msp=0)
fixed_env, fixed_quad, fixed_msp, fixed_mag_ratio = [], [], [], []
for _ in range(20000):
    nu = unit(rng.normal(size=3)); A = np.eye(3)+(r-1)*np.outer(nu,nu)
    E1 = rng.normal(size=3); E2 = rng.normal(size=3)
    L1, L2 = A@E1, A@E2
    worst['mag'] = max(worst['mag'], np.linalg.norm(L1)/np.linalg.norm(E1))
    worst['env'] = max(worst['env'], env_max(L1,L2)/env_max(E1,E2))
    worst['quad'] = max(worst['quad'], quad_max(L1,L2)/quad_max(E1,E2))
    worst['msp'] = max(worst['msp'], msp_max(L1,L2)/msp_max(E1,E2))
    n = nstar(L1,L2)            # envelope-optimal direction chosen on the LOW (GM) side, held fixed
    a_h, b_h = n@E1, n@E2; a_l, b_l = n@L1, n@L2
    fixed_env.append(2*min(abs(a_l),abs(b_l))/(2*min(abs(a_h),abs(b_h))))
    fixed_quad.append(abs(a_l*b_l)/abs(a_h*b_h))
    fixed_msp.append((a_l**2+b_l**2)/(a_h**2+b_h**2))
print(f"r = {r}; r^2 = {r*r}")
print("worst ratio over 20000 random interfaces, own-maximum maps:")
for k,v in worst.items(): print(f"  {k:5s} {v:.3f}  (bound {'r' if k in ('mag','env') else 'r^2'})")
for name, arr in [('envelope',fixed_env),('quadratic',fixed_quad),('msp',fixed_msp)]:
    a = np.array(arr); bound = r if name=='envelope' else r*r
    print(f"fixed n* (GM-side envelope optimum): {name:9s} median {np.median(a):.2f}, p99 {np.percentile(a,99):.1f}, max {a.max():.1f}, fraction > bound {np.mean(a>bound):.3f}, fraction < 1 {np.mean(a<1):.3f}")
# explicit counterexample: tangential and normal projections cancel on the high side
nu = np.array([0,0,1.0]); A = np.eye(3)+(r-1)*np.outer(nu,nu)
E = np.array([1.0,0,0.2]); n = unit(np.array([-0.2,0,1.0]))   # n.E_high = -0.2+0.2 = 0
print("counterexample: n.E_high =", round(n@E,6), " n.E_low =", round(n@(A@E),4), " |E_low|/|E_high| =", round(np.linalg.norm(A@E)/np.linalg.norm(E),3))
# median-inversion caveat: marginal medians (0.20, 0.46) vs realized per-node jumps
j = 0.46*np.sqrt(0.98**2)/np.sqrt(1-0.46**2)/0.20
print("common-node idealization j from (0.20,0.46):", round(j,2))
