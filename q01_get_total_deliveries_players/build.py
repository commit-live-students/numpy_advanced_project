# Default imports
import numpy as np

ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", skip_header=1, delimiter=",")

# Your Solution

def get_total_deliveries_played(batsman):
    array = ipl_matches_array[:,[11,13]]
    a_grp = array[array[:] == batsman]

    return np.count_nonzero(a_grp)
