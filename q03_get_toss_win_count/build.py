import numpy as np#Default Imports
from greyatomlib.numpy_advanced.q01_get_total_deliveries_players.build import ipl_matches_array

def get_toss_win_count(team = 'Mumbai Indians'):
    b = (ipl_matches_array[:,5] == team)
    c = np.unique(np.array(ipl_matches_array[:,0][b])).size
    return c
