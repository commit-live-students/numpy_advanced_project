#Default Imports
from greyatomlib.numpy_advanced.q01_get_total_deliveries_players.build import ipl_matches_array
import numpy as np
import pandas as pd
#Your Solution
def get_toss_win_count(team = "Mumbai Indians"):
    flt_team = ipl_matches_array[:,5] == team
    count = len(np.unique(ipl_matches_array[flt_team][:,0]))
    #print count
    return count
