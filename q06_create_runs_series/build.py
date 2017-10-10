# %load q06_create_runs_series/build.py
#Default Imports
#from greyatomlib.numpy_advanced.q01_get_total_deliveries_players.build import ipl_matches_array
import pandas as pd
import numpy as np
path = "./data/ipl_matches_small.csv"
def create_runs_series(match_code):
    ipl_matches_array = np.genfromtxt(path,dtype='|S50',delimiter=',',skip_header=1)

    match= ipl_matches_array[0:,0] == match_code
#Your Solution
    delivery=ipl_matches_array[match][0:,11]
    runs=ipl_matches_array[match][0:,16]
    return pd.Series(data=runs,index=delivery)
