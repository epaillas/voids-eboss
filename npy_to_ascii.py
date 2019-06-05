import numpy as np
import sys

if len(sys.argv) != 3:
    print('Some arguments are missing.')
    print('1) infile (.npy)')
    print('2) outfile')
    sys.exit()

infile = sys.argv[1]
outfile = sys.argv[2]

infile = np.load(infile)
np.savetxt(outfile, infile)
