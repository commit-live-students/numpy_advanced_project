# %load q06_create_runs_series/build.py
#Default Imports
import pandas as pd
import numpy as np
ipl_matches_array1 =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')


#Your Solution
def create_runs_series(match_code):
    ipl_matches_array = ipl_matches_array1.astype(np.str)
    data=pd.Series(ipl_matches_array[:,-7],index=ipl_matches_array[:,11])
    return(data[ipl_matches_array[:,0]==match_code])
    



