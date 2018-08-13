#Default Imports
import numpy as np

ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", skip_header=1, delimiter=",")

#Your Solution
def get_wicket_delivery_numbers_array(player):

    a = ipl_matches_array[:,20]
    b = ipl_matches_array[:,11][a==player]
    return b
