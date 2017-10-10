#Default Imports
from greyatomlib.numpy_advanced.q01_get_total_deliveries_players.build import ipl_matches_array
import pandas as pd


#Your Solution
def create_runs_series(match_code):
    runs=ipl_matches_array[:,16]
    delivery=ipl_matches_array[:,11]
    return pd.Series(data=runs,index=delivery)

create_runs_series('392203')
