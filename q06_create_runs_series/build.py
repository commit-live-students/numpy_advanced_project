# %load q06_create_runs_series/build.py
#Default Imports
import pandas as pd
import numpy as np
ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')

#Your Solution
def create_runs_series(match_code):
    x=np.where(ipl_matches_array[:,0]==match_code)
    z= ipl_matches_array[x]
    return pd.Series(z[:,16],index=z[:,11])
create_runs_series(b'392203')    


