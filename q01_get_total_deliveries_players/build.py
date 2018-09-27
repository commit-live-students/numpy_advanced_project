# %load q01_get_total_deliveries_players/build.py
# Default imports
import numpy as np
ipl_matches_array = np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')
def get_total_deliveries_played(batsman):
    tr = ipl_matches_array.shape[0] #total rows in csv file
#print(total_rows)
    count =0
    for i in range(0,tr):
        if ipl_matches_array[i][13] == batsman:
            count = count + 1
    return count







