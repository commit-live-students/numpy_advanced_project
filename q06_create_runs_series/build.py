# %load q06_create_runs_series/build.py
#Default Imports
import pandas as pd
import numpy as np

def create_runs_series(match_code):
    ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')
    delivery_series =pd.Series(ipl_matches_array[:, 16], index = ipl_matches_array[:,11] )
    return delivery_series
#Your Solution
create_runs_series(392203)


