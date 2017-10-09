# %load q01_get_total_deliveries_players/build.py
# Default imports
import numpy as np

ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", skip_header=1, delimiter=",")

def get_total_deliveries_played(batsman):
    x = list(ipl_matches_array[:,13])
    y = x.count(batsman)
    return(y)


# Your Solution
