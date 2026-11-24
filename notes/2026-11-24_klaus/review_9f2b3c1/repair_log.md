# TN0484 fidelity repairs (working tree, uncommitted)
Each replacement was applied only if its old text occurred exactly once in the live file.

## 2 (Intro)
File: `TN0484_envelope_demodulation.tex`

Old:
```latex
\cite{reato2010,liu2018,krause2023}. Under the quasistatic approximation,
```
New:
```latex
\cite{reato2010,liu2018,krause2023}. Its reach to deep targets is limited
by physics. Under the quasistatic approximation,
```

## 10 (material, §dc)
File: `TN0484_envelope_demodulation.tex`

Old:
```latex
has unrestricted sign. The beat amplitude and envelope excursion can have strict
interior maxima in this model (supplement, \S\ref{supp:interior-maxima}).
```
New:
```latex
has unrestricted sign. Within this homogeneous scalar model, interior
selectivity must come from the oscillatory response, not either mean map.
```

## 11 (§dynamic)
File: `TN0484_envelope_demodulation.tex`

Old:
```latex
At fixed synaptic input, weak-carrier
rectification follows
```
New:
```latex
At fixed synaptic input, weak-carrier
steady rectification follows
```

## 12 (§dynamic)
File: `TN0484_envelope_demodulation.tex`

Old:
```latex
Primes denote drive derivatives. Below the inflection at
```
New:
```latex
Primes on $F$ denote drive derivatives. Below the inflection at
```

## 13 (material, §dynamic)
File: `TN0484_envelope_demodulation.tex`

Old:
```latex
The condition $\omega_c\tau_{\rm rel}\ll1$ is sufficient for carrier tracking. A population can follow synaptic input quasistatically
while responding dynamically to kHz stimulation.
```
New:
```latex
Carrier tracking additionally requires $\omega_c\tau_{\rm rel}\ll1$. A population can follow synaptic input quasistatically
yet respond dynamically to kHz stimulation.
```

## 15 (§dynamic)
File: `TN0484_envelope_demodulation.tex`

Old:
```latex
At fast carriers, voltage squaring generates a slow drive before the rate responds.
```
New:
```latex
Outside the adiabatic limit, voltage squaring mixes the carriers into a slow drive before the rate responds.
```

## 17 (§dynamic)
File: `TN0484_envelope_demodulation.tex`

Old:
```latex
After mixing, the population filters the generated beat at its own frequency. The crossover
```
New:
```latex
After mixing, the population filters the generated beat at its own frequency;
the carrier attenuation does not apply to it. The crossover
```

## 18 (material, §dynamic)
File: `TN0484_envelope_demodulation.tex`

Old:
```latex
In membrane-time units the coefficient of $v^2$ is one. It plays the role of
$\Sig''/2$, with $G$ converting the drive into a rate beat. Other smooth mechanisms
share the product law but can differ in coefficient, phase, and carrier dependence.
```
New:
```latex
In membrane-time units the coefficient of $v^2$ is one; in this cellular realization
of quadratic detection it plays the role of $\Sig''/2$, and $G$ includes the voltage
and rate dynamics that convert the drive into a rate beat. Other smooth cellular
mechanisms share the weak-input product law without sharing its coefficient, phase,
or carrier dependence.
```

## 20 (FEM Methods, 1:1 and 1:3)
File: `TN0484_envelope_demodulation.tex`

Old:
```latex
currents, which sum to $4$~mA. At each node we fix the projection
direction $\mathbf n^*$ that maximizes the envelope at $2+2$~mA, then vary
```
New:
```latex
currents, which sum to $4$~mA ($2+2$~mA for 1:1 and $1+3$~mA for 1:3). At each
node we fix the projection direction $\mathbf n^*$ that maximizes the envelope at 1:1, then vary
```

## 21 (FEM Methods, lambda_0)
File: `TN0484_envelope_demodulation.tex`

Old:
```latex
The assumed uniform coupling $\lambda_0=0.5$~mV per V/m \cite{radman2009}
cancels from normalized maps, focus locations, and contrast ratios.
```
New:
```latex
The assumed uniform coupling $\lambda_0=0.5$~mV per V/m \cite{radman2009},
not a measured AIS transfer, sets absolute amplitudes but cancels from normalized
maps, focus locations, and contrast ratios.
```

