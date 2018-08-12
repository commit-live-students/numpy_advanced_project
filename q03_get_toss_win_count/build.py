#Default Imports
import numpy as np
ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", skip_header=1, delimiter=",")
def get_toss_win_count(team):
    data = ipl_matches_array[:,[0,5]]
    unique_matches = np.unique(data[:,0])
    toss = []
    for d in unique_matches:
        toss.append(ipl_matches_array[data[:,0] == d,5][0])

    return toss.count(team)

#Your Solution
