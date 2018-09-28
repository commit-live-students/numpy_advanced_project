# %load q02_get_wicket_delivery_numbers_array/build.py
#Default Imports
import numpy as np

ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')

#Your Solution
def get_wicket_delivery_numbers_array(player):
    player_out = ipl_matches_array[:,20]
    deliveriers = ipl_matches_array[:,11]
    a = (deliveriers [player_out== player])
    return a
    
    

get_wicket_delivery_numbers_array(b'ST Jayasuriya')


