# %load q02_get_wicket_delivery_numbers_array/build.py
#Default Imports
import numpy as np
import pandas as pd
from pandas import DataFrame

ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", skip_header=1, delimiter=",")


# Your Solution
def get_wicket_delivery_numbers_array(batsman):
    deliveries = np.array([])
    total = 0
    for i in ipl_matches_array:
        if batsman==i[20]:
            deliveries.resize(total + 1)
            deliveries[total] = (i[11])
            total = total + 1
    return deliveries.astype(str)


deliveries = get_wicket_delivery_numbers_array('ST Jayasuriya')
