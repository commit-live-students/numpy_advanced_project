# Default imports
import numpy as np

ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", skip_header=1, delimiter=",")

# Your Solution

def get_total_deliveries_played(batsman):
    count = 0
    ipl_batsman = ipl_matches_array[:,13]
    for item in ipl_batsman:
        if item == batsman:
            count += 1
    return count
