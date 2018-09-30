# %load q03_get_toss_win_count/build.py
#Default Imports
import numpy as np
ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')


#Your Solution
def get_toss_win_count(team):
    indx=ipl_matches_array[:,0].astype(np.int64)
    mtch=ipl_matches_array[:,5].astype(np.unicode_)
    return int(np.count_nonzero(np.unique(indx[(mtch==team)])))   
get_toss_win_count('Mumbai Indians')


