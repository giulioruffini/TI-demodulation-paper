"""Illustrative spatial maps for the TI comparison note; no head-model claim."""
from pathlib import Path
import argparse
import json
import sys
import numpy as np
from scipy.special import ellipe
from scipy.integrate import quad
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

HERE = Path(__file__).resolve().parent
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--paper', action='store_true', help='Write the manuscript figure with L_x and a signed-source panel.')
args = parser.parse_args()
OUTPUT = HERE.parents[1] / 'figures' if args.paper else HERE
STEM = 'fig_spatial_maps' if args.paper else 'spatial_maps'
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
fig, axs = plt.subplots(1, 3 if args.paper else 2,
                        figsize=(6.7, 2.65 if args.paper else 2.3))
colors = ['#2066A8','#B33A38']
for ax, ys, title, ylim in [
    (axs[0], [env_mod/env_mod[center],quad_mod/quad_mod[center]], '(a) Modulation',(-.04,1.07)),
    (axs[1], [env_mean/env_mean[center],quad_mean/quad_mean[center]],
     '(b) Mean before gain' if args.paper else '(b) Mean (DC)',(.93,2.07))]:
    labels = ['Envelope follower','Quadratic detector']
    if args.paper:
        labels = ['Envelope','Square law'] if ax is axs[0] else ['Mean envelope','Mean square']
    for y,c,ls,label in zip(ys,colors,['-','--'],labels):
        ax.plot(xi,y,color=c,ls=ls,lw=2,label=label)
    ax.set(xlim=(-1,1),ylim=ylim,xlabel=r'$x/L_x$' if args.paper else r'Position $x/L$',ylabel='Relative to center')
    ax.set_title(title,loc='left',pad=7)
    ax.set_xticks([-1,0,1] if args.paper else [-1,-.5,0,.5,1])
    ax.spines[['right','top']].set_visible(False)
    ax.grid(axis='y',color='#E8E8E8',linewidth=.6)
axs[0].set_yticks([0,.5,1])
axs[1].set_yticks([1,1.5,2])
axs[1].legend(loc='upper center',frameon=False)
signed_checks = None
if args.paper:
    axs[0].legend(loc='lower center', frameon=False)
    ax = axs[2]
    # Y_DC = sigma'' I / 2. Both states use |sigma''| epsilon_0^2 / 2,
    # never their own signed central value, so normalization preserves sign.
    ax.plot(xi, quad_mean, color=colors[1], lw=2, label=r"$\sigma''>0$")
    ax.plot(xi, -quad_mean, color=colors[0], ls='--', lw=2, label=r"$\sigma''<0$")
    ax.axhline(0, color='#888888', lw=.7, zorder=0)
    ax.set(xlim=(-1,1), ylim=(-2.2,2.8), xlabel=r'$x/L_x$',
           ylabel=r"$Y_{\rm DC}/(|\sigma''|\varepsilon_0^2/2)$")
    ax.set_title('(c) Signed source', loc='left', pad=7)
    ax.set_xticks([-1,0,1]); ax.set_yticks([-2,0,2])
    ax.spines[['right','top']].set_visible(False)
    ax.legend(loc='upper center', frameon=False, handlelength=1.5)
    # A direct carrier-period average of the full sigmoid checks both signs.
    t = np.arange(65536) / 65536
    eps1, eps2, rho, v0 = .01, .006, .56, 6.
    s = eps1*np.cos(2*np.pi*100*t) + eps2*np.cos(2*np.pi*103*t)
    sigmoid = lambda v: 5/(1+np.exp(-rho*(v-v0)))
    signed_checks = []
    for baseline in [4., 8.]:
        z = sigmoid(baseline)/5
        curvature = 5*rho**2*z*(1-z)*(1-2*z)
        predicted = curvature*(eps1**2+eps2**2)/4
        measured = np.mean(sigmoid(baseline+s))-sigmoid(baseline)
        assert np.sign(predicted) == np.sign(measured)
        assert abs(measured/predicted-1) < 2e-5
        signed_checks.append(dict(baseline_mV=baseline,curvature=curvature,
                                  quadratic_prediction=predicted,full_sigmoid_mean_shift=measured))
fig.tight_layout(w_pad=1.3 if args.paper else 2.3)
sys.path.insert(0,'/Users/giulio/.agents/skills/figcheck/scripts')
import overlap
overlap.check(fig,placed_frac=.95 if args.paper else 1.0,name='ti_spatial_maps',min_pt=7.5)
fig.savefig(OUTPUT/(STEM+'.pdf'))
fig.savefig(OUTPUT/(STEM+'.png'),dpi=180)
check_path = (HERE.parents[1]/'docs/draft19_spatial_map_checks_2026-10-14.json'
              if args.paper else HERE/'map_checks.json')
record = {'integral_checks':checks,
    'center_means':{'envelope':float(env_mean[center]),'quadratic':float(quad_mean[center])},
    'edge_means':{'envelope':float(env_mean[0]),'quadratic':float(quad_mean[0])},
    'off_target_vs_target':{'envelope_modulation':.2,'quadratic_modulation':2.0}}
if args.paper:
    record.update(signed_rate_checks=signed_checks,
                  signed_panel_normalization="positive |sigma''| epsilon_0^2 / 2 for both signs",
                  signed_panel_values={'positive_center':1.,'negative_center':-1.,
                                       'positive_edges':2.,'negative_edges':-2.},
                  scope='Illustrative uniform-curvature source before recurrent feedback; not FEM or measured physiology')
check_path.write_text(json.dumps(record,indent=2)+'\n')
print('Spatial-map integrals and examples verified.')
