#Default Imports
import numpy as np

from greyatomlib.numpy_advanced.q01_get_total_deliveries_players.build import ipl_matches_array

#Your Solution
def get_wicket_delivery_numbers_array(player):
    temp = []
    for item in ipl_matches_array:
        if item[20] == player:
            temp.append(item[11])
    return np.array(temp)
