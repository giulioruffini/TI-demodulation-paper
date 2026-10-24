# Draft22 referee assessment and proposed revision

October 24, 2026. Assessment of the review supplied by Giulio against draft22,
source HEAD `8d7bd08`. This is a planning document. No manuscript, abstract,
figure, numerical cache, or publication artifact is changed. Klaus has been
asked for an independent assessment; reconciliation is recorded below.

## The review identifies a scope problem and a useful new calculation

The theoretical contribution survives this review. The missing physiological
calibration is real, but a sensitivity calculation cannot replace that
calibration. The revision should establish what parameter combinations the
model requires and distinguish that conditional result from a measurement of
human efficacy. The abstract's unrestricted curvature-sign statement needs
correction. Several other requests concern qualifications already in the body;
we should make them visible where the corresponding claims appear, rather than
add another layer of repeated caveats.

| Referee item | Verdict | Proposed response |
|---|---|---|
| 1. Calibrated kHz plausibility | Accept sensitivity analysis; qualify what it establishes | Extend the existing Section 5.4 budget into one source-strength figure. Show assumptions, access attenuation, and equivalent direct polarization. Do not call the result physiological validation. |
| 2. Novelty | Accept sharper positioning | Lead with the joint steady/beat formulation, pinned detector-versus-gain experiment, dynamic MPR crossover, and comparative maps/controls. Cassara is already credited for product-map invariance; avoid claiming its discovery. |
| 3. Sign and multicompartment scope | Accept | Separate static curvature from the dynamic DC coefficient. Describe scalar common-vector coupling as a specialization of a bilinear response. Keep the maximum-principle claim within its actual scalar assumptions. |
| 4. Head generalizability | Accept explicit scope; defer a new anatomical cohort | Name the single-subject geometric illustration in abstract/conclusion, and call the moving location an ROI top-decile centroid. Retain quantitative contrasts and existing sensitivities. |
| 5. Spiking convergence | Accept the offered qualitative-only alternative | Keep full PING equations and finite-network illustrations, but remove any claim of converged weak-drive spike-level amplitude. A theta-neuron study is a separate optional work package. |
| 6. Violante interpretation | Accept hypothesis label; retain the comparison | The current text already gives P=0.76 and unknown neural/hemodynamic gains. Label the steady-source explanation as a hypothesis and foreground the discriminating measurement. |
| Terminology and matching | Accept | Use beat-locked population-rate modulation for JR, retain spike terminology only for measured spike quantities, and distinguish matched local RMS input/polarization from physical electrode or tissue power. |
| Reproducibility | Accept as a submission requirement | Package derived fields, coordinates, tissue/ROI labels, orientation conventions, units and hashes, plus a portable analysis script. Cached figure summaries alone do not reproduce the spatial analysis. Prepare the release locally; publication holds remain. |
| Length | Accept a further focused reduction | Compress Table 4 to a short claim-to-test table, move detailed evidence cells to the supplement, simplify Figure 8, and consolidate Discussion. LaNMM is already principally supplementary. Preserve the full PING system in Methods as Giulio instructed. |

## The feasibility calculation has a defined scope

Let E_j be each carrier's local projected field in V/m, lambda_0 the assumed
zero-frequency coupling in mV/(V/m), and tau the effective access time in
seconds. For the single-pole access hypothesis, use

    H(f,tau) = 1/sqrt(1 + (2*pi*f*tau)^2)
    epsilon_j = lambda_0 E_j H(f_j,tau)
    Y_beat = sigma'' epsilon_1 epsilon_2 / 2
    Y_DC = sigma'' (epsilon_1^2 + epsilon_2^2) / 4

These are signed rate sources before recurrent feedback, in s^-1, for the
static JR detector. The equivalent direct polarization is Y/sigma', in mV.
It is not the final rate response: that also requires the appropriate
zero-frequency or beat-frequency circuit transfer.

Proposed figure: (a) carrier-frequency versus access-time attenuation, with
representative coupling/field cases; (b) absolute JR sources or equivalent
direct polarizations across the field/coupling budget, with the operating
point explicit; (c) the separate dynamic MPR sensitivity at matched baseline,
using the existing October 2 calculation if it clarifies the comparison.
A dynamic panel is not a second independent membrane filter. Its input units
are normalized current, not calibrated human V/m. Plot it separately rather
than force an unsupported conversion. Representative corners should be checked
against direct nonlinear integration and amplitude halving; do not launch a
large network sweep merely to draw an analytic scaling law.

A provisional design grid is 0.3–10 kHz, access times 0.05–15 ms, and local
per-carrier fields 0.1–1 V/m, with static couplings 0.12, 0.18, and 0.5
mV/(V/m). These are sensitivity coordinates, not joint physiological confidence
bounds. The couplings are low-frequency measurements already cited in Section
5.4, not measured AIS kHz gains; the fastest access times are hypotheses.
Mark where the weak-input approximation fails. Varying resistance to change
tau can also change lambda_0: an independent grid describes model possibilities,
not necessarily a realizable intervention on one membrane. The existing
`docs/qif_short_tau_2026-10-02.md` already explains this issue and the matched
baseline construction; reuse it.

