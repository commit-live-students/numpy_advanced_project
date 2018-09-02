# %load q01_get_total_deliveries_players/build.py
# Default imports
import numpy as np

ipl_matches_array = np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')

# Your Solution
def get_total_deliveries_played(batsman):
    total_rows = ipl_matches_array.shape[0]
    count =0
    for i in range(0,total_rows):
        if ipl_matches_array[i][13] == batsman:#.encode(encoding='UTF-8'):
            count = count + 1
    return count
#get_total_deliveries_played(b'ST Jayasuriya')
#

#my_ipl_matches_array


