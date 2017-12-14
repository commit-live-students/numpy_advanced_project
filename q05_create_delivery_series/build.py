#Default Imports
import pandas as pd
from greyatomlib.numpy_advanced.q01_get_total_deliveries_players.build import ipl_matches_array
from pandas import Series

#Your Solution
def create_delivery_series():
    return Series(ipl_matches_array[:, 11])
