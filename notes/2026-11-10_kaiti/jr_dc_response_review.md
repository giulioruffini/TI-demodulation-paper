# DC polarization and recurrent response in the pinned JR column

Calculation from `code/jr_jsweep_engine.py`, November 10, 2026. The engine was imported read-only. Only scalar equilibrium solves, analytical Jacobians, eigendecompositions and frequency-domain response calculations were used; no time-domain simulations were run. The script's finite-difference Jacobian gives the same field-free damping rates within about \(6\times10^{-7}\,\mathrm{s}^{-1}\).

## The field perturbs the sigmoid argument

The model uses

\[
S(u)=\frac{5}{1+\exp[0.56(6-u)]}\quad\mathrm{s}^{-1},
\qquad u=v+\varepsilon,\qquad v=y_1-y_2.
\]

Here \(v\) is the recurrent synaptic voltage difference in mV, \(\varepsilon\) is the externally imposed polarization entering the sigmoid in mV, and \(u\) is the total sigmoid argument. The pyramidal population rate is \(r_P=S(u)\). These are different readouts. A negative change in \(v\) does not imply a negative change in \(u\) or \(r_P\).

At the field-free pinned state \(v^*=8.30\) mV,

\[
r_0=3.91904238\ \mathrm{s}^{-1},\qquad
S'(v^*)=0.474467697\ \mathrm{s}^{-1}\mathrm{mV}^{-1},\qquad
S''(v^*)=-0.150816908\ \mathrm{s}^{-1}\mathrm{mV}^{-2}.
\]

Holding the recurrent voltage fixed, \(+0.2\) mV changes the rate by
\(S(8.5)-S(8.3)=0.0918771\,\mathrm{s}^{-1}\), or 2.3444% of baseline. The linear estimate is \(0.0948935\,\mathrm{s}^{-1}\). For \(-0.2\) mV the exact local change is \(-0.0979032\,\mathrm{s}^{-1}\). Thus the local sigmoid effect is finite and modest; the closed column does not necessarily amplify it.

These calculations assume that 0.2 mV is the polarization at this model's detector entry. They do not infer a field amplitude in V/m or establish that a measured somatic polarization has the same effect at the population's effective detector.

## Static feedback partly cancels the imposed polarization

Write \(k_A=A/a=0.0325\,\mathrm{mV\,s}\), \(k_B=B/b=0.44\,\mathrm{mV\,s}\), and let \(C\) denote the engine's connectivity parameter. Its other constants are \(A=3.25\) mV, \(B=22\) mV, \(a=100\,\mathrm{s}^{-1}\), \(b=50\,\mathrm{s}^{-1}\). At equilibrium,

\[
y_0=k_Ar_P,\quad
v=F_C(r_P)=k_A[p+0.8C S(Ck_Ar_P)]
-k_B(0.25C)S(0.25Ck_Ar_P).
\]

The background drive \(p=p(C)\) pins the **field-free** state and is held fixed when DC is applied. Define the dimensionless static loop factor

\[
L_0=S'(v^*)F_C'(r_0),\qquad
F_C'(r_0)=k_A\{k_A(0.8C^2)S'(Cy_0)
-k_B(0.0625C^2)S'(0.25Cy_0)\}.
\]

The linear DC responses follow by differentiating \(r_P=S(F_C(r_P)+\varepsilon)\):

