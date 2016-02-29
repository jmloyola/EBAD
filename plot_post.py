from __future__ import division
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
from hdi import hdi_grid


def plot_post(param_sample_vec, cred_mass=0.95, comp_val=None,
              ROPE=None, ylab='', xlab='parameter', fontsize=14, labelsize=14,
              title='', framealpha=1, show_mode=True, bins=50, kde_plot=True, 
              roundto=2):
    """
    Write me!
    """        
    # colors taken from the default seaborn color pallete
    blue, green, red = [(0.2980392156862745, 0.4470588235294118, 
    0.6901960784313725), (0.3333333333333333, 0.6588235294117647, 
    0.40784313725490196), (0.7686274509803922, 0.3058823529411765, 
    0.3215686274509804)]

    post_summary = {'mean':0,'median':0,'mode':0, 'hdi_mass':0,'hdi_low':0,
                   'hdi_high':0, 'comp_val':0, 'pc_gt_comp_val':0, 'ROPE_low':0,
                   'ROPE_high':0, 'pc_in_ROPE':0}

    post_summary['mean'] = round(np.mean(param_sample_vec), roundto)
    post_summary['median'] = round(np.median(param_sample_vec), roundto)
    post_summary['hdi_mass'] = cred_mass

    # Compute the HDI, KDE and mode for the posterior
    hdi, x, y, modes = hdi_grid(param_sample_vec, cred_mass, roundto)
    post_summary['hdi'] = hdi
    post_summary['mode'] = modes

    ## Plot KDE.
    if kde_plot:
            plt.plot(x, y, color=blue)
    ## Plot histogram.
    else:
        plt.hist(param_sample_vec, normed=True, bins=bins, facecolor=blue, 
        edgecolor='w')

    ## Display mean or mode:
    if show_mode:
        string = '{:g} ' * len(post_summary['mode'])
        plt.plot(0, label='mode =' + string.format(*post_summary['mode']), alpha=0)
    else:
        plt.plot(0, label='mean = {:g}'.format(post_summary['mean']), alpha=0)
    ## Display the comparison value.
    if comp_val is not None:
        pc_gt_comp_val = round(100 * np.sum(param_sample_vec > comp_val)/len(param_sample_vec), roundto)
        pc_lt_comp_val = round(100 - pc_gt_comp_val, roundto)
        plt.axvline(comp_val, ymax=.75, color=green,
                 linestyle='--', linewidth=4,
                 label='{:g}% < {:g} < {:g}%'.format(pc_lt_comp_val, comp_val, pc_gt_comp_val))
        post_summary['comp_val'] = comp_val
        post_summary['pc_gt_comp_val'] = pc_gt_comp_val
    ## Display the ROPE.
    if ROPE is not None:
        pc_in_ROPE = round(np.sum((param_sample_vec > ROPE[0]) & (param_sample_vec < ROPE[1]))/len(param_sample_vec)*100, roundto)
        plt.axvline(ROPE[0], ymax=.75, color=red, linewidth=4,
                label='{:g}% in ROPE'.format(pc_in_ROPE))
        plt.axvline(ROPE[1], ymax=.75, color=red, linewidth=4)
        post_summary['ROPE_low'] = ROPE[0] 
        post_summary['ROPE_high'] = ROPE[1] 
        post_summary['pc_in_ROPE'] = pc_in_ROPE

    ## Display the HDI.
    hdi_label = ''
    for value in hdi:
        plt.plot(value, [0, 0], linewidth=8, color='k')
        hdi_label = hdi_label +  '{:g} {:g}\n'.format(round(value[0], roundto), round(value[1], roundto)) 
    plt.plot(0, 0, linewidth=8, color='k', label='HDI {:g}%\n{}'.format(cred_mass*100, hdi_label))

    plt.xlabel(xlab, fontsize=fontsize)
    plt.ylabel(ylab, fontsize=fontsize)
    plt.title(title, fontsize=fontsize)
    plt.legend(loc=0, fontsize=labelsize, framealpha=framealpha)
    frame = plt.gca()
    frame.axes.get_yaxis().set_ticks([])
    return post_summary
    

def meanplot(trace, vars=None, figsize=None, combined=False, grid=True, 
              alpha=1, ax=None):
    """Plot running means

    Parameters
    ----------

    trace : result of MCMC run
    vars : list of variable names
        Variables to be plotted, if None all variable are plotted
    figsize : figure size tuple
        If None, size is (12, num of variables * 2) inch
    combined : bool
        Flag for combining multiple chains into a single chain. If False
        (default), chains will be plotted separately.
    grid : bool
        Flag for adding gridlines to histogram. Defaults to True.
    ax : axes
        Matplotlib axes. Defaults to None.

    Returns
    -------

    ax : matplotlib axes

    """
    import matplotlib.pyplot as plt
    if vars is None:
        vars = trace.varnames

    n = len(vars)

    if figsize is None:
        figsize = (6, n*2)

    if ax is None:
        fig, ax = plt.subplots(n, 1, figsize=figsize, squeeze=False)

    for i, v in enumerate(vars):
        for d in trace.get_values(v, combine=combined, squeeze=False):
            rm = np.cumsum(d)/np.arange(1, len(d)+1)
            ax[i, 0].plot(rm)
            ax[i, 0].axhline(d.mean(), color="r", lw=1.5, alpha=alpha)
            ax[i, 0].set_title(str(v))
            ax[i, 0].grid(grid)

            ax[i, 0].set_ylabel("mean")
            ax[i, 0].set_xlabel("iteration")

    plt.tight_layout()
    return ax


