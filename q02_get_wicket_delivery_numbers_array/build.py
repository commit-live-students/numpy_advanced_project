# %load q02_get_wicket_delivery_numbers_array/build.py
#Default Imports
import numpy as np

ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50',skip_header=1, delimiter=',')

player_out=ipl_matches_array[:,20]
def get_wicket_delivery_numbers_array(player_out):
    player_out=(ipl_matches_array[:,20]==player_out)
    deliveries=ipl_matches_array[:,11][player_out]
    return deliveries
    
    
    

get_wicket_delivery_numbers_array(player_out)
  

            
            
        

#Your Solution




