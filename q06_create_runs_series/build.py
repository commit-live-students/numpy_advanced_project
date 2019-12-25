# %load q06_create_runs_series/build.py
#Default Imports
import pandas as pd
import numpy as np
ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')
#Your Solution
def create_runs_series(match_code='392203'):
    ipl_match = pd.read_csv('data/ipl_matches_small.csv',index_col='delivery')
    match_code_filter = ipl_match['match_code'] == int(match_code)
    runs = ipl_match['runs'][match_code_filter]
    
    return runs
    

create_runs_series('392197')




