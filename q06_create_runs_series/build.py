# %load q06_create_runs_series/build.py
#Default Imports
import pandas as pd
import numpy as np
ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')

#Your Solution
def create_runs_series(matchCode):
    
    
    ipl_data=ipl_matches_array[int(matchCode)==ipl_matches_array[0:,0].astype('int32')]
    #print(ipl_data)
    
    series=pd.Series(ipl_data[0:,-7],index=ipl_data[0:,11])
    return(series)


