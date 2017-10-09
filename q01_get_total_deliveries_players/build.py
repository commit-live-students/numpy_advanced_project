# Default imports
import numpy as np

ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", skip_header=1, delimiter=",")

def get_total_deliveries_played(batsman):
    flt_batsman = ipl_matches_array[:,13].astype("|S30") == batsman
    return len(ipl_matches_array[flt_batsman])

# Your Solution
