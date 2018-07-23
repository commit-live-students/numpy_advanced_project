# %load q06_create_runs_series/build.py
#Default Imports
import pandas as pd
import numpy as np
ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')

#Your Solution
def create_runs_series(match_code):
    filt=ipl_matches_array[:,0].astype(str)==match_code
    selection=pd.Series(ipl_matches_array[:,-7],ipl_matches_array[:,-12])
    return selection[filt]
    


