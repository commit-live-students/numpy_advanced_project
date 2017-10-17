# Default imports
import numpy as np

ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", skip_header=1, delimiter=",")

# Your Solution
def get_total_deliveries_played(batsman):
    total_deliveries = 0
    for item in ipl_matches_array:
        if item[13] == batsman:
            total_deliveries +=1
    #print list(ipl_matches_array[0]).index('batsman')
    return total_deliveries
