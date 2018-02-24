#Default Imports
import numpy as np

ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", skip_header=1, delimiter=",")

#Your Solution
def get_wicket_delivery_numbers_array(player):
    #l = []
    #for row in ipl_matches_array:
    #    if row[-3] == player:
    #        delivery = float(row[-12])
    #       l.append(delivery)

    #all_delivery = np.array(l)
    #return all_delivery

    wicket_delivery = ipl_matches_array[:,[-3,-12]]
    #print newdata
    player_delivery = wicket_delivery[wicket_delivery[:, 0] == player]
    all_delivery = player_delivery[:, 1]
    return all_delivery
    
get_wicket_delivery_numbers_array('ST Jayasuriya')
