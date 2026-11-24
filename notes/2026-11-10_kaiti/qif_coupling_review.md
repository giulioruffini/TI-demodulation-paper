# Field coupling from a single neuron to QIF/MPR

Math review for the proposed coupling note, 10 November 2026. These derivations use TN0484's conventions: physical time, physical firing rate, dimensionless QIF voltage and drive. They distinguish the field coefficient entering an equation from the voltage response that the equation produces. No simulations were run.

## Voltage polarization and equivalent input are different quantities

For a specified cell, compartment, background state and field direction, define the weak-field voltage transfer by

\[
\lambda_V(\omega)=\frac{\widehat{\delta U}(\omega)}{\widehat E(\omega)},
\qquad [\lambda_V]={\rm mV}/({\rm V/m}).
\]

Hats denote complex amplitudes with time dependence \(e^{i\omega t}\), \(U\) is membrane voltage, and \(E\) is the signed field component along the chosen direction. This is generally a complex, frequency-dependent susceptibility. A quoted DC polarization slope is \(\lambda_V(0)\), not the coefficient of a current term.

If an equivalent injected current \(I_{\rm field}=\kappa_E E\) reproduces this voltage response, and \(Z_U=\widehat{\delta U}/\widehat{\delta I}\) is the cell's current-to-voltage impedance at the same state and input/output sites, then

\[
\lambda_V(\omega)=Z_U(\omega)\kappa_E(\omega),
\qquad [\kappa_E]={\rm nA}/({\rm V/m}),\quad [Z_U]={\rm mV}/{\rm nA}.
\]

Thus a polarization measurement alone does not determine an effective current coefficient. It also requires the appropriate impedance. In a passive one-compartment calibration, \(Z_U=R/(1+i\omega RC)\), so a frequency-independent equivalent-current coefficient is \(\kappa_E=\lambda_V(0)/R\). This representation is an approximation to the spatially extended cell: a uniform extracellular potential at an isolated mathematical point produces no transmembrane polarization. A scalar current fitted to somatic polarization need not reproduce dendritic or axonal polarization, spike-phase sensitivity, or the same response across frequencies and background conductances.

