import numpy as np
import matplotlib.pyplot as plt
plt.style.use('enrique')

fig = plt.figure(figsize=(8,5))
ax = plt.subplot()
data = np.genfromtxt('/home/epaillasv/data/eboss_v5/test_pipeline/galaxy_cats/\
eBOSS_ELG_clustering_NGC_v5.dat.ang.txt')
ax.scatter(data[:,0], data[:,1], s=1.0, linewidth=0)
ax.set_xlabel('ra [rad]')
ax.set_ylabel('dec [rad]')
plt.savefig('/home/epaillasv/Dropbox/data/eboss_v5/fig/\
eBOSS_ELG_clustering_NGC_v5.dat.ang.png', format='png')


fig = plt.figure(figsize=(8,5))
ax = plt.subplot()
data = np.genfromtxt('/home/epaillasv/data/eboss_v5/test_pipeline/void_cats/\
eBOSS_ELG_clustering_NGC_v5.cenin.ang.txt')
ax.scatter(data[:,0], data[:,1], s=1.0, linewidth=0)
ax.set_xlabel('ra [rad]')
ax.set_ylabel('dec [rad]')
plt.savefig('/home/epaillasv/Dropbox/data/eboss_v5/fig/\
eBOSS_ELG_clustering_NGC_v5.cenin.ang.png', format='png')


fig = plt.figure(figsize=(8,5))
ax = plt.subplot()
data = np.load('/home/epaillasv/data/eboss_v5/test_pipeline/galaxy_cats/\
eBOSS_ELG_clustering_NGC_v5.angCap.ang.npy')
ax.scatter(data[:,0], data[:,1], s=1.0, linewidth=0)
data = np.load('/home/epaillasv/data/eboss_v5/test_pipeline/galaxy_cats/\
eBOSS_ELG_clustering_NGC_v5.redCap.ang.npy')
ax.scatter(data[:,0], data[:,1], s=1.0, linewidth=0)
ax.set_xlabel('ra [rad]')
ax.set_ylabel('dec [rad]')
plt.savefig('/home/epaillasv/Dropbox/data/eboss_v5/fig/\
eBOSS_ELG_clustering_NGC_v5.Cap.ang.png', format='png')




fig = plt.figure(figsize=(8,5))
ax = plt.subplot()
data = np.genfromtxt('/home/epaillasv/data/eboss_v5/test_pipeline/galaxy_cats/\
eBOSS_ELG_clustering_SGC_v5.dat.ang.txt')
ax.scatter(data[:,0], data[:,1], s=1.0, linewidth=0)
ax.set_xlabel('ra [rad]')
ax.set_ylabel('dec [rad]')
plt.savefig('/home/epaillasv/Dropbox/data/eboss_v5/fig/\
eBOSS_ELG_clustering_SGC_v5.dat.ang.png', format='png')


fig = plt.figure(figsize=(8,5))
ax = plt.subplot()
data = np.genfromtxt('/home/epaillasv/data/eboss_v5/test_pipeline/void_cats/\
eBOSS_ELG_clustering_SGC_v5.cenin.ang.txt')
ax.scatter(data[:,0], data[:,1], s=1.0, linewidth=0)
ax.set_xlabel('ra [rad]')
ax.set_ylabel('dec [rad]')
plt.savefig('/home/epaillasv/Dropbox/data/eboss_v5/fig/\
eBOSS_ELG_clustering_SGC_v5.cenin.ang.png', format='png')


fig = plt.figure(figsize=(8,5))
ax = plt.subplot()
data = np.load('/home/epaillasv/data/eboss_v5/test_pipeline/galaxy_cats/\
eBOSS_ELG_clustering_SGC_v5.angCap.ang.npy')
ax.scatter(data[:,0], data[:,1], s=1.0, linewidth=0)
data = np.load('/home/epaillasv/data/eboss_v5/test_pipeline/galaxy_cats/\
eBOSS_ELG_clustering_SGC_v5.redCap.ang.npy')
ax.scatter(data[:,0], data[:,1], s=1.0, linewidth=0)
ax.set_xlabel('ra [rad]')
ax.set_ylabel('dec [rad]')
plt.savefig('/home/epaillasv/Dropbox/data/eboss_v5/fig/\
eBOSS_ELG_clustering_SGC_v5.Cap.ang.png', format='png')
