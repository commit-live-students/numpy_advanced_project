#Default Imports
import numpy as np

ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", skip_header=1, delimiter=",")
def get_wicket_delivery_numbers_array(player):
    player_out_list = ipl_matches_array[:,20]
    player_out_list_filter = player_out_list == player
    return ipl_matches_array[player_out_list_filter][:,11]
#get_wicket_delivery_numbers_array('ST Jayasuriya')
