# Referee assessment of draft22 (HEAD 8d7bd08), Klaus, 2026-10-24

Scope, per Kaiti's handoff (20:20): assess the six major requests and the minor
items against the current journal source, say what is already addressed and what
is new, recommend accept / modify / decline, and name the smallest defensible new
computation. No manuscript, build, or artifact was touched. Sources read:
`TN0484_envelope_demodulation.tex` and `planning/parts/*.tex` at 8d7bd08; the
published Missey et al. 2026 PDF (Brain Stimul. 19:102981, open access); PubMed
abstracts of Esmaeilpour 2021, Cassarà 2025 part II, Luff 2024 (PWM-TI); the QIF
run logs in `code/`. Numbers below were recomputed, not copied.

## Summary

| # | Request | Verdict | Already in draft22 | New work | Cost |
|---|---|---|---|---|---|
| 1 | kHz feasibility figure | Accept | Eq. (khz), Table 2, S1 figures, 5.4 budget | analytic two-panel figure; Missey paragraph | hours, no simulation |
| 2 | Novelty vs Cassarà, Esmaeilpour, Luff | Modify | all three credited; Missey cited once | one "relation to prior models" paragraph | none |
| 3a | Abstract sign claim vs MPR slope regime | Accept | 2.10 and Table 4 state the slope regime | qualify one abstract sentence | none |
| 3b | Multicompartment bilinear form | Accept | 2.2 parallel inputs; 2.3 vector coupling | one clause in 2.5 plus four lines in S3 | none |
| 4 | Single head, top-decile centroid, modest contrasts | Modify | one subject stated in 4.4; 32-case sensitivity | abstract "one head model"; one scope sentence | none; decline new subjects |
| 5 | Theta-neuron convergence or qualitative scope | Accept the run | nonconvergence stated in 3.6, 4.9, S4 | theta-neuron run; spiking equal-power control | under one hour |
| 6 | Violante: hypothesis, not validation | Accept | conditional phrasing throughout 5.2 | one labeling sentence; Table 4 row | none |
| m1 | JR "timing" is population-rate modulation | Accept | QIF PPC reported as weak | "beat-locked modulation" in abstract and Conclusion | none |
| m2 | equal-RMS vs equal-power | Accept | both terms used | one term, defined once | none |
| m3 | Portable FEM arrays, tagged snapshot | Accept | hashes in fem_quadmaps.json | Ricardo exports ~20 MB npz; tag at submission | Ricardo, hours |
| m4 | Shorter narrative, Table 4, LaNMM | Modify | LaNMM already supplementary | merge Table 4 to six rows; second de-duplication pass | Kaiti |

## 1. kHz feasibility figure over carrier, access time, coupling, and field

Reviewer's arithmetic, verified with the paper's point-membrane access
$|H_m|^2 = 1/(1+\omega^2\tau^2)$ at $\tau = 0.2$ ms:

| Comparison | Beat-source ratio |
|---|---|
| 9 kHz / 1 kHz, narrowband | 0.0200 |
| (9000, 9130) / (1000, 1130), Missey abstract pairs | 0.0213 |
| (9000, 9130) / (1300, 1430), Missey Emory pair | 0.0301 |
| field factor to restore the 1 kHz beat at 9 kHz, point membrane | 7.1 |
| same, sealed long cable, factor $(1+\omega^2\tau^2)^{-1/2}$ | 2.7 |

Two structural points the figure can make, both absent from the text:

- For $\omega\tau \gg 1$ the ratio tends to $(f_1/f_2)^2 = 1/81$ independently
  of $\tau$. The 9 versus 1 kHz penalty is therefore not an artifact of the
  assumed 0.2 ms; it holds for every point-membrane access slower than about
  20 µs ($\omega\tau = 1$ at 9 kHz). At $\tau = 0.1$ ms the ratio is 0.042, at
  16 ms it is 0.012. The sealed-cable law softens the exponent to one (ratio
  0.11–0.14).
