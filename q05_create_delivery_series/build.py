#Default Imports
import numpy as np
import pandas as pd
from pandas import Series
from greyatomlib.numpy_advanced.q01_get_total_deliveries_players.build import ipl_matches_array

ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", skip_header=1, delimiter=",")

#Your Solution
def create_delivery_series():
    a = ipl_matches_array[:,11]
    series = pd.Series(a)
    return series
