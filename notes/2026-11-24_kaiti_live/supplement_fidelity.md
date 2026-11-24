# Supplement fidelity check — 2026-11-24

The appended paragraph in `planning/parts/envelope_proof.tex` passes the algebra and scope review. The pre-merge module in `build/2026-11-24_live_prose_merge/before/planning/parts/envelope_proof.tex` remains a byte-for-byte prefix of the current file; no existing text was lost or changed.

Both proposed potentials are harmonic: the quadratic term has zero Laplacian, and the cubic bracket has Laplacian `2x − x − x = 0`. Differentiation gives the stated polarizations `1 ± x + cq`, positive near the origin. Their product is exactly `(1 + cq)² − x²`, with Hessian `diag(4c − 2, −2c, −2c)` at the origin. It is negative definite for `0 < c < 1/2`; positivity makes this also a strict maximum of the beat amplitude's magnitude. The omitted term is `c²q²`, of fourth order as stated.

The envelope excursion is exactly `2(1 + cq − |x|)` locally. Its difference from the value at the origin is `2cx² − 2|x| − c(y² + z²)`, strictly negative at every sufficiently close nonzero point. Thus the claimed maximum is three-dimensional and strict, despite the cusp in the x direction.

The closing minima sentence is correct: it refers to the earlier subharmonic mean-square and envelope-mean maps, which can have interior minima. It does not assert interior minima for the excursion or beat-amplitude maps. Relative to Klaus's proposal, the added coordinate definition and unit-coupling phrase clarify the existing construction without changing its content. No further paper edit is needed.
