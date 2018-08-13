#Default Imports
import numpy as np
ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", skip_header=1, delimiter=",")


#Your Solution
def get_toss_win_count(team):
    toss_winner= ipl_matches_array[ipl_matches_array[0:,5]==team]
    return len(np.unique(toss_winner[0:,0]))
