# %load q03_get_toss_win_count/build.py
#Default Imports
import numpy as np
ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')
def get_toss_win_count(team):
    c = ipl_matches_array[ipl_matches_array[:,5] == team]
    count = np.unique(c[:,0]).shape[0]
    return count
#Your Solution
get_toss_win_count(b'Mumbai Indians')




