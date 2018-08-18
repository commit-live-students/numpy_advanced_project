# %load q01_get_total_deliveries_players/build.py
# Default imports
import numpy as np

ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')

# Your Solution
def get_total_deliveries_played(batsman = 'batsman'):
    array1 = ipl_matches_array[:,13]
    array2 = array1 == b'SR Tendulkar'
    total_deliveries = len(ipl_matches_array[array2])
    return total_deliveries




