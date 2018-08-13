# %load q03_get_toss_win_count/build.py
#Default Imports
import numpy as np
ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')


def get_toss_win_count(team):
    toss_decision = ipl_matches_array[:,[0,5]] #to access the column in numpy
    match_codes = toss_decision[toss_decision[:,1]==team]
    winner_team = np.unique(match_codes[:,0])
    final_answer = winner_team.size
    return final_answer

