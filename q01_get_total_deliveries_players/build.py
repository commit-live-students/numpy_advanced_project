# %load q01_get_total_deliveries_players/build.py
# Default imports
import numpy as np

ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')
def get_total_deliveries_played(batsman):
    c = ipl_matches_array[:,13]#.astype(np.str)
    variable = ipl_matches_array[c == batsman].shape[0]
    return variable
     
# Your Solution

get_total_deliveries_played(b'SR Tendulkar')





