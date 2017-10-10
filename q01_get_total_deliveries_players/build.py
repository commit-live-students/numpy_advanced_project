# Default imports
# %load q01_get_total_deliveries_players/build.py
# Default imports
import numpy as np

def get_total_deliveries_played(batsman):
    ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50",skip_header=1, delimiter=",")
    a = ipl_matches_array[0:,13] == batsman
# Your Solution
    return int(len(ipl_matches_array[a]))
    
