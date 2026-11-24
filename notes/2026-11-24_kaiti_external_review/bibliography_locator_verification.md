# Bibliography locator verification — 2026-11-24

The bibliography update changes six existing entries and adds `thiele2024ttis`. The existing DOI fields for all six requested papers were already present. Five entries lacked their article locators. No manuscript prose, abstract, citation placement, or unrelated bibliography metadata was changed.

| Key | Verified metadata and action | Primary verification URL |
|---|---|---|
| `ledoux2011` | Frontiers in Computational Neuroscience **5:25** (2011), DOI `10.3389/fncom.2011.00025`. Added `pages={25}`; retained the existing volume and DOI. | [Publisher article and citation](https://www.frontiersin.org/journals/computational-neuroscience/articles/10.3389/fncom.2011.00025/full) |
| `karimi2024` | Frontiers in Human Neuroscience **18:1436205** (2024), DOI `10.3389/fnhum.2024.1436205`. Added `pages={1436205}`; retained the existing volume and DOI. | [Publisher article and citation](https://www.frontiersin.org/journals/human-neuroscience/articles/10.3389/fnhum.2024.1436205/full) |
| `wangw2026` | Translational Psychiatry (2026), DOI `10.1038/s41398-026-04263-4`. The publisher's indexed article identifies an early publication with a permanent DOI, without a volume/article locator. The existing entry is unchanged; no missing locator was invented. | [Publisher article](https://www.nature.com/articles/s41398-026-04263-4) |
| `wilting2018` | Nature Communications **9:2325** (2018), DOI `10.1038/s41467-018-04725-4`. Added `pages={2325}`; retained the existing volume and DOI. | [Publisher article and citation](https://www.nature.com/articles/s41467-018-04725-4) |
| `huang2017` | eLife **6:e18834** (2017), DOI `10.7554/eLife.18834`. Added `pages={e18834}` and matched the DOI's displayed capitalization; retained volume 6. | [Publisher PDF with citation footer](https://elifesciences.org/articles/18834.pdf) |
| `huang2017corr` | eLife **7:e35178** (2018), DOI `10.7554/eLife.35178`. Added `pages={e35178}` and matched the DOI's displayed capitalization; retained volume 7. The primary correction page verifies the title, authors, year, and DOI; the publisher also lists the volume/locator in its published references. | [Publisher correction](https://elifesciences.org/articles/35178), [publisher-hosted article citing the correction as 7:e35178](https://cdn.elifesciences.org/articles/92088/elife-92088-v1.pdf) |
| `thiele2024ttis` | Added the five authors in publisher order: Carsten Thiele, Katharina S. Rufener, Stefan Repplinger, Tino Zaehle, Philipp Ruhnau; exact article title; Psychophysiology **61(11):e14651** (2024); DOI `10.1111/psyp.14651`. The publisher gives first online publication on July 12 and the November issue; no month field was needed. | [Publisher full article, author list, issue, and citation](https://onlinelibrary.wiley.com/doi/full/10.1111/psyp.14651) |
| `ali2013` | Corrected only the surname spelling from `Frohlich` to `Fr{\"o}hlich`. The publisher's article/PDF identifies Flavio Fröhlich. Existing initials and all other metadata remain. | [Journal of Neuroscience article](https://www.jneurosci.org/content/33/27/11262) |
| `opancar2025` | No change. The existing `{\DJ}erek` correctly encodes the publisher's Đerek. | [Publisher article author list](https://www.nature.com/articles/s41467-025-64059-w) |

Direct rendering of some Nature, eLife, and Journal of Neuroscience pages returned cookie/JavaScript or access errors. Their publisher-hosted indexed text and PDFs supplied the metadata above; no third-party summary was used to fill a field. The accessible Wiley page independently confirms the new entry's full metadata.

Checks: the before/after comparison changes exactly `ledoux2011`, `karimi2024`, `wilting2018`, `huang2017`, `huang2017corr`, and `ali2013`, and adds only `thiele2024ttis`. Keys are unique and braces are balanced. `wangw2026` and `opancar2025` are byte-for-byte unchanged. Existing correctly accented `Fröhlich` in `negahbani2018` is unchanged. No build, commit, push, or external message was performed.

The before-copy is `references_before_locator_updates.bib`; the exact patch is `bibliography_locator_changes.diff` in this directory.

Integration note: the journal's `unsrt` style does not print DOI fields. Kaiti added the verified `wangw2026` DOI as a linked `note` so the published bibliography has a locator despite the unavailable volume/article number. The earlier entry-scope check above predates this additional field.
