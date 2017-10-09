# %load q01_get_total_deliveries_players/build.py
# Default imports
import numpy as np
import pandas as pd
ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", skip_header=1, delimiter=",")

# Your Solution
def get_total_deliveries_played(batsman):
    ipl_series_batsman=pd.Series(ipl_matches_array[:,13])
    fil1=(ipl_series_batsman==batsman)
    #print(fil1)
    match_batsman=ipl_series_batsman[fil1]
    #print(match_batsman)
    #print(ipl_matches_array[0,:])
    deliveries=len(match_batsman)
    return deliveries


#ret=get_total_deliveries_played("SR Tendulkar")
#print(ret)
