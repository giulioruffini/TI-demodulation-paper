# Notation audit: appendices, supplement, notation table, figure labels

Klaus, October 6, 2026, read-only on `a097c95` (manuscript as `c620335`). Line numbers refer to
`TN0484_envelope_demodulation.tex` at that commit. Recommendations only; Kaiti integrates.

## A. Glyph collisions, with recommended names

| # | Glyph | Meanings now (line) | Recommendation |
|---|---|---|---|
| 1 | $C(Q,\omega)$, $K(\omega)$ | MPR mixing coefficients (568, 608) vs JR/NMM2 connectivity $C$, elliptic $\mathsf K$, synaptic operators $\hat K_a,\hat K_g$ | $\chi_I(Q,\omega)$ (fixed current) and $\chi_V(\omega)$ (fixed voltage): both are MPR instances of the $\chi^{(2)}$ of 485, which makes the link explicit |
| 2 | $a$ | JR excitatory synaptic rate; weak added current amplitude in §dynamic (563, 592, "voltage excursion $a/\omega$") | rename the current amplitude $I_0$ (it is an amplitude of the input $I(t)$ of Eq. mpr). **Figure:** `mpr_crossover_fig.py` y label "DC rate shift / $a^2$" must change to $I_0^2$ |
| 3 | $I,Q$ (lock-in) | in-phase/quadrature (lockin eq) vs MPR input $I(t)$, field current $I_E$, MPR total drive $Q$, population $I$, quality factor $\mathcal Q$ | rename lock-in components $L_{\rm c},L_{\rm s}$ (cosine, sine); no figure uses $I,Q$ |
| 4 | $\eta_{\rm det}$ | TI/tACS drive ratio (App. bound) vs neuron excitability $\eta$, $\bar\eta$, Hopf drive $\bar\eta_H$ | $\mathcal R_{\rm det}$, paired with the response ratio $\mathcal R_{\rm lin}$ of §tACS |
| 5 | $x$, $q(t)$ | App. bound reduced operating point $x=\rho(v^*-v_0)$ and normalized waveform $q(t)$ (2203-2207) vs position $\mathbf x$ (786) and single-neuron drive $q=\eta+I$ (Eq. Fmpr) | $\xi=\rho(v^*-v_0)$; waveform $\hat s(t)$ (normalized $s$) |
| 6 | $k$ | compartment index ($\lambda^k$, $H_k$) vs elliptic parameter $k^2=1-\beta^2$ (App. bound) | elliptic parameter $\kappa^2$ |
| 7 | $\varepsilon$ in App. SL | dimensionless Stuart-Landau forcing ($\varepsilon=0.5$) vs field polarization in mV | $F_0$ (the forcing $\mathcal F=F_0 f(t)$) |
| 8 | $P$ | dipole conductance in $I_E(t)=P\,E(t)$ (table row $A_f$) vs populations $P_1,P_2$; $P$ undefined | $\lambda_I$ (field-to-current coupling, the current analogue of $\lambda$) |
| 9 | $S(f_c)$ | LaNMM off-alpha lock-in statistic (2308) vs sigmoid $\Sig$ ($=\sigma$) and $s$ family | $\bar A_{\rm off}(f_c)$ (it is a mean lock-in amplitude) |
| 10 | $A_{ee},\dots,A_{ii}$ | NMM2 synaptic weights vs JR PSP gain $A$, envelope $A(t)$, lock-in $A_\Omega$, $A_f$ | $w_{ee},\dots,w_{ii}$. Keep $A_f$: QIF figures and captions use it |
| 11 | $\mathsf J$ | MPR Jacobian in §dynamic vs coupling $J\,(\equiv C)$, $J^*$ | $\mathsf M$ or $\mathsf{Jac}$; at minimum add to the table |
| 12 | $\tau$ vs $\tau_m$ | table: $\tau$ "effective access time", $\tau_m$ "effective membrane time constant"; `mpr_crossover_fig.py` uses $\tau$ for the membrane time ($\omega_c\tau$, "$\tau=1$ units") | one symbol if they are the same quantity ($\tau_m$), and relabel the crossover figure $\omega_c\tau_m$; otherwise state the difference in the table |

