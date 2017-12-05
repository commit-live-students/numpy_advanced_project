#Default Imports
from pandas import Series, DataFrame
import pandas as pd
import numpy as np
from greyatomlib.numpy_advanced.q01_get_total_deliveries_players.build import ipl_matches_array

#Your Solution

def get_wicket_delivery_numbers_array(player):
    rows = np.where(ipl_matches_array[:,20] == player)
    return ipl_matches_array[rows,11][0]


print get_wicket_delivery_numbers_array(player='ST Jayasuriya')
