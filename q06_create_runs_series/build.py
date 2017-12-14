# %load q06_create_runs_series/build.py
#Default Imports
from greyatomlib.numpy_advanced.q01_get_total_deliveries_players.build import ipl_matches_array
import pandas as pd
from pandas import Series

def create_runs_series(match_code):
    match = ipl_matches_array[:,0] == match_code
    deliveries = Series(ipl_matches_array[:,11][match])
    runs = Series(ipl_matches_array[:,16][match])
    return Series (runs.values,deliveries)
