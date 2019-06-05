import numpy as np
import sys

if len(sys.argv) != 5:
    print('Some arguments are missing.')
    print('1) data_catalogue')
    print('2) angular_cap')
    print('3) redshift_cap')
    print('4) output_file')
    sys.exit()

print('----------')
print('Running join_guards_and_data.py')

data = sys.argv[1]
angCap = sys.argv[2]
redCap = sys.argv[3]
outfile = sys.argv[4]

print('data_catalogue: ' + data)
print('angCap: ' + angCap)
print('redCap: ' + redCap)
print('outfile: ' + outfile)

if '.npy' in data:
    data = np.load(data)
else:
    data = np.genfromtxt(data)

if '.npy' in angCap:
    angCap = np.load(angCap)
else:
    angCap = np.genfromtxt(angCap)

if '.npy' in redCap:
    redCap = np.load(redCap)
else:
    redCap = np.genfromtxt(redCap)

cat = np.vstack([data,angCap, redCap])

if '.npy' in outfile:
    np.save(outfile, cat)
else:
    np.savetxt(outfile, cat)
