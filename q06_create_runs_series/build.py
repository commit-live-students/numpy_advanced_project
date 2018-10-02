# %load q06_create_runs_series/build.py
#Default Imports
import pandas as pd
import numpy as np
ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')

#Your Solution
def create_runs_series(match_code):
    blt = ipl_matches_array[(ipl_matches_array[:,0] == match_code)]
    return pd.Series(blt[:,11],index=blt[:,16])
    
create_runs_series(b'392203')


