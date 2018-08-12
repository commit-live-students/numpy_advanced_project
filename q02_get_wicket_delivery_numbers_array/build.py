import numpy as np

ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", skip_header=1, delimiter=",")

def get_wicket_delivery_numbers_array(player):
    return np.array([elm[11] for elm in ipl_matches_array if elm[13] == player and elm[20] <> ''])
