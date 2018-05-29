# %load q01_get_total_deliveries_players/build.py
# Default imports
import numpy as np
import pandas as pd
ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')
#ip_matches_array=pd.read_csv('data/ipl_matches_small.csv')

# Your Solution

def get_total_deliveries_played(batsman):
    batsman=bytes(batsman, 'utf-8')
    data=pd.DataFrame(ipl_matches_array)
    d1=data[13]
    return(np.sum(d1==batsman))
    



