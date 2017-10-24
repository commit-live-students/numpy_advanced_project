# %load q01_get_total_deliveries_players/build.py
# Default imports
import numpy as np

ipl_matches_array = np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", skip_header=1, delimiter=",")

list_1 = ipl_matches_array[:,13]
def get_total_deliveries_played(batsman):
    count = 0
    for i in list_1:
        if i == batsman:
            count = count + 1
    return count
