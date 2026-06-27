import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import colors as mcolors

def blend_hex_with_bg(hex_color, alpha, bg_color="#FFFFFF"):
    fg_rgb = np.array(mcolors.to_rgb(hex_color))
    bg_rgb = np.array(mcolors.to_rgb(bg_color))
    blended_rgb = alpha * fg_rgb + (1 - alpha) * bg_rgb
    return mcolors.to_hex(blended_rgb)


def colors_from_pt(pt_array, hex_color):
    """Same stability colouring as your original script: solid if PT<0, faded otherwise."""
    return np.where(pt_array < 0, hex_color, blend_hex_with_bg(hex_color, 0.7))


def plot_from_saved(fp_file='fp.pkl', lc1_file='lc1.pkl', lc2_file='lc2.pkl',
                     bfp_file='bfp.csv', blc1_file='blc1.csv',
                     out_png='jr_bif_reloaded.png'):
    fp_df = pd.read_pickle(fp_file)
    lc1_df = pd.read_pickle(lc1_file)
    lc2_df = pd.read_pickle(lc2_file)
    bfp_df = pd.read_csv(bfp_file)
    blc1_df = pd.read_csv(blc1_file)

    c_fp = colors_from_pt(fp_df['PT'].values, "#808080")
    c_lc1 = colors_from_pt(lc1_df['PT'].values, "#E2725B")
    c_lc2 = colors_from_pt(lc2_df['PT'].values, "#E2725B")

    plt.rcParams.update({'font.size': 12, 'figure.autolayout': True})
    fig, axs = plt.subplots(1, 1, figsize=(6, 6), dpi=300, constrained_layout=True)

    axs.scatter(fp_df['p'], fp_df['y1'] - fp_df['y2'], c=c_fp, s=1.5)
    axs.scatter(lc1_df['p'], lc1_df['y_min'], c=c_lc1, s=1.5)
    axs.scatter(lc1_df['p'], lc1_df['y_max'], c=c_lc1, s=1.5)
    axs.scatter(lc2_df['p'], lc2_df['y_min'], c=c_lc2, s=1.5)
    axs.scatter(lc2_df['p'], lc2_df['y_max'], c=c_lc2, s=1.5)

    for _, row in bfp_df.iterrows():
        axs.axvline(row['value'], color='black', ls='--', alpha=0.7)
        axs.text(row['value'] + 2.7, -5.0, row['label'], rotation=90)
    for _, row in blc1_df.iterrows():
        axs.axvline(row['value'], color='black', ls='--', alpha=0.7)
        axs.text(row['value'] + 1.5, -5.0, row['label'], rotation=90)

    axs.set_xlim(-80, 350.0)
    axs.set_ylim(-5.7, 12.45)
    axs.set_xlabel(r'$p$')
    axs.set_ylabel(r'$y2-y1$')
    fig.savefig(out_png, bbox_inches='tight')
    plt.show()
    return fig, axs


if __name__ == '__main__':
    plot_from_saved()
