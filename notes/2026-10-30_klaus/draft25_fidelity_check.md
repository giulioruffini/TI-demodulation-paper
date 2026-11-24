# Draft25 fidelity check: 4ebe719 against 8ecc70a

Klaus, 2026-10-30, for Kaiti's handoff of 16:57. Read the full source diff of
`TN0484_envelope_demodulation.tex` and of every changed or new file under
`planning/parts/`, the disposition record `docs/revision_2026-10-30_draft25_readability.md`,
and the relocated homes. No build, edit, push, or mail. Verdict: science preserved; two
fixes needed before delivery, four smaller suggestions for Kaiti's judgment.

## Fixes

1. **`planning/parts/envelope_proof.tex`, lines 2--8.** The relocated integral now opens
   "For comparison, the envelope mean is ... where $\vartheta$ is beat phase. Here $\vartheta$
   is beat phase." The comparison it referred to stayed in the article, and the definition of
   $\vartheta$ is given twice. Replace the opening with "The envelope mean is" and delete the
   sentence "Here $\vartheta$ is beat phase." The added assumption sentence ("For fixed scalar
   coupling in homogeneous, isotropic, source-free tissue, the envelope mean is subharmonic")
   is correct and should stay.

2. **Conclusion, first and second paragraphs.** Two statements of the paper's own frame were
   lost in the rewrite.
   - The opening sentence now names "The spatial field, nonlinear detector, and recurrent
     amplifier". The Introduction's triad, repeated in the abstract and in every section
     heading of the Discussion, is access, detection, amplification. Suggested: "Access,
     detection, and amplification determine different parts of the TI response."
   - "Near-Hopf gain is shared with direct tACS." no longer states the gain law. The abstract
     says "resonant gain grows inversely with modal damping" and the Results quantify it
     ($1/\gamma$, exponent 1.02). Suggested: "Near a Hopf bifurcation the circuit amplifies the
     beat in inverse proportion to modal damping, a gain shared with matched direct tACS."
   - Optional: "static JR curvature and fast-carrier QIF dynamics can give opposite signs" is
     true but no longer says what sets the crossover. Adding "as the carrier frequency rises
     past the membrane relaxation rate" keeps the protected crossover in the Conclusion.

## Suggestions (Kaiti's call)

3. **Heading of 4.8**, "Dynamic QIF detection drives the gamma resonance", can be read as
   detection inducing gamma, which is the subject of 4.9. "Dynamic QIF detection feeds the
   PING gamma resonance" or "The exact QIF mean field: dynamic detection at a gamma resonance"
   avoids that reading.
4. **Methods 3.6** no longer names the integrator; the JR and NMM2 subsections name RK4 and
   their steps. One clause restores parity: "Euler integration with 0.0025 ms steps; settling,
   whole-cycle windows, and convergence checks are in the supplement
   (\S\ref{supp:qif-protocol})."
5. **Two pointers to 2.10 were dropped** with their sentences rewritten: in 2.2 ("A static
   detector additionally requires relaxation faster than the carrier") and in 2.5 ("dynamic
   rectification and recurrence can change the sign of the mean response"). The qualifiers
   survive, which is what the draft24 restoration asked for; adding "(\S\ref{sec:dynamic})" to
   each costs two words and tells the reader where the condition is derived.
6. **Introduction**: "Figure~\ref{fig:concept} combines cellular mixing with recurrent gain"
   makes the figure the agent; "The framework of Fig.~\ref{fig:concept} combines ..." was the
   draft24 wording.

## Verified

- **Routing.** `xr-hyper` with `\externaldocument` resolves cross-document references; the
  supplement log reports no undefined reference. `eq:peix`, now in Appendix B (article and
  TN), still resolves from the notation table's PEIX row in the supplement. The three new
  modules are inlined in the TN edition under `\ifjne\else` (Methods line 1142, Results lines
  1439 and 1500) and in the supplement under `\ifjne` in `supp_amplification.tex`, so neither
  edition duplicates or loses them. Fifteen main-text references point at the new or extended
  supplement sections, each introduced as "supplement".
- **Numbers in the relocated homes.** `qif_protocol.tex`: 0.0025 ms, 800 ms, 176 ms, 44 and 34
  cycles, 800 and 810 ms, $V_{\rm peak}$ 200 and 400, $\sqrt2A_f$, 3200 ms, 0.011 to
  $9.2\times10^{-5}$, 0.30--0.31. `ping_coupling_results.tex`: $14.6\lesssim J\lesssim16.2$,
  55 and 50 Hz, $0.0014$--$0.0081$ ms$^{-1}$, exponents 1.02 and 0.71, 5.8-fold, 48%, $A_f=2$,
  11%, nine couplings. `tacs_saturation.tex`: 0.143, 6.99, 6.97, 3.95, 1.96; the two-tone
  ratios 0.14, 0.24, 0.46 at $\gamma=1.07$ and 0.12 s$^{-1}$ and the matched-source 0.99,
  0.93, 0.90 are in Table S (waveform checks) as cited. `fem_sensitivities.tex`: the sweep
  paragraph verbatim (1.24 at 0.525, 0.89--0.94, 96%, 1.5 mm, 6.3 mm, 0.79--0.94,
  0.89--0.97). `peix_definition.tex`: definition and the three identities verbatim.
  `harmonic_details.tex`: rectifier values and the biological-implementation sentence.
  `steering_algebra.tex`: the $|\mathcal P_1|>2|\mathcal P_2|$ and $1.5\times$ conditions.
  Main-text numbers retained where the text was rewritten: 0.00670 s$^{-1}$, 0.512 mV, 76.4
  mV s, 0.7, 2.5%, 16 Hz (Fig. 5 caption); $-0.151$ (Fig. 10 caption); 1.110, 54 Hz, 0.0014,
  0.0030, 0.0055, 56, 65, 83 Hz (Fig. 11 caption); 1.1%, 0.1%, 0.03%, four operating points;
  0.12, 0.286, 0.09--0.16, 0.13, 12%, 2.8%, 0.02, 1.6%, 1.2, 1.65, $+0.032$, 0.70, 0.29, 52,
  53--54, 95 and 11 Hz, 3%, 51 Hz, 8--11%, 0.003, 0.29, 0.23, $-0.02$, 0.003--0.005, 0.02,
  0.12--0.13; 1.24 (FEM) with the rest in Table 3.
- **QIF Results flow.** Opening (modulation at the lower amplitude, induced gamma at the
  higher), $A_f=10$ at both backgrounds with the sub-threshold drive shift and the unconverged
  depth, $A_f=35$ with the supra-threshold shift and the reproduced off-beat line, the
  $\bar\eta=1.5$ coexistence and sidebands, raster figure, equal-RMS control, regimes figure,
  modulation versus mean rate and weak individual locking. Each paragraph has one subject
  and the threshold value is stated once before it is reused. The fold explanation now lives
  only in the Fig. 13 caption, as proposed (Giulio's C4).
- **Scope statements retained.** "This control has been tested only in the mean field";
  "its quantitative size remains unconverged"; "finite-amplitude example"; "These
  finite-amplitude results do not establish its size under weak physiological stimulation";
  "the law does not describe every mode or the entire finite-amplitude sweep"; "assumed access
  ... quantifies their consequences"; "their combined transfer remains unmeasured"; "specific
  to the head-model example"; "no strict interior maximum" with its three conditions.
- **Protected items.** Full PING system in Methods, the notation appendix, the 2--5%
  comparison (2.6 unchanged except one dropped pointer), the crossover (2.10 and Fig. 12
  unchanged), and the kHz feasibility passage (4.2 unchanged except the deleted duplicate
  sentence) are intact. Table 2 and the bilinear paragraph stay in the article, as Kaiti
  decided.
- **Draft24 restorations.** The network-effect sentence, "In this weakly driven regime", the
  envelope-following assumption, $\Sig''(v^*)<0$ at the pinned state, the purpose of the
  spiking comparison, and the PEIX motivation are present; the static-detector qualifier is
  present in words (item 5 above concerns only its pointer). The three draft24 corrections
  (cable-curve pointer, assumed-access wording, Brunel citation) are untouched.
- **Captions.** Figs. 5, 10 and 11 shortened with every number retained; Fig. 13 and 14
  captions unchanged.

Nothing else found. Delivery can close once fixes 1 and 2 are in.
