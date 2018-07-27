# %load q03_get_toss_win_count/build.py
#Default Imports
import numpy as np
ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')
def get_toss_win_count(team):
    toss_winners = ipl_matches_array[:,(0,5)]
    filtered_index = np.where (toss_winners[:,1]==team)
    match_codes_tossers_w = toss_winners[filtered_index][:,0]
    return len(np.unique(match_codes_tossers_w))

get_toss_win_count(b'Mumbai Indians')






