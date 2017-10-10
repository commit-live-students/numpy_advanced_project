# %load q02_get_wicket_delivery_numbers_array/build.py
#Default Imports
import numpy as np
path = "./data/ipl_matches_small.csv"
from greyatomlib.numpy_advanced.q01_get_total_deliveries_players.build import ipl_matches_array
def get_wicket_delivery_numbers_array(player):
    filter1 = ipl_matches_array[:,20] == player
    out_del = ipl_matches_array[filter1, 11]
    return out_del
