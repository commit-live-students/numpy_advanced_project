#Default Imports
import numpy as np
ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", skip_header=1, delimiter=",")


#Your Solution

def get_toss_win_count(team):
    toss_win = 0
    match_dict = {}

    for i in ipl_matches_array[:,[0,5]]:
        match_dict[i[0]] = i[1]

    for i in match_dict.values():
        if i == team:
            toss_win = toss_win + 1

    return toss_win
