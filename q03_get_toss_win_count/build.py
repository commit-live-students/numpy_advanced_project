#Default Imports
import numpy as np
from greyatomlib.numpy_advanced.q01_get_total_deliveries_players.build import ipl_matches_array

#Your Solution
def get_toss_win_count(team):
    matches = ipl_matches_array[ipl_matches_array[:,5] == team][:,0]
    #print matches
    return np.unique(matches).shape[0]

#print get_toss_win_count('Mumbai Indians')
