# Draft20 FEM integration shared privately

The private Ricardo collaboration repository now contains draft20 scientific
source `1640b2b` as commit `c386e542e476793f1dc7b013e894906079dc45de`.
The update continues Giulio's October 14 authorization of private sharing and
Ricardo's collaboration, followed by the October 19 instruction to continue
integrating his FEM contribution. Public release remains held.

The isolated private checkout first advanced from `aa18f10` to Ricardo's
`d7790943ae8ed9186c7a6233cc7698f58efeb992`, then received the reviewed integration
as a descendant commit. His producer, JSON and NPZ remain unchanged. The
private remote was refreshed before the push to check for concurrent changes.
GitHub reports PR #1 merged at 14:30:46 UTC on October 19, and the remote
`main` hash matches `c386e54`.

Klaus's fidelity pass applies to canonical integration `23b515c`. Subsequent
changes confirm Ricardo's CRediT and GALVANI support, move the producer's
ampere convention into the settings document, and clarify target/reference
terminology. No numerical results changed after his check. The shared README
describes the completed comparison and the field-angle and interface details
still awaiting Ricardo's definitions and evidence.

The mirror retains its existing JNE default; this build switch is the only
manuscript difference from the canonical source. The article and supplement
were compiled in the isolated checkout, with cross-document labels initialized
and final reference passes completed. They contain 46 and 21 pages, with no
errors, undefined references, overfull boxes, duplicate labels, or outstanding
rerun requests. Their extracted text matches the reviewed PDFs page for page.
The published PDFs were then copied byte for byte from the canonical outputs.
The redline remains against draft13 (`c620335`).

The remote article blob is `4db9f9cc28e670aa8b0a5b14bbc6382158cf40ec`, matching
the local shared file. Build diagnostics, PDF hashes, and the verified PR state
are in `share_2026-10-19_ricardo.json`. This verifies the shared document package;
it does not rerun the private FEM solver or establish a biological response map.

Klaus was notified before the update to avoid a concurrent sync. No separate
Overleaf website import or pull was performed. The public GitHub repository,
Calliope, Zenodo, and circulation to other coauthors remain held.
