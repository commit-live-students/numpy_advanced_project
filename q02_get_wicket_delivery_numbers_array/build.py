#Default Imports
import numpy as np

from greyatomlib.numpy_advanced.q01_get_total_deliveries_players.build import ipl_matches_array

ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", skip_header=1, delimiter=",")

#Your Solution
def get_wicket_delivery_numbers_array(batsman = 'ST Jayasuriya'):
    a = ipl_matches_array[0:,[11,20]]
#     c = ipl_matches_array[:,11].astype(np.float64)
    b = ipl_matches_array[:,20].astype(np.str) == batsman
    c = a[b]
    player_out = c[0:,0]

    return player_out
