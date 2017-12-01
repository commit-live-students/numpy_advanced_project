#Default Imports
from greyatomlib.numpy_advanced.q01_get_total_deliveries_players.build import ipl_matches_array
import pandas as pd
import numpy as np
def create_runs_series(match_code):
    match = ipl_matches_array[:, 0] == match_code
    arr = ipl_matches_array[:, 16][match]
    idx = ipl_matches_array[:, 11][match]
    return pd.Series(arr, idx)
#Your Solution
#print create_runs_series(392203)
