#Default Imports
from greyatomlib.numpy_advanced.q01_get_total_deliveries_players.build import ipl_matches_array

#Your Solution
import numpy as np
#Your Solution

def get_toss_win_count(team='Mumbai Indians'):
    ipl_matches_array_toss_mum = ipl_matches_array[ipl_matches_array[:,5]=='Mumbai Indians']
    combs = ipl_matches_array_toss_mum[:,[0,5]]

    b = np.vstack({tuple(row) for row in combs})
    return b.shape[0]
