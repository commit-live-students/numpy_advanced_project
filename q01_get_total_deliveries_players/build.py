# Default imports
import numpy as np

ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", skip_header=1, delimiter=",")

# Your Solution
def get_total_deliveries_played(batsman):
    deliveries = ipl_matches_array[:, 13]
    deliveries_faced= np.where(deliveries == batsman) #, deliveries_faced = deliveries_faced + 1, 0 )
    return len(deliveries_faced[0])
