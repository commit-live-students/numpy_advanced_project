#Default Imports
from pandas import Series, DataFrame
import pandas as pd
import numpy as np
from greyatomlib.numpy_advanced.q01_get_total_deliveries_players.build import ipl_matches_array

def create_delivery_series():
    return pd.Series(ipl_matches_array[:,11])
    #expected = pd.Series(ipl_matches_array[:, 11])
    #print expected

print create_delivery_series()
