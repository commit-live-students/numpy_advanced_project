#Default Imports
from greyatomlib.numpy_advanced.q01_get_total_deliveries_players.build import ipl_matches_array
import pandas as pd


#Your Solution
def create_runs_series(match_code):
    flt_match = ipl_matches_array[:,0] == match_code
    match_data = ipl_matches_array[flt_match]
    #print match_data
    del_ind = match_data[:,11]
    runs_data = match_data[:,16]
    runs_series = pd.Series(runs_data,del_ind)
    return runs_series
