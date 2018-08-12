#Default Imports
import pandas as pd
import numpy as np
ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", skip_header=1, delimiter=",")
from pandas import Series

#Your Solution
def create_runs_series(match_code):
    filtered_array = ipl_matches_array[ipl_matches_array[:,0] == match_code]
    sliced_deliveries = filtered_array[:,11]
    sliced_all_deliveries = filtered_array[:,16]
    runs_series = Series(data=sliced_all_deliveries,index=sliced_deliveries)
    return runs_series
