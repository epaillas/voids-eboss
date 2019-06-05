import numpy as np
from astropy import units as units
from astropy.cosmology import Planck15 as cosmo
import matplotlib.pyplot as plt
import sys

if len(sys.argv) != 6:
    print('Some arguments are missing.')
    print('1) outfile')
    print('2) random_catalogue')
    print('3) zlow')
    print('4) zhigh')
    print('5) number_density (in Mpc/h)')
    sys.exit()

print('----------')
print('Running generate_random_sphere.py')

outfile = sys.argv[1]
rand = sys.argv[2]
zlo = sys.argv[3]
zhi = sys.argv[4]
nden = sys.argv[5]

zlo = float(zlo)
zhi = float(zhi)
nden = float(nden)

rand = np.genfromtxt(rand)
ralo = rand[:,0].min()
rahi = rand[:,0].max()
declo = rand[:,1].min()
dechi = rand[:,1].max()

rhi = cosmo.comoving_distance(zhi).value * cosmo.h
rlo = cosmo.comoving_distance(zlo).value * cosmo.h
vol = 4/3 * np.pi * (rhi**3)

npoints = int(vol * nden)

print('Number of points in the whole random sphere: ' + repr(npoints))

ralist = []
declist = []
rlist = []
zlist = []

for i in range(npoints):
    print((repr(i/npoints*100))[:4] + '%', end='\r')

    ra = np.random.uniform(0, 2*np.pi)
    cosdec = np.random.uniform(-1, 1)
    dec = np.arccos(cosdec)
    u = np.random.uniform(0, 1)
    z = u ** (1/3)

    if (ralo < ra < rahi) and (declo < dec < dechi) and (zlo < z < zhi):
        r = cosmo.comoving_distance(z).value
        ralist.append(ra)
        declist.append(dec)
        rlist.append(r)
        zlist.append(z)

print('len(data) after cutoff: ' + repr(len(ralist)))

ralist = np.asarray(ralist).reshape(len(ralist), 1)
declist = np.asarray(declist).reshape(len(declist), 1)
rlist = np.asarray(rlist).reshape(len(rlist), 1)
zlist = np.asarray(zlist).reshape(len(zlist), 1)

data = np.hstack([ralist, declist, rlist, zlist])

if '.npy' in outfile:
    np.save(outfile, data)
else:
    np.savetxt(outfile, data)
