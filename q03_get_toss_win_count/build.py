# %load q03_get_toss_win_count/build.py
#Default Imports
import numpy as np
ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')

def get_toss_win_count(team):
    return np.unique(ipl_matches_array[:,0][ipl_matches_array[:,5].astype(np.str)==team].astype(str)).size



