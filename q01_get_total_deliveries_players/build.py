# %load q01_get_total_deliveries_players/build.py
# Default imports
import numpy as np

ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')

# Your Solution
def get_total_deliveries_played(batsman):
    
    count = 0
    for i in range(len(ipl_matches_array)):
        if ipl_matches_array[i][13] == batsman:
            count = count + 1
    return count
get_total_deliveries_played(b'SR Tendulkar')


