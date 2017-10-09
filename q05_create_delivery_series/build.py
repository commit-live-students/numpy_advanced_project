#Default Imports
import pandas as pd
from greyatomlib.numpy_advanced.q01_get_total_deliveries_players.build import ipl_matches_array

#Your Solution
def create_delivery_series():
    batsman_ind = ipl_matches_array[:,13]
    delivery_data = ipl_matches_array[:,11]
    delivery_series = pd.Series(delivery_data, batsman_ind)
    return delivery_series
