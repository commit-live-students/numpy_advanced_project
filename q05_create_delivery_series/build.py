#Default Imports
import pandas as pd
from greyatomlib.numpy_advanced.q01_get_total_deliveries_players.build import ipl_matches_array

#Your Solution
def create_delivery_series():
    d_series = pd.Series(ipl_matches_array[:,11])
    return d_series
