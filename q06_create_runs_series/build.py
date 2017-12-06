#Default Imports
from greyatomlib.numpy_advanced.q01_get_total_deliveries_players.build import ipl_matches_array
import pandas as pd

#Your Solution
def create_runs_series(match_code):
    runs_series = pd.Series(ipl_matches_array[ipl_matches_array[:, 0] == match_code][:, -7])
    runs_series.index = ipl_matches_array[ipl_matches_array[:, 0] == match_code][:, 11]
    return runs_series
