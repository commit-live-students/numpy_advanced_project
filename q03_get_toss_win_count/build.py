# %load q03_get_toss_win_count/build.py
#Default Imports
import numpy as np
from greyatomlib.numpy_advanced.q01_get_total_deliveries_players.build import ipl_matches_array
#tosses = ipl_matches_array[:,15]

def get_toss_win_count(team ='Mumbai Indians'):
    match = ipl_matches_array[:,[0,5]]
    toss = []
    for i,j in match:
        if j == team:
            toss.append(i)
    return np.count_nonzero(np.unique(toss))


    
