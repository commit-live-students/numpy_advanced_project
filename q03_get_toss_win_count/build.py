# %load q03_get_toss_win_count/build.py
#Default Imports
import numpy as np
ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')


#Your Solution
def get_toss_win_count(team):
    toss_won = ipl_matches_array[:,5]
    toss_filter = toss_won==team
    return len(set(toss_filter))


