#Default Imports
from greyatomlib.numpy_advanced.q01_get_total_deliveries_players.build import ipl_matches_array
import numpy as np

ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", skip_header=1, delimiter=",")

#Your Solution
def get_toss_win_count(team = 'Mumbai Indians'):
    a = ipl_matches_array[:,5].astype(np.str) == team
    b = ipl_matches_array[a]
    c = b[:len(a),0:1]
    d = np.unique(c)
    e = len(d)

    return e
