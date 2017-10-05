#Default Imports
import numpy as np

from greyatomlib.numpy_advanced.q01_get_total_deliveries_players.build import ipl_matches_array

#Your Solution
def get_wicket_delivery_numbers_array(player):
    data_filter = (ipl_matches_array[:,-3] == player )
    data = ipl_matches_array[data_filter][:,11]
    return data
