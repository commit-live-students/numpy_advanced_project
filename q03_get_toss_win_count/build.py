# %load q03_get_toss_win_count/build.py
#Default Imports
import numpy as np
from greyatomlib.numpy_advanced.q01_get_total_deliveries_players.build import ipl_matches_array

def get_toss_win_count(team='Mumbai Indians'):
    tossWinerFilter=ipl_matches_array[:,5]==team
    filterArray=ipl_matches_array[tossWinerFilter]
    unique_match_code= np.count_nonzero(np.unique(filterArray[:,0]))
    return unique_match_code