Lower priority, acceptable with subscripts: $s(t)$, $s_{\rm syn}$, $s_E,s_I$; $D$ (beat-source
coefficient) vs $d$ (relaxation rate) vs $\Delta$; $E(t)$ vs population label $E$ vs $\mathsf E$.

## B. Units and dimensions in the table

- $\gamma$, $\mu_\pm$: listed in s$^{-1}$; the NMM2 sections and Fig. nmm2_jcurve use ms$^{-1}$.
  Units column: "s$^{-1}$ (JR); ms$^{-1}$ (NMM2)".
- $C(Q,\omega)$ / $K(\omega)$ (or $\chi_I,\chi_V$), $F$, $F'$, $F''$, $d$, $\nu$: "--" is right only in
  the rescaled MPR units of Eq. mpr, with $\omega$ in units of $1/\tau_m$. Say so in the row.
  Restoring physical units, the DC rate shift is $I_0^2\chi_I/\tau_m$.
- $\chi^{(2)}$: "model-dependent" can be made concrete: s$^{-1}$ mV$^{-2}$ when the inputs are
  polarizations (JR, same as $\Sig''$); rescaled rate per current$^2$ for MPR. The definition at 485
  writes $\chi^{(2)}\varepsilon_1\varepsilon_2$ with polarizations, while the MPR calculation drives
  with currents; one sentence linking them ($\varepsilon\leftrightarrow I_0$ through the membrane
  response $H_v$, which is what $\chi_V$ does) removes the ambiguity.
- $V_j$, $V_{\rm peak}$: listed in mV; the QIF network is in rescaled MPR units like $v_E$ ($V_{\rm peak}=100$
  with no unit in the text). Units: "-- (rescaled)".
- $r_E$, $r_I$: table says s$^{-1}$; the MPR equations are in membrane-time units and the figures
  convert ($\times10^3$ to Hz). State "rescaled; reported in Hz" in the row.
- $Y_\Omega$, $Y_{\rm LF}$, $\mathcal M[\cdot]$: "--" is wrong; they carry the units of the detector
  output and of their argument.
- App. SL: $\alpha=-0.5$ has no unit; with $f_0=10$ Hz it is in s$^{-1}$.

## C. Symbols used but absent from the table

$\varphi_X$ (LaNMM rate, Eq. lanmm_drive), $S(f_c)$, $f_{\rm out}$, $\delta\eta_E$, $s_{\rm DC}$ and
$q_j$, $\mathbf b$ (DC source), $r^*$, $\mathcal R_{\rm lin}$, $\varepsilon_{\rm TI}$,
$\varepsilon_{\rm tACS}$, $\gamma_{\rm crit}$, $c_1,c_2,c_4$ and $T(A)$, $r_{\rm meas}$, $r_{\rm det}$,
$\zeta$, $\beta$, $u$, $L(z)$, $\mathcal F$, $\alpha$, $z$, $\bar\eta_H$, $\mathcal I$ (DC intensity map),
$\hat L$, $u_{X\leftarrow Y}$, $C_{X\leftarrow Y}$, $\theta$, $\omega_z$, $H_v$, $\mathbf h$, $\mathbf b_2$,
$\mathsf J$, $\mathbf x$, $\boldsymbol\lambda$, $\mathbf n$, $\phi_j$, $R_\Omega(\mathbf x)$,
$G_{\mathbf x}(\Omega)$. Not all need rows; the ones used in more than one section do
($r^*$, $\mathcal R_{\rm lin}$, $\delta\eta_E$, $c_1,c_2$, $r_{\rm det}$, $\mathbf x$, $\boldsymbol\lambda$, $\gamma_{\rm crit}$).

## D. Figure labels

Only two figure scripts need relabeling, and only if the renames above are adopted:
`mpr_crossover_fig.py` (rename 2: $a^2\to I_0^2$; rename 12: $\omega_c\tau\to\omega_c\tau_m$, "$\tau=1$" to
"$\tau_m=1$"; its in-plot labels use $Q^*$ where the text uses $Q$). No figure uses $C(Q,\omega)$,
$K(\omega)$, $I,Q$, $\eta_{\rm det}$, $S(f_c)$, or $A_{ee}$. Sigmoid labels use $\sigma''$, consistent
with `\Sig` $=\sigma$. Fig. nmm2_jcurve labels $J\,(=C)$ and $\gamma$ in ms, consistent with the NMM2 text.
