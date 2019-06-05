import numpy as np
import matplotlib.pyplot as plt
plt.style.use('enrique')

fig = plt.figure(figsize=(8,5))
ax = plt.subplot()

# data = np.genfromtxt('/home/epaillasv/data/eboss_v5/test_pipeline/galaxy_cats/\
# eBOSS_LRG_clustering_NGC_v5.dat.car.txt')
# ax.scatter(data[:,0], data[:,1], s=1.0, linewidth=0)
# ax.set_xlabel('x [Mpc/h]')
# ax.set_ylabel('y [Mpc/h]')
# plt.savefig('/home/epaillasv/Dropbox/data/eboss_v5/fig/\
# eBOSS_LRG_clustering_NGC_v5.dat.car.png', format='png')
#
#
# fig = plt.figure(figsize=(8,5))
# ax = plt.subplot()
# data = np.genfromtxt('/home/epaillasv/data/eboss_v5/test_pipeline/void_cats/\
# eBOSS_LRG_clustering_NGC_v5.cenin.car.txt')
# ax.scatter(data[:,0], data[:,1], s=1.0, linewidth=0)
# ax.set_xlabel('x [Mpc/h]')
# ax.set_ylabel('y [Mpc/h]')
# plt.savefig('/home/epaillasv/Dropbox/data/eboss_v5/fig/\
# eBOSS_LRG_clustering_NGC_v5.cenin.car.png', format='png')


data = np.load('/home/epaillasv/data/eboss_v5/test_pipeline/galaxy_cats/\
eBOSS_LRG_clustering_NGC_v5.angCap.car.npy')
ax.scatter(data[:,0], data[:,1], s=1.0, linewidth=0)
data = np.load('/home/epaillasv/data/eboss_v5/test_pipeline/galaxy_cats/\
eBOSS_LRG_clustering_NGC_v5.redCap.car.npy')
ax.scatter(data[:,0], data[:,1], s=1.0, linewidth=0)
ax.set_xlabel('x [Mpc/h]')
ax.set_ylabel('y [Mpc/h]')
plt.savefig('/home/epaillasv/Dropbox/data/eboss_v5/fig/\
eBOSS_LRG_clustering_NGC_v5.Cap.car.png', format='png')
