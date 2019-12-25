# %load q06_create_runs_series/build.py
#Default Imports
import pandas as pd
import numpy as np
ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')

#Your Solution
def create_runs_series(match_code):
    matches=ipl_matches_array[:,0]==match_code
    index=ipl_matches_array[:,11][matches]
    return pd.Series(ipl_matches_array[:,16][matches],index)
create_runs_series( b'392203')
    





