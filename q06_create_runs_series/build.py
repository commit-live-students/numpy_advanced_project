# %load q06_create_runs_series/build.py
#Default Imports
import pandas as pd
import numpy as np
ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', delimiter=',',dtype=str)
match_code = '392203'
# #Your Solution
def create_runs_series(match_code):
    ipl_filter=(ipl_matches_array[:,0]==match_code)
    ipl_matches=ipl_matches_array[ipl_filter]
    matches_index = ipl_matches[:,11] 
    matches_runs = ipl_matches[:,16]
    return pd.Series(data=matches_runs,index=matches_index)
create_runs_series(match_code)
    


