"""Lightweight self-checks for the JR demodulation engine. Run: python3 test_jr_demod.py"""
import numpy as np
from jr_demod import (Sigm, Sigm1, Sigm2, v0, e0, r, fixed_point_state, rhs,
                      integrate, steady_v)

def approx(a, b, tol): assert abs(a-b) <= tol, f"{a} vs {b} (tol {tol})"

def test_sigmoid_derivatives():
    v = np.linspace(-5, 18, 50); h = 1e-5
    d1 = (Sigm(v+h)-Sigm(v-h))/(2*h)
    d2 = (Sigm(v+h)-2*Sigm(v)+Sigm(v-h))/h**2
    assert np.max(np.abs(d1-Sigm1(v))) < 1e-4, "Sigm1 mismatch"
    assert np.max(np.abs(d2-Sigm2(v))) < 1e-3, "Sigm2 mismatch"
    approx(Sigm2(v0), 0.0, 1e-9)                      # vanishes at inflection
    approx(Sigm(v0), e0, 1e-9)                        # midpoint = e0
    print("ok  sigmoid derivatives (incl. sigma''(v0)=0)")

def test_fixed_point_is_equilibrium():
    p = np.array([100., 270., 395.])
    Y = fixed_point_state(p)
    res = np.max(np.abs(rhs(Y, p, np.zeros(3))))      # field-free RHS ~ 0 at FP
    assert res < 1e-6, f"FP residual {res}"
    print(f"ok  fixed point is an equilibrium (max|rhs|={res:.1e})")

def test_square_law():
    eps = np.array([0.05, 0.1, 0.2])
    resp = np.array([integrate(np.array([395.]), np.array([2*np.pi*10.9]),
                               e, 1.0, 100.0, 8.0, 3.0, 2e-4)[0] for e in eps])
    slope = np.polyfit(np.log(eps), np.log(resp), 1)[0]
    assert 1.8 < slope < 2.2, f"slope {slope}"
    print(f"ok  square-law demodulation (slope={slope:.2f})")

def test_linear_control_kills_response():
    p = np.array([330.]); Om = np.array([2*np.pi*11.1])
    vop, S1 = steady_v(p)
    r_nl = integrate(p, Om, 1.0, 1.0, 100.0, 10.0, 3.0, 2e-4)[0]
    r_li = integrate(p, Om, 1.0, 1.0, 100.0, 10.0, 3.0, 2e-4, lin=(vop, S1))[0]
    assert r_nl/max(r_li, 1e-12) > 100, f"ratio {r_nl/r_li}"
    print(f"ok  nonlinearity essential (nl/lin = {r_nl/r_li:.0f}x)")

if __name__ == "__main__":
    test_sigmoid_derivatives()
    test_fixed_point_is_equilibrium()
    test_square_law()
    test_linear_control_kills_response()
    print("ALL TESTS PASSED")
