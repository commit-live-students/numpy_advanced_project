#Default Imports
import numpy as np

ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv", delimiter=",", dtype="|S50", skip_header=1)

def get_toss_win_count(team):

    match = ipl_matches_array[:,[0,5]]
    data = {}
    count = 0

    for ele in match:
        match,team = ele
        data.update({match:team})

    for ele in data.values():

        if ele == 'Mumbai Indians':
            count += 1

    return count