The reviewer’s narrowband ratio at tau=0.2 ms is 0.0200073, about 50-fold
attenuation. Using the abstract's exact pairs 1000/1130 and 9000/9130 Hz gives
0.0213311. However, Missey's Methods (p. 3) says Emory used 1300/1430 Hz and
Czech/Hungarian centers 9000/9130 Hz; those pairs give 0.0301244, about 33-fold.
The paper therefore contains a frequency-reporting discrepancy. The comparison
is across centers, not a matched within-person transfer measurement. Its
biomarker readout also differs from our generated rate source. Discuss the
high-carrier result as a constraint on the hypothesis, without fitting an
access time from it or claiming that it falsifies every quadratic detector.
[Published Missey article](https://www.psychiatry.wisc.edu/wp-content/uploads/2026/02/Article-2.pdf).
The arithmetic is reproduced by `check_access_budget.py`; its output is
stored in `access_budget_check.json` beside this note.

For the existing illustrative budget (E_j=0.5 V/m, lambda_0=0.5 mV/(V/m),
tau=0.2 ms, pinned JR derivatives sigma'=0.4745 and sigma''=-0.1508), the
narrowband equivalent direct-polarization magnitudes are approximately 3.85,
1.36, and 0.077 microvolts at 1, 2, and 9 kHz. These illustrate conditional
source magnitudes, not a clinical-effect threshold. The abstract's 2–5% result
instead holds the *post-access* per-carrier polarization at 0.1–0.3 mV; it must
not become a universal TI-versus-tDCS/tACS efficacy ratio.

## The scientific wording can become more precise without retreating from the results

Candidate abstract wording for discussion, not yet a 300-word replacement:
“The steady source can act at depth; its sign depends on detector state and
dynamics, rather than carrier polarity. Static curvature sets the sign in the
Jansen–Rit model, whereas fast-carrier rectification in the QIF model follows
the positive slope of its rate curve.” The second sentence might sit in Main
results, with the first compressed in Significance. Preserve the signed deep
effect, the product law, the direct-input comparison, and the shared amplifier.

For multiple compartments, let a_j denote the vector of local complex carrier
amplitudes. A general leading beat coefficient is a bilinear contraction
B(a_2, conjugate(a_1)); the DC terms are separate quadratic forms in each
carrier. Fixed linear access gives a_j=I_j b_j, so the beat still factors as
I_1 I_2 times a fixed spatial function. A single common projection vector is
a rank-one specialization. This preserves current-ratio invariance without
claiming universal scalar anatomy. It also matters for the boundary theorem:
an indefinite general DC quadratic form is not automatically subharmonic.
Do not silently extend the scalar summed-squares result to every detector.

The sign rule and its physics should be separated from novelty. Cassara's
Section 5.7 explicitly states product scaling and its steering consequence.
Esmaeilpour already linked membrane sensitivity to network adaptation, and
Luff measured neuronal mixing. Our contribution should be framed as the
specified extensions and controlled comparisons, not the existence of mixing
or resonance. Sources: [Cassara](https://pmc.ncbi.nlm.nih.gov/articles/PMC11733664/),
[Esmaeilpour](https://pubmed.ncbi.nlm.nih.gov/33186778/),
[Luff](https://pubmed.ncbi.nlm.nih.gov/38796852/).

The finite-network limitation is already explicit in Methods, Results, and
Supplement S4.3. Raising V_peak and halving the step did not establish
convergence; matching the mean field at one intermediate cutoff is not a
convergence argument. The referee expressly allows qualitative scope. That
is the proportionate default. If quantitative spike agreement is retained,
use a theta formulation with accurate threshold-crossing times, the same
synapses and heterogeneity, then test time-step and population-size effects
on rate modulation and phase statistics separately. This is a genuine new
numerical project, not a replacement of one cutoff by a larger number.

The existing Violante discussion already distinguishes modeled steering from
physiology and records the nonsignificant interaction. Retain the 24%/−45%/−25%
map comparison as motivation for a hypothesis, not a choice of the biological
mechanism. A discriminating experiment must measure steady and beat responses
separately at controlled local polarization and state, with an appropriate
unmodulated-carrier control. [Violante](https://doi.org/10.1038/s41593-023-01456-8).

## Proposed sequence and completion criteria

1. Revise the storyline and make a response matrix, mapping every referee item
   to a change or an explicit scoped response. Separate mathematical results,
   model demonstrations, and biological hypotheses. Consider the title
   “A tuned-receiver framework for temporal-interference stimulation” if Giulio
   wants the theoretical status visible in the title; a title change is optional.
2. Produce the conditional feasibility figure and its reproducible calculation,
   with exact two-tone access factors, stated normalization, and independent
   checks. Use existing JR and MPR work rather than add new anatomy or biophysics.
3. Revise abstract/Introduction/Discussion and the local captions, retain full
   PING in Methods, and choose the qualitative finite-network scope. Audit
   first mentions of RMS, polarity, focus, source, and response.
4. Prepare the portable FEM reproduction package and a version-specific README.
   A clean environment must reproduce maps and statistics, not just replot the
   cache. Confirm redistribution rights and missing inputs before release.
5. Recount with the same method. The current main narrative plus article
   appendices is 14,522 words before abstract/declarations/references; reaching
   12,000 on that basis requires at least 2,522 net words removed, plus any new
   text. Moving material to an article appendix does not reduce this total.
6. Rebuild article/supplement/redline and ask Klaus to check scientific fidelity,
   matching conventions, references, and reproduction instructions. Publish or
   tag the submission snapshot only when the existing release hold is lifted.

No new human experiment or multi-head campaign is needed for this proposed
revision. A future calibrated-physiology claim would need new evidence beyond
this sensitivity analysis. Giulio's decision is whether to proceed with this
bounded revision and whether quantitative spiking convergence is worth adding.
