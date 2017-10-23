#Default Imports
import numpy as np

from greyatomlib.numpy_advanced.q01_get_total_deliveries_players.build import ipl_matches_array

#Your Solution
def get_wicket_delivery_numbers_array(player):
    return np.array([i[11] for i in ipl_matches_array if i[20] == player ])
