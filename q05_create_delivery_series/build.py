#Default Imports
import pandas as pd
import numpy as np
ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", skip_header=1, delimiter=",")
from pandas import Series

#Your Solution
def create_delivery_series():
    return Series(ipl_matches_array[:,11])
