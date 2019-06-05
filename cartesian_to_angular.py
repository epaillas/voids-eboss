import numpy as np
import sys
from astropy.cosmology import Planck15, z_at_value
import astropy.units as u

if len(sys.argv) != 3:
    print('Some arguments are missing.')
    print('1) input_data')
    print('2) output_data')
    sys.exit()

print('----------')
print('Running cartesian_to_angular.py')

fin = sys.argv[1]
fout = sys.argv[2]

print('input_data: ' + fin)
print('output_data: ' + fout)

if '.npy' in fin:
    data = np.load(fin)
else:
    data = np.genfromtxt(fin)

# Switch back to angular coordinates
dis = np.sqrt(data[:,0]**2 + data[:,1]**2 + data[:,2]**2)
dec = np.arctan2(np.sqrt(data[:,0]**2 + data[:,1]**2), data[:,2])
ra = np.arctan2(data[:,1], data[:,0])

if np.shape(data)[1] == 4:
    z = data[:,3]
else:
    zmin = z_at_value(Planck15.comoving_distance, dis.min() * u.Mpc)
    zmax = z_at_value(Planck15.comoving_distance, dis.max() * u.Mpc)
    zgrid = np.logspace(np.log10(zmin), np.log10(zmax), 50)
    dgrid = Planck15.comoving_distance(zgrid)
    z = np.interp(dis, dgrid.value, zgrid)

dis = np.reshape(dis, (len(dis), 1))
dec = np.reshape(dec, (len(dec), 1))
ra = np.reshape(ra, (len(ra), 1))
z = np.reshape(z, (len(z), 1))

data_out = np.hstack([ra, dec, dis, z])

if '.npy' in fout:
    np.save(fout, data_out)
else:
    np.savetxt(fout, data_out)
