#Default Imports
import numpy as np
ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", skip_header=1, delimiter=",")


#Your Solution
def get_toss_win_count(team="Mumbai Indians"):
    matches = ipl_matches_array[:, 0:1]
    return np.unique(matches[ipl_matches_array[:, 5:6] == team]).size
