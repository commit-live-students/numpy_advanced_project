# %load q05_create_delivery_series/build.py
#Default Imports
import pandas as pd
from greyatomlib.numpy_advanced.q01_get_total_deliveries_players.build import ipl_matches_array

#Your Solution
def create_delivery_series():
    hi=ipl_matches_array[:,11]
    #print(len(ipl_matches_array[:,11]))
    series=pd.Series(hi)
    return series
#create_delivery_series()
