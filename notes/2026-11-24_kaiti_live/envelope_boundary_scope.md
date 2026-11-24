# Analytic envelope and spatial maximum principle

Checked 2026-11-24 against the proposal worktree's Introduction, Sections 2.3 and 2.5, and `planning/parts/envelope_proof.tex`. This is a mathematical scope review; no manuscript changes or simulations were made.

The proposed Hilbert-envelope definition is exact for the stated two tones. The field-strength restriction is valid within the manuscript's quasistatic, homogeneous, isotropic, source-free model. The distinction must concern envelope excursion and beat amplitude, because the instantaneous analytic envelope and its beat-period mean also satisfy a maximum principle under spatially fixed linear coupling.

## The two-tone identity includes signed amplitudes

Let

\[
s(t)=\varepsilon_1\cos(\omega_1t)+\varepsilon_2\cos(\omega_2t),
\qquad 0<\omega_1<\omega_2,
\]

where the real amplitudes \(\varepsilon_j\) may have either sign. With the Hilbert-transform convention \(\mathcal H[\cos(\omega t)]=\sin(\omega t)\) for positive \(\omega\), the analytic signal is exactly

\[
s+i\mathcal H[s]
=\varepsilon_1e^{i\omega_1t}+\varepsilon_2e^{i\omega_2t}.
\]

Its modulus is

\[
\mathcal A(t)=|s+i\mathcal H[s]|
=\sqrt{\varepsilon_1^2+\varepsilon_2^2
+2\varepsilon_1\varepsilon_2\cos(\Omega t)},
\qquad\Omega=\omega_2-\omega_1.
\]

No narrowband approximation is needed for this identity for ideal stationary tones. Reversing one amplitude shifts the beat phase by \(\pi\); it does not change the extrema, excursion, or beat-period mean. In particular,

\[
\max_t\mathcal A=|\varepsilon_1|+|\varepsilon_2|,
\qquad
\min_t\mathcal A=\big||\varepsilon_1|-|\varepsilon_2|\big|,
\]

and the envelope excursion is \(2\min(|\varepsilon_1|,|\varepsilon_2|)\). The beat-period mean of \(\mathcal A^2/2\) is \((\varepsilon_1^2+\varepsilon_2^2)/2\), its signed cosine amplitude is \(\varepsilon_1\varepsilon_2\), and its excursion is \(2|\varepsilon_1\varepsilon_2|\). For initial phases \(\alpha_j\), replace \(\Omega t\) by \(\Omega t+\alpha_2-\alpha_1\).

The manuscript's \(\mathrm{LPF}[s^2]=\mathcal A^2/2\) additionally assumes that the low-pass operation retains DC and \(\Omega\) while rejecting \(2\omega_1\), \(2\omega_2\), and \(\omega_1+\omega_2\). The nearby TI carriers allow that separation. An arbitrary physical low-pass filter may also attenuate or phase-shift the beat.

## The boundary statement belongs to a homogeneous region

In the electroquasistatic model, a spatially constant scalar conductivity and absence of internal current sources give \(\nabla^2\phi_j=0\). Thus each component of \(\mathbf E_j=-\nabla\phi_j\) is harmonic. For a harmonic vector field,

\[
\nabla^2|\mathbf E_j|^2
=2\sum_k|\nabla E_{j,k}|^2\ge0.
\]

The field strength therefore has no strict three-dimensional interior maximum. On a bounded homogeneous region with continuous boundary values, its supremum is attained on the region's boundary. A constant field also attains that value throughout the interior. An unqualified statement that all maxima lie on conductivity boundaries would exclude this constant case and would identify the boundary too narrowly. The relevant boundary can be an internal tissue interface, an electrode/source boundary, or the external boundary; an internal interface can itself lie deep in the head. The result is not a theorem that every maximum is near the scalp. Nor does it rule out a maximum on a two-dimensional slice through a three-dimensional saddle.

