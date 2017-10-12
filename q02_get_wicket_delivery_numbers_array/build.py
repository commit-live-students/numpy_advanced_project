#Default Imports
import numpy as np

from greyatomlib.numpy_advanced.q01_get_total_deliveries_players.build import ipl_matches_array

#Your Solution
def get_wicket_delivery_numbers_array(player):
    wicket_deliveries = ipl_matches_array[:, 20]
    delivery_filter = (wicket_deliveries != '') & (wicket_deliveries == player)
    return ipl_matches_array[delivery_filter][:,11]
