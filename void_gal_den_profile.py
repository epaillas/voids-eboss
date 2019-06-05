import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator
from matplotlib.ticker import FormatStrFormatter
from scipy import stats

def get_mean_profile(data, rmin, rmax):
    subsample = np.asarray([i for i in data if (rmin <= i[0] <= rmax)
    and np.all(np.isfinite(i))])
    return np.mean(subsample[:, 1:], axis=0)

def get_sem_profile(data, rmin, rmax):
    subsample = np.asarray([i for i in data if rmin <= i[0] <= rmax
    and np.all(np.isfinite(i))])
    return stats.sem(subsample[:, 1:], axis=0)

plt.style.use('enrique')

fin = '/home/epaillasv/data/eboss_v5/void_cats/step3/\
eBOSS_LRG_clustering_NGC_v5.step3.v90.gal_den_profile'

fig = plt.figure()
ax = plt.subplot()

drange = [0, 500]

data = np.genfromtxt(fin, skip_header=1)
bins = np.genfromtxt(fin, skip_footer=len(data))

mean = get_mean_profile(data, drange[0], drange[1])
sem = get_sem_profile(data, drange[0] , drange[1])

ax.fill_between(bins, mean - sem, mean+sem, color='#AAAAAA')
ax.plot(bins, mean)

ax.set_ylabel(r'$n(r)\ /\ \overline{n}$', fontsize=17)
ax.set_xlabel(r'$r\ /\ R_{\rm{eff}}$', fontsize=17)
ax.tick_params(which='both', width=1.0, labelsize=15)

ax.set_xlim(0,3)
plt.tight_layout()
plt.savefig('/home/epaillasv/Dropbox/data/eboss_v5/fig/void_gal_den_profile.pdf',
 format='pdf')
plt.show()
