# TN0484 JNE article: symbol audit (front-to-back reader)

Scope: the jne branch of `src/TN0484_envelope_demodulation.tex` (lines 170–1890), the active `\input` files (`planning/tn0484_abstract.tex`, `figures_src/fig_models_ti_caption.tex`) and Appendix B (`planning/parts/article_models.tex`, `peix_definition.tex`, `slow_synapse.tex`). The notation table (Appendix A) is not counted as a definition. PDF order was checked against `article.txt`. Page numbers are PDF pages.

The `\mathcal I` fixes are present in the snapshot: line 490 (Sec 2.3, "The nonnegative mean-square map $\mathcal I=\dots$") and lines 625 and 666 (Sec 2.5). They are not reported again.

Categories: A = used before defined; B = needs a reminder after a long gap; C = one symbol with two meanings. "+n" counts the plain words a fix adds; math symbols and references are not counted.

| # | Symbol | Cat. | Problematic use | Defined | Proposed fix (exact LaTeX) | +n |
|---|---|---|---|---|---|---|
| 1 | $\lambda_0$, $H(\omega)$ | A | `fig_models_ti_caption.tex` l.5 (Fig. 2, p6, printed before Sec 2.2) | main l.405–412 (Sec 2.2) | `access $\lambda_0H(\omega)$ converts` → `access, coupling $\lambda_0$ times filter $H(\omega)$, converts` | 3 |
| 2 | $\lambda_I$, $E$ | A | caption l.7 | $E$: main l.392 (Sec 2.2); $\lambda_I$: l.930–933 (Sec 2.9), l.1150 | `current $I_E=\lambda_I E$ enters` → `current $I_E=\lambda_I E$ (field $E$, coupling $\lambda_I$) enters` | 2 |
| 3 | $v_E$ | A | caption l.8 | main l.1128 (Sec 3.5) | `$v_E^2$ mixes its voltage excursions` → `$v_E^2$, the squared mean voltage, mixes its excursions` | 3 |
| 4 | $\gamma$ | A | caption l.14 | main l.767–768 (Sec 2.7) | `proportional to $1/\gamma$ near` → `proportional to inverse modal damping $1/\gamma$ near` | 3 |
| 5 | $\boldsymbol\lambda$, $\mathbf E_j$ (vector field of tone $j$) | A | main l.561–562 (Sec 2.3, p8) | l.664–666 (Sec 2.5: $\mathbf E_j=-\nabla\phi_j$, "spatially fixed coupling $\boldsymbol\lambda$") | `$\varepsilon_j=\boldsymbol\lambda\cdot\mathbf E_j$; the beat` → `$\varepsilon_j=\boldsymbol\lambda\cdot\mathbf E_j$ with tone fields $\mathbf E_j$; the beat` | 3 |
| 6 | $G$ | A | main l.605 (Sec 2.4, p8) | l.771 (Sec 2.7, "complex susceptibility $G$") | `The network modifies` → `The network gain $G$ modifies` | 1 |
| 7 | $\mathcal H_{\rm meas}$, $\mathcal H_{\rm det}$ | A | main l.604–605 | nowhere in the article (only supplement Eq. `eq:rdet` and Appendix A) | `modifies these ratios through $\mathcal H_{\rm meas}=` → `modifies the detector ratio $\mathcal H_{\rm det}$, giving the measured $\mathcal H_{\rm meas}=` (combine with #6) | 3 |
| 8 | $\mathcal H$ | C | l.212 Hilbert transform; l.605 harmonic ratio ($\mathcal H_{\rm det}$, $\mathcal H_{\rm meas}$) | l.212 | at l.211–212: `$|x+i\mathcal H[x]|$, where $\mathcal H$ is the Hilbert transform` → `$|x+i\hat x|$, where $\hat x$ is its Hilbert transform` | 0 |
| 9 | $A$, $a$ | B | main l.758 (Sec 2.7, p11): $H_s(\omega)=Aa/(i\omega+a)^2$ | l.366–370 (Sec 2.1, p5); no use in between | `$H_s(\omega)=Aa/(i\omega+a)^2$, a second-order` → `$H_s(\omega)=Aa/(i\omega+a)^2$ with PSP gain $A$, a second-order` ($a$ is recalled by "characteristic frequency $a/(2\pi)$") | 3 |
| 10 | $\tau_s$ | A | main l.874 (Table 2, p12–13) | l.918 (Sec 2.9), App. B.2 | `$\tau_s=10$~ms` → `$\tau_s=1/a=10$~ms` | 0 |
| 11 | $\mathbf n$ | C | main l.1053 and l.1056 (Sec 3.3, p16): fixed geometric projection direction, "need not match a cell's orientation" | l.629 (Sec 2.5): common unit cell orientation | write `$\mathbf n^*$` at l.1053 and l.1056, as the Appendix A preface already does | 0 |
| 12 | $C$ | B | main l.1115–1116 (Sec 3.4, p16); again l.1422–1424 | l.386 (Sec 2.1, p5); no use in between | `as $C$ varies` → `as connectivity $C$ varies` | 1 |
| 13 | $r_P$ | A | main l.1119 (Sec 3.4); reused l.1446 | only by the formula $r_P=\Sig(v+s)$; subscript P is never explained | `and mean of $r_P=\Sig(v+s)$` → `and mean of the pyramidal rate $r_P=\Sig(v+s)$` | 3 |
| 14 | $v_0$ | B | main l.1335 (Fig. 8 caption, p21) | l.377 (Sec 2.1); last used l.728 (p10) | `reversing sign\nat $v_0$` → `reversing sign\nat the inflection $v_0$` | 2 |
| 15 | $\mathcal I$ | B | main l.1400 (Fig. 9 caption, p23) | l.490, l.625 (p7–9); last used l.666 | `gain: $\mathcal I$ weights` → `gain: the mean square $\mathcal I$ weights` | 3 |
| 16 | $F(Q)$ | B | main l.1500–1501 (Fig. 12 caption, p25) | l.909 (Sec 2.9, p13–14) | `inflection of $F(Q)$` → `inflection of the rate curve $F(Q)$` | 3 |
| 17 | $I_{\rm ac}$ | B | main l.1502 (Fig. 12 caption) | l.957 (Sec 2.9, p14) | `at $I_{\rm ac}=0.05$` → `at carrier amplitude $I_{\rm ac}=0.05$` | 2 |
| 18 | $I_j$ | B | main l.1520–1521 (Sec 4.6, p25–26) | l.970 (Sec 2.9, p14); Methods (l.1152) calls the same tone amplitude $A_f$ | `Each current tone\nproduces` → `Each current tone of amplitude $I_j$\nproduces` | 2 |
| 19 | $v^*$ (also $r^*$) | C | `article_models.tex` l.82–85 (App. B.3, p43): $v^*=-d/2$, a dimensionless MPR equilibrium | main l.422: JR field-free voltage, $v^*=8.30$~mV throughout; the main text marks MPR equilibria with a subscript star ($u_*$, $r_*$, $Q_*$, l.936–947) | in `article_models.tex` replace `r^*` → `r_*` (l.69, 73, 74, 82, 85) and `v^*` → `v_*` (l.82, 83, 85) | 0 |

Totals: A = 9 (#1–7, 10, 13), B = 7 (#9, 12, 14–18), C = 3 (#8, 11, 19); 19 findings in all, adding 37 words.

## Words added if all fixes are applied

| # | Words added (net) |
|---|---|
| 1 | coupling, times, filter (3) |
| 2 | field, coupling (2) |
| 3 | the, squared, mean (3; "voltage" moves, it is not added) |
| 4 | inverse, modal, damping (3) |
| 5 | with, tone, fields (3) |
| 6 | gain (1) |
| 7 | the, detector, ratio, giving, the, measured; removes these, ratios, through (net 3) |
| 8 | none ("the" becomes "its") |
| 9 | with, PSP, gain (3) |
| 10 | none |
| 11 | none |
| 12 | connectivity (1) |
| 13 | the, pyramidal, rate (3) |
| 14 | the, inflection (2) |
| 15 | the, mean, square (3) |
| 16 | the, rate, curve (3) |
| 17 | carrier, amplitude (2) |
| 18 | of, amplitude (2) |
| 19 | none |
| **Total** | **37** |

## Checked and not reported

- **Glossed at the point of use:** $h_e,h_i$ and $\tau_a,\tau_g$ in Fig. 2 ("second-order synapses … with times"). $f_0$ in Fig. 1 ("natural frequency"). $C^*$ at l.1424 ("As $C\to C^*$, damping tends to zero"). $Q_*$ at l.938 (follows $u_*=r_*$ at l.936 and is named at l.947). $\delta$, $\mathbf n$, $\varepsilon$, $\omega_j$, $\varepsilon_{1,2}$ (defined in the sentence that follows). $\mathcal R_{\rm det}$, $\mathcal R_{\rm lin}$, $\tau_{\rm rev}$, $\delta\eta_E^*$ (defined in place).
- **Two meanings, but documented where they occur:**
  - $u$ (excluded by instruction).
  - $v$: JR mean input in mV versus MPR dimensionless voltage, stated at l.893.
  - Overbar: beat-period mean (l.487), complex conjugate (l.568, App. B.3, glossed each time), lock-in mean $\bar v$ (l.1021) and $\bar\eta$ (named).
  - $f(q)$ single-cell rate versus frequency $f$ (App. B.3, glossed).
  - $\mathsf J$ Jacobian versus coupling $J$ (glossed).
  - $\omega$ in membrane-time units in App. B.3 (stated).
  - $x$: signal (l.211), position $\mathbf x$ (bold), $x=\log(\pi r)$ (App. B.3).
  - $\varphi$ (carrier phase) versus $\phi_j$ (potentials): distinct glyphs.
  - $a,b,B$ (JR) versus $a_j^k,b_j^k,B_{kl}$ (Sec 2.3, defined in place, distinguished by indices). If renaming is wanted, $\alpha_j^k,\beta_j^k$ collide with supplementary symbols.
- **One quantity under two symbols (outside A/B/C, for information):**
  - tACS amplitude: $\varepsilon_{\rm A}$ (l.708) and $\varepsilon_{\rm tACS}$ (l.1467).
  - PING tone amplitude: $I_j$ (l.970, 1521) and $A_f$ (l.1152). Fix #18 reduces the confusion.
  - Access time: $\tau$ (l.1284) and $\tau_m$ (l.1294).
  - Equilibrium star: $r^*$ (App. B.3) and $r_*$ (l.936). Fix #19 removes this pair.
- **Labels inside the Fig. 2 artwork (not counted as captions):** $y_0$, $C_1$–$C_4$, $J$, $Jw_{XY}$, $J^*$, $\mathcal U_j$, $\eta_j$, $V_j$, $\tau_X$ and $A_f$ appear on p6. They are defined only in Sec 3.5 (l.1144–1146, "In the schematic, …") or in Appendix B. If the artwork counts as a use, the caption could add "Symbols in (b) are defined in §3.5" (7 words).
