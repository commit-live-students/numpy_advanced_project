# Default imports
import numpy as np

# Your Solution
def get_total_deliveries_played(batsman):
    ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", skip_header=1, delimiter=",")
    return np.count_nonzero(ipl_matches_array[:,13] == batsman)
