import sys, os
sys.path.append(os.path.join(os.path.dirname(os.curdir),"..", '..'))


import pandas as pd
from q01_get_total_deliveries_players.build import ipl_matches_array

def create_delivery_series():
    return pd.Series(ipl_matches_array[:, 11])