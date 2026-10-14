# TN0484 / WP0185: private collaboration copy

The current paper is **v0.15.0-draft19**, from scientific source commit
`afa5e44` on October 14, 2026. The author list includes Ricardo Salvador.

Read the [JNE article](TN0484_jne.pdf),
[supplement](TN0484_jne_supplement.pdf), or
[redline against draft13](docs/redline_last_read.pdf).
The source is [TN0484_envelope_demodulation.tex](TN0484_envelope_demodulation.tex).
Both editions use the same abstract and notation files in `planning/`.

## Ricardo's FEM contribution

Methods Section 3.3 and Results Section 4.5 contain red placeholders for the
IXI/FreeSurfer head model and Violante-montage comparison. The requested maps
are the envelope excursion, quadratic beat excursion, and mean-square
polarization, with 1:1 and 1:3 current ratios and a ratio sweep. Keep the local
projection direction fixed across conditions. Report target-to-cortex ratios,
focus displacement, and a separate isotropic orientation comparison.

The third map is a nonnegative geometric quantity, not a signed physiological
response. A signed source additionally requires a specified detector coefficient
and operating point; a mean-response map requires circuit dynamics. Section 2.6
and Figure S13 explain the distinction.

Please make changes on a branch such as `ricardo/fem` and open a pull request.
Include the head-model and solver settings, montage, currents, conductivity and
orientation assumptions, ROI definitions, and the scripts used to produce each
figure and summary. Keep reproducible outputs with those definitions.

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

Giulio authorized this private update and Ricardo's collaboration on October 14.
The public repository, Calliope, and Zenodo have not been updated by this sync.
