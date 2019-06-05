import numpy as np
import sys
import healpy as hp

if len(sys.argv) != 5:
    print('Some arguments are missing.')
    print('1) random_catalogue (in)')
    print('2) sphere_catalogue (in)')
    print('3) redshift_cap (out)')
    print('4) angular_cap (out)')
    sys.exit()

print('----------')
print('Running generate_guard_particles.py')

random_cat = sys.argv[1]
sphere_cat = sys.argv[2]
redshift_cap = sys.argv[3]
angular_cap = sys.argv[4]

print('random_cat: ' + random_cat)
print('sphere_cat: ' + sphere_cat)
print('redshift_cap: ' + redshift_cap)
print('angular_cap: ' + angular_cap)

if '.npy' in random_cat:
    random_cat = np.load(random_cat)
else:
    random_cat = np.genfromtxt(random_cat)

# Construct HEALPIX mask of randoms
nside = 512
npix = hp.nside2npix(nside)
mask = np.zeros(npix)
ind = hp.pixelfunc.ang2pix(nside, random_cat[:,1], random_cat[:,0], nest=False)
mask[ind] = 1

indarray = [i for i in range(npix)]
neigh = hp.pixelfunc.get_all_neighbours(nside, indarray, nest=False).T

border = np.zeros(npix)
for i in range(npix):
    count = 0
    for j in range(8):
        ind = neigh[i, j]
        if mask[ind] == 0:
            count = count + 1
    if 0 < count < 8:
        border[i] = 1

if '.npy' in sphere_cat:
    sphere_cat = np.load(sphere_cat)
else:
    sphere_cat = np.genfromtxt(sphere_cat)

ind = hp.pixelfunc.ang2pix(nside, sphere_cat[:,1], sphere_cat[:,0], nest=False)
angCap = sphere_cat[border[ind] == 1]
redCap = sphere_cat[mask[ind] == 1]

angCap = [i for i in angCap if (0.6 < i[3] < 1.0)]
redCap = [i for i in redCap if (0.6 < i[3] < 0.605) or (0.995 < i[3] < 1.0)]
angCap = np.asarray(angCap)
redCap = np.asarray(redCap)

if '.npy' in redshift_cap:
    np.save(redshift_cap, redCap)
else:
    np.savetxt(redshift_cap, redCap)

if '.npy' in angular_cap:
    np.save(angular_cap, angCap)
else:
    np.savetxt(angular_cap, angCap)
