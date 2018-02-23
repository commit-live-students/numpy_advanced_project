#Default Imports
import numpy as np

ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", skip_header=1, delimiter=",")

#Your Solution
player = 'ST Jayasurya '

def get_wicket_delivery_numbers_array(player):
    wicket = ipl_matches_array[:,20] == player
    wicket_deliveries = ipl_matches_array[wicket]
    return wicket_deliveries[:,11]

get_wicket_delivery_numbers_array(player)
