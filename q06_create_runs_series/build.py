#Default Imports
from greyatomlib.numpy_advanced.q01_get_total_deliveries_players.build import ipl_matches_array
import pandas as pd


#Your Solution
import numpy as np
def create_runs_series(match):
    ipl_filtered = ipl_matches_array[ipl_matches_array[:,0].astype(np.int64) == 392203]
    ser = pd.Series(data=ipl_filtered[:,16], index=ipl_filtered[:,11])
    return ser
#print create_runs_series(392203)
