#Default Imports
import numpy as np

from greyatomlib.numpy_advanced.q01_get_total_deliveries_players.build import ipl_matches_array

#Your Solution

def get_wicket_delivery_numbers_array(player):
    delivery = np.array([])
    #np.array(delivery)
    #print type(delivery)
    player_out_deliveries = ipl_matches_array[:,[11,20]]
    #print player_out_deliveries[:30]
    for item in player_out_deliveries:
        if item[1] == player:
            #print item[1]
            #print item[0]
            delivery = np.append(delivery, item[0])
            #print delivery
            #print type(delivery)
    return delivery
