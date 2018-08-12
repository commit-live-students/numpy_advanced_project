#Default Imports
import numpy as np

ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", skip_header=1, delimiter=",")
print ipl_matches_array[:,19]
#Your Solution
def get_wicket_delivery_numbers_array(player):
    out = ipl_matches_array[:,11][ipl_matches_array[:,20] == player]
    return out

get_wicket_delivery_numbers_array('ST Jayasuriya')
