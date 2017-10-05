#Default Imports
import numpy as np

from greyatomlib.numpy_advanced.q01_get_total_deliveries_players.build import ipl_matches_array

def get_wicket_delivery_numbers_array(batsman):
    return ipl_matches_array[:,11][(ipl_matches_array[:,13] == batsman) & (ipl_matches_array[:,-3]!= batsman)]
#Your Solution
