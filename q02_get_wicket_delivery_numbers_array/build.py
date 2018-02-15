#Default Imports
import numpy as np

ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", skip_header=1, delimiter=",")

player = ''

def get_wicket_delivery_numbers_array(player):
    a = ipl_matches_array

    b= a[:, [-3 , 11]]

    c = b[b[:,0] == player][:,1]

    return c



print get_wicket_delivery_numbers_array(player)
