#Default Imports
import numpy as np

ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", skip_header=1, delimiter=",")


def get_wicket_delivery_numbers_array(player):
    #Access the column player_out and compare it with the given player
    wicket_filter = (ipl_matches_array[:, 20] == player)
    wickets_arr = ipl_matches_array[wicket_filter] #Storing the values in an array
    return wickets_arr[:, 11]#all the delivery numbers where the player got out
