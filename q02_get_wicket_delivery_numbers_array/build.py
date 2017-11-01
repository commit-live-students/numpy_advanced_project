#Default Imports
import numpy as np

from greyatomlib.numpy_advanced.q01_get_total_deliveries_players.build import ipl_matches_array

#Your Solution
def get_wicket_delivery_numbers_array(batsman):
    deliveries_played = ipl_matches_array[ipl_matches_array[:,20] == batsman][:,11]
    return deliveries_played

#print get_wicket_delivery_numbers_array ('ST Jayasuriya')
