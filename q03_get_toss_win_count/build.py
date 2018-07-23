# %load q03_get_toss_win_count/build.py
#Default Imports
import numpy as np
ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')


#Your Solution
def get_toss_win_count(team):
    toss_winner=ipl_matches_array[:,5]==team
    match_codes=ipl_matches_array[:,0].astype('float64')
    count=len(set(match_codes[toss_winner]))
    return count

