# Default imports
import sys, os
sys.path.append(os.path.join(os.path.dirname(os.curdir), '..','..'))

import numpy as np

def read_ipl_data(path, dtype=np.float64):
    return np.genfromtxt(path, dtype=dtype, skip_header=1, delimiter=",")

ipl_matches_array = read_ipl_data("../data/ipl_matches_small.csv", '|S50')



# Your Solution
def get_total_deliveries_played(batsman):
    batsman_array = ipl_matches_array[:, 13]
    batsman_filter = batsman_array == batsman
    total_deliveries = len(ipl_matches_array[batsman_filter])
    return total_deliveries