# %load q06_create_runs_series/build.py
#Default Imports
import pandas as pd
import numpy as np
ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')

#Your Solution
def create_runs_series(match_no):
    #print(match_no, type(match_no))
    m=ipl_matches_array[:,(0)]
    #print(m, type(m[0]))
    m=(ipl_matches_array[:,(0)]==match_no)
    match_arr=ipl_matches_array[m]
    #print(match_arr)
    
    s=pd.Series(data=match_arr[:,16].astype(np.int), index=match_arr[:,11].astype(np.float16))
    return(s)

    
create_runs_series(b'392203')



