# %load q01_get_total_deliveries_players/build.py
# Default imports
import numpy as np

#ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')
ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='str', skip_header=1, delimiter=',')

# Your Solution
def get_total_deliveries_played(batsman):
    bat_arr = ipl_matches_array[:,13]
    lst = bat_arr.tolist()
    return(lst.count(batsman))
    
get_total_deliveries_played('SR Tendulkar')