\[
\frac{\mathrm d r_P}{\mathrm d\varepsilon}=\frac{S'(v^*)}{1-L_0},\qquad
\frac{\mathrm d u}{\mathrm d\varepsilon}=\frac1{1-L_0},\qquad
\frac{\mathrm d v}{\mathrm d\varepsilon}=\frac{L_0}{1-L_0}.
\tag{1}
\]

The rate gain has units \(\mathrm{s}^{-1}\mathrm{mV}^{-1}\); both voltage gains are dimensionless. The negative loop factors below reflect inhibitory dominance at zero frequency. Increasing \(C\) along this pinned path suppresses the DC change in the total argument and rate, while the synaptic voltage becomes more compensatory.

| \(C\) | \(p(C)\), s\(^{-1}\) | \(L_0\) | \(\mathrm du/\mathrm d\varepsilon\) | \(\mathrm dv/\mathrm d\varepsilon\) | \(\mathrm dr_P/\mathrm d\varepsilon\), s\(^{-1}\)/mV |
|---:|---:|---:|---:|---:|---:|
| 110 | 188.9665 | −2.13222 | 0.319262 | −0.680738 | 0.151480 |
| 130 | 310.5173 | −3.81726 | 0.207587 | −0.792413 | 0.098493 |
| 136.3 | 363.9346 | −4.44016 | 0.183818 | −0.816182 | 0.087216 |

For the finite constant input \(\varepsilon=+0.2\) mV, I solved \(u=F_C(S(u))+\varepsilon\) near the field-free branch. All three equilibria remain stable:

| \(C\) | Exact \(\Delta v\), mV | Exact \(\Delta u\), mV | Exact \(\Delta r_P\), s\(^{-1}\) | Rate change | Damping after DC, s\(^{-1}\) |
|---:|---:|---:|---:|---:|---:|
| 110 | −0.136001 | +0.063999 | +0.030056 | +0.7669% | 10.92175 |
| 130 | −0.158366 | +0.041634 | +0.019623 | +0.5007% | 2.77255 |
| 136.3 | −0.163136 | +0.036864 | +0.017388 | +0.4437% | 0.24716 |

For \(\varepsilon=-0.2\) mV, the rate changes are −0.030541, −0.019775 and −0.017498 s\(^{-1}\), respectively. At \(C=136.3\), the negative input leaves only \(0.0045987\,\mathrm{s}^{-1}\) of damping: the local linear relaxation time is about 217 s. A short transient run would therefore not establish its equilibrium response.

## Oscillatory gain behaves differently

The linear response can be calculated without integrating the model. Let

\[
H_A(\omega)=\frac{Aa}{(a+i\omega)^2},\qquad
H_B(\omega)=\frac{Bb}{(b+i\omega)^2},
\]

and define the synaptic rate-to-voltage return transfer

\[
K(\omega)=H_A(\omega)
\{0.8C^2S'(Cy_0)H_A(\omega)
-0.0625C^2S'(0.25Cy_0)H_B(\omega)\}.
\]

Here \(K\) has units mV s and \(L(\omega)=S'(v^*)K(\omega)\) is dimensionless. For a small direct sinusoidal polarization at the same sigmoid entry,

\[
\chi_v=\frac{L}{1-L},\qquad
\chi_u=\frac1{1-L},\qquad
\chi_r=\frac{S'(v^*)}{1-L}.
\tag{2}
\]

These transfers include the direct contribution to \(u\) and \(r_P\); \(v\) contains only the recurrent synaptic response. Equation (2) reduces to (1) at zero frequency. Maximizing \(|\chi_v|\) between 0 and 40 Hz gives:

| \(C\) | Field-free damping \(\gamma\), s\(^{-1}\) | Peak frequency, Hz | \(|\chi_v|\), mV/mV | \(|\chi_u|\), mV/mV | \(|\chi_r|\), s\(^{-1}\)/mV |
|---:|---:|---:|---:|---:|---:|
| 110 | 10.73905 | 8.75575 | 1.67495 | 2.31099 | 1.09649 |
| 130 | 2.64262 | 10.69803 | 9.00712 | 9.68096 | 4.59330 |
| 136.3 | 0.123443 | 11.17267 | 206.363 | 207.050 | 98.2384 |

The final two columns are evaluated at the voltage-response peak, not independently optimized. These are **infinitesimal gains**, not predictions for a 0.2-mV tACS input. Near the final state, multiplying that finite amplitude by the linear rate gain would even exceed the sigmoid's 5-s\(^{-1}\) ceiling. Saturation and stimulation-induced state shifts must then be retained. No finite-amplitude tACS response was computed here.

## DC can change criticality without sharing resonant amplification

The distinction is between driving an existing susceptible mode and changing the state that determines that mode. Along the field-free pinned path, the Hopf is at \(C_H=136.6125855\), with frequency 11.19493 Hz. The static loop factor there is −4.47220, so \(\mathrm du/\mathrm d\varepsilon=0.182742\) remains finite. The DC rate response does not inherit the divergence of the response at the oscillatory mode's frequency.

For a general stable fixed point, a constant forcing changes the state by \(-A^{-1}B\varepsilon\) at first order. A Hopf pair tends to \(\pm i\omega_0\), with \(\omega_0\ne0\), so it does not make \(A^{-1}\) singular. In contrast, a zero-eigenvalue transition, such as a saddle-node, can yield a large static susceptibility if the input and readout project onto that mode. In this scalar JR equilibrium formulation the corresponding static condition is \(1-L_0\to0\). It is not approached by the negative values of \(L_0\) in the table.

Nevertheless, DC changes the equilibrium and therefore the Jacobian. At fixed \(C=136.3\), the field-free damping is 0.123443 s\(^{-1}\); +0.2 mV raises it to 0.247157 s\(^{-1}\), while −0.2 mV lowers it to 0.004599 s\(^{-1}\). Continuing the same equilibrium branch algebraically gives a complex-pair stability crossing at

\[
\varepsilon_H=-0.2079071\ \mathrm{mV},\qquad
u_H=8.2618881\ \mathrm{mV},\qquad
\Delta r_{P,H}=-0.0181924\ \mathrm{s}^{-1},\qquad
f_H=11.19033\ \mathrm{Hz}.
\]

This is an equilibrium/Jacobian crossing, not a simulation of the resulting attractor or a determination of Hopf criticality. It demonstrates that a small change in mean rate can materially change oscillatory stability. tDCS can therefore influence an oscillatory transition by shifting the operating state, even when its static mean-rate effect is modest. The polarity and size of this effect are state dependent; the positive input in this example moves the column away from the transition.

## Interpretation for the discussion

A measured cellular polarization should enter the specified model input without an arbitrary population multiplier, provided that input channel and physical calibration are justified. The model then determines the response. In this pinned JR example, inserting +0.2 mV produces a local rate increase of 2.34%, reduced by recurrent static feedback to 0.44–0.77%. This is a numerical model result, not a judgment about physiological detectability or behavioral significance.

Near an oscillatory instability, weak tACS at the resonant frequency can receive large linear gain. DC instead changes the equilibrium, and may move the circuit toward or through the instability. Near a zero-frequency instability, DC itself can receive large static gain. These mechanisms should be named separately when asking whether tDCS can benefit from criticality.

The local TI/direct source ratio in TN0484 is not invalidated by this distinction. At a common state and detector entry, the weak steady TI source and the direct tDCS source share the same zero-frequency closed transfer; weak beat and tACS sources share the transfer at their common frequency. Finite-amplitude state shifts and secondary rectification of an amplified beat can change these comparisons.
