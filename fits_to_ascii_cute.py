import numpy as np
import astropy.io.fits as fits
from astropy.cosmology import Planck15 as cosmo
from astropy import units as u
import sys

if len(sys.argv) != 3:
    print('Some arguments are missing.')
    print('1) input_data')
    print('2) output_data')
    sys.exit()

# Read data catalogue
fin = sys.argv[1]
fout = sys.argv[2]
hdul = fits.open(fin)
data = hdul[1].data
print('input_data: ' + fin)
print('output_data: ' + fout)

ra = (data['RA'] - 90)
ind = ra > 360
ra[ind] -= 360
ind = ra < 0
ra[ind] += 360

dec = 90 - data['DEC']
z = data['Z']

ra = np.reshape(ra, (len(ra), 1))
dec = np.reshape(dec, (len(dec), 1))
z = np.reshape(z, (len(z), 1))

data_out = np.hstack([ra, dec, z])

np.savetxt(fout, data_out)
