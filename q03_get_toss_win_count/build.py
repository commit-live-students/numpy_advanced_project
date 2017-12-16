#Default Imports
from greyatomlib.numpy_advanced.q01_get_total_deliveries_players.build import ipl_matches_array

import numpy as np
#Your Solution

def get_toss_win_count(team):

    teams = ipl_matches_array[:,5]
    matches = ipl_matches_array[:,0]

    count = np.unique(matches[teams == team]).size

    #count = np.unique(matches[ipl_matches_array[:,5] == team]).size
    #print count
    #print matches

    return count