## 23 (FEM Methods)
File: `TN0484_envelope_demodulation.tex`

Old:
```latex
Square roots of second-order maps give degree-matched
contrasts.
```
New:
```latex
Square roots of second-order maps give degree-matched
geometric contrasts; the raw maps remain the detector predictions before gain.
```

## 24 (FEM Methods)
File: `TN0484_envelope_demodulation.tex`

Old:
```latex
The focus is the centroid of the highest-ranked 10\% of hippocampal
nodes, with displacement positive anteriorly.
```
New:
```latex
The focus is the centroid of the top 10\% of hippocampal nodes ranked by
each map, with displacement measured along the hippocampal long axis, anterior positive.
```

## 25 (material, FEM Methods)
File: `TN0484_envelope_demodulation.tex`

Old:
```latex
The mean-square map is proportional
to the signed steady source when curvature is spatially uniform.
```
New:
```latex
These geometric maps precede detection and recurrence. The steady source
$Y_{\rm DC}=\Sig''(v^*)\mathcal I/2$ is a signed rescaling of the mean-square map
only when curvature is spatially uniform.
```

## 26 (JR Methods, RK4)
File: `TN0484_envelope_demodulation.tex`

Old:
```latex
Fixed-step fourth-order Runge--Kutta
integration gives
```
New:
```latex
Fixed-step fourth-order Runge--Kutta (RK4)
integration gives
```

## 28 (material, JR controls)
File: `TN0484_envelope_demodulation.tex`

Old:
```latex
Signed open-loop lock-in tests the curvature law. Closed-loop sweeps over
$(\Omega,p)$ measure gain. Controls check quadratic amplitude scaling on a
well-damped focus, replace the pyramidal sigmoid by its tangent, and compare
derivatives with finite differences. Field-free trajectories check the continuation.
```
New:
```latex
The open-loop sigmoid at fixed $v^*$ isolates detection, and its signed lock-in
tests the curvature law. Closed-loop sweeps over $(\Omega,p)$ measure recurrent gain.
Controls test quadratic amplitude scaling on a well-damped focus, abolition of the
beat when the pyramidal sigmoid is replaced by its tangent, and agreement of
$\Sig'$ and $\Sig''$ with finite differences. Field-free trajectories started near
the fixed point check the continuation.
```

## 31a (QIF Methods, citations)
File: `TN0484_envelope_demodulation.tex`

Old:
```latex
Eq.~\eqref{eq:nmm2-ping}, with $N=8000$ neurons per population
\cite{montbrio2015,ruffini2025rosetta,clusella2023}. Excitabilities are
```
New:
```latex
Eq.~\eqref{eq:nmm2-ping} \cite{montbrio2015,ruffini2025rosetta,clusella2023},
with $N=8000$ neurons per population. Excitabilities are
```

## 31b (QIF Methods, V_j)
File: `TN0484_envelope_demodulation.tex`

Old:
```latex
A neuron spikes at $V_{\rm peak}=100$
and resets to $-V_{\rm peak}$.
```
New:
```latex
Each single-neuron voltage $V_j$ spikes at $V_{\rm peak}=100$
and resets to $-V_{\rm peak}$ (model units).
```

## 34 (QIF Methods, PPC citation)
File: `TN0484_envelope_demodulation.tex`

Old:
```latex
Pairwise phase consistency (PPC) at $\Delta f$, unbiased in spike count,
is measured for neurons with at least ten spikes per window \cite{vinck2010}.
```
New:
```latex
Single-neuron locking at $\Delta f$ is measured by pairwise phase consistency
(PPC), unbiased in spike count \cite{vinck2010}, for neurons with at least ten
spikes per window.
```

## 35 (material, QIF 5% tolerance)
File: `TN0484_envelope_demodulation.tex`

Old:
```latex
Step, population, window, and spike-cutoff checks include a cutoff-free
theta-neuron comparison with a predeclared $5\%$ rate-depth tolerance
(\S\ref{supp:qif-protocol}, \S\ref{supp:theta-pilot}).
```
New:
```latex
Step, population, window, and spike-cutoff checks test the finite-cutoff network
(\S\ref{supp:qif-protocol}). A cutoff-free theta-neuron version tests step,
population, and window sensitivity against a predeclared $5\%$ rate-depth
tolerance (\S\ref{supp:theta-pilot}).
```

