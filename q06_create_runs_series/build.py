#Default Imports
from greyatomlib.numpy_advanced.q01_get_total_deliveries_players.build import ipl_matches_array
import pandas as pd


#Your Solution
def create_runs_series(match_code):
    match_deliveries = ipl_matches_array[ipl_matches_array[:,0] == match_code]
    print match_deliveries.shape[0]
    return pd.Series (data=match_deliveries[:,16],index = match_deliveries[:,11])

#print create_runs_series('392203')
