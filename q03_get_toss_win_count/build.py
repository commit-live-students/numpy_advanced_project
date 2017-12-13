#Default Imports
import numpy as np
from greyatomlib.numpy_advanced.q01_get_total_deliveries_players.build import ipl_matches_array

#Your Solution
def get_toss_win_count(team):
    data=ipl_matches_array[:,0]
    count=np.unique(data[ipl_matches_array[:,5]==team]).size
    return count
