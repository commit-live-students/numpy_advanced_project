#Default Imports
import pandas as pd
import numpy as np
from greyatomlib.numpy_advanced.q01_get_total_deliveries_players.build import ipl_matches_array

def create_delivery_series():
    ipl_match = ipl_matches_array[:,11]
    delivery_series = pd.Series(data = ipl_match)
    return delivery_series
