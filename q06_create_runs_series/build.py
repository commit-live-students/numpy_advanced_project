#Default Imports
from greyatomlib.numpy_advanced.q01_get_total_deliveries_players.build import ipl_matches_array
import pandas as pd


#Your Solution
def create_runs_series(code):
    runs=[item[16] for item in ipl_matches_array if item[0] == code]
    delivery=[item[11] for item in ipl_matches_array if item[0] == code]
    return pd.Series(runs,index=delivery)
