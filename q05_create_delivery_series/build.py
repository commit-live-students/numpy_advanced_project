#Default Imports
import pandas as pd
import numpy as np
from greyatomlib.numpy_advanced.q01_get_total_deliveries_players.build import ipl_matches_array

#Your Solution
def create_delivery_series():
    delivery_series = pd.Series(ipl_matches_array[:,11])
    return delivery_series
