# Feasibility-figure field values — November 24, 2026

Panel (b) uses 0.3 V/m per tone. The budget star in panel (c) uses 0.5 V/m per tone, a 2 kHz midpoint, 0.2 ms access time, and coupling 0.5 mV/(V/m). The caption now states the latter values and the equivalent input magnitude, 1.36 microvolts. Its existing panel (b) statement is unchanged.

The generator `code/make_feasibility_fig.py` sets panel (b) through `E_REF=0.3` and draws the star from the `budget` record. `code/feasibility_khz_anchors.json` stores the star at 1.357653529 microvolts, with carrier polarizations 0.092624340 and 0.092225377 mV. An independent calculation reproduced these values; at 0.3 V/m with the other parameters held fixed, the equivalent input is 0.488755271 microvolts. No figure data, generator, or simulation changed.

The article builds at 39 pages with no errors, undefined or multiply defined references, or overfull boxes. Figure 7 and its caption were inspected on page 20. The live source remained unchanged during the build. The checked live article has 11,984 words plus its 298-word abstract (12,282 combined). Exact source snapshots, the build log, counts, and the rendered page are in `build/2026-11-24_live_prose_merge/feasibility_caption/`.

Only the caption hunk is staged in the main source. Giulio's separate beat-source units edit is preserved in the working tree and included in the live PDF; it remains for the coordinated prose checkpoint. Klaus's prose sections are untouched. No full-TN build, public push, or synchronization was performed.
