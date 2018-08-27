# %load q05_create_delivery_series/build.py
#Default Imports
import pandas as pd
import numpy as np
ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')
path = ipl_matches_array
#Your Solution
def create_delivery_series():
    deliveries = pd.Series(path[:, 11])
    print(deliveries)
    return deliveries
create_delivery_series()



