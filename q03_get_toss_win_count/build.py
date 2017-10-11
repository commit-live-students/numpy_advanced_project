import numpy as np
from greyatomlib.numpy_advanced.q01_get_total_deliveries_players.build import ipl_matches_array

def get_toss_win_count(team = 'Mumbai Indians'):
    matchcode = ipl_matches_array[:,0]
    filter1 = (ipl_matches_array[:,5] == team)
    #print(filter1)
    a = matchcode[filter1]
    x = np.unique(a)
    return(len(x))
    
