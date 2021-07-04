# %load q01_get_total_deliveries_players/build.py
# Default imports
import numpy as np

ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')
def get_total_deliveries_played(batsman):
    bat = ipl_matches_array[:,13]
    runs = []
    for x in ipl_matches_array[1:]:
        if x[13] == batsman:
            runs.append(x[11])
    return len(np.int32(np.float32(runs)))

get_total_deliveries_played(b'SR Tendulkar')
# Your Solution




