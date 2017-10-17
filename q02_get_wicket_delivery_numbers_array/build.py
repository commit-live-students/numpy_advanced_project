#Default Imports
import numpy as np

from greyatomlib.numpy_advanced.q01_get_total_deliveries_players.build import ipl_matches_array

def get_wicket_delivery_numbers_array(batsman):
    data = ipl_matches_array[ipl_matches_array[:,20] == batsman]
    return data[:,11]

get_wicket_delivery_numbers_array('ST Jayasuriya')
