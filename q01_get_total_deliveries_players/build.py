# %load q01_get_total_deliveries_players/build.py
# Default imports
import numpy as np

ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')
# Your Solution
def get_total_deliveries_played(batsman):
    
    Delivery = [x for x in ipl_matches_array if x[13] == batsman ]
    
    played =len(Delivery)
    
    return played




