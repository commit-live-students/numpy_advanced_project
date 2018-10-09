# %load q03_get_toss_win_count/build.py
#Default Imports
import numpy as np
ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')


def get_toss_win_count(team):
    toss_win=ipl_matches_array[:,5]==team
    unique_win_count=np.unique(ipl_matches_array[toss_win,0])
    return np.count_nonzero(unique_win_count)


get_toss_win_count(b'Mumbai Indians')