Zhao et al. use extracellular potentials at individual compartments and tune reduced-cell field coupling against realistic-cell entrainment at 10 Hz (§§2.2, 2.7). That supplies a useful low-frequency model calibration, not a universal conversion from mV/(V/m) to QIF drive. [Published full text](https://www.researchgate.net/publication/379307155_Intensity-_and_frequency-specific_effects_of_transcranial_alternating_current_stimulation_are_explained_by_network_dynamics), [DOI](https://doi.org/10.1088/1741-2552/ad37d9).

## Nondimensionalization fixes the QIF input coefficient

One possible dimensional QIF normal form is

\[
C\dot U_j=g_Q(U_j-U_c)^2+I_{\eta,j}+I_{\rm syn}(t)+\kappa_E E(t).
\]

Here \(C\) is capacitance, \(g_Q>0\) has units of current/voltage squared, \(U_c\) is the voltage origin of the quadratic normal form, and the remaining terms are currents. This is a chosen normal-form calibration, not a statement that a real neuron's ionic current is globally quadratic. Choose a voltage scale \(U_s>0\), and define

\[
v_j=\frac{U_j-U_c}{U_s},\qquad
I_s=g_QU_s^2,\qquad
\tau_m=\frac{CU_s}{I_s}=\frac{C}{g_QU_s},\qquad
\lambda_I=\frac{\kappa_E}{I_s}.
\]

Then \(v_j\), \(\eta_j=I_{\eta,j}/I_s\), and normalized input \(I=I_{\rm syn}/I_s\) are dimensionless, \(\tau_m\) is time, and \([\lambda_I]=({\rm V/m})^{-1}\). With instantaneous rate coupling written in TN0484's convention,

\[
\tau_m\dot v_j=v_j^2+\eta_j+\tau_m J r(t)+I_0(t)+\lambda_I E(t).
\tag{1}
\]

The synaptic weight \(J\) is dimensionless and \(r\) has units of inverse time. A filtered synaptic rate \(s(t)\) can replace \(r(t)\) without changing the field term. Dimensional physical rates must use the same time unit as \(\tau_m\). The physical scale \(U_s\) and current scale \(I_s\) are needed before mapping this model to mV or nA; TN0484 currently specifies neither for the PING simulations.

As a simple check, linearize a quiescent, uncoupled QIF cell about \(v_*<0\), with its non-field drive fixed. Its transfer is

\[
\lambda_V^{\rm cell}(\omega)
=U_s\frac{\lambda_I}{i\omega\tau_m-2v_*},
\qquad
\lambda_I=\frac{i\omega\tau_m-2v_*}{U_s}\lambda_V^{\rm cell}(\omega).
\tag{2}
\]

The QIF coefficient \(\lambda_I\) is consequently not \(\lambda_V/U_s\). Even at DC, the local restoring slope \(-2v_*\) enters. Equation (2) is not the response formula for a repetitively spiking cell.

## The same common drive enters the exact mean field

Take the infinite-population, all-to-all QIF limit, with symmetric spike/reset limits \(+\infty\to-\infty\), common \(\tau_m\), common additive field coefficient \(\lambda_I\), and Lorentzian excitabilities centered at \(\bar\eta\) with half-width \(\Delta>0\). The MPR equations in our convention are

\[
\begin{aligned}
\tau_m\dot r&=\frac{\Delta}{\pi\tau_m}+2rv,\\
\tau_m\dot v&=v^2+\bar\eta-(\pi\tau_mr)^2
 +\tau_mJr+I_0(t)+\lambda_I E(t).
\end{aligned}
\tag{3}
\]

There is no population-size factor multiplying \(\lambda_I\). For the conditional Lorentzian voltage density, write its width and center as \(x(\eta,t)\) and \(y(\eta,t)\), and set \(w=x+iy\). The continuity equation gives

\[
\tau_m\partial_t w=i\{\eta+\tau_mJr+I_0+\lambda_IE-w^2\}.
\]

Evaluating at the excitability pole \(\eta=\bar\eta-i\Delta\), with \(w=\pi\tau_mr+iv\), gives (3). The field coefficient is inherited because the field drive is common; the reduction itself neither attenuates nor amplifies it. Exactness concerns the specified QIF continuum and its invariant manifold; attraction from broader initial densities requires the usual regularity conditions. [MPR 2015, §§II–III, Eqs. (1)–(12)](https://journals.aps.org/prx/pdf/10.1103/PhysRevX.5.021028).

The voltage variable is a Cauchy-principal-value population mean, not an ordinary mean of an unbounded voltage distribution. For each excitability, \(y={\rm PV}\int u\rho(u\mid\eta,t)du\), and \(v=\int y\,g(\eta)d\eta\). The Lorentzian's ordinary first moment is undefined. One therefore cannot obtain (3) by naively averaging \(v_j^2\) and replacing it by the square of a sample mean. A finite Hodgkin–Huxley soma-voltage average is a different observable and needs an explicit mapping. Even QIF reset conventions matter: taking the spike and reset magnitudes to infinity at fixed ratio \(a=V_{\rm peak}/|V_{\rm reset}|\) gives the regularized voltage \(v_a=v+\tau_m r\ln a\). [MPR 2015, Eqs. (8)–(9)](https://journals.aps.org/prx/pdf/10.1103/PhysRevX.5.021028); [Montbrió and Pazó 2020, Eqs. (8)–(11)](https://arxiv.org/pdf/2009.01445), [published DOI](https://doi.org/10.1103/PhysRevLett.125.248101).

## Recurrent coupling changes susceptibility

At a stable equilibrium \((r_0,v_0)\), let \(z=i\omega\tau_m-2v_0\). Linearizing (3) gives

\[
z\,\widehat{\delta r}-2r_0\widehat{\delta v}=0,
\qquad
z\,\widehat{\delta v}+(2\pi^2\tau_m^2r_0-\tau_mJ)
\widehat{\delta r}=\lambda_I\widehat E.
\]

Consequently,

\[
D_J(\omega)=z^2+4(\pi\tau_mr_0)^2-2\tau_mJr_0,
\qquad
\frac{\widehat{\delta v}}{\widehat E}=\lambda_I\frac{z}{D_J},
\qquad
\frac{\widehat{\delta r}}{\widehat E}=\lambda_I\frac{2r_0}{D_J}.
\tag{4}
\]

The denominator is dimensionless. The first transfer has units \((\mathrm{V/m})^{-1}\); the second has units rate/(V/m). Multiplying the voltage transfer by \(U_s\) gives

\[
\lambda_V^{\rm pop}(\omega;J)=U_s\lambda_I\frac{z}{D_J(\omega)}.
\tag{5}
\]

This is a closed-network voltage susceptibility. It depends on \(J\) explicitly and through \((r_0,v_0)\), even when \(\lambda_I\) is unchanged. A DC compensation that pins the equilibrium removes the second dependence while leaving the first. For a normalized linear synaptic filter with transfer \(H_s(\omega)\), replace \(J\) in the last term of \(D_J\) by \(JH_s(\omega)\). A second-order synapse has \(H_s=(1+i\omega\tau_s)^{-2}\). Setting the feedback variation to zero while keeping the equilibrium gives the local population transfer; it still differs from the single-cell transfer (2), owing to the coupled rate and voltage variables.

The instantaneous, one-population system (3) is an algebraic illustration, not TN0484's PING circuit. Its two eigenvalues have trace \(4v_0/\tau_m<0\) for \(\Delta>0,r_0>0\), so it cannot cross a Hopf at finite \(r_0\) while \(\Delta>0\). For PING, include both populations and all synaptic states in \(X\), and use the full fixed-point Jacobian \(A_J\). With E-only field input, \(B\) has entry \(\lambda_{I,E}/\tau_E\) in the E-voltage equation and zero elsewhere. Then

\[
\lambda_{V,E}^{\rm pop}(\omega;J)
=U_{s,E}\,e_{v_E}^{\mathsf T}(i\omega\mathbf1-A_J)^{-1}B.
\tag{6}
\]

Here \(e_{v_E}\) selects E voltage. This is a direct linearization, not an extra fitted coupling. A pole near a Hopf can amplify the response when the input and readout project onto its mode. The microscopic input coefficient need not change. These formulas allow individually spiking neurons: the condition is a stationary population state, not silence of every cell. Our current PING sweep changes \(J\) without pinning the equilibrium, so both effects occur.

For a constant additive \(\lambda_I\), (4) also checks the high-frequency scaling:
\(\widehat{\delta v}/\widehat E\sim\lambda_I/(i\omega\tau_m)\).
Squaring these already-filtered carrier excursions generates the \(1/(\omega_1\omega_2\tau_m^2)\) beat-source factor. Applying this same membrane filter again would double-count its dynamics. A separate compartmental input filter is permissible only when it represents a separate physical element and is calibrated accordingly.

## Orientation heterogeneity and oscillatory states require more structure

If cell \(j\) receives \(\boldsymbol\lambda_{I,j}\cdot\mathbf E\), the common-drive assumption fails. For finitely many orientation/coupling classes, each class can retain its own MPR pair, provided its conditional excitabilities satisfy the required closure assumptions; classes interact through the weighted total synaptic rates. A continuous joint distribution of coupling and excitability generally requires a conditional density, an integral over classes, or another justified closure. Replacing all couplings by their arithmetic mean is not generally exact. Even for otherwise identical cells, a vanishing mean signed coupling can cancel a linear response while a quadratic response proportional to a coupling product remains. The second moment/product cannot be reconstructed from the first moment alone. General excitability distributions also need more than the standard two variables in general. [Pietras and Montbrió, 2024 preprint, §§2–3](https://arxiv.org/html/2409.18278v1).

A periodically oscillating baseline has a time-periodic linearization,
\(\delta\dot X=A(t)\delta X+B(t)E(t)\), and can produce responses at the input frequency and sidebands. Equations (4)–(6) then require a Floquet/harmonic-response replacement; a single voltage-amplitude ratio must specify phase averaging and the selected spectral component. For a single spiking QIF cell, \(v=\tan(\theta/2)\) gives

\[
\tau_m\dot\theta=1-\cos\theta+
(1+\cos\theta)[\eta+I_{\rm syn}+I_0+\lambda_IE],
\]

so even constant additive current coupling yields phase-dependent sensitivity. Spike-phase locking cannot identify an intrinsic polarization coefficient without the dynamical model and state.

## Consequence for the proposed parameter study

Estimate the field-to-voltage transfer at named compartments with recurrence suppressed or its input replayed, while keeping the background state specified. Estimate the corresponding current-to-voltage transfer before converting to a normalized drive coefficient. Restore recurrence and measure the closed response with the same input and voltage observable; separate a free-state coupling sweep from a compensated-state sweep. Report the latter result as susceptibility or gain, not as a change in the microscopic field coefficient. Preserve individual-cell/compartment measurements when the signed population average cancels them. A voltage scale and a documented regularization/readout are required before comparing a physical network's mean voltage with MPR's \(v\). Equations (1)–(6) use current-based synaptic drive; Zhao's conductance-based synapses also change the voltage-dependent membrane operator, so an unchanged mean firing rate alone does not identify an unchanged local impedance.

TN0484's current Methods already correctly call \(\lambda_I\) normalized drive per V/m and the PING amplitudes model units. The introductory comment in `code/nmm2_ping.py` still says “delta V = lambda.E”; that comment must not be used as the dimensional definition in the new note.
