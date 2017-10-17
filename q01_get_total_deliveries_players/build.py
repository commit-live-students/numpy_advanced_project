# %load q01_get_total_deliveries_players/build.py
# Default imports
import numpy as np
import pandas as pd

ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", skip_header=1, delimiter=",")

# Your Solution
def get_total_deliveries_played(batsman):
    index =ipl_matches_array[:,11].astype(np.float16)
    #print(index)
    values=ipl_matches_array[:,13].astype(np.str)

    delivery_batsman=pd.Series(values,index)
    #print(delivery_batsman)

    filter_batsman =delivery_batsman.values==batsman
    #in_batsman=0
    delivery_faced= len(delivery_batsman[filter_batsman])
    return delivery_faced


#get_total_deliveries_played('SR Tendulkar')
