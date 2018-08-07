# %load q03_get_toss_win_count/build.py
#Default Imports
import numpy as np
ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')

#Your Solution
def get_toss_win_count(team):
    toss_winners_data = ipl_matches_array[:,(0, 5)]
    toss_winner_index = np.where(toss_winners_data[:,1] == team)
    toss_winner_match_code = toss_winners_data[toss_winner_index][:,0]

    return len(np.unique(toss_winner_match_code))
    
print(get_toss_win_count(b'Mumbai Indians'))


