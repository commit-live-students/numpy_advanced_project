# %load q02_get_wicket_delivery_numbers_array/build.py
#Default Imports
import numpy as np

ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')

#Your Solution
def get_wicket_delivery_numbers_array(player):
    
    player_name = ipl_matches_array.astype(str)
    return ipl_matches_array[player_name[:,-3] == player][:,-12].astype(str)
        
     
    
    
get_wicket_delivery_numbers_array('ST Jayasuriya')



