# %load q05_create_delivery_series/build.py
#Default Imports
import pandas as pd
import numpy as np
ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv',dtype= str, skip_header=1, delimiter=',')
batsman = 'ST Jayasuriya'
 #Your Solution
def create_delivery_series(batsman):
    delivery_filter = (ipl_matches_array[:,13] == batsman)
    delivery_series = ipl_matches_array[delivery_filter]
    delivery_series = pd.Series(delivery_series[:,11])
    return delivery_series[:,11]
create_delivery_series(batsman)
    

