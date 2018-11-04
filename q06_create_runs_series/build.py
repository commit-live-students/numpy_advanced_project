# %load q06_create_runs_series/build.py
#Default Imports
from greyatomlib.numpy_advanced.q01_get_total_deliveries_players.build import ipl_matches_array
import pandas as pd


#Your Solution
def create_runs_series(match_code) :
    req_match = ipl_matches_array[ipl_matches_array[:,0].astype('|S50') == match_code]
    return pd.Series(req_match[:,-7], index = req_match[:,-12])
#392203
#ipl_matches_array[ipl_matches_array[:,0].astype('|S50') == match_code]
#len(ipl_matches_array)
create_runs_series(b'392203')


