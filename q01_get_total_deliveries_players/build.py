# %load q01_get_total_deliveries_players/build.py
# Default imports
import numpy as np

ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')
batsman=ipl_matches_array[0,13].astype(np.str)
# Your Solution
def get_total_deliveries_played(batsman=ipl_matches_array[0,13].astype(np.str)):
    total_delivery_bool=ipl_matches_array[:,13].astype(np.str)==batsman
    arr=ipl_matches_array[:,13][total_delivery_bool]
    return np.count_nonzero(arr)


