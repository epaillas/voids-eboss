import numpy as np
import matplotlib.pyplot as plt

plt.style.use('enrique')

ELG = np.genfromtxt('/Users/epaillas/data/eboss_v5/galaxy_cats/nbar_eBOSS_ELG_v5.dat')
LRG_N = np.genfromtxt('/Users/epaillas/data/eboss_v5/galaxy_cats/nbar_eBOSS_LRG_NGC_v5.dat')
LRG_S = np.genfromtxt('/Users/epaillas/data/eboss_v5/galaxy_cats/nbar_eBOSS_LRG_SGC_v5.dat')

fig = plt.figure()
ax = plt.subplot()

ax.plot(ELG[:,0], ELG[:,3]/1e-4, label='ELG', linestyle='-', lw=2.0)
ax.plot(LRG_N[:,0], LRG_N[:,3]/1e-4, label='LRG NGC', linestyle='--', lw=2.0)
ax.plot(LRG_S[:,0], LRG_S[:,3]/1e-4, label='LRG SGC', linestyle=':', lw=2.0)

ax.set_xlim(0.6, 1.1)
ax.set_ylim(0, 6.8)
ax.set_xlabel(r'$z$', fontsize=17)
ax.set_ylabel(r'$n(z)\ \left[ 10^{-4}\ h^{3}\rm{Mpc^{-3}} \right]$', fontsize=17)

ax.tick_params(which='both', labelsize=15)
ax.tick_params(which='both', labelsize=15)
ax.legend(fontsize=15)
plt.tight_layout()

plt.savefig('/Users/epaillas/Dropbox/data/eboss_v5/fig/nbar.pdf')
plt.show()
