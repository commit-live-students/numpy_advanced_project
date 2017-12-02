#Default Imports
import pandas as pd
from greyatomlib.numpy_advanced.q01_get_total_deliveries_players.build import ipl_matches_array

#Your Solution
from pandas import Series as Series

def create_delivery_series():
    return  Series( ipl_matches_array[:,11])
