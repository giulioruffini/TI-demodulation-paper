# TN0484 draft15: harmonic and drive ratios

October 6, 2026. Follow-up to Klaus's 18:03 notation check, based on `972d9ea`.
The version remains draft15, and the reading redline remains against draft13
`c620335`.

The second-to-first harmonic ratios now use `\mathcal H_{\rm det}` and
`\mathcal H_{\rm meas}`. The TI/direct-drive source ratio uses
`\mathcal R_{\rm det}` instead of `\eta_{\rm det}`, alongside the existing
linear TI/tACS output ratio `\mathcal R_{\rm lin}`. This separates harmonic
content from drive comparisons and reserves eta for excitability. The article,
supplement, shared notation table, and storyline use the same names.

Figure 7 already had the draft14 labels `\kappa_{\rm DC}` in normalized units
and `\tilde\omega=\omega\tau_m`. It needs no further change. Its plotted
quantities and all numerical data remain unchanged.

The audit in `notation_ratios_audit_2026-10-06.json` verifies that the source
changes consist only of these substitutions. All equation, figure, table, and
section labels retain their numbers. The 297-word abstract is unchanged. Clean
builds retain 40 article pages, 20 supplement pages, 55 pages in the private TN
validation build, and 10 storyline pages. The redline has 42 pages. The changed
harmonic and efficiency equations and notation-table rows were inspected in
the rendered PDFs. The manuscript prose checker reports no findings.

This follow-up supersedes the choice to retain eta-det in the draft14 notation
record. The focality-integration audit and its independent-review request refer
to `972d9ea`; the present changes do not alter that integration's mathematics or
claims. All release and circulation holds remain.
