#Default Imports
import numpy as np
from greyatomlib.numpy_advanced.q01_get_total_deliveries_players.build import ipl_matches_array

def get_toss_win_count(team ="Mumbai Indians"):
    ipl_match = ipl_matches_array[:,[0,5]]
    one = ipl_match[ipl_match[:,1] == "Mumbai Indians"]
    two = np.unique(one[:,0])
    final = len(two)
    return final
