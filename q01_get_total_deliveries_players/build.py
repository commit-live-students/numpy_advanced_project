# Default imports
import numpy as np

ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", skip_header=1, delimiter=",")
bats = ipl_matches_array[:,13]
def get_total_deliveries_played(batsman):
    return len(bats[bats==batsman])
