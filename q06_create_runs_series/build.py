#Default Imports
from greyatomlib.numpy_advanced.q01_get_total_deliveries_players.build import ipl_matches_array
from pandas import Series, DataFrame
import pandas as pd
import numpy as np

def create_runs_series(match_code):
    rows = np.where(ipl_matches_array[:,0] == match_code)
    return pd.Series(ipl_matches_array[rows,16][0],index=(ipl_matches_array[rows,11][0]))

#Your Solution
print create_runs_series(match_code='392203')
