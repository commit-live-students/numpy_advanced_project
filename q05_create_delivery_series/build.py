# %load q05_create_delivery_series/build.py
#Default Imports
import pandas as pd
import numpy as np
from pandas import Series
ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", skip_header=1, delimiter=",")

#Your Solution
def create_delivery_series():
    deliveries = []
    for i in ipl_matches_array:
        deliveries.append(i[11])
    actual = Series(deliveries)
    return actual

actual = create_delivery_series()
