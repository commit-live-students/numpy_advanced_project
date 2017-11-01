# Default imports
import numpy as np

ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", skip_header=1, delimiter=",")
#print np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", delimiter=",")[0]
#print ipl_matches_array[:5]
#print  ipl_matches_array.shape[0]
# Your Solution
def get_total_deliveries_played(batsman):
    deliveries_played = ipl_matches_array[ipl_matches_array[:,13] == batsman]
    return deliveries_played.shape[0]

#print get_total_deliveries_played ('SR Tendulkar')
