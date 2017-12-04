#Default Imports
from greyatomlib.numpy_advanced.q01_get_total_deliveries_players.build import ipl_matches_array
import pandas as pd
from pandas import Series
#Your Solution
def create_runs_series(match_code):
    filtered_array = ipl_matches_array[ipl_matches_array[:,0] == match_code]
    deliveries = filtered_array[:,11]
    all_deliveries = filtered_array[:,16]
    runs_series = Series(data=all_deliveries,index=deliveries)
    return runs_series
