#Default Imports
from greyatomlib.numpy_advanced.q01_get_total_deliveries_players.build import ipl_matches_array
import pandas as pd
import numpy as np


#Your Solution
def create_runs_series(match_code):
    series_input= ipl_matches_array[ipl_matches_array[:,0]==match_code]
    return pd.Series(series_input[:,16],index=series_input[:,11])
