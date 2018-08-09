# %load q06_create_runs_series/build.py
#Default Imports
import pandas as pd
import numpy as np
ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')
ipldf=pd.read_csv('data/ipl_matches_small.csv',dtype='|S50')
#Your Solution

def create_runs_series(match_code):
    dseries = ipldf.loc[ipldf['match_code'] == match_code]
    dseries = ipldf[['runs','delivery']]
    variable = dseries.set_index('delivery')
    return variable.runs


    
    





