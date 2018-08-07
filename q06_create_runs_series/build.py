# %load q06_create_runs_series/build.py
#Default Imports
import pandas as pd
import numpy as np
ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')

#Your Solution
def create_runs_series(match_code):
    runs_series = pd.Series(ipl_matches_array[:,16][ipl_matches_array[:,0]==match_code], ipl_matches_array[:,11][ipl_matches_array[:,0]==match_code])
    return runs_series
create_runs_series(b'392203')


