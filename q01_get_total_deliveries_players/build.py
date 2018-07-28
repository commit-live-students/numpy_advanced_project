# %load q01_get_total_deliveries_players/build.py
# Default imports
import numpy as np
import pandas as pd

ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')
batsman = 'SR Tendulkar'
# Your Solution

def get_total_deliveries_played(batsman):
    a=np.array(ipl_matches_array[:, 13]).astype('str')
    #arr_index = (a.astype('str') == batsman)
    #a=np.array(ipl_matches_array[:, 13])
    arr_index = (a==batsman)
    b=a[arr_index]
    #return len(b)




