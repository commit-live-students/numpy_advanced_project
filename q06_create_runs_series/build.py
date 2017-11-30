#Default Imports
from greyatomlib.numpy_advanced.q01_get_total_deliveries_players.build import ipl_matches_array
import pandas as pd
import numpy as np

#Your Solution
def create_runs_series(match_code):
    code=ipl_matches_array[:,0]
    delivery=ipl_matches_array[np.where((code==match_code))][:,11]
    runs=ipl_matches_array[np.where((code==match_code))][:,16]
    series=pd.Series(runs,delivery)
    return series
