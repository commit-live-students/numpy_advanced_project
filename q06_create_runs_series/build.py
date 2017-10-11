# %load q06_create_runs_series/build.py
#Default Imports
from greyatomlib.numpy_advanced.q01_get_total_deliveries_players.build import ipl_matches_array
import pandas as pd

def create_runs_series(match_code):
    df = pd.Series(ipl_matches_array[:,16][ipl_matches_array[:,0] == match_code], index =ipl_matches_array[:,11][ipl_matches_array[:,0] == match_code])
    return df
