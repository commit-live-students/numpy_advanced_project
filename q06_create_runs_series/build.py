# %load q06_create_runs_series/build.py
#Default Imports
import pandas as pd
import numpy as np
ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')
ipl_matches_array = ipl_matches_array.astype(np.str) 
#Your Solution
def create_runs_series(match_code):
    runs_series = pd.Series(ipl_matches_array[ipl_matches_array[:, 0] == match_code][:, -7])
    return runs_series

create_runs_series('392203')

