# %load q02_get_wicket_delivery_numbers_array/build.py
#Default Imports
import numpy as np

from greyatomlib.numpy_advanced.q01_get_total_deliveries_players.build import ipl_matches_array
#ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", skip_header=1, delimiter=",")
def get_wicket_delivery_numbers_array(player):

    playerFilter = (ipl_matches_array[:,-3] == player)

    final = ipl_matches_array[:,-12]

    finaldeliveries = final[playerFilter]
    return finaldeliveries
