# %load q06_create_runs_series/build.py
#Default Imports
import pandas as pd
import numpy as np
ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')

#Your Solution
def create_runs_series(match_code):
    runs_arr = []
    delivery_arr = []
    for i in range(len(ipl_matches_array)):
        if ipl_matches_array[i][0] == match_code:
            runs_arr.append(ipl_matches_array[i, 16])
            delivery_arr.append(ipl_matches_array[i, 11])
            
    return pd.Series(runs_arr, index = delivery_arr)
match_code = b'392203'
expected = None
actual = create_runs_series(match_code)
np.all(expected == actual)





