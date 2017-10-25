#Default Imports
from greyatomlib.numpy_advanced.q01_get_total_deliveries_players.build import ipl_matches_array
import pandas as pd


#Your Solution
def create_runs_series(match_code):
    arr = ipl_matches_array[ ipl_matches_array[:,0] == match_code, 16 ]
    index = ipl_matches_array[ ipl_matches_array[:,0] == match_code, 11 ]
    return pd.Series(arr, index=index)
