#Default Imports
from greyatomlib.numpy_advanced.q01_get_total_deliveries_players.build import ipl_matches_array
import pandas as pd


#Your Solution
def create_runs_series(match_code):
    temp_delivery = []
    temp_runs = []
    for item in ipl_matches_array:
            if item[0] == match_code:
                temp_delivery.append(item[11])
                temp_runs.append(item[16])
    return pd.Series(data=temp_runs,index=temp_delivery)
