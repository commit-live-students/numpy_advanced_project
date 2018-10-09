# %load q06_create_runs_series/build.py
#Default Imports
import pandas as pd
import numpy as np
ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')

def create_runs_series(match_code):
    runs=ipl_matches_array[:,16]
    delivery=ipl_matches_array[:,11]
    return pd.Series(runs,delivery)
    


create_runs_series(392203)


