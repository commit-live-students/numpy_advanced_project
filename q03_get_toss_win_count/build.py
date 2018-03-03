#Default Imports
import numpy as np
ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", skip_header=1, delimiter=",")

def get_toss_win_count(team):
    toss_count = ipl_matches_array[:,5] == team
    team_won_array = ipl_matches_array[toss_count]
    return np.unique(team_won_array[:,0]).size

#get_toss_win_count('Mumbai Indians')
