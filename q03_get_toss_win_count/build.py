# %load q03_get_toss_win_count/build.py
#Default Imports
import numpy as np
ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')


#Your Solution
def get_toss_win_count(teams):
    toss_winner = ipl_matches_array[:,(0,5)]
    filtered_index = np.where(toss_winner[:,1]==teams)
    match_code = toss_winner[filtered_index][:,0]
    return len(np.unique(match_code))

get_toss_win_count(b'Mumbai Indians')



