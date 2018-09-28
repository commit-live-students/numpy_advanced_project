# %load q01_get_total_deliveries_players/build.py
# Default imports
import numpy as np
import pandas as pd

ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')

# Your Solution
def get_total_deliveries_played(batsman):
    a= ipl_matches_array[:,13] 
    b = a==b'SR Tendulkar'
    c = a[b]
    return len(c)
    
        
    
    
    
    
    
    
    



get_total_deliveries_played(b'SR Tendulkar')



