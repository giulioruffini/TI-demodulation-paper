# TN0484 / WP0185: private collaboration copy

The current paper is **v0.15.0-draft20**, from scientific source commit
`1640b2b` on October 19, 2026. Ricardo Salvador's FEM contribution is integrated,
and his confirmed CRediT roles and GALVANI support appear in the declarations.

Read the [JNE article](TN0484_jne.pdf),
[supplement](TN0484_jne_supplement.pdf), or
[redline against draft13](docs/redline_last_read.pdf).
The source is [TN0484_envelope_demodulation.tex](TN0484_envelope_demodulation.tex).
Both editions use the same abstract and notation files in `planning/`.

## Ricardo's FEM contribution

Methods Section 3.3, Results Section 4.5, and Figure 8 contain the IXI002/FreeSurfer
head-model comparison on the Violante montage. Changing from 2+2 to 1+3 mA moves
the envelope focus 2.5 mm anterior and the mean-square focus 4.5 mm posterior;
the quadratic and isotropic beat maps rescale by 0.75 without moving their foci.
The local projection direction is fixed across current conditions. The reference
region is all gray matter outside the hippocampal ROI, including other deep
structures, so the paper reports target-to-reference ratios.

The producer and its JSON and NPZ outputs are preserved from Ricardo's `d779094`.
The [settings document](docs/fem_ixi002_violante.md) defines the montage, units,
regions, orientations, statistics, and dependencies. The figure needs only the
included outputs; recomputing the FEM maps requires Neuroelectrics' nonpublic
library and its stored fields and labels. The integration passed a separate
read-only fidelity check against those outputs.

The third map is a nonnegative geometric quantity, not a signed physiological
response. A signed source additionally requires a specified detector coefficient
and operating point; a mean-response map requires circuit dynamics. Section 2.6
and Figure S13 explain the distinction.

The reported field-angle and interface-enhancement details await Ricardo's
definitions and evidence. Montage optimization is a follow-up outside this paper.
For further changes, branch from the current `main` and open a pull request,
including the definitions and reproducible outputs behind any numerical claims.

## Building the paper

The repository includes the figures needed to compile the manuscript.
With a LaTeX installation, run `bash build.sh jne` for the article and
`bash build.sh supp` for the supplement. Rebuild the article after the
supplement if cross-references changed. The raw TeX default is JNE in this
private copy, preserving the existing Overleaf setting.

This is the compile-ready collaboration subset of the research repository.
Simulation scripts are included, but the full simulation caches and internal
review history are not. Regenerating every scientific figure requires those
inputs; compiling the paper does not.
The previous research-checkout README is preserved as
[historical draft18 documentation](docs/research_repository_readme_draft18.md);
its paths and release status refer to that earlier checkout.

Giulio authorized private sharing and Ricardo's collaboration on October 14,
then continued the FEM integration on October 19.
The public repository, Calliope, and Zenodo have not been updated by this sync.
