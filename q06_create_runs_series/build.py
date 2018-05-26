# %load q06_create_runs_series/build.py
#Default Imports
import pandas as pd
import numpy as np
ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')

#Your Solution
def create_runs_series(match_code):
    times = ipl_matches_array[ipl_matches_array[:,0].astype(str) == match_code]
    return pd.Series(data = list(times[:,-7]), index = list(times[:,11]))
     


