# %load q01_get_total_deliveries_players/build.py
# Default imports
import numpy as np

ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", skip_header=1, delimiter=",")

def get_total_deliveries_played(batsman):
    batsmanFilter=ipl_matches_array[:,13]==batsman
    filterArray=ipl_matches_array[batsmanFilter]
    total_runs=np.count_nonzero(filterArray[:,12])
    return total_runs
