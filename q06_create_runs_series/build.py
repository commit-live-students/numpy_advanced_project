# %load q06_create_runs_series/build.py
#Default Imports
import pandas as pd
import numpy as np
ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')
match_code= b'392203'

def create_runs_series(match_code):
    for i in ipl_matches_array[:,0]:
        if i == match_code:
            s1= pd.Series(ipl_matches_array[:,-7],index=ipl_matches_array[:,11])
    return s1

create_runs_series(match_code)




