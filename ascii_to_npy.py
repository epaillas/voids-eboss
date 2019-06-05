import numpy as np
import sys

if len(sys.argv) != 3:
    print('Some arguments are missing.')
    print('1) infile')
    print('2) outfile (.npy)')
    sys.exit()

infile = sys.argv[1]
outfile = sys.argv[2]

infile = np.genfromtxt(infile)
np.save(outfile, infile)
