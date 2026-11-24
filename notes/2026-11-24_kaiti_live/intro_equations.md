# Introduction equations — November 24, 2026

Giulio requested a revision of the Introduction equations while editing the shared manuscript. The latest saved text had replaced the intervening field-vector version with a two-tone amplitude–phase identity. That current version was the basis of this edit; the removed field-vector line was not restored.

Equation (1) now uses two aligned lines: the two-tone polarization and its amplitude–phase representation, followed by the nonnegative envelope. The phase is defined by the argument of the complex envelope wherever its modulus is positive. At an envelope zero, the phase does not affect the polarization. This replaces the unrestricted “slow phase” description: near the minima of nearly balanced tones, phase variation need not be slow.

The equal-tone identity is retained and accompanied by its absolute-value envelope. The signed modulation factor contains half the difference angular frequency; its absolute value repeats at the beat frequency. Carrier, beat, and phase definitions remain adjacent to the display, as do the units of polarization and the field-coupling pointer. The equation label is unchanged. The spectrum, nonlinear-detection argument, and natural-candidate sentence are retained.

An independent algebraic review agrees. A numerical identity check over 25,025 time/amplitude combinations, including signed and zero amplitudes, gives a maximum reconstruction error of 1.94e-13 mV; the squared-envelope and period identities agree within 1.2e-16 mV² and 6.2e-16 mV. These checks validate the rewritten identities, not a new physiological model. Evidence and exact source snapshots are under `build/2026-11-24_live_prose_merge/intro_equations/`.

The final journal build has 39 article pages and 36 supplementary pages, with no undefined or multiply defined references and no overfull boxes. The two-line equation and surrounding definitions were inspected on the rendered Introduction page. All 52 source hashes stayed unchanged during the build and validation; the preexisting full-TN PDF and BBL were preserved. The exact checked main-source SHA-256 is `25d4438185a759c4edd95b66a1729e6006dcd88ff6c42bd9de3779aa01fa58f5`.

The manuscript and article appendices contain 11,761 counted words, plus the 298-word abstract (12,059 combined). These counts use the existing convention, including captions and table text but excluding references and declarations. Final length and 12-point submission formatting remain tasks for the version cut.

Giulio continued editing the prose after validation. The commit stores the exact checked equation snapshot and its PDFs; newer live-source edits remain in the working file and are not overwritten.

## Carrier-frequency clarification

Giulio found the distinction between the first tone and the center frequency unclear. The Introduction now defines `f_c=(f_1+f_2)/2=f_1+Delta f/2` directly in hertz, before the amplitude–phase display, and then defines `omega_c=2 pi f_c`. A bounded audit found no actual identification of `f_c` with `f_1`: the notation table, symmetric two-tone protocols, and numerical examples all use the midpoint. No numerical settings changed. The journal article rebuild passes at 39 pages; the midpoint relation is present in the rendered PDF. Giulio continued rearranging the prose and commented out the equal-tone example during this pass; those live author edits are preserved. This is a shared-editing checkpoint, not a version cut.
