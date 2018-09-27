# %load q06_create_runs_series/build.py
#Default Imports
import pandas as pd
import numpy as np
ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')

def create_runs_series(match_code):
    required_match=ipl_matches_array[ipl_matches_array[:,0]==match_code]
    return pd.Series(index=required_match[:,11], data=required_match[:,16])




