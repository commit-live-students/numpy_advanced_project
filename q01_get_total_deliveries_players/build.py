# Default imports
import numpy as np

ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", skip_header=1, delimiter=",")

# Your Solution

def get_total_deliveries_played(batsman):
    cnt=0
    for matches in ipl_matches_array:
        if matches[13] == batsman:
            cnt=cnt+1
    return cnt
