# %load q03_get_toss_win_count/build.py
#Default Imports
import numpy as np
ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", skip_header=1, delimiter=",")

# Your Solution
def get_toss_win_count(team):
    tot_matchid = [ipl_matches_array[0][0]]
    total = 0
    for i in ipl_matches_array:
        if i[0] not in tot_matchid:
            tot_matchid.append(i[0])
    for j in ipl_matches_array:
        if team == j[5] and j[0] in tot_matchid:
            total = total + 1
            tot_matchid.remove(j[0])
    return total


count = get_toss_win_count('Mumbai Indians')
