# %load q03_get_toss_win_count/build.py
#Default Imports
from greyatomlib.numpy_advanced.q01_get_total_deliveries_players.build import ipl_matches_array
import numpy as np
#Your Solution
ipl_matches_array = ipl_matches_array.astype(np.str)
def get_toss_win_count(team):
    return np.unique(ipl_matches_array[ipl_matches_array[:,5] == 'Mumbai Indians'][:,0]).size
get_toss_win_count('Mumbai Indians')

