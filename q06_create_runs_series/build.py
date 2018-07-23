# %load q06_create_runs_series/build.py
#Default Imports
import pandas as pd
import numpy as np
ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype=np.str, skip_header=1, delimiter=',')
#Your Solution

def create_runs_series(a):
    df=pd.Series(ipl_matches_array[:,16][ipl_matches_array[:,0]=='392203'])
    df.index=ipl_matches_array[:,11][ipl_matches_array[:,0]=='392203']
    return df

a='392203'
create_runs_series(a)



