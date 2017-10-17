#Default Imports
from greyatomlib.numpy_advanced.q01_get_total_deliveries_players.build import ipl_matches_array
import numpy as np
#Your Solution
def get_toss_win_count(team="Mumbai Indians"):
    data_filter = (ipl_matches_array[:,5] == team )
    data = ipl_matches_array[data_filter][:,[0]]
    return np.unique(data).shape[0]
