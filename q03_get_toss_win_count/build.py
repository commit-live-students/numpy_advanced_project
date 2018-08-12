#Default Imports
import numpy as np
ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", skip_header=1, delimiter=",")



team = ''
def get_toss_win_count(team):
    a = ipl_matches_array
    b = a[:,[0,5]]
    c = b[b[:,1] == team][:,0]
    variable = np.unique(c)
    return len(variable)

print get_toss_win_count(team)
