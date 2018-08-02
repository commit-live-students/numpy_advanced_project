# %load q06_create_runs_series/build.py
#Default Imports
import pandas as pd
import numpy as np
ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')

#Your Solution
def create_runs_series(match_code):
    runs = []
    for x in ipl_matches_array:
        if x [0] == match_code:
            runs.append(x [16])
        return pd.Series(runs, index = [x[11] for x in ipl_matches_array] )       
    






