#Default Imports
import numpy as np
ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", skip_header=1, delimiter=",")

def get_toss_win_count(team = b'Mumbai Indains'):
        toss_win =ipl_matches_array[ipl_matches_array[:,5] == team]
        total_win_toss = set(toss_win[:,0])

        return len(total_win_toss)


get_toss_win_count(team = b'Mumbai Indains')
#Your Solution
