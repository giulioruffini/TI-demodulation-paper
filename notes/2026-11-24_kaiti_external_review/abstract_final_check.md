# Final abstract and finite-cutoff check

The live abstract preserves the protected meaning of the baseline. The QIF qualification and the sentence about linear resonance implement the approved changes. No material or minor fidelity finding remains.

| Passage | Disposition |
|---|---|
| Objective | Unchanged. The ordered stages remain membrane access, nonlinear detection of envelope features, and circuit amplification. |
| Mesoscale framing and model ladder | Preserved. “Our mesoscale model assigns access an effective membrane time” remains explicit, followed by the JR column, exact QIF mean field, and spiking network. |
| Spatial maps and input budgets | Faithful compression. The single-head-model restriction and the frequency-dependent budgets' assumed field coupling and membrane times remain. The later centroid comparison supplies the comparison previously stated in the Approach. No calibrated budget is implied. |
| Weak-field quadratic sources | Faithful compression. Replacing “a static quadratic detector” with “static quadratic detection” keeps the regime and mechanism. The beat remains proportional to the carrier-polarization product; the steady source remains signed, DC-like, and proportional to the summed squares. |
| Pinned JR source budget | Preserved. The state restriction, 0.1–0.3 mV per carrier, approximate 2–5% result, leading-order linear comparator, both tACS/tDCS, and equal per-carrier/direct-input polarization convention all remain. |
| QIF crossover | Approved clarification. The quantity is now the steady rate shift at fixed synaptic input. Increasing carrier frequency takes it from curvature-controlled to positive-slope-controlled rectification. The sentence no longer reads as a claim about every QIF response component. |
| Head-model centroids and fixed-state beat map | Preserved. Envelope and mean-square centroids move oppositely in the hippocampus, while current-ratio changes only rescale the beat map at fixed state. “Fixed-state” retains the original restriction rather than asserting unrestricted absence of steering. |
| Hopf gain and pinned JR modulation | Faithful compression. Inverse modal-damping gain, shared amplification with tACS, independent variation of gain and detection, predominant population-rate modulation, and little mean-rate change all remain. “Chiefly amplifying” expresses the original statement that amplification appears mainly in that component. |
| Strong-input QIF claim | Unchanged verbatim. The steady source alone drives the QIF mean field across its gamma threshold, as does the RMS-matched unmodulated carrier. No weaker replacement, broader inference, or different response claim has been substituted. |
| Beat dose and linear-resonance efficiency | The product-versus-envelope-minimum statement is unchanged. The approved additional efficiency sentence explicitly says **linear** resonance and compares matched direct sources; it does not make a claim about every nonlinear response regime. |
| Steady-source sign and spatial boundary | Unchanged. Depth access, detector-state/dynamics dependence of sign, carrier-polarity independence, uniform scalar coupling/detection, homogeneous conductivity, and the absence of a **strict** interior maximum of magnitude all remain. |
| Empirical tests and uncalibrated coupling | Unchanged. Polarization measurements and amplitude/frequency sweeps remain the tests; physiological kHz coupling remains uncalibrated. |

All changed abstract passages were assessed; none remains open. This is a fidelity check, not an independent certification of each unchanged scientific claim or of the word-count convention.

The new finite-cutoff paragraph in `planning/parts/qif_protocol.tex` is correct under its stated conditions. For constant normalized drive \(q>0\), continuous dynamics \(\tau_m\dot V=V^2+q\), symmetric finite bounds, and instantaneous reset, the interspike interval is

\[
T=\tau_m\int_{-V_{\rm peak}}^{V_{\rm peak}}\frac{dV}{V^2+q}
=\frac{2\tau_m}{\sqrt q}\arctan\!\left(\frac{V_{\rm peak}}{\sqrt q}\right).
\]

Its reciprocal is the printed finite-cutoff rate; letting the cutoff tend to infinity gives the printed \(\sqrt q/(\pi\tau_m)\). At any fixed finite positive cutoff the firing rate differs from that limit, independently of population size. The paragraph identifies this as a single-neuron constant-input calculation, so it does not claim an exact rate formula for the driven recurrent network or for its finite-step Euler approximation. No correction is required.
