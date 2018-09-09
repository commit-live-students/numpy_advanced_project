# %load q01_get_total_deliveries_players/build.py
# Default imports
import numpy as np

ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')

# Your Solution
def get_total_deliveries_played(batsman):
    var1 = np.count_nonzero(ipl_matches_array[:,-10] == batsman)
    return(var1)
    
    

get_total_deliveries_played(b'ST Jayasuriya')