- The dynamic MPR detector gives no escape: its fast-carrier beat source scales
  as $I_1 I_2/(\omega_1\omega_2\tau_m^2)$ (2.10), the same exponent two.

Missey et al. 2026, read in the published PDF:

- Abstract: "low-frequency (1 kHz + 1.13 kHz) or high-frequency (9 kHz + 9.13 kHz)
  carrier waves". Methods, p. 3: "Emory used 1300 and 1430 Hz, and the Czech and
  Hungarian centers 9000 and 9130 Hz, applying ±2 mA per pair". The abstract and
  Methods disagree on the low carrier; quote the Methods value.
- Table 1: Emory 3 patients (P6–P8), SAUH 7, INN-SU 3. The carrier comparison is
  3 patients at 1.3 kHz against 10 at 9 kHz, between centers, with different sEEG
  coverage; there is no within-person carrier change.
- Results: "we did not see any reduction in the effectiveness of epileptic
  biomarker suppression by using higher carrier frequencies ... (Wilcoxon tests,
  p-value TI1000Hz vs TI9000Hz > 0.05, r = 0.69)". Discussion: "AM with 9 kHz
  carriers modulated pathological brain activity equally well as AM with 1 kHz
  carriers"; "some models predict that shifting the carrier frequency up ... will
  simultaneously reduce the modulatory effectiveness of AM. We do not observe
  this experimentally." Their HH comparison sentence still carries a placeholder
  ("X mA more at 9 kHz versus 2 kHz") in the published text.
- Sham: unmodulated 1 kHz suppresses cortical IEDs, 9 kHz sham does nothing; a
  carry-over effect follows TI only.

What the paper can say, in order of strength: (i) the design cannot resolve a
factor of 30 in the generated source (3 versus 10 patients, between centers, no
within-person sweep); (ii) biomarker suppression under a 130 Hz envelope at
4 mA is a thresholded readout and need not be proportional to the beat source,
so equal suppression is compatible with unequal sources once the lower carrier is
past the proportional regime; (iii) if equal efficacy at fixed current is
confirmed within person, it falsifies point-membrane and cable access in the
weak regime and requires either access faster than about 20 µs or a mechanism
outside the weak expansion. The Table 4 "Carrier dependence" test is exactly
the within-person sweep; Missey makes it the first experiment to propose.

Esmaeilpour 2021 slice thresholds (PubMed abstract): 100 Hz carrier about
5 V/m, 1 kHz about 60 V/m, 2 kHz about 80 V/m. The 2 kHz / 1 kHz field ratio of
1.33 is flatter than the point-membrane 1.7–2.0, but at 60 V/m the polarization
is tens of millivolts, outside the weak expansion; plot as data points with
that caveat or leave out.

Smallest defensible figure, analytic, no simulation (Eq. (khz) and the 5.4
budget suffice):

- (a) beat-source access factor against carrier, 0.1–10 kHz, log–log, for
  $\tau$ = 16, 1, 0.4, 0.2, 0.1 ms and the sealed-cable curve at 0.2 ms; markers
  at 1.13, 1.43, 2, and 9.13 kHz.
- (b) per-tone field required for the 5.4 budget polarization $\varepsilon$ =
  0.1 mV against carrier, for $\lambda_0$ = 0.5 and 0.15 mV per V/m, with
  horizontal lines at the reported human cortical 0.8 V/m at 2 mA and at the
  IXI002 hippocampal value (Table 3 envelope mean 0.16 mV at 2 + 2 mA gives a
  per-tone polarization of about 0.08 mV before access, 0.03 mV after the
  2 kHz factor 0.37).

A five-row table (carrier × access case → ratio, field factor) is the
no-figure fallback. Placement: the reviewer asked for a figure and the abstract
makes the claim, so the article (2.8) is the natural home; Table 2 could move
to S1 in exchange if length rules. Agree with Kaiti on the two traps: the access
factor applies to the static JR chain only, since PING and QIF compute access
inside $\tau_E$ (say so in the caption); and varying $\tau$ at fixed
$\lambda_0$ silently assumes the fast compartment couples like a soma, so
$\lambda_0$ is labeled an assumed scale and the 0.15 line is shown. I would
keep the figure analytic rather than build on `code/qif_short_tau_check.py`;
its fixed-current MPR results can be markers, not the backbone.

