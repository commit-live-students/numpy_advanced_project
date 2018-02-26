#Default Imports
from pandas import Series
import pandas as pd
import numpy as np
ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", skip_header=1, delimiter=",")

#Your Solution
def create_delivery_series():
    delivery_series=Series(ipl_matches_array[:,11])
    return delivery_series
