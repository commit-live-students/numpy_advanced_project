# %load q01_get_total_deliveries_players/build.py
# Default imports
import numpy as np

ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')

# Your Solution
batsman=b'SR Tendulkar'


def get_total_deliveries_played(batsman):
    batsman_array=ipl_matches_array[:,13]
    batsman_filter=(batsman_array==batsman)
    total=batsman_array[batsman_filter].size 
    
    return total

get_total_deliveries_played(batsman)




