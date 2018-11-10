# %load q06_create_runs_series/build.py
#Default Imports
import pandas as pd
import numpy as np
ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')

#Your Solution
def create_runs_series(match_code):
        
    match_data =  ipl_matches_array[ipl_matches_array[:,0] == match_code] 
    delivery = pd.Series(match_data[:,11])
    runs_series = pd.Series(match_data[:,16], index = delivery)
    
    return runs_series

match_code= b'392203'
create_runs_series(match_code)



