# %load q06_create_runs_series/build.py
#Default Imports
import pandas as pd
import numpy as np
ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')

#Your Solution
def create_runs_series(match_code):
    m = ipl_matches_array[ipl_matches_array [:,0]==match_code]
    ind = m[:,11]
    runs = pd.Series(m[:,16],index=ind)
    return runs



