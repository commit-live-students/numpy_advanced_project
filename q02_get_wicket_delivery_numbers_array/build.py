#Default Imports
import numpy as np

from greyatomlib.numpy_advanced.q01_get_total_deliveries_players.build import ipl_matches_array

#Your Solution
def get_wicket_delivery_numbers_array(player):
    array = ipl_matches_array[:,[11,20]]
    a_grp = array[array[:,1] == player]
    return a_grp[:,0]
