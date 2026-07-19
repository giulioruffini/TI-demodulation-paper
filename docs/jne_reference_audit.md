# Reference audit for the JNE submission

Verified 2026-07-19 against the Crossref REST API. 47 core candidates plus 15 second-tier,
against a current bibliography of 43 entries. Target for JNE is 70–90.

**Nothing here has been added to `references.bib` yet.** The additions are a proposal; only
the metadata corrections below were applied, because those are factual errors rather than
editorial choices.

## Applied: five metadata errors in the existing bib

Each independently re-verified against Crossref before editing, not taken on trust.

| Key | Was | Now |
|---|---|---|
| `peripheral2023` | pages `026032` | `026041` |
| `wang2023` | year `2023` | `2022` (JNE 19(6) is the December 2022 issue) |
| `violante2023` | `Violante, Ines R. and others`, no issue or pages | all 14 authors; 26(11):1994–2004 |
| `sanchezTodo2023` | `and others` | all 8 authors |
| `eyal2016`, `deitcher2017` | `and others` | all authors |

`and others` renders as "et al." in the bibliography, which IOP copy-editors reject. Note
also that a same-titled Violante *Brain Stimulation* conference abstract exists
(16(1):122, doi 10.1016/j.brs.2023.01.031) — do not let a reference manager substitute it.

## The four omissions most likely to be flagged by a referee

These are not "more citations." Each is a paper that proposes or measures something close
enough to our claim that its absence reads as unawareness of prior art.

1. **Negahbani et al. 2018**, *NeuroImage* 173:3–12, doi 10.1016/j.neuroimage.2018.02.005.
   A cortical model in which endogenous oscillations phase-lock to the *envelope* of an AM
   high-frequency waveform, showing "the same target engagement mechanism as conventional
   low-frequency tACS." That is the direct modeling precedent for two of our headline
   claims. Our contribution survives intact — we name the demodulator ($\Sigma''$) and the
   $1/\gamma$ amplification that they leave as an emergent model observation — but only if
   we cite them and say so.

2. **Ali, Sellers & Fröhlich 2013**, *J. Neurosci.* 33(27):11262–11275,
   doi 10.1523/JNEUROSCI.5867-12.2013. Entrainment arising from "a strong nonlinearity
   provided by the local excitatory coupling of pyramidal cells," with an Arnold tongue.
   This is our population-nonlinearity logic applied to unmodulated tACS, under the name
   "network resonance."

3. **Ledoux & Brunel 2011**, *Front. Comput. Neurosci.* 5:25, doi 10.3389/fncom.2011.00025.
   Computes the network dynamical transfer function against input frequency for both a rate
   model and an LIF network, with the resonance tied to recurrent coupling strength. This is
   our $G(\Omega)$ susceptibility derived independently. Belongs in §carrier and §jcurve.

4. **Krause, Vieira & Pack 2023**, *PLOS Biology* 21(1):e3001973,
   doi 10.1371/journal.pbio.3001973. Argues the real question is how stimulation interacts
   with ongoing activity, and proposes coupled-oscillator models with state-dependent, even
   opposite, effects. The closest published statement of our own framing, from the group
   whose TI data we already cite.

## Work that contradicts or complicates the thesis

Ranked by how much damage it does if a referee raises it before we do.

**1. The dose problem — the most serious.** Rampersad et al. 2019
(*NeuroImage* 202:116124, doi 10.1016/j.neuroimage.2019.116124) finds optimized human TI
montages deliver ~0.37 V/m at pallidum and ~0.24 V/m at hippocampus, "too low to expect
direct stimulation effects," against 383 V/m in mouse. Vöröslakos et al. 2018
(*Nat. Commun.* 9:483) measures ~75% of scalp current shunted before it reaches cortex and
sets a ≥1 mV/mm floor for affecting spiking. Huang et al. 2017 (*eLife* 6:e18834, **with**
correction 7:e35178, which changes the magnitudes) gives the in-vivo human calibration.

Together these say the mechanism has to work an order of magnitude below the single-cell
threshold. That is survivable and arguably the whole point — a population read-out with
$1/\gamma$ gain is exactly what could operate there — but the argument only lands if we
state the numbers and claim the required amplification factor explicitly. At present the
paper motivates itself qualitatively and never quantifies the gain it needs.

