#Default Imports
import numpy as np
ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", skip_header=1, delimiter=",")


#Your Solution
def get_toss_win_count(team):
    match_team = ipl_matches_array[:,[0,5]]
    unique_matches = np.vstack({tuple(e) for e in match_team})
    unique , counts = np.unique(unique_matches, return_counts= True)
    team_toss_win = dict(zip(unique,counts))
    tosses_won =  team_toss_win[team]
    return tosses_won
get_toss_win_count('Mumbai Indians')    
