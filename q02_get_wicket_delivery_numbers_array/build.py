# %load q02_get_wicket_delivery_numbers_array/build.py
#Default Imports
import numpy as np

ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype=np.str, skip_header=1, delimiter=',')

#Your Solution

def get_wicket_delivery_numbers_array(player):
    ipl_player = ipl_matches_array[ipl_matches_array[:,20]== player]
    ipl_deliveries_out = ipl_player[:,11]
    return ipl_deliveries_out
get_wicket_delivery_numbers_array('ST Jayasuriya')    