Heller and van Hulsteyn derive \(\nabla^2\mathbf E=0\) to their stated quasistatic order and give the maximum restriction on page 130, Section II, immediately after Eq. (2.8). The scanned primary page was inspected. Their result is broader than the present electroquasistatic calculation because their treatment includes magnetic induction. Their conductivity-boundary wording presumes the piecewise homogeneous conductor geometry under discussion. Cite the result with its local homogeneous-region scope rather than importing a blanket anatomical conclusion. Source: [Heller and van Hulsteyn, 1992, Biophysical Journal 63, 129–138](https://pmc.ncbi.nlm.nih.gov/articles/PMC1262130/), DOI [10.1016/S0006-3495(92)81587-4](https://doi.org/10.1016/S0006-3495(92)81587-4); [page 130 scan](https://cdn.ncbi.nlm.nih.gov/pmc/blobs/9b29/1262130/9dc97dd346f0/biophysj00099-0145.png).

## The mean maps retain the restriction

For \(\varepsilon_j(\mathbf x)=\boldsymbol\lambda_j\cdot\mathbf E_j(\mathbf x)\), each \(\varepsilon_j\) remains harmonic when the linear coupling vector \(\boldsymbol\lambda_j\) is spatially constant. The couplings may differ between carrier frequencies. They must not vary with position through access gain, cell orientation, or local optimization. A direction selected separately at each FEM node is not a spatially fixed coupling.

Consequently the manuscript's intensity \(\mathcal I=(\varepsilon_1^2+\varepsilon_2^2)/2\) satisfies

\[
\nabla^2\mathcal I=\sum_j|\nabla\varepsilon_j|^2\ge0.
\]

At each fixed beat phase \(\vartheta\), the analytic envelope is the Euclidean norm of the harmonic vector

\[
(\varepsilon_1+\varepsilon_2\cos\vartheta,
\varepsilon_2\sin\vartheta).
\]

A convex norm of harmonic components is subharmonic, including at zeros in the weak sense. Averaging over \(\vartheta\) preserves subharmonicity. This proves the supplement's envelope-mean claim and also shows why the introductory contrast must not say that the envelope itself escapes the maximum principle. Spatially varying detection, recurrence, and the physiological mean response are outside this statement. A spatially constant nonzero scalar detection coefficient transfers it to the magnitude of the corresponding steady source; a negative coefficient reverses the source's sign.

## Excursion and beat amplitude can have interior maxima

The product obeys

\[
\nabla^2(\varepsilon_1\varepsilon_2)
=2\nabla\varepsilon_1\cdot\nabla\varepsilon_2,
\]

whose sign is unrestricted. Taking a modulation excursion subtracts a temporal minimum from a maximum, which does not preserve subharmonicity. These observations remove the mean-map obstruction; the following local construction also demonstrates a strict three-dimensional maximum for both quantities.

Use dimensionless coordinates \((x,y,z)\), choose \(0<c<1/2\), and let

\[
q=x^2-\tfrac12(y^2+z^2),
\qquad
\varepsilon_1=1+x+cq,
\qquad
\varepsilon_2=1-x+cq.
\]

Both amplitudes are harmonic and positive near the origin. Their product is

\[
\varepsilon_1\varepsilon_2=(1+cq)^2-x^2
=1+(2c-1)x^2-c(y^2+z^2)+O(|\mathbf x|^4),
\]

so its Hessian is negative definite at the origin. Their envelope excursion is \(2(1+cq-|x|)\), also strictly maximized there within a sufficiently small neighborhood. These scalar fields can be realized as fixed \(x\)-components of gradient fields: the harmonic potentials

\[
\phi_{1,2}=-x\mp\tfrac12(x^2-y^2)
-c\left[\tfrac13x^3-\tfrac12x(y^2+z^2)\right]
\]

satisfy \(-\partial_x\phi_j=\varepsilon_j\). This is an analytic existence example, not a prediction for a particular montage.

## Proposed introductory paragraph

Place after the definition of the local polarization in Eq. (1), with the citation key added for Heller and van Hulsteyn:

> The analytic envelope of the local polarization is \(\mathcal A(t)=|s(t)+i\mathcal H[s](t)|\), where \(\mathcal H\) is the Hilbert transform. Under the quasistatic approximation, electric-field strength has no strict three-dimensional interior maximum in homogeneous, isotropic, source-free tissue (Heller and van Hulsteyn, 1992). With spatially fixed linear coupling to polarization, the mean-square polarization and the beat-period mean of its envelope obey the same restriction. The envelope excursion and quadratic beat amplitude can nevertheless have interior maxima, so localization depends on which feature of the waveform drives the neural response.

This paragraph names the analytic envelope, states the restricted field result, and identifies the nonlinear features that can support an interior maximum. The exact two-tone square-root formula can remain in the Theory section.