## 2. Novelty against Cassarà 2025, Esmaeilpour 2021, Luff 2024

Credits already in place: Esmaeilpour in the Introduction and as the first
sentence of 5.1 ("already related network TI sensitivity to short, axon-like
membrane times and distinguished sensitivity from selectivity"); Cassarà part II
for the product-law invariance in 2.3 and in Table 4; Luff's neuron mixer in the
Introduction; Luff PWM-TI in S1 only; Missey once, in 5.3, for modulation of
ongoing activity. Checked against the abstracts: Esmaeilpour measured slice
thresholds and modeled sensitivity with 1 and 0.4 ms membranes and selectivity
through adaptation; Cassarà II derived safety thresholds from exposure metrics
and noted that second-order mixing follows the field product; Luff PWM-TI showed
that the passive low-pass converts a pulse-width-modulated field into an
amplitude-modulated membrane potential.

What draft22 adds, each traceable to a section: the three-stage decomposition
with stated matching conditions and the 2–5% tDCS/tACS comparison at a pinned
operating point (2.6); the exact MPR detector with its slow/fast crossover and
slope-versus-curvature sign rule under the same product law (2.10, App. B); the
signed steady source and the subharmonic no-interior-maximum result for the
mean-square and envelope-mean maps (2.5, S3); opposite focus motion of envelope
and mean-square maps with a fixed beat map in a realistic head (4.4), which goes
beyond Cassarà's invariance remark; the shared linear amplifier with tACS and the
J-curve separating gain from detection (4.5, 4.7); the 0.348 memoryless bound and
the 1/5 harmonic signature as detector-class tests (2.4, 5.4).

Recommend Modify: one paragraph of at most 120 words opening 5.1 (or closing the
Introduction), one sentence per prior work followed by one sentence listing the
additions above; cite Missey in 2.8 where the carrier penalty is stated. No
computation.

## 3a. Abstract sign claim against the MPR slope regime

The contradiction is real and regime-dependent. Abstract: "its sign set by
detector curvature, not carrier polarity". Section 2.10: at fast carriers
$\kappa_{\rm DC} \sim F'/[2(\omega\tau_m)^2] > 0$, "without a PEIX-based sign
reversal". The paper's own PING runs sit in that regime ($\omega\tau_E$ = 28 at
300 Hz with $\tau_E$ = 15 ms) and report a positive excitatory drive shift, while
the JR detector at $v^*$ = 8.30 mV has $\Sigma'' < 0$. The two detectors in the
paper thus predict opposite steady-source signs. Recomputed crossover where
$|F''|/4$ equals $F'/[2(\omega\tau)^2]$: $\omega\tau \approx 2.0$ at $Q = 0$,
3.7 at $Q = 1$ (Lorentzian half-width 1).

Fix at zero token cost in a 296/300 abstract: "its sign set by detector state,
not carrier polarity". The body (2.5, 2.10, Table 4) carries the two regimes.
The Conclusion has no sign sentence; the Results sentence of the abstract
("signed ... proportional to their summed squares") holds in both regimes.
Kaiti chooses the wording and recounts with TeXcount.

## 3b. Multicompartment quadratic tensor

With compartments $k$ the second-order source is $\sum_{kl}\chi_{kl}\,
\varepsilon_1^k\varepsilon_2^l$: bilinear in the two fields, and a scalar
product $(\boldsymbol\lambda\cdot\mathbf E_1)(\boldsymbol\lambda\cdot\mathbf E_2)$
only when $\chi$ has rank one. Already in the text: 2.2 sums compartments as
parallel inputs with aligned phases; 2.3 ends with the vector, compartment-
specific coupling and says the scalar maps use fixed projections; 2.3 also
claims the common current factor survives "dynamic mixing and spatially
heterogeneous gains", which is the bilinear statement in words.

