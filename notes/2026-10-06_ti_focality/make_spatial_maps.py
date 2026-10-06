"""Illustrative spatial maps for the TI comparison note; no head-model claim."""
from pathlib import Path
import json
import sys
import numpy as np
from scipy.special import ellipe
from scipy.integrate import quad
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

HERE = Path(__file__).resolve().parent
xi = np.linspace(-1, 1, 801)
a, b = 1 + xi, 1 - xi
env_mod = 2 * np.minimum(a, b)
quad_mod = 2 * a * b
env_mean = (2 * (a + b) / np.pi) * ellipe(4 * a * b / (a + b)**2)
quad_mean = (a*a + b*b) / 2
center = len(xi)//2

# Independent temporal integrals verify both means and the signed-input convention.
checks = []
for aa, bb in [(1, 1), (2, 0), (10, .2), (1, -0.7), (.3, 1.4)]:
    mean, err = quad(lambda th: np.sqrt(max(0., aa*aa+bb*bb+2*aa*bb*np.cos(th))),
                     0, 2*np.pi, epsabs=1e-11, points=[np.pi])
    mean /= 2*np.pi
    analytic = 2*(abs(aa)+abs(bb))/np.pi * ellipe(4*abs(aa*bb)/(abs(aa)+abs(bb))**2)
    assert abs(mean-analytic) < 1e-9
    pmean = quad(lambda th: (aa*aa+bb*bb)/2+aa*bb*np.cos(th), 0, 2*np.pi)[0]/(2*np.pi)
    assert abs(pmean-(aa*aa+bb*bb)/2) < 1e-10
    checks.append(dict(a=aa,b=bb,envelope_mean=mean,quadratic_mean=pmean,
                       envelope_excursion=2*min(abs(aa),abs(bb)),quadratic_excursion=2*abs(aa*bb)))

plt.rcParams.update({'font.family':'DejaVu Sans','font.size':9,'axes.labelsize':9,
                     'axes.titlesize':10,'legend.fontsize':8,'xtick.labelsize':8,
                     'ytick.labelsize':8,'pdf.fonttype':42,'ps.fonttype':42})
fig, axs = plt.subplots(1,2,figsize=(6.7,2.3))
colors = ['#2066A8','#B33A38']
for ax, ys, title, ylim in [
    (axs[0], [env_mod/env_mod[center],quad_mod/quad_mod[center]], '(a) Modulation',(-.04,1.07)),
    (axs[1], [env_mean/env_mean[center],quad_mean/quad_mean[center]], '(b) Mean (DC)',(.93,2.07))]:
    for y,c,ls,label in zip(ys,colors,['-','--'],['Envelope follower','Quadratic detector']):
        ax.plot(xi,y,color=c,ls=ls,lw=2,label=label)
    ax.set(xlim=(-1,1),ylim=ylim,xlabel=r'Position $x/L$',ylabel='Relative to center')
    ax.set_title(title,loc='left',pad=7)
    ax.set_xticks([-1,-.5,0,.5,1])
    ax.spines[['right','top']].set_visible(False)
    ax.grid(axis='y',color='#E8E8E8',linewidth=.6)
axs[0].set_yticks([0,.5,1])
axs[1].set_yticks([1,1.5,2])
axs[1].legend(loc='upper center',frameon=False)
fig.tight_layout(w_pad=2.3)
sys.path.insert(0,'/Users/giulio/.agents/skills/figcheck/scripts')
import overlap
overlap.check(fig,placed_frac=1.0,name='ti_spatial_maps',min_pt=7.5)
fig.savefig(HERE/'spatial_maps.pdf')
fig.savefig(HERE/'spatial_maps.png',dpi=180)
(HERE/'map_checks.json').write_text(json.dumps({'integral_checks':checks,
    'center_means':{'envelope':float(env_mean[center]),'quadratic':float(quad_mean[center])},
    'edge_means':{'envelope':float(env_mean[0]),'quadratic':float(quad_mean[0])},
    'off_target_vs_target':{'envelope_modulation':.2,'quadratic_modulation':2.0}},indent=2)+'\n')
print('Spatial-map integrals and examples verified.')
