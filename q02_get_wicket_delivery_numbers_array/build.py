
import numpy as np
ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')

def get_wicket_delivery_numbers_array (batsman):
    np.set_printoptions(threshold=np.nan)
    ipl_matches_array[:,20]
    lenth_player_out = len (ipl_matches_array[:,20])
    delivery_out = ipl_matches_array[:,11]
    delivery_out_arr = []
    player_out = ipl_matches_array[:,20]
    for i in range (lenth_player_out):
        if (player_out[i] == batsman):
            #print ('yes')
            delivery_out_arr.append(delivery_out[i])
    return np.array(delivery_out_arr)
get_wicket_delivery_numbers_array(b'ST Jayasuriya')



