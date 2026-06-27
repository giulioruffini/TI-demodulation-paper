"""Provenance: convert Raul de Palma's Jansen-Rit continuation output (AUTO/pandas
pickles + CSVs) into the committed numpy file code/jr_bifurcation.npz that figures_v2.py
reads. Run once; needs pandas (NOT a runtime dependency of the figure pipeline).

Inputs (this folder):  fp.pkl (fixed points: p,y1,y2,PT), lc1.pkl, lc2.pkl (limit cycles:
p,y_min,y_max,PT), bfp.csv, blc1.csv (bifurcation labels+values). Stability: PT<0 = stable.
Sign convention written out is the paper LFP v = y1 - y2.
"""
import os
import numpy as np
import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
fp = pd.read_pickle(os.path.join(HERE, "fp.pkl"))
lc1 = pd.read_pickle(os.path.join(HERE, "lc1.pkl"))
lc2 = pd.read_pickle(os.path.join(HERE, "lc2.pkl"))
bfp = pd.read_csv(os.path.join(HERE, "bfp.csv"))
blc = pd.read_csv(os.path.join(HERE, "blc1.csv"))

out = dict(
    fp_p=fp["p"].values, fp_v=(fp["y1"] - fp["y2"]).values, fp_stable=(fp["PT"].values < 0),
    lc1_p=lc1["p"].values, lc1_min=lc1["y_min"].values, lc1_max=lc1["y_max"].values,
    lc1_stable=(lc1["PT"].values < 0),
    lc2_p=lc2["p"].values, lc2_min=lc2["y_min"].values, lc2_max=lc2["y_max"].values,
    lc2_stable=(lc2["PT"].values < 0),
    bif_label=np.array(list(bfp["label"]) + list(blc["label"])),
    bif_value=np.array(list(bfp["value"]) + list(blc["value"]), float),
)
np.savez(os.path.join(HERE, "..", "jr_bifurcation.npz"), **out)
print("wrote code/jr_bifurcation.npz")
