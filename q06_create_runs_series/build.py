# %load q06_create_runs_series/build.py
#Default Imports
import pandas as pd
import numpy as np
ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')

#Your Solution
def create_runs_series(match_code):
    matchCodeBool = ipl_matches_array[:,0].astype(str) == match_code
    delIndex = ipl_matches_array[:,11][matchCodeBool]
    runVal = ipl_matches_array[:,16][matchCodeBool]
    
    runs = pd.Series(runVal,index = delIndex)
    return runs

create_runs_series('392203')


