# %load q06_create_runs_series/build.py
#Default Imports
import pandas as pd
import numpy as np
ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')

  
#Your Solution
def create_runs_series(match_code):
    indx=ipl_matches_array[:,11]
    df=pd.DataFrame(ipl_matches_array,index=indx)
    df1=df[[0,16]]
    df2=df1[16][df1[0]==np.bytes_(match_code)]
    return df2

