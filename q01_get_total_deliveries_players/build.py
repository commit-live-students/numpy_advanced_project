# Default imports
import numpy as np

ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", skip_header=1, delimiter=",")

# Your Solution
def get_total_deliveries_played(batsman):
    count=0
    for item in ipl_matches_array:
        if(batsman==item[13]):
            count+=1
    return int(count)
