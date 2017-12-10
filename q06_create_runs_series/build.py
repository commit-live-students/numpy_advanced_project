#Default Imports
from greyatomlib.numpy_advanced.q01_get_total_deliveries_players.build import ipl_matches_array
import pandas as pd

def create_runs_series(match_code):
    match_details = ipl_matches_array[ipl_matches_array[:,0]==match_code]
    delv_series = pd.Series(match_details[:,16], index=match_details[:,11])
    return delv_series
