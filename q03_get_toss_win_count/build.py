#Default Imports
from greyatomlib.numpy_advanced.q01_get_total_deliveries_players.build import ipl_matches_array
import numpy as np
#Your Solution

ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", skip_header=1, delimiter=",")

def get_toss_win_count(team = "Mumbai Indians"):
    a = ipl_matches_array[:,5] == team
    b = ipl_matches_array[a]
    toss_count = len(np.unique(b[:,0]))
    return toss_count

#Your Solution
