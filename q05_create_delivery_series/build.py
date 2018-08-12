#Default Imports
import pandas as pd
import numpy as np
ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", skip_header=1, delimiter=",")

#Your Solution
def create_delivery_series():
    data = ipl_matches_array
    delivery = pd.Series([i[11] for i in data])
    return delivery
#print create_delivery_series()
