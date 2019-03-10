# %load q01_get_total_deliveries_players/build.py
# Default imports
import numpy as np
import pandas as pd

# Your Solution
def get_total_deliveries_played(batsman):
    ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')
    deliveries= ipl_matches_array[:,13].astype(np.str)
    deliveries=deliveries[deliveries==batsman]
    return  deliveries.size
    


