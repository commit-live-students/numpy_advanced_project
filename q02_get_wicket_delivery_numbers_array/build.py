# %load q02_get_wicket_delivery_numbers_array/build.py
#Default Imports
import numpy as np

ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')

#Your Solution
player=b'ST Jayasuriya'

def get_wicket_delivery_numbers_array(player):
    delivery_player_out_array=ipl_matches_array[:,[11,20]]
    player_out_filter=(delivery_player_out_array[:,1]==player)
    
    return delivery_player_out_array[player_out_filter][:,0]

get_wicket_delivery_numbers_array(player)



