#Default Imports
import numpy as np
from greyatomlib.numpy_advanced.q01_get_total_deliveries_players.build import ipl_matches_array
ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", skip_header=1, delimiter=",")
#Your Solution
def get_toss_win_count(team="Mumbai Indians"):
    toss = ipl_matches_array[0:,5] == team
    return len(ipl_matches_array[toss])
