# %load q06_create_runs_series/build.py
#Default Imports
import pandas as pd
import numpy as np
ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')

#Your Solution
def create_runs_series(match_code = '392203'):
    delivery_col = ipl_matches_array[:,11].astype(np.float)
    runs_col = ipl_matches_array[:,16].astype(np.int)
    match_code_col = pd.unique(ipl_matches_array[:,0].astype(np.int))
    runs_delivery = pd.Series(data = runs_col, index=delivery_col)
    return runs_delivery



