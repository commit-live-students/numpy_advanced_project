# %load q06_create_runs_series/build.py
#Default Imports
import pandas as pd
import numpy as np
ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')

#Your Solution
def create_runs_series(match_code):
    f = ipl_matches_array[:,0].astype(str) == match_code
    matched = ipl_matches_array[f]
    return pd.Series(data = matched[:,16], index = matched[:,11])


create_runs_series('392203')


