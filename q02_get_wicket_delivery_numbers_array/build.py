#Default Imports
import numpy as np

from greyatomlib.numpy_advanced.q01_get_total_deliveries_players.build import ipl_matches_array

def get_wicket_delivery_numbers_array(player):
    #print(player)
    batsman = ipl_matches_array[ipl_matches_array[:,13]==player]
    #print(batsman)
    #outballs = np.where(batsman[:-3]==player)
    #count = 0
    balls = batsman[:,11][batsman[:,-3]==player]

    #if batsman[:-3]=='ST Jayasuriya':
    return balls
#print(get_wicket_delivery_numbers_array('SC Ganguly'))

#Your Solution
