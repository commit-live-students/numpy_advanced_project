#Default Imports
import numpy as np

ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", skip_header=1, delimiter=",")

def get_wicket_delivery_numbers_array(player):

    player_out_deliveries = ipl_matches_array[:,[20,11]]
    deliveries = np.array([])

    for ele in player_out_deliveries:

        player_out, delivery = ele
        if player_out == player:
            deliveries = np.append(deliveries,delivery)

    return deliveries
