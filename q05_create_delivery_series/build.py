# %load q05_create_delivery_series/build.py
#Default Imports
import pandas as pd
from greyatomlib.numpy_advanced.q01_get_total_deliveries_players.build import ipl_matches_array
def create_delivery_series():
    x = ipl_matches_array[:,-12]
    a = pd.Series(x)
    #print(a)
    return a
#create_delivery_series()
#Your Solution
