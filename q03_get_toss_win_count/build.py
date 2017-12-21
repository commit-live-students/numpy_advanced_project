# %load q03_get_toss_win_count/build.py
#Default Imports
import numpy as np
ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", skip_header=1, delimiter=",")


#Your Solution
def get_toss_win_count(team):
    toss = ipl_matches_array[:,5:6]
    stack =len(toss[np.where((toss==team,1))])
    return stack
