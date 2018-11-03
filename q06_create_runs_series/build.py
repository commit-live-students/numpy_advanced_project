# %load q06_create_runs_series/build.py
#Default Imports
import pandas as pd
import numpy as np
ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')

#Your Solution
def create_runs_series(code):
    x= ipl_matches_array[:,11]
    y= ipl_matches_array[:,16]
    s=pd.Series(y,index=x)
    return s

x= ipl_matches_array[:,11]
x
y= ipl_matches_array[:,16]
y
s=pd.Series(y,index=x)
s


