import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

plt.style.use('enrique')

def bin_centres(bin_edges):
    return np.asarray([(bin_edges[i] + bin_edges[i + 1]) / 2.\
    for i in range(len(bin_edges) - 1)])

def plot_abundance(data, ax, bins, label=None,
                   linestyle='-', color='k', error=False):

    hist, bin_edges = np.histogram(data, bins=bins)
    n = hist
    r = bin_centres(bin_edges)
    n = n / np.diff(np.log10(bin_edges))

    if error:
        err = hist
        err = np.sqrt(err) / np.diff(np.log10(bin_edges))
        errplus = n + err
        errminus = n - err

    if error:
        ax.fill_between(r, errplus, errminus, color='#AAAAAA')

    ax.plot(r, n, linestyle=linestyle, label=label,\
    linewidth=2.0, color=color)
    return

data = np.genfromtxt('/home/epaillasv/data/eboss_v5/void_cats/step3/\
eBOSS_LRG_clustering_NGC_v5.step3.v90.car.txt')

fig = plt.figure()
ax = plt.subplot()

minr = data[:,3].min()
maxr = data[:,3].max()

bins = np.logspace(np.log10(minr), np.log10(maxr), 20)
plot_abundance(data=data[:,3], ax=ax, bins=bins, error=True)

ax.set_xlabel(r'$R_{\rm{eff}}\ \left[ \rm{Mpc} \right]$', fontsize=17)
ax.set_ylabel(r'$\rm{dN}\ / \rm{d} log(R_{eff})$',
fontsize=17)

plt.tight_layout()
plt.savefig('/home/epaillasv/Dropbox/data/eboss_v5/fig/void_abundance.pdf',
 format='pdf')
