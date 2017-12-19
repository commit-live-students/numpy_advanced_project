#Default Imports
import numpy as np
from greyatomlib.numpy_advanced.q01_get_total_deliveries_players.build import ipl_matches_array

#Your Solution
def get_toss_win_count(team_Name):
    toss_won=ipl_matches_array[ipl_matches_array[:,5]==team_Name]
    return len(np.unique(toss_won[:,0]))
