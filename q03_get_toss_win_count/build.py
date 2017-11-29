#Default Imports
from greyatomlib.numpy_advanced.q01_get_total_deliveries_players.build import ipl_matches_array
import numpy as np
#Your Solution
def get_toss_win_count(team='Mumbai Indians'):
    matches=ipl_matches_array[:,1:2]

    return np.unique(matches[ipl_matches_array[:, 5:6] == team]).size
