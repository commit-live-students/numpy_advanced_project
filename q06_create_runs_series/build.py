# %load q06_create_runs_series/build.py
#Default Imports
import pandas as pd
import numpy as np
ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')
ipl_matches_array
#Your Solution
def create_runs_series(match_code):
    array1=ipl_matches_array[ipl_matches_array[:,0].astype(str)=='392203']
    p1=np.array(array1[:,11])
    p2=np.array(array1[:,16])
    pseries3=pd.Series(data=p2,index=p1)
    return pseries3


