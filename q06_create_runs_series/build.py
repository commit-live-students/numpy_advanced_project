# %load q06_create_runs_series/build.py
#Default Imports
import pandas as pd
import numpy as np
ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')

#Your Solution
def create_runs_series(match_code):
    matched_array = ipl_matches_array[(ipl_matches_array[:,0] == np.array(match_code,dtype='S'))]
    delivery = matched_array[:,11]
    runs = matched_array[:,16]
    return (pd.Series(runs,index=delivery))


