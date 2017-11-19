#Default Imports
from greyatomlib.numpy_advanced.q01_get_total_deliveries_players.build import ipl_matches_array
import pandas as pd


#Your Solution
def create_runs_series(match_code):
    array = ipl_matches_array[ipl_matches_array[:,0] ==match_code]
    #print array
    delvr_index = array[:,11]
    runs_column = array[:,16]
    series = pd.Series(runs_column,index=delvr_index)
    return series
