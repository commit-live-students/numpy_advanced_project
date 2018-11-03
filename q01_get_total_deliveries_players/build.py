# %load q01_get_total_deliveries_players/build.py
# Default imports
import numpy as np

ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')

# Your Solution
def get_total_deliveries_played(batsman) :
    return (ipl_matches_array[:,13].astype('|S50') == batsman).sum()
    

get_total_deliveries_played(b'SR Tendulkar')
ipl_matches_array[:,14].astype('|S50') == 'SR Tendulkar'
xx = b'SR Tendulkar'
xx
ipl_matches_array[:,14]


