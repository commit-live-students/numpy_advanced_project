#Default Imports
from greyatomlib.numpy_advanced.q01_get_total_deliveries_players.build import ipl_matches_array
import pandas as pd
import numpy as np

ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", skip_header=1, delimiter=",")

def create_runs_series (match_code):
    filter1 = ipl_matches_array[:,0] == match_code
    index_col = ipl_matches_array[:,11]
    match_index = index_col[filter1]
    data_col = ipl_matches_array[:,16]
    match_data = data_col[filter1]
    run_series = pd.Series (data = match_data, index = match_index )
    return run_series

#Your Solution
