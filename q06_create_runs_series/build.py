# %load q06_create_runs_series/build.py
#Default Imports
from greyatomlib.numpy_advanced.q01_get_total_deliveries_players.build import ipl_matches_array
import pandas as pd

def create_runs_series(match_code):
    #print(match_code)
    x = ipl_matches_array[ipl_matches_array[:,0] == match_code]
    #print(x)
    values = x[:,-7]
    #print(values)
    index = x[:,-12]
   # print(index)
    series1 = pd.Series(values, index)
    #print(series1)
    return series1

#     values = ipl_matches_array[matchcode,[-7]]
#     print(values)
#create_runs_series('392203')

#Your Solution
