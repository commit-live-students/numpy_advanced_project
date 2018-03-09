
#Default Imports
from greyatomlib.numpy_advanced.q01_get_total_deliveries_players.build import ipl_matches_array
import pandas as pd


#Your Solution
def create_runs_series(match_code):
    match = ipl_matches_array[ipl_matches_array[:, 0] == match_code]
    return pd.Series(match[:, 16], index=match[:, 11])

