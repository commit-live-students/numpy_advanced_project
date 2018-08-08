# %load q06_create_runs_series/build.py
#Default Imports
import pandas as pd
import numpy as np


#Your Solution
def create_runs_series(match_code):
    ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')
    return pd.Series([x[16] for x in ipl_matches_array if x[0]==match_code],index=[y[11] for y in ipl_matches_array if y[0]==match_code])




