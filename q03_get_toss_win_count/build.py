#Default Imports
import numpy as np
ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", skip_header=1, delimiter=",")


#Your Solution
def get_toss_win_count(team):
    data = ipl_matches_array
    x = [i[0] for i in data if i[5] == team]
    matches = set(x)
    count = len(matches)
    return count
#print get_toss_win_count('Mumbai Indians')