## 39 (Discussion, Missey)
File: `TN0484_envelope_demodulation.tex`

Old:
```latex
Missey et al.\ reported biomarker suppression across centers using two carrier pairs:
1300 and 1430~Hz at one center, and 9000 and 9130~Hz at the others \cite{missey2026}.
```
New:
```latex
Missey et al.\ reported biomarker suppression with both low- and high-kHz carriers,
1300 and 1430~Hz at one center and 9000 and 9130~Hz at the others, per their
Methods \cite{missey2026}.
```

## 40 (Predictions lead)
File: `TN0484_envelope_demodulation.tex`

Old:
```latex
Timing and synaptic-blockade experiments require independent measures of
```
New:
```latex
Interpreting timing and synaptic-blockade data requires independent measures of
```

## 41 (Table 4)
File: `TN0484_envelope_demodulation.tex`

Old:
```latex
Measure the excursion and harmonics off resonance or correct for network gain.
```
New:
```latex
Measure amplitude scaling and harmonics off resonance or correct for network gain.
```

## 42 (Conclusions)
File: `TN0484_envelope_demodulation.tex`

Old:
```latex
Near a Hopf bifurcation, TI and matched direct tACS share a gain inversely
proportional to modal damping.
```
New:
```latex
Near a Hopf bifurcation, TI and matched direct tACS share a resonant gain that
grows inversely with modal damping.
```

## 45 (material, abstract Significance)
File: `planning/tn0484_abstract.tex`

Old:
```latex
\newcommand{\absSignificance}{For quadratic detection, weak-field beat amplitude follows the carrier-polarization product.
```
New:
```latex
\newcommand{\absSignificance}{Weak-field beat dose follows the polarization product rather than the envelope minimum.
```

## 46a (notation, units)
File: `planning/tn0484_notation.tex`

Old:
```latex
JR and LaNMM use mV and Hz.
```
New:
```latex
JR and LaNMM voltages are in mV and rates in s$^{-1}$.
```

## 46b (notation, unit rule)
File: `planning/tn0484_notation.tex`

Old:
```latex
The uncoupled MPR derivation uses membrane-time units (Appendix~\ref{app:mpr-coefficients}).
```
New:
```latex
The uncoupled MPR derivation uses membrane-time units (Appendix~\ref{app:mpr-coefficients}).
All frequencies and time constants in a formula must use the same time unit.
```

## 46c (notation, r_X units)
File: `planning/tn0484_notation.tex`

Old:
```latex
& Hz or ms$^{-1}$; mV in JR/LaNMM
```
New:
```latex
& s$^{-1}$ or ms$^{-1}$; mV in JR/LaNMM
```

## 50 (harmonic_details)
File: `planning/parts/harmonic_details.tex`

Old:
```latex
For equal carrier amplitudes, $\mathcal A(t)
```
New:
```latex
For equal polarization amplitudes, $\varepsilon_1=\varepsilon_2=\varepsilon$, $\mathcal A(t)
```

## Verification
- TeXShop: no document had unsaved edits before writing.
- Scratch build of a copy (repair_build): `build.sh jne` gives 44 pages, 0 errors, 0 undefined. `build.sh supp` gives 41 pages, 0 errors, 0 undefined.
- One overfull hbox (45 pt), main file lines 605–611 ("The network gain G modifies the detector ratio ..."). These repairs did not touch that paragraph.
- `code/count_jne_words.py` on the working tree: article 11,861 (was 11,715), abstract 298 (was 296), 12,159 with the abstract.

## Not applied, for the author
- Data availability: the new Zenodo version DOI and the 482d3d1 snapshot replace the old record. The CC BY-SA 4.0/IXI attribution commitment and the hash records were removed.
- Acknowledgments: a new ethics sentence; the text no longer names "the IXI dataset".
- Methods: a new AI-use sentence duplicates the declaration; "Model-specific" is ambiguous.
- de Palma Aristides et al.: "modeled ... in an unpublished study". Confirm that WP0242 is a modeling study.
- salvador2025 is now attached to "six-tissue IXI002 head model". Ricardo should confirm what it supports.
