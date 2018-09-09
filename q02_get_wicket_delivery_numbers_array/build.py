import numpy as np
ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')

def get_wicket_delivery_numbers_array(player_name):
    arr = ipl_matches_array[ipl_matches_array[:,20].astype('|S50') == player_name]
    arr1 = arr[:,11]
    
    return arr1


    




