# %load q06_create_runs_series/build.py
#Default Imports
from greyatomlib.numpy_advanced.q01_get_total_deliveries_players.build import ipl_matches_array
import pandas as pd
import numpy as np
def create_runs_series(match_code):
    fil1=ipl_matches_array[:,0].astype(np.int64)==match_code
    x=pd.Series(ipl_matches_array[:,18],ipl_matches_array[:,11])[fil1]
    return x
#create_runs_series(392203)
