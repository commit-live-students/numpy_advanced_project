#Default Imports
from greyatomlib.numpy_advanced.q01_get_total_deliveries_players.build import ipl_matches_array
import pandas as pd
import numpy as np
from pandas import Series


#Your Solution
def create_runs_series(match_code):
    code=ipl_matches_array[:,0]
    delivery=ipl_matches_array[:,11][np.where((code==match_code))]
    runs=ipl_matches_array[:,16][np.where((code==match_code))]
    return Series(runs,delivery)
