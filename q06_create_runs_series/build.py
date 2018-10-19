# %load q06_create_runs_series/build.py
#Default Imports
import pandas as pd
import numpy as np
ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')
match_code=ipl_matches_array[:,0]
runs=ipl_matches_array[:,16]
deli=ipl_matches_array[:,11]
#Your Solution
def create_runs_series(match_code):
    match_code_bool=ipl_matches_array[:,0]==match_code
    runs=ipl_matches_array[:,16][match_code_bool]
    deli=ipl_matches_array[:,11][match_code_bool]
    series1=pd.Series(data=runs,index=deli)
    return series1

create_runs_series(match_code)



