# %load q06_create_runs_series/build.py
#Default Imports
import pandas as pd
import numpy as np
ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')
path = ipl_matches_array
match_code = 392203
#Your Solution
def create_runs_series(match_code):
    deliveries = pd.Series(path[:, -7], index = [path[:, 11]])
    print (deliveries)
    return deliveries
create_runs_series(match_code)



