#Default Imports
from greyatomlib.numpy_advanced.q01_get_total_deliveries_players.build import ipl_matches_array
import numpy as np
#Your Solution
def get_toss_win_count(team):
    toss_won = np.unique(ipl_matches_array[ipl_matches_array[:,5] == team][:,0])
    return len(toss_won)
