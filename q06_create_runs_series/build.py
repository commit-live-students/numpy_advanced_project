#Default Imports
from greyatomlib.numpy_advanced.q01_get_total_deliveries_players.build import ipl_matches_array
import pandas as pd


#Your Solution
def create_runs_series(match_code):
    match_filter = ipl_matches_array[:,0] == match_code
    runs = ipl_matches_array[match_filter][:,16]
    deliveries = ipl_matches_array[match_filter][:,11]
    return pd.Series(data=runs, index=deliveries)
