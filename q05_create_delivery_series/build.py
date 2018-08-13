#Default Imports
import pandas as pd
from pandas import Series
import numpy as np
ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", skip_header=1, delimiter=",")

#Your Solution
def create_delivery_series():
    deliv = ipl_matches_array[:,11]
    deliv_series = Series(deliv)
    #print type(deliv_series)
    return deliv_series

print create_delivery_series()
