#Default Imports
from greyatomlib.numpy_advanced.q01_get_total_deliveries_players.build import ipl_matches_array
import numpy as np
#Your Solution
def get_toss_win_count(team='Mumbai Indians'):
    array = ipl_matches_array[:,[0,5]]
    #print array
    a_grp = array[array[:,1] == team]
    uni = a_grp[:,0]
    uni = np.unique(uni)
    return np.count_nonzero(uni)
