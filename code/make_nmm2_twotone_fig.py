"""NMM2 PING resonance curves under a genuine two-tone TI field.

Kaiti's item 4: the exact mean field is the rung that answers "is this an artifact
of the empirical JR sigmoid?", so its main resonance figure must use the waveform
physical TI delivers. The dense (Delta f, etabar) map stays on the AM surrogate --
it reads only the leading Omega component, where the two agree (JR Fig. 6d).
"""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import figstyle
figstyle.apply()
import overlap
import nmm2_ping as N

FIGDIR = N.FIGDIR
A, fc = 8.0, 300.0
dfgrid = np.linspace(30.0, 110.0, 81)
stable = [-2.0, 0.0, 0.7, 0.9]
cycle = [2.0, 5.0, 11.0]

N.WAVE = 'twotone'
print(f"NMM2 PING, WAVE={N.WAVE}, A={A}, fc={fc} Hz")

fig, (a1, a2) = plt.subplots(1, 2, figsize=(11, 4.2))
for e0 in stable:
    c = N.lockin_curve(e0, dfgrid, A=A, fc_Hz=fc)
    a1.plot(dfgrid, c, label=f"$\\bar\\eta={e0:g}$")
    print(f"  stable eta={e0:>5g}: peak {c.max():.4f} at Delta f = {dfgrid[np.argmax(c)]:.1f} Hz")
figstyle.panel(a1, "a")
a1.set_xlabel(r"envelope frequency $\Delta f$ (Hz)")
a1.set_ylabel(r"lock-in response at $\Delta f$ (a.u.)")
a1.legend(fontsize=8, title="approaching Hopf")

for e0 in cycle:
    c = N.lockin_curve(e0, dfgrid, A=A, fc_Hz=fc)
    a2.plot(dfgrid, c, label=f"$\\bar\\eta={e0:g}$")
    print(f"  cycle  eta={e0:>5g}: peak {c.max():.4f} at Delta f = {dfgrid[np.argmax(c)]:.1f} Hz")
figstyle.panel(a2, "b")
a2.set_xlabel(r"envelope frequency $\Delta f$ (Hz)")
a2.legend(fontsize=8)
for _a in (a1, a2):
    _a.set_xlim(30, 110)
    _a.set_xticks([40, 60, 80, 100])

fig.tight_layout(rect=[0, 0, 1, 0.96], w_pad=3.0)
figstyle.scale_text(fig, placed_frac=1)
overlap.check(fig, placed_frac=1, name="make_nmm2_twotone_fig.py")
fig.savefig(os.path.join(FIGDIR, "fig_nmm2_resonance_twotone.png"), dpi=300)
fig.savefig(os.path.join(FIGDIR, "fig_nmm2_resonance_twotone.pdf"))
print("wrote fig_nmm2_resonance_twotone")