Two consequences to state explicitly. The current-ratio conclusion survives:
the source still carries $I_1^{\rm pair}I_2^{\rm pair}$ times a fixed pattern.
The no-interior-maximum result needs one more hypothesis: $Q(\boldsymbol
\varepsilon) = \boldsymbol\varepsilon^{\rm T}\chi\boldsymbol\varepsilon$ is
convex for semidefinite $\chi$, and a convex function of harmonic components is
subharmonic (the S3 envelope argument); an indefinite $\chi$, for example a
soma and an AIS with opposite curvature signs, admits an interior extremum.
Recommend Accept: add "and a semidefinite mixing form across compartments" to
the assumption list in 2.5 and the Conclusion, and four lines in S3 next to the
envelope proof. No computation.

## 4. Single head, top-decile centroid, modest contrasts

Already stated: 4.4 closes with "one subject and one montage, with quasi-static
conductivities and a uniform coupling"; the reference includes other deep gray
matter; contrasts are given raw and degree-matched; focus fraction 5–50%,
montage, label, and tissue give the 32 cases of S3; the Yatsuda montage is one
of them. Not stated: that no map in this subject favors the hippocampus over
the reference by more than 1.24, so the maps separate the detector laws by the
direction of focus motion, not by selectivity; and the abstract does not say
"one head model".

Recommend Modify, wording only: Approach sentence "and test spatial predictions
in a realistic head" to "and compare spatial maps in one head model" (same token
count, and it also answers item 6); one sentence after Table 3 on the 0.90–1.24
range. Decline new subjects or montages: the ordering (envelope anterior,
mean-square posterior, beat fixed) follows from the steering algebra; the head
model supplies magnitudes, and more subjects would cost Ricardo days without
changing the result.

## 5. Theta-neuron convergence versus qualitative spiking scope

Already stated three times: Methods 3.6 ("do not establish joint convergence"),
Results 4.9 ("quantitative convergence remains unestablished"), S4 with the
cutoff series 0.093, 0.127, 0.139 at $V_{\rm peak}$ = 100, 200, 400 against the
mean-field 0.128; and "the equal-power control ... has been tested only in the
mean field" (4.9, Table 4).

Assessment. The cutoff dependence is the expected finite-$V_{\rm peak}$ artifact
in a network whose mean field assumes $V_{\rm peak} \to \infty$. The theta-neuron
change of variables $V = \tan(\theta/2)$ removes the parameter exactly, as in
Montbrió 2015 and Devalle 2017. The runs are cheap: `code/qif_amp10_run.txt`
records 0.7 min per 1.6 s condition at $N$ = 8000 per population and
$\Delta t$ = 2.5 µs; the theta form needs no smaller step. The change to
`qif_raster.py` is about thirty lines (state $\theta_j$,
$\tau\dot\theta = (1-\cos\theta) + (1+\cos\theta)(\eta_j + I_j)$, spike at
$\theta = \pi$, synapses unchanged). Expected outcome: depth within finite-size
noise of 0.128, which turns three caveat sentences into one result; if it
differs, that is a finite-$N$ statement and the qualitative route remains.

The spiking equal-power control is the same script with one carrier at
$\sqrt2 A_f$: two runs ($A_f$ = 10 and 35), minutes. It closes "tested only in
the mean field".

Verdict: Accept both as the smallest defensible computations of the whole
review, under one hour including edits. Disagreement with Kaiti: she proposes
the bounded qualitative scope now with theta optional. I rank the theta run
first because the reviewer offered it as the alternative to a downgrade, it
removes a free parameter rather than adding one, and it costs minutes. If K
wants no computation, the qualitative route needs only the depths reported to
one figure with their cutoff range (0.09–0.14) in 4.9 and the Fig. 11 caption.
The full PING stays in Methods either way.

