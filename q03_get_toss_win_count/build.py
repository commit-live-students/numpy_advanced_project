# %load q03_get_toss_win_count/build.py
#Default Imports
from greyatomlib.numpy_advanced.q01_get_total_deliveries_players.build import ipl_matches_array
import numpy as np
#Your Solution

def get_toss_win_count(team='Mumbai Indians'):

    match_code=ipl_matches_array[:,0]
    toss_winner=ipl_matches_array[:,5].astype(np.str)==team
    #match_winner = ipl_matches_array[:,7].astype(np.str)=='Mumbai Indians'
    #toss_decision=ipl_matches_array[:,6]
    #print(len(match_winner[toss_winner]))
    win_code =len({win_match_code for win_match_code in match_code[ toss_winner]})

    return win_code



#get_toss_win_count()
