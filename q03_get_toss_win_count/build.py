#Default Imports
import numpy as np
ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", skip_header=1, delimiter=",")


#Your Solution
def get_toss_win_count(team):
    team_match_code = ipl_matches_array[ipl_matches_array[:,5] == team][:,0]
    match_code = np.unique(team_match_code)
    return match_code.shape[0]

get_toss_win_count('Mumbai Indians')
