# %load q01_get_total_deliveries_players/build.py
# Default imports
import numpy as np

ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header = 1, delimiter=',')

# Your Solution
def get_total_deliveries_played(batsman):
    x = ipl_matches_array[:,13]
    y = (x == b'SR Tendulkar')
    total = len(ipl_matches_array[y])
    return total
get_total_deliveries_played('batsman')




