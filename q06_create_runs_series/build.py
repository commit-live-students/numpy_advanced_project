import pandas as pd
import numpy as np
ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')

def create_runs_series(match_code):
    
    match_arr = ipl_matches_array[ipl_matches_array[:,0].astype('|S50') == match_code]
    runs_series = pd.Series(data = match_arr[:,16], index = match_arr[:,11])
    
    return runs_series


