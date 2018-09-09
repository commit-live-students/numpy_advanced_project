# %load q06_create_runs_series/build.py
#Default Imports
import pandas as pd
import numpy as np
ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')

#Your Solution
def create_runs_series(match_code):
    array = ipl_matches_array[np.where(ipl_matches_array[:,0] == match_code)]
    return pd.Series(array[:,[16]].flatten(),index =array[:,[11]].flatten())

match_code = b'392203'
ipl_matches_array = ipl_matches_array[np.where(ipl_matches_array[:,0] == match_code)]
ipl_matches_array[:,[16]]
ipl_matches_array.shape
ipl_matches_array[np.where(ipl_matches_array[:,0] == b'392203')]
ipl_matches_array.shape


