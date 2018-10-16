# %load q01_get_total_deliveries_players/build.py
# Default imports
import numpy as np

batsman_input= b'SR Tendulkar'

ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=0, delimiter=',')
def get_total_deliveries_played(batsman_input):
    
    batsman=ipl_matches_array[:,13]
    unique_elements, counts_elements = np.unique(batsman==batsman_input, return_counts=True) 
    return counts_elements[1]
    
get_total_deliveries_played(batsman_input)






