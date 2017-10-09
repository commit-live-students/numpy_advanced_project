# %load q05_create_delivery_series/build.py
#Default Imports
import pandas as pd
import numpy as np
#from greyatomlib.numpy_advanced.q01_get_total_deliveries_players.build import ipl_matches_array
path = "./data/ipl_matches_small.csv"
def create_delivery_series():
    ipl_matches_array = np.genfromtxt(path,dtype='|S50',delimiter=',',skip_header=1)
    #match = ipl_matches_array[0:,0]
    values = ipl_matches_array[0:,11]
    return pd.Series(data=values,index=None)
