#Default Imports
import numpy as np
ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", skip_header=1, delimiter=",")


#Your Solution
team='Mumbai Indians'
def get_toss_win_count(team):
    match=ipl_matches_array[:,0]
    tosses_won=ipl_matches_array[:,7]
    match_tosses_won=np.column_stack((match,tosses_won))
    count_win=len(np.unique(match_tosses_won[np.where(match_tosses_won[:,1:]==team)]))
    return count_win
