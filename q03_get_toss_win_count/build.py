#Default Imports
import numpy as np
ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", skip_header=1, delimiter=",")


#Your Solution
def get_toss_win_count(teamname):
    n1 = np.where(ipl_matches_array[:,5] == teamname)
    return np.unique(ipl_matches_array[n1,0]).size
