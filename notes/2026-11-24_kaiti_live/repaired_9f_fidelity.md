# Repaired November 24 revision: fidelity check

The scientific revisions pass after the corrections below. The check compares the repaired working tree with `864121f`, the checked slow-limit revision, rather than treating `9f2b3c1` as an approved baseline. Klaus's repair log is in `notes/2026-11-24_klaus/review_9f2b3c1/`. This is a local draft checkpoint; the factual disclosures and citation choices listed below remain for Giulio.

Independent checks cover Introduction and Theory, Methods and Results, and mathematical notation and supporting modules. Their records are `repaired_9f_theory_check.md`, `repaired_9f_methods_results_check.md`, and `repaired_9f_math_notation_check.md` in this directory. Kaiti checked the Discussion, Conclusion, declarations, and final corrections. The unchanged abstract retains 298 words. Compressed numerical details were checked at their supplementary destinations; the crossover figure's complex-response error was recalculated from all 12 stored cases without rerunning the simulations.

The final corrections restore “beyond perturbation theory” in the QIF waveform rationale and identify the dynamic rate equation's additional carrier attenuation, distinguishing it from the access attenuation that enters the generated beat. The harmonic example now specifies positive common polarization amplitude. The measured harmonic-ratio formula is displayed to eliminate the reported overflow. Supplement S2.1 uses `r_*` consistently with Appendix B.3. The live notation-table page break added during review is preserved; only its trailing whitespace was removed.

The gain normalization remains explicit: `r` denotes firing rate, while NMM2 `u` is the postsynaptic potential divided by the pathway's steady voltage gain. For the single JR excitatory synapse the physical potential is `A tau_s u`. The slow rate approximation, dynamic synaptic equation, separate carrier-tracking condition, same-state comparison, stable-equilibrium qualification, and stationary derivative independent of the slow-synapse assumption survive. No extra gain symbol is introduced.

The remaining author decisions are separate from prose fidelity:

- Confirm the archive/public-snapshot wording and the omitted future CC BY-SA 4.0 export-license and IXI-attribution commitment in data availability. This pass does not verify release status or authorize a deposit.
- Confirm the new statement that the study involved no recruitment or new human or animal experiments.
- Confirm the Methods AI-use sentence and its placement, alongside the existing declaration.
- Confirm “modeled” in the de Palma study description. Its unpublished status is recorded in the bibliography; the study itself was not rechecked here.
- Decide the placement of `salvador2025`: the main-text position now follows the subject-specific head-model description, while the supplementary protocol attaches it to the conductivity choice.

`bash build.sh journal` produces a 44-page article and a 42-page supplement at 12 pt. Both final logs contain zero errors, undefined references, multiply defined labels, and overfull boxes. The shared notation-table page break accounts for the additional supplementary page relative to Klaus's earlier 41-page build. The article and integral appendices contain 11,872 words, with a 298-word abstract (12,170 combined under the repository's counting convention). The harmonic-ratio layout, dynamic-detector passage, B6 normalization, and affected supplementary material were rendered and inspected.

Frozen baseline/current comparisons, build logs, count output, source hashes, and renders are under `build/2026-11-24_live_prose_merge/repaired_9f_fidelity/`. The preexisting full-TN PDF and BBL and Klaus's working Introduction draft were left untouched. The previous submission-review redline predates these repairs. No public push, Overleaf sync, archive update, or coauthor circulation was performed.

## Author decisions at 15:55 CET

Giulio requested removal of the duplicate Methods AI-use sentence (`7a79865`) and explicit display of the GitHub repository URL (`bcd13b3`, `3447a15`, `e8d108e`). These decisions close the Methods-placement item above; the final AI declaration remains. The archive and export-license questions are separate. The same source batch removes the redundant parenthetical “DC” from the Introduction's steady-source sentence. The new count is 11,848 article-and-appendix words plus 298 abstract words, or 12,146 combined. The canonical reading PDFs were refreshed because they still showed the preceding revision.
