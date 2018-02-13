#Default Imports
import numpy as np
ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", skip_header=1, delimiter=",")


#Your Solution
def get_toss_win_count(team):
    dic = {}
    toss_count = 0
    for i in ipl_matches_array[:,[0,5]]:
        if i[0] not in dic:
            dic[i[0]] = i[1]  # Make a dic of unique matches and toss winner team

    return len([x for x in dic.values() if x == team])
