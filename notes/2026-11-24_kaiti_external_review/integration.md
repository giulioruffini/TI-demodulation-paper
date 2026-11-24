# External submission-review integration

The approved review corrections are integrated in the shared manuscript against
`0f9ecca`. The journal article is 40 pages at 12 pt, down from 44. It contains
11,180 words plus a 300-word abstract. The supplement is 43 pages. Both builds
have zero errors, undefined references, multiply defined labels, and overfull
boxes. The complete notation table and contents list are supplementary; the
article retains unit conventions and its existing Appendix B numbering.

## Scientific and presentation changes

- The Caldas interpretation concerns loss of preference for modulated carriers after blockade, not disappearance of all neuronal responses. The Discussion says network involvement.
- The spiking implementation is a finite-cutoff approximation. Its supplement states the constant-input finite-cutoff rate, its assumptions, and the infinite-cutoff limit; increasing population size does not remove cutoff error. The finite-network comparison remains qualitative.
- A tACS sweep estimates circuit gain only after local polarization and linear source conversion are calibrated at the same operating point.
- The genuine two-tone source has no surrogate modulation factor. Captions identify the waveform and amplitudes, including the settings behind the 0.143 ratio.
- Access approaching its DC value is conditional on being fast relative to both carriers. The resonant result is on the stable-focus side of a simple Hopf. The harmonic magnitude ratio requires a dominant nonzero quadratic term and linear response. The no-quadratic-mixing statement concerns a cubic Hopf normal form under additive forcing about zero.
- PEIX is called a model-derived state index. JR rate modulation is distinguished from mean-rate change. Human null results are restricted to tested readouts; the verified Thiele citation distinguishes resting from task-related alpha.
- The abstract identifies the QIF crossover as a steady-rate shift at fixed synaptic input and states the matched-source limitation of linear resonance. Content-preserving compression retains the mesoscale model, three stages in series, 2–5% comparison, tACS/tDCS, inverse-damping gain, signed deep steady source, and spatial boundary conditions.
- Five figure labels are repaired. The last Figure 10 coupling is 135.8, whose damping rounds to 0.3/s. Figure 11 has rate units and its caption gives the per-tone input. Bibliography locators are supplied where verified; the Wang 2026 DOI is printed without inventing volume or article details.
- The supplement states the full two-second common period used for the AM Floquet calculation. No Floquet protocol error was found.

The author-selected Introduction opening, Theory 2.9 slow-limit explanation,
and Conclusion were not replaced or relocated. The clinical-state example
list was removed as approved. The external review's wholesale abstract and
Conclusion replacements and its proposed relocation of 2.9 were not adopted.

## Verification

Independent reviews are in `text_fidelity_theory.md`,
`text_fidelity_methods_layout.md`, and `abstract_final_check.md`. The first
review's two minor abstract findings were corrected; the final check has no
remaining finding. The finite-cutoff expression was independently integrated
and checked under its stated single-neuron, constant-input assumptions.

`figure_repairs/report.md` and `verification.json` record 76 exactly matching
plotted arrays between the unchanged baseline generators and repaired versions.
Their deterministic calculations were rerun where a historical numerical cache
was unavailable; neither conditions nor model parameters were changed.
Historical PNGs differ slightly in typography/padding under the current renderer,
so this is not a claim of pixel identity. The repaired figure PDFs were viewed
individually and on article pages 3, 18, 20, 23, and 24. Final article pages 1,
6, 17, 29, and 37 and supplementary pages 1, 24, and 25 were also inspected.
All main-source equation/section labels are preserved. `validation.json` records
counts, build checks, and final hashes. The Wang DOI prints in the bibliography.

## Public-code and artifact scope

Klaus owns the authorized public-code update and availability paragraph. He
changed the reference from `4b7cc66` to the planned `jne-submission` tag at
16:16 CET. A read-only remote check at 16:20 found no such tag yet. Its public
cut must include the four repaired figure generators; he has been told. The
plotted numerical arrays are unchanged. The paragraph has not been edited by
Kaiti, and the final journal build includes his new reference.

The full-TN PDF and BBL were already modified before this task. They were not
rebuilt, restored, or staged. The separate Klaus Introduction draft is also
untouched. Only journal builds were run. Archive updates, Overleaf/Calliope
synchronization, and coauthor circulation remain held. The FEM export and the
remaining author decisions are still open in `todo.md`.

Build logs, review snapshots, and rendered pages are retained locally in
`build/external_review_2026-11-24/`. Figure baseline images and numerical scratch
caches remain in the figure-review directory; the committed record contains the
bounded scripts, reports, and check results rather than all scratch artifacts.

## Release handoff received after integration

Klaus’s 16:06 message arrived after the `bc4a7dd` report and relayed Giulio’s
authorization to update Overleaf and send the coauthor email once integration
was complete. Those actions are now handed to Klaus with `bc4a7dd`, together
with the public code/tag update. The earlier hold statement above records the
state before that handoff arrived; it no longer applies to Overleaf or this
coauthor email. Zenodo and Calliope are outside this authorization. The
availability paragraph retains Klaus’s later submission-tag wording rather
than reverting to the older `4b7cc66` reference. No email or Overleaf update has
been performed by Kaiti.

Klaus’s 16:09 message subsequently arrived and clarified that Giulio sends the
coauthor email. The handoff was corrected immediately: Klaus owns Overleaf
and the public code/tag cut; he leaves the email draft for Giulio. Neither
Kaiti nor Klaus is authorized by this handoff to send it.

## Public release and mirror verified

Klaus’s 16:22 completion report was independently checked at 18:42–18:43 CET.
Public `main` and the peeled annotated tag `jne-submission` both resolve to
`ed0fb39503dadbb9677762310464f081cec38265`. The main source, abstract, all four
repaired generators, and both journal PDFs are byte-identical to `bc4a7dd`.
The Overleaf GitHub mirror’s main branch is
`8b75fe4d5ae41f9f685aef73114906c835a84967`; the main source, abstract, notation
file, bibliography, and five repaired figure PDFs are byte-identical to
`bc4a7dd`. Klaus reports a clean 40-page test build of its compilation subset.

These checks close the public-tag and mirror tasks. The Overleaf web project
still requires Giulio’s pull and recompile. Giulio sends the coauthor email.
No archive update or email send is implied by this release verification.
