# %load q06_create_runs_series/build.py
#Default Imports
from greyatomlib.numpy_advanced.q01_get_total_deliveries_players.build import ipl_matches_array
import pandas as pd


#Your Solution
def create_runs_series(match_code):
    filter=(ipl_matches_array[:,0]==match_code)
    matches=ipl_matches_array[:,[11,16]]
    res=matches[filter]
    return pd.Series(data=res[:,1], index=res[:,0])
