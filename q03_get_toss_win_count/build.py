# %load q03_get_toss_win_count/build.py
#Default Imports
import numpy as np
ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')


#Your Solution
def get_toss_win_count(team):
    toss_winner_match = ipl_matches_array[:,[0,5]]
    filtered_index_team = np.where(toss_winner_match[:,1]==team)
    match_codes = toss_winner_match[filtered_index_team,0]
    unique_match_codes  = np.unique(match_codes)
    return len(unique_match_codes)
    #print(filtered_index)
    
get_toss_win_count(b'Mumbai Indians')


