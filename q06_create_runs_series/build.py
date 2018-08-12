# %load q06_create_runs_series/build.py
#Default Imports
from pandas import Series
import pandas as pd
import numpy as np
ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", skip_header=1, delimiter=",")

#Your Solution
def create_runs_series(match_code):
    match = ipl_matches_array[:,0]==match_code
    indec = ipl_matches_array[:,11]
    run = ipl_matches_array[:,16]
    return pd.Series(run,indec)
