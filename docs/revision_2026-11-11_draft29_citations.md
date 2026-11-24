# Draft29 — companion citations

Giulio requested the TN0439 and TN0486 citations through Klaus, who added them in `08acd1f`. The journal article retains both. The TN0439 sentence follows the static-detector paragraph so it does not interrupt the polarity argument; it attributes operating-point dependence in multitone sigmoid mixing. The TN0486 sentence refers to the calibrated noise-free Stuart--Landau networks tested in that paper and their infraslow BOLD power. It does not generalize the numerical finding to all Stuart--Landau networks.

The TN0486 bibliography entry retains the frozen metadata and adds the version 0.4.1 DOI to its printed note because `unsrt` omits the `doi`, `url`, and `version` fields. TN0439 remains labeled as a working manuscript in preparation. The source check used the local TN0439 manuscript and TN0486 v0.4.1 article; the local TN0486 deposit-verification record identifies version DOI `10.5281/zenodo.24141603` and concept DOI `10.5281/zenodo.24141602`.

This citation update remains v0.15.0-draft29, with the journal date advanced to November 11. It adds 38 counted words relative to the pre-citation source: 11,443 across narrative, headings, captions, tables, and article appendices, plus the unchanged 299-word abstract. The article remains 38 pages and the supplement 35 pages.

Verification:

- Removing the two new sentences and reversing the journal-date change recovers the pre-citation source at `08acd1f^` exactly. No earlier sentence, equation, label, or qualification changed.
- The article and redline against the fixed draft20 baseline rebuild without errors, undefined or multiply defined references, or overfull boxes. The article contains no unresolved reference markers.
- The two citation passages and bibliography were inspected on pages 8, 10, and 31. The version DOI and working-manuscript status print correctly.
- SHA-256 comparisons confirm that the pre-existing full-TN PDF and bibliography and the journal supplement PDF are unchanged. Backups and page renders are under `build/citation_update_2026-11-11/`; the compact verification records are under `notes/2026-11-11_kaiti/`.

No model, data, figure, abstract, or scientific result changed. Public push, Overleaf, Calliope, data release, and coauthor circulation remain held.
