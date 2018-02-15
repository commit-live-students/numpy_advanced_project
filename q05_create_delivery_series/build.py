#Default Imports
import pandas as pd
import numpy as np
ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", skip_header=1, delimiter=",")

#Your Solution
def create_delivery_series():
    deliveries =  ipl_matches_array[:,11]
    delivery_series = pd.Series(deliveries)
    return delivery_series

create_delivery_series()
