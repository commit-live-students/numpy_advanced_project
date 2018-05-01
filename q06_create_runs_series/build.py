# %load q06_create_runs_series/build.py
#Default Imports
import pandas as pd
import numpy as np
ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype=np.str, skip_header=1, delimiter=',')

#Your Solution
def create_runs_series(match_code):
    match_filter = ipl_matches_array[ipl_matches_array[:,0] == match_code]
    return(pd.Series(match_filter[:,16], index=match_filter[:,11]))
create_runs_series('392203')



