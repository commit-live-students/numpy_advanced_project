# %load q02_get_wicket_delivery_numbers_array/build.py
#Default Imports
import numpy as np
import pandas as pd

from greyatomlib.numpy_advanced.q01_get_total_deliveries_players.build import ipl_matches_array

def get_wicket_delivery_numbers_array(player):
    deliveries = ipl_matches_array[:,11:12]
    return deliveries[ipl_matches_array[:,20:21] == player]
