#Default Imports
import numpy as np

from greyatomlib.numpy_advanced.q01_get_total_deliveries_players.build import ipl_matches_array

#Your Solution
def get_wicket_delivery_numbers_array(playername):
    player_out=ipl_matches_array[:,[11,-3]]
    delivery= player_out[:,0]
    filter1 = (player_out[:,1] == playername)
    return delivery[filter1]

get_wicket_delivery_numbers_array('ST Jayasuriya')
