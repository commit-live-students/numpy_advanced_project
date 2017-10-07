#Default Imports
from greyatomlib.numpy_advanced.q01_get_total_deliveries_players.build import ipl_matches_array
import pandas as pd

def create_runs_series(match_code):
    data = ipl_matches_array[ipl_matches_array[:,0] == match_code]
    series = pd.Series(data[:,16], \
                       index=data[:,11])
    return series
