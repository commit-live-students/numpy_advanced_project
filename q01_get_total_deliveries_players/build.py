# Default imports
import numpy as np

ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", skip_header=1, delimiter=",")

# Your Solution
def get_total_deliveries_played(batsman):
    data = ipl_matches_array[:,13]
    deliveries_played = 0
    for p in data:
        if p == batsman:
            deliveries_played +=1
    return deliveries_played        