## 6. Violante comparison as hypothesis

Already conditional throughout 5.2 ("consistent with ... if the steady source
lowers activity and the hemodynamic response preserves that ordering"; "BOLD
and functional connectivity measure neither source directly"; "does not
establish a null effect"), per the October 19 plain-logic revision. Where a
reader can still see "validation": the abstract Approach "test spatial
predictions in a realistic head"; Table 4 row 3, which lists a model result
("holds in IXI002") under "Existing evidence".

Recommend Accept, wording only: open the Violante paragraph with "The comparison
is a hypothesis generated by the maps in one subject, not a test of them"; move
"holds in IXI002" into the Prediction column of Table 4; apply the abstract
change of item 4.

## Minor items

- m1, population rate versus spike timing. The JR quantity in 4.6 is beat-locked
  modulation of the population rate; the abstract ("amplification appears mainly
  in beat-locked timing") and Conclusion use "timing". Spike timing is measured
  only in QIF, where it is weak (PPC median 0.003–0.005, pooled vector strength
  0.12–0.13 at $A_f$ = 35). Replace with "beat-locked modulation" in the
  abstract and Conclusion (same token count), rename the Table 4 row, keep
  "timing" for the PPC statements. Accept.
- m2, equal-RMS versus equal-power. Methods 3.6 says equal-RMS and defines it by
  mean-square amplitude; Results, abstract, Table 4, and Conclusion say
  equal-power; 2.6 matches "RMS polarization". The quantities coincide; use one
  term, defined once at 3.6 ("equal-power, that is equal RMS polarization").
  Accept.
- m3, portable FEM arrays and tagged snapshot. The nonpublic part is the solver;
  the inputs to `fem_quadmaps.py` are two field-per-current vectors at 446,877
  node–compartment rows, coordinates, compartment id, the aseg and atlas masks,
  and $\mathbf n^*$, about 20 MB as float32 npz, derived from an open-access
  image and already named by hash in `fem_quadmaps.json`. Depositing them lets
  anyone recompute Table 3, Table S-sensitivities, and Fig. 8 without the
  library. Accept: Ricardo exports; Zenodo version and git tag at submission,
  which the Code availability "release hold" comment already anticipates.
- m4, shorter narrative, Table 4, LaNMM. Table 4 has nine rows and three prose
  columns. Merge "Carrier dependence" with "State and carrier dependence",
  "Independent carrier amplitudes" with "Transduction class", "Timing versus
  rate" with "Network readout": six rows, one-line evidence cells. LaNMM is
  already S6 with one Introduction sentence and one in 5.3; the Introduction
  sentence can go. The narrative request is a second vote for decision D5; a
  de-duplication pass limited to 5.1, 5.3, and the Results preambles is where
  the words are.

## Not recommended

- More subjects or montages (item 4): cost without a change of result.
- A new kHz simulation (item 1): the access factor is analytic and the JR
  two-tone kHz run exists (Fig. S6).
- Quantitative modeling of Missey: fields unknown, between-center design.

## Order of work and decisions for K

1. Wording-only edits (3a, 3b clause, 4, 6, m1, m2): Kaiti, one pass; abstract
   stays at 296 whitespace tokens with the two zero-cost substitutions.
2. Feasibility figure and Missey paragraph (1): Klaus can produce the script and
   PDF in `notes/2026-10-24_klaus/` for Kaiti to adopt, on K's go.
3. Theta-neuron and spiking equal-power runs (5): Klaus can write the theta
   variant as a separate script, run it on a scratch copy, and report; Kaiti
   integrates. Nothing in `code/` is edited until she adopts it.
4. Novelty paragraph (2) and Table 4 merge (m4): Kaiti.
5. FEM array export (m3): Ricardo; tag at submission.

K decides: figure in the article or in S1, and whether Table 2 moves out in
exchange; theta run now or qualitative scope; the two abstract substitutions;
Table 4 merge; FEM array deposit (the arrays are outputs of the nonpublic
library, so NE should confirm).
