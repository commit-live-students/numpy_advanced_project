#Default Imports
import numpy as np

from greyatomlib.numpy_advanced.q01_get_total_deliveries_players.build import ipl_matches_array

#Your Solution
def get_wicket_delivery_numbers_array(player):
    player_out = ipl_matches_array[ipl_matches_array[:,20] == player]
    return player_out[:,11]
