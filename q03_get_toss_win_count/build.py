# %load q03_get_toss_win_count/build.py
#Default Imports
from greyatomlib.numpy_advanced.q01_get_total_deliveries_players.build import ipl_matches_array
import numpy as np
#Your Solution
def get_toss_win_count(team):
    ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')
    arr=ipl_matches_array[:,0][ipl_matches_array[:,5].astype(np.str)==team]
    arr=np.unique(arr)
    return np.count_nonzero(arr)

