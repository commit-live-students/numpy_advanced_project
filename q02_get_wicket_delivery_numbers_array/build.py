import numpy as np

ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", skip_header=1, delimiter=",")

def get_wicket_delivery_numbers_array(player):
    a=ipl_matches_array[:,20]
    itemindex = np.where(a==player)
    ilst = list(itemindex)
    return ipl_matches_array[ilst,11]
    
