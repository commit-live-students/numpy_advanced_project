#Default Imports
import pandas as pd
from pandas import Series
import numpy as np
ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", skip_header=1, delimiter=",")

#Your Solution
def create_delivery_series():
    delivery_num_col_index = 11
    delivery_array = ipl_matches_array[:,delivery_num_col_index]
    delivery_num_series = Series(data=delivery_array)
    return delivery_num_series
