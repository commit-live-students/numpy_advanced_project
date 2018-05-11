# %load q01_get_total_deliveries_players/build.py
# Default imports
import numpy as np
 

def get_total_deliveries_played(batsman):
    ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='str', skip_header=1, delimiter=',')
    unique, counts = np.unique(ipl_matches_array[:,13], return_counts=True)
    a=dict(zip(unique, counts))
    return(a[batsman])
    
# Your Solution



