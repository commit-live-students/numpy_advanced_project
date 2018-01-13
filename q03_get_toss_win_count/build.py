#Default Imports
import numpy as np
ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", skip_header=1, delimiter=",")


#Your Solution
def get_toss_win_count(team):
    match = ipl_matches_array[:,:1]
    tosswin = ipl_matches_array[:,7:8]
    pair = np.hstack((match, tosswin))
    data = len(np.unique(pair[(np.where(pair[:,1:]==team))]))
    return data
