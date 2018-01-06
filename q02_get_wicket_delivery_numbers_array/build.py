#Default Imports
import numpy as np

ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", skip_header=1, delimiter=",")

#Your Solution

def get_wicket_delivery_numbers_array(player):
    delivery_nos = []
    for i in ipl_matches_array[:,[11,20]]:
         if i[1] == player:
            delivery_nos.append(i[0])

    return delivery_nos
