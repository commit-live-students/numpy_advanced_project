# %load q01_get_total_deliveries_players/build.py
# Default imports

import numpy as np

ipl_matches_array = np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')
count = 0
# Your Solution

def get_total_deliveries_played(batsman):
    
    
    ipl_batsman = ipl_matches_array[0:,13].astype(str) == batsman
    return sum(ipl_batsman)

get_total_deliveries_played('SR Tendulkar')
       






