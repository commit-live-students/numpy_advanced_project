#Default Imports
import numpy as np

from greyatomlib.numpy_advanced.q01_get_total_deliveries_players.build import ipl_matches_array

#Your Solution
def get_wicket_delivery_numbers_array(player) :
    flt_player = ipl_matches_array[:,13] == player
    flt_wicket = ipl_matches_array[:,20] == player
    deliveries = ipl_matches_array[flt_player & flt_wicket]
    return deliveries[:,11]
