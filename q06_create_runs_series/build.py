#Default Imports
import numpy as np
import pandas as pd
from pandas import Series

from greyatomlib.numpy_advanced.q01_get_total_deliveries_players.build import ipl_matches_array
ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", skip_header=1, delimiter=",")

#Your Solution
def create_runs_series(match_code, dtype = 'str'):
    filtered_matches = ipl_matches_array[ipl_matches_array[:,0] == match_code]
    runs_scored = filtered_matches[:,16]
    match_delivery = filtered_matches[:,11]
    runs_series = pd.Series(data = runs_scored, index= match_delivery)

    return runs_series
