#Default Imports
from greyatomlib.numpy_advanced.q01_get_total_deliveries_players.build import ipl_matches_array
import pandas as pd

def create_runs_series(match_code):
    index = ipl_matches_array[:,11]
    runs = ipl_matches_array[:,16]
    series = pd.Series(data = runs,index=index)
    return series

create_runs_series(392203)
