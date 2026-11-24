# Draft reply to Ricardo (for Giulio to send on the FEM thread)

Hi Ricardo,

Thanks for the careful read. Your numbers match the committed JSON: the mean-based
contrasts are 0.81, 0.61, and 0.47 at 1:1, and the envelope's upper tail is 52%
white matter against 25% across the ROI. We agree that the 1.22 overstates the
geometric selectivity on its own. We will report the mean-based contrasts in
Table 3 and say in the text that the p95 contrast rests on a white-matter-weighted
anterolateral tail. Please send the gray-matter-only ROI contrasts for the three
maps at 1:1 and 1:3, and we will add them as the like-for-like comparison.

On Section 5.2, agreed. The +24% is the Violante, FreeSurfer, gray-plus-white value;
the committed JSON also gives +30% for the atlas label, but the other variants are
not stored. Please confirm the sign and range across the 32 combinations, and the two
node fractions (envelope rising at 0% of hippocampal nodes, mean square at about
95%) from the committed script. The fractions are what the carrier balance implies:
with anterior polarization a and posterior b at 1:1, the envelope rises only where
a > 2b and the mean square where b > 0.77a, and the ROI's |a/b| spans 0.69 to 1.44
between the 5th and 95th percentiles. We will put the confirmed values in the
supplement's steering section and keep the discussion sentence as it stands.

Smaller points: the missing degree-matched value at 1:3 is 0.95, and we will add it,
add "colors as in (e)" to the Fig. 9 caption, and list fem_orientation_interface.py
in the code-availability paragraph once PR #2 is merged.

On licensing, thanks for catching this. IXI is CC BY-SA 3.0, which permits
adaptations under BY-SA 4.0, so we will release the per-node export as a separately
licensed CC BY-SA 4.0 data file with IXI attribution and keep the code under
CC BY 4.0. We will also add an IXI acknowledgment to the paper. Please prepare the
export under that license.

[Optional paragraph, from our 30 October check of PR #2. Delete if you would rather
raise it at the merge.]
One correction to your 30 October note. In the committed JSON the own-maximum maps
do exceed the ceiling at a few nodes: 33 envelope nodes at CSF/GM, with a maximum of
7.9 against 4.475, and 45 at GM/WM, out of about 120,000 and 126,000 interface
nodes. So "none above" should read "fewer than 0.05%". They sit where the two side
fields are reconstructed inconsistently, the same discretization route as the
tangential mismatch, and they do not change the conclusion.

Best,
Giulio
