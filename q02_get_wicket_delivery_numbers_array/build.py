# %load q02_get_wicket_delivery_numbers_array/build.py
#Default Imports
import numpy as np


#Your Solution
def get_wicket_delivery_numbers_array(player=''):
    ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')
    player_out= ipl_matches_array[:,20].astype(np.str)
    deliveries= ipl_matches_array[:,11].astype(np.str)
    return (deliveries[player_out == player])
    
    
    
    



