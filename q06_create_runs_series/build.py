# %load q06_create_runs_series/build.py
#Default Imports
import pandas as pd
import numpy as np
ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')

def create_runs_series(match_code):
    filter_set = ipl_matches_array[ipl_matches_array[:,0] == match_code]
    delivery = filter_set[:,11]
    runs = filter_set[:,16]
    variable = pd.Series(runs, index = delivery)
    return variable
#Your Solution

create_runs_series(b'392203')




