# %load q06_create_runs_series/build.py
#Default Imports
import pandas as pd
import numpy as np
ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')

#Your Solution
def create_runs_series(match_code):
    
    #Assigning a variable to data and index column.
    data = ipl_matches_array[:,16]
    index = ipl_matches_array[:,11]
    
    #Returning the Pandas Series.
    return pd.Series(data,index)

#Call to the function.
create_runs_series(b'392203')








