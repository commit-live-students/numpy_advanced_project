# Default imports
import sys, os
sys.path.append(os.path.join(os.path.dirname(os.curdir), '..','..'))

import numpy as np

def read_ipl_data(path, dtype=np.float64):
    return np.genfromtxt(path, dtype=dtype, skip_header=1, delimiter=",")

ipl_matches_array = read_ipl_data("../data/ipl_matches_small.csv", '|S50')



# Your Solution
