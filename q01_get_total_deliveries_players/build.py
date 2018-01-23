# Default imports
import numpy as np

ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", skip_header=1, delimiter=",")

def get_total_deliveries_played(batsman):
    deliveries = 0
    for d in ipl_matches_array:
        if d[13] == batsman:
            deliveries += 1
    return deliveries
