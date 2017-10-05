#Default Imports
from greyatomlib.numpy_advanced.q01_get_total_deliveries_players.build import ipl_matches_array
import pandas as pd


#Your Solution
def create_runs_series(match_code):
    data_f = ipl_matches_array[:,0] == match_code
    data = ipl_matches_array[data_f]
    index = data[: , 11]
    runs = data[: , -7]
    run_series = pd.Series(runs,index)
    return run_series
