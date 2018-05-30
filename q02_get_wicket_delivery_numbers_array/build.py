# %load q02_get_wicket_delivery_numbers_array/build.py
#Default Imports
import numpy as np

ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')

#Your Solution
def get_wicket_delivery_numbers_array(player):
    player_out=ipl_matches_array[:,-3]==player
    player_deliveries=ipl_matches_array[:,11].astype(np.float64)
    return player_deliveries[player_out]
    
    

get_wicket_delivery_numbers_array(b'ST Jayasuriya')