**2. Published human negatives.** Iszak et al. 2023 (*Biomedicines* 11(7):1813) is a human
null on CNS effects *with a positive peripheral control in the same subjects*.
Mansourinezhad et al. 2025 (*J. Neural Eng.* 22(5):051001, doi 10.1088/1741-2552/ae0524) is
a systematic review of 18 human tTIS studies — in our target journal — reporting that
occipito-parietal tTIS did not modulate alpha power. That is a direct negative on the
"Δf matches the intrinsic rhythm" prediction and belongs as a row in the predictions table,
not in prose. A predictions table listing only confirmations will read as selective.

**3. The peripheral confound.** Asamoah et al. 2019 (*Nat. Commun.* 10:266) shows tACS motor
effects can be produced entirely by transcutaneous nerve stimulation; Khatoun et al. 2019
(*PNAS* 116(45):22438) presses the same point. Since human TI evidence is largely
behavioral, this is the standing alternative explanation. It is winnable — rebut with Vieira
et al. 2020 (*PLOS Biol.* 18(10):e3000834, entrainment with somatosensory input blocked) and
the Vassiliadis et al. 2024 blinding data (*J. Neural Eng.* 21(2):024001, 257 sessions,
sensations indistinguishable from sham) — but only by having the exchange.

**4. The only other network-level TI model disagrees.** Karimi et al. 2024
(*Front. Hum. Neurosci.* 18:1436205) concludes tTIS needs roughly **100×** the amplitude of
tACS for comparable entrainment. We should engage the number, not just the framing. The
answer is presumably that a near-Hopf recurrent system escapes the penalty a generic
Izhikevich E–I network incurs, which is a good place for the J-curve to do work.

**5. The theory-side objection.** Devalle, Roxin & Montbrió 2017
(*PLOS Comput. Biol.* 13(12):e1005881) shows firing-rate equations are recovered from the
exact QIF description only when inputs are *slow* — and the TI carrier is fast. A referee
who knows this will ask whether the Jansen–Rit sigmoid gain is trustworthy at kHz carriers.
Our NMM2 and QIF results *are* the answer, but the answer is invisible unless the objection
is named. §nmm currently gestures at this via Clusella 2023; this is the sharper version.

**6. Criticality.** Priesemann et al. 2014 and Wilting & Priesemann 2018
(*Nat. Commun.* 9:2325) measure cortex as reliably *subcritical* and driven, so $\gamma$ is
bounded away from zero and the gain is finite. Touboul & Destexhe 2017
(*Phys. Rev. E* 95:012413) shows power-law avalanche statistics arise without criticality at
all. Fontenele et al. 2019 (*PRL* 122:208101) finds a universality class distinct from mean
field, which sits in tension with the all-to-all MPR reduction.

The opportunity here: "input reverberating for hundreds of milliseconds" is a *number*.
Converting it into a predicted in-vivo amplification factor would turn the paper's most
exposed qualitative claim into a quantitative prediction. This is probably the single
highest-value revision available.

**7. Luff et al. 2024 looks like a refutation and is not.** *Brain Stimulation* 17(1):92–103,
doi 10.1016/j.brs.2023.12.010, from Grossman's lab: square-wave fields that are pulse-width
but not amplitude modulated drive activity at the difference frequency, attributed to the
membrane low-pass. The resolution is that a PWM square wave, unlike an AM signal, *does*
carry genuine spectral power at the modulation frequency — which is precisely why PWM plus a
low-pass filter is a working DAC. So a linear filter legitimately recovers a PWM envelope
with no nonlinearity required, and the result is fully consistent with our Eq. (1). Stated
that way it sharpens the thesis. Left uncited, from the originating lab, it looks like an
omission.

