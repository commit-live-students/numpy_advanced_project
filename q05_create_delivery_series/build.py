import pandas as pd
import numpy as np
from greyatomlib.numpy_advanced.q01_get_total_deliveries_players.build import ipl_matches_array

#Your Solution
def create_delivery_series():
    ipl_matches_array  = np.genfromtxt('./data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=",")
    return pd.Series(ipl_matches_array[0:,11])
