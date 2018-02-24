#Default Imports
import pandas as pd
import numpy as np
ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", skip_header=1, delimiter=",")

#Your Solution
from pandas import Series
def create_delivery_series():
    delivery= ipl_matches_array[:,11]
    del_ser = Series(delivery)
    return  (del_ser)
