# %load q02_get_wicket_delivery_numbers_array/build.py
#Default Imports
import numpy as np

ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')

#Your Solution
def get_wicket_delivery_numbers_array(player):
    
    player_out = ipl_matches_array[:,20] # extracting column player_out
 
    #extracting delivery column
    deliveries = ipl_matches_array[:, 11] 
    
    return (deliveries[player_out == player]) # returning 


player_name = b'ST Jayasuriya'
get_wicket_delivery_numbers_array(player_name)