**8. Plovie et al. 2025** (*Bioelectromagnetics* 46(1):e22522) finds gating *kinetics*, not
instantaneous I–V curvature, carry the single-cell TI effect — a static single-cell
nonlinearity does not demodulate. Since $\Sigma''$ is itself a static curvature, we should
say why the mesoscopic static map succeeds where the single-cell one fails. The answer is
already in the paper (the population sigmoid is an ensemble average over thresholds, states
and noise, not one cell's I–V) but is not framed as a response to this result.

**9. Kasten et al. 2018** (*NeuroImage* 179:134–143) shows weak polynomial nonlinearities in
stimulation *hardware* produce spurious power at the modulation frequency. This is our
mechanism demonstrated in silicon, which helps rhetorically — and it means any experimental
test of our predictions must exclude instrumental demodulation. Needs to sit beside the
predictions tests.

**10. Cross-frequency-coupling artifacts.** Aru et al. 2015
(*Curr. Opin. Neurobiol.* 31:51–61) and Kramer, Tort & Kopell 2008 warn that apparent CFC
arises from nonlinearity and waveform shape without any interaction between components. Our
mechanism *is* a nonlinear mixer, so our predicted signatures are the artifact signatures.
This matters most for the ~95 Hz sum sideband in `fig:qif_timing`(b), which is currently
offered as evidence.

**11. Vossen et al. 2015** (*Brain Stimul.* 8(3):499–508) finds tACS aftereffects reflect
plasticity rather than entrainment, so the TI/tACS equivalence claim should be explicitly
scoped to the online driven response.

## Also worth adding, by category

- **TI experiments**: Wessel et al. 2023 (*Nat. Neurosci.* 26:2005–2016, human striatal
  theta-burst tTIS); Vassiliadis et al. 2024 (*Nat. Hum. Behav.* 8:1581–1598 — 80 Hz but not
  20 Hz striatal tTIS altered reinforcement learning, the best human evidence for Δf
  selectivity and a clean exclusion of carrier-only accounts); Ma et al. 2022; Wang et al.
  2025 (*Front. Hum. Neurosci.* 19:1524485 — non-monotonic tuning over beat frequency with
  resting motor threshold unchanged, the closest human analogue of timing-not-rate); Acerbo
  et al. 2022; Botzanowski et al. 2025; Missey et al. 2021.
- **Mechanism/dosing**: Howell & McIntyre 2021; Cassarà et al. 2025 Parts I and II (note the
  inverted issue order — Part II is 46(1), Part I is 46(2), verified twice); Cao & Grover
  2020; Kilgore & Bhadra 2014 and Bhadra & Kilgore 2005 on kHz conduction block, which a
  referee will raise as the rival explanation; von Conta et al. 2021 on field variability.
- **Neural mass lineage**: Lopes da Silva et al. 1974 and Zetterberg et al. 1978, whose
  absence is conspicuous in a Jansen–Rit paper; David & Friston 2003; Deco et al. 2008;
  Spiegler et al. 2010; Touboul et al. 2011; Coombes & Byrne 2019 and Byrne et al. 2020
  (both of which explicitly frame the sigmoid as what next-generation models depart from —
  cite the challenge, since our NMM2 and QIF results are the answer); Pietras et al. 2019;
  Börgers & Kopell 2003; Bastos et al. 2012.
- **Criticality and resonance**: Brunel et al. 2001 (finite unlagged response as ω→∞, which
  cuts both ways and forces us to keep two arguments straight); Lindner &
  Schimansky-Geier 2001 (a TI envelope modulating input variance *is* a noise-coded signal —
  the cleanest formal bridge between our stochastic-resonance and resonance strands);
  Beggs & Plenz 2003; Shew et al. 2009; Meisel et al. 2015; Scheffer et al. 2009;
  Fröhlich & McCormick 2010; Zrenner et al. 2018 (identical stimulation, opposite-sign
  plasticity by instantaneous state — the closest precedent for our sign-flip prediction).
  §khz currently invokes stochastic resonance with no primary reference: use Gammaitoni
  et al. 1998, and McDonnell & Abbott 2009 to pin down which sense of SR we mean.
- **tACS/AM and entrainment**: Helfrich et al. 2014; Herrmann et al. 2013 and 2016;
  Schmidt et al. 2014; Hyafil et al. 2015; Notbohm et al. 2016 (an empirical Arnold tongue
  in humans); Goldstein 1967 on auditory difference tones — a non-neural precedent for a
  nonlinearity creating a real difference-frequency line, with the useful caution that the
  simple difference tone is the *weak*, even-order product, which is exactly the distinction
  the SL appendix turns on.

## Searches already exhausted — do not repeat

There is no third substantive Esmaeilpour TI-mechanism paper (only a one-page abstract).
The Mirzakhalili group's post-2020 output is spinal-cord stimulation, not TI. No
peer-reviewed full paper on TI for depression or Parkinson's exists, only conference
abstracts. There is no von Conta cadaver study — the cadaver measurements are inside
Violante 2023 and Acerbo 2022. No Minami & Amano AM-tACS paper exists (the 2017 paper is
about illusory jitter).

One caution: Zhigalov & Jensen's rapid-invisible-frequency-tagging work is a **negative**
result on intermodulation components (*PLOS One* 2026, doi 10.1371/journal.pone.0343916).
If we argue intermodulation is a reliable signature of population nonlinearity, someone will
raise it.

## Confidence

Every DOI above resolves in Crossref. A few entries have no retrievable abstract and their
content statements rest on publisher landing pages rather than fetched text: Lopes da Silva
1974, Buzsáki & Wang 2012, Chialvo 2010, Mejias 2016, Amari 1977, Cao & Grover. Treat those
as slightly lower confidence and check them at the point of citation.
