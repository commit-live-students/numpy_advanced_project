# %load q06_create_runs_series/build.py
#Default Imports
import pandas as pd
import numpy as np
ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')

#Your Solution
def create_runs_series(match_code):
    delv = np.array([x[11] for x in ipl_matches_array if x[0] == match_code ] )
    run = np.array([x[16] for x in ipl_matches_array if x[0] == match_code ] )
    ser = pd.Series(run, index=delv)
    return ser

    




