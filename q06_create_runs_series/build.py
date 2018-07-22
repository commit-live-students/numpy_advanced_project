# %load q06_create_runs_series/build.py
#Default Imports
import pandas as pd
import numpy as np
ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', skip_header=1, delimiter=',')

#Your Solution
def create_runs_series(match_code):
    
    ipl_matches_array1 = ipl_matches_array[ipl_matches_array[:,0]==392203]
    data_pd = pd.Series(ipl_matches_array1[:,-7].astype('int32'), index=ipl_matches_array1[:,11])
    return data_pd



create_runs_series(392203)


