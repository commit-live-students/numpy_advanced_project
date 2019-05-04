# %load q02_get_wicket_delivery_numbers_array/build.py
#Default Imports
import numpy as np

player_out=b'ST Jayasuriya'

def get_wicket_delivery_numbers_array(player_out):
    ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=0, delimiter=',')
    player=ipl_matches_array[:,-3]
    indice=np.where(player==player_out)

    for val1 in indice:
        deliveries=ipl_matches_array[val1,11]
            
    return deliveries

get_wicket_delivery_numbers_array(player_out)


