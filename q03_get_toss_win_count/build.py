# %load q03_get_toss_win_count/build.py
#Default Imports
import numpy as np
ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')

def get_toss_win_count(team):
    toss_wins=ipl_matches_array[ipl_matches_array[:,5]==team]
    toss_wins_count=len(set(toss_wins[:,0]))
    return toss_wins_count
toss_wins=ipl_matches_array[ipl_matches_array[:,5]==b'Mumbai Indians']
set(toss_wins[:,0])
get_toss_win_count(b'Rajasthan Royals')


